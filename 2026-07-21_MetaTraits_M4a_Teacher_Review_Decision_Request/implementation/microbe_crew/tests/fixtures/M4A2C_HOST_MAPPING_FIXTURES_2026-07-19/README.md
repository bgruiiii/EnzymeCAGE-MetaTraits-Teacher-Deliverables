# MetaTraits M4a-2C Host-Mapping Fixtures

Status: `FROZEN_FROM_TEACHER_ACCEPTED_MT_D5_EVIDENCE`

Date: 2026-07-19

This package freezes the ten accepted MT-D5 P0 UID cases for deterministic
`Enzyme2OrganismTool` development and testing. It contains no live-query result,
no inferred confidence and no M4b/M4c trait implementation.

## Binding Decisions Encoded

```text
UniProt reviewed record       primary host evidence
NCBI taxon ID                 production taxonomy key
KEGG conversion               independent supplementary evidence
KEGG multiplicity             preserve exact 0/1/N
TrEMBL/unreviewed             excluded from v1
organism_confidence float     prohibited in v1
```

The fixture does not encode the unresolved complete A/B/C comparison formulas.
It may carry the frozen EnzymeCAGE score as an input fact, but no host confidence,
weighted score or scientific-optimality claim is derived from it.

## Source Identities

Accepted raw source:

```text
03_HPC_Returned_Result_Summaries/
metatraits_mt_d5_interface_coverage_probe_20260716/
MANIFEST.sha256 SHA256:
9f646442d7ccd8ac24de4feb446825309059a92be8ca9d5d60b3d002edcb9503
```

Teacher acceptance and decisions:

```text
00_Authority_Teacher_Plan/
TEACHER_REPLY_MTD5_ACCEPTED_AND_MTD1_D8_DECISIONS_2026-07-18.md
```

Pinned ADRMATS source contract:

```text
git@github.com:Water-Quality-Risk-Control-Engineering/ADRMATS.git
commit ca5eabe1d521bbcb8aae67c0b2fd24f9f16667a5
```

## Contents

```text
host_mapping_cases.json       structured ten-case fixture contract
raw/uniprot/                  exact accepted UniProt response bodies
raw/kegg/                     exact accepted KEGG conversion bodies
FIXTURE_MANIFEST.sha256       hashes of fixture JSON and raw bodies
scripts/build_fixtures.py     deterministic source-to-fixture builder
scripts/validate_fixtures.py  independent semantic and hash validator
scripts/run_negative_tests.py semantic mutation tests
```

`Q8EFP8` uses the accepted successful `conversion.txt.attempt2` body. Its earlier
empty `conversion.txt` attempt is not silently promoted. `P29931` deliberately
retains an empty KEGG conversion as the required zero-mapping case. `P71875` and
`P76113` retain two and three KEGG gene mappings respectively.

## Rebuild

From this fixture directory:

```bash
python3 scripts/build_fixtures.py \
  --source-root ../../../03_HPC_Returned_Result_Summaries/metatraits_mt_d5_interface_coverage_probe_20260716 \
  --output-root .
python3 scripts/validate_fixtures.py .
python3 scripts/run_negative_tests.py .
```

The relative source path above is illustrative only; callers should use an exact
resolved source root and record it in their execution evidence.

## Boundaries

- The ten cases prove fixture behavior only, not production-wide coverage.
- Missing KEGG evidence is preserved as missing, not converted to failure.
- Species names do not prove strain preservation.
- No fixture field may be interpreted as organism suitability for wastewater.
- The sparse `Debaryomyces hansenii` case must remain present in later smoke work.
- M4b/M4c, porTraits, bulk observation scraping and training remain prohibited.
