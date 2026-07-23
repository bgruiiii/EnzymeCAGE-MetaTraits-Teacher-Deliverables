# EnzymeCAGE MetaTraits Task 4 Snapshot Contract Draft Local Audit

Date: 2026-07-22

Task scope: latest teacher reply MT-TQ-02 and Section 6.2.2 item 4 only.

Latest authority:

```text
00_Authority_Teacher_Plan/
TEACHER_REPLY_M3_P1_UNLOCK_CASE1_REBOUND_AND_METATRAITS_M4A_ADJUDICATION_2026-07-21.md
SHA256 57699b8a92ba6b555c96c0216c3961af0e80299d150b21979cb4fa7a19a18d57
```

Referenced MT-D5 authority:

```text
00_Authority_Teacher_Plan/
TEACHER_REPLY_MTD5_ACCEPTED_AND_MTD1_D8_DECISIONS_2026-07-18.md
```

The referenced authority file is stored under a 2026-07-18 filename and its
document body is dated 2026-07-16. This explains the latest teacher reply's
reference to the "2026-07-16 document Section 2.1"; it does not create two
different snapshot contracts.

## 1. Objective And Boundaries

Objective:

```text
Provide one SNAPSHOT_CONTRACT_DRAFT.md covering the exact teacher-required
version, update, license, local-path, hash-validation and online-fallback
decisions for separate teacher adjudication.
```

Only deliverable audited by this task:

```text
16_MetaTraits_Integration_Research_2026-07-15/02_Planning/
SNAPSHOT_CONTRACT_DRAFT.md
```

Forbidden in this task:

```text
start or implement M4b or M4c
run porTraits, bulk observation collection or model training
query the metaTraits website or API
promote current unversioned files to production
send the maintainer email
change M4a code, accepted scientific evidence or other teacher tasks
publish or submit the final consolidated teacher packet
```

## 2. Verdict

```text
TASK4_LOCAL_AUDIT_PASS
SNAPSHOT_CONTRACT_DRAFT_COMPLETE_PASS
ALL_SIX_LATEST_TEACHER_FIELDS_PASS
MT_D5_FALLBACK_CONTROLS_PASS
CURRENT_FILES_UNVERSIONED_CANDIDATES_ONLY_PASS
M4B_M4C_REMAIN_NOT_STARTED_PASS
NO_DRAFT_REWRITE_REQUIRED
SINGLE_DIRECT_FILE_READY_FOR_FINAL_TEACHER_DELIVERY
TEACHER_APPROVAL_NOT_YET_CLAIMED
```

The existing draft already satisfies the latest teacher request and is
byte-identical to the copy in the locally accepted M4a implementation return.
No content correction was justified. Task 4 therefore preserved the draft
byte-for-byte and created only this independent audit report.

Completing this task means the requested draft is locally ready for the final
teacher delivery. It does not mean the teacher has approved the contract, an
official upstream version exists, a production snapshot exists or M4b is
unlocked.

## 3. Requirement-To-Evidence Matrix

| Teacher requirement | Exact draft closure | Result |
|---|---|---|
| version fields | immutable `contract_schema_version`, `snapshot_id`, `upstream_version`, release/retrieval times, `files`, content-manifest hash and approval state | PASS |
| update frequency | 30-day discovery check plus maintainer notices; no automatic activation; promotion only on a new official version after validation | PASS as proposed policy pending teacher decision |
| license display | SPDX/URL, metaTraits attribution, source/version/snapshot identity in manifest, `LICENSE.txt`, `CITATION.txt` and redistributed evidence | PASS |
| local storage path | `data/metatraits/` with separate incoming, quarantine, immutable snapshots and atomic active pointer | PASS |
| hash validation | byte sizes, compressed and decompressed SHA256, gzip integrity, schema/header checks, canonical files-array hash and deterministic validator log | PASS |
| online fallback switch | explicit opt-in mode, valid snapshot retained, bounded single-taxon lookup, missing snapshot record or authorized freshness check, closed circuit and complete provenance | PASS |

The MT-D5 Section 2.1 controls beyond the six headline fields also close:

