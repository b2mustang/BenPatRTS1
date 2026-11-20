# Paper prototype playtest log

Kit: [`paper-prototype.html`](paper-prototype.html). Session 1 used version 0.1; the kit is now version 0.2 (changes at the end of this file). Played in chat: the player decides, Claude runs the rules and rolls a d10 with a shell random number.

## Rulings made during play

Gaps in the v0.1 rules, decided at the table. Fold them into v0.2.

1. **When operations resolve.** An operation counts down in the same block it starts, so a 1-block operation resolves at the end of that block and a 2-block one at the end of the next.
2. **Needs are checked at start.** Location and time-of-day needs apply when an operation starts. Running Laptop operations keep running wherever you go.
3. **Where you are when you start** (revised in block 5). Laptop operations can start from where you are either before or after the free Café–HQ walk this block. Body operations check where you are after moving. A Travel block ends with you at the destination. The first version (Laptop location fixed at the start of the block) made returning from HQ cost a block of Laptop starts, a hidden trap that contradicts "moving between them is free".
4. **Alert modifiers apply at the roll**, using the Alert level at the start of that block's Run step.
5. **Recon pays once.** A recon card gives its Intel and reveal only the first time it succeeds. Otherwise OSINT Sweep (100%, silent) is a free, unlimited Intel source.
6. **Intel is declared before the roll.** When several operations resolve in the same block, the player picks the order, so Intel gained from one can be spent on the next.
7. **Keys don't stack.** Succeeding at an operation for a key you already hold gives nothing, though Noise and Trail still apply. During "Start operations" you may cancel a running operation: no refund, no Noise, and its slot frees up.
8. **A running Body operation keeps you at its location** (added in block 9). You can't walk away until it resolves, so you can't start Laptop operations from HQ while staking out the lobby. Claude first offered a walk to the Café mid-stakeout, then corrected it before rolling.
9. **A successful Exfiltrate ends the contract at once.** Its Noise can't trigger a Lockdown.
10. **Losing a key cancels running operations that need it** (proposed after session 2; used by the simulation). v0.2 only says this for the Foothold after a Hunt, not for Admin credentials and MFA bypass after a credential reset.
11. **One Bug Bounty at a time** (proposed after the simulation; used by it). v0.2 sets no limit, so a player could run it in both Laptop slots and repeat it for $600 every 12 hours.

## Session 1: Corrigan Freight (solo)

Start: D1 Morning, at the Desk. Cash $1,000. Intel 0, Heat 0, Alert 0, Trail 0. Known: Website, Staff email.

