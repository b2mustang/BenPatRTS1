# Footprint (BenPatRTS1): Game Plan

Status: **planning** · Last updated: 2026-11-19 · This is a living document; update it whenever a decision changes. The game design lives in [`CONCEPT.md`](CONCEPT.md) and the story in [`STORY.md`](STORY.md).

## 1. Decisions so far

| Area | Decision | Notes |
|---|---|---|
| Game | Single-player hacking strategy game with a story campaign | Direction changed 2026-11-19 from an online versus RTS (`CONCEPT.md` §2). |
| Multiplayer | None at launch; a 1v1 race mode may come later | The game is built so that mode stays possible (§4). |
| Store and release | Steam: closed Playtest, then a free prologue demo at a Next Fest, then a full 1.0 release | No Early Access. Windows first; a Linux build later helps Steam Deck. |
| Engine | Godot 4.7.x, .NET (C#) edition | Latest stable is 4.7.2 (Aug 2026); 4.8 is in beta. Pin one version and upgrade only between milestones. |
| Visuals | Stylized interface and maps, framed by a 3D hideout with a third-person view of your character | `CONCEPT.md` §17. |
| Protagonist | Morrow: fixed handle, man or woman, appearance configurator, six skill branches | `CONCEPT.md` §5, `STORY.md`. |
| Story | "The climb": a laid-off IT worker rises through Halden Bay's hacking underground | `STORY.md`. |
| Campaign | ~10 story missions (8–10 hours), 2 endings, plus generated side contracts | `CONCEPT.md` §4. |
| Voice | Human actors for key moments; protagonist lines in key scenes recorded twice | `CONCEPT.md` §16. |
| Team | Solo, part-time (~10–15 h/week) | Roughly 50 h/month, or 550–600 h/year. |
| Competition | Friendly challenge with a friend | No official rules, format or deadline; Steam is the real target. |
| Working title | Footprint | No exact match on Steam as of 2026-11-19; trademarks not yet checked. |

## 2. Scope reality check

Going single-player removed the hardest technical work (netcode and online balance) and the risk of empty online lobbies. In its place come writing, story-mission design, a character configurator and voice work. Solo and part-time, this is still a large game. The plan controls the risk with:

- **A tight campaign** (8–10 hours) whose replay value comes from generated side contracts and skill builds, not from more hand-made missions.
- **Data-driven content:** operations, assets and target types are data files, so adding content doesn't need new code.
- **Bought art kits** for the character creator, the hideout props and the city.
- **Go/no-go gates** at the end of M1, M2 and M4, where you re-decide with real data.

Rough estimate: **~1,500 hours to 1.0, about 2.5 years at this pace.** Re-estimate after M1 using your real velocity.

## 3. Content at 1.0

| Item | Amount |
|---|---|
| Story missions | ~10 (8–10 hours), 2 endings |
| Side contracts | Generated from 4 target types, with seeded events |
| Mission types | 4 (steal, alter, plant, leak) |
| Skill branches | 6 |
| Operations | ~40 |
| Assets | ~50 |
| City | 1 |
| Characters | Morrow (two versions plus configurator), the rival, 6 supporting characters |
| Voice | Key scenes only |
| Modes | Campaign (normal and Ironman), job board after the story |
| Not at 1.0 | Versus mode, typed command bar, extra story (possible DLC), localization beyond English (to decide) |

## 4. Technical architecture

```
            ┌───────────────────────────────────────────────┐
            │  Sim: plain .NET class library (no Godot)      │
            │  campaign state · mission state · defenders AI │
            │  rival AI · contract generator · seeded RNG    │
            └──────────▲──────────────────────────┬─────────┘
            commands   │                          │  what the player knows
            ┌──────────┴──────────────────────────▼─────────┐
            │  Godot presentation: hideout (3D), network and │
            │  city maps, op cards, live feed, dialogue,     │
            │  audio, time controls                          │
            └────────────────────────────────────────────────┘
```

### Rules for the simulation

1. **The sim is its own .NET class library** (`src/Sim`) with no reference to Godot. Godot code reads sim state and sends commands; it never changes sim state directly.
2. **Commands are the only input.** The player, the rival AI, tests and any future online opponent all send the same commands.
3. **Truth and knowledge are separate.** The sim tracks what is really there (the target network, the rival's moves) separately from what the player knows (revealed nodes, intel). The UI only reads the player's knowledge. This is fog of war, and it is also what makes a later versus mode possible: a host would send each player only their own knowledge.
4. **Integers for game quantities:** money in cents, time in sim ticks, probabilities in basis points. Saves, tests and seeded runs stay exact. Floats are for presentation only.
5. **One seeded RNG per mission** (and one for contract generation), so a seed plus a command list reproduces a mission exactly for tests and bug reports.
6. **Fixed sim tick.** Speed controls (1×, 2×, 3×) change how many ticks run per real second; pause runs none.
7. **Data-driven content:** operations, assets, skill branches and target templates are defined in data files, not code.
8. **Everything saveable:** campaign and mission state serialize to a versioned save format from the start.

### Story and dialogue

- Choose a branching-dialogue tool with a C# runtime during the vertical slice (for example ink or Yarn Spinner).
- Story beats are triggered by sim events (mission start, an operation finishing, Heat thresholds) through the same command and event system.

### Steam integration

- **Steamworks.NET** from C#: overlay, achievements, Steam Cloud saves, rich presence.
- Develop against Valve's test App ID **480 (Spacewar)** until you own your own App ID.
- No networking at launch. A future versus mode would use Steam lobbies and Networking Sockets with the host-authoritative model above.

### Proposed repository layout

```
/game              Godot project (project.godot, scenes, presentation C#)
/game/assets       imported art and audio (Git LFS)
/game/data         operations, assets, skill branches, target templates, dialogue
/src/Sim           simulation (.NET class library)
/src/Sim.Tests     unit, scenario, save/load and generator tests
/tools             build and SteamPipe upload scripts, content tools
/docs              plan, concept, story bible, art style guide, asset licence ledger
```

### Testing

- `dotnet test` on the sim: fast, no Godot needed.
- **Scenario tests:** a seed plus a scripted command list must produce the expected outcome.
- **Save/load round trips:** save at any tick, load, continue, and get the same result as never saving.
- **Generator tests:** every generated side contract is winnable (a route exists from the start to the crown jewel) and stays within difficulty bounds.
- **Balance runs:** a bot plays thousands of generated contracts headless to measure success rates, Heat and mission length.
- **Godot headless smoke test:** launch, load the hideout, start a contract, run N ticks, quit.
- **Human playtests** from M1 (paper) onward.

### Tooling and repository hygiene

- **The repository lives at `C:\dev\BenPatRTS1`, outside OneDrive.** Keep it out of synced folders: Godot's `.godot/` cache and .NET `bin/`/`obj/` change constantly, and OneDrive locks files and can create conflicted copies inside `.git`. GitHub is the backup.
- **Git LFS** for binary assets (`.glb`, `.fbx`, `.png`, `.wav`, `.ogg`, …). Check GitHub's LFS storage and bandwidth quota; voice recordings and 3D kits grow quickly. Keep source art (`.blend`, `.psd`) in LFS or separate backed-up storage.
- `.gitignore` for Godot and .NET: `.godot/`, `bin/`, `obj/`, export output.
- GitHub Actions: build and test the sim on every push.
- Track work in GitHub Issues or Projects, one milestone per roadmap row.

## 5. Art, audio and voice plan

- **Style guide** (one page, in M2): palette, the look of the network and city maps, UI language, the hideout's mood.
- **Character:** buy a stylized character-creator kit that exports to glTF and allows commercial use in Godot: two body types, faces, hair, clothing. Add an animation pack (sitting and typing, idle, walking, phone call, reactions).
- **Hideout:** a modular room kit plus ~30 upgrade props (screens, rigs, phones, cables, decorations).
- **Network map:** mostly shaders and effects, built in code.
- **City map:** a low-poly city kit.
- **Story scenes:** short in-engine scenes in the hideout and at key locations; stylized stills where full scenes would cost too much.
- **Voice:**
  - Write the full script and lock it before recording.
  - Cast through voice-actor marketplaces: two protagonist actors plus the main supporting characters.
  - Use placeholder text-to-speech during development only; ship human voices.
- **Music and sound:** marketplace sound effects plus licensed or commissioned music.
- **Licences:** confirm every asset allows use in Godot and in a commercial Steam game. Keep `docs/asset-licenses.md` as a ledger from the first asset onward.
- **AI-generated content:** if any shipped asset is AI-generated, it must be disclosed in Steam's content survey.

## 6. Roadmap

Hours assume ~50 h/month. Re-estimate after M1.

| # | Milestone | When (from start) | ~Hours | Done when |
|---|---|---|---|---|
| M0 | Foundations | Month 1 | 40 | LFS and `.gitignore`, Godot 4.7 .NET project, `src/Sim` library with tests, CI green |
| M1 | Paper and systems prototype | Months 2–5 | 200 | Paper prototype played; plain digital prototype of one generated side contract with ~10 operations, defenders AI, time controls, save/load |
| M2 | Vertical slice | Months 6–12 | 350 | First story mission playable start to finish: hideout with configured character, both maps, dialogue tool, placeholder voice, job board with one target type, scars between missions |
| M3 | Store page and Playtest | ~Month 13 | 50 | Steam Direct fee paid, store page live as Coming Soon, closed Steam Playtest running with the slice |
| M4 | Prologue demo | Months 13–17 | 150 | First 1–2 story missions plus a few side contracts, polished, with a tutorial; registered for the next Next Fest |
| M5 | Full production | Months 17–28 | 550 | All ~10 story missions, 4 target types, 6 skill branches, ~40 operations, ~50 assets, rival AI, both endings, Ironman, final voice, music and sound |
| M6 | Polish and 1.0 launch | Months 28–31 | 160 | Bugs, balance, settings, accessibility, achievements, cloud saves; Steam release checklist complete |

### Go/no-go gates

- **End of M1:** Are side contracts fun on paper and in the plain prototype? If not, rework the operation system before any art or story.
- **End of M2:** Do outside players finish the first story mission and want the next one? Is the art pipeline (character kit, hideout props, city) affordable? Adjust scope before M4.
- **After the Next Fest (M4):** Wishlists and demo feedback decide whether to keep the 1.0 scope, cut it or expand it.

## 7. Steam release checklist

Current as of November 2026; confirm each figure in your Steamworks account.

- [ ] Steamworks partner account: legal name or company, bank details, tax interview, identity verification.
- [ ] Steam Direct fee: **US$100 per game**, recouped once the game reaches $1,000 in adjusted gross revenue.
- [ ] At least **30 days** between paying the fee and releasing.
- [ ] Store page assets: capsule images in every required size, description, screenshots, trailer, system requirements, content survey (including any AI-content disclosure).
- [ ] Store page review (allow several business days), then a public **Coming Soon page for at least 2 weeks** before release. Aim for 12+ months to build wishlists.
- [ ] Closed **Steam Playtest** for the vertical slice.
- [ ] Free **demo** (the prologue), set up as a demo of the main game.
- [ ] Builds uploaded with SteamPipe (`steamcmd` plus build scripts), with a default branch and a beta branch.
- [ ] Build review passed before release.
- [ ] Steamworks features: overlay, achievements, Steam Cloud saves, rich presence.
- [ ] Release is a manual button press after both reviews are approved.

**Steam Next Fest** is a one-time opportunity per game and needs a playable demo. Known 2027 editions: February 22 – March 1 (register by January 10) and June 14–21 (register by April 25); October 2027 dates are not announced yet. The prologue demo is planned for about month 17, so target the first edition after that (likely 2028) and register before its deadline.

## 8. Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Scope too large for solo part-time | High | High | Tight campaign, data-driven content, bought art kits, gates |
| The core loop isn't fun | Medium | High | Paper prototype and plain prototype before any art or story |
| Writing quality | Medium | High | Outline the whole story before production; get outside readers; consider a freelance editor |
| Generated side contracts feel samey | Medium | Medium | 4 target types, seeded events, mission types, modifiers |
| Character configurator cost | Medium | Medium | Bought kit, limited options, configurator built once |
| Voice cost and scheduling | Medium | Medium | Key scenes only; lock the script before recording |
| Hacking games are a niche | Medium | High | Strong store page early, prologue demo, Next Fest, devlog |
| Name conflict (an upcoming game is called *Digital Footprint: Cyber Investigation*) | Low | Medium | Trademark check before the store page (M3) |
| Burnout | Medium | High | Steady weekly hours, small monthly goals, public devlog for accountability |

## 9. Open questions

- **Story details:** the names of mission targets (`STORY.md` §11).
- **Mission length:** 30–60 minutes is a starting value to test in M1.
- **Art style details** and which character-creator kit to buy (M2).
- **Dialogue tool:** ink, Yarn Spinner or another option (M2).
- **Minimum-spec PC** (before M2).
- **Localization** at 1.0 or later.
- **Business entity and taxes** (talk to an accountant before M3).
- **Price** (before M6).

## 10. Next steps

1. Name the mission targets (`STORY.md` §11).
2. Run the paper prototype ([`prototype/paper-prototype.html`](prototype/paper-prototype.html), now v0.2): session 1 on v0.1 is in [`prototype/playtest-log.md`](prototype/playtest-log.md). Play 2–4 more contracts on v0.2 and log them.
3. Start M1: the plain digital prototype of one side contract, built on what the paper prototype shows. (M0 is done: scaffold, tests, Godot smoke test and green CI.)

## Sources

- [Steam Direct (Valve)](https://partner.steamgames.com/steamdirect)
- [Steamworks onboarding documentation](https://partner.steamgames.com/doc/gettingstarted/onboarding)
- [Steam Next Fest, February 2027 (Steamworks)](https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest/feb_2027)
- [Steam Next Fest, June 2027 (Steamworks)](https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest/june_2027)
- [Godot 4.7.2 released (OpenSourceForU)](https://www.opensourceforu.com/2026/08/godot-4-7-2-released/)
- [Digital Footprint: Cyber Investigation (Steam)](https://store.steampowered.com/app/4611490)
