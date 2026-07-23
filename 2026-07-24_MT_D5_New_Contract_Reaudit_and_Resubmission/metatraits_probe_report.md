# metaTraits D5 New-Contract Probe Report

Date: 2026-07-24

Status:

```text
NEW_CONTRACT_REAUDIT_OF_ACCEPTED_2026_07_16_EVIDENCE
NO_NEW_NETWORK_REQUEST
NO_NEW_HPC_RUN
NO_NEW_MODEL_INFERENCE
```

## 1. Decision summary

This report re-evaluates the accepted 2026-07-16 D5A2 evidence against the
teacher's 2026-07-24 prerequisite contract. It does not treat the earlier
acceptance or the filename `metatraits_probe_report.md` as sufficient by
itself.

The bounded answer for the five real P0-derived host samples is:

```text
core soft-trait usefulness
  oxygen / temperature / pH / salinity      sufficient in 5/5 samples

incomplete dimensions
  wastewater metabolism                     present in 4/5 samples
  safety/pathogenicity                      present in 4/5 samples
  biofilm                                   present in 0/5 samples
  one sparse organism                       only 9 total summary records

decision
  SUFFICIENT_FOR_BOUNDED_SOFT_TRAIT_PROTOTYPING
  NOT_SUFFICIENT_FOR_HARD_FILTERING_OR_PRODUCTION
```

The data are useful for conservative soft-trait exploration on this bounded
sample. They are not complete enough for irreversible exclusion, exact
strain-level attribution, or production claims.

## 2. What came from which source

The evidence chain has three distinct sources:

```text
P0 Top-MRR enzyme selection
  EnzymeCAGE frozen v1 ESM-2 3B corrected-pocket test tables, seeds 40--44

enzyme UID -> host organism/taxon
  reviewed UniProt entries, with KEGG as independent supplemental evidence

host species -> trait summary JSON
  metaTraits website /taxon/download endpoint
```

The hosts were not discovered from metaTraits. The five trait JSON bodies were
downloaded from metaTraits only after host organisms had been mapped from the
P0 enzyme UIDs.

## 3. P0 Top-MRR selection provenance

The five frozen P0 seed tables contain 70,815 aligned test rows each. Their
SHA256 identities match the frozen `enzymecage_v1_20260714` package.

The deterministic selection procedure was:

1. group candidates by canonical reaction;
2. rank each reaction's candidates by five-seed ensemble mean;
3. retain the highest-ranked positive enzyme from each valid reaction group;
4. sort by positive rank, then ensemble mean and deterministic tie-breakers;
5. retain the first ten distinct enzyme UIDs.

All ten selected enzymes have `positive_rank=1` and
`mrr_at_10_contribution=1.0`. Therefore "Top-MRR enzyme" here means the
first-positive enzyme from a maximum-MRR-contribution reaction group. MRR is a
reaction-group ranking metric, not an independent per-enzyme metric.

An independent 2026-07-24 recomputation reproduced all ten rows exactly:

```text
P0_ROWS_RECOMPUTED=70815
TOP10_MATCH_STORED=TRUE
```

The complete ten-row chain is in
`P0_TOP_MRR_ENZYME_TO_HOST_METATRAITS_CROSSWALK.csv`.

## 4. Ten hosts and five metaTraits samples

All ten selected UIDs resolve to their exact primary accession in reviewed
UniProt entries and contain direct organism/taxon annotations. Nine combined
mapping states are `exact`; `P29931` is retained as
`MAPPING_DRIFT_OR_CONFLICT` because its *Sinorhizobium sp.* mapping is
ambiguous across the probed mapping/query surfaces.

The five successful metaTraits samples are a fixed subset of those ten:

| P0 order | Enzyme UID | UniProt host annotation | UniProt tax ID | metaTraits query |
|---:|---|---|---:|---|
| 1 | `Q8EFP8` | *Shewanella oneidensis* MR-1 | 211586 | `Shewanella oneidensis`, species |
| 2 | `Q12WS1` | *Methanococcoides burtonii* ACE-M | 259564 | `Methanococcoides burtonii`, species |
| 3 | `A0A0H3C8X0` | *Caulobacter vibrioides* NA1000 | 565050 | `Caulobacter vibrioides`, species |
| 5 | `Q6BQK1` | *Debaryomyces hansenii* CBS 767 and synonyms | 284592 | `Debaryomyces hansenii`, species |
| 6 | `P71875` | *Mycobacterium tuberculosis* H37Rv | 83332 | `Mycobacterium tuberculosis`, species |

"Host" here means the organism/taxon directly attached to the reviewed
UniProt protein entry. It does not by itself prove that the organism performs
a target wastewater transformation under environmental conditions.

The successful metaTraits summaries are species-name aggregates. They must not
be represented as exact strain-level trait records.

## 5. Five original metaTraits JSON bodies

Each body is directly visible in the teacher-deliverables repository:

