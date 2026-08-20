# HPC executor-only prompt: C8-P2A porTraits runtime bootstrap

You are running on Chenyu/HPC as an executor for EnzymeCAGE / MetaTraits. Your
job is to resolve the **runtime environment blockers** found by C8-P1 as far as
they can be resolved without crossing teacher/user boundaries.

This is **not** a porTraits prediction run. This is **not** a genome download
task. This is **not** a model/database asset download task. This is a bounded
runtime bootstrap and version-resolution task.

## 0. Task Identity

```text
TASK_ID=enzymecage_c8_p2a_portraits_runtime_bootstrap_20260820
RUN_TYPE=runtime_bootstrap_no_prediction_no_genome_download
FULL_RUN_AUTHORIZED=false
PREDICTION_AUTHORIZED=false
GENOME_DOWNLOAD_AUTHORIZED=false
MODEL_DATABASE_DOWNLOAD_AUTHORIZED=false
PRODUCTION_AUTHORIZED=false
```

Allowed final statuses:

```text
C8_P2A_RUNTIME_BOOTSTRAP_READY_FOR_LOCAL_AUDIT
C8_P2A_RUNTIME_BOOTSTRAP_PARTIAL_NEXTFLOW_ONLY
C8_P2A_RUNTIME_BOOTSTRAP_BLOCKED_CONTAINER_RUNTIME_REQUIRED
C8_P2A_RUNTIME_BOOTSTRAP_BLOCKED_NETWORK_OR_PERMISSION
C8_P2A_RUNTIME_BOOTSTRAP_BLOCKED_OUTPUT_PATH_EXISTS
C8_P2A_SCOPE_VIOLATION_ABORTED
C8_P2A_RUNTIME_BOOTSTRAP_FAILED_RUNTIME_ERROR
```

## 1. Authority And Required Read-First Files

Read if available:

```text
/home/a/EnzymeCAGE/custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/00_Authority_Teacher_Plan/老师回复8.19.md
/home/a/EnzymeCAGE/custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/01_Path_Contract_Objective/M4b_C8_P_porTraits_Genome_Prediction_Preflight_2026-08-20/M4B_C8_P_PORTRAITS_PREFLIGHT_PATH_CONTRACT_AND_TASK_BREAKDOWN_2026-08-20.md
/home/a/EnzymeCAGE/custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/04_Local_Review_Audits/C8_P_PORTRAITS_ENVIRONMENT_AND_INPUT_PREFLIGHT_RETURN_LOCAL_AUDIT_2026-08-20.md
```

If local authority files are unavailable, read the C8-P1 returned package and
its local audit if they are present in the project tree or uploaded payload.

C8-P1 found:

```text
target universe clean: 322 bacteria + 90 archaea
fungi excluded identity-only: 428
all 412 C8-P targets have assembly_accession
runtime blocked: no Nextflow, no container runtime, no porTraits assets
current porTraits v0.1.7 does not support query_metatraits=none
```

## 2. Hard Boundaries

```text
Do not run porTraits.
Do not run nextflow run.
Do not run phenotype prediction.
Do not run small-sample prediction.
Do not download genome FASTA.
Do not download the 412 target genomes.
Do not download GTDB-Tk, eggNOG, metatraits_models, PFAM, reCOGnise, or other large databases.
Do not pull container images unless explicitly instructed in a later prompt.
Do not install Docker.
Do not use sudo, apt, yum, dnf, systemctl, or root-level package installation.
Do not patch porTraits code.
Do not mutate production D4, production pool, formal assets, or C8 main outputs.
Do not include fungi as porTraits targets.
Do not emit trait_score, hard rejection, or uncalibrated confidence.
Do not predict F5.
```

Allowed:

```text
Read-only environment inspection.
User-space Nextflow installation if Java is present and network/permissions allow.
Module-system search for existing Singularity/Apptainer/Nextflow.
Read-only search for existing shared porTraits assets and databases.
Read-only search or clone/download of porTraits source code for version inspection only.
No workflow execution.
```

