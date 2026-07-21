# MetaTraits M4a-3A Portable Validator And Transport Final-Correction Local Audit

Date: 2026-07-20

Status: `PASS_M4A3_IMPLEMENTATION_AND_OFFLINE_TEST_STAGE_LOCALLY_ACCEPTED`

Scope: MetaTraits M4a-3/M4a-3A only. This audit does not close full M4a, does
not authorize M4b or M4c, and does not replace the pending teacher, maintainer
or GPU-integration decisions.

## 1. Authority And Audited Artifacts

Primary teacher authority:

```text
00_Authority_Teacher_Plan/
TEACHER_REPLY_MTD5_ACCEPTED_AND_MTD1_D8_DECISIONS_2026-07-18.md
```

Frozen M4a-3 placement contract:

```text
16_MetaTraits_Integration_Research_2026-07-15/02_Planning/
M4A2D_ADRMATS_MODULE_IMPORT_SCHEMA_TEST_PLACEMENT_CONTRACT_2026-07-19.md
```

M4a-3A correction prompt:

```text
07_HPC_Prompts/
HPC_ENZYMECAGE_METATRAITS_M4A3A_CHENYU_PORTABLE_VALIDATOR_AND_TRANSPORT_FINAL_CORRECTION_EXECUTOR_ONLY_PROMPT_2026-07-20.md
```

Audited three-part return:

```text
03_HPC_Returned_Result_Summaries/
metatraits_m4a3a_portable_validator_transport_final_correction_20260720/

03_HPC_Returned_Result_Summaries/
metatraits_m4a3a_portable_validator_transport_final_correction_20260720.tar

03_HPC_Returned_Result_Summaries/
metatraits_m4a3a_portable_validator_transport_final_correction_20260720.tar.identity.txt
```

Declared final token:

```text
M4A3A_READY_PORTABLE_VALIDATOR_AND_TRANSPORT_FOR_LOCAL_AUDIT
```

## 2. Findings

No blocking or major finding remains after independent local verification.

### Non-blocking transfer-mode note

The separately copied local directory has mode `0644` for
`scripts/validate_m4a3_package.py`, while the tar stores the required `0755`.
Every regular file's bytes in the directory match the corresponding tar member.
This is consistent with executable-bit loss during directory transfer, not with
a defect in the canonical archive.

The tar is therefore the authoritative deployment/audit artifact. Do not deploy
from the directly copied directory without restoring modes; extract the audited
tar instead. The tar's member modes and its deterministic reconstruction both
passed independently.

## 3. Three-Part Identity Closure

The external identity claims were independently recomputed:

```text
tar bytes: 819200
tar SHA256: 7f213605f1aed7065bdda256a6b33955e64f8cabb547a597e5ac8e74be766f87
tar members: 131
single root: metatraits_m4a3a_portable_validator_transport_final_correction_20260720

manifest bytes: 11208
manifest SHA256: cc88cf2eb8d3c93ce3617e600a743f5cf10579fda2c0882cf3e00dab9321ff3a
manifest-listed regular files: 93
package regular files including manifest: 94
```

All values match the external identity file. The final token also matches
`FINAL_STATUS.txt`, `M4A3A_CORRECTION_REPORT.md` and the validator result.

## 4. Tar Safety And Determinism

Every tar member was inspected before extraction. Results:

```text
absolute or parent-traversal paths: 0
backslash aliases: 0
duplicate member names: 0
links/devices/FIFOs/sockets: 0
multiple roots: 0
unsorted members: 0
nonzero mtime: 0
nonzero UID/GID: 0
nonempty owner/group names: 0
files with wrong tar mode: 0
directories with wrong tar mode: 0
tar/directory regular-file byte mismatches: 0
```

The tar contains 94 regular files and 37 directories. The validator script is
`0755`, ordinary files are `0644`, and directories are `0755`.

After safe extraction, a new Python `tarfile.USTAR_FORMAT` archive was generated
from sorted members with the same normalized metadata. The rebuilt tar was
byte-for-byte identical to the returned tar:

```text
rebuilt bytes: 819200
rebuilt SHA256: 7f213605f1aed7065bdda256a6b33955e64f8cabb547a597e5ac8e74be766f87
byte-identical reconstruction: PASS
```

This closes the deterministic-packaging and reverse-transport gate.

## 5. Package Integrity

The tar-extracted package passed:

```text
MANIFEST.sha256: 93/93 entries present and hash-matching
manifest missing entries: 0
manifest unlisted entries: 0
manifest duplicate paths: 0
strict JSON: 23/23
CSV structural parse: 2/2
links or other special filesystem objects: 0
files larger than 2 MiB: 0
cache/bytecode members: 0
```

The source ZIP, input payload and wrapper schema independently match:

```text
ADRMATS ZIP bytes/SHA256:
1040341 / dc33c60b6876fed6969dc56a28a688077b17ef2f5a3510fadd78f085e13834b2

ADRMATS ZIP members/files/directories/uncompressed bytes:
264 / 233 / 31 / 3323348

M4a-3 input payload bytes/SHA256:
348160 / 83e5d167bd0012ca43fec0480f2ed19bd359b50e9d925ef50403d54bc5403704

wrapper schema SHA256:
a27f33adf78bb2c7a9961d4372cfea0f7728ca91eb89e3b0a6cc7a1e6488fc35
```

## 6. Frozen Scientific Implementation

All 34 files under corrected `source/microbe_crew/` were compared against the
prior M4a-3 return:

