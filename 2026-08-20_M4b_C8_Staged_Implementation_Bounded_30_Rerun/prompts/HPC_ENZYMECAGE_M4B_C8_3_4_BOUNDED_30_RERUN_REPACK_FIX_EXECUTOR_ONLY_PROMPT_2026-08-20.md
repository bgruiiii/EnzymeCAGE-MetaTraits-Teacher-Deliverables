# HPC executor-only prompt: M4b C8-3/C8-4 bounded 30 rerun repack fix

Date: 2026-08-20

Executor role: Chenyu/HPC executor only.

## Mission

Perform a **repack-only** fix for the already completed C8-3/C8-4 bounded
30-row rerun.

The prior returned package passed the core 30-row C8 validation, but local audit
found two packaging/provenance defects:

```text
1. Missing prompt-required script:
   scripts/run_c8_3_4_bounded_30_rerun.py

2. Missing dependency payload SHA256 in returned provenance:
   3e701443b70a82ac32a819999a7b69ee4540b3443ac9ecea9d1899d1bc0cef86
```

Your task is only to fix those packaging/provenance issues and regenerate the
archive/identity.

## Absolute Scope Boundary

```text
REPACK ONLY.
Do not change the 30 selected rows.
Do not replace any UID.
Do not change enzyme_uid/source_signature pairs.
Do not change trait_annotation values.
Do not change fungi identity-only policy.
Do not change validation logic except to report the repack fixes.
Do not call MetaTraits API.
Do not call BacDive API.
Do not run porTraits.
Do not run genome prediction.
Do not read raw MetaTraits TSV gzip files.
Do not read raw BacDive cache JSON files.
Do not generate enzyme assets.
Do not run ESM/GVP/P2Rank/AlphaFill.
Do not edit production code or production data.
Do not connect to production D4 / production pool.
Do not mutate formal assets.
Do not hard reject organisms.
Do not output trait_score.
Do not output uncalibrated confidence.
Do not merge the 137 delta sources into the 2,478 main universe.
```

If any operation would require changing row content, stop and return BLOCKED.

Allowed final statuses:

```text
C8_3_4_BOUNDED_30_RERUN_REPACK_FIX_COMPLETE
BLOCKED_C8_3_4_BOUNDED_30_REPACK_FIX_INPUT_MISSING
BLOCKED_C8_3_4_BOUNDED_30_REPACK_FIX_ROW_CONTENT_CHANGED
BLOCKED_C8_3_4_BOUNDED_30_REPACK_FIX_OUTPUT_PATH_EXISTS
BLOCKED_C8_3_4_BOUNDED_30_REPACK_FIX_VALIDATION_FAILED
```

Do not write COMPLETE unless all checks pass.

## Fixed Chenyu Paths

Use these variables:

```bash
TASK_ID=enzymecage_m4b_c8_3_4_bounded_30_rerun_repack_fix_20260820
CHENYU_DATA_ROOT=/usrdata/EnzymeCAGE_data
PROJECT_ROOT=${CHENYU_DATA_ROOT}/EnzymeCAGE-master
ALT_PROJECT_ROOT=/root/projects/EnzymeCAGE-master
RETURN_ROOT=${PROJECT_ROOT}/HPC_Returned_Result_Summaries
ALT_RETURN_ROOT=${ALT_PROJECT_ROOT}/HPC_Returned_Result_Summaries
RETURN_DIR=${RETURN_ROOT}/${TASK_ID}
ARCHIVE=${RETURN_ROOT}/${TASK_ID}.tar.gz
IDENTITY=${RETURN_ROOT}/${TASK_ID}.tar.gz.identity.txt
WORK_ROOT=/tmp/${TASK_ID}
```

Fresh-run rule:

```text
If RETURN_DIR, ARCHIVE, IDENTITY, or WORK_ROOT already exists, do not overwrite,
delete, reuse, or repair it. Return a small blocked package with
FINAL_STATUS = BLOCKED_C8_3_4_BOUNDED_30_REPACK_FIX_OUTPUT_PATH_EXISTS.
```

Allowed write locations:

```text
RETURN_DIR
WORK_ROOT
```

## Required Input Package

Use the prior C8-3/C8-4 bounded 30 rerun package:

```text
enzymecage_m4b_c8_3_4_bounded_30_rerun_20260820
```

