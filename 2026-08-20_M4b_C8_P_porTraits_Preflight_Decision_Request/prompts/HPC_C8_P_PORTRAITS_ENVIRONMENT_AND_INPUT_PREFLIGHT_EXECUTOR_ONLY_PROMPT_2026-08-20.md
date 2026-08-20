# HPC executor-only prompt: C8-P porTraits environment and input preflight

You are running on Chenyu/HPC as an executor for EnzymeCAGE / MetaTraits. Your job
is to produce a read-only C8-P porTraits environment and input feasibility
package.

This is **not** a full porTraits run. This is **not** production. This is **not**
the C8 main staged implementation. This is the Stage 0 evidence package needed
before asking Huang-laoshi whether C8-P may proceed to a controlled smoke test.

## 0. Task Identity

```text
TASK_ID=enzymecage_c8_p_portraits_environment_and_input_preflight_20260820
RUN_TYPE=read_only_environment_and_input_feasibility_preflight
TAXONOMY_SCOPE=target_bacteria,target_archaea
EXPLICITLY_EXCLUDED_TAXONOMY=target_fungi
PREDICTION_SCOPE=none_for_this_stage
FULL_RUN_AUTHORIZED=false
PRODUCTION_AUTHORIZED=false
```

Allowed final statuses:

```text
C8_P_ENV_INPUT_PREFLIGHT_READY_FOR_TEACHER_REVIEW
C8_P_ENV_INPUT_PREFLIGHT_BLOCKED_WITH_ACTIONABLE_GAPS
C8_P_ENV_INPUT_PREFLIGHT_BLOCKED_REQUIRED_INPUT_MISSING
C8_P_ENV_INPUT_PREFLIGHT_BLOCKED_OUTPUT_PATH_EXISTS
C8_P_SCOPE_VIOLATION_ABORTED
C8_P_ENV_INPUT_PREFLIGHT_FAILED_RUNTIME_ERROR
```

Do not write a READY status unless all required reports are present and the
package contains enough evidence for a teacher-side decision about whether a
later C8-P smoke test is feasible.

## 1. Authority And Scope

Read these files before execution if they are available on Chenyu:

```text
/home/a/EnzymeCAGE/custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/NEXT_CHAT_HANDOFF.md
/home/a/EnzymeCAGE/custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/00_Authority_Teacher_Plan/老师回复8.19.md
/home/a/EnzymeCAGE/custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/00_Authority_Teacher_Plan/PORTRAITS_OFFICIAL_WORKFLOW_API_DECOUPLING_CODEX_CORRECTION_2026-08-18.md
/home/a/EnzymeCAGE/custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/01_Path_Contract_Objective/M4b_C8_TraitFilterLayer_Implementation_Plan_2026-08-19/M4B_C8_PENDING_TEACHER_DECISIONS_RESCUED_SOURCES_AND_PORTRAITS_2026-08-19.md
/home/a/EnzymeCAGE/custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/01_Path_Contract_Objective/M4b_C8_P_porTraits_Genome_Prediction_Preflight_2026-08-20/M4B_C8_P_PORTRAITS_PREFLIGHT_PATH_CONTRACT_AND_TASK_BREAKDOWN_2026-08-20.md
/home/a/EnzymeCAGE/custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/01_Path_Contract_Objective/M4b_C8_TraitFilterLayer_Staged_Implementation_2026-08-20/C8_0_Input_Source_Audit_2026-08-20/C8_INPUT_SOURCE_AUDIT.md
```

Effective teacher boundary from 2026-08-19:

```text
C8 v1 staged-only implementation is approved.
C8 v1 does not automatically start porTraits.
If MetaTraits-uncovered bacteria / archaea need porTraits, first submit a
controlled C8-P preflight plan for teacher review.
Fungi remain identity-only and must not use porTraits v1.
porTraits output, if later authorized, must be staged-only prediction evidence
with source_type = porTraits_genome_prediction.
Predicted evidence must not replace observed evidence and must not be written
as experimental fact.
```

Current denominator facts to preserve:

```text
Original C8 main universe = 2,478 source_signatures
target_bacteria = 1,897
target_archaea = 153
target_fungi = 428

MetaTraits local snapshot covered = 1,638 / 2,478
MetaTraits-uncovered target_bacteria = 322 / 1,897
MetaTraits-uncovered target_archaea = 90 / 153
target_fungi = 428 identity-only, no porTraits v1
```

## 2. Hard Boundaries

