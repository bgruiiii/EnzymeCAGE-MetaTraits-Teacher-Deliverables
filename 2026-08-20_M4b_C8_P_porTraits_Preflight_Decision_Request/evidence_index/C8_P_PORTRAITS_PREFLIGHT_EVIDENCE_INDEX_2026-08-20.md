# C8-P porTraits Preflight Evidence Index

Date: 2026-08-20

## Teacher-Facing Files

```text
README.md
M4B_C8_P_PORTRAITS_PREFLIGHT_DECISION_REQUEST_2026-08-20.md
pending_teacher_decisions/C8_P_TEACHER_DECISION_CHECKLIST_D1_D7_2026-08-20.md
```

## Authority And Context

```text
authority_reference/TEACHER_REPLY_C8_P_PREFLIGHT_AUTHORITY_2026-08-19.md
authority_reference/M4B_C8_P_PORTRAITS_PREFLIGHT_PATH_CONTRACT_AND_TASK_BREAKDOWN_2026-08-20.md
authority_reference/PORTRAITS_V0_2_1_OFFICIAL_DEPENDENCY_AUDIT_2026-08-20.md
```

Use:

```text
Teacher 2026-08-19 ruling defines C8-P as separate controlled preflight.
Path contract defines denominator, red lines, stage order, and no-production boundary.
Official dependency audit explains v0.2.1, query_metatraits=none, assets, containers, and no light-mode caveat.
```

## Chenyu Executor Prompts

```text
prompts/HPC_C8_P_PORTRAITS_ENVIRONMENT_AND_INPUT_PREFLIGHT_EXECUTOR_ONLY_PROMPT_2026-08-20.md
prompts/HPC_C8_P2A_PORTRAITS_RUNTIME_BOOTSTRAP_EXECUTOR_ONLY_PROMPT_2026-08-20.md
prompts/HPC_C8_P2B_PORTRAITS_ASSET_CONTAINER_PREPARATION_PREFLIGHT_EXECUTOR_ONLY_PROMPT_2026-08-20.md
```

Use:

```text
These show what Chenyu was authorized to do and, more importantly, what it was forbidden to do.
```

## Chenyu Return Archives

```text
hpc_archives/enzymecage_c8_p_portraits_environment_and_input_preflight_20260820.tar.gz
hpc_archives/enzymecage_c8_p2a_portraits_runtime_bootstrap_20260820.tar.gz
hpc_archives/enzymecage_c8_p2b_portraits_asset_container_preparation_preflight_20260820.tar.gz
```

Identity sidecars:

```text
hpc_identity/enzymecage_c8_p_portraits_environment_and_input_preflight_20260820.tar.gz.identity.txt
hpc_identity/enzymecage_c8_p2a_portraits_runtime_bootstrap_20260820.tar.gz.identity.txt
hpc_identity/enzymecage_c8_p2b_portraits_asset_container_preparation_preflight_20260820.tar.gz.identity.txt
```

Use:

```text
P1: environment/input target derivation preflight.
P2A: user-space Nextflow and porTraits v0.2.1 route resolver.
P2B: asset/container/quota metadata-only preflight.
```

## Local Audits

```text
audits/C8_P_PORTRAITS_ENVIRONMENT_AND_INPUT_PREFLIGHT_PROMPT_LOCAL_AUDIT_2026-08-20.md
audits/C8_P_PORTRAITS_ENVIRONMENT_AND_INPUT_PREFLIGHT_RETURN_LOCAL_AUDIT_2026-08-20.md
audits/C8_P2A_PORTRAITS_RUNTIME_BOOTSTRAP_PROMPT_LOCAL_AUDIT_2026-08-20.md
audits/C8_P2A_PORTRAITS_RUNTIME_BOOTSTRAP_RETURN_LOCAL_AUDIT_2026-08-20.md
audits/C8_P2B_PORTRAITS_ASSET_CONTAINER_PREPARATION_PREFLIGHT_PROMPT_LOCAL_AUDIT_2026-08-20.md
audits/C8_P2B_PORTRAITS_ASSET_CONTAINER_PREPARATION_PREFLIGHT_RETURN_LOCAL_AUDIT_2026-08-20.md
```

Use:

```text
Each Chenyu prompt and each return package was locally audited before being used for the next step.
```

## Key Facts To Trace

```text
2,478 denominator preserved:
  audits/C8_P_PORTRAITS_ENVIRONMENT_AND_INPUT_PREFLIGHT_RETURN_LOCAL_AUDIT_2026-08-20.md

322 bacteria + 90 archaea = 412 C8-P targets:
  audits/C8_P_PORTRAITS_ENVIRONMENT_AND_INPUT_PREFLIGHT_RETURN_LOCAL_AUDIT_2026-08-20.md

428 fungi excluded identity-only:
  audits/C8_P_PORTRAITS_ENVIRONMENT_AND_INPUT_PREFLIGHT_RETURN_LOCAL_AUDIT_2026-08-20.md

Nextflow 24.10.5 installed:
  audits/C8_P2A_PORTRAITS_RUNTIME_BOOTSTRAP_RETURN_LOCAL_AUDIT_2026-08-20.md

porTraits v0.2.1 commit 945795b supports query_metatraits=none:
  audits/C8_P2A_PORTRAITS_RUNTIME_BOOTSTRAP_RETURN_LOCAL_AUDIT_2026-08-20.md
  authority_reference/PORTRAITS_V0_2_1_OFFICIAL_DEPENDENCY_AUDIT_2026-08-20.md

Assets/container/runtime still blocked:
  audits/C8_P2B_PORTRAITS_ASSET_CONTAINER_PREPARATION_PREFLIGHT_RETURN_LOCAL_AUDIT_2026-08-20.md

No forbidden execution:
  all return local audits
```

## Checksums

```text
checksums/MANIFEST.files
checksums/MANIFEST.sha256
checksums/DELIVERABLE_SHA256SUMS.txt
```
