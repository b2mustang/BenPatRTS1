# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

BenPatRTS1 (working title **Footprint**) is a single-player hacking strategy game with a story campaign, planned for release on Steam. It started as the developer's entry in a friendly RTS-building challenge with a friend; that challenge has no official rules, format or deadline.

- `docs/CONCEPT.md`: the game design. All decisions so far are in §2.
- `docs/PLAN.md`: the production plan (architecture, content at 1.0, roadmap, Steam checklist, risks, open questions).
- `docs/STORY.md`: the story bible (premise, Morrow, the rival, cast, key choices, endings, tone).

Keep them up to date when a decision changes.

Concept in short: in Halden Bay, a present-day fictional coastal city, Morrow, a laid-off IT worker who starts with a laptop, takes hand-made story missions and generated side contracts. Inside a mission they run parallel real-time operations (digital, physical and social) with pause and speed controls, trading time, cost, success chance and noise. Between missions they earn money, reputation and skill points, upgrade a 3D hideout and live with persistent consequences (Heat, burned gear and identities). A recurring AI rival races or hunts them.

Keep all IP original: nothing from *Mr. Robot* (characters, names, organizations, plot points, logos, music, visual signatures), no real company or security-product brands, and no real exploit code or step-by-step attack instructions.

## Decisions

- Engine: Godot 4.7.x, .NET (C#) edition. Pin one version; upgrade only between milestones. Pinned: 4.7.2 (`Godot.NET.Sdk/4.7.2` in `game/Footprint.csproj`).
- .NET: SDK 8.0.428 pinned in `global.json`; all projects target `net8.0`, Godot 4.7's baseline. .NET 8 support ended in November 2026, so revisit the target framework at a milestone boundary.
- "Footprint" is also the code name (solution, assemblies, namespaces). A different store title later doesn't require renaming code.
- Single-player at launch. A 1v1 online race mode may come later, so keep the sim structured to allow it (see the architecture rules).
- Release: closed Steam Playtest, free prologue demo at a Steam Next Fest, then a full 1.0 release (no Early Access). Steamworks.NET for overlay, achievements, cloud saves and rich presence; develop against test App ID 480.
- Visuals: stylized interface with stylized network and city maps, framed by a 3D hideout with a third-person view of the player's character.
- Protagonist: handle "Morrow", man or woman, appearance configurator, six skill branches. Key story moments voiced by human actors.
- Morrow's real name is redacted everywhere (a bar in text, a glitch in voice) until the final scenes. Every text source and voiced line must render the name through a real-name tag that one story flag can unredact; never hard-code the name.
- Solo, part-time developer.

## Architecture rules

- The simulation is a plain .NET class library (`src/Sim`) with no Godot references. Godot (`game/`) reads sim state and sends commands; it never mutates sim state.
- Commands are the only input to the sim: the player, the rival AI, tests and any future online opponent share one command path.
- Keep truth (what is really there) separate from player knowledge (what the player has revealed). The UI reads only the player's knowledge.
- Use integers for game quantities (money in cents, time in ticks, probabilities in basis points); floats only in presentation.
- One seeded RNG per mission and one for contract generation, so a seed plus a command list reproduces a run exactly.
- Fixed sim tick; speed controls change ticks per real second, pause runs none.
- Content (operations, assets, skill branches, target templates) is data, not code.
- Campaign and mission state serialize to a versioned save format.

## Current state

M0 (foundations) is in place:

- `Footprint.sln` (repository root): `src/Sim`, `src/Sim.Tests` and `game/Footprint.csproj`.
- `src/Sim` (`Footprint.Sim`): `DeterministicRandom` (xoshiro256** seeded with SplitMix64; integer and basis-point rolls; saveable `RandomState`) and a placeholder `Simulation` (seed and tick count). Commands, missions, truth versus knowledge and saves start in M1.
- `src/Sim.Tests`: xUnit tests, including reference outputs for both generators.
- `game/`: the Godot project. `scenes/main.tscn` with `Main.cs` steps the sim and shows the tick; `-- --smoke-test` runs 100 ticks headless and quits with exit code 0 on success. Godot builds `game/Footprint.csproj`, which references `src/Sim`; `dotnet/project/solution_directory="../"` points the editor at the root solution.
- `.github/workflows/ci.yml`: on every push and pull request, restore, build and test the solution on Ubuntu. It doesn't download LFS files or run Godot.

## Build, run and test

Needs the .NET 8 SDK and Godot 4.7.2 (.NET edition).

```powershell
dotnet build Footprint.sln     # sim, tests and the Godot C# project
dotnet test Footprint.sln      # all tests
dotnet test src/Sim.Tests --filter "FullyQualifiedName~DeterministicRandomTests.SameSeed_GivesSameSequence"   # one test
```

Godot is installed with winget. Run its real executable, not winget's `godot` alias in `%LOCALAPPDATA%\Microsoft\WinGet\Links`: the .NET edition looks for its `GodotSharp` folder next to the path it was started from, and through the alias it crashes with ".NET assemblies not found".

```powershell
$godot = (Get-ChildItem "$env:LOCALAPPDATA\Microsoft\WinGet\Packages\GodotEngine.GodotEngine.Mono_*\Godot_v4.7.2-stable_mono_win64\Godot_v4.7.2-stable_mono_win64_console.exe").FullName
& $godot --headless --path game --import                     # first run after a fresh clone
& $godot --headless --path game --build-solutions --quit     # build the C# the way the editor does
& $godot --headless --path game -- --smoke-test              # exit code 0 = passed
& $godot --path game -e                                      # open the editor
```

## Repository conventions

- `.gitattributes` sets `* text=auto`, so Git normalizes line endings of text files to LF in the repository. Development happens on Windows, so working-copy files may be CRLF; don't commit line-ending-only diffs.
- Remote: `origin` is `github.com/b2mustang/BenPatRTS1`; the default branch is `main`.
- The working copy lives at `C:\dev\BenPatRTS1`. Keep it out of OneDrive and other synced folders: sync conflicts with Godot's `.godot/` cache, .NET `bin/`/`obj/` and `.git`.
- Git LFS stores binary art, audio, video, fonts and Godot binary resources (rules in `.gitattributes`). Before committing a new binary file type, add an LFS rule for it first.
- Commit Godot's `.uid` files next to scripts and resources; Godot uses them to keep references working when files move. `.godot/` is a cache and stays ignored.
- Planned: record every third-party asset's licence in `docs/asset-licenses.md` from the first asset onward.
