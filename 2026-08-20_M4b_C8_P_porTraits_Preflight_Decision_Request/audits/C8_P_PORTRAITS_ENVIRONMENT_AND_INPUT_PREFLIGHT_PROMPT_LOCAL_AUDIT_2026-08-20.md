# Local audit: C8-P porTraits environment and input preflight executor prompt

Date: 2026-08-20

Audited prompt:

```text
/home/a/EnzymeCAGE/custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/07_HPC_Prompts/HPC_C8_P_PORTRAITS_ENVIRONMENT_AND_INPUT_PREFLIGHT_EXECUTOR_ONLY_PROMPT_2026-08-20.md
```

Path contract:

```text
/home/a/EnzymeCAGE/custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/01_Path_Contract_Objective/M4b_C8_P_porTraits_Genome_Prediction_Preflight_2026-08-20/M4B_C8_P_PORTRAITS_PREFLIGHT_PATH_CONTRACT_AND_TASK_BREAKDOWN_2026-08-20.md
```

Audit status:

```text
PROMPT_AUDIT_PASS_FOR_CHENYU_EXECUTOR_HANDOFF
```

## Scope Check

```text
PASS: The prompt is aligned to Huang-laoshi's 2026-08-19 ruling.
PASS: The prompt now references the C8-P path contract and task breakdown.
PASS: The prompt now documents the optional dependency payload fallback for Chenyu.
PASS: The prompt states that C8 v1 does not automatically start porTraits.
PASS: The prompt limits this executor task to Stage 0 environment and input feasibility.
PASS: The prompt forbids full porTraits prediction.
PASS: The prompt forbids small-sample phenotype prediction in this Stage 0 task.
PASS: The prompt forbids bulk genome FASTA download.
PASS: The prompt scopes C8-P targets to bacteria and archaea only.
PASS: The prompt explicitly excludes fungi from porTraits v1 and keeps fungi identity-only.
PASS: The prompt preserves the original 2,478 microbe source denominator.
PASS: The prompt keeps the 137 rescued-asset-linked outside-universe sources out of the target list.
PASS: The prompt requires verification, not assumption, of query_metatraits=none support.
PASS: The prompt forbids porTraits code patching and requires blocker reporting instead.
PASS: The prompt forbids production D4, production pool, formal asset, C8 main output, and trait_annotation mutation.
PASS: The prompt forbids hard rejection, trait_score, uncalibrated confidence, F5 prediction, and exact pollutant degradation claims from F8.
PASS: The prompt requires complete return folder, tar.gz archive, identity txt, manifests, command transcript, and local audit.
```

## Intended Decision After Execution

```text
Use the returned package to decide whether Chenyu has enough environment,
porTraits code support, model/database assets, and bacteria/archaea genome FASTA
availability to ask Huang-laoshi for a later controlled C8-P smoke test.

Do not treat the returned package as teacher approval for prediction, full rollout,
fungal prediction, or production integration.
```
