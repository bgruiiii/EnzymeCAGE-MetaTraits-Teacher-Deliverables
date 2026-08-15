# M4b / C7-2 Feature Encoding Proposal

Date: 2026-08-15

Status: proposal for Huang teacher review; not implemented; not production.

Scope: Chen Haoran microbe-side M4b/C7 TraitFilterLayer line only. This file does not cover Gong Sai's reaction-prediction line.

## 0. Purpose

This C7-2 proposal translates the teacher-frozen C7-1 trait panel into an auditable feature encoding and interface design.

It does three things only:

```text
1. define how frozen F1-F15 traits should be represented;
2. define how enzyme staged assets and microbe trait annotations should be joined without losing provenance;
3. define fail-closed validation rules before any later staged implementation.
```

This proposal does not implement `TraitFilterLayer`, does not generate a 2,478-source status table, does not train a model, does not write production D4, and does not enable hard filtering.

## 1. Authority And Evidence

Primary teacher authority:

```text
00_Authority_Teacher_Plan/
TEACHER_REPLY_FULL_4681_ACCEPTANCE_AND_C7_1_FREEZE_2026-08-14.md
```

Key teacher decisions now in force:

```text
1. full 4,681 staged status table is accepted as the second milestone, staged-only;
2. C7-1 trait panel F1-F15 is frozen item by item;
3. C7-2 shall be a feature encoding proposal referencing F1-F15 and keeping fungi identity-only;
4. teacher-side loader contract 7.2 and microbe feature consumption interface 7.3 are in force;
5. red lines continue: no production D4, no production pool mutation, no hard rejection,
   no uncalibrated confidence, no trait_score, no unlabelled predicted values.
```

Secondary authority and source evidence:

```text
00_Authority_Teacher_Plan/
TEACHER_REPLY_M4_E2_SECOND_MILESTONE_AND_M4B_C7_AUTHORIZATION_2026-08-14.md

01_Path_Contract_Objective/
M4b_C7_TraitFilterLayer_C7_1_Trait_Panel_Candidate_2026-08-14/
M4B_C7_1_TRAIT_PANEL_CANDIDATE_REPORT_2026-08-14.md

01_Path_Contract_Objective/
M4b_C7_TraitFilterLayer_C7_1_Trait_Panel_Candidate_2026-08-14/
C7_1_TRAIT_PANEL_CANDIDATE_TABLE_2026-08-14.csv

01_Path_Contract_Objective/
M4b_C7_TraitFilterLayer_Initiation_Blueprint_2026-08-13/
M4B_C7_TRAITFILTERLAYER_INITIATION_BLUEPRINT_2026-08-13.md

01_Path_Contract_Objective/
M4b_C7_TraitFilterLayer_Initiation_Blueprint_2026-08-13/
M4B_C7_SENIOR_DISCUSSION_QUESTIONS_2026-08-14.md

04_Local_Review_Audits/
M4B_C7_1_TRAIT_PANEL_CANDIDATE_LOCAL_AUDIT_2026-08-14.md
```

Uploaded teacher-facing evidence already reviewed by teacher:

```text
microbe-side:
https://github.com/bgruiiii/EnzymeCAGE-MetaTraits-Teacher-Deliverables/tree/main/2026-08-14_M4b_C7_1_Trait_Panel_Candidate

enzyme-side:
https://github.com/bgruiiii/EnzymeCAGE-Teacher-Deliverables/tree/main/2026-08-14_M4_E2_Full_4681_Staged_Status_Table
```

## 2. Numbering Note

The 2026-08-13 initiation blueprint originally split:

```text
C7-2 = observed/predicted route and fungal policy;
C7-3 = feature encoding proposal.
```

The 2026-08-14 teacher freeze has already frozen the C7-1 panel and incorporated the route/fungal policy into the effective decision. The latest teacher instruction now names the next Chen Haoran task as:

```text
C7-2: feature encoding proposal.
```

