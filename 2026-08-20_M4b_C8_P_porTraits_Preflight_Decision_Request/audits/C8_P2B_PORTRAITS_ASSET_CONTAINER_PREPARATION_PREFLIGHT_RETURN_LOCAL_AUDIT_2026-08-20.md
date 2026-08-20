# Local Audit: C8-P2B porTraits Asset / Container Preparation Preflight Return

Date: 2026-08-20

Audited return package:

```text
03_HPC_Returned_Result_Summaries/enzymecage_c8_p2b_portraits_asset_container_preparation_preflight_20260820.tar.gz
03_HPC_Returned_Result_Summaries/enzymecage_c8_p2b_portraits_asset_container_preparation_preflight_20260820.tar.gz.identity.txt
```

Audit status:

```text
PASS_AS_METADATA_ONLY_PREFLIGHT_PACKAGE
NOT_READY_FOR_PORTRAITS_SMOKE
```

## 1. Archive Integrity

```text
identity FINAL_STATUS=C8_P2B_ASSET_CONTAINER_PREFLIGHT_READY_FOR_LOCAL_AUDIT
identity ARCHIVE_SHA256=04a879ead4c478688fc3e4fab7e37ad64ede815d9b400da8a6b8010847b82462
local sha256=04a879ead4c478688fc3e4fab7e37ad64ede815d9b400da8a6b8010847b82462
single_root=yes
MANIFEST.sha256=PASS for all listed files
```

The package contains the expected planning and audit artifacts:

```text
README.md
LOCAL_AUDIT_REPORT.md
FINAL_STATUS.txt
COMMAND_TRANSCRIPT.txt
ENVIRONMENT_QUOTA_RECHECK.md/json
OFFICIAL_ASSET_URL_METADATA.csv
OFFICIAL_ASSET_URL_METADATA_SUMMARY.md
ASSET_SIZE_BUDGET.csv
QUOTA_RISK_ASSESSMENT.md
PROPOSED_ASSET_LAYOUT.md
CONTAINER_IMAGE_REFERENCE_PLAN.csv
APPTAINER_SIF_PULL_PLAN.md
CONTAINER_RUNTIME_ADMIN_QUESTIONS.md
EXISTING_REUSABLE_ASSET_PATHS.csv
EXISTING_REUSABLE_ASSET_SUMMARY.md
TEACHER_DECISION_CHECKLIST_FOR_C8_P.md
MANIFEST.files
MANIFEST.sha256
```

## 2. Boundary Compliance

The returned transcript and local audit table consistently report no forbidden execution:

```text
porTraits_executed=false
nextflow_run_executed=false
nextflow_config_executed=false
genome_download_executed=false
model_database_download_executed=false
container_pull_executed=false
production_data_modified=false
```

Manual string review found no evidence of actual `nextflow run`, `nextflow config`, genome FASTA download, model/database archive download, container pull, SIF build, sudo/system install, production mutation, fungal prediction, F5 prediction, trait_score, hard rejection, or uncalibrated confidence.

The `APPTAINER_SIF_PULL_PLAN.md` file contains future `apptainer pull` commands as a plan only. The transcript confirms no pull/build was executed.

## 3. Environment And Reusable Asset Findings

Environment recheck:

```text
Nextflow: present, 24.10.5 build 5935
porTraits candidate: present, v0.2.1 code at commit 945795b
singularity/apptainer/docker/module: absent
/usrdata: 423T total, 159T available
/: 100G total, 95G available
quota/lfs tools: absent
```

Reusable asset search:

```text
metatraits_models: not found
BacDive-AI models: not found
GenomeSPOT models: not found
MICROPHERRET: not found
Traitar: not found
reCOGnise marker genes: not found
GTDB-Tk database: not found
eggNOG database: not found
PFAM mapping: not found
container SIF images: not found
```

Conclusion: there are no reusable local porTraits assets on this machine. All required model/database assets and container images would need teacher-approved download/transfer or an existing shared HPC cache.

## 4. Asset URL Metadata And Size Budget

Confirmed metadata:

```text
porTraits-DB.tar.gz: HTTP 200, 1,421,564,553 bytes, Zenodo MD5 confirmed
recognise_markers.tar.gz: HTTP 200, 1,021,341,841 bytes, Zenodo MD5 confirmed
gtdbtk_r220_data.tar.gz: HTTP 200, 108,491,169,765 bytes, ETag/Last-Modified present
```

Failed metadata:

```text
eggnog.db.gz: HEAD failed, curl error 52 / empty reply
eggnog_proteins.dmnd.gz: HEAD failed, curl error 52 / empty reply
eggnog.taxa.tar.gz: HEAD failed, curl error 52 / empty reply
pfam.tar.gz: HEAD failed, curl error 52 / empty reply
```

Size estimate:

```text
compressed downloads: ~152 GB
decompressed / on-disk assets: ~294 GB
/usrdata available: 159 TB
quota risk: LOW
```

Audit note: the 294 GB storage estimate is adequate for planning, but the eggNOG portion remains estimate-only because the server did not return metadata. This does not block teacher discussion, but it blocks a clean asset download prompt unless an eggNOG source or mirror is confirmed.

## 5. Container Plan

The package identified 10 unique image references from porTraits v0.2.1 code:

```text
ghcr.io/grp-bork/recognise:v0.8.0
quay.io/biocontainers/gtdbtk:2.4.1--pyhdfd78af_1
ghcr.io/cschu/genomespot:main
registry.git.embl.org/schudoma/genomespot-docker:v1.0.1plus
quay.io/biocontainers/eggnog-mapper:2.1.12--pyhdfd78af_2
registry.git.embl.org/schudoma/portrait_sklearn:v1.2.2_micropherret
registry.git.embl.org/schudoma/portrait_sklearn:v.1.4.0_traitar_bacdive
registry.git.embl.org/schudoma/portraits_metatraits:latest
registry.git.embl.org/schudoma/portraits_metatraits:with_pandas
quay.io/biocontainers/prodigal:2.6.3--h031d066_7
```

This is compatible with the prior official dependency audit, with one useful correction: the prompt expected 9 references, while the code-derived scan found an additional `ghcr.io/cschu/genomespot:main` reference. The package correctly records this as a difference from the prompt.

Container registry metadata checks were incomplete because registry APIs timed out or required auth. This is acceptable for a metadata-only preflight, but actual SIF preparation remains blocked until Singularity/Apptainer is available and registry access is verified.

## 6. Teacher/Admin Decisions Still Required

The package's D1-D7 checklist is appropriate and concrete:

```text
D1 approve porTraits main commit 945795b / manifest 0.2.1
D2 decide how Singularity/Apptainer will be made available
D3 approve model/database asset downloads or transfers
D4 approve OCI-to-SIF container preparation
D5 approve tiny bacteria/archaea FASTA smoke inputs
D6 confirm storage path / quota owner
D7 confirm fungi stay identity-only and no production integration
```

These are real gates. P2B does not authorize a smoke test by itself.

## 7. Audit Conclusion

P2B is a valid and useful metadata-only deployment planning package. It did the right thing for this stage:

```text
PASS: no prediction or download scope violation
PASS: archive and manifest are internally valid
PASS: asset URL metadata was checked without body downloads
PASS: quota appears sufficient
PASS: proposed asset layout is specific enough for teacher/admin review
PASS: container image list is more complete than the prompt's initial list
PASS: teacher/admin decision checklist is usable
```

But C8-P is not ready for porTraits smoke:

```text
BLOCKED: no Singularity/Apptainer/Docker/module runtime
BLOCKED: 0/10 reusable porTraits assets found
BLOCKED: GTDB/eggNOG/reCOGnise/porTraits-DB assets not downloaded or staged
BLOCKED: eggNOG 5.0.2 source metadata failed and needs mirror/source resolution
BLOCKED: container SIF images not available
BLOCKED: tiny bacteria/archaea FASTA inputs are not authorized
BLOCKED: teacher D1-D7 decisions are still pending
```

Recommended next step:

```text
Prepare C8-P3 teacher-facing decision card using C8-P1, C8-P2A, C8-P2B, and the official dependency audit.
```

Do not proceed to C8-P4 smoke until teacher/admin decisions close the runtime, asset, container, FASTA, and v0.2.1 approval gates.