| Block | Shop and move | Started | Resolved (roll) | After: Cash · Intel · Alert · Heat · Trail · Keys |
|---|---|---|---|---|
| 1 · D1 Morning · Desk | Travel to Café | OSINT Sweep, Perimeter Scan | OSINT ✓ (100%). Perimeter Scan ✓ (8 vs ≤9): Employees, VPN gateway revealed | $1,000 · 3 · 1 · 0 · 1 · none |
| 2 · D1 Afternoon · Café | none | Spear-Phish ($200), Helpdesk Pretext Call, Wardrive the Block | Wardrive ✓ (7 vs ≤9): Guest Wi-Fi revealed. Helpdesk ✓ with 2 Intel (2 vs ≤5): **Foothold**, +10% on MFA Push Fatigue. No noise, so Alert −1 | $800 · 2 · 0 · 0 · 1 · Foothold |
| 3 · D1 Evening · Café | none (Body idle: no Evening body ops) | Cancelled Spear-Phish ($200 lost). Abuse a Misconfiguration with 2 Intel | Abuse ✓ (5 vs ≤5): **Admin credentials** | $800 · 0 · 1 · 0 · 2 · Foothold, Admin |
| 4 · D1 Late ☾ · Café → HQ | Move to HQ (free) | Pivot to Billing, Wipe Logs (from Café). Dumpster Dive (at HQ) | Wipe Logs ✓ (7 vs ≤8): Trail 2 → 0. Dumpster Dive ✗ (7 vs ≤6): Heat +2. No noise, so Alert −1 | $800 · 0 · 0 · 2 · 0 · Foothold, Admin |
| 5 · D2 Night ☾ · HQ | Stay at HQ (walk back next block) | Dumpster Dive (retry after a failure) | Pivot to Billing ✗ (8 vs ≤6): Noise 3, Trail +1. Dumpster Dive ✓ (3 vs ≤6): +3 Intel | $800 · 3 · 3 · 2 · 1 · Foothold, Admin |
| 6 · D2 Dawn ☾ · HQ → Café | Walk to Café | Pivot to Billing (retry, 3 Intel declared), Wipe Logs | Wipe Logs ✓ at 70% with Elevated −10% (7 vs ≤7): Trail 1 → 0. No noise, so Alert −1 | $800 · 3 (held for Pivot) · 2 · 2 · 0 · Foothold, Admin |
| 7 · D2 Morning ☀ · Café | none | MFA Push Fatigue | Pivot to Billing ✓ at 90% with 3 Intel (7 vs ≤9): **Route**. MFA Push Fatigue ✓ at 60% with the Helpdesk bonus (2 vs ≤6): **MFA bypass**. Noise 3 | $800 · 0 · 5 · 2 · 1 · all four keys |
| 8 · D2 Afternoon ☀ · Café → HQ | Walk to HQ (after starting Laptop ops) | Exfiltrate the Ledger, Stake Out the Lobby | Nothing resolves. No noise, so Alert −1 | $800 · 0 · 4 · 2 · 1 · all four keys |
| 9 · D2 Evening · HQ | none (Wipe Logs not allowed: the stakeout keeps you at HQ) | none | Stake Out ✓ (1 vs ≤8): +1 Intel, Lobby revealed. **Exfiltrate ✗** at 80% (70% Elevated + 1 Intel; 10 vs ≤8): Noise 4, Trail +2. Defenders at Alert 8: Trace +1 Heat (Trail 3), Hunt survived (4 vs 1–3) | $800 · 0 · 8 · 3 · 3 · all four keys |
| 10 · D2 Late ☾ · HQ → Café | Walk to Café | Wipe Logs (chosen after Claude corrected that its failure makes Noise 1) | Wipe Logs ✗ at 70% (8 vs ≤7): Noise 1, so **Alert 9, Incident response**: credentials reset (**lose Admin and MFA bypass**), VPN patched. Trace +1 Heat. Hunt survived (7 vs 1–5) | $800 · 0 · 9 · 4 · 3 · Foothold, Route |
| 11 · D3 Night ☾ · Café | Bought GPU rig ($600) | Crack Password Hashes (2 blocks with GPU rig), Steal Session Token | Nothing resolves. Defenders at Alert 9: Trace +1 Heat, Hunt survived (10 vs 1–5). No noise, so Alert −1 | $200 · 0 · 8 · 5 · 3 · Foothold, Route |
| 12 · D3 Dawn ☾ · Café | none (chose not to cancel Steal Session Token) | none | Crack ✓ at 60% (1 vs ≤6): **Admin credentials**. Steal Session Token ✗ at 30% (5 vs ≤3). Noise 3, so Alert 11. Trace +1 Heat (Trail 5). Hunt survived (6 vs 1–5) | $200 · 0 · 11 · 6 · 5 · Foothold, Admin, Route |
| 13 · D3 Morning ☀ · Café | none | none: lie low (any noise would have meant Lockdown) | Trace +1 Heat. Hunt survived (7 vs 1–5). No noise, so Alert −1 | $200 · 0 · 10 · 7 · 5 · Foothold, Admin, Route |
| 14 · D3 Afternoon ☀ · Café | none | MFA Push Fatigue (the only way left to finish in time) | MFA Push Fatigue ✗ at 40% (8 vs ≤4): Noise 2, so **Alert 12, Lockdown. Contract failed.** | $200 · 0 · 12 · 7 · 5 · Foothold, Admin, Route |

### Result

| # | Result | Blocks used | Cash left | Heat | Alert | Keys: how you got each | Notes |
|---|---|---|---|---|---|---|---|
| 1 | **Lost: Lockdown** | 14 of 16 | $200 | 7 | 12 | Foothold: Helpdesk Pretext Call (2 Intel). Admin: Abuse a Misconfiguration (2 Intel); lost to the credential reset, regained with Crack Password Hashes (GPU rig). Route: Pivot to Billing (second try, 3 Intel). MFA bypass: MFA Push Fatigue; lost to the reset, retry failed | All four keys by block 7, then one failed Exfiltrate (20%) started a spiral |

