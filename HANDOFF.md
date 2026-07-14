# Handoff: CALAIRE-EA Commercial Release Gates

**Generated:** 2026-07-14 14:26 -05  
**Workspace:** `/home/w182/w421/calaire-ea`  
**Branch:** `main`

## Objective for the next session

Move the approved commercial proposal toward release by collecting external
evidence, obtaining institutional reviews and implementing the enrollment
tracker. Do not reopen settled commercial choices unless new evidence requires a
formal CS-01 revision.

## Start here

1. Read `logs/CURRENT_SESSION.md`.
2. Read `logs/260714_rundown.md`.
3. Use `commercial_service/00_control/CS-01_commercial_decisions.md` as the
   commercial source of truth.
4. Consult `ptservice_art_prop.md` for artifact interfaces and build order.
5. Review `logs/history/260714_1426_findings.md` and
   `logs/history/260714_1426_problems.md`.

## Verified state

- CS-01 v0.3 is approved for proposal use; market-release gates remain open.
- The offer has four blocks: CO, SO₂, O₃ and NO/NO₂.
- The indicative flat fee is COP 5,928,000 before taxes per participating
  organization for one to four blocks.
- The fee is not approved for publication and cannot be quoted below verified
  direct cost.
- One additional analyzer can be accepted without surcharge only from residual
  capacity and without displacing another organization's first position.
- Commercial templates, blueprint and QMS complaint/appeal interfaces are
  aligned.
- `git diff --check` passes.

## Remaining release gates

1. Populate CS-04 with equipment inventory, maintenance history, staff/facility
   costs and supplier quotations.
2. Verify physical capacity and the certificate, suitability and validity of the
   CO/SO₂/NOx multicomponent cylinder.
3. Obtain University finance/tax approval for billing, taxes and refunds.
4. Obtain legal approval of CS-08, especially dispute resolution and liability.
5. Implement CS-10 as a protected institutional Excel workbook.
6. Run the synthetic end-to-end workflow before publication.

## Guardrails

- University policies take precedence for payment, taxation, refunds and credit
  notes.
- Quote and invoice only in COP.
- Do not claim accreditation.
- Keep technical results out of CS-10.
- Preserve unrelated local changes; do not reset the worktree.

## Suggested skills

- `xlsx`: build and validate the protected CS-10 workbook when explicitly
  requested.
- `doc-coauthoring`: coordinate institutional wording after legal feedback.
- `grill-with-docs`: resolve any new decision that arises from cost, legal or
  technical evidence.
- `saver`: refresh session memory after the next material milestone.

