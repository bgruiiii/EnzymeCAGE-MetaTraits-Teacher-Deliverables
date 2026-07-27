# Organism ID Alignment Explicit Tri-State Supplement

Date: 2026-07-26  
Status: `COMPLETED_NEGATIVE_FINDING / EXPLICIT_CLASSIFICATION ADDED /
PRODUCTION PATH UNRESOLVED`

## 1. Purpose

This supplement makes the organism-ID result directly auditable under three
mutually exclusive classes:

```text
exact_strain
exact_species
no_exact_match_established
```

It does not add a new network probe or reinterpret a species-name query as an
exact TaxID match. It normalizes the already delivered ten-row result in
`P0_TOP_MRR_ENZYME_TO_HOST_METATRAITS_CROSSWALK.csv`.

## 2. Normative class definitions

### `exact_strain`

Use only when all of the following are evidenced:

1. the queried UniProt NCBI TaxID is a strain-level taxon;
2. a returned metaTraits record exposes a tax ID;
3. the returned tax ID exactly equals the queried TaxID.

A species-name match or a related species TaxID is insufficient.

### `exact_species`

Use only when all of the following are evidenced:

1. the queried UniProt NCBI TaxID is a species-level taxon;
2. a returned metaTraits record exposes a tax ID;
3. the returned tax ID exactly equals the queried TaxID.

A strain record under that species cannot be inherited into this class.

### `no_exact_match_established`

Use when exact TaxID equality cannot be demonstrated from the delivered
evidence. This includes:

- the documented TaxID endpoint returning HTTP 404;
- a working species-name summary that exposes no `tax_id`;
- no delivered summary;
- ambiguous or multiple related TaxIDs without exact equality.

This class means **the current evidence chain did not establish an exact
match**. It does not mean metaTraits definitely lacks the organism or trait.

## 3. Ten-row normalized result

| Order | Enzyme UID | UniProt TaxID | Existing bounded result | Explicit class |
|---:|---|---:|---|---|
| 1 | `Q8EFP8` | 211586 | TaxID API 404; species-name summary only | `no_exact_match_established` |
| 2 | `Q12WS1` | 259564 | TaxID API 404; species-name summary only | `no_exact_match_established` |
| 3 | `A0A0H3C8X0` | 565050 | TaxID API 404; species-name summary only | `no_exact_match_established` |
| 4 | `P29931` | 42445 | TaxID API 404; no delivered summary; host mapping conflict disclosed | `no_exact_match_established` |
| 5 | `Q6BQK1` | 284592 | TaxID API 404; species-name summary only | `no_exact_match_established` |
| 6 | `P71875` | 83332 | TaxID API 404; species-name summary only | `no_exact_match_established` |
| 7 | `S5SC42` | 484429 | TaxID API 404; no delivered summary | `no_exact_match_established` |
| 8 | `P76113` | 83333 | TaxID API 404; no delivered summary | `no_exact_match_established` |
| 9 | `C8WLM1` | 479437 | TaxID API 404; no delivered summary | `no_exact_match_established` |
| 10 | `Q02198` | 303 | TaxID API 404; no delivered summary | `no_exact_match_established` |

Counts:

```text
exact_strain:
  0
exact_species:
  0
no_exact_match_established:
  10

contextual species-name summary only:
  5
no delivered summary:
  5
```

The explicit class is also present row by row in the crosswalk column:

```text
metatraits_exact_id_alignment_class
```

## 4. Species/strain non-inheritance

The existing exact-tax-ID contract remains controlling:

```text
strain TaxID -> species trait:
  no inheritance

species TaxID -> strain trait:
  no inheritance

name-only species summary:
  contextual soft evidence only
  never exact strain evidence
```

Therefore the five species-name summaries do not count as
`exact_species` or `exact_strain`. They remain bounded contextual evidence.

## 5. Relationship to the previous ID fields

The existing crosswalk field `metatraits_id_alignment_state` records how the
bounded probe ended:

```text
taxid_api_404_species_name_summary_only:
  5

taxid_api_404_no_delivered_summary:
  5
```

The new `metatraits_exact_id_alignment_class` field answers the separate
teacher-facing question: was an exact strain TaxID, exact species TaxID, or no
exact TaxID match established?

The field `enzyme_to_host_mapping_state` concerns UniProt/KEGG enzyme-to-host
mapping and must not be confused with metaTraits ID alignment.

## 6. Decision boundary

```text
initial direct TaxID test:
  complete

exact production organism_uid -> traits path:
  unresolved

allowed current use of species-name summaries:
  contextual soft evidence only

exact strain/species trait assignment:
  forbidden unless exact TaxID equality is evidenced

M4b/M4c:
  not authorized
```

No exact-ID success is claimed, and no database absence is inferred from the
HTTP 404 result.