```text
READ / INVENTORY / DERIVE TARGET LIST / REPORT ONLY.
Do not run full porTraits prediction.
Do not run small-sample phenotype prediction in this Stage 0 task.
Do not run `nextflow run` unless it is a help/config/list/dry-run command that
cannot start workflow processes.
Do not download genome FASTA files in bulk.
Do not download all 322 bacteria + 90 archaea genomes.
Do not use fungi as porTraits input.
Do not predict fungal traits.
Do not call predicted traits observed, experimental, curated, or verified.
Do not write production D4.
Do not mutate production pool.
Do not mutate formal EnzymeCAGE assets.
Do not activate any snapshot.
Do not edit C8 main outputs.
Do not merge C8-P output into C8 trait_annotation.
Do not add or remove sources from the original 2,478 denominator.
Do not merge the 137 rescued-asset-linked outside-universe sources.
Do not emit hard rejection.
Do not emit trait_score.
Do not emit uncalibrated confidence.
Do not predict F5 culture collection / availability / preservation status.
Do not rewrite F8 broad degradation context as exact target-pollutant degradation.
Do not use F15 for ranking.
Do not patch porTraits code.
Do not install or modify system software unless explicitly instructed by the user
outside this prompt.
```

If any command would cross these boundaries, do not run it. Instead, record the
blocked command, the reason it would cross scope, and the exact next approval
needed.

## 3. Fresh Output Paths

Use these exact paths on Chenyu if the repository root exists there:

```text
PROJECT_ROOT=/home/a/EnzymeCAGE
RETURN_ROOT=/home/a/EnzymeCAGE/custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/03_HPC_Returned_Result_Summaries
TASK_ID=enzymecage_c8_p_portraits_environment_and_input_preflight_20260820
RETURN_DIR=${RETURN_ROOT}/${TASK_ID}
ARCHIVE=${RETURN_ROOT}/${TASK_ID}.tar.gz
IDENTITY=${RETURN_ROOT}/${TASK_ID}.tar.gz.identity.txt
WORK_ROOT=/tmp/${TASK_ID}
```

If Chenyu uses `/usrdata/EnzymeCAGE_data/EnzymeCAGE-master` as the project root,
use this compatible fallback:

```text
PROJECT_ROOT=/usrdata/EnzymeCAGE_data/EnzymeCAGE-master
RETURN_ROOT=${PROJECT_ROOT}/HPC_Returned_Result_Summaries
TASK_ID=enzymecage_c8_p_portraits_environment_and_input_preflight_20260820
RETURN_DIR=${RETURN_ROOT}/${TASK_ID}
ARCHIVE=${RETURN_ROOT}/${TASK_ID}.tar.gz
IDENTITY=${RETURN_ROOT}/${TASK_ID}.tar.gz.identity.txt
WORK_ROOT=/tmp/${TASK_ID}
```

Fresh-run rule:

```text
If RETURN_DIR, ARCHIVE, IDENTITY, or WORK_ROOT already exists, do not overwrite,
delete, reuse, or repair it.
Create a uniquely suffixed blocked return package instead and set FINAL_STATUS to:
C8_P_ENV_INPUT_PREFLIGHT_BLOCKED_OUTPUT_PATH_EXISTS
```

Allowed write locations:

```text
RETURN_DIR
WORK_ROOT
```

If helper scripts are needed, put them under:

```text
RETURN_DIR/scripts/
```

Do not write helper scripts to source-code, production-data, C8 main output, or
teacher-deliverable repositories.

## 3A. Optional Dependency Payload

If the following dependency payload was uploaded to Chenyu, unpack it into a
read-only working location and use its `inputs/` tree as the first fallback when
the fixed local paths in Section 4 are missing:

```text
enzymecage_c8_p_portraits_preflight_dependency_payload_20260820.tar.gz
enzymecage_c8_p_portraits_preflight_dependency_payload_20260820.tar.gz.identity.txt
single_root=enzymecage_c8_p_portraits_preflight_dependency_payload_20260820
```

Expected payload subdirectories:

```text
inputs/main_2478_universe/
inputs/enzyme_to_microbe_source/
inputs/metatraits_coverage_probe/
inputs/c8_0_audit/
inputs/portraits_reference/
inputs/genome_download_pilot/
```

The payload is input-dependency evidence only. It must not be treated as a
returned result package and must not be modified in place.

## 4. Fixed Inputs To Inspect

