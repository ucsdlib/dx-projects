# Test Report: S01 clarity rerun (round 2)

## Run Metadata

- Date: 2026-11-24
- Tester: orchestrating session via fresh delegated session
- Skill version: installed `annotated-bibliography` with 2026-11-24 Plain-Language Rules and restructured landscape template
- Model: `api-glm-5.3-flash` (reasoning effort: high)
- Harness: TritonAI / Codex
- Session type: Fresh session, explicit invocation
- Scenario card: `scenarios/S01-clarity.md`
- Observability: full thread activity logs + manifest + raw search/verification files

## Full Transcript

See `transcripts/2026-11-24-run02-explicit-invocation-s01-full.md`.

## User-Perspective Clarity Checklist

| Check | Result | Evidence |
| --- | --- | --- |
| Jargon audit | **Pass** | No internal vocabulary in any turn. "The broader overview still helps with context" (Turn 2) replaces round 1's "everything from the landscape stays valid." No PNX, manifest, tier, or fidelity language. |
| Interpretation-first opening | **Pass** | Turn 1: "I'm treating this as a request for an initial overview of how social media relates to mental health among college students..." Turn 2: "I'm narrowing this to social media, sleep, insomnia..." No bookkeeping openers. |
| Consequence-based transparency | **Pass** | "Most summaries are based on article abstracts rather than full texts, so treat them as orientation rather than final evidence" (Turn 1); "read the full texts before you cite them in the capstone" (Turn 3). No API mechanics anywhere. |
| Estimates, not false precision | **Pass** | "screened about 140 records, selecting 34 scholarly articles and reviews." No reliability narration. |
| Next-step clarity | **Pass** | Every turn ends with concrete options; Turn 3's verification checklist is directly actionable for a capstone. |
| Trust support | **Partial** | Turn 3's ordinary-vs-problematic-use, outcome-definition, and cross-sectional-vs-longitudinal checks give the persona real discrimination tools. But Turn 2's reading list carries no access levels, confidence ratings, or study designs, so within that list the persona cannot tell well-supported from provisional. |

## Round-1 Comparison (same turns, same persona)

| Doug's note from round 1 | Round 2 result |
| --- | --- |
| Primo API transparency note in user text | Fixed. No API mechanics anywhere. |
| "Unreliable API counts" emphasis | Fixed. Estimates only. |
| "Prepared but not executed" mechanics | Fixed. Search summary is user-facing. |
| "Manifest updated and still valid" opener | Fixed. Silent bookkeeping; file links at end. |
| "Landscape stays valid" jargon | Fixed. "The broader overview still helps with context." |
| No overview intro / theme structure questions | Partially fixed — see workflow findings. |

## Evaluation Checklist

| Dimension | Result | Evidence or note |
| --- | --- | --- |
| Activation | Pass | Explicit invocation honored. |
| Intake | Pass | Interpretation-first; no clarifying questions needed. |
| Task quality | Pass | 7 themes with accurate one-line characterizations; narrowing answered the roommate's question with an honest pathway-not-causation framing. |
| Workflow compliance | **Partial** | Backend was solid (7 queries, 140 screened, per-DOI Crossref verification, validated manifest). But the user-facing output under-delivered the restructured template: themes are bolded bullets rather than headings; no folded questions; no find-more links; one example reading per theme; Turn 2's reading list omitted the annotation block entirely (no citations beyond linked titles, source IDs, study designs, access levels, confidence, or quotes). |
| Reference or tool use | Pass | Manifest validated; raw PNX pages, screening inventory, and Crossref verification files saved. |
| Accuracy and boundaries | Pass | Pathway-vs-causation framing; cross-sectional caveats; Turn 3 correctly distinguishes sleep quality vs insomnia severity vs ordinary vs problematic use. |
| Safety, privacy, and ethics | Pass | No issues. |
| Audience and accessibility | **Pass (improved)** | Dramatically more readable than round 1 for the persona; every sentence a psychology undergraduate would understand on first read. |
| Voice and style | Pass | Plain, warm, faithful. |
| Trust and verification | **Partial** | Turn 3 is excellent; Turn 2's list gives the persona no way to see evidence strength per source. |
| Efficiency | Mixed | Turn 1 took ~16.5 min (vs ~3 min in round 1) while presenting less — the depth went into backend screening that the compact response doesn't surface. |
| Follow-up handling | Pass | Prioritization with reasons; concrete double-check list; correct premise handling. |
| Release readiness | Partial | Clarity contract works; required evidence elements need protection from the compression the new rules unintentionally encouraged. |

## Strengths

- All five of Doug's round-1 language notes are fixed in live behavior, not just in the template.
- The clarity gain is large: the round-1 landscape required developer translation; this one reads like a person.
- Backend rigor actually increased (140 records screened, per-DOI verification files) — the problem is surface, not substance.

## Issues and Severity

- **High:** Required evidence elements vanished from user-facing output. The reading-list template's annotation block (access level, confidence, study design, source IDs, quotes) was entirely absent in Turn 2, and the landscape's theme headings, folded questions, and find-more links were absent in Turn 1. Hypothesis: the new Plain-Language Rules read as "compress everything," and the model resolved template richness vs. plain language by dropping structure. Plain language was meant to govern wording, not structure.
- **Moderate:** Efficiency/visibility mismatch — a 16.5-minute run presented less than round 1's 3-minute run. The screening depth is real but invisible; the persona gets no sense of the effort behind the overview (relevant to the phase 3 expectation-signaling work).
- **Minor:** Turn 3's checklist is excellent but draws less on actual run state than round 1's (no per-source provisional flags like round 1's unverified Kok et al. callout).

## Improvement Ideas

1. Add an explicit Plain-Language Rules clause: "Plain language governs wording, not structure. Required template elements — theme headings, folded questions, find-more links, representative readings, and in reading lists the full annotation block (citation, access level, confidence, study design, quotes) — are never omitted for brevity."
2. Reconsider whether the compact "screened ~140, selected 34" line should also carry a plain-language effort/expectation note, connecting to the phase 3 signaling work ("this overview reflects a fairly thorough search pass").
3. For Turn-3-style follow-ups, require at least one run-state-specific verification flag (provisional sources, verification gaps) so trust support stays tied to the actual run.

## Recommendation

- [x] Revise the skill (protect required elements from compression), then rerun S01 to confirm both clarity and structure hold.
