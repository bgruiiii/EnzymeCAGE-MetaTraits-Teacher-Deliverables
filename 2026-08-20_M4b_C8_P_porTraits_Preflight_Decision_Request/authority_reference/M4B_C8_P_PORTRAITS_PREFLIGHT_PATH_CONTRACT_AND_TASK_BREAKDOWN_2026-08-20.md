# M4b C8-P porTraits Genome Prediction Preflight Path Contract And Task Breakdown

Date: 2026-08-20

Status: path contract / task breakdown for discussion and controlled execution.

This document defines the C8-P porTraits exploration route before any executor
run is treated as meaningful. It exists to prevent scope drift: C8-P is a
separate controlled branch for MetaTraits-uncovered bacteria / archaea only, not
a hidden full prediction rollout and not a fungal trait workaround.

## 1. Authority

Primary authority:

```text
00_Authority_Teacher_Plan/老师回复8.19.md
```

Teacher 2026-08-19 ruling relevant to C8-P:

```text
C8 v1 staged-only implementation is approved.
C8 v1 does not automatically start porTraits.
If MetaTraits-uncovered bacteria / archaea need porTraits, first submit a
controlled C8-P preflight plan for teacher review.
Fungi remain identity-only; porTraits v1 is not for fungi.
porTraits output, if later authorized, is staged-only prediction evidence.
source_type must be porTraits_genome_prediction.
Predicted evidence must not replace observed evidence.
Predicted evidence must not be written as experimental fact.
```

Current red lines:

```text
No production D4 mutation.
No production pool mutation.
No formal asset mutation.
No silent denominator change.
No merge of 137 outside-universe rescued sources into the original 2,478.
No hard rejection.
No trait_score.
No uncalibrated confidence.
No F5 prediction.
No fungal porTraits v1 prediction.
No exact target-pollutant degradation claim from F8 broad degradation context.
No F15 ranking use.
```

## 2. Why C8-P Exists

C8 v1 uses observed-first local MetaTraits TSV lookup plus frozen C7/C8 rules.
The current local MetaTraits snapshot covers part of the original 2,478 microbe
source universe:

```text
original C8 microbe universe = 2,478 source_signatures
target_bacteria = 1,897
target_archaea = 153
target_fungi = 428

MetaTraits covered = 1,638 / 2,478
MetaTraits-uncovered target_bacteria = 322 / 1,897
MetaTraits-uncovered target_archaea = 90 / 153
target_fungi = 428 identity-only
```

C8-P asks a narrower question:

```text
Can the MetaTraits official porTraits genome prediction branch later provide
staged-only soft-fill evidence for the 322 bacteria + 90 archaea sources not
covered by local MetaTraits lookup?
```

C8-P does not ask:

```text
Can we fill all missing microbe traits now?
Can we predict fungal traits with porTraits v1?
Can prediction replace observed evidence?
Can predicted traits enter production or ranking?
```

## 3. What porTraits Is In This Route

porTraits is treated as the MetaTraits ecosystem genome/MAG FASTA to phenotype
prediction workflow.

Expected input:

```text
genome FASTA / MAG FASTA
```

Not sufficient as direct porTraits input:

```text
UniProt ID only
TaxID only
species name only
source_signature only
```

Expected predictor families to inventory before any run:

```text
BacDive-AI
GenomeSPOT
Traitar
MICROPHERRET
```

Required supporting assets to inventory:

```text
Nextflow
Docker/Singularity/Apptainer runtime
metatraits_models
reCOGnise marker genes
GTDB-Tk database
eggNOG database
PFAM assets or mappings
porTraits code version and schema
```

Important version caveat:

```text
Some official porTraits documentation/schema may support query_metatraits=none,
but the local v0.1.7 snapshot previously inspected did not expose that parameter
in nextflow_schema.json. Therefore query_metatraits=none must be verified against
the actual Chenyu porTraits code before any smoke test.
```

## 4. Denominator Contract

Main denominator:

```text
2,478 source_signatures from the audited C8 microbe universe.
```

Primary denominator file:

```text
custom/github_upload/EnzymeCAGE-MetaTraits-Teacher-Deliverables/2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/02_bacdive_full_closure/bacdive_metatraits_overlap_by_source_signature.csv
```

Auxiliary source metadata file:

```text
custom/github_upload/reaction_enzyme_microbe_training_clean_2026-06-01/tables/enzyme_to_microbe_source.csv
```

Auxiliary MetaTraits coverage file:

```text
custom/github_upload/EnzymeCAGE-MetaTraits-Teacher-Deliverables/2026-08-12_MetaTraits_BacDive_Microbe_Trait_Availability/01_metatraits_species_coverage/source_signature_metatraits_coverage.csv
```

Rules:

```text
Use the 2,478-row audited universe as the denominator.
Use the 3,234-row coverage probe only as auxiliary lookup evidence.
Do not silently switch denominator to 3,234.
Do not add the 137 rescued-asset-linked outside-universe sources.
Do not include fungi in porTraits target list.
```

Expected C8-P target universe:

```text
target_bacteria MetaTraits-uncovered = 322
target_archaea MetaTraits-uncovered = 90
total C8-P bacteria/archaea targets = 412
target_fungi excluded identity-only = 428
```

If derived counts differ, report the mismatch rather than force the expected
numbers.

## 5. Stage Breakdown

### C8-P0: Path Contract And Task Breakdown

Purpose:

```text
Define route, authority, denominator, red lines, and allowed next executor step.
```

Output:

```text
M4B_C8_P_PORTRAITS_PREFLIGHT_PATH_CONTRACT_AND_TASK_BREAKDOWN_2026-08-20.md
```

Status:

```text
This document. No porTraits run.
```

### C8-P1: Chenyu Environment And Input Feasibility Preflight

Purpose:

```text
Check whether Chenyu has the environment, porTraits code support, required
model/database assets, target source inventory, and genome FASTA availability
needed to design a later teacher-approved smoke test.
```

Executor prompt:

```text
07_HPC_Prompts/HPC_C8_P_PORTRAITS_ENVIRONMENT_AND_INPUT_PREFLIGHT_EXECUTOR_ONLY_PROMPT_2026-08-20.md
```

Optional dependency payload for Chenyu upload:

```text
07_HPC_Prompts/enzymecage_c8_p_portraits_preflight_dependency_payload_20260820.tar.gz
07_HPC_Prompts/enzymecage_c8_p_portraits_preflight_dependency_payload_20260820.tar.gz.identity.txt
```

Allowed:

```text
Read-only environment inventory.
porTraits code/schema/config inspection.
query_metatraits=none feasibility classification.
Model/database asset inventory.
C8-P bacteria/archaea target derivation from the 2,478 universe.
Genome FASTA availability dry check.
Non-invasive Nextflow version/help/config checks.
Return package creation.
```

Forbidden:

```text
Full porTraits prediction.
Small-sample phenotype prediction.
Bulk genome FASTA download.
Fungal prediction.
Production or C8 main output mutation.
porTraits code patching.
```

Expected returned package location:

```text
03_HPC_Returned_Result_Summaries/enzymecage_c8_p_portraits_environment_and_input_preflight_20260820/
03_HPC_Returned_Result_Summaries/enzymecage_c8_p_portraits_environment_and_input_preflight_20260820.tar.gz
03_HPC_Returned_Result_Summaries/enzymecage_c8_p_portraits_environment_and_input_preflight_20260820.tar.gz.identity.txt
```

### C8-P2: Local Audit Of C8-P1 Return

Purpose:

```text
Independently audit the Chenyu returned package before using it for teacher
discussion or for any next prompt.
```

Required checks:

```text
Verify archive identity and manifest.
Verify no full prediction ran.
Verify no small-sample phenotype prediction ran.
Verify no bulk genome download happened.
Verify fungi were excluded.
Verify denominator stayed 2,478.
Verify 322/90 target derivation or explain mismatch.
Verify query_metatraits=none feasibility evidence.
Verify asset gaps and genome FASTA availability claims.
Verify next-step recommendation does not claim teacher approval.
```

Output location:

```text
04_Local_Review_Audits/
```

Gate:

```text
Do not proceed to C8-P3 until C8-P2 local audit is complete.
```

### C8-P2A: Runtime Bootstrap After C8-P1 Blocker Audit

Status:

```text
Optional technical remediation step added after C8-P1 local audit on 2026-08-20.
Not a prediction step.
```

Purpose:

```text
Resolve what can be resolved locally before asking teacher about a porTraits
smoke: user-space Nextflow availability, Singularity/Apptainer resolver, existing
asset resolver, and newer porTraits version inspection for query_metatraits=none.
```

Executor prompt:

```text
07_HPC_Prompts/HPC_C8_P2A_PORTRAITS_RUNTIME_BOOTSTRAP_EXECUTOR_ONLY_PROMPT_2026-08-20.md
```

Allowed:

```text
User-space Nextflow bootstrap if Java/network/permissions allow.
Read-only module/binary search for Singularity/Apptainer.
Read-only search for existing shared porTraits assets.
Read-only newer porTraits source/version inspection.
```

Forbidden:

```text
No porTraits run.
No nextflow run.
No genome FASTA download.
No model/database download.
No container image pull.
No Docker installation.
No sudo/system package installation.
No porTraits patching.
No fungi.
No production mutation.
```

Gate:

```text
After C8-P2A returns, local audit is required before any C8-P smoke prompt or
teacher decision card uses its result.
```

### C8-P2B: Asset / Container Preparation Preflight

Status:

```text
Optional metadata-only exploration step added after reading the 2026-08-20
official dependency/HPC output audit.
Not a download step.
Not a prediction step.
```

