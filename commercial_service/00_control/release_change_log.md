# Release Change Log

**Location:** `commercial_service/00_control/release_change_log.md`
**Owner:** Service manager
**Last updated:** 2026-07-14

## Rules

- Every controlled release of a commercial artifact is recorded here. A "release" is a change that affects **multiple artifacts simultaneously** or that is significant enough to require cross-team awareness (e.g., a CS-01 rule change that propagates to CS-02, CS-06, CS-08).
- Per-artifact revisions (e.g., fixing a typo in CS-11 only) are tracked **only in the inline changelog at the bottom of the affected artifact**, not here. This avoids duplication and keeps the per-artifact history local.
- Revisions to a quote (CS-06) are tracked in `03_sales_contracting/CS-06_quotes.md` per quote family; this log records only template-level releases.
- Technical QMS document changes are logged in `docs/qms/`; this log covers only the commercial artifact layer.
- Each release row must include: release date, artifact ID(s) affected, version, change summary, author, approver, and effectivity date.

## How this log relates to the artifact register

- `00_control/artifact_register.md` lists the **current state** of each artifact (status, version, owner, location).
- This `release_change_log.md` lists the **history of releases** (cross-artifact template changes).
- For per-artifact revision history, see the inline changelog at the bottom of each artifact (last table in the file).

The two are complementary, not redundant: the register answers "what is the current state?", the log answers "what changed in this release?".

## Log

| Release date | Artifact ID(s) | Version | Change summary | Author | Approver | Effectivity |
|---|---|---|---|---|---|---|
| [FILL] | CS-01 | 0.1 | Initial draft created from MVP blueprint | [FILL] | [FILL] | Upon approval |
| 2026-07-14 | CS-01, CS-04, CS-11, CS-13 | 0.2 | QMS code renumbering reconciliation; CS-01 evidence guidance; CS-04 round-use factor + Tab 6.A + Tab 10; CS-11 onboarding pack QMS code fix; CS-13 standard report-use reminder + CS-12 link + no-reception handling | [FILL] | [FILL] | Upon approval |
| 2026-07-14 | CS-02, CS-03, CS-05, CS-06, CS-07, CS-08, CS-09, CS-10, CS-11, CS-12, CS-14, CS-15 | 0.2 | Per-artifact minor improvements: language, version, calibration dates, payment tables, consent branches, wait-list, dual authorization, anonymity, SLA, CS-05 sync. See each artifact's inline changelog. | [FILL] | [FILL] | Upon approval |
| 2026-07-14 | 00_control (new) | 1.0 | Added `qms_code_equivalence.md` and `journey.md` to support artifact readers | [FILL] | [FILL] | Immediate |
| 2026-07-14 | 02_pricing_restricted, 04_enrollment_restricted (new) | 1.0 | Added `OWNERS.md` per restricted folder | [FILL] | [FILL] | Immediate |
| 2026-07-14 | README | 0.2 | Added conventions section, QMS code mapping reference, cross-references | [FILL] | [FILL] | Immediate |
| 2026-07-14 | ptservice_art_prop.md (blueprint) | 0.2 | Section 19 updated with post-renumeración codes; new sub-section 19.1 added | [FILL] | [FILL] | Immediate |

## Pending changes

| Target date | Artifact ID | Proposed change | Owner | Blocker |
|---|---|---|---|---|
| [FILL] | CS-01 | Approve commercial rules (close all `[FILL]` markers with management sign-off) | Service manager | Management approval |
| [FILL] | CS-04 | Populate cost assumptions, lifecycle provisions, cylinder comparison, Tab 6.A benchmark derivation, Tab 10 institutional pricing | Finance / commercial | CS-01 approval; equipment inventory + maintenance history |
| [FILL] | CS-02 | Draft catalogue content (close all narrative `[FILL]` markers) | Commercial lead | CS-01 approval |
| [FILL] | CS-03 | Draft round notice for next programme | Round coordinator | Calendar confirmation |
| [FILL] | CS-08 | Legal review of clauses 18 (force majeure, dispute resolution, liability) and 19 (data protection) | Management / legal | Legal counsel engagement |
| [FILL] | CS-10 | Migrate from template to operational spreadsheet with capacity flags, FX exposure, wait-list priority | Round coordinator | CS-01 approval; CRM / spreadsheet platform selection |
| [FILL] | All | Resolve remaining `[FILL]` markers identified in review `logs/history/260714_0927_review-ptservice-art-impl.md` | Various | Sequential dependencies on CS-01 approval |
