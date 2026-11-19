# Footprint: Game Concept

Status: **concept**; direction set 2026-11-19 (single-player story campaign) · Working title: **Footprint** · Mark ideas as kept, cut or changed as you decide.

## 1. Pitch

> **Start with a laptop. Build a reputation. Leave no footprint.**

A single-player hacking strategy game with a story. You play a hacker in a present-day city who starts with nothing but a laptop and a café's Wi-Fi. You take jobs: hand-made story missions and generated side contracts. Every job pays in money and reputation, which buy better equipment, unlock new skills and open doors to bigger clients. Inside a mission you plan and run operations in real time (recon, phishing, exploits, rented servers, trips into the physical world to plant devices or clone badges), trading speed against success chance against noise. Noise alerts the target's defenders and leaves a footprint. Footprints follow you from job to job: Heat builds, identities get burned, and a rival hacker learns how you work.

**Setting:** present day, in **Halden Bay**, a fictional booming coastal city. **Tone:** grounded and tense, with dry humor.

**Story:** Morrow, a laid-off helpdesk tech blamed for a breach at Plumbline Civic Systems that they didn't cause, climbs Halden Bay's hacking underground and has to decide whether they've become what they once despised. Details are in [`STORY.md`](STORY.md).

### Inspiration and IP guardrails

The tone is inspired by hacker techno-thrillers such as *Mr. Robot*. Everything in the game is original:

- No characters, names, organizations, plot points, logos, masks, music or visual signatures from the show.
- No real companies or real security-product brands; tools get generic names ("keystroke-injection USB", "rogue access point", "onion relay network").
- Hacking is shown with authentic concepts and vocabulary, but it stays abstract: no real exploit code or step-by-step instructions.

## 2. Decisions

### Campaign direction (2026-11-19)

| # | Question | Answer |
|---|---|---|
| 1 | Multiplayer | Single-player at launch. A 1v1 race mode may come later, so the game is built to allow it. |
| 2 | Protagonist | One written character with a fixed name (as in *Mass Effect*), playable as a man or a woman, appearance set in a configurator. Grows through skill branches. |
| 3 | Story structure | A story spine of hand-made missions, with a job board of generated side contracts between them. A few key choices change later missions and the ending. |
| 4 | Time in missions | Pause plus 1×, 2× and 3× speed. Important events drop the speed back to 1× automatically. |
| 5 | Failure | Failures leave scars (burned gear and identities, lost money, lingering Heat). Optional Ironman mode with one save. |
| 6 | Story and voice | Story told mostly through the desk (emails, chats, calls, news). Key moments voiced by human actors, including a small set of protagonist lines recorded in both voices. |
| 7 | Campaign length | 8–10 hours, ~10 story missions, 2 endings. |
| 8 | Release | Free prologue demo (Steam Next Fest) and an earlier closed Steam Playtest, then a full 1.0 release. |

Story decisions are in [`STORY.md`](STORY.md).

### Carried over from the versus concept

| Topic | Decision | Status in the campaign |
|---|---|---|
| Raids | A raid ends your run unless you prepared; each protection turns one raid into a setback | Kept: an unprotected raid ends the campaign (load a save) |
| Presentation | Stylized interface and two stylized maps, framed by a 3D hideout | Kept; the hideout view becomes third person so you see your character |
| Input | Click-driven with flavor commands in the live feed; typed command bar later | Kept |
| Objectives | One mission structure with four endings: steal, alter, plant, leak | Kept, as mission types |
| City map | "Go to" actions that take in-game time; chance to spot the rival at the same location | Kept |
| Setting | Present day, fictional city | Kept |
| Netcode | Host-authoritative with per-player visibility | Applies only to a future versus mode |
| Content | 6 backgrounds, ~40 operations, ~50 assets, 4 target types | Kept; backgrounds become skill branches; free-for-all dropped |
| Hideout between matches | (was open) | Answered by the campaign: the hideout persists and grows |
| Match length 30–45 min | | Replaced by mission length (§6) |

## 3. Design pillars

1. **Every action is a trade-off** between time, cost, success chance and noise.
2. **OPSEC is half the game.** Protecting yourself matters as much as breaking in.
3. **Two worlds, one operation.** Digital and physical methods open doors for each other.
4. **Your footprint follows you.** What you do on one job (Heat, burned identities, reputation, story choices) shapes the next.
5. **Authentic, not technical.** Real concepts and terms, playable without security knowledge.

