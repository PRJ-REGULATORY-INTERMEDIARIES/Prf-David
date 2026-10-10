"""Independent access audit of a subagent transcript: inspects ONLY tool_use inputs (paths/commands), never tool results or analytical text."""
import json, re, sys, collections
tp, cid = sys.argv[1], sys.argv[2]
ROOT = "g:/meu drive/prj-david/prf-david/"
ALLOW = [ROOT + "new test 3x3/11_rgam_protocol_freeze/rgam_paired_", ROOT + "new test 3x3/11_rgam_protocol_freeze/rgam_case_output_schema.md", ROOT + "new test 3x3/11_rgam_protocol_freeze/rgam_blindness_and_access_policy.md",
         ROOT + "new test 3x3/11_rgam_protocol_freeze/rgam_execution_gap_decisions_v1_0.md", ROOT + "new test 3x3/11_rgam_protocol_freeze/capsules/" + cid.lower() + "/", ROOT + "new test 3x3/12_rgam_case_execution/" + cid.lower() + "/"]
FORBID = ["09_v8", "v8_active", "v8_comp", "r4_cross", "envio_r4", "relational_leximetrics", "autonomous_rotem", "codex_rotem", "before_r2", "enviados", "comparative_pilots", "work_2_1",
          "/logs/", "01_case_universe", "02_comparability", "03_domain", "04_ranking", "05_selection", "06_paired", "08_strict", "07_common", "rgam/pilot", "rgam/paper", "rgam/ontology", "rgam/theory", ".claude/", "memory", "claude.md", "settings"]
other_caps = ["rgam_c1_scf", "rgam_c2_cbam", "rgam_ai_ai_act", "rgam_o_dir_86_361"]
calls = collections.Counter(); flagged = []; paths_seen = set()
def norm(s): return s.replace("\\", "/").lower()
for line in open(tp, encoding="utf-8"):
    try: o = json.loads(line)
    except Exception: continue
    msg = o.get("message") or {}
    content = msg.get("content")
    if not isinstance(content, list): continue
    for c in content:
        if isinstance(c, dict) and c.get("type") == "tool_use":
            calls[c.get("name")] += 1
            inp = c.get("input") or {}
            strings = [str(v) for k, v in inp.items() if isinstance(v, (str, int)) and not (c.get("name") in ("Write", "Edit") and k in ("content", "new_string", "old_string"))]
            blob = norm(" ".join(strings))
            # explicit file paths
            for k in ("file_path", "path", "notebook_path"):
                if k in inp:
                    p = norm(str(inp[k])); paths_seen.add(p)
                    if p.startswith("g:/") and not any(p.startswith(a) for a in ALLOW):
                        flagged.append((c.get("name"), "PATH_OUTSIDE_ALLOWLIST", p[:160]))
            for f in FORBID:
                if f in blob and not (f == "memory" and False):
                    flagged.append((c.get("name"), "FORBIDDEN_TOKEN:" + f, blob[:160]))
            for oc in other_caps:
                if oc != cid.lower() and oc in blob:
                    flagged.append((c.get("name"), "OTHER_CAPSULE:" + oc, blob[:160]))
            if c.get("name") in ("Bash", "PowerShell", "Glob", "Grep"):
                # absolute paths in commands that are outside allow-list
                for m in re.findall(r"g:/meu drive/prj-david/prf-david/[^\s'\"]*", blob):
                    if not any(m.startswith(a.rstrip("/")) or a.startswith(m) for a in ALLOW):
                        flagged.append((c.get("name"), "CMD_PATH_OUTSIDE", m[:160]))
print("tool calls:", dict(calls))
print("distinct file_path/path args:", len(paths_seen))
print("FLAGGED:", len(flagged))
seen = set()
for f in flagged:
    if f not in seen:
        seen.add(f); print(" ", f)