Use these exact local paths if present. If a path is missing on Chenyu, record it
in `MISSING_INPUTS.tsv` and continue with any available equivalent only if the
equivalent path is clearly documented.

### 4.1 C8 main denominator and source metadata

Primary denominator:

```text
custom/github_upload/EnzymeCAGE-MetaTraits-Teacher-Deliverables/2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/02_bacdive_full_closure/bacdive_metatraits_overlap_by_source_signature.csv
```

Expected rows and taxonomy counts:

```text
rows = 2,478
target_bacteria = 1,897
target_archaea = 153
target_fungi = 428
```

Auxiliary source table with assembly accession:

```text
custom/github_upload/reaction_enzyme_microbe_training_clean_2026-06-01/tables/enzyme_to_microbe_source.csv
```

Important columns expected:

```text
example_id
UniprotID
TaxID
organism_name
lineage
reviewed
gene_primary
proteome_id
strain_name
source_signature
source_resolution_level
mapping_confidence
assembly_accession
```

### 4.2 MetaTraits coverage probe

```text
custom/github_upload/EnzymeCAGE-MetaTraits-Teacher-Deliverables/2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/01_metatraits_species_coverage/source_signature_metatraits_coverage.csv
```

Expected columns:

```text
source_signature
taxonomy_group
source_resolution_level
uid_count
taxid
organism_name
species_name
direct_taxid_in_ncbi_all
species_name_in_ncbi_all
organism_name_in_ncbi_all
union_in_ncbi_all
union_in_ncbi_no_predictions
union_in_ncbi2gtdb
trait_count_ncbi_all
```

Boundary:

```text
This table may be used only as auxiliary coverage evidence.
It is not the 2,478 main denominator.
```

### 4.3 C8-0 local input audit

```text
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/01_Path_Contract_Objective/M4b_C8_TraitFilterLayer_Staged_Implementation_2026-08-20/C8_0_Input_Source_Audit_2026-08-20/C8_INPUT_SOURCE_AUDIT.md
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/01_Path_Contract_Objective/M4b_C8_TraitFilterLayer_Staged_Implementation_2026-08-20/C8_0_Input_Source_Audit_2026-08-20/C8_INPUT_SOURCE_AUDIT.json
```

### 4.4 Local porTraits reference snapshot

```text
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/16_MetaTraits_Integration_Research_2026-07-15/00_Raw_Downloads/porTraits-v0.1.7.zip
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/16_MetaTraits_Integration_Research_2026-07-15/01_Extracted/porTraits-v0.1.7/grp-bork-porTraits-742d0c6/
```

Known local snapshot caution:

```text
The local v0.1.7 nextflow_schema.json may not expose query_metatraits.
Do not assume query_metatraits=none works in the installed Chenyu version.
Verify from the actual Chenyu porTraits code/schema/config/main.nf.
```

### 4.5 Genome download pilot evidence

```text
data/processed/rhea/2026-01-21/microbe/genome_download_probe_2026-04-28/
```

This is only a prior pilot. It may be used to understand the historical genome
download route, but it is not proof that all C8-P targets have FASTA available.

## 5. Required Work

### 5.1 Environment inventory

Record:

```text
hostname
date with timezone
user
pwd
OS/kernel
disk free summary for project/work/output roots
available conda/mamba environments
Python version
Java version
Nextflow version
Docker availability and version
Singularity availability and version
Apptainer availability and version
SLURM availability and version if present
network policy observation based on safe metadata-only command attempts, if any
```

Do not require GPU. Do not use GPU.

Write:

```text
ENVIRONMENT_REPORT.md
ENVIRONMENT_REPORT.json
```

### 5.2 porTraits code and version inventory

Locate porTraits sources under likely roots:

```text
${PROJECT_ROOT}
/usrdata/EnzymeCAGE_data
/usrdata
/home/a/EnzymeCAGE
/tmp
```

For each candidate porTraits repo/archive found, record:

```text
path
repo_or_archive_type
git_remote_if_any
git_commit_if_any
version/tag if discoverable
README presence
nextflow_schema.json presence
main.nf presence
nextflow.config presence
module files count
contains BacDive-AI module
contains GenomeSPOT module
contains Traitar module
contains MICROPHERRET module
contains GTDB-Tk module
contains reCOGnise module
contains eggNOG mapper module
contains MetaTraits query module
SHA256 for main.nf, nextflow_schema.json, nextflow.config if present
```

Inspect, do not patch.

Write:

```text
PORTRAITS_VERSION_AND_CODE_AUDIT.md
PORTRAITS_CODE_CANDIDATES.tsv
PORTRAITS_SCHEMA_PARAMETERS.tsv
```