Expected prior archive SHA256:

```text
b164df242fa3002c31bb71425fb83a9494efb3a3756ecfe5aaf67142a2fa3f02
```

Search paths:

```text
${RETURN_ROOT}/enzymecage_m4b_c8_3_4_bounded_30_rerun_20260820.tar.gz
${ALT_RETURN_ROOT}/enzymecage_m4b_c8_3_4_bounded_30_rerun_20260820.tar.gz
./enzymecage_m4b_c8_3_4_bounded_30_rerun_20260820.tar.gz
```

Required prior files:

```text
POLICY_MANIFEST.json
TRAIN_SET_MANIFEST.csv
trait_annotation.jsonl
C8_BOUNDED_30_INPUT_TABLE.csv
C8_INPUT_PATH_RESOLUTION_TABLE.csv
C8_VALIDATION_REPORT.json
C8_VALIDATION_REPORT.md
C8_BOUNDARY_VALIDATION_REPORT.md
C8_TRAITFILTERLAYER_CONSUMPTION_CONTRACT.md
COMMAND_LOG.txt
FINAL_STATUS.txt
MANIFEST.files
MANIFEST.sha256
```

Prior package expected status:

```text
FINAL_STATUS.txt = C8_3_4_BOUNDED_30_RERUN_COMPLETE
trait_annotation.jsonl rows = 30
TRAIN_SET_MANIFEST.csv data rows = 30
C8_BOUNDED_30_INPUT_TABLE.csv data rows = 30
```

## Required Provenance Constants

Record these exact values in the repacked outputs:

```text
prior_c8_3_4_archive_sha256 =
b164df242fa3002c31bb71425fb83a9494efb3a3756ecfe5aaf67142a2fa3f02

c8_1_rerun2_archive_sha256 =
ebae0d9ffbf1cb3cec666bba0d7a8b5562d59d0a140fe3ab06c6e1da6f094b33

c8_2a_archive_sha256 =
d2d9ba4ba94a830cd268355588ce6d8041ed2cd3eb66e615891a5313c9a70c79

c8_3_4_bounded_30_dependency_payload_sha256 =
3e701443b70a82ac32a819999a7b69ee4540b3443ac9ecea9d1899d1bc0cef86
```

The dependency payload is the small payload that carried the already uploaded
2026-08-18 C7-2 bounded 30 reference. This SHA256 must appear in:

```text
POLICY_MANIFEST.json
C8_INPUT_PATH_RESOLUTION_TABLE.csv
COMMAND_LOG.txt
identity sidecar
```

## Required Work

### Step 1: Verify prior package integrity

Validate:

```text
prior archive SHA256 matches expected
prior MANIFEST.sha256 passes
prior FINAL_STATUS is complete
prior row counts are 30/30/30
```

### Step 2: Freeze row-content hashes before modification

Before changing anything, compute SHA256 for these prior files:

```text
TRAIN_SET_MANIFEST.csv
trait_annotation.jsonl
C8_BOUNDED_30_INPUT_TABLE.csv
C8_VALIDATION_REPORT.json
C8_VALIDATION_REPORT.md
C8_BOUNDARY_VALIDATION_REPORT.md
C8_TRAITFILTERLAYER_CONSUMPTION_CONTRACT.md
```

After copying into the new return package, verify the same SHA256 values remain
unchanged for all of those files, except files explicitly allowed below.

Allowed files to modify:

```text
POLICY_MANIFEST.json
C8_INPUT_PATH_RESOLUTION_TABLE.csv
COMMAND_LOG.txt
FINAL_STATUS.txt
MANIFEST.files
MANIFEST.sha256
identity sidecar
```

Required new file:

```text
scripts/run_c8_3_4_bounded_30_rerun.py
```

Do not modify:

```text
TRAIN_SET_MANIFEST.csv
trait_annotation.jsonl
C8_BOUNDED_30_INPUT_TABLE.csv
C8_VALIDATION_REPORT.json
C8_VALIDATION_REPORT.md
C8_BOUNDARY_VALIDATION_REPORT.md
C8_TRAITFILTERLAYER_CONSUMPTION_CONTRACT.md
```

If any protected file changes, block with:

```text
BLOCKED_C8_3_4_BOUNDED_30_REPACK_FIX_ROW_CONTENT_CHANGED
```