Purpose:

```text
Prepare the evidence needed for teacher/senior feedback before any large asset
download or smoke test: official asset URLs, size metadata, quota risk, proposed
asset layout, container image/SIF plan, Apptainer/Singularity admin questions,
and teacher decision checklist.
```

Executor prompt:

```text
07_HPC_Prompts/HPC_C8_P2B_PORTRAITS_ASSET_CONTAINER_PREPARATION_PREFLIGHT_EXECUTOR_ONLY_PROMPT_2026-08-20.md
```

Allowed:

```text
Metadata-only official URL checks.
Registry metadata checks without pulling layers.
Read-only quota/disk checks.
Read-only existing asset path search.
Writing deployment plan and teacher decision checklist.
```

Forbidden:

```text
No porTraits run.
No nextflow run/config.
No genome FASTA download.
No database/model archive download.
No container pull.
No SIF build.
No Docker install.
No sudo/system package install.
No porTraits patching.
No fungi.
No production mutation.
```

Gate:

```text
After C8-P2B returns, local audit is required. Its output may support a
teacher-facing C8-P3 decision card, but cannot authorize smoke by itself.
```

### C8-P3: Teacher-Facing C8-P Preflight Plan / Decision Card

Purpose:

```text
Use C8-P1 + C8-P2 + optional C8-P2A/C8-P2B evidence to ask Huang-laoshi whether
a later controlled smoke test may be started.
```

Content:

```text
What Chenyu environment supports.
What porTraits version supports.
Whether query_metatraits=none is possible without patching.
What assets are present or missing.
How many bacteria/archaea targets have assembly_accession.
How many already have local FASTA.
Proposed tiny smoke scope if feasible.
Blockers if not feasible.
Red lines preserved.
```

Forbidden:

```text
Do not claim C8-P prediction has started.
Do not include prediction results.
Do not request fungal porTraits v1 use.
```

### C8-P4: Teacher-Approved Tiny Smoke Test

Status:

```text
Not authorized as of 2026-08-20.
```

Only after explicit teacher/user approval, a tiny smoke may test the workflow on
the smallest feasible bacteria/archaea genome FASTA set.

Allowed only after approval:

```text
Use query_metatraits=none if supported.
Use bacteria/archaea only.
Use already available or explicitly authorized tiny FASTA inputs.
Write staged-only smoke evidence.
```

Still forbidden:

```text
No full rollout.
No fungi.
No production.
No observed-evidence replacement.
No F5 prediction.
```

### C8-P5: Small-Sample Phenotype Prediction

Status:

```text
Not authorized as of 2026-08-20.
```

This stage can exist only if C8-P4 succeeds and teacher approves a small-sample
phenotype prediction.

### C8-P6: Bounded Expansion Or Closure Decision

Status:

```text
Not authorized as of 2026-08-20.
```

Possible outcomes after C8-P1 to C8-P5:

```text
Close C8-P because environment/assets/input FASTA are not feasible.
Hold C8-P pending missing databases or code update.
Proceed to a teacher-approved bounded bacteria/archaea prediction expansion.
Keep fungi identity-only and route fungal prediction as a separate future branch.
```

## 6. Current Next Step

Current next step is only:

```text
C8-P1: Chenyu environment and input feasibility preflight.
```

It should be executed with:

```text
07_HPC_Prompts/HPC_C8_P_PORTRAITS_ENVIRONMENT_AND_INPUT_PREFLIGHT_EXECUTOR_ONLY_PROMPT_2026-08-20.md
```

Success of C8-P1 does not mean porTraits is approved for prediction. It means
there is enough evidence to prepare a teacher-facing C8-P decision card or to
document blockers.

## 7. Stop Conditions

Stop and audit before any next step if:

```text
Chenyu lacks porTraits code or a supported code version.
query_metatraits=none is unsupported or unclear.
Required models/databases are missing.
Genome FASTA availability is too low for a meaningful smoke test.
Derived target counts differ from 322 bacteria / 90 archaea and the mismatch is
not explained.
Any command accidentally starts workflow tasks or bulk downloads.
Any output includes fungi as porTraits targets.
Any output mutates production or C8 main staged outputs.
```

## 8. Placement Rules For This Branch

```text
00_Authority_Teacher_Plan: teacher replies, authority, external/source plans.
01_Path_Contract_Objective: this path contract, task breakdown, teacher-facing
  plan drafts, decision cards.
03_HPC_Returned_Result_Summaries: returned C8-P packages from Chenyu.
04_Local_Review_Audits: prompt local audits and returned-package local audits.
07_HPC_Prompts: Chenyu/HPC executor-only prompts and execution payloads.
```

Do not put Chenyu executor prompts in `01_Path_Contract_Objective` unless the
task is explicitly a local/manual exploration exception and the reason is stated.
