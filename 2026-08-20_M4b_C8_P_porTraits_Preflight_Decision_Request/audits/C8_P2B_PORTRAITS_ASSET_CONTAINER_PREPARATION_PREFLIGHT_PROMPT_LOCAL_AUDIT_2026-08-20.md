# Local audit: C8-P2B porTraits asset/container preparation preflight prompt

Date: 2026-08-20

Audited prompt:

```text
/home/a/EnzymeCAGE/custom/docs/enzyme_feature_expansion/ENZYMECAGE_LUCAPCYCLE_MODEL_TRAINING_RUN_2026-07-01/07_HPC_Prompts/HPC_C8_P2B_PORTRAITS_ASSET_CONTAINER_PREPARATION_PREFLIGHT_EXECUTOR_ONLY_PROMPT_2026-08-20.md
```

Audit status:

```text
PROMPT_AUDIT_PASS_FOR_CHENYU_EXECUTOR_HANDOFF
```

## Scope Check

```text
PASS: Prompt is an asset/container metadata preflight, not a porTraits run.
PASS: Prompt uses C8-P1/C8-P2A findings and the 2026-08-20 official dependency report.
PASS: Prompt allows metadata-only URL checks but forbids model/database downloads.
PASS: Prompt forbids genome FASTA download.
PASS: Prompt forbids container pull and SIF build.
PASS: Prompt forbids nextflow run and nextflow config.
PASS: Prompt forbids Docker installation, sudo, apt, yum, dnf, systemctl, and root-level changes.
PASS: Prompt requires proposed asset layout, size budget, quota risk assessment, container image plan, admin questions, and teacher decision checklist.
PASS: Prompt keeps fungi excluded and prohibits production mutation, F5 prediction, trait_score, hard rejection, and uncalibrated confidence.
PASS: Prompt requires return folder, tar.gz archive, identity txt, manifest, command transcript, and local audit.
```

Intended use:

```text
Use this prompt to prepare evidence for teacher/senior feedback about whether to
approve porTraits v0.2.1, Apptainer/Singularity setup, large asset preparation,
container SIF preparation, and later tiny bacteria/archaea smoke input download.
```
