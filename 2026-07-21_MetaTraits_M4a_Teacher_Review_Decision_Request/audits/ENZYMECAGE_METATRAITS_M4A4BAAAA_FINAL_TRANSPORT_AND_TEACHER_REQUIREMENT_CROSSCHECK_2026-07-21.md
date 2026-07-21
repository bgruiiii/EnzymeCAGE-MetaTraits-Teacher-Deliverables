# MetaTraits M4a-4BAAAA Final Transport And Teacher Requirement Crosscheck

Date: 2026-07-21

Scope:

```text
03_HPC_Returned_Result_Summaries/
metatraits_m4a4baaaa_adversarial_status_and_transcript_semantics_final_correction_20260721/

03_HPC_Returned_Result_Summaries/
metatraits_m4a4baaaa_adversarial_status_and_transcript_semantics_final_correction_20260721.tar

03_HPC_Returned_Result_Summaries/
metatraits_m4a4baaaa_adversarial_status_and_transcript_semantics_final_correction_20260721.tar.identity.txt
```

Primary teacher authority:

```text
00_Authority_Teacher_Plan/
TEACHER_REPLY_MTD5_ACCEPTED_AND_MTD1_D8_DECISIONS_2026-07-18.md
```

## 1. Final Verdict

```text
M4A4BAAAA_DIRECTORY: PASS
M4A4BAAAA_TAR: PASS
M4A4BAAAA_IDENTITY: PASS
M4A4BAAAA_THREE_PART_TRANSPORT: PASS
PACKAGED_VALIDATOR_CAPTURED: PASS
POSITIVE_STATUS_FIXTURES_FROM_TAR: PASS_6_OF_6
NEGATIVE_SUITE_FROM_TAR: PASS_73_OF_73
NEW_ADVERSARIAL_RECHECKS: PASS_5_OF_5_REJECTED
SCIENTIFIC_EVIDENCE_RECOMPUTE: PASS
GPU_RERUN_REQUIRED: NO
M4A_EXECUTABLE_ENGINEERING_EVIDENCE: COMPLETE_FOR_CURRENT_SCOPE
FULL_TEACHER_CLOSURE: NOT_YET_TEACHER_ACCEPTED
M4B_M4C: NOT_AUTHORIZED
```

M4a-4BAAAA is accepted locally as the final M4a-4 benchmark/validator evidence
package. It closes the five M4a-4BAAA adversarial semantic gaps and preserves
the inherited M4a-4B scientific benchmark bytes unchanged.

This does not mean the whole MetaTraits task can be reported as teacher-closed
without qualifications. Several items in the teacher reply are explicitly
teacher-review or teacher-decision gates and must be returned to the teacher
as such.

## 2. Tar And Identity Audit

External identity values recomputed locally:

```text
tar bytes actual: 2355200
tar bytes identity: 2355200
tar SHA256 actual: 809bc2c14e087e8a0bca2f674024084444f88b19c2c5b23c357fdfc6bbf255a8
tar SHA256 identity: 809bc2c14e087e8a0bca2f674024084444f88b19c2c5b23c357fdfc6bbf255a8
identity match: true
identity file bytes: 2354
```

Tar structure:

```text
member count: 86
regular files: 80
directories including root: 6
single top-level root: true
absolute/parent-traversal/backslash paths: 0
links/devices/FIFOs/sockets: 0
uid/gid: 0/0
uname/gname: root/root
mtime: 0
directory modes: 0755
script modes: 0755
ordinary file modes: 0644
```

The tar uses a deterministic directory-first sorted member order: root,
subdirectories, then regular files. Rebuilding the tar from the extracted tree
with the same directory-first sorted order and normalized POSIX USTAR metadata
was byte-identical:

```text
rebuilt bytes: 2355200
rebuilt SHA256: 809bc2c14e087e8a0bca2f674024084444f88b19c2c5b23c357fdfc6bbf255a8
byte-identical reconstruction: PASS
```

The separately copied convenience directory has `scripts/*.py` mode `0644`,
while the tar stores the required `0755`. All regular-file bytes match between
the convenience directory and tar extraction. This is a nonblocking transfer
mode loss; the tar is the authoritative package artifact.

## 3. Extracted Package Validation

After safe extraction to `/tmp`:

```text
MANIFEST.sha256: 79/79 OK
file set equals convenience directory: true
regular-file byte mismatches: 0
extracted script modes: 0755
pyc/__pycache__ before and after reruns: 0
```

Package self-validation from tar extraction:

```text
packaged validator:
  exit code = 0
  stderr bytes = 0
  token = M4A4B_BENCHMARK_READY_FOR_LOCAL_AUDIT_COEXISTENCE_OPEN

positive fixture runner:
  exit code = 0
  stderr bytes = 0
  rows = 6
  result = 6/6 PASS

negative suite runner:
  exit code = 0
  stderr bytes = 0
  rows = 73
  result = 73/73 PASS
```

The five independent local adversarial rechecks also reject correctly:

```text
A01 INCOMPLETE blocker/row mismatch -> exit 1, incomplete_blocker_evidence
A02 BLOCKED_PROVENANCE inside accepted root -> exit 1, provenance_blocker_semantics
A03 BLOCKED_GPU contradictory message -> exit 1, gpu_blocker_schema
A04 packaged transcript extra contradictory line -> exit 1, transcript_cross_consistency
A05 READY malformed UTC -> exit 1, call_utc
```

## 4. Scientific Evidence Recompute

Inherited benchmark evidence remains internally consistent:

```text
warmups rows: 5/5 success and integrity pass
sequential rows: 100/100 success and integrity pass
concurrency_2 rows: 100/100 success and integrity pass
concurrency_4 rows: 100/100 success and integrity pass
total global request IDs: 305 unique

latency summaries:
  sequential: recompute PASS
  concurrency_2: recompute PASS
  concurrency_4: recompute PASS

memory rows: 6917
memory phase order:
  baseline -> preload -> warmups -> sequential -> concurrency_2 -> concurrency_4 -> final
memory summary row counts: recompute PASS

benchmark stderr warning counts:
  Mean of empty slice = 1525
  invalid value encountered in scalar divide = 1513
fatal stream terms:
  Traceback/CUDA OOM/prediction exception = absent
```

The warning counts remain disclosed metric-only all-zero synthetic-label AUC
warnings. They do not make the run warning-free.

## 5. Teacher Requirement Crosscheck

The table below compares the latest accepted evidence against the teacher's
2026-07-18 requirements. `PASS` means locally satisfied for the authorized M4a
scope. `WAIT_TEACHER` means the work is prepared or evidenced but cannot be
truthfully closed without a teacher ruling or review.

| Teacher item | Local result | Verdict |
|---|---|---|
| MT-D5 accepted and do not repeat probing | D5 accepted package preserved; no new D5 probe needed. | `PASS` |
| API path A: produce `SNAPSHOT_CONTRACT_DRAFT.md` with version, update frequency, license, local path, hash and fallback switch conditions | Draft exists and local audit closes all required fields. It is still a teacher-review draft, not production approval. | `PASS_LOCAL_DRAFT; WAIT_TEACHER_REVIEW` |
| API path B: draft maintainer inquiry email | English email draft exists, asks `/api/v1` retirement/replacement/bulk snapshot questions and is explicitly unsent. | `PASS_LOCAL_DRAFT; WAIT_TEACHER_REVIEW_AND_SEND` |
| API path C: website endpoint fallback only with TTL, >=2s spacing, provenance, circuit breaker and replaceable adapter | Snapshot contract draft includes these controls and does not make website endpoint production primary. | `PASS_LOCAL_DRAFT` |
| Do not put M4b online without snapshot | M4b not started; current local downloads remain unversioned candidates only. | `PASS` |
| Schema v1.1: `is_ai`, `majority_label`, source database/url/tax_id separated; no three-state `evidence` field | Recorded as future M4b/M4c schema policy. M4a does not consume traits and therefore does not implement this layer. | `PASS_BOUNDARY; FUTURE_NOT_AUTHORIZED` |
| MT-D1 UniProt reviewed organism/taxon ID primary; KEGG supplementary with 0/1/N multiplicity; TrEMBL excluded | M4a-3A accepted: 10/10 reviewed UniProt fixtures; KEGG 7/1/2 preserved; unreviewed negative rejected. | `PASS` |
| MT-D2 no `organism_confidence` float | M4a-3A accepted and negative test rejects prohibited confidence field. | `PASS` |
| MT-D3 v1 default B ordering | M4a-3A accepted default ordering: supporting-enzyme count descending and NCBI taxon ID ascending. | `PASS_WITH_DISCLOSURE` |
| MT-D3 smoke should report A/B/C differences | Complete A/B/C formulas remain teacher-pending because confidence was removed and source documents conflict on B/C semantics. Do not fabricate columns. | `WAIT_TEACHER` |
| MT-D4 all traits soft/uncertain in v1; biofilm unknown; no irreversible filtering | M4b not started; M4a docs preserve this boundary. | `PASS_BOUNDARY` |
| MT-D6 future LLM prompt hard-constraint discipline | M4c not started; prompt requirements preserved for later. | `PASS_BOUNDARY` |
| MT-D7 independent `MicrobeCrew` | M4a source is under `microbe_crew/` and is separate from AdsorptionCrew. | `PASS` |
| MT-D8 startup preload default until evidence exists | M4a-4 uses startup preload; runtime evidence confirms checkpoint load once and singleton reuse. | `PASS` |
| MT-D8 100 warm P50/P95/P99 and concurrency 2/4 degradation | M4a-4BAAAA inherits accepted 305-call benchmark: 100 sequential and 100 each for concurrency 2/4; summaries recompute. | `PASS` |
| MT-D8 peak GPU memory with ADRMATS other models coexisting | M4a-4P/M4a-4PBB evidence found zero additional local ADRMATS GPU models/checkpoints/load entrypoints; M4a-4 measured EnzymeCAGE-in-ADRMATS process memory. Do not call zero-model coexistence PASS without teacher interpretation. | `WAIT_TEACHER_INTERPRETATION` |
| Taxonomy: NCBI taxon ID production key; GTDB only by versioned crosswalk; species query does not promise strain preservation; preserve all tax IDs | M4a output uses NCBI taxon ID; no GTDB silent mix. Student-identified exact-strain/species trait attribution policy remains teacher-pending before later trait consumption. | `PASS_M4A; WAIT_TEACHER_POLICY_FOR_TRAITS` |
| Timeout dimensions separate | Snapshot contract draft separates connection, socket-read and end-to-end wall-clock timeouts. | `PASS_LOCAL_DRAFT` |
| Debaryomyces sparse sample retained | Q6BQK1 / *Debaryomyces hansenii* retained in smoke report; no trait/safety fabrication. | `PASS` |
| M4a authorized deliverables: `Enzyme2OrganismTool`, `OrganismAggregator`, tests, `M4A_SMOKE_REPORT.md`, `SNAPSHOT_CONTRACT_DRAFT.md` | M4a-3A accepted implementation/tests/report/snapshot draft; M4a-4BAAAA accepted benchmark evidence. Smoke report remains partial until A/B/C and final teacher decisions are incorporated. | `PASS_EXECUTABLE; FINAL_REPORT_UPDATE_NEEDED` |
| Do not start M4b/M4c | No accepted M4b/M4c implementation; scope files report unauthorized. | `PASS` |
| Do not execute porTraits, bulk observation scraping or model training | No such action in accepted M4a evidence. | `PASS` |

