# ADR 0001: isolated local foundation

Date: 2026-10-09. Status: implemented technical decision; scientific definitions remain draft.

The parent directory already contains an unrelated research Git repository and existing untracked work. Create `09_BLOG/Regulatory-Intermediaries-Observatory` as a dedicated independent repository. Do not stage, ignore, import, reorganize or edit parent-project files. The supplied conception document recommends a local work directory such as C:/Research; the user's authorized location is used here for a reviewable deliverable. Google Drive may sync local files independently of Git: `.gitignore` is not an access-control mechanism. Restricted empirical collection must wait for a storage decision.

Use Python standard library + SQLite; pytest is the only direct development dependency. Use a local virtual environment and editable checkout. Quarto sources live under `website/`, as requested in the detailed bootstrap specification; this minor variation from the DOCX's root-level site keeps research and presentation separate. No frontend, cloud service, analytics, credentials, hosting config or external integration is needed.

Use a shared record identity registry to support referentially sound evidence and coding decisions. Share instruments across episodes via a linking table. Require evidence and review for validated records, while allowing incomplete candidates. Public export rejects a mixed snapshot and requires exact-content authorization; no automatic release-by-status.

No `.env.example`, LICENSE, remote, publication workflow or initial commit is created. These would imply decisions or configuration not made. A local Git repository with inspectable uncommitted files is sufficient for this bootstrap.
