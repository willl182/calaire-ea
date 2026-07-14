# Access Control — `02_pricing_restricted/`

**Folder:** `commercial_service/02_pricing_restricted/`
**Classification:** RESTRICTED
**Owner:** Finance / commercial
**Last updated:** 2026-07-14

## Files in this folder

| File | Classification | Read access | Write access |
|---|---|---|---|
| `CS-04_cost_price_model.md` | RESTRICTED — internal cost & margin | Finance, commercial lead, service manager, management | Finance + commercial lead (dual authorization for any change) |
| `approved_price_lists.md` | Customer-facing — published | Public (after approval) | Finance + commercial lead (dual authorization) |

## Why this folder is restricted

- `CS-04_cost_price_model.md` contains the **internal cost buildup**, **margin targets**, **lifecycle provision by asset**, **cylinder strategy cost comparison**, and **break-even scenarios**. Disclosure to participants or competitors would expose CALAIRE-EA's commercial position and could compromise future pricing.
- The customer-facing `approved_price_lists.md` is published only after the values in `CS-04` are approved by management; the cost and margin data is never published.

## Access procedures

- **Read access** is granted to: finance team, commercial lead, service manager, management. Other roles (round coordinator, technical staff) may request read access on a need-to-know basis, recorded in the audit log.
- **Write access** requires dual authorization: a proposed change is drafted by one role and approved by the other (finance or commercial lead). Both signatures appear in the inline changelog of the affected file.
- **No export** of `CS-04_cost_price_model.md` content to external systems (email, customer-facing documents, third-party SaaS) without explicit management approval documented in the file's inline changelog.
- **Versioning** of both files is tracked in `00_control/release_change_log.md` plus each file's inline changelog.

## Audit

- Any read or write of `CS-04_cost_price_model.md` should be logged in the institutional access-log system.
- Quarterly review: finance and commercial lead verify that access lists are current.

## Related artifacts

- `00_control/CS-01_commercial_decisions.md` — pricing objective and rules.
- `00_control/release_change_log.md` — release history.
- `docs/qms/` — does not contain equivalent cost data; commercial costs are not duplicated in the QMS.