This document follows the latest teacher authority.

## 3. Frozen Inputs

### 3.1 Enzyme Staged Assets

Teacher-accepted M4 E2 package:

```text
full denominator: 4,681 UID
PASS staged asset sets in submitted package: 1,704 UID
unique sequences after sequence_sha256 deduplication: 1,597
evidence_tier: lower_evidence_predicted_pocket
mutation checks: formal / production pool / production D4 all false
```

Teacher note:

```text
The accepted package has 1,704 PASS assets.
The teacher reply also records a later P0DXV0 +1 PASS closure, giving a 1,705 effective口径.
For C7-2 encoding, do not silently merge the +1 asset unless its own manifest,
identity/provenance, and teacher closure record are present in the implementation package.
```

Required staged asset six-pack per UID:

```text
staged_assets/{UID}/pockets/pocket/{UID}.pdb
staged_assets/{UID}/pockets/pocket_info.csv
staged_assets/{UID}/esm3b/protein_level/seq2feature.pkl
staged_assets/{UID}/esm3b/pocket_node_feature/esm_node_feature.torch.pt
staged_assets/{UID}/gvp/gvp_protein_feature_flat.pt
staged_assets/{UID}/validation_input.csv
```

### 3.2 Frozen Trait Panel

Teacher-frozen first-screen traits:

| ID | Trait | Encoding role |
|---|---|---|
| F1 | oxygen_tolerance | first-screen environment compatibility hint |
| F2 | temperature | first-screen environment compatibility hint |
| F3 | pH | first-screen environment compatibility hint |
| F4 | salinity | first-screen environment compatibility hint |
| F5 | bacdive_availability | first-screen availability/provenance hint; observed only |

Teacher-frozen detail-on-request traits:

| ID | Trait | Encoding role |
|---|---|---|
| F6 | respiration_electron_acceptor | metabolic context |
| F7 | carbon_and_substrate_utilization | broad substrate / carbon context |
| F8 | degradation_capacity_broad | broad degradation context only |
| F9 | enzyme_activity | biochemical context |
| F10 | motility | ecological / colonization context |
| F11 | cell_morphology | phenotype context |
| F12 | cell_envelope_gram | phenotype context |
| F13 | sporulation | stress / persistence context |
| F14 | genome_basic | genome background |
| F15 | habitat_generalism | low-coverage ecological background only |

Global frozen constraints:

```text
observed always wins;
predicted never overwrites observed;
predicted values must be visibly labelled;
fungi remain identity-only;
F5 culture availability / collection number must not be predicted;
F8 cannot be used to claim exact degradation of a user-entered pollutant;
F15 must not participate in ranking, scoring, or recommendation;
no hard rejection, no trait_score, no uncalibrated confidence.
```

### 3.3 Coverage Reference For Encoding

Coverage below is carried forward from the 2026-08-14 C7-1 candidate table and local audit. The denominator is the 2,478-source microbe universe.

| ID | Coverage reference |
|---|---|
| F1 | atmosphere / oxygen all 1,631 / 2,478; no_predictions 1,528 / 2,478 |
| F2 | temperature all 1,638 / 2,478; no_predictions 1,606 / 2,478 |
| F3 | pH all 1,621 / 2,478; no_predictions 420 / 2,478 |
| F4 | salinity all 1,622 / 2,478; no_predictions 919 / 2,478 |
| F5 | BacDive validated species-or-better 1,746 / 2,478; exact-strain main 597 / 2,478; culture collection among validated 1,737 / 1,746; species representative expansion 1,149 source signatures |
| F6 | respiration all 1,611 / 2,478, no_predictions 286 / 2,478; electron acceptor all 1,608 / 2,478, no_predictions 7 / 2,478 |
| F7 | carbon utilization all 1,614 / 2,478, no_predictions 576 / 2,478; utilizes metabolite all 1,591 / 2,478, no_predictions 106 / 2,478 |
| F8 | catabolic process all 1,615 / 2,478; no_predictions 505 / 2,478 |
| F9 | enzyme activity all 1,611 / 2,478; no_predictions 1,150 / 2,478 |
| F10 | motility all 1,626 / 2,478; no_predictions 1,454 / 2,478 |
| F11 | cell morphology all 1,613 / 2,478; no_predictions 1,507 / 2,478 |
| F12 | cell envelope all 1,637 / 2,478; no_predictions 1,627 / 2,478 |
| F13 | sporulation all 1,623 / 2,478; no_predictions 1,262 / 2,478 |
| F14 | composition / gene content / genome size all/no_predictions 1,620 / 2,478 |
| F15 | habitat generalism all 356 / 2,478; no_predictions 0 / 2,478 |

