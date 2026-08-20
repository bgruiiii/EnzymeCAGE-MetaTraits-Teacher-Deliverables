# Local audit: C8-P2A porTraits runtime bootstrap executor prompt

Date: 2026-08-20

Audited prompt:

```text
/home/a/EnzymeCAGE/custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/07_HPC_Prompts/HPC_C8_P2A_PORTRAITS_RUNTIME_BOOTSTRAP_EXECUTOR_ONLY_PROMPT_2026-08-20.md
```

Audit status:

```text
PROMPT_AUDIT_PASS_FOR_CHENYU_EXECUTOR_HANDOFF
```

## Scope Check

```text
PASS: Prompt responds to C8-P1 runtime blockers without starting porTraits.
PASS: Prompt allows only user-space Nextflow bootstrap, not root-level installation.
PASS: Prompt forbids sudo, apt, yum, dnf, systemctl, and Docker installation.
PASS: Prompt resolves Singularity/Apptainer by existing binary/module only.
PASS: Prompt searches for newer porTraits query_metatraits=none support but forbids patching.
PASS: Prompt searches existing assets read-only and forbids model/database downloads.
PASS: Prompt forbids genome FASTA download.
PASS: Prompt forbids nextflow run, phenotype prediction, production mutation, fungi targets, F5 prediction, hard rejection, trait_score, and uncalibrated confidence.
PASS: Prompt requires return folder, tar.gz archive, identity txt, manifest, command transcript, and local audit.
```

Intended use:

```text
Use this prompt only if the user decides to try resolving runtime prerequisites
before writing the teacher-facing C8-P blocker/decision card.
```