### 5.1 Disclosure On Default Tie-Break

The teacher's MT-D3 prose says v1 B is "supporting-enzyme count descending +
UID ascending tie-break." The accepted local M4a matrix and M4a-3A audit
freeze the implemented tie-break as count descending plus numeric NCBI taxon ID
ascending for organism candidates.

This is not treated as a hidden failure because it was explicitly audited and
accepted in the M4a matrix, but it must be disclosed in the teacher-facing
packet. If the teacher intended enzyme UID rather than organism/taxon tie-break
at the candidate level, the teacher should correct the formula in `MT-TQ-01`.

## 6. Remaining Teacher-Facing Items

The current engineering/HPC work is complete for the authorized M4a execution
scope. The following must still be sent to the teacher or preserved as pending
before claiming full teacher closure:

```text
MT-TQ-01: exact A/B/C formulas, source fields and deterministic tie-breaks
MT-TQ-02: approval/amendment of SNAPSHOT_CONTRACT_DRAFT.md
MT-TQ-03: maintainer email recipient/signature/project-name/wording, then sent-date evidence
MT-TQ-04: final checkpoint loading strategy after accepted benchmark evidence
MT-TQ-06: zero-additional-local-model coexistence interpretation
MT-TQ-07: exact-tax-ID versus species/sibling-strain trait attribution policy
MT-EQ-01: maintainer facts on API replacement and official versioned snapshot
```

Do not ask for M4b/M4c authorization as if it were already granted. Do not
promote the current website endpoint or unversioned files to production
snapshot status.

## 7. Final Local State

```text
M4A3A_IMPLEMENTATION_AND_OFFLINE_TEST_STAGE_LOCALLY_ACCEPTED
M4A4BAAAA_BENCHMARK_VALIDATOR_TRANSPORT_LOCALLY_ACCEPTED
M4A_EXECUTABLE_EVIDENCE_READY_FOR_TEACHER_REVIEW_PACKET
FULL_M4A_TEACHER_CLOSURE_NOT_CLAIMED
M4B_M4C_NOT_AUTHORIZED
NO_GPU_RERUN_REQUIRED
```

The next local action is not another HPC run. Prepare/update the teacher-facing
MetaTraits M4a review packet with this final audit, the M4a-3A implementation
audit, the snapshot/email drafts, and the pending decision questions above.