### Step 3: Add reproducibility script

Add:

```text
scripts/run_c8_3_4_bounded_30_rerun.py
```

This script must be a faithful reproduction script or compact executable record
for the C8-3/C8-4 bounded 30 rerun. It must:

```text
document all input packages and SHA256 values
document the fixed C7-2 bounded 30 reference source
document that this is bounded rerun only, not real candidate selection
contain checks for 30 rows, 10/10/10 taxonomy, MAIN_2478, READY_FOR_C8_3
contain checks for fungi identity-only, F5 not predicted, F8/F15 red lines
not contain API calls
not contain porTraits/genome prediction calls
not contain production mutation calls
```

If reconstructing the full original script is not possible, write a
`scripts/run_c8_3_4_bounded_30_rerun.py` reproducibility script that validates
and regenerates the package from the prior inputs using the same logic. The
script must be runnable with Python 3 and must not require production access.

### Step 4: Add dependency payload SHA256 provenance

Update `POLICY_MANIFEST.json`:

```text
source_provenance.c8_3_4_bounded_30_dependency_payload_sha256 =
3e701443b70a82ac32a819999a7b69ee4540b3443ac9ecea9d1899d1bc0cef86
source_provenance.prior_c8_3_4_archive_sha256 =
b164df242fa3002c31bb71425fb83a9494efb3a3756ecfe5aaf67142a2fa3f02
```

Update `C8_INPUT_PATH_RESOLUTION_TABLE.csv`:

```text
row for c7_2_bounded_30_reference must contain dependency payload SHA256
add row for prior_c8_3_4_bounded_30_rerun archive with SHA256
```

Update `COMMAND_LOG.txt`:

```text
state this is repack-only
state protected row-content file hashes were checked unchanged
state script was added
state dependency payload SHA256 was added to provenance
```

Update `FINAL_STATUS.txt`:

```text
C8_3_4_BOUNDED_30_RERUN_REPACK_FIX_COMPLETE
```

### Step 5: Validate repack

Validate:

```text
TRAIN_SET_MANIFEST.csv data rows = 30
trait_annotation.jsonl rows = 30
C8_BOUNDED_30_INPUT_TABLE.csv data rows = 30
taxonomy distribution = 10 target_bacteria + 10 target_archaea + 10 target_fungi
same 30 enzyme_uid/source_signature pairs as prior package
protected row-content files unchanged except allowed provenance files
scripts/run_c8_3_4_bounded_30_rerun.py present
dependency payload SHA256 present in POLICY_MANIFEST.json
dependency payload SHA256 present in C8_INPUT_PATH_RESOLUTION_TABLE.csv
dependency payload SHA256 present in COMMAND_LOG.txt
dependency payload SHA256 present in identity sidecar
no raw TSV gzip included
no raw BacDive cache JSON included
no dependency payload tarball included
no __pycache__ or .pyc included
```

### Step 6: Package

Required final files:

```text
POLICY_MANIFEST.json
TRAIN_SET_MANIFEST.csv
trait_annotation.jsonl
C8_BOUNDED_30_INPUT_TABLE.csv
C8_INPUT_PATH_RESOLUTION_TABLE.csv
C8_VALIDATION_REPORT.json
C8_VALIDATION_REPORT.md
C8_BOUNDARY_VALIDATION_REPORT.md
C8_TRAITFILTERLAYER_CONSUMPTION_CONTRACT.md
COMMAND_LOG.txt
FINAL_STATUS.txt
MANIFEST.files
MANIFEST.sha256
scripts/run_c8_3_4_bounded_30_rerun.py
```

Archive:

```text
${ARCHIVE}
${IDENTITY}
```

Identity sidecar must include:

```text
archive path
archive byte size
archive sha256
created UTC time
task_id
final status
prior c8_3_4 archive sha256
c8_1 archive sha256
c8_2a archive sha256
c8_3_4 bounded 30 dependency payload sha256
row counts
protected file hash check result
validation_pass
```

## Final Response Required From Executor

Report only:

```text
FINAL_STATUS
RETURN_DIR
ARCHIVE
IDENTITY
archive sha256
whether protected row-content files remained unchanged
whether script is present
whether dependency payload SHA256 is present in all required provenance files
any blockers
```

Do not summarize biological conclusions beyond the repack fix scope.
