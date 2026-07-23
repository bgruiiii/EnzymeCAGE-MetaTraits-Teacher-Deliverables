# metaTraits Bounded Interface And Coverage Probe Report

Date: 2026-07-16

Authority:

```text
00_Authority_Teacher_Plan/
ENZYMECAGE_METATRAITS_INTEGRATION_TECHNICAL_FRAMEWORK_2026-07-14.md
```

Accepted evidence package:

```text
03_HPC_Returned_Result_Summaries/
metatraits_mt_d5a2_https_handler_and_required_evidence_final_correction_20260716/
metatraits_mt_d5a2_https_handler_and_required_evidence_final_correction_20260716.tar
metatraits_mt_d5a2_https_handler_and_required_evidence_final_correction_20260716.tar.identity.txt
```

Independent acceptance audit:

```text
04_Local_Review_Audits/
ENZYMECAGE_METATRAITS_MT_D5A2_ACCEPTED_RETURN_LOCAL_AUDIT_2026-07-16.md
```

## 1. Scope And Decision

This report closes the teacher-assigned bounded MT-D5 pre-research task. It
uses ten fixed Top-MRR P0 enzyme UIDs for enzyme-to-organism mapping and five
fixed organisms for current metaTraits interface and trait sampling.

The probe supports the following bounded decision:

```text
documented /api/v1 routes           unavailable at probe time
website taxon summary download      working for 5/5 fixed samples
bounded observation pages           working for 2/2 fixed pages
three-repeat payload stability      byte-identical after one allowed retry
production interface stability      not established
published rate-limit threshold      not documented / UNKNOWN
```

No model inference, training, GPU work, porTraits run, bulk observation export
or production implementation was performed.

## 2. Fixed Enzyme-To-Organism Probe

The ten fixed P0 UIDs all resolve to the same UniProt primary accession:

```text
UniProt accession exact/missing           10/0
KEGG single/missing/multiple               7/1/2
```

All ten sampled UniProt entries are reviewed, but `reviewed`, UniProt
`annotation_score`, protein-existence evidence and KEGG mapping multiplicity
are different evidence dimensions. No normalized organism-confidence value was
calculated.

KEGG cannot be treated as a guaranteed one-to-one replacement for UniProt in
this sample: one UID has no KEGG conversion and two have multiple conversions.
The ten-UID result does not prove production-wide mapping coverage.

## 3. Five Required Raw Summary JSON Bodies

All five bodies are current HTTP-200, JSON-compatible, strict top-level
list-of-object responses whose identities match the request ledger.

| UID | Query | Records | Bytes | SHA256 |
|---|---|---:|---:|---|
| `Q8EFP8` | `Shewanella oneidensis` | 146 | 55324 | `0d0eeecd9b5cd6314d71e680119b5fd155fac2980f59581436501ed2f42d0604` |
| `Q12WS1` | `Methanococcoides burtonii` | 134 | 50477 | `c3da972bb5214ef65f9631b48882dbd8eec96e2ebe0edb38901856ae96ec9e6b` |
| `A0A0H3C8X0` | `Caulobacter vibrioides` | 161 | 61707 | `99ca0fb51622ba9d30eba9befabe6e90f96750eac96f1af31f8638807479a0e5` |
| `Q6BQK1` | `Debaryomyces hansenii` | 9 | 3148 | `28b4e749f70dafba8ad5ccf5c1948ce9ce8623709959687c4ebfd718ca1f8735` |
| `P71875` | `Mycobacterium tuberculosis` | 147 | 56471 | `414606627724f0ada3dcbc5be618291d94378fa60b0756e9dd62741fd4faa202` |

Raw evidence paths, relative to the accepted package:

```text
raw/metatraits/samples/01_Q8EFP8/summary.json
raw/metatraits/samples/02_Q12WS1/summary.json
raw/metatraits/samples/03_A0A0H3C8X0/summary.json
raw/metatraits/samples/05_Q6BQK1/summary.json
raw/metatraits/samples/06_P71875/summary.json
```

The five bodies also happen to be byte-identical to the pinned earlier bodies.
That is a bounded freshness/stability observation, not a contract that public
data will never change.

## 4. Interface Findings

### 4.1 Documented API

Sixteen bounded logical requests covering the documented `/api/v1` route
family all returned HTTP 404 with headers and bodies saved:

```text
documented API probes                 16/16 HTTP 404
finding                               DOCUMENTED_API_ROUTE_NOT_LIVE_AT_PROBE_TIME
```

This proves that those documented routes were not usable during the probe. It
does not prove permanent removal or a general network outage.

### 4.2 Website summary and observation surfaces

The website taxon pages and `/taxon/download` summaries returned HTTP 200 for
all five fixed samples. Two bounded page-zero Shewanella observation requests
also returned HTTP-200 strict JSON:

