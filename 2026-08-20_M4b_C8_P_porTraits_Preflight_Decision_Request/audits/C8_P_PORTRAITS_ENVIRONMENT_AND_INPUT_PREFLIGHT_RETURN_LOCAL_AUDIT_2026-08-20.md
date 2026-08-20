# C8-P porTraits Environment And Input Preflight Return Local Audit

Date: 2026-08-20

Audited package:

```text
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/03_HPC_Returned_Result_Summaries/enzymecage_c8_p_portraits_environment_and_input_preflight_20260820.tar.gz
```

Identity sidecar:

```text
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/03_HPC_Returned_Result_Summaries/enzymecage_c8_p_portraits_environment_and_input_preflight_20260820.tar.gz.identity.txt
```

## Verdict

```text
LOCAL_AUDIT_VERDICT=C8_P1_COMPLETE_BUT_NOT_READY_FOR_PORTRAITS_SMOKE
```

The return package is structurally valid and completes the requested C8-P1
environment/input preflight. It should not be treated as approval to run
porTraits.

Data-side feasibility is strong:

```text
original 2,478 denominator preserved
322 bacteria + 90 archaea uncovered targets derived exactly
428 fungi excluded identity-only
412 / 412 C8-P targets have assembly_accession
0 target duplicates
0 fungal target rows
```

Execution-side feasibility is blocked:

```text
Nextflow missing
Docker/Singularity/Apptainer missing
porTraits model/database assets missing: 10 / 10 categories
query_metatraits=none not supported by the inspected v0.1.7 code
local genome FASTA files found for C8-P targets: 0 / 412
```

Recommended next step is **not** a phenotype prediction smoke test. The next
scientifically safe step is either:

```text
C8-P3 teacher-facing decision card / blocker report
```

or, if the user wants one more technical clarification before asking teacher:

```text
C8-P1b Chenyu global environment/asset/version resolver
```

that only searches real Chenyu module paths, shared database paths, container
support, and newer porTraits versions. C8-P1b must still not run prediction,
download genomes, or patch porTraits.

## Package Integrity

Identity check:

```text
actual archive sha256 = 5ccb5e82fbe53a3ff58f98de8e71299c32465236eb430964d86894bcd504d405
identity archive sha256 = 5ccb5e82fbe53a3ff58f98de8e71299c32465236eb430964d86894bcd504d405
sha256 match = YES
actual archive bytes = 49,581
identity archive bytes = 49,581
bytes match = YES
```

Archive structure:

```text
single_root = enzymecage_c8_p_portraits_environment_and_input_preflight_20260820
single_root_check = PASS
required output files missing = 0
MANIFEST.sha256 check = PASS
```

Required files present:

```text
README.md
FINAL_STATUS.txt
LOCAL_AUDIT_REPORT.md
COMMAND_TRANSCRIPT.txt
MISSING_INPUTS.tsv
ENVIRONMENT_REPORT.md
ENVIRONMENT_REPORT.json
PORTRAITS_VERSION_AND_CODE_AUDIT.md
PORTRAITS_CODE_CANDIDATES.tsv
PORTRAITS_SCHEMA_PARAMETERS.tsv
QUERY_METATRAITS_NONE_FEASIBILITY.md
QUERY_METATRAITS_NONE_EVIDENCE.tsv
PORTRAITS_ASSET_INVENTORY.csv
PORTRAITS_ASSET_INVENTORY_SUMMARY.md
C8_P_TARGET_UNIVERSE_SUMMARY.csv
C8_P_TARGET_SOURCES_BACTERIA_ARCHAEA_UNCOVERED.csv
C8_P_TARGET_DERIVATION_AUDIT.md
C8_P_TARGET_COUNT_MISMATCHES.tsv
GENOME_FASTA_AVAILABILITY_PREFLIGHT.csv
GENOME_FASTA_AVAILABILITY_SUMMARY.csv
GENOME_FASTA_AVAILABILITY_DRY_CHECK.md
NEXTFLOW_DRY_CHECKS.md
BLOCKERS_AND_NEXT_STEPS.md
MANIFEST.files
MANIFEST.sha256
scripts/c8_p_target_derivation_v2.py
```

## Boundary Compliance

PASS:

```text
No full porTraits prediction.
No small-sample phenotype prediction.
No bulk genome download.
No sequence-content download.
No fungi in porTraits target list.
No production D4 / production pool / formal asset mutation.
No C8 main trait_annotation mutation.
No hard rejection.
No trait_score.
No uncalibrated confidence.
No F5 prediction.
No porTraits code patching.
```

The package's own final status is:

```text
C8_P_ENV_INPUT_PREFLIGHT_BLOCKED_WITH_ACTIONABLE_GAPS
```

This final status is appropriate.

## Target Derivation Audit

Machine checks on `C8_P_TARGET_SOURCES_BACTERIA_ARCHAEA_UNCOVERED.csv`:

```text
rows = 412
unique source_signature = 412
target_bacteria = 322
target_archaea = 90
target_fungi = 0
missing assembly_accession = 0
metatraits_covered=False = 412
portraits_stage0_target_status=C8_P_STAGE0_TARGET = 412
```

Summary file matches expected teacher-denominator counts:

```text
total_denominator_rows = 2,478 / expected 2,478 / YES
target_bacteria_total = 1,897 / expected 1,897 / YES
target_archaea_total = 153 / expected 153 / YES
target_fungi_total = 428 / expected 428 / YES
metatraits_covered_total = 1,638 / expected 1,638 / YES
target_bacteria_uncovered = 322 / expected 322 / YES
target_archaea_uncovered = 90 / expected 90 / YES
total_c8_p_targets = 412 / expected 412 / YES
target_fungi_excluded_identity_only = 428 / expected 428 / YES
```

