#!/usr/bin/env python3
"""Monte Carlo balance runs for the Footprint paper prototype.

Plays the paper kit's Corrigan Freight contract (docs/prototype/paper-prototype.html)
thousands of times with scripted play styles, under the v0.1 and v0.2 rules and
candidate tweaks, and reports win rates and how contracts are lost.

This is a throwaway balance tool for the paper kit. The real game's simulation is
the C# library in src/Sim.

Usage:
    python tools/paper_prototype_sim.py                 # 10,000 games per style and ruleset
    python tools/paper_prototype_sim.py --games 2000 --seed 7
"""
from __future__ import annotations

import argparse
import random
from dataclasses import dataclass, field

PARTS = ("Morning", "Afternoon", "Evening", "Late", "Night", "Dawn")  # turn 1 is Day 1 Morning
SUN = {"Morning", "Afternoon"}
MOON = {"Late", "Night", "Dawn"}
LAST_TURN = 16
KEYS = ("foothold", "admin", "route", "mfa")
LAPTOP_PLACES = {"Desk", "Cafe"}


def part_of_day(turn: int) -> str:
    return PARTS[(turn - 1) % 6]


@dataclass(frozen=True)
class Rules:
    name: str
    alert_decay: int = 2        # Alert drop in a turn with no Noise (v0.1: 1)
    new_gear: bool = True       # v0.2 gear: Lookalike domain, Caller-ID spoofer, Hi-vis vest
    exfil_fail_noise: int = 4
    wipe_alert_drop: int = 0    # candidate tweak: Wipe Logs also lowers Alert on success
    watch_building: int = 0     # candidate tweak: uses of a silent Body operation for +1 Intel (0 = off)


@dataclass(frozen=True)
class Op:
    name: str
    slot: str                   # "laptop" or "body"
    turns: int
    chance: int                 # percent
    grants: str | None = None   # key earned ("foothold", "admin", "route", "mfa") or "win"
    cost: int = 0
    time: str | None = None     # "sun" (business hours), "moon" (night) or None
    places: tuple = ()          # body operations: where you must be
    needs_keys: tuple = ()
    needs_revealed: tuple = ()
    noise: tuple = (0, 0)       # (on success, on failure)
    trail: tuple = (0, 0)
    heat: tuple = (0, 0)
    recon: bool = False


OPS = {op.name: op for op in (
    Op("OSINT Sweep", "laptop", 1, 100, recon=True),
    Op("Perimeter Scan", "laptop", 1, 90, recon=True, noise=(1, 1), trail=(1, 1)),
    Op("Wardrive the Block", "body", 1, 90, places=("Cafe", "HQ"), recon=True),
    Op("Stake Out the Lobby", "body", 2, 80, time="sun", places=("HQ",), recon=True, heat=(0, 1)),
    Op("Dumpster Dive", "body", 1, 60, time="moon", places=("HQ",), recon=True, heat=(0, 2)),
    Op("Spear-Phish", "laptop", 2, 40, "foothold", time="sun", needs_revealed=("employees",),
       noise=(1, 2), trail=(1, 1)),
    Op("Exploit the VPN", "laptop", 1, 30, "foothold", cost=300, needs_revealed=("vpn",),
       noise=(1, 3), trail=(1, 1)),
    Op("Helpdesk Pretext Call", "laptop", 1, 30, "foothold", time="sun", needs_revealed=("employees",),
       noise=(0, 2), heat=(0, 1)),
    Op("Evil-Twin Wi-Fi", "body", 2, 50, "foothold", time="sun", places=("Cafe",), needs_revealed=("wifi",),
       noise=(0, 1)),
    Op("Tailgate and Plant", "body", 1, 40, "foothold", time="sun", places=("HQ",), needs_revealed=("lobby",),
       noise=(0, 3), heat=(0, 2)),
    Op("Buy Access", "laptop", 1, 100, "foothold", cost=1500),
    Op("Crack Password Hashes", "laptop", 3, 70, "admin", needs_keys=("foothold",), noise=(1, 1), trail=(1, 1)),
    Op("Abuse a Misconfiguration", "laptop", 1, 30, "admin", needs_keys=("foothold",), noise=(1, 3), trail=(1, 1)),
    Op("Pivot to Billing", "laptop", 2, 60, "route", needs_keys=("admin",), noise=(2, 3), trail=(1, 1)),
    Op("Server Room After Hours", "body", 1, 50, "route", time="moon", places=("HQ",), needs_revealed=("lobby",),
       noise=(0, 2), heat=(0, 3)),
    Op("MFA Push Fatigue", "laptop", 1, 50, "mfa", time="sun", needs_keys=("admin",), noise=(1, 2)),
    Op("Steal Session Token", "laptop", 2, 40, "mfa", needs_keys=("foothold",), noise=(1, 2), trail=(1, 1)),
    Op("Exfiltrate the Ledger", "laptop", 2, 80, "win", needs_keys=KEYS, noise=(0, 4), trail=(0, 2)),
    Op("Bug Bounty", "laptop", 3, 70),
    Op("Sell Scraped Data", "laptop", 1, 90, needs_keys=("foothold",), noise=(1, 1), trail=(1, 1), heat=(1, 1)),
    Op("Wipe Logs", "laptop", 1, 80, needs_keys=("foothold",), noise=(0, 1)),
    # Candidate for v0.3, only with Rules.watch_building: sit at the Café or near HQ and watch staff come and go.
    Op("Watch the Building", "body", 1, 100, places=("Cafe", "HQ")),
)}

