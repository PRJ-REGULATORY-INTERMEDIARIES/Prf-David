"""Size/mtime snapshot of every project file outside .git and outside this run folder (preservation test)."""
import os, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import RUN_ROOT, PROJECT_ROOT, write_csv  # noqa: E402

out = sys.argv[1]
rows = []
for root, dirs, files in os.walk(PROJECT_ROOT):
    dirs[:] = [d for d in dirs if d != ".git" and Path(root, d).resolve() != RUN_ROOT.resolve()]
    for fn in files:
        p = Path(root, fn)
        st = p.stat()
        rows.append([p.relative_to(PROJECT_ROOT).as_posix(), st.st_size, int(st.st_mtime)])
rows.sort()
write_csv(RUN_ROOT / "00_ADMIN" / out, ["PATH", "SIZE", "MTIME_EPOCH"], rows)
print(len(rows), "files")
