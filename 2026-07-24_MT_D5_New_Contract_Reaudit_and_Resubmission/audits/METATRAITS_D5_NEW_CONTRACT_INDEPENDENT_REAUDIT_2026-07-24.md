# MetaTraits D5 New-Contract Independent Reaudit

Date: 2026-07-24

Verdict:

```text
P0_TOP_MRR_SOURCE_IDENTITY_PASS
TOP10_SELECTION_INDEPENDENT_RECOMPUTATION_PASS
TEN_ENZYME_TO_HOST_CROSSWALK_PASS_WITH_ONE_DISCLOSED_CONFLICT
FIVE_ORIGINAL_METATRAITS_JSON_PASS
FOUR_REQUIRED_REAL_SAMPLE_CHECKS_PASS_WITH_BOUNDED_CONCLUSIONS
TAXID_DIRECT_QUERY_NEGATIVE_RESULT_DISCLOSED_PASS
PRODUCTION_ID_ALIGNMENT_UNRESOLVED
NO_NEW_HPC_OR_NETWORK_RUN_PASS
TEACHER_ACCEPTANCE_NOT_CLAIMED
```

## 1. Audit interpretation

The 2026-07-24 teacher supplement requires actual checks on P0-derived host
organisms. It is not satisfied merely because an earlier file has the same
name or because the old D5 package was accepted under an earlier contract.

This reaudit separately checks:

1. P0 provenance;
2. enzyme-to-host derivation;
3. original metaTraits response identity;
4. interface stability;
5. wastewater-trait usefulness;
6. `No robust majority`;
7. rate-limit evidence;
8. organism-ID alignment.

## 2. P0 and host-chain audit

The five frozen ESM-2 3B seed test tables were independently hashed and match
the recorded v1 identities. A fresh read-only recomputation over 70,815 aligned
rows reproduced the stored ten UID order, reaction IDs, positive ranks and
ensemble means exactly:

```text
TOP10_MATCH_STORED=TRUE
```

All ten selected rows have `positive_rank=1` and MRR@10 contribution 1.0.
All ten exact primary accessions have reviewed UniProt organism/taxon
annotations. The combined crosswalk retains nine `exact` states and one
explicit `MAPPING_DRIFT_OR_CONFLICT` state for `P29931`.

The five trait samples are orders 1, 2, 3, 5 and 6 of that deterministic
ten-row P0 list. No unrelated organism was substituted.

## 3. Data-source audit

The source split is explicit and non-interchangeable:

```text
P0 rank evidence       frozen EnzymeCAGE v1 test tables
host mapping evidence  UniProt + supplemental KEGG
trait summary bodies   metaTraits /taxon/download
```

The five delivered summary bodies have the exact accepted SHA256 identities,
parse as strict top-level lists of objects, and contain 597 records total.

## 4. Four required checks

| Required check | Recomputed evidence | Audit result |
|---|---|---|
| interface/download stability | API 16/16 404; website summary 5/5 200; observation 2/2 200; repeats 3/3 byte-identical; one TLS timeout | PASS as bounded evidence; production stability not established |
| wastewater-trait usefulness | oxygen/temperature/pH/salinity 5/5; metabolism 4/5; safety 4/5; biofilm 0/5; one 9-record sample | PASS with decision: soft-trait prototyping only |
| `No robust majority` | 43/597 = 7.202680% | PASS; five-sample record proportion only |
| rate limit | 15 HTTP 200 responses, one network exception, zero 429, published threshold UNKNOWN | PASS as investigation; numeric rate not established |

The report now answers whether the data are useful on the sampled real host
organisms: useful for bounded soft evidence, insufficient for hard filtering,
exact strain attribution or production.

## 5. ID-alignment audit

The documented endpoint was tested with all ten UniProt NCBI tax IDs:

```text
GET /api/v1/traits/taxon/<taxonomy_id>
10/10 HTTP 404
```

The five successful summaries use species names. Summary objects have no
`tax_id`; bounded observation rows can contain multiple tax IDs under one
species query. Therefore the initial TaxID test is complete, but a working
`organism_uid -> traits` path is not.

The report correctly treats this as a negative result and leaves production
ID alignment unresolved.

## 6. Execution and preservation audit

No new HTTP request, HPC execution, GPU use, model inference, trait filtering,
M4b or M4c implementation was needed or performed. All quantitative results
were recomputed locally from accepted immutable response bodies.

The historical root report and five JSON bodies remain unchanged. This
delivery adds only the new-contract interpretation, a crosswalk, an audit and
a checksum manifest.

## 7. Conclusion

The teacher's four D5 research questions now have explicit answers on the five
P0-derived host samples. The result is scientifically bounded and does not
claim a usable TaxID API, complete trait coverage, production readiness or
teacher acceptance.