`C8_P_TARGET_COUNT_MISMATCHES.tsv` reports:

```text
NO_MISMATCHES
```

Interpretation:

```text
The data denominator and target-list part of C8-P is reliable enough to use in a
teacher-facing plan.
```

## Genome FASTA Availability Audit

Machine checks on `GENOME_FASTA_AVAILABILITY_PREFLIGHT.csv`:

```text
rows = 412
target_bacteria = 322
target_archaea = 90
assembly_accession_present=YES = 412
local_fasta_found=YES = 0
local_fasta_found=NO = 412
prior genome pilot overlap = 18
needs_download_for_later_smoke=YES = 412
```

The package reports:

```text
pilot_100_success_count = 100
pilot_100_c8_p_overlap = 18
smoke_5_success_count = 5
smoke_5_c8_p_overlap = 0
bulk_download_performed = NO
metadata_only_check_performed = NO
download_route_documented = NCBI_datasets_API_v2
```

Interpretation:

```text
Input accession coverage is excellent, but no actual FASTA inputs are available
in the execution environment. A later smoke test would need explicit approval to
download or transfer a tiny bacteria/archaea FASTA set.
```

## porTraits Code / query_metatraits Audit

The package inspected porTraits v0.1.7 from the dependency payload:

```text
version/tag = 0.1.7
git commit inferred from directory = 742d0c6
main.nf present = YES
nextflow_schema.json present = YES
nextflow.config present = YES
module files = 9
```

Direct evidence supports the package's classification:

```text
QUERY_METATRAITS_NONE_FEASIBILITY = NOT_SUPPORTED_BY_CURRENT_CHENYU_CODE
```

Reason:

```text
nextflow_schema.json defines no query_metatraits parameter.
main.nf calls metatraits_speci_call unconditionally.
metatraits.nf makes live curl calls to https://metatraits.embl.de/api/v1.
nextflow.config has no query_metatraits default.
docs/usage.md does not document query_metatraits.
```

Interpretation:

```text
The current v0.1.7 route cannot satisfy the teacher-requested
query_metatraits=none smoke without either a newer supported porTraits version
or an explicitly approved code patch.
```

## Environment / Asset Audit

Execution environment reported:

```text
hostname = 674db4f51184
user = root
pwd = /usrdata/EnzymeCAGE_data/EnzymeCAGE-master
filesystem = overlay, 100G
Python = 3.12.3
Java = OpenJDK 17.0.19
Nextflow = missing
Docker = missing
Singularity = missing
Apptainer = missing
conda/mamba = missing
SLURM = missing
```

Important caveat:

```text
This looks like a container/sandbox execution environment rather than a full
traditional Chenyu SLURM node. Therefore the absence of Nextflow/container/SLURM
is a proven fact for this run environment, but not necessarily for every shared
Chenyu module or cluster path. If needed, a C8-P1b resolver should explicitly
search module systems and shared software/database locations.
```

Asset inventory reports all required categories missing:

```text
metatraits_models = NO
BacDive-AI models = NO
GenomeSPOT models = NO
MICROPHERRET assets = NO
Traitar assets = NO
reCOGnise marker genes = NO
GTDB-Tk database = NO
eggNOG database = NO
PFAM assets/mappings = NO
container images/cache = NO
```

Interpretation:

```text
Even if target FASTA files were available, this environment cannot currently run
porTraits because core runtime and model/database prerequisites are absent.
```

## Findings

1. **Blocker: current porTraits v0.1.7 cannot run `query_metatraits=none`.**
   This blocks the exact teacher-specified smoke-test condition unless we find a
   newer porTraits version with the parameter or get explicit approval for a
   minimal skip-MetaTraits patch.

2. **Blocker: runtime stack is absent in the tested environment.**
   Nextflow and container runtime are both missing. porTraits v0.1.7 cannot run
   without resolving this.

3. **Blocker: porTraits model/database assets are absent.**
   The package found 0 / 10 required asset categories. This is likely a large
   transfer/download issue, not a small prompt tweak.

4. **Blocker: no local FASTA inputs are available.**
   All 412 targets have assembly accessions, but a later smoke still needs
   explicit authorization to download or transfer a tiny FASTA set.

5. **Caveat: environment may not represent the full Chenyu cluster.**
   Because the run environment appears containerized and has no SLURM, one more
   read-only resolver can be justified if the user believes Chenyu has modules or
   shared assets outside this container.

## Go / No-Go

```text
Proceed to porTraits tiny smoke now: NO
Proceed to small-sample phenotype prediction now: NO
Proceed to full C8-P rollout now: NO
Proceed to teacher-facing C8-P blocker/decision card: YES
Optional proceed to C8-P1b real Chenyu environment/asset/version resolver: YES
```

## Recommended Next Action

Recommended immediate next action:

```text
Write a concise C8-P3 teacher-facing decision card:
- C8-P target universe is clean and ready: 322 bacteria + 90 archaea, all with assembly_accession.
- C8-P execution is blocked by runtime/assets/query_metatraits/version.
- Ask teacher whether to close C8-P for now, authorize a C8-P1b resolver, or authorize
  a specific route to obtain Nextflow/container/assets/new porTraits version.
```

If the user wants one more technical step before teacher discussion, write a
C8-P1b resolver prompt with these limits:

```text
read-only only
search module avail / shared paths / porTraits versions / assets
do not run porTraits
do not patch code
do not download genomes
do not install software
do not use fungi
```
