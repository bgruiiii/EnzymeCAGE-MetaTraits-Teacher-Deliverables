# M4a Partial CPU Smoke Report

Date: 2026-07-19

## Scope and identity

This report covers only the teacher-authorized M4a-3 implementation of
`Enzyme2OrganismTool`, `OrganismAggregator`, and bounded offline tests. It is
not full M4a closure and does not authorize M4b or M4c.

- ADRMATS ZIP SHA256: `dc33c60b6876fed6969dc56a28a688077b17ef2f5a3510fadd78f085e13834b2`
- Declared commit: `ca5eabe1d521bbcb8aae67c0b2fd24f9f16667a5`
- Declared tree: `4a986ed4d2eca0c92523bc7c4133f60732350e68`
- `src/tools/base.py`: `cf1e9702fbc2edbdcbec7ce2ab98ba90ab4a23e7af7e65584a8d3e7096edc330`
- `src/tools/pubchem_tool.py`: `08c13a26b9a2578f5e9cbe50dad31a5d491c0b9d94157e6715f90a6c2f5018fb`
- `src/tools/crewai_pubchem_tool.py`: `4c249bb3a03e351933f3bdb3597d455073a3c17da27fe0625dbc56135455be29`
- `src/tools/epa_comptox_tool.py`: `de37c24a83d0c57bf543487009c636b027dc13942eee5a7b2af0bb05e37d924c`
- `src/tools/crewai_epa_comptox_tool.py`: `5bdaaad0e246801c950efe25826ba7f6f3df3a49337cf2be781fa3791d1f29be`
- `src/tools/__init__.py`: `813039db150a398a962e6e0d66599d1988b4dbaee907265611ad6519000b28d5`
- Payload SHA256: `83e5d167bd0012ca43fec0480f2ed19bd359b50e9d925ef50403d54bc5403704`
- Fixture cases SHA256: `fb39ca1388e320c0f7e6642e71991ed00332265bc076d0a75e54c96f508b332d`
- Fixture manifest SHA256: `f188569245d3384be8c6cb068fbfb37b04a9a5edada31041802acb5a4c39b181`
- Snapshot draft SHA256: `e7be952c34fd0425cd97c902830b01a475f764d56e68f8096d5913468f6d9d6f`
- Authoritative wrapper schema: `/root/projects/EnzymeCAGE-master/HPC_Returned_Result_Summaries/d4b_v11_wrapper_implementation_formal_smoke_20260716/enzymecage_wrapper/schema.py`
- Wrapper schema SHA256: `a27f33adf78bb2c7a9961d4372cfea0f7728ca91eb89e3b0a6cc7a1e6488fc35`
- Real `RankedEnzyme` compatibility test: PASS with exact UID, score, rank, and ensemble CI preservation.

The exact source ZIP was safely extracted twice. All 233 pre-existing regular
files remained byte-identical between implementation and immutable baseline;
only `microbe_crew/` was added.

## Offline test result

Command:

```text
python -m pytest -q microbe_crew/tests/test_enzyme2organism.py
```

Result: **15 passed, 0 failed, 0 skipped; exit 0**. `compileall` also exited 0.
No UniProt, KEGG, MetaTraits, model, checkpoint, CUDA, or GPU operation ran.

## Ten-UID reviewed UniProt evidence

| UID | NCBI taxon ID | Reviewed organism |
|---|---:|---|
| Q8EFP8 | 211586 | Shewanella oneidensis (strain ATCC 700550 / JCM 31522 / CIP 106686 / LMG 19005 / NCIMB 14063 / MR-1) |
| Q12WS1 | 259564 | Methanococcoides burtonii (strain DSM 6242 / NBRC 107633 / OCM 468 / ACE-M) |
| A0A0H3C8X0 | 565050 | Caulobacter vibrioides (strain NA1000 / CB15N) |
| P29931 | 42445 | Sinorhizobium sp |
| Q6BQK1 | 284592 | Debaryomyces hansenii (strain ATCC 36239 / CBS 767 / BCRC 21394 / JCM 1990 / NBRC 0083 / IGC 2968) |
| P71875 | 83332 | Mycobacterium tuberculosis (strain ATCC 25618 / H37Rv) |
| S5SC42 | 484429 | Sphingobium sp. (strain YBL2) |
| P76113 | 83333 | Escherichia coli (strain K12) |
| C8WLM1 | 479437 | Eggerthella lenta (strain ATCC 25559 / DSM 2243 / CCUG 17323 / JCM 9979 / KCTC 3265 / NCTC 11813 / VPI 0255 / 1899 B) |
| Q02198 | 303 | Pseudomonas putida |

UniProt fixture match: 10/10. Synthetic test-only TrEMBL and accession-mismatch
mutations were excluded and are not biological evidence.

## Independent KEGG supplement

| UID | State | Multiplicity | Complete gene IDs |
|---|---|---:|---|
| Q8EFP8 | single | 1 | `son:SO_1922` |
| Q12WS1 | single | 1 | `mbu:Mbur_1182` |
| A0A0H3C8X0 | single | 1 | `ccs:CCNA_01212` |
| P29931 | missing | 0 | — |
| Q6BQK1 | single | 1 | `dha:DEHA2E04576g` |
| P71875 | multiple | 2 | `mtu:Rv3526`, `mtv:RVBD_3526` |
| S5SC42 | single | 1 | `syb:TZ53_25070` |
| P76113 | multiple | 3 | `eco:b1449`, `ecj:JW5907`, `ecoc:C3026_08430` |
| C8WLM1 | single | 1 | `ele:Elen_2529` |
| Q02198 | single | 1 | `ag:AAB17356` |

Distribution: single/missing/multiple = **7/1/2**. P29931 retained its reviewed
UniProt host while KEGG remained missing. KEGG did not create organism candidates.

## Sparse and aggregator paths

Q6BQK1 retained reviewed *Debaryomyces hansenii* evidence at NCBI taxon 284592.
No trait or safety value was added.

The test-only aggregator input used E1/E2 for taxon 20, E3 for taxon 3, and E4
for taxon 11, with a duplicate E2 row. Exact output taxon order was
`[20, 3, 11]`: count descending first, then numeric NCBI taxon ID ascending.
The duplicate counted once; supporting UID/score/rank/CI fields were unchanged.

## Behavioral evidence and boundaries

- Inherited transient retry: PASS; one test-only connection failure then success.
- Inherited HTTP 4xx no-retry: PASS; exactly one UniProt attempt.
- Inherited minimum interval: PASS; mocked remaining sleep was exactly 0.75 s.
- Inherited TTL cache: PASS; repeated mapping issued no additional source request.
- Process singleton identity: PASS.
- CrewAI `BaseTool`, Pydantic `args_schema`, and parseable core JSON: PASS.
- Unmocked biological network denial guard: active for every test.
- Source errors/environment limitations: no final-suite source errors; dependencies were isolated under the fresh run path.
- Default v1 sorting: supporting-enzyme count descending, numeric NCBI taxon ID ascending.
- Complete A/B/C comparison status: **WAIT_TEACHER**; no formula or comparison table was fabricated.
- Snapshot status: **DRAFT_WAITING_TEACHER_REVIEW**.
- 100-warm/concurrency/VRAM status: **NOT_RUN_IN_CPU_STAGE**.
- M4b/M4c status: **NOT_AUTHORIZED**.