GEAR = {
    "Lookalike domain": 200, "Caller-ID spoofer": 250, "Hi-vis vest": 150, "Rogue AP kit": 400,
    "Network implant": 500, "Badge cloner": 300, "Lock picks": 150, "Known exploit": 400,
    "GPU rig": 600, "Burner laptop": 700, "Proxy chain": 300, "Lawyer": 800,
}
NEW_GEAR = {"Lookalike domain", "Caller-ID spoofer", "Hi-vis vest"}


@dataclass
class State:
    turn: int = 1
    loc: str = "Desk"
    cash: int = 1000
    intel: int = 0
    alert: int = 0
    heat: int = 0
    trail: int = 0
    keys: set = field(default_factory=set)        # the four keys, plus "implant"
    revealed: set = field(default_factory=set)    # employees, vpn, wifi, lobby
    gear: set = field(default_factory=set)
    recon_done: set = field(default_factory=set)
    helpdesk_bonus: bool = False
    vpn_patched: bool = False
    reset_done: bool = False
    lawyer_used: bool = False
    sell_count: int = 0
    watches: int = 0
    running: list = field(default_factory=list)   # [op, turns_left]
    traveling_to: str | None = None
    alert_at_run: int = 0
    noise_this_turn: bool = False
    # statistics
    idle_laptop: int = 0
    idle_body: int = 0
    hunts_lost: int = 0
    max_alert: int = 0
    trace: list | None = None       # turn-by-turn notes when tracing

    def note(self, text: str) -> None:
        if self.trace is not None:
            self.trace.append(f"T{self.turn:>2} {part_of_day(self.turn):<9} {text}")


# --- rules helpers ------------------------------------------------------------------------------

def laptop_slots(s: State) -> int:
    return 3 if "Burner laptop" in s.gear else 2


def body_busy(s: State) -> bool:
    return s.traveling_to is not None or any(op.slot == "body" for op, _ in s.running)


def free_laptop_slots(s: State) -> int:
    return laptop_slots(s) - sum(1 for op, _ in s.running if op.slot == "laptop")


def gear_needed(op: Op, s: State, rules: Rules) -> str | None:
    """The gear an operation still needs, or None if nothing is missing."""
    if op.name == "Spear-Phish" and rules.new_gear and "Lookalike domain" not in s.gear:
        return "Lookalike domain"
    if op.name == "Evil-Twin Wi-Fi" and "Rogue AP kit" not in s.gear:
        return "Rogue AP kit"
    if op.name == "Tailgate and Plant" and "Network implant" not in s.gear:
        return "Network implant"
    if op.name == "Server Room After Hours" and not ({"Badge cloner", "Lock picks"} & s.gear):
        return "Lock picks"
    return None


