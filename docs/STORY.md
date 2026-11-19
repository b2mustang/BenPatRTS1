# Footprint: Story Bible

Status: **story direction set and cast named** 2026-11-19; **mission outline drafted** (§12) · The script is still to come. Keep everything original: no characters, names, organizations or plot points from *Mr. Robot* or any other existing work.

## 1. Decisions

| # | Question | Answer |
|---|---|---|
| 1 | Premise | **The climb:** rise through Halden Bay's hacking underground; the endings ask whether you became what you once despised. |
| 2 | Protagonist | **The laid-off IT worker:** fired and blamed for a breach at Plumbline Civic Systems, left with only the laptop they never returned. |
| 3 | Rival | **The former colleague:** Splice (Julian Ashby) caused that breach, let Morrow take the blame, and is now a step ahead in the underground. |
| 4 | Supporting cast | Pawn (the Fixer), Claire Calder (the loved one), Grace Liu (the Insider), Detective Paul Hollis (the Investigator), Evelyn Harrow (the Client) and Jumper (the Crew member). |
| 5 | Key choices | Four big moments drawn from people, loyalty and the work (§8). |
| 6 | Endings | Two endings, "The Top" and "The Way Out". Your record shapes which options you have; the final choice is yours. |
| 7 | Handle | **Morrow**; real name **Elena Calder / Elias Calder**, redacted until the final scenes. |
| 8 | Tone | Grounded and tense, with dry humor. The stakes are legal, financial and personal; violence is rare and offscreen. |

## 2. Names and places

| Who or what | Name | Notes |
|---|---|---|
| Protagonist | **Morrow**: Elena Calder (woman) or Elias Calder (man) | Real name redacted until the final scenes (§5) |
| Rival | **Splice**: Julian Ashby (man) | Morrow's former colleague at Plumbline |
| The Fixer | **Pawn** (woman, in her 60s) | Never shares a real name. Runs a pawn and electronics-repair shop in the old port district, which doubles as the hardware market. From an old dockworker family; has seen every hustle in the city. |
| The loved one | **Claire Calder** | Morrow's older sister. Comes across as judgmental, but would do anything for her sibling. |
| The Crew member | **Jumper**: Dani Reyes (man, late 20s) | Hardware specialist on Pawn's repair bench. Chatty, curious, fiercely loyal; Pawn half-adopted him off the street. |
| The Insider | **Grace Liu** (woman) | An exhausted, underpaid claims processor at the M4 insurance company: who Morrow used to be. |
| The Investigator | **Detective Paul Hollis** (man) | A patient, methodical cybercrime detective, never in a hurry and always one step closer. |
| The Client | **Evelyn Harrow** (woman), **Harrow Development** | A polished, gracious property developer with political ties. |
| The company that fired Morrow | **Plumbline Civic Systems** | A government-tech contractor running Halden Bay's permits, building inspections and payments platform. |
| The city | **Halden Bay** | A booming coastal city: an old port and industrial waterfront, new tech money, glass towers going up fast, rents pushing old neighborhoods out. |

### Name check (2026-11-19)

| Name | Result |
|---|---|
| Elena / Elias Calder | No well-known character found. |
| Julian Ashby, Detective Paul Hollis | No matching characters found; "Hollis" appears only as minor TV guest roles. |
| Plumbline Civic Systems | No company by that name. Small unrelated firms use "Plumbline" (a consultancy, a plumbing contractor). Low risk. |
| Halden Bay | No city, game or novel by that name. Halden is a real Norwegian town, and "Halden City" is a fan tabletop setting. Low risk. |
| Evelyn Marsh / Marsh Holdings (dropped) | Clash: Evelyn Marsh is a *Twin Peaks* character, "Marsh" is a major insurance-broker brand, and Marsh Properties is a real, long-running family real-estate developer. Replaced by Evelyn Harrow. |
| **Evelyn Harrow / Harrow Development** | No book, film or TV character found (only an AI roleplay persona). No company named exactly "Harrow Development"; the closest are Harrow Estates (a UK land developer) and a small Scottish homebuilder, and Harrow is also a London borough. Low risk. |

## 3. Premise

Morrow kept Plumbline Civic Systems' platform running from the helpdesk, until a breach hit and Plumbline needed someone to blame. Fired and publicly named, Morrow is left with one thing: the work laptop they never handed back. With no references and no prospects, and with older sister Claire covering the rent, Morrow starts taking small jobs in Halden Bay's hacking underground. The jobs get bigger, the money gets better and the people get more dangerous. Somewhere above Morrow in that world is Julian Ashby, the former colleague who actually caused the breach, now known as Splice. Climbing toward him means becoming more like him.

## 4. Theme