Encoding implication:

```text
Coverage should be reported per F ID.
The all vs no_predictions distinction must be preserved where available.
Prediction-like records increase trait density among covered sources but do not increase
the total MetaTraits source coverage beyond the local snapshot.
```

## 4. Proposed Encoding Model

### 4.1 Per-Trait Evidence Container

Every F1-F15 entry should use the same evidence container. This keeps observed, predicted, missing, and fungal identity-only cases auditable.

```json
{
  "trait_id": "F1",
  "trait_name": "oxygen_tolerance",
  "display_layer": "first_screen",
  "observed_value": null,
  "predicted_value": null,
  "resolved_display_value": null,
  "value_status": "OBSERVED_USED|PREDICTED_SOFT_FILL_USED|NOT_OBSERVED|NOT_APPLICABLE|FUNGI_IDENTITY_ONLY",
  "evidence_type": "observed_database_record|predicted_soft_fill|prediction_like_context|missing|not_applicable",
  "prediction_used": false,
  "observed_available": false,
  "predicted_available": false,
  "source_database": null,
  "source_resolution": "species|exact_strain|species_representative|genome_derived|not_applicable",
  "provenance": {
    "source_file": null,
    "source_file_sha256": null,
    "record_id_or_url": null,
    "database_snapshot": null
  },
  "missing_reason": null,
  "warnings": []
}
```

Resolution rule:

```text
if taxonomy_group == fungi:
    value_status = FUNGI_IDENTITY_ONLY
    prediction_used = false
    missing_reason = fungi_no_local_trait_source
elif observed_available:
    resolved_display_value = observed_value
    value_status = OBSERVED_USED
elif predicted_available and trait_id in teacher_allowed_predicted_soft_fill:
    resolved_display_value = predicted_value
    value_status = PREDICTED_SOFT_FILL_USED
    prediction_used = true
else:
    resolved_display_value = null
    value_status = NOT_OBSERVED
```

### 4.2 Trait-Specific Encoding

| ID | Encoding type | Predicted soft fill | Special rule |
|---|---|---|---|
| F1 | controlled categorical / multi-label | allowed | label oxygen / atmosphere predictions |
| F2 | numeric range + categorical preference | allowed | preserve min / max / optimum where available |
| F3 | numeric range + categorical preference | allowed | preserve pH min / max / optimum where available |
| F4 | numeric range + categorical preference | allowed | preserve salinity unit / category where available |
| F5 | string/list provenance fields | forbidden | exact strain first; species representative must be labelled |
| F6 | controlled multi-label | allowed | keep respiration and electron acceptor labels separate |
| F7 | controlled multi-label | allowed | broad substrate/carbon context only |
| F8 | controlled multi-label | allowed only as broad catabolic context | never claim target pollutant degradation from this trait alone |
| F9 | controlled multi-label | source-labelled context only | prediction-like records must be labelled |
| F10 | categorical / boolean / unknown | source-labelled context only | no hard rejection |
| F11 | categorical / unknown | source-labelled context only | phenotype background |
| F12 | categorical / unknown | source-labelled context only | Gram/cell-envelope context |
| F13 | categorical / boolean / unknown | source-labelled context only | stress/persistence context |
| F14 | numeric/genome-derived background | no trait_score | genome background, not ranking |
| F15 | categorical/count-like low-coverage context | source-labelled only | UI must label low coverage; never used for ranking |