| UID | Records | Bytes | SHA256 |
|---|---:|---:|---|
| `Q8EFP8` | 146 | 55,324 | `0d0eeecd9b5cd6314d71e680119b5fd155fac2980f59581436501ed2f42d0604` |
| `Q12WS1` | 134 | 50,477 | `c3da972bb5214ef65f9631b48882dbd8eec96e2ebe0edb38901856ae96ec9e6b` |
| `A0A0H3C8X0` | 161 | 61,707 | `99ca0fb51622ba9d30eba9befabe6e90f96750eac96f1af31f8638807479a0e5` |
| `Q6BQK1` | 9 | 3,148 | `28b4e749f70dafba8ad5ccf5c1948ce9ce8623709959687c4ebfd718ca1f8735` |
| `P71875` | 147 | 56,471 | `414606627724f0ada3dcbc5be618291d94378fa60b0756e9dd62741fd4faa202` |

The request ledger records for all five:

```text
URL host        metatraits.embl.de
endpoint        /taxon/download
HTTP status     200
content type    application/json
body contract   strict top-level list of objects
```

These are original HTTP response bodies, not collapsed conclusions or
reconstructed JSON.

## 6. Actual four-question validation

### 6.1 Interface and download stability

```text
documented /api/v1 logical probes             16/16 HTTP 404
website taxon summary downloads                5/5 HTTP 200 strict JSON
bounded observation pages                      2/2 HTTP 200 strict JSON
successful Shewanella repeat bodies             3/3 byte-identical
transient TLS handshake timeout                    1
```

Decision:

```text
BOUNDED_WEBSITE_DOWNLOAD_USABLE_WITH_RETRY
DOCUMENTED_API_UNAVAILABLE_AT_PROBE_TIME
PRODUCTION_STABILITY_NOT_ESTABLISHED
```

The five successful downloads and three byte-identical repeats demonstrate a
usable bounded website surface. One TLS timeout, the API 404 result, and the
absence of an SLA prevent a production-stability claim.

### 6.2 Wastewater-relevant trait usefulness

Coverage was recomputed from the five delivered raw bodies:

| Category | Samples with matches | Exact matching records | Bounded usefulness |
|---|---:|---:|---|
| oxygen/atmosphere | 5/5 | 30 | usable as soft evidence |
| temperature | 5/5 | 25 | usable as soft evidence |
| pH | 5/5 | 13 | usable as soft evidence |
| salinity | 5/5 | 19 | usable as soft evidence |
| biofilm | 0/5 | 0 | unavailable in this sample |
| safety/pathogenicity | 4/5 | 7 | incomplete; manual review required |
| wastewater metabolism | 4/5 | 158 | useful but incomplete |

Record presence means only that relevant trait observations exist. It does not
prove wastewater suitability. Missing records are unknown, not negative
biological evidence.

### 6.3 `No robust majority`

| UID | Total records | `No robust majority` | Percentage |
|---|---:|---:|---:|
| `Q8EFP8` | 146 | 12 | 8.219178% |
| `Q12WS1` | 134 | 2 | 1.492537% |
| `A0A0H3C8X0` | 161 | 24 | 14.906832% |
| `Q6BQK1` | 9 | 0 | 0.000000% |
| `P71875` | 147 | 5 | 3.401361% |
| aggregate | 597 | 43 | 7.202680% |

This is a five-sample record proportion, not a global metaTraits rate.

### 6.4 Rate-limit behavior

The final correction run recorded:

```text
D5A2 attempts                         16
completed HTTP responses              15
HTTP 200                              15
transient network exceptions           1
HTTP 429                               0
published rate-limit threshold   UNKNOWN
```

Decision:

```text
NO_429_OBSERVED_IN_BOUNDED_SERIAL_PROBE
NUMERIC_RATE_LIMIT_NOT_ESTABLISHED
```

Zero observed 429 does not prove an unlimited service or authorize a
production request rate.

## 7. Organism-ID alignment result

The original probe did test the documented NCBI TaxID route for all ten
P0-derived host tax IDs:

```text
GET /api/v1/traits/taxon/<taxonomy_id>
result: 10/10 HTTP 404
```

The working five summaries instead used species-name queries. Summary records
contain no `tax_id` field. Bounded source-observation rows expose tax IDs, but
a species query may include the target species and multiple strain/taxon IDs.

Therefore:

```text
tax-ID direct-query initial test                 complete
documented tax-ID API usable                     no
species-name website summary usable              yes, bounded
exact strain-level trait attribution             not established
production organism_uid -> traits path           unresolved
```

This is a completed negative alignment finding, not a working ID-aligned data
path. A future data-plane decision must use an official versioned snapshot,
a restored stable API, or another separately approved mapping route.

## 8. Scope and next gate

No new HPC execution is required to answer the four D5 questions: the accepted
D5A2 return already contains the raw HTTP bodies, request ledger, repeat
evidence and deterministic analyses. This new-contract report only makes the
previously collected evidence and its decision boundaries explicit.

This report does not start M4b or M4c, authorize hard filtering, select a
production data plane, or claim teacher acceptance. Teacher review is still
required.
