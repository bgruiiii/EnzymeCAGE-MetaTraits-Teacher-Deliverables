# C8-P2A porTraits Runtime Bootstrap Return Local Audit

Date: 2026-08-20

Audited package:

```text
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/03_HPC_Returned_Result_Summaries/enzymecage_c8_p2a_portraits_runtime_bootstrap_20260820.tar.gz
```

Identity sidecar:

```text
custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/03_HPC_Returned_Result_Summaries/enzymecage_c8_p2a_portraits_runtime_bootstrap_20260820.tar.gz.identity.txt
```

## Verdict

```text
LOCAL_AUDIT_VERDICT=C8_P2A_PARTIAL_PASS_NEXTFLOW_AND_VERSION_RESOLVED_NOT_READY_FOR_SMOKE
```

C8-P2A did solve two important blockers:

```text
Nextflow installed in user space: 24.10.5 build 5935
Official porTraits latest/main v0.2.1 supports query_metatraits=none by default
```

C8-P2A did not solve the execution blockers needed for a smoke test:

```text
Singularity/Apptainer not found
Docker not installed and was forbidden
porTraits model/database assets found: 0 / 10
local genome FASTA inputs still not present
teacher approval still required to switch from v0.1.7 to v0.2.1
```

Therefore:

```text
Proceed to porTraits smoke now: NO
Proceed to phenotype prediction now: NO
Proceed to full C8-P rollout now: NO
Proceed to teacher-facing decision card: YES
```

## Package Integrity

Identity check:

```text
actual archive sha256 = 951de7cbeea615647d82a56ab4a20440e1ad15513644184d98f7c8e8f988e612
identity archive sha256 = 951de7cbeea615647d82a56ab4a20440e1ad15513644184d98f7c8e8f988e612
sha256 match = YES
actual archive bytes = 8,386
identity archive bytes = 8,386
bytes match = YES
```

Manifest:

```text
MANIFEST.sha256 check = PASS
single root = enzymecage_c8_p2a_portraits_runtime_bootstrap_20260820
```

Final status from package:

```text
C8_P2A_RUNTIME_BOOTSTRAP_PARTIAL_NEXTFLOW_ONLY
```

The final status is appropriate.

## Boundary Audit

PASS:

```text
No porTraits run.
No nextflow run.
No genome FASTA download.
No model/database download.
No Docker installation.
No sudo / apt / yum / dnf / systemctl use.
No porTraits patching.
No production data mutation.
No fungi target handling.
No trait_score / hard rejection / uncalibrated confidence.
No F5 prediction.
```

Only allowed checks were run:

```text
nextflow -version
nextflow help
git ls-remote official porTraits
git clone official porTraits for source inspection
read-only filesystem searches for container runtime and existing assets
```

## What Was Resolved

### R1. Nextflow

Status:

```text
RESOLVED
```

Evidence:

```text
Install path = /usrdata/EnzymeCAGE_data/tools/c8_p_portraits_runtime_20260820/nextflow/nextflow
Version = 24.10.5 build 5935
Java prerequisite = OpenJDK 17.0.19
Install method = official user-space bootstrap script
```

Boundary:

```text
No nextflow run executed.
No pipeline launched.
No container pulled.
```

### R2. query_metatraits=none Version Route

Status:

```text
RESOLVED AS A VERSION-CHOICE OPTION, NOT YET TEACHER-APPROVED
```

Evidence:

```text
Baseline v0.1.7 / commit 742d0c6 = NOT_SUPPORTED
Official latest/main v0.2.1 / commit 945795b = SUPPORTED
```

v0.2.1 evidence:

```text
nextflow_schema.json defines query_metatraits enum none/NCBI/GTDB/both
schema default = none
nextflow.config default = query_metatraits = "none"
main.nf skips MetaTraits query when params.query_metatraits == "none"
docs/usage.md documents --query_metatraits
CHANGELOG v0.2.0 notes toggle for metatraits reference queries
```

Interpretation:

```text
We no longer need to patch v0.1.7 if teacher allows switching to official
v0.2.1. But v0.2.1 is not automatically approved; it must be presented as a
version-change decision.
```

## What Remains Blocked

### B1. Container Runtime

Status:

```text
BLOCKED_ADMIN_OR_MODULE_REQUIRED
```

Evidence:

```text
which singularity = not found
which apptainer = not found
module command = not found
no .sif files found
no singularity/apptainer cache directories found
```

Impact:

```text
porTraits cannot execute workflow processes without Docker or
Singularity/Apptainer. Docker installation was correctly forbidden by prompt.
```

### B2. porTraits Assets

Status:

```text
0 / 10 found
```

Missing:

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

Impact:

```text
Even with Nextflow and v0.2.1, porTraits cannot run a meaningful smoke until
assets are transferred/downloaded under teacher-approved scope.
```

### B3. Genome FASTA Inputs

Status:

```text
Still not solved in C8-P2A
```

This was expected because C8-P2A forbade genome downloads. C8-P1 already showed
412 / 412 targets have assembly_accession, but 0 / 412 local FASTA were found.

### B4. Teacher Approval

Still needed for:

```text
Using official porTraits v0.2.1 instead of local v0.1.7.
Installing/enabling Singularity or Apptainer.
Transferring/downloading porTraits model/database assets.
Downloading tiny bacteria/archaea genome FASTA inputs for smoke.
```

## Go / No-Go

```text
Nextflow blocker resolved: YES
query_metatraits=none blocker resolved by official v0.2.1 option: YES
Container runtime blocker resolved: NO
Model/database asset blocker resolved: NO
Genome FASTA input blocker resolved: NO
Teacher approval for version switch/assets/smoke: NO
```

Current state:

```text
C8-P is no longer blocked by Nextflow.
C8-P is no longer blocked by lack of a query_metatraits=none code route if v0.2.1 is approved.
C8-P remains blocked by container runtime, model/database assets, genome FASTA inputs, and teacher approval.
```

## Recommended Next Step

Write a teacher-facing C8-P decision card rather than another execution prompt.

The decision card should ask Huang-laoshi / senior side to decide:

```text
1. Approve official porTraits v0.2.1 for C8-P because it supports query_metatraits=none.
2. Approve or arrange Singularity/Apptainer runtime on Chenyu.
3. Approve transfer/download of porTraits model/database assets.
4. Approve a tiny bacteria/archaea genome FASTA smoke set only after runtime/assets are ready.
```

Do not start a smoke test until those decisions are explicit.