| Additional control | Draft closure | Result |
|---|---|---|
| website is experimental fallback only | production defaults to `snapshot_only`; website can never be the sole production dependency | PASS |
| TTL cache | 24 hours, keyed by adapter version and exact request | PASS |
| request spacing | global interval at least two seconds | PASS |
| circuit breaker | three consecutive failures return to snapshot-only behavior | PASS |
| complete provenance | request, timing, timeout, cache, status, body hash, parser, taxon, snapshot and circuit fields enumerated | PASS |
| replaceable adapter | snapshot, future official API and experimental website adapters are separated | PASS |
| timeout dimensions | connection, socket-read and end-to-end wall-clock controls remain distinct | PASS |
| no bulk observation scraping | explicitly prohibited | PASS |

## 4. Draft Identity And Structural Validation

Audited draft:

```text
SNAPSHOT_CONTRACT_DRAFT.md
bytes 14771
SHA256 e7be952c34fd0425cd97c902830b01a475f764d56e68f8096d5913468f6d9d6f
status DRAFT_FOR_TEACHER_REVIEW_NOT_PRODUCTION_APPROVED
contract draft version metatraits-snapshot-contract-v0.1
```

Byte comparisons:

```text
planning draft == accepted M4a-3A source copy                         PASS
planning draft == remote commit 65bbd2d planning copy                PASS
planning draft == remote commit 65bbd2d implementation source copy   PASS
```

Both illustrative JSON bodies parse strictly. Static checks found all nine
required content groups, including the six teacher fields, fallback controls
and forbidden-stage statements. The draft contains no `EnzymeCAGE` project
name, which is consistent with the latest MT-TQ-03 naming decision without
performing Task 6.

## 5. Candidate File Identity Recheck

The draft correctly labels all four current local downloads as unversioned
candidates rather than a production snapshot. Fresh local checks confirmed:

| Candidate file | Bytes | SHA256 | gzip |
|---|---:|---|---|
| `ncbi_species_summary_all.tsv.gz` | 36,900,021 | `9118379f800c5f2d8f0d0787ffd3045cbe3bb84a592657b06723252c13799bcd` | PASS |
| `ncbi_species_summary_no_predictions.tsv.gz` | 6,523,019 | `9e16ca57b94819fa591f32bc1cf194c82eae85b0dbbc454a3c1a449257a33873` | PASS |
| `GTDB2NCBI.tsv.gz` | 2,937,650 | `892ecf0410091e3f2b4c88e5e129cae3cc43117613b1745aa73f95ccdcfbb9e3` | PASS |
| `NCBI2GTDB.tsv.gz` | 2,895,086 | `761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd` | PASS |

These hashes establish local byte identity only. No official upstream version,
release cadence, production approval or maintainer response was inferred.

## 6. Prior Delivery Diagnosis

Read-only verification of the teacher-deliverables repository confirmed remote
commit:

```text
65bbd2d459591f068340467740e972a4a689a42d
```

The exact draft was present twice in the 2026-07-21 review packet, but only in
nested paths:

```text
planning/SNAPSHOT_CONTRACT_DRAFT.md
implementation/microbe_crew/SNAPSHOT_CONTRACT_DRAFT.md
```

The latest teacher reply nevertheless lists the draft as pending and requests
it as a next-round main deliverable. Therefore the final consolidated delivery
must present exactly one direct `SNAPSHOT_CONTRACT_DRAFT.md` rather than asking
the teacher to locate either nested copy. No remote write was performed by
Task 4.

## 7. Independent Self-Review

The task was checked for both omission and overreach:

```text
six latest teacher-required fields present                       PASS
all MT-D5 Section 2.1 fallback controls present                  PASS
JSON examples parse                                              PASS
candidate bytes/hashes/gzip independently rechecked              PASS
official-version absence disclosed                               PASS
teacher-review-only status retained                             PASS
M4b/M4c authorization not inferred                              PASS
no API request, scraping, code change, model run or email send  PASS
one requested draft, no invented companion deliverable          PASS
```

## 8. Task State

```text
Task 1: BLOCKED pending teacher clarification on RHEA:11880 versus C=15/2
Task 2: NOT STARTED as a separately accepted task
Task 3: LOCALLY AUDITED PASS
Task 4: LOCALLY AUDITED PASS; direct file ready for final delivery
Task 5 and later: NOT STARTED in the one-task-at-a-time workflow
M4b/M4c: NOT STARTED
```
