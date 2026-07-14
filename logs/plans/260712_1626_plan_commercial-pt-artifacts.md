# Plan: Commercial PT Service Artifacts

**Created**: 2026-07-12 16:26
**Updated**: 2026-07-14 10:24
**Status**: in_progress
**Slug**: commercial-pt-artifacts

## Objective

Create the 15 controlled commercial artifacts defined in `ptservice_art_prop.md` while reusing the existing PSEA QMS for all technical round operations.

## Phases

### Phase 1: Freeze offer and economics

| # | Artifact | Action | Notes |
|---|---|---|---|
| 1.1 | CS-01 | Create/approve | Freeze scope, capacity, pricing, claims and conditions |
| 1.2 | CS-04 | Create/approve | Include lifecycle, cylinder and capacity scenarios |

### Phase 2: Market and validate demand

| # | Artifact | Action | Notes |
|---|---|---|---|
| 2.1 | CS-02 | Create | Paid-service catalogue |
| 2.2 | CS-03 | Create | Annual programme and round notice |
| 2.3 | CS-05 | Create | Expression-of-interest form |

### Phase 3: Contract and confirm

| # | Artifact | Action | Notes |
|---|---|---|---|
| 3.1 | CS-06 to CS-11 | Create/test | Quote through onboarding; reuse QMS registration fields |

### Phase 4: Exceptions and closure

| # | Artifact | Action | Notes |
|---|---|---|---|
| 4.1 | CS-12 to CS-15 | Create/test | Changes, delivery, feedback and renewal |

## Cross-cutting work (added 2026-07-14)

| # | Item | Action | Notes |
|---|---|---|---|
| X.1 | QMS code renumbering reconciliation | Apply | Map blueprint + artifacts to vigente QMS codes (post-2026-06-14 renumbering) |
| X.2 | Implementation review | Complete | `logs/history/260714_0927_review-ptservice-art-impl.md` |
| X.3 | Apply 16 review improvements | Complete | 3 bloqueantes + 13 no bloqueantes |
| X.4 | Journey map | Create | `commercial_service/00_control/journey.md` |
| X.5 | QMS equivalence table | Create | `commercial_service/00_control/qms_code_equivalence.md` |
| X.6 | OWNERS.md per restricted folder | Create | `02_pricing_restricted/`, `04_enrollment_restricted/` |
| X.7 | README conventions | Update | Status markers, inline changelog rule, standard text block rule |

## Execution Log

- [x] Blueprint approved as the implementation route (2026-07-12)
- [x] 15 CS artifacts created as v0.1 PLANNED skeleton (2026-07-14 09:00)
- [x] Implementation review completed (2026-07-14 09:27)
- [x] All 16 review improvements applied; all artifacts at v0.2 DRAFT (2026-07-14 09:55)
- [x] QMS code renumbering reconciled across blueprint + artifacts (2026-07-14 09:55)
- [x] Supporting documents created: qms_code_equivalence.md, journey.md, OWNERS.md × 2 (2026-07-14 09:55)
- [x] README conventions and cross-references updated (2026-07-14 09:55)
- [ ] CS-01 approved by management (blocked on management sign-off)
- [ ] Equipment lifecycle and cylinder inputs collected (blocked on equipment inventory + maintenance history)
- [ ] CS-04 cost model populated with real data (blocked on 1.2 inputs)
- [ ] CS-02 and CS-03 narrative content drafted (blocked on CS-01 approval)
- [ ] CS-08 legal review of clauses 18 and 19 (blocked on legal counsel engagement)
- [ ] CS-10 migrated from template to operational spreadsheet (blocked on platform selection)
- [ ] Contracting workflow simulated end-to-end (blocked on Phase 1 + 2 + 3 data)
- [ ] First paid-round commercial workflow released (blocked on Phase 5 readiness)
