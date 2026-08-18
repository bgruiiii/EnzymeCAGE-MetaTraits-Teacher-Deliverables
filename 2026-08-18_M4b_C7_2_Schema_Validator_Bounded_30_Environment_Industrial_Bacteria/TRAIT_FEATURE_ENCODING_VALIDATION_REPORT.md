# C7-2 Trait Feature Encoding Validation Report

Date: 2026-08-18

Scope: read-only schema/validator implementation against a 30-row bounded staged subset.

## Overall

overall_pass: True
errors: 0
warnings_sampled: 50

## Subset

Rows: 30 = 10 target_bacteria + 10 target_archaea + 10 target_fungi.
All rows come from the teacher-accepted 1,704 staged PASS package and real UID-to-source_signature mappings.
P0DXV0 is not included.

## Prediction And Source Policy

MetaTraits values are read from local downloaded snapshots only; no online genome prediction was run.
BacDive values are read from prior audited local closure/cache tables only; no new BacDive API query was run.
F5 availability is observed-only and is never predicted.
Fungi rows are identity-only in this round.

## Bacteria First-Screen Coverage

The 10 bacteria rows are environmental/industrial-facing examples selected from the real staged PASS intersection.
First-screen traits follow the senior discussion display order: temperature, pH, oxygen/anaerobic status, salinity, and BacDive availability / culture collection.
The route is observed-first; prediction-like soft-fill is used only when observed evidence is missing and the F item is allowed by the frozen C7-2 policy.

| First-screen trait | OBSERVED_USED | PREDICTED_SOFT_FILL_USED | NOT_OBSERVED |
|---|---:|---:|---:|
| F2 temperature | 10 | 0 | 0 |
| F3 pH | 5 | 5 | 0 |
| F1 oxygen / anaerobic | 10 | 0 | 0 |
| F4 salinity | 8 | 2 | 0 |
| F5 BacDive availability / culture collection | 10 | 0 | 0 |

| UID | Organism | temperature | pH | oxygen / anaerobic | salinity | BacDive availability |
|---|---|---|---|---|---|---|
| A0A089LCJ8 | Paenibacillus borealis | OBSERVED_USED | OBSERVED_USED | OBSERVED_USED | OBSERVED_USED | OBSERVED_USED |
| Q09LY5 | Geobacillus stearothermophilus (Bacillus stearothermophilus) | OBSERVED_USED | OBSERVED_USED | OBSERVED_USED | OBSERVED_USED | OBSERVED_USED |
| P60338 | Thermus thermophilus | OBSERVED_USED | OBSERVED_USED | OBSERVED_USED | OBSERVED_USED | OBSERVED_USED |
| P0DX40 | Lactiplantibacillus plantarum (Lactobacillus plantarum) | OBSERVED_USED | OBSERVED_USED | OBSERVED_USED | PREDICTED_SOFT_FILL_USED | OBSERVED_USED |
| P0DW79 | Rhodococcus erythropolis (Arthrobacter picolinophilus) | OBSERVED_USED | PREDICTED_SOFT_FILL_USED | OBSERVED_USED | OBSERVED_USED | OBSERVED_USED |
| I6TCK3 | Paracoccus pantotrophus (Thiosphaera pantotropha) | OBSERVED_USED | PREDICTED_SOFT_FILL_USED | OBSERVED_USED | OBSERVED_USED | OBSERVED_USED |
| P80435 | Streptomyces anulatus (Streptomyces chrysomallus) | OBSERVED_USED | PREDICTED_SOFT_FILL_USED | OBSERVED_USED | OBSERVED_USED | OBSERVED_USED |
| Q01767 | Streptomyces clavuligerus | OBSERVED_USED | PREDICTED_SOFT_FILL_USED | OBSERVED_USED | OBSERVED_USED | OBSERVED_USED |
| Q52522 | Stutzerimonas stutzeri (Pseudomonas stutzeri) | OBSERVED_USED | PREDICTED_SOFT_FILL_USED | OBSERVED_USED | OBSERVED_USED | OBSERVED_USED |
| Q01698 | Thermus aquaticus | OBSERVED_USED | OBSERVED_USED | OBSERVED_USED | PREDICTED_SOFT_FILL_USED | OBSERVED_USED |

## Trait Status Counts