| Tab | `recordsTotal` | `recordsFiltered` | Saved rows |
|---|---:|---:|---:|
| `Environmental_preferences` | 69 | 69 | 69 |
| `Metabolites` | 9 | 9 | 9 |

Actual observation rows contain `database_record`, `record_url`, `tax_id`,
`trait` and `value`. Current distinct Shewanella `tax_id` values are `70863`
and `211586`.

The website download/observation surfaces are useful bounded evidence, but they
must not silently be promoted to a documented production API contract.

### 4.3 Stability and transient behavior

The exact first successful Shewanella summary was requested three more times
in a fresh session. One first attempt had a TLS handshake timeout and was
recorded as a transient network exception; the allowed attempt-2 retry
succeeded. All three successful bodies are byte-identical:

```text
successful repeats                       3/3
successful-body SHA256
0d0eeecd9b5cd6314d71e680119b5fd155fac2980f59581436501ed2f42d0604
semantic equality                        3/3
```

This shows stable payloads in the bounded repeat window. The observed transient
failure and absence of an SLA mean production reliability is not established.

### 4.4 Rate behavior

```text
D5A2 attempts                              16
actual HTTP responses                      15
HTTP status 200                            15
transient network exceptions                1
local programming exceptions                0
observed HTTP 429                            0
published rate-limit threshold        UNKNOWN
```

Zero observed 429 in 15 responses does not establish an unlimited API or a
safe production request rate.

## 5. Wastewater-Relevant Trait Coverage

Coverage below means only that at least one matching trait record exists in
the current summary. It does not mean the organism is suitable for a treatment
scenario.

| Category | Samples with matching records | Total exact matching records |
|---|---:|---:|
| oxygen/atmosphere | 5/5 | 30 |
| temperature | 5/5 | 25 |
| pH | 5/5 | 13 |
| salinity | 5/5 | 19 |
| biofilm | 0/5 | 0 |
| safety/pathogenicity | 4/5 | 7 |
| wastewater metabolism | 4/5 | 158 |

`Debaryomyces hansenii` is sparse in this bounded sample: its summary contains
9 total records and no matching safety/pathogenicity or wastewater-metabolism
record. Missing records remain unknown, not negative evidence.

The five-sample probe is enough to expose interface and schema behavior, but it
is not a population estimate of wastewater-trait coverage.

## 6. No Robust Majority And Source Conflict

Exact `majority_label == "No robust majority"` counts are:

| UID | Total summary records | No robust majority | Percentage |
|---|---:|---:|---:|
| `Q8EFP8` | 146 | 12 | 8.219178% |
| `Q12WS1` | 134 | 2 | 1.492537% |
| `A0A0H3C8X0` | 161 | 24 | 14.906832% |
| `Q6BQK1` | 9 | 0 | 0.000000% |
| `P71875` | 147 | 5 | 3.401361% |
| aggregate | 597 | 43 | 7.202680% |

Three current Shewanella examples connect a no-robust-majority summary to
conflicting source observations. The saved examples include `obligate
aerobic`, `oxygen preference` and `presence of hemolysis`.

The aggregate percentage describes only these 597 current records. It is not a
global metaTraits conflict rate.

## 7. Evidence-Semantics Finding

The current data do not support the framework's proposed single three-state
field:

```text
experimental / predicted / no_robust_majority
```

The observed dimensions are independent:

```text
summary is_ai             independent boolean
summary majority_label    independent consensus label
observation source        database_record / record_url
observation value         source-specific value
```

`No robust majority` is a summary consensus condition, not a replacement for
source provenance or prediction status. A production schema must preserve
these dimensions separately; otherwise it will lose evidence and create
logically false categories.

## 8. Taxonomy Boundary

Current website queries used species names. The resulting observations contain
multiple taxon IDs, and species queries can collapse strains or multiple taxa.
No strain-preservation claim is justified.

The documented API describes NCBI taxonomy IDs. GTDB use requires an explicit,
versioned GTDB/NCBI crosswalk and must not be silently mixed with NCBI IDs.

## 9. Production Decision Boundary

The D5 probe supports further contract design, not immediate implementation.
Before `MicrobeTraitTool` is implemented, the teacher should confirm:

1. whether production uses a versioned official bulk snapshot, waits for the
   documented API, or explicitly authorizes the website surfaces as an
   experimental fallback;
2. the split evidence schema replacing the unsupported three-state field;
3. the NCBI/GTDB taxonomy-ID and strain-resolution policy;
4. retry, cache, freshness and rate limits without treating the bounded probe
   as an SLA.

The complete accepted evidence remains in the immutable D5A2 package and its
independent local audits.