**Are people disposable?** Morrow was treated as disposable by people with power. The climb rewards treating others the same way: burning an insider, abandoning a crew member, lying to the people who care. Every key choice tests whether Morrow refuses to become that or slowly does.

## 5. Morrow

- **Handle:** Morrow. Most characters use it.
- **Real name:** **Elena Calder** or **Elias Calder**, depending on the version you play, and **redacted until the final scenes** (below). Claire and, later, Detective Hollis use it at key moments.
- **Background:** helpdesk tech at Plumbline Civic Systems. Knows how organizations work from the inside: who resets passwords, which systems nobody patches, how badges and vendors work. This makes Morrow good at social and insider methods early on.
- **What Morrow despises at the start:** being treated as disposable by people with power.
- **Playable as a man or a woman**, appearance set in the configurator, voiced in key scenes by two actors.

### The redacted name

Whenever anyone says or writes Morrow's real name, it is redacted until the final scenes:

- **Text** (subtitles, emails, chats, news articles, case files, ID cards): a black redaction bar, such as "█████ Calder" or "█████ █████". *(Whether the surname "Calder" is also redacted is open; Claire's name would give it away.)*
- **Voice:** the name is masked with a short glitch or burst of static. Actors record the name clean and the mask is applied in processing, so the final reveal reuses the same performances.
- **The final scenes** reveal the name in full, in text and voice.

Why it works:

- It turns the OPSEC theme into storytelling: even the player doesn't know who Morrow really is.
- It creates a mystery the player carries through the whole campaign, paid off at the end.
- The name only has to be said clearly once, so one name per version costs little.

Implementation: every text source (dialogue, UI, documents, news) supports a real-name tag that renders as a redaction bar, with a matching audio marker in voiced lines. One story flag turns the redaction off for the final scenes.

Ideas, not decided:

- The reveal could differ by ending: in "The Way Out" Claire says the name clearly as Morrow's name is cleared; in "The Top" the Client says it, as if she owns it.
- Detective Hollis's case file sits in the hideout. As Heat rises it fills in other details (photo, address, known handles), but never the name.

## 6. The rival: Splice (Julian Ashby)

- Morrow's former colleague at Plumbline. Carried out the breach deliberately, on the Client's orders, and picked Morrow as the scapegoat.
- Now established in the underground as **Splice**, one step ahead. Races Morrow to targets in some missions and hunts Morrow in others.
- Morrow first meets "Splice" as a message (M2) and works out that Splice is Julian during their first race (M3).
- A mirror: already the person Morrow fears becoming, and charming about it.
- In "The Way Out", Morrow proves Julian caused the Plumbline breach.

## 7. Supporting cast

| Character | In the story | Gameplay tie-in |
|---|---|---|
| **Pawn** (the Fixer) | Hands out jobs, sets prices and is Morrow's way into the underground. Gruff, sarcastic and transactional; treats everyone as a piece on the board, and can become the piece that gets sacrificed. | Job board, the hardware market (her shop is on the city map), reputation gates |
| **Claire Calder** (the loved one) | Morrow's older sister. Covers the rent with commentary, disapproves of everything, and would do anything for her sibling. Doesn't know what Morrow does. | At risk when Heat rises; uses Morrow's (redacted) real name |
| **Grace Liu** (the Insider) | An exhausted claims processor whom Morrow recruits in M4. Protected or used up, depending on Morrow's choices. | Insider Networks skill branch; can testify in "The Way Out" |
| **Detective Paul Hollis** (the Investigator) | A cybercrime detective closing in on Morrow, the human face of Heat. Might offer a deal. | Heat thresholds trigger scenes; his deal is one route to "The Way Out" |
| **Evelyn Harrow** (the Client) | A polished property developer with political ties who hires Morrow for the biggest late-story jobs. Commissioned the Plumbline breach. Everything Morrow once despised, and the final temptation. | Late story missions; the route to "The Top" |
| **Jumper / Dani Reyes** (the Crew member) | A hardware specialist from Pawn's repair bench who joins Morrow for physical operations. Companionship and banter. | Acts in parallel as a field operative; can be left behind in a key choice |

## 8. Key choices

Four key choices, each placed in the outline (§12). Each decides whether an **ally** is available in the final mission.

| # | Mission | Kind | The choice | If Morrow chooses the harder path |
|---|---|---|---|---|
| 1 | M3 *Manifest* | The work | The shipment records Morrow is paid to alter hide something harmful. Finish the job, or quietly sabotage it and lose the pay. | Sabotage: Hollis later traces it and learns Morrow has limits, so **Hollis's deal** is offered in M10. |
| 2 | M6 *Counter-Trace* | People | Splice exposes Grace. Spend money and take Heat to scrub her trail, or cut her loose and let her take the fall, as was done to Morrow. | Protect: **Grace** will testify in M10. |
| 3 | M7 *Job Offer* | Loyalty | The Client wants Morrow exclusively and asks for Pawn's network as proof. Side with Pawn or hand her over. | Side with Pawn: **Pawn's network** helps in M10. If betrayed, Pawn sells Morrow out in M9, triggering a raid threat. |
| 4 | M9 *Insurance* | People | Jumper is caught during the physical break-in. Go back for him, risking the mission and Heat, or leave him. | Go back: **Jumper** joins the final mission. |

### Smaller choices

These shape dialogue, scenes and the epilogue, not which ending is available:

- Tell Claire the truth or keep lying (M5 and M8 scenes).
- Accept or refuse Splice's offer to team up against the Client (M8).
- How Morrow treats contacts and insiders in side contracts.

## 9. Endings

| Ending | What happens |
|---|---|
| **The Top** | Morrow takes over Splice's operation and becomes the Client's go-to hacker: rich, untouchable and alone, having treated people as disposable to get there. Morrow became exactly what they once despised. |
| **The Way Out** | Morrow uses everything they've built to expose the Client and prove Julian Ashby caused the Plumbline breach, clearing the Calder name. Morrow protects their people but loses the empire, and may have to accept Hollis's deal to walk away. |

### How the ending is decided

Morrow's record decides which options are open in the final mission (M10), and the player makes the last choice:

- **"The Top" is always open.** It is the easy road.
- **"The Way Out" needs at least two of the four allies** from §8: Hollis's deal, Grace's testimony, Pawn's network, Jumper's help. With fewer than two, nobody will help Morrow get out, and only "The Top" remains.
- **More allies make "The Way Out" easier:** each one unlocks extra operations or removes an obstacle in M10.
- **The smaller choices** change the epilogue: whether Claire is still in Morrow's life, and what Splice's offer cost.

## 10. Tone

- Grounded and tense, with dry humor that comes from the characters (Pawn's sarcasm, Claire's commentary, banter with Jumper), not jokes.
- The stakes are prison, ruined careers, broken trust and lost money. Violence is rare and offscreen.
- Aim for a moderate age rating.

## 11. Still open

- Whether the surname "Calder" is redacted along with the first name.
- How the name reveal plays in each ending.
- Names for mission targets: the property-management firm, the coworking building, the port logistics company, the insurance company, the private security firm, the investment firm.
- Halden Bay's districts.
- Mission titles are working titles.

## 12. Mission outline (draft)

Three acts, ten story missions, about 45 minutes each at 1×, giving 8–10 hours with time in the hideout and side contracts. The **prologue demo** is M1 and M2 plus the job board, ending on M2's cliffhanger.

### Act 1: "Nobody" (M1–M3)

Morrow is broke, blamed and invisible. The underground gives them a way to earn, and a reason to keep going.

| # | Title | Type | Target | What happens | Teaches | Introduces |
|---|---|---|---|---|---|---|
| M1 | *Severance* | Steal | A property-management firm's cloud storage | Weeks after the firing, Claire is covering Morrow's rent, with commentary. Morrow answers an anonymous job post: steal an internal memo. It's a test by Pawn, who is impressed: "Clean work. I have more." Pawn mentions that the Plumbline breach "was a professional job; whoever did it is doing very well now." | Recon, scanning, phishing, footholds, exfiltration, cleanup, Heat, time controls | Pawn and her shop, Claire, the job board (opens after M1) |
| M2 | *Tailgate* | Plant | A coworking building in the new tech district | Pawn's client wants a network implant planted inside. Morrow stakes out the lobby, clones a badge at the café next door and tailgates in. When the implant connects, Morrow finds another implant already there, carrying the same tool signature as the Plumbline breach. A message arrives from someone called Splice: "Small world. Stay out of my way." **Demo ends here.** | City map, "go to", physical operations, cameras and witnesses | Splice (by message only) |
| M3 | *Manifest* | Alter (race) | A port logistics company | Pawn double-books the job to see who's better: Morrow and Splice race to alter a shipment's records. Mid-race, Morrow recognizes Julian's old habits in Splice's work: Splice is Julian Ashby. Inside, Morrow also sees what the shipment really is. **Key choice 1.** | Racing the rival, interference moves (close the door, tip off the defenders), the Alter ending | Splice as a live opponent; Splice is Julian |

### Act 2: "Somebody" (M4–M7)

Morrow's reputation grows, and so does the number of people who depend on them, or are hunting them.

| # | Title | Type | Target | What happens | Teaches | Introduces |
|---|---|---|---|---|---|---|
| M4 | *Overtime* | Steal | A regional insurance company | A bigger job needs someone inside. Morrow recruits Grace Liu, an exhausted claims processor: exactly who Morrow used to be. Afterwards the news reports a string of breaches, and Detective Hollis is quoted. | Insider operations, the Insider Networks branch, lying low to cool Heat | Grace, Hollis (on the news) |
| M5 | *Air Gap* | Plant | A private security firm's data center | The target's crown jewel is air-gapped, too much for one person. Pawn sends Jumper from her repair bench to handle the physical side. At home, Claire notices the new money and starts asking questions (smaller choice). | Field operatives acting in parallel, air-gapped targets | Jumper |
| M6 | *Counter-Trace* | Steal (hunted) | Splice's own infrastructure | Splice goes on the offensive: tracing Morrow, burning servers and exposing Grace's identity. Morrow fights back by tracing Splice's command server and stealing his client list. Hollis visits Claire. **Key choice 2.** | Being hunted, counter-tracing, burned infrastructure and personas | Splice as a hunter |
| M7 | *Job Offer* | Alter | Halden Bay's inspections department, on Plumbline's platform | With Morrow's reputation high, Evelyn Harrow makes contact: polished, generous, and testing Morrow with a quiet job, altering an inspection report on one of her own towers. Then she asks for exclusivity, with Pawn's network as the price. **Key choice 3.** | Higher market tiers, bigger budgets, the Client's resources | Evelyn Harrow |

### Act 3: "The Top" (M8–M10)

Morrow reaches the people at the top and learns how they got there.

| # | Title | Type | Target | What happens | Teaches | Introduces |
|---|---|---|---|---|---|---|
| M8 | *Due Diligence* | Steal | A major investment firm (Harrow's competitor) | Harrow's biggest job yet: a large multi-method break-in. In the stolen files, Morrow finds the truth: Harrow commissioned the Plumbline breach to erase records of her unsafe buildings, Julian carried it out, and Morrow was the planned scapegoat from the start. Splice offers to team up against Harrow (smaller choice). Claire asks Morrow directly what's going on (smaller choice). | Everything combined; the largest network map so far | The truth about the breach |
| M9 | *Insurance* | Plant | Harrow Development's private office network | Morrow needs leverage before Harrow decides Morrow is a liability: plant a backdoor in her own systems, which requires a physical break-in at her tower. If Morrow betrayed Pawn, Pawn sells Morrow out and a raid looms. During the break-in, Jumper is caught. **Key choice 4.** | High stakes with everything on the line; raid protections matter | |
| M10 | *Tomorrow* | Leak or Steal | Harrow and Splice | The final race against Splice, with Harrow moving to bury both of them. Morrow's allies (or lack of them) decide what's possible. **Final choice:** leak the proof and walk away (**"The Way Out"**, if at least two allies are available) or take over Splice's operation and hand Harrow what she wants (**"The Top"**). In the final scenes, Morrow's real name is heard and shown unredacted for the first time. | Endings | Epilogue; Morrow's real name |

### Character threads

| Character | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Pawn | ● test job | ● | ● double-books | ● | ● sends Jumper | | ● clash | | ● (betrayal?) | ● (ally?) |
| Claire | ● rent | | | | ● questions | ● visited | | ● asks | | ● epilogue |
| Splice | | ● message | ● race; unmasked | | | ● hunts | | ● offer | | ● final race |
| Grace | | | | ● recruited | | ● exposed | | | | ● (testifies?) |
| Hollis | | | | ● news | | ● visits Claire | | | | ● (deal?) |
| Harrow | | | | | | | ● appears | ● truth | ● target | ● final |
| Jumper | | | | | ● joins | ● | ● | ● | ● caught | ● (ally?) |

### Mission types across the campaign

Steal: M1, M4, M6, M8 · Alter: M3, M7 · Plant: M2, M5, M9 · Leak: M10 ("The Way Out"); Steal: M10 ("The Top").

## Sources for the name check

- [Plumbline Consulting (CB Insights)](https://www.cbinsights.com/investor/plumbline-consulting) · [Plumbline Services (BuildZoom)](https://www.buildzoom.com/contractor/plumbline-services-plm)
- [Marsh Properties](https://platform.reverecre.com/company/marsh.properties) · [Marsh real-estate practice](https://www.marsh.com/en/industries/real-estate/expertise/developers.html)
- [Evelyn Marsh, *Twin Peaks* (TVmaze)](https://www.tvmaze.com/characters/40532/twin-peaks-evelyn-marsh)
- [Evelyn Harrow (AI roleplay persona)](https://www.shapes.inc/evelynharrow) · [Harrow Estates](https://open.endole.co.uk/insight/brand/95601-harrow-estates) · [Harrow Homes Developments](https://www.creditsafe.com/business-index/en-us/company/harrow-homes-developments-ltd-uk18832769)
- [Halden City (fan setting)](https://kaleb-one.pages.dev/masks/halden-city/meta/player-facing-doc) · [Halden, Norway (Wikipedia)](https://www.wikipedia.org/wiki/Halden)