### What the game master saw

1. **A fast start, then one roll decided it.** Intel-boosted rolls of 50–90% won all four keys by block 7 of 16, so the deadline never pressured the early game. Then a single failed Exfiltrate (a 20% chance) added Noise 4, a third of the Alert track, and the run never recovered.
2. **Alert ratchets up much faster than it falls.** Operations add 1–4 Noise; a silent block removes only 1. At Alert 6+, lying low costs Heat (Trace) and risks the Foothold (Hunt) every block, so waiting is punished exactly when it's the only safe play. From Alert 9 on, every action was one noise away from Lockdown, and the last four blocks had at most one real decision each.
3. **Recovery depended on luck.** After the credential reset, winning needed 5 Hunt survivals in a row (about 10% combined), then two more successful rolls.
4. **The Body slot sat idle in 8 of 14 blocks** (3, 6, 7 and 10–14). Physical operations disappear in the Evening and once recon is done.
5. **Money barely mattered.** Spent $200 on a Spear-Phish that was cancelled and $600 on the GPU rig. Never sold data or bought access; no other shop items.
6. **Never played:** Exploit the VPN, Evil-Twin Wi-Fi, Tailgate and Plant, Buy Access, Server Room After Hours, Bug Bounty, Sell Scraped Data. **Played most:** Wipe Logs (3 times).
7. **Intel was the strongest resource.** 7 Intel from recon turned 30–60% rolls into 50–90% ones. Without ruling 5, OSINT Sweep would give unlimited Intel.
8. **The rules were easy to misread, even for the game master.** Claude described Wipe Logs as silent (it makes Noise 1 when it fails) and missed that it removes only up to 3 Trail. The digital version must show the success and failure outcomes (Noise, Trail, Heat) of every operation before the player commits.

### Player's answers

1. **Real decisions?** Yes, they felt like real decisions, but some context was missing. Give the player background on what each action technically is.
2. **Blocks with nothing useful to start?** Couldn't say: the blocks weren't clear enough to judge.
3. **Parallel operations?** Understood only later in the game, but they'll be useful.
4. **Did Alert and Heat change how you played?** Definitely.
5. **Physical operations?** Used them, and they were easier to understand than the digital ones.
6. **Cards never or always played?** From the log: never played Exploit the VPN, Evil-Twin Wi-Fi, Tailgate and Plant, Buy Access, Server Room After Hours, Bug Bounty, Sell Scraped Data; Spear-Phish was started and cancelled. Played most: Wipe Logs (3 times).
7. **Did money matter?** Yes, but less than expected. Money should matter in preparation: buying an item before an action and planning around using it.
8. **The ending?** Tense.
9. **Anything else?** The blocks weren't clear. Play should be framed as parts of a day, so the player understands when an action is best to run.

### Tuning candidates after session 1

Change one thing at a time. A was chosen for v0.2.

