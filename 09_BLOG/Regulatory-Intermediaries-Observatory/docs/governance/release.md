# Governance and local release staging

**DRAFT — NOT VALIDATED**

Human review must determine conceptual scope, eligibility, role definitions, evidence sufficiency, adjudication, team credits, institutional representation, ownership, licenses and editorial/publication approval. Technical validation does not settle any of these. The tentative gates are conception, protocol approval, pilot, adjudication, pre-publication review and authorized release. Phase 01 implements infrastructure only; no scientific gate has been passed by implication.

There is no public export until every record in a deliberately curated database is `validated`, `public_eligible=1`, `is_synthetic=0`, with documentary links and current validation decisions as required by the validator. Each decision needs an identified coder, reviewer and rationale. Do not flip flags on synthetic material to create research data.

Obtain a fingerprint with:

```powershell
.\.venv\Scripts\python.exe -m rio validate --db data/working/curated.sqlite
.\.venv\Scripts\python.exe -m rio fingerprint --db data/working/curated.sqlite
```

A responsible human may then prepare `data/working/release-approval.json` documenting `snapshot_sha256`, `authorized_by`, `authorized_on`, `license_decision`, `rights_review`, `privacy_review`, and `scientific_review`. All review fields must contain meaningful review records, not placeholders. No filled approval is bundled. Approvals and coding identities remain internal. Approval review covers every potentially released field, including excerpts and notes. Preserve the authorization file securely with the internal audit record.

```powershell
.\.venv\Scripts\python.exe -m rio export --db data/working/curated.sqlite --public --approval data/working/release-approval.json --out data/public/approved-version
```

This command stages files locally only. The fingerprint changes when records, links, metadata or coding decisions change. No publication, Git push or Zenodo deposit is implemented. Scientific/license/privacy decisions cannot be authenticated by a local JSON file: this is an auditable workflow requiring responsible use, not a substitute for institutional access control.

The project has no selected source-code or data license. Team identities, affiliation and contact information require confirmation. Future posts follow idea → evidence note → factual/methodological review → editorial approval → dated publication → corrections archive.
