# C8-P Teacher Decision Checklist D1-D7

Date: 2026-08-20

This checklist summarizes the decisions needed before any C8-P porTraits smoke
test or phenotype prediction can start.

## D1. porTraits Version

Question:

```text
May C8-P use official porTraits main commit 945795b5a6577f881c451f292eb3a60d94d33eed
with manifest.version = 0.2.1?
```

Context:

```text
Local v0.1.7 does not support query_metatraits=none.
Official main commit 945795b supports query_metatraits=none and defaults to none.
There is no GitHub v0.2.1 tag/release yet, so this needs explicit teacher approval.
```

## D2. Container Runtime

Question:

```text
How should Singularity/Apptainer be made available?
```

Options needing teacher/admin decision:

```text
Admin installs Singularity/Apptainer on the current machine;
or run on a real HPC cluster with Singularity/Apptainer module;
or hold C8-P until container runtime exists.
```

Current status:

```text
singularity / apptainer / docker / module all absent.
```

## D3. Model And Database Assets

Question:

```text
May we download or transfer the porTraits model/database assets?
```

Assets:

```text
porTraits-DB.tar.gz: 1.32 GB, Zenodo confirmed
recognise_markers.tar.gz: 974 MB, Zenodo confirmed
gtdbtk_r220_data.tar.gz: 101 GB compressed, GTDB confirmed
eggNOG emapperdb-5.0.2: required, current HEAD metadata failed
PFAM archive / Pfam-A.clans.tsv.gz: required, current HEAD metadata failed
```

Storage:

```text
estimated compressed download: ~152 GB
estimated decompressed/on-disk: ~294 GB
/usrdata available: 159 TB
```

## D4. Container SIF Preparation

Question:

```text
May we pull and convert the porTraits container images to SIF after Singularity/Apptainer is available?
```

Code-derived image count:

```text
10 unique image references
```

Risk:

```text
registry.git.embl.org may require credentials;
ghcr.io registry API may require token;
actual pull/build was not attempted in preflight.
```

## D5. Tiny FASTA Smoke Input

Question:

```text
May we later download or transfer a tiny bacteria/archaea genome FASTA set for smoke testing?
```

Current status:

```text
412/412 C8-P targets have assembly_accession.
0/412 local FASTA files found.
No genome FASTA download has been performed.
```

Boundary:

```text
Only bacteria/archaea.
No fungi.
Tiny smoke only.
No full rollout.
```

## D6. Asset Storage Path

Question:

```text
Is this proposed path acceptable?
/usrdata/EnzymeCAGE_data/databases/portraits/v0.2.1/
```

Proposed layout:

```text
metatraits_models/
recognise_markers/
gtdb/release220/
eggnog/emapperdb-5.0.2/
containers/sif/
```

## D7. Boundary Reconfirmation

Question:

```text
Please confirm that all C8-P red lines remain active.
```

Red lines:

```text
Fungi remain identity-only.
No porTraits v1 prediction for fungi.
No production D4 mutation.
No production pool mutation.
No formal asset mutation.
Predicted evidence does not replace observed evidence.
Predicted evidence is not written as experimental fact.
source_type must be porTraits_genome_prediction.
No hard rejection.
No trait_score.
No uncalibrated confidence.
No F5 prediction.
F8 broad degradation cannot be written as exact target-pollutant degradation.
```

## Current Recommendation

```text
Approve D1-D4 and D6 only if teacher wants us to prepare runtime/assets.
Keep D5 as a separate explicit switch before genome FASTA download.
Always keep D7 active.
```
