# CALAIRE-EA Commercial Service Artifacts

Folder structure for the MVP commercial artifact system that turns the existing CALAIRE-EA technical PT scheme into a contractable paid service.

## Structure

| Folder | Contents | Access |
|---|---|---|
| `00_control/` | CS-01 commercial decisions, artifact register, release change log, QMS code equivalence map, journey map | Service manager |
| `01_market/` | Catalogue, programme notice, expression-of-interest form | Commercial lead |
| `02_pricing_restricted/` | Cost model and approved price lists | Finance / commercial |
| `03_sales_contracting/` | Quotes, registrations, terms, contract reviews | Commercial lead |
| `04_enrollment_restricted/` | Tracker and confirmation / wait-list / rejection / onboarding packs | Round coordinator |
| `05_changes_finance/` | Change, cancellation and refund records | Commercial / finance |
| `06_delivery_retention/` | Report delivery, feedback, renewal | Round coordinator |

## Rules

- All artifacts source wording from `00_control/CS-01_commercial_decisions.md` or existing QMS documents in `docs/qms/`.
- No file outside `docs/qms/` is treated as the current QMS master.
- Technical round records stay in the PSEA / QMS structure under `docs/qms/`.
- `02_pricing_restricted/` and `04_enrollment_restricted/` contain cost and participant identity data: access-controlled. Per-file access may be more restrictive than folder-level; see `02_pricing_restricted/OWNERS.md` and `04_enrollment_restricted/OWNERS.md`.

## QMS code mapping (renumbering 2026-06-14)

The QMS underwent a code renumbering approved on 2026-06-14 (`docs/sgc/matriz_equivalencias_codigos_sgc_pea.md`). The commercial artifacts cite `P-PSEA-XX`, `F-PSEA-XX`, `I-PSEA-XX`, `DG-PSEA-XX` codes that may have changed meaning or number. The canonical mapping used by the artifacts is in:

- `00_control/qms_code_equivalence.md` — full equivalence table for the codes that appear in CS-01 through CS-15.

**When in doubt:** if an artifact references a `*-PSEA-NN` code, check `00_control/qms_code_equivalence.md` before opening the QMS file. The QMS is authoritative; this table is a translation aid for artifact readers.

## Phases

1. **Phase 1 — Freeze the offer (Week 1):** Approve CS-01.
2. **Phase 2 — Build price and market-facing materials (Weeks 2–3):** Complete CS-02 through CS-05.
3. **Phase 3 — Build order-to-confirmation flow (Weeks 3–4):** Complete CS-06 through CS-11.
4. **Phase 4 — Build exception and closure flow (Week 5):** Complete CS-12 through CS-15.
5. **Phase 5 — Release and pilot (Week 6):** Train users, publish CS-02 / CS-03, run first paid-round workflow.

## Conventions

- **File naming:** `CS-NN_short-name.md` (e.g., `CS-04_cost_price_model.md`). Approved files only inside the folder.
- **Versioning:** every artifact has a "Last revision" line in the header with date and summary. Substantive changes increment the version in the artifact header AND the `release_change_log.md` (one entry per release).
- **Status markers:**
  - `DRAFT` — pending approval; content may change.
  - `PLANNED` — structure only; `[FILL]` markers remain.
  - `APPROVED` — content is locked; changes require new revision.
- **Evidence guidance:** decision-level `[FILL]` markers should identify the expected evidence source (organigrama, política financiera, QMS, etc.) or point to the controlling artifact. See `CS-01_commercial_decisions.md` for the canonical example. Transaction fields in reusable forms do not require a separate evidence note for every marker.
- **QMS code references:** when citing a `*-PSEA-NN` code, add a parenthetical with the pre-renumbering code if the meaning or number changed (e.g., "`F-PSEA-04` (post-renumeración; antiguo `F-PSEA-05A`)").
- **Inline changelog:** every artifact keeps a 4-column table at the bottom (Version, Date, Approver, Notes) recording all revisions. The `release_change_log.md` is a **summary index** of releases across artifacts, not a replacement for inline changelogs.
- **Standard text blocks:** some artifacts share exact text (e.g., the "report-use reminder" in CS-01 section 9, CS-08 clause 16, and CS-13 template). If a standard block needs to change, update all instances in the same revision and note the change in the inline changelog of every affected artifact.

## Approval Gates

| Gate | Required artifacts | Approval question |
|---|---|---|
| Market release | CS-01–CS-05 | Is the offer accurate, priced, understandable and honestly positioned? |
| Quote release | CS-04, CS-06, CS-08 | Can the price and conditions be defended and accepted? |
| Order acceptance | CS-07–CS-10 | Do scope, capacity, terms and payment / PO align? |
| Technical handoff | CS-11 + QMS inputs | Can the existing round-planning process act on the confirmed order? |
| Change / refund | CS-12 | Is the financial and capacity effect documented and authorized? |
| Report delivery | CS-13 + existing QMS report approval | Is the correct controlled report going to the correct recipient? |
| Commercial closure | CS-14–CS-15 | Are feedback, revenue status and future interest recorded? |

## Cross-references

- **Journey map:** see `00_control/journey.md` for an end-to-end view of how the 15 artifacts connect.
- **Artifact register:** see `00_control/artifact_register.md` for the canonical list, owners and statuses.
- **Release log:** see `00_control/release_change_log.md` for the cross-artifact release history (template-level changes only; per-artifact revisions are in each artifact's inline changelog).
- **QMS source of truth:** `docs/qms/`. The commercial layer references, never duplicates.
- **Implementation blueprint:** `ptservice_art_prop.md` (parent document).