- **A. Alert falls by 2, not 1, in a block with no Noise.** Makes lying low a real recovery tool. (Claude's first pick: the spiral decided this session.)
- **B. Exfiltrate failure Noise 4 → 2.** Softens the single roll that decided the game.
- **C. Wipe Logs also lowers Alert by 1 on success.** Gives a tool for climbing down from high Alert.
- **D. Give the Body slot work in the Evening and after recon**, for example a repeatable "Watch the building" for +1 Intel.
- **E. Make money matter:** start with $600, or make the shop items more central to the routes.

### Takeaways for v0.2

- **Explain every action.** Each card gets one plain-language line on what the action is in the real world, at the level of a news article, never instructions. Physical actions were easier to grasp because they're concrete; digital and social ones need the same concreteness.
- **Frame time as parts of a day, not "blocks".** Show a day timeline (Night, Dawn, Morning, Afternoon, Evening, Late) with what each part opens up: business hours for social engineering and the lobby, night for dumpsters and the server room. Give every day the same shape: Day 1 currently has 4 parts while Days 2 and 3 have 6, which is confusing.
- **Teach parallel operations early**, for example a first contract or tutorial step that has the player run two things at once.
- **Make money about preparation.** More operations that need or are improved by gear bought ahead, so shopping becomes planning.
- **Fold rulings 1–9 into the rules text.**
- **One tuning change**, from the candidates above.

## Version 0.2 (built after session 1)

- **Time:** turns are parts of the day (4 hours). The clock is a grid of three days with the same six parts each, numbered turns 1–16, with a "what's open when" table. Card times are in hours (4 h, 8 h, 12 h).
- **Explanations:** every card has a plain-language "what it is" line and separate ✓ success and ✗ failure lines. "Words to know" explains the keys and tracks; a first-turn guide shows three slots running at once.
- **Gear:** Spear-Phish now needs a Lookalike domain ($200, reusable) instead of costing $200 per attempt. New: Caller-ID spoofer ($250: +20% Helpdesk Pretext Call, +10% MFA Push Fatigue) and Hi-vis vest and clipboard ($150: +20% Stake Out the Lobby and Tailgate and Plant). Every shop item says what it is.
- **Tuning (the one balance change):** Target Alert drops by 2, not 1, in a turn with no Noise.
- **Rulings 1–9** are written into the rules. Exfiltrate's success line no longer lists Noise, since success ends the contract.
- **Fix:** the rival variant's advance turns now really are every third turn (3, 6, 9, 12, 15).

The gear changes affect balance too, so session 2 tests two balance changes at once: the Alert drop and the gear. If it plays very differently, those are the two suspects. Not changed yet: the idle Body slot in the Evening and after recon, starting cash, and Exfiltrate's failure Noise.

## Session 2: Corrigan Freight (solo, v0.2, Claude plays)

Claude played this one to test balance and rules, not clarity: Claude wrote the rules, so it can't judge whether they're easy to understand. Strategy: a quiet social route with gear, lying low to bring Alert down before the key rolls. Dice rolled in the shell, one call per turn, after the turn's decisions.

| Turn | Shop and move | Started | Resolved (roll) | After: Cash · Intel · Alert · Heat · Trail · Keys |
|---|---|---|---|---|
| 1 · D1 Morning ☀ · Desk | Caller-ID spoofer ($250). Travel to Café | OSINT Sweep, Bug Bounty (12 h) | OSINT ✓ (100%): Employees revealed | $750 · 2 · 0 · 0 · 0 · none |
| 2 · D1 Afternoon ☀ · Café | none | Helpdesk Pretext Call, Wardrive the Block | Wardrive ✓ (5 vs ≤9): +1 Intel, Guest Wi-Fi. Helpdesk ✓ at 80% (50% with spoofer + 3 Intel; 8 vs ≤8): **Foothold** | $750 · 0 · 0 · 0 · 0 · Foothold |
| 3 · D1 Evening · Café | none | Crack Password Hashes (12 h) | Bug Bounty ✗ (10 vs ≤7) | $750 · 0 · 0 · 0 · 0 · Foothold |
| 4 · D1 Late ☾ · Café → HQ | Walk to HQ | Dumpster Dive | Dumpster Dive ✗ (8 vs ≤6): Heat +2 | $750 · 0 · 0 · 2 · 0 · Foothold |
| 5 · D2 Night ☾ · HQ | none | Dumpster Dive (retry) | Dumpster Dive ✓ (3 vs ≤6): +3 Intel. Crack ✗ at 70%, no Intel spent (9 vs ≤7): Noise 1, Trail 1 | $750 · 3 · 1 · 2 · 1 · Foothold |
| 6 · D2 Dawn ☾ · HQ → Café | GPU rig ($600). Walk to Café | Crack Password Hashes (8 h with the GPU rig) | Nothing resolves. Quiet, so Alert −2 | $150 · 3 · 0 · 2 · 1 · Foothold |
| 7 · D2 Morning ☀ · Café | none | none | Crack ✓ at 80% with 1 Intel (7 vs ≤8): **Admin credentials**. Noise 1, Trail 1 | $150 · 2 · 1 · 2 · 2 · Foothold, Admin |
| 8 · D2 Afternoon ☀ · Café | none | MFA Push Fatigue, Pivot to Billing (8 h) | MFA Push ✗ at 70% (9 vs ≤7): Noise 2 | $150 · 2 · 3 · 2 · 2 · Foothold, Admin |
| 9 · D2 Evening · Café | none | Wipe Logs (resolved before Pivot) | Wipe Logs ✓ at 70% (3 vs ≤7): Trail 2 → 0. Pivot ✓ at 70% (60% − 10% Elevated + 2 Intel; 1 vs ≤7): **Route**. Noise 2, Trail 1 | $150 · 0 · 5 · 2 · 1 · Foothold, Admin, Route |
| 10–12 · D2 Late to D3 Dawn | none | none: lie low until business hours | Three quiet turns: Alert 5 → 3 → 1 → 0 | $150 · 0 · 0 · 2 · 1 · Foothold, Admin, Route |
| 13 · D3 Morning ☀ · Café | none | MFA Push Fatigue | MFA Push ✓ at 70% (2 vs ≤7): **MFA bypass**. Noise 1 | $150 · 0 · 1 · 2 · 1 · all four keys |
| 14 · D3 Afternoon ☀ · Café → HQ | Hi-vis vest ($150). Walk to HQ after starting Exfiltrate | Exfiltrate the Ledger, Stake Out the Lobby (100% with the vest) | Nothing resolves. Quiet, so Alert −2 | $0 · 0 · 0 · 2 · 1 · all four keys |
| 15 · D3 Evening · HQ | none | none | Stake Out ✓ (100%): +1 Intel. **Exfiltrate ✓** at 90% with 1 Intel (5 vs ≤9): **contract complete** | $3,000 · 0 · 0 · 2 · 1 · won |

### Result

| # | Result | Turns used | Cash left | Heat | Alert | Keys: how you got each | Notes |
|---|---|---|---|---|---|---|---|
| 2 | **Won** | 15 of 16 | $0, then +$3,000 | 2 | 0 | Foothold: Helpdesk Pretext Call (spoofer + 3 Intel). Admin: Crack Password Hashes (second try, GPU rig, 1 Intel). Route: Pivot to Billing (2 Intel, after Wipe Logs). MFA bypass: MFA Push Fatigue (second try, after lying low) | Three quiet turns before the last keys; Alert never passed 5 |

### What Claude saw

1. **Lying low works now.** Three quiet turns took Alert from 5 to 0, so MFA Push and Exfiltrate rolled at full strength. Before deciding, Claude estimated about 73% to win by waiting against about 66% by pushing on with Steal Session Token. With v0.1's drop of 1, Alert would only have reached 2 by turn 13.
2. **It also creates dead turns.** Turns 10–12 had no decisions at all. In the real-time game that's fast-forward; on paper it's dull.
3. **Money mattered this time.** All $1,000 went on the spoofer, the GPU rig and the vest; the vest used the last $150 to lift the final roll from 80% to 90%. The failed Bug Bounty limited the options. This supports "money as preparation".
4. **Careful play uses few slots.** Laptop 2 sat idle in 9 of 15 turns and the Body slot in 9 of 15. Every running noisy operation threatens Alert, so only silent ones (recon, Bug Bounty, Wipe Logs, the stakeout) paired well in parallel.
5. **Spending Intel is a real decision.** Saving Intel for Pivot left Crack at 70%, and it failed by 2; one more Intel would have passed.
6. **Business hours are the real clock for the endgame.** MFA Push needs ☀, so the failure on turn 8 meant waiting until turn 13.
7. **New rules gap:** losing Admin and MFA bypass to a credential reset doesn't say what happens to running operations that need them. Proposed as ruling 10.

## Simulation: v0.2 balance runs

[`tools/paper_prototype_sim.py`](../../tools/paper_prototype_sim.py) plays the contract 10,000 times per play style and ruleset. The seed is fixed, so `python tools/paper_prototype_sim.py` reproduces these numbers exactly; `--trace "quiet social"` prints sample games turn by turn. Traces were read to check the bots follow the rules.

The bots follow scripted styles and never take a roll that could cause a Lockdown, so some of their time-outs would be last-chance gambles for a human, like the final roll of session 1. They test balance, not clarity or fun.

- **Quiet social:** Caller-ID spoofer, Helpdesk call, Crack, Pivot, MFA Push; lies low before key rolls (like session 2).
- **Balanced:** no gear up front; phone or email in, Abuse or Crack, MFA Push; moderate risk (like session 1).
- **Fast digital:** Known exploit, the VPN, Abuse or Crack, Steal Session Token; never wipes logs; ignores Alert until Lockdown is possible.
- **Physical:** Hi-vis vest, Network implant and Lock picks; tailgate in, Server Room for the Route.
- **Buy access:** Bug Bounty to afford Buy Access; a phone call only if the money doesn't come.

### Win rate by ruleset

| Ruleset | Average | Quiet social | Balanced | Fast digital | Physical | Buy access |
|---|---|---|---|---|---|---|
| v0.1 | **40%** | 53% | 42% | 27% | 40% | 40% |
| v0.2 gear, but Alert drop 1 | **47%** | 67% | 43% | 26% | 58% | 40% |
| **v0.2** | **58%** | 73% | 58% | 45% | 59% | 53% |
| v0.2 + Exfiltrate failure Noise 2 (candidate B) | **59%** | 73% | 60% | 46% | 62% | 54% |
| v0.2 + Wipe Logs lowers Alert by 1 (candidate C) | **59%** | 73% | 61% | 44% | 61% | 54% |
| v0.2 + Watch the Building, unlimited (candidate D) | **78%** | 94% | 71% | 66% | 73% | 86% |
| v0.2 + Watch the Building, 3 uses | **65%** | 80% | 60% | 53% | 68% | 63% |

"Watch the Building" is a candidate Body operation: at the Café or near HQ, any time, 4 h, certain, silent, +1 Intel.

### How v0.2 contracts end

| Style | Win | Raid | Time out | Avg winning turn | Credential reset | Idle Laptop slot-turns (of 32) | Idle Body turns (of 16) |
|---|---|---|---|---|---|---|---|
| Quiet social | 73% | 1% | 26% | 12.9 | 9% | 8.4 | 10.0 |
| Balanced | 58% | 12% | 30% | 11.2 | 10% | 10.6 | 9.3 |
| Fast digital | 45% | 39% | 16% | 11.2 | 33% | 8.9 | 10.2 |
| Physical | 59% | 5% | 36% | 13.4 | 4% | 13.1 | 6.5 |
| Buy access | 53% | 3% | 44% | 14.0 | 19% | 9.3 | 11.3 |

### What the numbers say

1. **v0.2 works.** The average win rate rises from 40% to 58%. The Alert drop of 2 helps the risky styles most (Fast digital 26% → 45%, Balanced 43% → 58%); the new gear helps the careful and physical ones (Quiet social 53% → 67% and Physical 40% → 58% from gear alone).
2. **The spiral is handled.** Candidates B and C add about 1 point each: not worth the extra rules.
3. **Time is now the main way to lose** (16–44% of contracts). Business hours gate the Helpdesk call, MFA Push, the stakeout and tailgating, so one failure there waits until the next business day.
4. **Recklessness is punished by Heat, not Lockdown.** Fast digital loses 39% to raids: without Wipe Logs, Trail builds up and Trace turns it into Heat every turn.
5. **Several routes are viable.** The quiet social route is strongest (73%), but physical, balanced and buy-access play all win more than half the time.
6. **Slots sit idle:** 8–13 of 32 Laptop slot-turns and 6–11 of 16 Body turns.
7. **Body work must not give unlimited Intel.** Unlimited Watch the Building lifts the average to 78% (Quiet social 94%). Limited to 3 uses it gives 65% and cuts idle Body turns to about 6.
8. **Rules gap:** Bug Bounty has no limit (proposed ruling 11).

### Recommendation

Hold balance changes until a person plays v0.2. Win rates are in a reasonable range, and v0.2's main changes (the clock, the explanations) can only be tested by someone who didn't write them. After that playtest, v0.3 should write in rulings 10 and 11, and, if the idle Body slot still feels dull to a human, add Watch the Building with 3 uses as the one balance change.
