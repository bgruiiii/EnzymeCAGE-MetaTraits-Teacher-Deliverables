# MetaTraits MT-D5 Accepted Evidence Resubmission Audit

Date: 2026-07-24

## 1. Verdict

```text
MT_D5_ACCEPTED_EVIDENCE_RESUBMISSION_PASS
FINAL_2026_07_16_REPORT_BYTE_IDENTITY_PASS
FIVE_FINAL_D5A2_RAW_JSON_BYTE_IDENTITIES_PASS
FIVE_JSON_STRICT_PARSE_AND_RECORD_COUNTS_PASS
NO_ROBUST_MAJORITY_RECOMPUTATION_PASS
DETERMINISTIC_TAR_AND_IDENTITY_BYTE_IDENTITY_PASS
ORIGINAL_ACCEPTANCE_AUDIT_RETAINED_PASS
NO_NEW_PROBE_OR_NETWORK_ACTIVITY_PASS
M4B_M4C_NOT_STARTED_PASS
```

## 2. Authority And Interpretation

The 2026-07-24 teacher supplement requests the D5 pre-research report and five
raw sample JSON bodies as a P0 next-round prerequisite.

Earlier authority:

```text
TEACHER_REPLY_MTD5_ACCEPTED_AND_MTD1_D8_DECISIONS_2026-07-18.md
SHA256 230d67ff1e18af34d5c4b5d736f27203bf4c060ee4854eb37b192749a7333606
```

states that MT-D5 passed, is closed and needs no further action. The
non-conflicting implementation of the supplement is therefore a byte-identical
resubmission of the accepted evidence, not a new probe.

## 3. Report Identity

Resubmitted root file:

```text
metatraits_probe_report.md
SHA256 d263ec486d7def2516633d1ac1785175202ae0cc51eca42b3332e71ab949dfa5
```

Original source:

```text
16_MetaTraits_Integration_Research_2026-07-15/
03_Reports/metatraits_probe_report.md
```

Direct byte comparison result:

```text
cmp exit 0
BYTE_IDENTICAL
```

The report names the final D5A2 package and the independent 2026-07-16
acceptance audit. It covers all four items restated in the supplement:
interface stability, wastewater-related trait coverage,
`No robust majority`, and rate-limit evidence.

## 4. Five Raw JSON Identities And Parse Check

The five resubmitted bodies were copied only from the final accepted D5A2
directory:

```text
03_HPC_Returned_Result_Summaries/
metatraits_mt_d5a2_https_handler_and_required_evidence_final_correction_20260716/
raw/metatraits/samples/
```

| Sample | Bytes | Records | No robust majority | SHA256 | Direct comparison |
|---|---:|---:|---:|---|---|
| `01_Q8EFP8` | 55,324 | 146 | 12 | `0d0eeecd9b5cd6314d71e680119b5fd155fac2980f59581436501ed2f42d0604` | identical |
| `02_Q12WS1` | 50,477 | 134 | 2 | `c3da972bb5214ef65f9631b48882dbd8eec96e2ebe0edb38901856ae96ec9e6b` | identical |
| `03_A0A0H3C8X0` | 61,707 | 161 | 24 | `99ca0fb51622ba9d30eba9befabe6e90f96750eac96f1af31f8638807479a0e5` | identical |
| `05_Q6BQK1` | 3,148 | 9 | 0 | `28b4e749f70dafba8ad5ccf5c1948ce9ce8623709959687c4ebfd718ca1f8735` | identical |
| `06_P71875` | 56,471 | 147 | 5 | `414606627724f0ada3dcbc5be618291d94378fa60b0756e9dd62741fd4faa202` | identical |

Each file parses as a strict top-level JSON list, every member is an object,
and the aggregate was freshly recomputed:

```text
records = 597
majority_label == "No robust majority" = 43
percentage = 7.202680%
```

These values match the accepted report and original audit.

## 5. Complete Package Identity

Resubmitted deterministic tar:

```text
bytes 3952640
SHA256 b5e97d92fcbcd2f09a5709af9abc886fc654fa83107ded21868138a0fc2ffe2f
direct comparison with original tar = identical
```

Resubmitted tar identity:

```text
SHA256 c13f80de394e35925632c0d642b77decd7583dec6287d430bfbb7bc4207626c2
direct comparison with original identity = identical
```

The original independent audit is also copied unchanged:

```text
ENZYMECAGE_METATRAITS_MT_D5A2_ACCEPTED_RETURN_LOCAL_AUDIT_2026-07-16.md
SHA256 124800a723e23829a17ace729e77c2efef9014e240b9de5b6ee4806df731c935
```

That audit had already checked 95 regular files, safe tar members,
deterministic reconstruction, the portable validator, five mutation tests and
the R01–R16 evidence closure.

## 6. Requirement Matrix

| 2026-07-24 supplement requirement | Resubmitted evidence | Result |
|---|---|---|
| use 5–10 hosts derived from Top-MRR P0 enzymes | report documents 10 fixed UIDs and five fixed organisms | PASS, existing accepted work |
| interface stability | report §§4.1–4.4; full accepted tar | PASS, bounded evidence |
| wastewater trait coverage | report §5; five raw bodies | PASS |
| `No robust majority` proportion | report §6; fresh raw recomputation 43/597 | PASS |
| rate limit | report §4.4: 0 observed 429, published threshold UNKNOWN | PASS with boundary |
| five original JSON bodies | five individually visible raw files with exact hashes | PASS |

## 7. Forbidden-Action Audit

```text
new metaTraits HTTP request                        not performed
new D5 probe or changed sample set                 not performed
accepted report or raw JSON edit                   not performed
production API stability claim                     absent
unlimited-rate claim                               absent
population-wide coverage claim                     absent
M4b/M4c code, schema runtime or trait filtering    not started
```