## 4. Campaign structure

```
        ┌──────────────────────────────────────────────────────────┐
        │  HIDEOUT (hub)                                           │
        │  read messages · buy gear · spend skill points ·         │
        │  upgrade the room · lie low to cool Heat                 │
        └───────────────┬──────────────────────────▲───────────────┘
                        │ pick a job               │
          ┌─────────────▼─────────────┐            │
          │ Story mission (hand-made) │            │
          │   or side contract        │            │
          │   (generated)             │            │
          └─────────────┬─────────────┘            │
                        ▼                          │
          ┌───────────────────────────┐            │
          │ MISSION (real time, pause,│            │
          │ 1×/2×/3×)                 │            │
          └─────────────┬─────────────┘            │
                        ▼                          │
          ┌───────────────────────────┐            │
          │ DEBRIEF: money, reputation,├───────────┘
          │ skill points, Heat, scars │
          └───────────────────────────┘
```

- **Story spine:** ~10 hand-made story missions over 8–10 hours, leading to 2 endings. A few key choices (who to trust, which client to betray, what to leak) change later missions.
- **Job board:** generated side contracts between story missions, built from the 4 target types. They earn money and reputation, let you try new gear, and keep playing after the story ends. Taking too many raises Heat.
- **Progression:**
  - **Money** buys equipment, infrastructure and services.
  - **Reputation** unlocks better clients, higher market tiers and story missions, and grants skill points.
  - **Skill points** go into six skill branches (§5).
  - **The hideout** grows visibly as you upgrade.
- **Scars:** consequences persist between missions:
  - burned gear and cover identities stay burned;
  - money spent on failed jobs is gone;
  - Heat carries over and falls only when you lie low.
- **The rival:** Splice (Julian Ashby), Morrow's former colleague, who caused the breach Morrow was blamed for (`STORY.md`). Some story missions are races against them; in others they hunt you.
- **Difficulty:** normal saves by default, with an optional **Ironman** mode (one autosave, no reloading).

## 5. The protagonist

- **Morrow:** one written character with a fixed hacker handle, so dialogue and voice work stay simple. People from Morrow's old life use Morrow's real name, which is **redacted** (a black bar in text, a glitch in voice) until the final scenes (`STORY.md` §4).
- **Man or woman**, chosen at the start, with an **appearance configurator** (face, hair, skin tone, clothing).
- **Visible** in the hideout (third-person view of your character at the desk), in story scenes and during physical operations.
- **Six skill branches**, each with passive bonuses and one signature ability:

| Branch | Bonuses | Signature ability (idea) |
|---|---|---|
| **Social Engineering** | Better phishing and pretexting | Run two social operations in one op slot |
| **Exploit Development** | Better exploit success | Research your own zero-day (slow, costly, unlimited stock) |
| **Hardware** | Cheaper, better physical gear | Build custom implants that defenders struggle to find |
| **Botnets** | Cheaper compute, bigger botnet | Cheap DDoS; compute-based income |
| **Insider Networks** | Cheaper, more reliable insiders | Recruit an employee inside a target |
| **Ghost** | Smaller footprint, harder to trace | Wipe a trail instantly once per mission |

## 6. A mission at a glance

| | |
|---|---|
| **Length** | About 30–60 real minutes at 1× (starting value; less with speed-up). Covers a few in-game days. |
| **Time** | Pause plus 1×, 2× and 3× speed. Alerts drop to 1× when the defenders notice you, the rival appears or an operation finishes. Time of day matters (§14). |
| **Start** | Your current gear, infrastructure and skills, carried over from the campaign. |
| **Success** | Complete the mission's final operation (below). |
| **Failure** | Caught during a physical operation, the target locks you out, the rival finishes first (race missions), or a raid when Heat maxes out. Failures leave scars (§4). |

### The endgame

The objective node (for example, the server holding the files the client wants) needs several keys: a route into its network segment, admin credentials and a way past multi-factor authentication. Once you have all three, the final operation takes real time and the defenders notice it, so missions end with a tense finish rather than a silent win.

### Mission types (final operations)

| Type | How it plays |
|---|---|
| **Steal** | Exfiltrate the data. Limited by time and bandwidth, and noisy. |
| **Alter** | Change records (for example, falsify a shipping manifest). Quick, but you must stay undetected for some in-game hours afterward or the change is reverted. |
| **Plant** | Put evidence or a payload in place. Needs physical or insider access. |
| **Leak** | Steal, then publish. You can be traced while you publish. |