def op_cost(op: Op, rules: Rules) -> int:
    if op.name == "Spear-Phish" and not rules.new_gear:
        return 200      # v0.1: paid per attempt instead of a reusable domain
    return op.cost


def fail_noise(op: Op, rules: Rules) -> int:
    return rules.exfil_fail_noise if op.grants == "win" else op.noise[1]


def requirements_met(op: Op, s: State, rules: Rules, part: str) -> bool:
    """Everything except slot, location and gear."""
    if op.time == "sun" and part not in SUN:
        return False
    if op.time == "moon" and part not in MOON:
        return False
    if any(k not in s.keys for k in op.needs_keys):
        return False
    if any(r not in s.revealed for r in op.needs_revealed):
        return False
    if op.name == "Exploit the VPN" and s.vpn_patched:
        return False
    if op.name == "Abuse a Misconfiguration" and s.intel < 2:
        return False
    if op.name == "Sell Scraped Data" and s.sell_count >= 2:
        return False
    if op.recon and op.name in s.recon_done:
        return False
    return s.cash >= op_cost(op, rules)


def bonus(op: Op, s: State) -> int:
    g, n = s.gear, op.name
    if n == "Exploit the VPN":
        return 20 if "Known exploit" in g else 0
    if n == "Helpdesk Pretext Call":
        return 20 if "Caller-ID spoofer" in g else 0
    if n == "Stake Out the Lobby":
        return 20 if "Hi-vis vest" in g else 0
    if n == "Tailgate and Plant":
        return 20 * ("Badge cloner" in g) + 20 * ("Hi-vis vest" in g)
    if n == "Server Room After Hours":
        return 20 if {"Badge cloner", "Lock picks"} <= g else 0
    if n == "MFA Push Fatigue":
        return 10 * ("Caller-ID spoofer" in g) + 10 * s.helpdesk_bonus
    if n == "Steal Session Token":
        return 20 if "implant" in s.keys else 0
    return 0


def alert_penalty(alert: int) -> int:
    if alert >= 9:
        return 20
    if alert >= 3:
        return 10
    return 0


def lose_keys(s: State, lost: set) -> None:
    """Remove keys and cancel running operations that need them (rulings 7 and 10)."""
    s.keys -= lost
    s.running = [e for e in s.running if not (set(e[0].needs_keys) & lost)]


def check_raid(s: State) -> str | None:
    if s.heat < 10:
        return None
    if "Lawyer" in s.gear and not s.lawyer_used:
        s.lawyer_used = True
        s.heat = 6
        s.gear = {"Lawyer"}     # lose all other gear
        return None
    return "raid"


# --- resolving operations -----------------------------------------------------------------------

def resolve(op: Op, s: State, rules: Rules, rng: random.Random, intel_spent: int) -> str | None:
    chance = op.chance + bonus(op, s) + 10 * intel_spent
    if op.slot == "laptop":
        chance -= alert_penalty(s.alert_at_run)
    s.intel -= intel_spent
    roll = rng.randint(1, 10)
    ok = roll * 10 <= chance
    s.note(f"  {op.name}: {'OK  ' if ok else 'FAIL'} roll {roll} vs {chance}% ({intel_spent} Intel)")
    if op.name == "Tailgate and Plant":
        s.gear.discard("Network implant")     # used up either way

    if ok:
        if op.grants == "win":
            return "win"
        apply_success(op, s, rules)
    i = 0 if ok else 1
    noise = fail_noise(op, rules) if not ok else op.noise[0]
    if noise:
        s.alert += noise
        s.noise_this_turn = True
    s.trail += op.trail[i]
    s.heat += op.heat[i]
    s.max_alert = max(s.max_alert, s.alert)
    if s.alert >= 12:
        return "lockdown"
    return check_raid(s)


