# M4b C7-2 Feature Encoding Proposal Local Audit

Date: 2026-08-15

Audit status: LOCAL_AUDIT_PASS_FOR_USER_REVIEW_BEFORE_TEACHER_SUBMISSION

Audited file:

```text
01_Path_Contract_Objective/
M4b_C7_TraitFilterLayer_C7_2_Feature_Encoding_Proposal_2026-08-15/
M4B_C7_2_FEATURE_ENCODING_PROPOSAL_2026-08-15.md
```

## 1. Authority Check

Primary authority reviewed:

```text
00_Authority_Teacher_Plan/
TEACHER_REPLY_FULL_4681_ACCEPTANCE_AND_C7_1_FREEZE_2026-08-14.md
```

Relevant teacher requirements found:

```text
1. C7-1 F1-F15 trait panel is frozen;
2. C7-2 shall be a feature encoding proposal;
3. proposal must reference F1-F15 item IDs;
4. fungi remain identity-only;
5. teacher 7.2 loader contract and 7.3 microbe feature consumption interface should be used;
6. staged-only and no-production red lines remain active.
```

Audit result:

```text
PASS: proposal cites the latest teacher authority as primary.
PASS: proposal treats the 2026-08-13 blueprint numbering as superseded by the latest teacher task naming.
PASS: proposal does not claim C7-2 implementation or production authorization.
```

## 2. C7-1 Frozen Trait Panel Check

Sources reviewed:

```text
01_Path_Contract_Objective/
M4b_C7_TraitFilterLayer_C7_1_Trait_Panel_Candidate_2026-08-14/
M4B_C7_1_TRAIT_PANEL_CANDIDATE_REPORT_2026-08-14.md

01_Path_Contract_Objective/
M4b_C7_TraitFilterLayer_C7_1_Trait_Panel_Candidate_2026-08-14/
C7_1_TRAIT_PANEL_CANDIDATE_TABLE_2026-08-14.csv

04_Local_Review_Audits/
M4B_C7_1_TRAIT_PANEL_CANDIDATE_LOCAL_AUDIT_2026-08-14.md
```

Trait IDs checked:

```text
F1 oxygen_tolerance
F2 temperature
F3 pH
F4 salinity
F5 bacdive_availability
F6 respiration_electron_acceptor
F7 carbon_and_substrate_utilization
F8 degradation_capacity_broad
F9 enzyme_activity
F10 motility
F11 cell_morphology
F12 cell_envelope_gram
F13 sporulation
F14 genome_basic
F15 habitat_generalism
```

Audit result:

```text
PASS: all 15 frozen IDs are present in the proposal.
PASS: first-screen items match teacher freeze: F1-F5.
PASS: detail-on-request items match teacher freeze: F6-F15.
PASS: biosafety is excluded and not reintroduced.
PASS: proposal carries forward per-F coverage references from the C7-1 table/audit.
```

## 3. Teacher 7.2 Loader Contract Check

Teacher frozen requirements checked:

```text
staged_assets/{UID}/ six-pack input;
esm_node_feature_shape[0] == p2rank_pocket_residue_count;
same_pocket_for_esm_node_and_gvp == True;
loader_validation_status == PASS and dataset0_constructed == True;
formal / production pool / production D4 mutation flags all False;
sequence_sha256 matches manifest;
evidence_tier = lower_evidence_predicted_pocket;
deduplicate by sequence_sha256;
TRAIN_SET_MANIFEST.csv output.
```

Audit result:

```text
PASS: proposal includes all teacher-listed hard checks.
PASS: proposal keeps split as UNASSIGNED_C7_2_PROPOSAL_ONLY.
PASS: proposal does not claim training split or model training.
```

## 4. Teacher 7.3 Microbe Interface Check

Teacher frozen requirements checked:

```text
asset side: uid, sequence_sha256, esm_shape, pocket_score;
mapping side: uid -> strain/source list with mapping source, method, coverage;
panel side: F1-F15 observed / predicted / identity-only / NOT_OBSERVED annotations;
output: trait_annotation.jsonl;
aggregation must preserve F1-F15 IDs;
interface only annotates and counts coverage, not filtering decisions.
```

Audit result:

```text
PASS: proposal defines trait_annotation.jsonl with asset, mapping, and F1-F15 trait sections.
PASS: proposal forbids collapsing F IDs.
PASS: proposal keeps hard_rejection_applied false and production_authorized false.
```

## 5. Fungi And Predicted Soft-Fill Boundary Check

Teacher and senior-discussion boundaries checked:

```text
fungi 428 identity-only;
missing_reason = fungi_no_local_trait_source;
observed always wins;
predicted never overwrites observed;
predicted values must be labelled;
F5 availability / collection number cannot be predicted;
F8 broad degradation cannot prove exact target pollutant degradation;
F15 low coverage and no ranking / scoring / recommendation.
```

Audit result:

```text
PASS: proposal encodes fungi as FUNGI_IDENTITY_ONLY.
PASS: proposal limits predicted soft fill to teacher-allowed categories.
PASS: proposal explicitly forbids F5 prediction and fungal prediction in this round.
PASS: proposal preserves F8 and F15 red-line wording.
```

## 6. Evidence Number Check

Numbers copied from teacher-reviewed sources:

```text
full denominator: 4,681 UID
accepted submitted PASS staged assets: 1,704 UID
unique sequences after deduplication: 1,597
teacher note: P0DXV0 +1 PASS gives 1,705 effective口径 after later closure
microbe universe: 2,478 source signatures
fungi: 428
```

Audit result:

```text
PASS: proposal distinguishes the submitted 1,704 package from the later 1,705 effective note.
PASS: proposal does not silently alter the accepted package manifest count.
PASS: proposal does not claim all 4,681 UIDs were backfilled.
```

## 7. Forbidden-Claim Check

Checked absent or explicitly denied:

```text
production D4 merge;
production pool mutation;
all 4,681 UIDs backfilled;
strict AlphaFill equivalence;
hard filtering / automatic candidate deletion;
LLM strain selection;
trait_score;
uncalibrated confidence;
exact pollutant degradation proof from broad trait;
culture availability prediction;
fungal trait prediction included in current round.
```

Audit result:

```text
PASS: proposal is written as a proposal only.
PASS: no implementation, production, or teacher-freeze-for-C7-2 claim is made.
```

## 8. Remaining Before Upload

Before teacher-facing upload, recommended steps:

```text
1. user review of this local proposal;
2. if approved, copy proposal and audit into a dated microbe-side GitHub folder;
3. update microbe-side current teacher review entrypoint README;
4. generate MANIFEST.files / MANIFEST.sha256 / DELIVERABLE_SHA256SUMS.txt;
5. do not upload any private teacher-message draft.
```
