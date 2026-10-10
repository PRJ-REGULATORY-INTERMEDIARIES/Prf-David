# R4 Workspace Structure

This workspace is additive. Historical R1–R3 directories remain in place and are not reorganized.

```text
R4_CROSS_DOMAIN_VALIDATION/
├── 00_protocol/
│   ├── PROTOCOLO_USO_IA_R1_R3_PRE_R4_v1_1.docx
│   ├── R4_INITIAL_SETUP_PROMPT_VERBATIM.txt
│   └── R4_WORKSPACE_STRUCTURE.md
├── 01_baseline/
│   ├── R3_ORIGINAL/              # frozen copies of inherited R3 artifacts
│   │   ├── governance/
│   │   ├── final_package/
│   │   └── communications/
│   └── R4_WORKING_REFERENCE/     # copies used by R4; never overwrite R3_ORIGINAL
├── 02_sources/                   # fresh GDPR, DSA and AI Act sources, later phase
├── 03_extraction/                # structural extraction only, later phase
├── 04_coding/                    # independent R4 coding, later phase
├── 05_mechanisms/                # mechanism candidates and traces, later phase
├── 06_validation/                # structural and substantive QA
├── 07_comparison/                # post-lock comparisons only
├── 08_reports/                   # phase reports
├── 09_logs/                      # execution, escalation and provenance logs
└── 10_adjudication/              # human decisions after independent coding
```

The initial setup populates only `00_protocol`, `01_baseline`, the corpus register, and the two model logs. No digital legal text or substantive digital coding is placed in the workspace at this stage.