def apply_success(op: Op, s: State, rules: Rules) -> None:
    n = op.name
    if op.recon:
        s.recon_done.add(n)
        gains = {"OSINT Sweep": (2, "employees"), "Perimeter Scan": (1, "vpn"), "Wardrive the Block": (1, "wifi"),
                 "Stake Out the Lobby": (1, "lobby"), "Dumpster Dive": (3, None)}
        intel, reveal = gains[n]
        s.intel = min(10, s.intel + intel)
        if reveal:
            s.revealed.add(reveal)
    if op.grants in KEYS:
        s.keys.add(op.grants)
    if n == "Tailgate and Plant":
        s.keys.add("implant")
    if n == "Helpdesk Pretext Call":
        s.helpdesk_bonus = True
    if n == "Bug Bounty":
        s.cash += 600
    if n == "Sell Scraped Data":
        s.cash += 800
    if n == "Wipe Logs":
        s.trail = max(0, s.trail - 3)
        s.alert = max(0, s.alert - rules.wipe_alert_drop)
    if n == "Watch the Building":
        s.intel = min(10, s.intel + 1)
        s.watches += 1


def defenders(s: State, rules: Rules, rng: random.Random) -> str | None:
    a = s.alert
    if a >= 9 and not s.reset_done:
        s.reset_done = True
        s.vpn_patched = True
        lose_keys(s, {"admin", "mfa"})
    if a >= 6:
        s.heat += max(0, s.trail // 3 - (1 if "Proxy chain" in s.gear else 0))
        result = check_raid(s)
        if result:
            return result
        if "foothold" in s.keys and s.trail >= 2:
            if rng.randint(1, 10) <= (5 if a >= 9 else 3):
                s.hunts_lost += 1
                if "implant" in s.keys:
                    s.keys.discard("implant")
                else:
                    lose_keys(s, {"foothold"})
    if not s.noise_this_turn:
        s.alert = max(0, s.alert - rules.alert_decay)
    return None


def run_order(entry) -> int:
    op = entry[0]
    if op.recon:
        return 0        # Intel first, so later rolls can spend it
    if op.grants == "win":
        return 1        # before anything noisy can cause a lockdown
    if op.name == "Wipe Logs":
        return 3        # last, so it also removes this turn's Trail
    return 2


# --- play styles --------------------------------------------------------------------------------

@dataclass(frozen=True)
class Style:
    name: str
    describe: str
    routes: dict                    # key -> operations to try, in order
    buy_first: tuple = ()           # gear bought on turn 1 if affordable
    on_demand_gear: tuple = ()      # gear bought when the next operation needs it
    noise_cap: int = 6              # don't start an operation whose failure could push Alert this high
    exfil_max_alert: int = 2        # start Exfiltrate only at or below this Alert, unless out of time
    wipe_at: tuple = (2, 3)         # Wipe Logs when Trail >= a and Alert >= b
    buy_gpu: bool = True
    bug_bounty: bool = True         # put Bug Bounty in an idle Laptop slot early
    dumpster: bool = True
    perimeter: bool = False
    not_before: dict = field(default_factory=dict)   # operation -> earliest turn
    backups_need_pressure: bool = False   # use a route's later operations only when time is short


STYLES = (
    Style("Quiet social", "Caller-ID spoofer, Helpdesk call, Crack, Pivot, MFA Push; lies low before key rolls",
          routes={"foothold": ["Helpdesk Pretext Call"], "admin": ["Crack Password Hashes"],
                  "route": ["Pivot to Billing"], "mfa": ["MFA Push Fatigue", "Steal Session Token"]},
          buy_first=("Caller-ID spoofer",), backups_need_pressure=True),
    Style("Balanced", "No gear up front; phone or email in, Abuse or Crack, MFA Push; moderate risk (like session 1)",
          routes={"foothold": ["Helpdesk Pretext Call", "Spear-Phish"],
                  "admin": ["Abuse a Misconfiguration", "Crack Password Hashes"],
                  "route": ["Pivot to Billing"], "mfa": ["MFA Push Fatigue", "Steal Session Token"]},
          on_demand_gear=("Lookalike domain",), noise_cap=9, exfil_max_alert=5, bug_bounty=False, perimeter=True),
    Style("Fast digital", "Known exploit, VPN, Abuse or Crack, Steal Session Token; ignores Alert until Lockdown",
          routes={"foothold": ["Exploit the VPN", "Helpdesk Pretext Call"],
                  "admin": ["Abuse a Misconfiguration", "Crack Password Hashes"],
                  "route": ["Pivot to Billing"], "mfa": ["Steal Session Token", "MFA Push Fatigue"]},
          buy_first=("Known exploit",), noise_cap=12, exfil_max_alert=11, wipe_at=(99, 99),
          bug_bounty=False, dumpster=False, perimeter=True),
    Style("Physical", "Hi-vis vest, implant and lock picks; tailgate in, server room for the Route",
          routes={"foothold": ["Tailgate and Plant", "Helpdesk Pretext Call"], "admin": ["Crack Password Hashes"],
                  "route": ["Server Room After Hours", "Pivot to Billing"],
                  "mfa": ["Steal Session Token", "MFA Push Fatigue"]},
          buy_first=("Hi-vis vest", "Network implant", "Lock picks"), buy_gpu=False, backups_need_pressure=True),
    Style("Buy access", "Bug Bounty to afford Buy Access ($1,500); phone call only if the money doesn't come",
          routes={"foothold": ["Buy Access", "Helpdesk Pretext Call"], "admin": ["Crack Password Hashes"],
                  "route": ["Pivot to Billing"], "mfa": ["MFA Push Fatigue", "Steal Session Token"]},
          buy_gpu=False, not_before={"Helpdesk Pretext Call": 7}),
)


def buy(s: State, item: str, rules: Rules) -> bool:
    if item in s.gear or (item in NEW_GEAR and not rules.new_gear) or s.cash < GEAR[item]:
        return False
    s.cash -= GEAR[item]
    s.gear.add(item)
    return True


def take_turn(style: Style, s: State, rules: Rules, part: str) -> None:
    """Shop, move and start operations for one turn."""
    # Keys don't stack: cancel anything still working on a key already held.
    s.running = [e for e in s.running if not (e[0].grants in KEYS and e[0].grants in s.keys)]
    if s.turn == 1:
        for item in style.buy_first:
            buy(s, item, rules)

    missing = [k for k in KEYS if k not in s.keys]
    turns_left = LAST_TURN - s.turn + 1
    pressure = turns_left <= 2 + 2 * len(missing)
    cap = 12 if pressure else style.noise_cap
    pending = sum(fail_noise(op, rules) for op, _ in s.running)
    working_on = {op.grants for op, _ in s.running}

    def noise_ok(op: Op) -> bool:
        if op.grants == "win":
            return True     # Exfiltrate's timing is governed by exfil_max_alert and the deadline
        return fail_noise(op, rules) == 0 or s.alert + pending + fail_noise(op, rules) < cap

    def startable(op: Op) -> bool:
        if s.turn < style.not_before.get(op.name, 0):
            return False
        if any(running.name == op.name for running, _ in s.running):
            return False    # one copy of an operation at a time (v0.2 doesn't limit Bug Bounty)
        if not requirements_met(op, s, rules, part):
            return False
        need = gear_needed(op, s, rules)
        if need and not (need in style.on_demand_gear and s.cash >= GEAR[need]):
            return False
        return True

    def start(op: Op) -> None:
        need = gear_needed(op, s, rules)
        if need:
            buy(s, need, rules)
        if op.name == "Crack Password Hashes" and style.buy_gpu:
            buy(s, "GPU rig", rules)
        turns = op.turns
        if op.name == "Crack Password Hashes" and "GPU rig" in s.gear:
            turns = 2
        s.cash -= op_cost(op, rules)
        if op.name == "Sell Scraped Data":
            s.sell_count += 1
        s.running.append([op, turns])
        working_on.add(op.grants)
        s.note(f"start {op.name} ({s.loc})")

    # What the style wants from each slot, best first.
    laptop_wants, body_wants = [], []
    if not missing and (s.alert <= style.exfil_max_alert or turns_left <= 4):
        if "win" not in working_on:
            laptop_wants.append(OPS["Exfiltrate the Ledger"])
    for key in missing:
        if key in working_on:
            continue
        for index, name in enumerate(style.routes[key]):
            if index > 0 and style.backups_need_pressure and not pressure:
                break
            op = OPS[name]
            if startable(op) and noise_ok(op):
                (laptop_wants if op.slot == "laptop" else body_wants).append(op)
                break
    if "foothold" in s.keys and s.trail >= style.wipe_at[0] and s.alert >= style.wipe_at[1]:
        laptop_wants.append(OPS["Wipe Logs"])
    laptop_wants.append(OPS["OSINT Sweep"])
    if style.perimeter:
        laptop_wants.append(OPS["Perimeter Scan"])
    if style.bug_bounty and s.turn <= 6:
        laptop_wants.append(OPS["Bug Bounty"])
    needs_lobby = any(n in ("Tailgate and Plant", "Server Room After Hours") for r in style.routes.values() for n in r)
    if needs_lobby or "Hi-vis vest" in s.gear:
        body_wants.append(OPS["Stake Out the Lobby"])
    body_wants.append(OPS["Wardrive the Block"])
    if style.dumpster and s.heat <= 5:
        body_wants.append(OPS["Dumpster Dive"])
    if s.watches < rules.watch_building:
        body_wants.append(OPS["Watch the Building"])

    laptop_wants = [op for op in laptop_wants if op.slot == "laptop" and startable(op) and noise_ok(op)]
    body_wants = [op for op in body_wants if op.slot == "body" and startable(op) and noise_ok(op)]
    # Recon and keys before income: Bug Bounty only fills a slot nothing else wants.
    laptop_wants = list(dict.fromkeys(laptop_wants))

    start_loc = s.loc
    pinned = body_busy(s)

    # Movement and the Body slot.
    if not pinned:
        if s.loc == "Desk":
            s.traveling_to = "Cafe"            # Laptop work can still start from the Desk this turn
        elif s.loc == "HQ" and laptop_wants and free_laptop_slots(s) > 0:
            s.loc = "Cafe"                    # walk back so Laptop work can start
            body_wants = [op for op in body_wants if "Cafe" in op.places]
        elif body_wants:
            s.loc = "HQ" if "HQ" in body_wants[0].places and "Cafe" not in body_wants[0].places else s.loc
        elif s.loc == "HQ":
            s.loc = "Cafe"

    # Laptop slots: from where you started or where you walked to.
    can_laptop = start_loc in LAPTOP_PLACES or s.loc in LAPTOP_PLACES
    if can_laptop:
        for op in laptop_wants:
            if free_laptop_slots(s) <= 0:
                break
            if startable(op) and op.grants not in (working_on - {None}) and noise_ok(op):
                start(op)
                pending += fail_noise(op, rules)
    s.idle_laptop += free_laptop_slots(s)

    # Body slot: at the place you are after moving.
    if not body_busy(s):
        for op in body_wants:
            if s.loc in op.places and startable(op) and op.grants not in (working_on - {None}):
                start(op)
                break
    if not body_busy(s):
        s.idle_body += 1


def intel_to_spend(op: Op, s: State) -> int:
    if op.grants in KEYS or op.grants == "win":
        return min(3, s.intel)
    return 0


# --- one contract -------------------------------------------------------------------------------

def play(style: Style, rules: Rules, rng: random.Random, s: State | None = None) -> tuple[str, State]:
    s = s or State()
    while True:
        part = part_of_day(s.turn)
        take_turn(style, s, rules, part)

        s.alert_at_run = s.alert
        s.noise_this_turn = False
        for entry in s.running:
            entry[1] -= 1
        finished = sorted((e for e in s.running if e[1] <= 0), key=run_order)
        s.running = [e for e in s.running if e[1] > 0]
        for op, _ in finished:
            if op.grants in KEYS and op.grants in s.keys:
                spend = 0
            else:
                spend = intel_to_spend(op, s)
            result = resolve(op, s, rules, rng, spend)
            if result:
                return result, s
        if s.traveling_to:
            s.loc, s.traveling_to = s.traveling_to, None

        result = defenders(s, rules, rng)
        s.note(f"end: ${s.cash} Intel {s.intel} Alert {s.alert} Heat {s.heat} Trail {s.trail} "
               f"at {s.loc} keys {sorted(s.keys)} gear {sorted(s.gear)}")
        if result:
            return result, s
        s.turn += 1
        if s.turn > LAST_TURN:
            return "timeout", s


# --- reporting ----------------------------------------------------------------------------------

RULESETS = (
    Rules("v0.1", alert_decay=1, new_gear=False),
    Rules("v0.2 gear only (Alert drop 1)", alert_decay=1),
    Rules("v0.2"),
    Rules("v0.2 + Exfiltrate failure Noise 2", exfil_fail_noise=2),
    Rules("v0.2 + Wipe Logs lowers Alert by 1", wipe_alert_drop=1),
    Rules("v0.2 + Watch the Building, unlimited (Body, any time, +1 Intel)", watch_building=99),
    Rules("v0.2 + Watch the Building, 3 uses", watch_building=3),
)


def run(games: int, seed: int) -> None:
    for rules in RULESETS:
        print(f"\n## {rules.name}\n")
        print("| Style | Win | Lockdown | Raid | Time out | Avg win turn | Reset | Avg Heat | Idle Laptop | Idle Body |")
        print("|---|---|---|---|---|---|---|---|---|---|")
        total_wins = 0
        for style in STYLES:
            rng = random.Random(f"{seed}-{rules.name}-{style.name}")
            results = {"win": 0, "lockdown": 0, "raid": 0, "timeout": 0}
            win_turns, resets, heat, idle_l, idle_b = 0, 0, 0, 0, 0
            for _ in range(games):
                result, s = play(style, rules, rng)
                results[result] += 1
                if result == "win":
                    win_turns += s.turn
                resets += s.reset_done
                heat += s.heat
                idle_l += s.idle_laptop
                idle_b += s.idle_body
            total_wins += results["win"]
            pct = {k: f"{100 * v / games:.0f}%" for k, v in results.items()}
            avg_turn = f"{win_turns / results['win']:.1f}" if results["win"] else "—"
            print(f"| {style.name} | **{pct['win']}** | {pct['lockdown']} | {pct['raid']} | {pct['timeout']} | "
                  f"{avg_turn} | {100 * resets / games:.0f}% | {heat / games:.1f} | "
                  f"{idle_l / games:.1f} | {idle_b / games:.1f} |")
        print(f"\nAverage win rate across styles: {100 * total_wins / (games * len(STYLES)):.0f}%")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--games", type=int, default=10_000, help="contracts per style and ruleset")
    parser.add_argument("--seed", type=int, default=1, help="random seed, for repeatable runs")
    parser.add_argument("--trace", metavar="STYLE", help="print a few v0.2 games of one style turn by turn")
    args = parser.parse_args()
    if args.trace:
        style = next(st for st in STYLES if st.name.lower() == args.trace.lower())
        rng = random.Random(args.seed)
        for game in range(3):
            s = State(trace=[])
            # play() creates its own State, so replay the loop here with tracing on.
            result, s = play(style, Rules("v0.2"), rng, s)
            print(f"\n--- {style.name}, game {game + 1}: {result} ---")
            print("\n".join(s.trace))
        return
    print(f"Footprint paper prototype: {args.games:,} contracts per style and ruleset, seed {args.seed}")
    print("\nStyles:")
    for style in STYLES:
        print(f"- **{style.name}:** {style.describe}")
    run(args.games, args.seed)


if __name__ == "__main__":
    main()