### 5.3 query_metatraits=none feasibility

Determine whether the actual available Chenyu porTraits version supports a
no-MetaTraits-context mode.

Use direct code evidence:

```text
nextflow_schema.json parameter definitions
main.nf conditional logic
nextflow.config defaults
docs/usage.md or README command examples
```

Classify feasibility as one of:

```text
SUPPORTED_BY_CURRENT_CHENYU_CODE
SUPPORTED_BY_OFFICIAL_REFERENCE_BUT_NOT_CURRENT_CHENYU_CODE
NOT_SUPPORTED_BY_CURRENT_CHENYU_CODE
UNKNOWN_CODE_MISSING
```

Important:

```text
If query_metatraits=none is not supported by the local Chenyu code, do not patch.
Report that a later teacher/user-approved code-version update or minimal patch plan
would be needed before any smoke test.
```

Write:

```text
QUERY_METATRAITS_NONE_FEASIBILITY.md
QUERY_METATRAITS_NONE_EVIDENCE.tsv
```

### 5.4 porTraits model/database asset inventory

Search likely roots for required assets. Record existence, path, rough size, and
evidence method. Do not download missing assets.

Assets to check:

```text
metatraits_models
BacDive-AI models
GenomeSPOT models
MICROPHERRET assets
Traitar assets
reCOGnise marker genes
GTDB-Tk database
eggNOG database
PFAM assets or mappings
container images/cache relevant to porTraits
```

For very large directories, do not compute recursive SHA256 of all files. Record
directory existence, top-level listing, file count estimate, and size summary.

Write:

```text
PORTRAITS_ASSET_INVENTORY.csv
PORTRAITS_ASSET_INVENTORY_SUMMARY.md
```

### 5.5 C8-P bacteria/archaea target inventory

Derive the C8-P target list from the original 2,478 denominator only.

Required derivation:

```text
1. Read the 2,478-row denominator file.
2. Validate row count and taxonomy counts.
3. Read the auxiliary source table with assembly_accession.
4. Read the MetaTraits coverage probe table.
5. Join by source_signature.
6. Keep source_signatures where taxonomy_group is target_bacteria or target_archaea.
7. Mark source as MetaTraits covered if union_in_ncbi_all is true in the coverage probe,
   or if the 2,478 denominator file has an explicit MetaTraits-covered indicator.
8. Select MetaTraits-uncovered bacteria/archaea targets.
9. Preserve fungi as excluded identity-only count; do not output fungi as porTraits targets.
```

Expected uncovered counts:

```text
target_bacteria_uncovered = 322
target_archaea_uncovered = 90
total_c8_p_targets = 412
target_fungi_excluded_identity_only = 428
```

If counts differ, do not force them. Report:

```text
observed counts
expected counts
join method
which file/field caused mismatch
first 20 mismatching source_signatures if available
```

Write:

```text
C8_P_TARGET_UNIVERSE_SUMMARY.csv
C8_P_TARGET_SOURCES_BACTERIA_ARCHAEA_UNCOVERED.csv
C8_P_TARGET_DERIVATION_AUDIT.md
C8_P_TARGET_COUNT_MISMATCHES.tsv
```

Required columns for `C8_P_TARGET_SOURCES_BACTERIA_ARCHAEA_UNCOVERED.csv`:

```text
source_signature
taxonomy_group
source_resolution_level
taxid
organism_name
species_name
strain_name
assembly_accession
assembly_accession_source_file
metatraits_covered
metatraits_coverage_evidence_field
portraits_stage0_target_status
notes
```

### 5.6 Genome FASTA availability dry check

For the 412 expected bacteria/archaea targets, do not download genomes. Only
classify input feasibility.

Allowed checks:

```text
Check assembly_accession presence in local source metadata.
Check whether an already existing local FASTA is present in prior genome pilot
or known Chenyu genome cache locations.
Check accepted FASTA suffixes: .fna, .fasta, .fa, .fna.gz, .fasta.gz, .fa.gz.
If safe and permitted, perform metadata-only checks for a tiny sample of at most
2 bacteria + 2 archaea, such as existing local manifest lookup or HTTP HEAD/API
metadata that does not download sequence content.
```

Forbidden checks:

```text
No bulk FASTA download.
No full 412-target download.
No sequence-content download unless a later user prompt explicitly authorizes a
tiny smoke input.
No prediction execution.
```

Write:

```text
GENOME_FASTA_AVAILABILITY_PREFLIGHT.csv
GENOME_FASTA_AVAILABILITY_SUMMARY.csv
GENOME_FASTA_AVAILABILITY_DRY_CHECK.md
```

Required columns for `GENOME_FASTA_AVAILABILITY_PREFLIGHT.csv`:

```text
source_signature
taxonomy_group
assembly_accession
assembly_accession_present
local_fasta_found
local_fasta_path
accepted_fasta_suffix
prior_pilot_evidence
metadata_only_download_route_status
needs_download_for_later_smoke
notes
```

### 5.7 Optional non-invasive Nextflow checks

Allowed:

```text
nextflow -version
nextflow help
nextflow config <porTraits_dir> if it does not start workflow processes
nextflow run <porTraits_dir> --help if it does not start workflow processes
```

Forbidden:

```text
No `nextflow run` that launches tasks.
No profile/container pull that downloads large images.
No executor submission.
No process execution.
```

Record every command and whether it was run or skipped.

Write:

```text
NEXTFLOW_DRY_CHECKS.md
```

## 6. Required Return Files

The returned folder must include:

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
```

Do not include large raw databases, genome FASTA files, container images, or raw
MetaTraits TSV gzip files inside the returned archive.

## 7. Required Local Audit Contents

`LOCAL_AUDIT_REPORT.md` must explicitly answer:

```text
Did this task avoid full porTraits prediction?
Did this task avoid small-sample phenotype prediction?
Did this task avoid bulk genome download?
Did this task exclude fungi from porTraits targets?
Did this task preserve the original 2,478 denominator?
Did this task keep the 137 outside-universe rescued sources out of the target list?
Did this task avoid production D4/pool/formal asset mutation?
Did this task avoid trait_score, hard rejection, and uncalibrated confidence?
Did this task avoid F5 prediction?
Can Chenyu currently run a later query_metatraits=none smoke without code changes?
Are all required model/database assets present?
How many bacteria/archaea targets have assembly_accession present?
How many already have local FASTA available?
What are the exact blockers before a later teacher-approved smoke test?
```

## 8. Required Packaging

At the end, create:

```text
MANIFEST.files
MANIFEST.sha256
${ARCHIVE}
${IDENTITY}
```

`MANIFEST.files` should list relative paths and file sizes for all files in
`RETURN_DIR`.

`MANIFEST.sha256` should contain SHA256 for all regular files in `RETURN_DIR`.

`${IDENTITY}` must contain:

```text
TASK_ID
FINAL_STATUS
RETURN_DIR
ARCHIVE
ARCHIVE_SHA256
ARCHIVE_SIZE_BYTES
CREATED_AT
HOSTNAME
USER
PROJECT_ROOT
```

After packaging, print these exact lines at the end of the executor response:

```text
C8_P_PORTRAITS_ENV_INPUT_PREFLIGHT_RETURN_DIR=<absolute path>
C8_P_PORTRAITS_ENV_INPUT_PREFLIGHT_ARCHIVE=<absolute path>
C8_P_PORTRAITS_ENV_INPUT_PREFLIGHT_IDENTITY=<absolute path>
C8_P_PORTRAITS_ENV_INPUT_PREFLIGHT_FINAL_STATUS=<status>
```

## 9. Decision Rule

Use `C8_P_ENV_INPUT_PREFLIGHT_READY_FOR_TEACHER_REVIEW` only if:

```text
required input files are present or documented with exact equivalent paths
environment inventory is complete
porTraits code/version inventory is complete
query_metatraits=none feasibility is classified with direct evidence
asset inventory is complete enough to identify present/missing prerequisites
C8-P target inventory is derived from the original 2,478 denominator
fungi are excluded from C8-P targets
genome FASTA availability is dry-checked without bulk download
all required reports, manifests, archive, and identity txt are written
no hard boundary is violated
```

Use `C8_P_ENV_INPUT_PREFLIGHT_BLOCKED_WITH_ACTIONABLE_GAPS` if the package is
complete but Chenyu lacks required assets, lacks an executable porTraits version,
lacks query_metatraits=none support, or lacks enough genome FASTA availability
for a later smoke test.

Use `C8_P_SCOPE_VIOLATION_ABORTED` if any accidental command starts full
prediction, downloads bulk genomes, includes fungi as porTraits targets, or
mutates production/staged C8 assets. If this happens, stop immediately and write
the incident into `LOCAL_AUDIT_REPORT.md`.