```text
path sets equal: PASS
regular-file count: 34/34
all file SHA256 values equal: PASS
fixture directory equal: PASS
snapshot draft equal: PASS
scientific implementation changes in M4a-3A: 0
```

The prior patch was already independently replayed against the pinned ADRMATS
ZIP and produced the same 34-file tree. The 233 pre-existing ADRMATS files
remain byte-identical to the frozen baseline.

Therefore M4a-3A changed only validator, evidence and transport surfaces; it did
not alter enzyme-to-organism mapping, aggregation, fixtures or scientific
claims.

## 7. Portable Validator

The tar-extracted, unmodified validator was run locally with explicit paths to
the independently held source ZIP, input tar, wrapper schema, reconstructed
source root and baseline root. The package's legacy execution-contract paths
remained Chenyu paths and were not rewritten.

Result:

```text
VALID:M4A3_PACKAGE:phase=packaged:
status=M4A3A_READY_PORTABLE_VALIDATOR_AND_TRANSPORT_FOR_LOCAL_AUDIT

exit: 0
```

This independently proves that explicit overrides take precedence and the
validator is no longer tied to the Chenyu absolute paths.

An independently supplied absent source ZIP produced no traceback and returned:

```text
M4A3_VALIDATION_ERROR:source_zip_external_missing:<local absent path>
exit: 1
```

## 8. Independent Negative Tests

The twelve required mutations were recreated locally rather than accepted only
from returned CSV claims:

| Mutation | Required rejection | Local result |
|---|---|---|
| Absent source ZIP | `source_zip_external_missing` | PASS |
| Wrong source ZIP hash | `source_zip_external_identity` | PASS |
| Invalid ZIP format | `source_zip_bad_zip` | PASS |
| Absent input tar | `input_tar_external_missing` | PASS |
| Wrong wrapper schema | `wrapper_schema_external_identity` | PASS |
| Absent baseline root | `baseline_root_invalid` | PASS |
| Changed pre-existing source | `preexisting_source_mismatch` | PASS |
| Changed frozen fixture | `fixture_identity_mismatch` | PASS |
| Removed BaseAPITool inheritance | `inheritance_mismatch` | PASS |
| Added confidence field | `prohibited_field` | PASS |
| Collapsed P76113 multiplicity | `kegg_multiplicity_semantics` | PASS |
| Reversed equal-count order | `aggregation_order_mismatch` | PASS |

Independent result:

```text
12/12 rejected
12/12 matched intended stable reason
unexpected pass: 0
traceback/non-deterministic failure: 0
```

This matches the returned `m4a3a_negative_tests.csv` and raw stderr evidence.

## 9. Core Regression

Returned Chenyu evidence:

```text
pytest: 15 passed, 0 failed, 0 skipped, exit 0
compileall: exit 0
```

The tar-extracted source was also rerun locally in the reconstructed ADRMATS
environment. Because the local host lacks real torch while the authoritative
wrapper package eagerly imports it, the same previously documented import-only
placeholder was used solely to reach `RankedEnzyme`; no tensor, model,
checkpoint, CUDA or prediction API was available or called.

Local result:

```text
15 passed in 2.35 s
```

The real torch-environment integration remains evidenced by the Chenyu 15/15
log. The local run independently closes all M4a mapping, aggregation, fixture,
retry, cache, rate-limit, singleton, CrewAI and wrapper-field semantics.

## 10. Requirement Verdict

| Requirement | Result |
|---|---|
| Reviewed UniProt primary evidence | PASS |
| TrEMBL excluded | PASS |
| NCBI taxon production key | PASS |
| KEGG independent `0/1/N` | PASS |
| No confidence float | PASS |
| Default count-descending/numeric-taxon ordering | PASS |
| Sparse Q6BQK1 retained without fabricated traits | PASS |
| BaseAPITool/retry/rate/cache/singleton/CrewAI | PASS |
| Frozen 10-UID evidence | PASS |
| 233-file ADRMATS baseline equality | PASS |
| 34-file scientific source freeze | PASS |
| Portable independent validator | PASS |
| Twelve semantic negative tests | PASS |
| Deterministic tar and external identity | PASS |
| Complete A/B/C comparison | `WAIT_TEACHER` |
| Snapshot contract approval | `WAIT_TEACHER` |
| 100-warm/concurrency/VRAM | `NOT_RUN_IN_CPU_STAGE` |
| M4b/M4c | `NOT_AUTHORIZED` |

## 11. Final Verdict And Remaining Boundaries

Final local verdict:

```text
M4A3A_CORRECTION_ACCEPTED
M4A3_IMPLEMENTATION_AND_OFFLINE_TEST_STAGE_LOCALLY_ACCEPTED
M4A_FULL_CLOSURE_NOT_REACHED
M4B_M4C_NOT_AUTHORIZED
```

The following remain open and must not be silently closed:

```text
MT-TQ-01  teacher-defined complete A/B/C formulas and tie-breaks
MT-TQ-02  teacher approval/amendment of SNAPSHOT_CONTRACT_DRAFT.md
MT-TQ-03  teacher review of the unsent maintainer inquiry
MT-EQ-01  maintainer API/versioned-snapshot facts
MT-TQ-04  final checkpoint strategy after 100-warm/concurrency/VRAM evidence
```

This return requires no additional M4a-3 correction. Preserve the tar, external
identity and this audit together as the accepted M4a-3 evidence set. Any next
HPC action must remain inside the separately authorized later M4a integration
evidence and must not begin M4b or M4c.
