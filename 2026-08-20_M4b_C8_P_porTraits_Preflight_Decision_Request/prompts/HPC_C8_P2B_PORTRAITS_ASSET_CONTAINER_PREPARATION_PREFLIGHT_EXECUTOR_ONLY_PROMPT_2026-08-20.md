# HPC executor-only prompt: C8-P2B porTraits asset/container preparation preflight

You are running on Chenyu/HPC as an executor for EnzymeCAGE / MetaTraits. Your
job is to prepare a **read-only asset/container deployment plan** for C8-P
porTraits, using the C8-P1 and C8-P2A findings.

This is not a porTraits run. This is not a database download task. This is not a
container pull task. This is not a genome FASTA download task.

## 0. Task Identity

```text
TASK_ID=enzymecage_c8_p2b_portraits_asset_container_preparation_preflight_20260820
RUN_TYPE=asset_container_preparation_preflight_metadata_only
PREDICTION_AUTHORIZED=false
GENOME_DOWNLOAD_AUTHORIZED=false
MODEL_DATABASE_DOWNLOAD_AUTHORIZED=false
CONTAINER_PULL_AUTHORIZED=false
PRODUCTION_AUTHORIZED=false
```

Allowed final statuses:

```text
C8_P2B_ASSET_CONTAINER_PREFLIGHT_READY_FOR_LOCAL_AUDIT
C8_P2B_ASSET_CONTAINER_PREFLIGHT_BLOCKED_NETWORK_OR_METADATA
C8_P2B_ASSET_CONTAINER_PREFLIGHT_BLOCKED_NO_CONTAINER_RUNTIME
C8_P2B_ASSET_CONTAINER_PREFLIGHT_BLOCKED_INSUFFICIENT_QUOTA
C8_P2B_ASSET_CONTAINER_PREFLIGHT_BLOCKED_OUTPUT_PATH_EXISTS
C8_P2B_SCOPE_VIOLATION_ABORTED
C8_P2B_ASSET_CONTAINER_PREFLIGHT_FAILED_RUNTIME_ERROR
```

## 1. Authority And Required Read-First Files

Read if available:

```text
/home/a/EnzymeCAGE/custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/00_Authority_Teacher_Plan/老师回复8.19.md
/home/a/EnzymeCAGE/custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/00_Authority_Teacher_Plan/porTraits_v0.2.1_official_dependency_HPC_output_audit_2026-08-20.md
/home/a/EnzymeCAGE/custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/01_Path_Contract_Objective/M4b_C8_P_porTraits_Genome_Prediction_Preflight_2026-08-20/M4B_C8_P_PORTRAITS_PREFLIGHT_PATH_CONTRACT_AND_TASK_BREAKDOWN_2026-08-20.md
/home/a/EnzymeCAGE/custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/04_Local_Review_Audits/C8_P_PORTRAITS_ENVIRONMENT_AND_INPUT_PREFLIGHT_RETURN_LOCAL_AUDIT_2026-08-20.md
/home/a/EnzymeCAGE/custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/04_Local_Review_Audits/C8_P2A_PORTRAITS_RUNTIME_BOOTSTRAP_RETURN_LOCAL_AUDIT_2026-08-20.md
```

Current audited state:

```text
C8-P target universe is clean: 322 bacteria + 90 archaea.
Fungi remain excluded identity-only: 428.
All 412 C8-P targets have assembly_accession.
Nextflow 24.10.5 is installed in user space.
Official porTraits main commit 945795b / manifest 0.2.1 supports query_metatraits=none.
Container runtime is missing.
porTraits model/database assets are missing.
Genome FASTA inputs are missing and must not be downloaded in this task.
```

## 2. Hard Boundaries

```text
Do not run porTraits.
Do not run nextflow run.
Do not run nextflow config.
Do not download genome FASTA.
Do not download GTDB, eggNOG, PFAM, reCOGnise, porTraits-DB, metatraits_models, or any large database.
Do not pull container images.
Do not build SIF images.
Do not install Docker.
Do not install Singularity or Apptainer.
Do not use sudo, apt, yum, dnf, systemctl, or root-level installation.
Do not patch porTraits code.
Do not mutate production D4, production pool, formal assets, C8 main outputs, or trait_annotation.
Do not include fungi as porTraits targets.
Do not emit trait_score, hard rejection, uncalibrated confidence, or F5 prediction.
```

Allowed:

```text
Metadata-only URL checks: HEAD requests, Zenodo API metadata, registry manifest metadata, HTML index listing.
Read-only filesystem search for existing assets, containers, and candidate shared directories.
Read-only quota/disk checks.
Creating small plan/manifest files under RETURN_DIR and WORK_ROOT.
Creating no large directories except optional empty proposed directory tree under WORK_ROOT for documentation.
```

If a command may download a large file or container layer, do not run it. Record
the skipped command and the reason.

## 3. Fresh Output Paths

Use:

