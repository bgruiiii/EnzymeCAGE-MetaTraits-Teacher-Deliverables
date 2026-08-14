# M4b / C7-1 Trait Panel Candidate Table

Date: 2026-08-14

Status: candidate, pending teacher freeze.

Scope: Chen Haoran microbe-side M4b/C7 only. This document does not cover Gong Sai's reaction-prediction line and does not authorize production integration.

## Purpose

This C7-1 package submits a candidate trait panel for `TraitFilterLayer v1` under Huang teacher's 2026-08-14 authorization.

The panel is intentionally a staged soft trait layer:

```text
trait evidence assembler + soft compatibility annotator
```

It is not a hard filter, not an LLM strain selector, not a confidence-scoring model, and not a production integration.

## Authority And Inputs

Teacher authority:

- `00_Authority_Teacher_Plan/TEACHER_REPLY_M4_E2_SECOND_MILESTONE_AND_M4B_C7_AUTHORIZATION_2026-08-14.md`

Teacher C7-1 requirement:

```text
Submit trait panel candidate table.
For each trait include source database, evidence level, soft role, allowed/forbidden category reference, data-plane coverage, and senior/domain discussion record.
Teacher side will freeze traits item by item later.
```

Senior discussion record:

- `01_Path_Contract_Objective/M4b_C7_TraitFilterLayer_Initiation_Blueprint_2026-08-13/M4B_C7_SENIOR_DISCUSSION_QUESTIONS_2026-08-14.md`

Data-plane evidence:

- Microbe-side 2026-08-12 MetaTraits + BacDive deliverable.
- `metatraits_observed_vs_all_group2_summary.csv`
- `proposed_pollutant_degradation_trait_panel_for_domain_review.csv`
- `metatraits_confirmed_group2_coverage.csv`
- BacDive closure and representative strain expansion reports.

## Candidate Table

Machine-readable table:

- `C7_1_TRAIT_PANEL_CANDIDATE_TABLE_2026-08-14.csv`

The table contains these fields:

```text
panel_item
display_layer
source_database_or_table
metatraits_group_reference
example_traits_or_fields
evidence_level
soft_role
teacher_allowed_for_predicted_soft_fill
teacher_forbidden_boundary
data_plane_coverage
senior_discussion_note_2026_08_14
candidate_execution_note
pending_status
```

## Display Policy From Senior Discussion

Senior discussion result, 2026-08-14:

```text
Retain available candidate traits broadly, but present them in layers.
```

First-screen fields when a user submits a pollutant and receives multiple candidate microbes:

```text
temperature
pH
oxygen / anaerobic status
salinity
BacDive culture collection number / availability provenance
```

Detailed-on-request fields, shown when the user asks about a specific microbe:

```text
respiration / electron acceptor
carbon and substrate utilization
broad catabolic / degradation context
enzyme activity
motility
cell morphology
cell envelope / Gram context
sporulation
genome background
habitat generalism
BacDive representative strain / medium / isolation provenance
```

This display policy is not a scientific hard filter. It is only a user-facing presentation rule.

## Observed / Predicted Route

Senior discussion accepts the B route:

```text
Use observed/database records first.
If observed evidence is missing, selected categories may use predicted soft fill.
Predicted values must be labeled as predicted.
Predicted values must not be written as experimental facts.
Predicted values must not overwrite observed values.
```

Teacher-allowed predicted soft-fill categories:

```text
pH
salinity
temperature
atmosphere / oxygen preference
catabolic / carbon utilization
respiration / electron acceptor
```

Teacher-forbidden or excluded categories:

```text
biosafety
exact pollutant degradation
strain-specific traits
culture availability
```

## Explicit Exclusion: Biosafety Level

`biosafety level` is excluded from the C7-1 candidate trait panel.

Reason:

```text
Local MetaTraits extraction records biosafety level with source_database = BacDive=2025-07-29.
NCIT:C164457 is the ontology/concept identifier for "biosafety level", not the actual local source database.
BacDive/DSMZ examples label the field as German classification risk group / biosafety classification.
Senior discussion recommends deleting this trait from the first version because local school/lab import rules may differ.
```

Execution boundary:

```text
biosafety level does not enter C7-1 trait panel;
does not enter first-screen display;
does not become model input;
does not use predicted fill;
does not become an automatic exclusion rule;
does not remain as a C7 manual-review field in this round.
```

If strain import or experiment safety approval is needed later, it should be handled outside C7 according to local school/lab biosafety procedures.

## Fungal Policy

Teacher boundary:

```text
Fungi in this round are identity-only.
missing_reason = fungi_no_local_trait_source.
Do not write fungi as BacDive failures.
Do not apply bacterial/archaeal trait rules to fungi.
Fungal trait prediction must be separately evaluated and separately authorized.
```

Senior discussion:

```text
Keep fungal entries identity-only in this round.
Test whether fungal genome-based trait prediction tools are usable as a separate feasibility exploration.
Do not merge fungal prediction into current C7-1/C7-2.
```

## Data Coverage Notes

Main MetaTraits/BacDive universe:

```text
source_signature total = 2,478
enzyme-source rows = 145,607
MetaTraits species-level coverage = 1,638 / 2,478 = 66.1%
BacDive validated species-or-better = 1,746 / 2,478 = 70.5%
```

Important panel coverage examples:

```text
Temperature: all 1638/2478; no_predictions 1606/2478
Atmosphere: all 1631/2478; no_predictions 1528/2478
Salinity: all 1622/2478; no_predictions 919/2478
pH: all 1621/2478; no_predictions 420/2478
Carbon utilization: all 1614/2478; no_predictions 576/2478
Respiration: all 1611/2478; no_predictions 286/2478
Electron acceptor: all 1608/2478; no_predictions 7/2478
Enzyme activity: all 1611/2478; no_predictions 1150/2478
Habitat / Generalism: all 356/2478; no_predictions 0/2478
```

Interpretation:

```text
Prediction-like information mainly increases trait density among already covered species.
It does not increase total MetaTraits source coverage beyond 1,638 sources in the current snapshot.
```

## Non-Claims

This C7-1 package does not claim:

```text
the panel has reached teacher-side freeze;
any trait has production authorization;
any candidate microbe should be automatically selected;
any candidate microbe should be automatically removed;
any exact pollutant degradation ability is proven by a broad trait;
any species representative strain is the original UniProt exact strain;
any biosafety judgment is made by TraitFilterLayer;
any fungal prediction result is included in this round.
```

## Next Step

Submit this candidate panel for teacher review and item-by-item freeze.

After freeze, proceed only to C7-2 route/fungal policy as authorized. Do not jump to feature encoding, validator implementation, staged smoke, or production integration before the required freeze step.
