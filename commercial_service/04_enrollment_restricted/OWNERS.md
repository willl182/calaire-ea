# Access Control — `04_enrollment_restricted/`

**Folder:** `commercial_service/04_enrollment_restricted/`
**Classification:** RESTRICTED
**Owner:** Round coordinator
**Last updated:** 2026-07-14

## Files in this folder

| File | Classification | Read access | Write access |
|---|---|---|---|
| `CS-10_tracker.md` (the operational tracker, in practice a spreadsheet) | RESTRICTED — participant identity, commercial status, payment, capacity, FX exposure | Commercial, finance, round coordinator, service manager | Round coordinator (with commercial lead authorization for Confirmed status changes) |
| `CS-11_confirmations.md` | RESTRICTED — participant codes, contact details, payment status | Commercial, round coordinator, service manager, management | Round coordinator (with commercial lead for any change to a Confirmed record) |

## Why this folder is restricted

- `CS-10_tracker.md` (the live tracker) contains **participant identity, organization legal name, contact data, payment status, capacity consumption, and FX exposure** — all PII and commercially sensitive data. Disclosure outside the authorized team would breach Ley 1581/2012 (Habeas Data) and compromise commercial confidentiality.
- `CS-11_confirmations.md` carries the **participant code assignment** (linked to QMS codes) and the **onboarding pack contents** that include technical QMS field references; this is the bridge between commercial confirmation and the QMS round planning intake.

## Access procedures

- **Read access** is granted to: commercial team, finance, round coordinator, service manager, management. Technical staff may receive read access for specific confirmed participants on a need-to-know basis, recorded in the audit log.
- **Write access** is granted to: round coordinator (primary), with commercial lead authorization for any change to a Confirmed-status record (capacity reallocation, withdrawal processing, etc.).
- **No export** of participant identity data to external systems (personal email, third-party SaaS, paper printouts left unattended) without explicit commercial lead authorization documented in the file's inline changelog.
- **Customer marketing consent** is a separate flag in `CS-10`; data may only be used for marketing if the flag is set per the consent captured in `CS-05` and confirmed in `CS-07`.
- **Data retention:** tracker records are retained for 5 years per ISO/IEC 17043 record-retention; CS-11 records follow the same period (per CS-13 retention section).

## Cross-border data

- For international participants, the **cross-border disclosure consent** captured in CS-09 check 13 governs any data transfer outside Colombia. Without explicit consent, the report is delivered to the participant's country of registration only when that country has an adequacy decision or treaty with Colombia, OR the participant signs a separate cross-border transfer agreement.

## Audit

- Any read or write of files in this folder should be logged in the institutional access-log system.
- Quarterly review: round coordinator and commercial lead verify that access lists are current and that stale records are archived per retention policy.

## Related artifacts

- `00_control/CS-01_commercial_decisions.md` — confidentiality / disclosure rules.
- `00_control/release_change_log.md` — release history.
- `docs/qms/P-PSEA-19` (vigente) — Confidencialidad operativa interna, the QMS control that this folder aligns with.
- `docs/sgc/matriz_equivalencias_codigos_sgc_pea.md` — for code mapping.
