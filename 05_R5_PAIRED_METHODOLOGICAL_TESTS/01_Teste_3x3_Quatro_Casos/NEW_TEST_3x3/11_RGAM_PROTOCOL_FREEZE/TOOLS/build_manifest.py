"""Writes RGAM_PROTOCOL_FREEZE_MANIFEST.csv (every file in the freeze directory except the manifest and its hash file) and the manifest SHA-256 file."""
import csv, hashlib, os

FREEZE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SELF = {"RGAM_PROTOCOL_FREEZE_MANIFEST.csv", "RGAM_PROTOCOL_FREEZE_MANIFEST_SHA256.txt"}
ROLE = {
    "RGAM_SOURCE_AUTHORITY_REGISTER.md": "deliverable 1", "RGAM_PAIRED_EXECUTION_PROTOCOL_v1_0.md": "deliverable 2 (frozen method)", "RGAM_PAIRED_DATA_DICTIONARY_v1_0.md": "deliverable 3 (frozen method)",
    "RGAM_PAIRED_DECISION_RULES_v1_0.md": "deliverable 4 (frozen method)", "RGAM_PRECEDENCE_AND_CONFLICT_REGISTER.csv": "deliverable 5", "RGAM_BLINDNESS_AND_ACCESS_POLICY.md": "deliverable 6 (frozen method)",
    "RGAM_CASE_OUTPUT_SCHEMA.md": "deliverable 7 (frozen method)", "RGAM_EXECUTION_CAPSULE_REGISTER.csv": "deliverable 8", "RGAM_PROTOCOL_QA_REPORT.md": "deliverable 9", "RGAM_PROTOCOL_GATE.md": "deliverable 12",
}


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for ch in iter(lambda: f.read(1 << 20), b""):
            h.update(ch)
    return h.hexdigest()


rows = []
for dp, dn, fn in os.walk(FREEZE):
    dn[:] = sorted(d for d in dn if d != "__pycache__")
    for f in sorted(fn):
        if f in SELF:
            continue
        p = os.path.join(dp, f)
        rel = os.path.relpath(p, FREEZE).replace(os.sep, "/")
        if rel in ROLE:
            role = ROLE[rel]
        elif rel.startswith("CAPSULES/") and "/LEGAL_SOURCE/" in rel:
            role = "capsule: controlling legal source (byte copy, hash-verified)"
        elif rel.startswith("CAPSULES/") and "/OUTPUT_TEMPLATES/" in rel:
            role = "capsule: blank output template"
        elif rel.startswith("CAPSULES/"):
            role = "capsule: input metadata/readme"
        elif rel.startswith("TOOLS/"):
            role = "construction tool (case-general)"
        else:
            role = "other"
        rows.append((rel, role, os.path.getsize(p), sha(p)))
rows.sort()
mp = os.path.join(FREEZE, "RGAM_PROTOCOL_FREEZE_MANIFEST.csv")
with open(mp, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["relative_path", "role", "bytes", "sha256"])
    w.writerows(rows)
h = sha(mp)
with open(os.path.join(FREEZE, "RGAM_PROTOCOL_FREEZE_MANIFEST_SHA256.txt"), "w", encoding="utf-8") as f:
    f.write(f"{h}  RGAM_PROTOCOL_FREEZE_MANIFEST.csv\n")
print(len(rows), "files in manifest; manifest sha256", h)