For all traits, missing values should be explicit:

```text
NOT_OBSERVED
NOT_APPLICABLE
FUNGI_IDENTITY_ONLY
SOURCE_NOT_COVERED
NO_LOCAL_TRAIT_SOURCE
```

Missing must not be interpreted as biological absence.

## 5. Proposed Output 1: TRAIN_SET_MANIFEST.csv

This output is the teacher 7.2 loader-contract view of staged enzyme assets. It should be generated only from rows that pass all hard checks.

Proposed minimum fields:

```text
UniprotID
sequence_sha256
sequence_length
esm_shape
p2rank_pocket_residue_count
p2rank_top_pocket_score
gvp_available
same_pocket_for_esm_node_and_gvp
loader_validation_status
dataset0_constructed
evidence_tier
formal_assets_mutated
production_pool_mutated
production_d4_mutated
deduplication_status
split
inclusion_status
exclusion_reason
source_status_table
source_asset_manifest
```

Hard inclusion rules:

```text
final_status == PASS_AFDB_P2RANK_PREDICTED_POCKET_D4_LOADER
esm_node_feature_shape[0] == p2rank_pocket_residue_count
same_pocket_for_esm_node_and_gvp == True
loader_validation_status == PASS
dataset0_constructed == True
formal_assets_mutated == False
production_pool_mutated == False
production_d4_mutated == False
sequence_sha256 matches manifest
evidence_tier == lower_evidence_predicted_pocket
```

Deduplication:

```text
Deduplicate by sequence_sha256.
The teacher-frozen baseline is 1,704 staged assets -> 1,597 unique sequences.
Do not introduce extra sequences in C7-2.
Do not silently include the P0DXV0 +1 asset unless its own verified asset record is present.
```

The `split` field should remain a placeholder in C7-2:

```text
split = UNASSIGNED_C7_2_PROPOSAL_ONLY
```

Actual train/validation/test split is outside this proposal unless separately authorized.

## 6. Proposed Output 2: trait_annotation.jsonl

This output is the teacher 7.3 microbe feature consumption interface. It should contain one row per enzyme-to-microbe candidate mapping.

Proposed row structure:

```json
{
  "uid": "A0A...",
  "sequence_sha256": "...",
  "asset": {
    "evidence_tier": "lower_evidence_predicted_pocket",
    "esm_shape": [85, 2560],
    "pocket_score": 118.99,
    "train_set_manifest_status": "INCLUDED_UNIQUE_SEQUENCE"
  },
  "mapping": {
    "source_signature": "...",
    "organism_uid": "...",
    "taxonomy_group": "bacteria|archaea|fungi",
    "species_name": "...",
    "strain_name_or_null": null,
    "mapping_source": "...",
    "mapping_method": "...",
    "mapping_resolution": "exact_strain|species|species_representative|unknown",
    "mapping_coverage_status": "MAPPED|NOT_MAPPED|REVIEW_REQUIRED"
  },
  "traits": {
    "F1": {},
    "F2": {},
    "F3": {},
    "F4": {},
    "F5": {},
    "F6": {},
    "F7": {},
    "F8": {},
    "F9": {},
    "F10": {},
    "F11": {},
    "F12": {},
    "F13": {},
    "F14": {},
    "F15": {}
  },
  "row_policy": {
    "hard_rejection_applied": false,
    "trait_score_emitted": false,
    "uncalibrated_confidence_emitted": false,
    "production_authorized": false
  }
}
```

Required preservation rules:

```text
F1-F15 IDs must remain explicit in every row.
No aggregation step may collapse F IDs into unnamed feature groups.
No observed/predicted merge may lose evidence_type.
No source_signature/species/strain inheritance may happen silently.
No fungal row may receive bacterial/archaeal trait soft fill.
```

