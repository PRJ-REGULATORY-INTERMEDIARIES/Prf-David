"""Build root INPUT_MANIFEST.csv from SOURCE_REGISTER.csv and OFFICIAL_TEXT_MANIFEST.csv."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import RUN_ROOT, read_csv, write_csv  # noqa: E402

rows = []
for r in read_csv(RUN_ROOT / "01_BASELINES/SOURCE_REGISTER.csv"):
    rows.append(dict(INPUT_ID=r["SOURCE_ID"], PATH_OR_URL=r["PATH"], LOCATION=r["LOCATION"], ORIGIN="LOCAL_FILE",
                     TYPE=r["CATEGORY"], ROLE=r["ROLE"], SCHEMA_LAYER=r["SCHEMA_LAYER"], SOURCE_STATUS=r["SOURCE_STATUS"],
                     VERSION_OR_DATE=r["MTIME"], SHA256=r["SHA256"], SIZE_BYTES=r["SIZE_BYTES"], READ_STATE=r["READ_STATE"],
                     EVIDENCE_STATUS="VERIFIED_LOCAL" if r["EXISTS"] == "YES" else "MISSING"))
for r in read_csv(RUN_ROOT / "01_BASELINES/official_texts/OFFICIAL_TEXT_MANIFEST.csv"):
    rows.append(dict(INPUT_ID=f"OFF-{r['CELEX']}", PATH_OR_URL=r["REQUEST_URL"], LOCATION="ONLINE_OFFICIAL (stored copy: 01_BASELINES/official_texts/%s.html)" % r["CELEX"],
                     ORIGIN="PUBLICATIONS_OFFICE_CELLAR", TYPE="LEGAL_TEXT", ROLE=r["PURPOSE"], SCHEMA_LAYER="LEGAL_SOURCE",
                     SOURCE_STATUS="OFFICIAL_TEXT", VERSION_OR_DATE="accessed " + r["ACCESSED_AT"], SHA256=r["SHA256_HTML"],
                     SIZE_BYTES=r["BYTES"], READ_STATE="FETCHED_AND_HASHED" if r["HTTP_STATUS"] == "200" else "FAILED",
                     EVIDENCE_STATUS=r["EVIDENCE_STATUS"]))
hdr = ["INPUT_ID", "PATH_OR_URL", "LOCATION", "ORIGIN", "TYPE", "ROLE", "SCHEMA_LAYER", "SOURCE_STATUS", "VERSION_OR_DATE", "SHA256", "SIZE_BYTES", "READ_STATE", "EVIDENCE_STATUS"]
write_csv(RUN_ROOT / "INPUT_MANIFEST.csv", hdr, rows)
print(len(rows), "inputs")