## 3. Fresh Output Paths

Use these paths, adapting `PROJECT_ROOT` only if Chenyu uses a different existing
project root:

```text
PROJECT_ROOT=/usrdata/EnzymeCAGE_data/EnzymeCAGE-master
RETURN_ROOT=${PROJECT_ROOT}/HPC_Returned_Result_Summaries
TASK_ID=enzymecage_c8_p2a_portraits_runtime_bootstrap_20260820
RETURN_DIR=${RETURN_ROOT}/${TASK_ID}
ARCHIVE=${RETURN_ROOT}/${TASK_ID}.tar.gz
IDENTITY=${RETURN_ROOT}/${TASK_ID}.tar.gz.identity.txt
WORK_ROOT=/tmp/${TASK_ID}
TOOL_ROOT=/usrdata/EnzymeCAGE_data/tools/c8_p_portraits_runtime_20260820
```

If `/usrdata/EnzymeCAGE_data/tools` is not writable, use:

```text
TOOL_ROOT=${PROJECT_ROOT}/tools/c8_p_portraits_runtime_20260820
```

Fresh-run rule:

```text
If RETURN_DIR, ARCHIVE, IDENTITY, WORK_ROOT, or TOOL_ROOT already exists, do not
overwrite or repair it. Create a uniquely suffixed blocked return package and set
FINAL_STATUS=C8_P2A_RUNTIME_BOOTSTRAP_BLOCKED_OUTPUT_PATH_EXISTS.
```

Allowed write locations:

```text
RETURN_DIR
WORK_ROOT
TOOL_ROOT
```

## 4. Required Work

### 4.1 Environment recheck

Record:

```text
hostname, date, user, pwd
OS/kernel
disk free for PROJECT_ROOT, RETURN_ROOT, WORK_ROOT parent, TOOL_ROOT parent
java -version
python3 --version
which nextflow/docker/singularity/apptainer/conda/mamba/sinfo/sbatch/module
module avail nextflow/singularity/apptainer if module command exists
```

Write:

```text
ENVIRONMENT_RECHECK.md
ENVIRONMENT_RECHECK.json
```

### 4.2 User-space Nextflow bootstrap

If an existing `nextflow` is found, do not reinstall. Record its path and version.

If Nextflow is missing and Java is present, attempt a user-space install into:

```text
${TOOL_ROOT}/nextflow/
```

Allowed approaches:

```text
Use official Nextflow bootstrap script only if network access allows.
Store the binary under TOOL_ROOT.
Run only `nextflow -version` after installation.
```

Forbidden:

```text
No nextflow run.
No pipeline launch.
No profile execution.
No container pull.
```

Write:

```text
NEXTFLOW_BOOTSTRAP.md
NEXTFLOW_VERSION.txt
```

### 4.3 Container runtime resolver

Do not install Docker. Do not use sudo.

Search for:

```text
singularity
apptainer
module avail singularity
module avail apptainer
module spider singularity/apptainer if supported
common shared paths under /usr/bin, /usr/local/bin, /opt, /usrdata, /public, /share
```

If Singularity/Apptainer is found, record version and path. Do not pull images.

If none is found, report:

```text
CONTAINER_RUNTIME_STATUS=BLOCKED_ADMIN_OR_MODULE_REQUIRED
```

Write:

```text
CONTAINER_RUNTIME_RESOLVER.md
```

### 4.4 porTraits version resolver for query_metatraits=none

Use current uploaded/local v0.1.7 as baseline. Then, if network access allows,
inspect the official porTraits repository or available local newer versions.

Allowed:

```text
git ls-remote / git clone official porTraits source into TOOL_ROOT/source_probe/
read nextflow_schema.json, main.nf, nextflow.config, docs
search for query_metatraits, params.query_metatraits, skip metatraits, none
record commit/tag evidence
```

Forbidden:

```text
Do not patch code.
Do not run porTraits.
Do not switch production code.
Do not claim a newer version is approved.
```

Classify:

```text
CURRENT_V017_NOT_SUPPORTED
NEWER_OFFICIAL_VERSION_SUPPORTS_QUERY_METATRAITS_NONE
NO_OFFICIAL_VERSION_FOUND_WITH_QUERY_METATRAITS_NONE
NETWORK_BLOCKED_CANNOT_VERIFY_NEWER_VERSION
```

Write:

```text
PORTRAITS_VERSION_RESOLVER.md
PORTRAITS_QUERY_NONE_VERSION_EVIDENCE.tsv
```

### 4.5 Existing asset resolver only

Search read-only for existing assets. Do not download databases.

Search likely roots:

```text
/usrdata
/public
/share
/mnt
/opt
/vol
${PROJECT_ROOT}
```

Record any existing candidate paths for:

```text
metatraits_models
BacDive-AI models
GenomeSPOT models
MICROPHERRET
Traitar
reCOGnise marker genes
GTDB-Tk database
eggNOG database
PFAM mapping
container images/cache
```

For large directories, record only path existence, rough size, and top-level
listing. Do not hash every file.

Write:

```text
EXISTING_ASSET_RESOLVER.csv
EXISTING_ASSET_RESOLVER_SUMMARY.md
```

### 4.6 No-run validation

If Nextflow becomes available, allowed checks are only:

```text
nextflow -version
nextflow help
```

Do not run:

```text
nextflow config
nextflow run
```

because config/run can trigger unexpected resolution or downloads in some
profiles. Leave config/run for a later approved smoke prompt.

Write:

```text
NO_RUN_VALIDATION.md
```

## 5. Required Return Files

Return folder must contain:

```text
README.md
FINAL_STATUS.txt
LOCAL_AUDIT_REPORT.md
COMMAND_TRANSCRIPT.txt
ENVIRONMENT_RECHECK.md
ENVIRONMENT_RECHECK.json
NEXTFLOW_BOOTSTRAP.md
NEXTFLOW_VERSION.txt
CONTAINER_RUNTIME_RESOLVER.md
PORTRAITS_VERSION_RESOLVER.md
PORTRAITS_QUERY_NONE_VERSION_EVIDENCE.tsv
EXISTING_ASSET_RESOLVER.csv
EXISTING_ASSET_RESOLVER_SUMMARY.md
NO_RUN_VALIDATION.md
BLOCKERS_AND_NEXT_STEPS.md
MANIFEST.files
MANIFEST.sha256
```

Do not include downloaded databases, genomes, container images, or large caches in
the returned archive.

## 6. Packaging

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
TOOL_ROOT
NEXTFLOW_STATUS
CONTAINER_RUNTIME_STATUS
QUERY_METATRAITS_NONE_VERSION_STATUS
ASSET_RESOLVER_STATUS
porTraits_executed=false
nextflow_run_executed=false
genome_download_executed=false
model_database_download_executed=false
production_data_modified=false
```

Print final paths:

```text
C8_P2A_RUNTIME_BOOTSTRAP_RETURN_DIR=<absolute path>
C8_P2A_RUNTIME_BOOTSTRAP_ARCHIVE=<absolute path>
C8_P2A_RUNTIME_BOOTSTRAP_IDENTITY=<absolute path>
C8_P2A_RUNTIME_BOOTSTRAP_FINAL_STATUS=<status>
```

## 7. Decision Rule

Use `C8_P2A_RUNTIME_BOOTSTRAP_READY_FOR_LOCAL_AUDIT` only if:

```text
Nextflow is available via existing install or user-space bootstrap.
Singularity or Apptainer is available via existing binary/module.
porTraits query_metatraits=none support is resolved by an official newer version
or clearly remains unsupported with evidence.
No hard boundary was violated.
```

Use partial/blocker statuses if only some conditions are resolved. Do not present
partial environment setup as permission to run porTraits.