## 7. Policy Manifest Draft

The later implementation should fail closed unless a policy manifest equivalent to the following is present.

```text
trait_panel_id = M4B_C7_PANEL_FROZEN_2026_08_14
trait_panel_items = F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,F13,F14,F15
teacher_authorization_id = TEACHER_REPLY_FULL_4681_ACCEPTANCE_AND_C7_1_FREEZE_2026-08-14
route = observed_first_predicted_soft_fill_for_allowed_categories
fungal_trait_policy = identity_only
fungal_missing_reason = fungi_no_local_trait_source
hard_rejection_enabled = false
trait_score_enabled = false
uncalibrated_confidence_enabled = false
production_integration_enabled = false
provenance_required = true
predicted_may_overwrite_observed = false
```

Allowed predicted soft-fill categories:

```text
F1 oxygen_tolerance
F2 temperature
F3 pH
F4 salinity
F6 respiration_electron_acceptor
F7 carbon_and_substrate_utilization
F8 degradation_capacity_broad, broad context only
```

Forbidden predicted soft-fill categories:

```text
F5 bacdive_availability
biosafety, excluded from C7-1 and C7-2
exact pollutant degradation
strain-specific traits without direct evidence
culture availability / collection number
fungal traits in this round
```

## 8. Validation Checklist For Later Implementation

Schema checks:

```text
all rows contain F1-F15 keys exactly once;
no extra unfrozen trait ID is emitted;
observed_value and predicted_value remain separate fields;
prediction_used is true only when observed is missing and category is allowed;
F5 prediction_used is always false;
fungi rows are identity-only and use missing_reason = fungi_no_local_trait_source;
hard_rejection_applied is always false;
trait_score_emitted is always false;
uncalibrated_confidence_emitted is always false;
production_authorized is always false.
```

Asset checks:

```text
TRAIN_SET_MANIFEST rows come only from staged PASS assets;
sequence_sha256 deduplication is reported;
esm_node_feature_shape[0] equals p2rank_pocket_residue_count;
same_pocket_for_esm_node_and_gvp is true;
loader_validation_status is PASS;
formal / production mutation flags remain false.
```

Provenance checks:

```text
every emitted trait value links to source database/table and source file or record ID;
MetaTraits species-level values are labelled species-level;
BacDive species representative records are labelled species representative;
prediction-like/clustering-derived values are labelled;
NOT_OBSERVED and NOT_APPLICABLE are not treated as biological negatives.
```

Boundary wording checks:

```text
Do not write that C7-2 is implemented.
Do not write that TraitFilterLayer is production-ready.
Do not write that broad degradation capacity proves degradation of a user-entered pollutant.
Do not write that availability can be predicted.
Do not write that fungi have predicted soft-filled traits in this round.
```

## 9. Proposed Next Step After Teacher Review

If Huang teacher freezes this C7-2 encoding proposal, the next small task should be a read-only schema/validator implementation against a bounded staged subset.

Suggested implementation outputs for that later step:

```text
POLICY_MANIFEST.json
TRAIN_SET_MANIFEST.csv
trait_annotation.jsonl
TRAIT_FEATURE_ENCODING_VALIDATION_REPORT.md
BOUNDARY_VALIDATION_REPORT.md
MANIFEST.sha256
FINAL_STATUS.txt
```

That later step should still remain staged-only unless Huang teacher separately authorizes production integration.

## 10. Non-Claims

This C7-2 proposal does not claim:

```text
feature encoding has been implemented;
the 2,478-source TraitFilterLayer status table has been generated;
any train/validation/test split has been frozen;
any microbe has been automatically accepted or rejected;
any trait_score or confidence score is available;
any exact pollutant degradation fact is inferred from broad traits;
any fungal trait prediction has entered this round;
any production D4 or production pool has been modified.
```