## 7. Mission loop

```
   ┌──► Recon: reveal nodes, learn defenses, find people to target
   │        │
   │        ▼
   │    Choose a method: digital, physical or social
   │        │
   │        ▼
   │    Run an operation: time, cost, success chance, noise, trail
   │        │
   │        ▼
   │    Gain: access, credentials, intel, cash, compute
   │        │
   │        ▼
   │    Adapt: buy or deploy assets mid-mission
   │        │
   │        ▼
   └─── Clean up and defend: wipe trails, rotate infrastructure, watch for the rival
```

Operations run in parallel, like an RTS production queue. The number of operations you can run at once (your **op slots**) is your "supply cap"; better hardware, a botnet or hired contractors raise it.

## 8. Resources and meters

| Name | Scope | Gained from | Spent on / effect |
|---|---|---|---|
| **Cash** | Campaign and mission | Jobs, side gigs, selling data | Hardware, infrastructure, tools, services |
| **Reputation** | Campaign | Completed jobs, especially clean ones | Unlocks clients, market tiers, story missions; grants skill points |
| **Skill points** | Campaign | Reputation milestones | Six skill branches |
| **Compute** | Mission | Your rigs, rented GPU servers, botnet nodes | Cracking, brute force, DDoS, faster exfiltration |
| **Intel** | Mission | Recon operations (digital and physical) | Raises success chance; reveals the map; unlocks targeted operations |
| **Access** | Mission | Successful operations | Footholds, credentials, badges, tokens |
| **Op slots** | Mission | Better laptop, more rigs, botnet, contractors | How many operations run at once |
| **Heat** | Campaign | Noisy or failed operations, being seen, being traced | Law-enforcement pressure; maximum means a raid; falls only when you lie low |
| **Target Alert** | Mission | Your noise (and the rival's) | Makes the defenders react |

## 9. Operations

Every action is an operation card with the same five numbers:

```
SPEAR-PHISHING CAMPAIGN                        Initial access · Social
Time    6 in-game hours (only during business hours)
Cost    $300 and 1 phishing domain
Chance  35%   +15% with employee OSINT · +10% Social Engineering branch · −20% after the target's awareness training
Noise   Low on success · Medium on failure
Trail   Phishing domain, mail-server logs
```

### Sample operations by stage

| Stage | Digital | Physical | Social |
|---|---|---|---|
| **Recon** | Scan the perimeter; map exposed services; search breach dumps | Dumpster dive; stake out the lobby (badge type, guard rotation); wardrive the block | OSINT on employees' social media; build an org chart |
| **Initial access** | Exploit an exposed service; credential stuffing; buy a foothold from an access broker | Tailgate in and plant a network implant; USB drop in the parking lot; rogue Wi-Fi near HQ | Spear-phishing; pretext call to the helpdesk for a password reset |
| **Persistence and privilege** | Install an implant; escalate privileges; crack password hashes | Clone a badge at the café employees use | Push-fatigue an MFA prompt; recruit an insider |
| **Lateral movement** | Pivot between segments; take the domain controller; pivot through a vendor's VPN | Reach the server room after hours | Impersonate IT to a remote employee |
| **Final operation** | Steal, alter, plant or leak | Physical access for an air-gapped target | An insider carries the data out |
| **Cleanup** | Wipe logs; remove artifacts; rotate infrastructure | Retrieve or destroy planted devices | Burn a persona before it is traced |

Success chance comes from: intel on the target, tool tier, skill branches, target defenses, Target Alert and time of day. Failed operations usually make more noise than successful ones.

## 10. Two maps

### Network map (digital)

A node graph in layers, revealed through recon (fog of war):

- **Internet:** your own infrastructure, the darknet market, public services.
- **Perimeter:** the target's website, mail, VPN gateway, cloud storage.
- **Internal:** workstations, file servers, the domain controller.
- **Crown-jewel segment:** where the objective lives. Sometimes **air-gapped**, which forces a physical or insider method.
- **Third parties:** vendors with access into the target, employees' home networks and social profiles.

Recon first reveals that a node exists, then its software and defenses, then its weaknesses.

### City map (physical)

Halden Bay, small and stylized: your hideout, cafés with public Wi-Fi, each target's site (lobby, parking garage, loading dock, server room), a data center, vendor offices, Pawn's pawn-and-repair shop in the old port district (the hardware market), places employees hang out.

- Your character's location is shown as an icon. You move by clicking a location ("go to"); travel takes in-game time and keeps you away from your desk's op slots.
- Physical operations are cards at each location, just like digital ones.
- Cameras, guards and witnesses add Heat. Physical operations are slow and risky, but they open doors that digital ones can't, like the air gap.
- In rival missions, if you and the rival are at the same location at the same time, each has a chance to spot the other.
- Later in the campaign you can hire field contractors to act in parallel.

## 11. OPSEC: protecting yourself

- **Infrastructure layers.** Every hop between your laptop and the target (VPN, onion relays, chained rented servers) adds time for anyone tracing you. More hops slow your operations slightly.
- **Footprint.** Every operation leaves artifacts on the nodes it touched. Artifacts let the defenders and the rival follow the chain back toward you. Cleaning them costs time.
- **Personas.** Cover identities buy infrastructure and run social operations. A burned persona stays burned for the rest of the campaign and only exposes what it touched, so compartmentalization pays.
- **Counter-intelligence.** Canary tokens and monitoring on your infrastructure warn you when someone is probing it.
- **Heat.** Rises with noisy or failed operations, being seen on camera and being traced. Carries between missions and falls only while you lie low. Thresholds: *Clean → Noticed → Watchlist → Investigation → Raid*.
- **Raids.** An unprotected raid ends the campaign (load a save; in Ironman, the run is over). Each protection (a lawyer, infrastructure kept offsite, encrypted drives, a dead-man switch that wipes on seizure) turns one raid into a heavy setback instead and is then used up. In a setback, police seize the hideout's hardware and anything traceable to it, you move to a new hideout, and Heat partly resets.

## 12. The rival

Splice (Julian Ashby), Morrow's former colleague, who caused the breach Morrow was blamed for and is now a step ahead in the underground (`STORY.md`). In race missions they go after the same target; in others they hunt you. Moves either of you can use:

| Move | What it does |
|---|---|
| **Trace** | Follow the other's artifacts back hop by hop, toward their infrastructure and hideout |
| **Close the door** | Patch a weakness after using it so the other can't follow |
| **Tip off the defenders** | Report the other's foothold anonymously, raising Target Alert for both |
| **Burn infrastructure** | Get the other's servers taken down or flooded |
| **Hijack** | Take over the other's implants or botnet |
| **Deception** | Plant honeypot credentials or fake nodes |
| **Market denial** | Buy out a limited-stock item first |
| **Anonymous tip** | Hand evidence of the other's identity to the police to raise their Heat |

The same structure, with a human on the other side, is what a later 1v1 race mode would use.

## 13. Assets and the market

Everything you buy improves one of three things: **access** (success chance and new methods), **speed** (shorter operations, more op slots) or **protection**.

| Category | Examples | Mostly improves |
|---|---|---|
| **Hardware** | Better laptop, GPU rig, burner phones, rogue access-point kit, keystroke-injection USB, badge cloner, network implant, software-defined radio, lock picks, a hi-vis vest and clipboard | Access, speed |
| **Infrastructure** | Rented servers, proxy chains, onion-relay access, command servers, phishing domains, bulletproof hosting, botnet | Speed, protection |
| **Tools** | Scanners, password crackers, exploit kits, low-detection custom implants, zero-days (rare, expensive), log wipers, rootkits | Access, protection |
| **Services** | Access brokers, leaked credential dumps, a helpdesk-pretext caller, a physical pentester, an insider, a lawyer, a fixer | Access, protection |
| **Defense** | VPN, full-disk encryption, air-gapped machine, canary tokens, dead-man switch, secure comms | Protection |

The darknet market has tiers unlocked by reputation, limited stock and rotating listings. Hardware you own appears in the hideout.

## 14. Income and the in-game clock

### Earning between and during missions

- **Job payouts:** story missions and side contracts.
- **Bug bounties:** clean, slow cash.
- **Selling data** from compromised nodes: fast cash, more Heat.
- **Cryptojacking:** compromised machines mine for you.
- **Renting out your botnet:** passive cash, but easier to trace.

### The in-game clock

- Phishing needs employees at work; physical entry is easier at night but guards still patrol.
- Defenders are short-staffed on nights and weekends.
- Seeded events vary each side contract: a patch day closes known holes, layoffs create a disgruntled insider, a holiday leaves a skeleton crew, an outside audit raises detection, a vendor is breached in the news.

## 15. The defenders (AI blue team)

| Alert level | Defenders' response |
|---|---|
| **Normal** | Routine monitoring; regular patch schedule |
| **Elevated** | More logging; failed logins get investigated |
| **Investigating** | Suspicious nodes inspected; artifacts found faster |
| **Incident response** | Passwords reset, known weaknesses patched, IP addresses blocked, footholds purged |
| **Lockdown** | Segments isolated; physical security doubled; outside responders brought in |

Target Alert decays over time, so lying low inside a mission is a real option.

## 16. Story delivery and voice

- **Through the desk:** emails, encrypted chats, phone calls, news feeds and the live feed carry most of the story. This is cheap, fits the hacker fantasy and is easy to rewrite and translate.
- **Story scenes:** short in-engine scenes in the hideout and at key locations, featuring your configured character.
- **Voice:** key moments (briefings, calls, story turns) voiced by human actors. The protagonist speaks only in those scenes, so a small set of lines is recorded twice (male and female). Everything else is text.
- **Redacted real name:** every mention of Morrow's real name, in text or voice, is masked until the final scenes, so dialogue, UI text and audio all need a real-name tag.
- **Writing tools:** a branching-dialogue tool with a C# runtime (for example ink or Yarn Spinner), chosen during the vertical slice.

## 17. Presentation and controls

- **Hideout:** a 3D room with a third-person view of your character at the desk. It changes as you upgrade: more screens, a GPU rig in the corner, burner phones, a Faraday bag. After a raid setback, you start over in a new, emptier hideout.
- **On the monitors:** the network map (stylized 3D or 2.5D node graph), the city map (low-poly or top-down), the op queue, the live feed, the market, and the Heat and Target Alert meters.
- **Input:** click and drag to launch operations, with hotkeys; each action prints a realistic-looking command in the live feed for flavor. A typed command bar with autocomplete comes after launch.
- **Time controls:** pause, 1×, 2×, 3×, with automatic drop to 1× on important events.
- **Mood:** dark and moody, synth soundtrack, glitch effects, all original.

## 18. Modes

- **Campaign:** normal or Ironman.
- **Job board after the story:** keep taking generated contracts with your build.
- **Possible later:** a 1v1 online race mode reusing the mission and rival systems.

## 19. Release

1. **Closed Steam Playtest** with the vertical slice, for early outside feedback.
2. **Free prologue demo:** the first one or two story missions plus a few side contracts, timed for a Steam Next Fest.
3. **Full 1.0 release** of the complete campaign.

## 20. Content at 1.0

| Item | Amount |
|---|---|
| Story missions | ~10 (8–10 hours) |
| Endings | 2 |
| Skill branches | 6 |
| Operations | ~40 |
| Assets | ~50 |
| Target types (for side contracts) | 4 |
| Mission types | 4 (steal, alter, plant, leak) |
| City | 1 |
| Characters | Morrow (two versions plus configurator), the rival, 6 supporting characters |
| Voice | Key scenes only |
| Modes | Campaign (normal and Ironman), post-story job board |

## 21. Still open

- **Story details:** the names of mission targets (`STORY.md` §11).
- **Mission length:** 30–60 minutes is a starting value to test.
- **Art style details** and which character-creator kit to buy.
- **Dialogue tool:** ink, Yarn Spinner or another option.
- **Price.**

## 22. Suggested first prototype

Test the fun before building the full game:

1. **Paper or spreadsheet prototype:** one target, ~12 operation cards, Heat and Target Alert tracks, a clock. Play a few side contracts solo to see whether the trade-offs are interesting.
2. **Plain digital prototype:** one generated side contract, ~10 operations, the AI defenders, simple UI, time controls. No story, no art.
3. **Vertical slice:** the first story mission with the hideout, both maps and placeholder voice.

## Comparable games (for positioning)

*Uplink* and *Hacknet* (single-player hacking sims), *Watch Dogs* (story-driven hacking that mixes physical and digital), *XCOM* (a home base between missions), *FTL* (real time with pause) and *Mass Effect* (a fixed-name protagonist with a chosen look). The gap this concept aims at: **a story-driven hacking strategy game where OPSEC and your footprint carry from mission to mission**, with **parallel real-time operations across digital, physical and social methods**.