```text
PROJECT_ROOT=/usrdata/EnzymeCAGE_data/EnzymeCAGE-master
RETURN_ROOT=${PROJECT_ROOT}/HPC_Returned_Result_Summaries
TASK_ID=enzymecage_c8_p2b_portraits_asset_container_preparation_preflight_20260820
RETURN_DIR=${RETURN_ROOT}/${TASK_ID}
ARCHIVE=${RETURN_ROOT}/${TASK_ID}.tar.gz
IDENTITY=${RETURN_ROOT}/${TASK_ID}.tar.gz.identity.txt
WORK_ROOT=/tmp/${TASK_ID}
NEXTFLOW_BIN=/usrdata/EnzymeCAGE_data/tools/c8_p_portraits_runtime_20260820/nextflow/nextflow
PORTRAITS_V021_CANDIDATE=/usrdata/EnzymeCAGE_data/tools/c8_p_portraits_runtime_20260820/source_probe/porTraits
```

Fresh-run rule:

```text
If RETURN_DIR, ARCHIVE, IDENTITY, or WORK_ROOT already exists, do not overwrite.
Create a uniquely suffixed blocked return package and set:
FINAL_STATUS=C8_P2B_ASSET_CONTAINER_PREFLIGHT_BLOCKED_OUTPUT_PATH_EXISTS.
```

Allowed write locations:

```text
RETURN_DIR
WORK_ROOT
```

## 4. Required Work

### 4.1 Environment and quota recheck

Record:

```text
hostname, date, user, pwd
NEXTFLOW_BIN exists and version
PORTRAITS_V021_CANDIDATE exists and commit/version if available
which singularity/apptainer/docker/module
df -h for /usrdata, PROJECT_ROOT, RETURN_ROOT, /tmp
du -sh for current TOOL_ROOT if present
available quota command output if quota/lfs/quota tools exist
```

Write:

```text
ENVIRONMENT_QUOTA_RECHECK.md
ENVIRONMENT_QUOTA_RECHECK.json
```

### 4.2 Official asset URL metadata preflight

Perform metadata-only checks for these official or report-identified assets:

```text
porTraits-DB:
  https://zenodo.org/records/16818976/files/porTraits-DB.tar.gz

reCOGnise markers:
  https://zenodo.org/records/17916463/files/recognise_markers.tar.gz

GTDB-Tk r220:
  https://data.gtdb.ecogenomic.org/releases/release220/220.0/auxillary_files/gtdbtk_package/full_package/gtdbtk_r220_data.tar.gz

eggNOG 5.0.2:
  http://eggnog6.embl.de/download/emapperdb-5.0.2/eggnog.db.gz
  http://eggnog6.embl.de/download/emapperdb-5.0.2/eggnog_proteins.dmnd.gz
  http://eggnog6.embl.de/download/emapperdb-5.0.2/eggnog.taxa.tar.gz
  http://eggnog6.embl.de/download/emapperdb-5.0.2/pfam.tar.gz
```

Allowed methods:

```text
curl -I / curl --head
curl metadata API endpoints returning JSON metadata only
wget --spider
small HTML directory listing fetches only when HEAD lacks Content-Length
```

Forbidden:

```text
No downloading archive body.
No partial database download.
No wget/curl without HEAD/spider/range-safe metadata guard.
```

Record:

```text
url
status_code
content_length_bytes if available
etag/checksum if available
last_modified if available
redirect_final_url if any
metadata_source
risk_notes
```

Write:

```text
OFFICIAL_ASSET_URL_METADATA.csv
OFFICIAL_ASSET_URL_METADATA_SUMMARY.md
```

### 4.3 Proposed asset layout and size budget

Create a proposed layout only as text, not as large directories:

```text
/usrdata/EnzymeCAGE_data/databases/portraits/v0.2.1/
  metatraits_models/
    BacDive-AI/models/
    GenomeSPOT/models/
    MICROPHERRET/
    Traitar/
  recognise_markers/
  gtdb/release220/
  eggnog/emapperdb-5.0.2/
    eggnog.db
    eggnog_proteins.dmnd
    eggnog.taxa/
    pfam/Pfam-A.clans.tsv.gz
  containers/sif/
```

Important:

```text
Use BacDive-AI capitalization from main.nf, not Bacdive-AI from params.yml example.
```

Estimate required storage using:

```text
official Content-Length where available
official known size from report for reCOGnise markers and GTDB r220
third-party estimate clearly labelled for eggNOG if official size is unavailable
unknown marker for porTraits-DB/PFAM if metadata cannot be resolved
```

Write:

```text
PROPOSED_ASSET_LAYOUT.md
ASSET_SIZE_BUDGET.csv
QUOTA_RISK_ASSESSMENT.md
```

### 4.4 Container image metadata and SIF plan

Do not pull images. Do not build SIF.

List v0.2.1 container references from `nextflow.config` and report:

```text
ghcr.io/grp-bork/recognise:v0.8.0
quay.io/biocontainers/gtdbtk:2.4.1--pyhdfd78af_1
registry.git.embl.org/schudoma/genomespot-docker:v1.0.1plus
quay.io/biocontainers/eggnog-mapper:2.1.12--pyhdfd78af_2
registry.git.embl.org/schudoma/portrait_sklearn:v1.2.2_micropherret
registry.git.embl.org/schudoma/portrait_sklearn:v.1.4.0_traitar_bacdive
registry.git.embl.org/schudoma/portraits_metatraits:latest
registry.git.embl.org/schudoma/portraits_metatraits:with_pandas
quay.io/biocontainers/prodigal:2.6.3--h031d066_7
```

Note: if v0.2.1 config contains fewer/more unique references, report the exact
code-derived list and explain differences.

For each image, do metadata-only registry checks if safe. Do not fetch layers.

Write:

```text
CONTAINER_IMAGE_REFERENCE_PLAN.csv
APPTAINER_SIF_PULL_PLAN.md
CONTAINER_RUNTIME_ADMIN_QUESTIONS.md
```

### 4.5 Existing assets and reusable local paths

Search read-only again for existing candidate paths under:

```text
/usrdata
/public
/share
/mnt
/opt
/vol
${PROJECT_ROOT}
```

Write only summaries. Do not hash large trees.

Write:

```text
EXISTING_REUSABLE_ASSET_PATHS.csv
EXISTING_REUSABLE_ASSET_SUMMARY.md
```

### 4.6 Teacher decision checklist

Generate a concise list of decisions required before any smoke:

```text
approve porTraits main commit 945795b / manifest 0.2.1
approve Singularity/Apptainer availability route
approve asset downloads/transfers
approve container OCI-to-SIF preparation
approve tiny bacteria/archaea FASTA smoke inputs
confirm asset storage path/quota owner
confirm no fungi and no production integration
```

Write:

```text
TEACHER_DECISION_CHECKLIST_FOR_C8_P.md
```

## 5. Required Return Files

Return folder must contain:

```text
README.md
FINAL_STATUS.txt
LOCAL_AUDIT_REPORT.md
COMMAND_TRANSCRIPT.txt
ENVIRONMENT_QUOTA_RECHECK.md
ENVIRONMENT_QUOTA_RECHECK.json
OFFICIAL_ASSET_URL_METADATA.csv
OFFICIAL_ASSET_URL_METADATA_SUMMARY.md
PROPOSED_ASSET_LAYOUT.md
ASSET_SIZE_BUDGET.csv
QUOTA_RISK_ASSESSMENT.md
CONTAINER_IMAGE_REFERENCE_PLAN.csv
APPTAINER_SIF_PULL_PLAN.md
CONTAINER_RUNTIME_ADMIN_QUESTIONS.md
EXISTING_REUSABLE_ASSET_PATHS.csv
EXISTING_REUSABLE_ASSET_SUMMARY.md
TEACHER_DECISION_CHECKLIST_FOR_C8_P.md
BLOCKERS_AND_NEXT_STEPS.md
MANIFEST.files
MANIFEST.sha256
```

No large assets, genome FASTA, containers, `.sif`, database archives, or model
files may be included in the return archive.

## 6. Local Audit Requirements

`LOCAL_AUDIT_REPORT.md` must answer:

```text
Did this task avoid porTraits execution?
Did this task avoid nextflow run/config?
Did this task avoid genome download?
Did this task avoid model/database download?
Did this task avoid container pull/SIF build?
Did this task avoid install/sudo/root changes?
Which asset URLs have confirmed metadata?
Which sizes are official, inferred, third-party, or unknown?
Is /usrdata quota enough for the planned assets?
Is Apptainer/Singularity available?
What admin questions remain?
What exact teacher decisions are needed before smoke?
```

## 7. Packaging

Create:

```text
${ARCHIVE}
${IDENTITY}
```

Identity must include:

```text
TASK_ID
FINAL_STATUS
RETURN_DIR
ARCHIVE
ARCHIVE_SHA256
ARCHIVE_SIZE_BYTES
asset_metadata_status
quota_status
container_runtime_status
existing_asset_status
teacher_decision_checklist_status
porTraits_executed=false
nextflow_run_executed=false
nextflow_config_executed=false
genome_download_executed=false
model_database_download_executed=false
container_pull_executed=false
production_data_modified=false
```

Print final paths:

```text
C8_P2B_ASSET_CONTAINER_PREFLIGHT_RETURN_DIR=<absolute path>
C8_P2B_ASSET_CONTAINER_PREFLIGHT_ARCHIVE=<absolute path>
C8_P2B_ASSET_CONTAINER_PREFLIGHT_IDENTITY=<absolute path>
C8_P2B_ASSET_CONTAINER_PREFLIGHT_FINAL_STATUS=<status>
```

## 8. Decision Rule

Use `C8_P2B_ASSET_CONTAINER_PREFLIGHT_READY_FOR_LOCAL_AUDIT` if the package
contains a complete metadata-only asset/container/quota plan, even if actual
downloads remain blocked pending teacher approval.

Use a blocked status if metadata checks cannot reach official sources, quota is
clearly insufficient, or container runtime/admin path is unresolved in a way that
prevents planning.