| Trait | OBSERVED_USED | PREDICTED_SOFT_FILL_USED | NOT_OBSERVED | FUNGI_IDENTITY_ONLY |
|---|---:|---:|---:|---:|
| F1 oxygen_tolerance | 10 | 0 | 10 | 10 |
| F2 temperature | 10 | 0 | 10 | 10 |
| F3 pH | 5 | 5 | 10 | 10 |
| F4 salinity | 8 | 2 | 10 | 10 |
| F5 bacdive_availability | 20 | 0 | 0 | 10 |
| F6 respiration_electron_acceptor | 4 | 6 | 10 | 10 |
| F7 carbon_and_substrate_utilization | 6 | 4 | 10 | 10 |
| F8 degradation_capacity_broad | 1 | 9 | 10 | 10 |
| F9 enzyme_activity | 8 | 0 | 12 | 10 |
| F10 motility | 10 | 0 | 10 | 10 |
| F11 cell_morphology | 10 | 0 | 10 | 10 |
| F12 cell_envelope_gram | 10 | 0 | 10 | 10 |
| F13 sporulation | 9 | 0 | 11 | 10 |
| F14 genome_basic | 10 | 0 | 10 | 10 |
| F15 habitat_generalism | 0 | 0 | 20 | 10 |

## Prediction Used Counts

{"F3": 5, "F4": 2, "F6": 6, "F7": 4, "F8": 9}

## Validation Errors

None

## Validation Warnings Sample

A0A089LCJ8 F15 NOT_OBSERVED means unknown, not biological absence
Q09LY5 F15 NOT_OBSERVED means unknown, not biological absence
P60338 F15 NOT_OBSERVED means unknown, not biological absence
P0DX40 F15 NOT_OBSERVED means unknown, not biological absence
P0DW79 F15 NOT_OBSERVED means unknown, not biological absence
I6TCK3 F13 NOT_OBSERVED means unknown, not biological absence
I6TCK3 F15 NOT_OBSERVED means unknown, not biological absence
P80435 F15 NOT_OBSERVED means unknown, not biological absence
Q01767 F9 NOT_OBSERVED means unknown, not biological absence
Q01767 F15 NOT_OBSERVED means unknown, not biological absence
Q52522 F15 NOT_OBSERVED means unknown, not biological absence
Q01698 F9 NOT_OBSERVED means unknown, not biological absence
Q01698 F15 NOT_OBSERVED means unknown, not biological absence
A8A8G1 F1 NOT_OBSERVED means unknown, not biological absence
A8A8G1 F2 NOT_OBSERVED means unknown, not biological absence
A8A8G1 F3 NOT_OBSERVED means unknown, not biological absence
A8A8G1 F4 NOT_OBSERVED means unknown, not biological absence
A8A8G1 F6 NOT_OBSERVED means unknown, not biological absence
A8A8G1 F7 NOT_OBSERVED means unknown, not biological absence
A8A8G1 F8 NOT_OBSERVED means unknown, not biological absence
A8A8G1 F9 NOT_OBSERVED means unknown, not biological absence
A8A8G1 F10 NOT_OBSERVED means unknown, not biological absence
A8A8G1 F11 NOT_OBSERVED means unknown, not biological absence
A8A8G1 F12 NOT_OBSERVED means unknown, not biological absence
A8A8G1 F13 NOT_OBSERVED means unknown, not biological absence
A8A8G1 F14 NOT_OBSERVED means unknown, not biological absence
A8A8G1 F15 NOT_OBSERVED means unknown, not biological absence
Q6L0M1 F1 NOT_OBSERVED means unknown, not biological absence
Q6L0M1 F2 NOT_OBSERVED means unknown, not biological absence
Q6L0M1 F3 NOT_OBSERVED means unknown, not biological absence
Q6L0M1 F4 NOT_OBSERVED means unknown, not biological absence
Q6L0M1 F6 NOT_OBSERVED means unknown, not biological absence
Q6L0M1 F7 NOT_OBSERVED means unknown, not biological absence
Q6L0M1 F8 NOT_OBSERVED means unknown, not biological absence
Q6L0M1 F9 NOT_OBSERVED means unknown, not biological absence
Q6L0M1 F10 NOT_OBSERVED means unknown, not biological absence
Q6L0M1 F11 NOT_OBSERVED means unknown, not biological absence
Q6L0M1 F12 NOT_OBSERVED means unknown, not biological absence
Q6L0M1 F13 NOT_OBSERVED means unknown, not biological absence
Q6L0M1 F14 NOT_OBSERVED means unknown, not biological absence
Q6L0M1 F15 NOT_OBSERVED means unknown, not biological absence
Q5JE27 F1 NOT_OBSERVED means unknown, not biological absence
Q5JE27 F2 NOT_OBSERVED means unknown, not biological absence
Q5JE27 F3 NOT_OBSERVED means unknown, not biological absence
Q5JE27 F4 NOT_OBSERVED means unknown, not biological absence
Q5JE27 F6 NOT_OBSERVED means unknown, not biological absence
Q5JE27 F7 NOT_OBSERVED means unknown, not biological absence
Q5JE27 F8 NOT_OBSERVED means unknown, not biological absence
Q5JE27 F9 NOT_OBSERVED means unknown, not biological absence
Q5JE27 F10 NOT_OBSERVED means unknown, not biological absence
