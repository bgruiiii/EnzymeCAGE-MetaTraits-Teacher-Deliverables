# MetaTraits Pending Decisions And Preparation Queue

Date: 2026-07-18

Last evidence update: 2026-07-21

Purpose: keep teacher/external decisions separate from work that can be
completed now. This register is MetaTraits-only.

Primary authority:

```text
00_Authority_Teacher_Plan/
TEACHER_REPLY_MTD5_ACCEPTED_AND_MTD1_D8_DECISIONS_2026-07-18.md
```

## 1. Working Rule

```text
DO_NOW:
  Complete every task that has sufficient authority and evidence.
  Audit each local or Chenyu result before using it.

WAIT:
  Do not invent a teacher formula, official upstream version, API contract,
  expert threshold or production approval.

CONSOLIDATE:
  When the pending replies arrive, incorporate them together, rerun the
  affected gates and prepare one truthful teacher-facing closure summary.
```

## 2. Pending Decision Register

| ID | Owner | Exact pending item | Current status | Blocks | Does not block | Closure evidence |
|---|---|---|---|---|---|---|
| `MT-PEND-01` | Teacher | Resolve the textual inconsistency in A/B/C names and formulas for the required M4a comparison table, and disambiguate MT-D3 "UID ascending" tie-break. | `QUESTION_SENT_WAITING_REPLY` | Final A/B/C comparison and its smoke-report closure; any correction if teacher meant a UID other than numeric NCBI taxon ID | Teacher-authorized v1 default count-descending order as currently operationalized with numeric NCBI taxon ID ascending; snapshot/email work; source inventory | New teacher authority text with explicit A, B and C formulas and tie-breaks, including the exact UID field |
| `MT-PEND-02` | Teacher | Review and approve or amend `SNAPSHOT_CONTRACT_DRAFT.md`. | `DRAFT_READY_WAITING_REVIEW` | Calling the draft teacher-approved; later snapshot production promotion | M4a host mapping, source inventory and fixture preparation | Teacher approval/amendment with version/update/license/storage/hash/fallback decisions |
| `MT-PEND-03` | Teacher | Review `METATRAITS_API_INQUIRY_EMAIL_DRAFT.md`, verify recipient, signature and whether to retain the EnzymeCAGE name, then send it. | `DRAFT_READY_UNSENT` | Claiming maintainer contact or waiting for an official API answer | All local M4a preparation | Teacher-approved final email identity and sent-date evidence |
| `MT-PEND-04` | metaTraits maintainers | Confirm `/api/v1` status, replacement endpoint and official versioned bulk snapshot/version/checksum/license metadata. | `NOT_CONTACTED_YET` | Production snapshot identity; official API adapter choice; promotion of current unversioned downloads | M4a enzyme-to-organism mapping and deterministic default aggregation | Saved maintainer response with date, sender identity and exact technical answers |
| `MT-PEND-05` | Local source audit / Chenyu transport | Preserve the pinned ADRMATS source/interface identity and accepted M4a-3A transport; keep the earlier blocked M4a-2 preflight transport historically separate. | `M4A3A_SOURCE_IMPLEMENTATION_TRANSPORT_LOCALLY_ACCEPTED; HISTORICAL_M4A2_BLOCKED_RETURN_NONBLOCKING` | No current M4a implementation gate; only any claim that the earlier blocked search package itself was transport-accepted | All current M4a work against pinned commit `ca5eabe1d521bbcb8aae67c0b2fd24f9f16667a5` | Accepted M4a-3A tar/identity/local audit remain canonical; do not relabel the historical blocked return |
| `MT-PEND-06` | Teacher after M4a benchmark | Select final checkpoint loading strategy after 100-warm, concurrency-2/4 and bounded VRAM evidence. | `M4A4BAAAA_BENCHMARK_EVIDENCE_ACCEPTED_WAITING_TEACHER_STRATEGY_DECISION` | Replacing the current startup-preload default | Current M4a evidence reporting; keeping startup preload until teacher decision | Accepted M4a-4BAAAA benchmark package plus teacher loading-strategy ruling |
| `MT-PEND-07` | Biological expert and teacher | Confirm later M4b trait allowlist directions and thresholds. | `FUTURE_NOT_AUTHORIZED` | Any upgrade from soft uncertainty to hard filtering | M4a; recording all current traits as soft/unknown where applicable | Versioned expert allowlist and explicit teacher authorization for M4b |
| `MT-PEND-08` | Teacher | Decide how to close the required "other ADRMATS models coexisting" VRAM item after pinned source and Chenyu preflight both establish zero additional local ADRMATS GPU models. | `EVIDENCE_CONFIRMED_WAITING_TEACHER_INTERPRETATION` | Claiming the additional-local-model coexistence subrequirement is complete | Portable/runtime correction; 100-warm; concurrency-2/4; EnzymeCAGE-in-ADRMATS process memory measurement | Teacher either accepts proven-zero as an unavailable/not-applicable boundary or names an exact executable additional local model set and load contract |
| `MT-PEND-09` | Teacher | Confirm how strain-level UniProt host evidence may consume species-level or sibling-strain metaTraits records, and whether another strain may become a candidate only after independent enzyme-presence proof. | `STUDENT_IDENTIFIED_CONCEPTUAL_SCOPE_QUESTION_NOT_RUNTIME_FAILURE` | Assigning species/sibling-strain traits to a specific enzyme host; any later strain expansion or M4b trait decision | Current M4a exact reviewed-host mapping, aggregation, GPU benchmark and preservation of all returned tax IDs | Explicit exact-taxon/fallback/strain-expansion policy and whether species-level evidence may affect filtering/ranking |

### 2.1 Current M4a execution-blocker classification

`Execution blocker` here means that a deliverable explicitly required in the
teacher's current M4a document cannot be truthfully completed without a new
teacher ruling. It does not mean an artifact that is already complete as a
draft but must later be submitted for review.

```text
CONFIRMED CURRENT TEACHER-RULING EXECUTION BLOCKERS:
  MT-PEND-01: complete A/B/C OrganismAggregator comparison formulas, source
              fields and deterministic tie-breaks, including whether MT-D3
              "UID ascending" means numeric NCBI taxon ID ascending as currently
              implemented or another exact UID field.
  MT-PEND-08: only the additional-local-model coexistence subrequirement. The
              pinned ADRMATS source and Chenyu M4a-4P preflight establish zero
              additional local ADRMATS GPU models; zero must not be called PASS
              without a teacher interpretation or a teacher-named model set.

NOT CURRENT M4A EXECUTION BLOCKERS:
  MT-PEND-02: the required snapshot DRAFT is already complete; teacher review
              blocks calling it approved and later production/M4b promotion,
              not completion of the current draft deliverable.
  MT-PEND-03: the required maintainer email DRAFT is already complete; teacher
              review/send blocks claiming contact, not completion of the draft.
  MT-PEND-06: the final loading-strategy ruling is now ready to ask because the
              M4a-4BAAAA benchmark evidence is locally accepted; it blocks only
              replacing the current startup-preload default.
  MT-PEND-07: M4b is a future separately authorized stage, not unfinished M4a.
  MT-PEND-09: current M4a already preserves the UniProt reviewed NCBI taxon ID.
              This student-identified issue is not a runtime failure and does
              not invalidate host mapping; it must be resolved before a later
              trait consumer assigns species/sibling-strain evidence or expands
              candidates across strains.
```

M4a-4P has now resolved the prior conditional issue. The pinned source is
complete, its configured LLMs are remote DashScope services, and no additional
local ADRMATS GPU model/checkpoint/load entrypoint exists. `MT-PEND-08` is
therefore a confirmed teacher-interpretation blocker for the coexistence
subrequirement, but it does not block collecting the other authorized benchmark
measurements after transport and runtime repair.

## 3. Already Completed Preparation

```text
MT-D5 accepted by teacher
MT-D1 through MT-D8 v1 defaults recorded
M4a-0 preimplementation audit complete
M4a R01-R24 requirement/evidence matrix complete
SNAPSHOT_CONTRACT_DRAFT.md complete and locally audited
METATRAITS_API_INQUIRY_EMAIL_DRAFT.md complete, locally audited and unsent
current four local download byte sizes and SHA256 values reverified
ADRMATS private GitHub source pinned to main commit ca5eabe1d521bbcb8aae67c0b2fd24f9f16667a5 and locally audited
ten-UID UniProt/KEGG M4a-2C fixture package frozen, validated and locally audited
M4a-2D ADRMATS module/import/schema/test placement contract frozen and locally audited
M4a-3 implementation and offline tests completed on Chenyu: 15/15 passed
M4a-3A portable validator and deterministic transport correction independently accepted locally
accepted M4a-3A tar SHA256: 7f213605f1aed7065bdda256a6b33955e64f8cabb547a597e5ac8e74be766f87
34-file microbe_crew source frozen; 233 pre-existing ADRMATS files unchanged
M4a-4 GPU integration/coexistence read-only preflight contract and executor prompt prepared
M4a-4P Chenyu preflight returned: fixed inputs/GPU/wrapper/model inventory credible; no additional local ADRMATS GPU model established
M4a-4PA directory/tar/identity and portable captured validator independently accepted locally; copied-directory mode loss is nonblocking and canonical tar modes are correct
M4a-4PB context-free prompt prepared to reconstruct a persistent isolated Pydantic 2.12.5 layer from the five frozen D4A1 wheels under the accepted D4B1A lock/hash contract
M4a-4PB returned runtime evidence independently found credible, but portable validator rejected for reproducible CSV/internal-cross-consistency bypass; formal benchmark remains closed
M4a-4PBA CPU-only validator/transport correction prompt prepared without overlay rebuild or GPU work
M4a-4PBA returned with exact inherited bytes and deterministic transport; original CSV/internal-runtime gates were materially corrected, but exact directory and provenance-boundary bypasses remain; inherited PB positive raw summaries were never present and must not be fabricated
M4a-4PBB bounded exact-structure/boundary-consistency correction prompt prepared; formal benchmark remains closed
M4a-4PBB directory/tar/identity independently accepted locally: exact structure, 57/57 inherited bytes, exact boundaries and portable captured validation pass
formal M4a-4 startup-preload benchmark prompt prepared; zero additional local ADRMATS GPU models remains an open teacher interpretation rather than coexistence PASS
formal M4a-4 return independently audited: runtime blocker is credible, but no benchmark measurement completed; fixed `PYTHONPATH` omitted the accepted EnzymeCAGE `CODE_ROOT`
formal M4a-4 canonical tar is byte-sound; bundled validator is rejected because it self-flags its N14 literal and has no BLOCKED-status schema
formal M4a-4 three stable GPU samples are historical but not strictly immediate (about 413 seconds before benchmark sampler start); a fresh immediate gate is required
M4a-4A canonical transport independently passed; corrected CODE_ROOT, accepted 17-file source ledger and strict 0.187-second GPU launch gate are credible
M4a-4A reached the final 5/100/100/100 control-flow phase, but a PyG generated helper was over-broadly rejected before 305 per-call rows were persisted; formal latency/success evidence remains unavailable
M4a-4A retained three valid first responses and 6166 raw memory rows; these are partial scientific evidence only and do not close the benchmark
M4a-4A validator fixed the self-secret false positive but remained READY-only; actual BLOCKED status packaged validation fails
M4a-4B correction prompt prepared: durable per-call persistence precedes provenance checks, PyG generated helpers require narrow class-linked proof, and the packaged validator dispatches the actual status
M4a-4B returned complete 305-call scientific evidence, independently recomputable latency/degradation and credible two-helper PyG provenance; no GPU rerun is required
M4a-4B package is not formally accepted because five cross-consistent validator bypasses reproduce and multiple claimed blocked statuses are semantically invalid or unreachable
M4a-4BA CPU-only validator/evidence correction prompt prepared; prior scientific evidence must remain byte-identical
M4a-4BA returned deterministic transport, exact scientific inheritance, a complete fixed-input ledger and materially corrected READY checks; all five historical bypasses are now rejected
M4a-4BA is not locally accepted because its default fixture runner writes package bytecode and fails, multiple blocked-status fixtures violate required semantics, test/final-gate logs remain forgeable, and the inherited new-manifest identity is stale
M4a-4BAA CPU-only portable-test/status-semantics/final-provenance correction prompt prepared; no GPU rerun is required
M4a-4BAA directory pre-audit passed manifest, exact inheritance, READY validation, two 6/6 positive runs and the executable 53/53 negative suite without source-tree changes
M4a-4BAA is not locally accepted because malformed INCOMPLETE/provenance call rows, a nonsensical GPU sample, invalid packaging-completeness evidence and contradictory duplicate-suite logs independently bypass validation; tar and identity were not transferred after this content failure
M4a-4BAAA bounded CPU-only complete-status/test-evidence semantic correction prompt prepared; no scientific byte or GPU benchmark rerun is authorized
M4a-4BAAA directory pre-audit passed manifest but is not locally accepted because five adversarial bypasses still return exit 0: INCOMPLETE blocker/row mismatch, BLOCKED_PROVENANCE inside-root rejected module semantics, contradictory BLOCKED_GPU blocker message, extra contradictory transcript lines and malformed READY UTC timestamps
M4a-4BAAAA CPU-only adversarial status/transcript semantic correction prompt prepared; no scientific byte or GPU benchmark rerun is authorized
M4a-4BAAAA directory/tar/identity independently accepted locally: manifest 79/79 OK, packaged validator PASS, positive fixtures 6/6 PASS, negative suite 73/73 PASS, five adversarial rechecks rejected, 305 call rows and 6917 memory rows recompute PASS
M4b/M4c and prohibited-scope boundaries recorded
```

## 4. Work Queue That Does Not Need New Teacher Authority

| Order | Stage | Work | Prerequisite | Execution site | Current state |
|---:|---|---|---|---|---|
| 1 | M4a-2 | Historical read-only ADRMATS source identity preflight | Chenyu access | Chenyu CPU only | `BLOCKED_SOURCE_NOT_FOUND_HISTORICAL_NONBLOCKING` |
| 2 | M4a-2A | Historical independent local audit of blocked M4a-2 return | Returned directory, tar and identity | Local | `BLOCKED_RETURN_NOT_PROMOTED_NONBLOCKING` |
| 3 | M4a-2B | Pin and audit the supplied private ADRMATS GitHub source | Authenticated source access | Local | `SOURCE_IDENTITY_PINNED_LOCAL_AUDIT` |
| 4 | M4a-2C | Freeze ten-UID UniProt/KEGG host-mapping fixtures from accepted D5 evidence | Pinned source patterns and accepted D5 evidence | Local | `FIXTURE_FROZEN_LOCAL_AUDIT_PASS` |
| 5 | M4a-2D | Pin ADRMATS module/import/schema/test placement contract | Source and fixtures pinned | Local | `PLACEMENT_CONTRACT_FROZEN_LOCAL_AUDIT_PASS` |
| 6 | M4a-3 | Implement `Enzyme2OrganismTool` against pinned ADRMATS contract | Frozen fixtures and accepted module/schema placement | Chenyu or authoritative code root | `LOCALLY_ACCEPTED_M4A3A` |
| 7 | M4a-3 | Implement deterministic v1 default `OrganismAggregator` order | Candidate schema pinned | Chenyu or authoritative code root | `LOCALLY_ACCEPTED_M4A3A` |
| 8 | M4a-3 | Focused tests for ten P0 UIDs, KEGG `0/1/N`, no confidence and sparse `Debaryomyces hansenii` | Implementation complete | Chenyu | `15_PASS_LOCALLY_ACCEPTED_M4A3A` |
| 9 | M4a-4P/M4a-4PA | Read-only preflight and portable-validator correction | Accepted M4a-3A and D4B1A identities | Chenyu plus local audit | `THREE_PART_RETURN_AND_PORTABLE_VALIDATOR_LOCALLY_ACCEPTED; DIRECTORY_MODE_LOSS_NONBLOCKING` |
| 10 | M4a-4PB | Reconstruct and validate a persistent isolated Pydantic 2.12.5 runtime layer from frozen wheels without modifying shared Python or touching GPU | Locally accepted M4a-4PA plus exact D4A1 wheel and D4B1A lock/hash identities | Chenyu CPU only | `RUNTIME_EVIDENCE_CREDIBLE; VALIDATOR_TRANSPORT_NOT_ACCEPTED` |
| 11 | M4a-4PB-A | Independently audit the M4a-4PB directory, deterministic tar and external identity | Complete M4a-4PB three-part return | Local | `AUDIT_COMPLETE_HISTORICAL_SUPERSEDED_BY_M4A4PBA` |
| 12 | M4a-4PBA | Correct portable validator internal cross-consistency while preserving prior runtime evidence and existing overlay | Credible M4a-4PB return plus exact prior/external identities | Chenyu CPU only | `RETURNED_TRANSPORT_SOUND_ORIGINAL_DEFECT_CORRECTED_BUT_NOT_LOCALLY_ACCEPTED` |
| 13 | M4a-4PBA-A | Independently audit the correction directory, deterministic tar and external identity | Complete M4a-4PBA three-part return | Local | `AUDIT_COMPLETE_HISTORICAL_SUPERSEDED_BY_M4A4PBB` |
| 14 | M4a-4PBB | Enforce exact directory sets, exact scope/boundary provenance and complete inherited raw-log cross-checks | Sound M4a-4PBA transport plus reproduced local bypasses | Chenyu CPU only | `LOCALLY_ACCEPTED` |
| 15 | M4a-4PBB-A | Independently audit the PBB directory, deterministic tar and external identity | Complete M4a-4PBB three-part return | Local | `AUDIT_COMPLETE_ACCEPTED` |
| 16 | M4a-4 | Recheck live GPU availability, then run 100-warm, concurrency and bounded VRAM benchmark under startup preload | Accepted M4a-4PBB local audit and unchanged fixed scientific inputs | Chenyu GPU | `HISTORICAL_BLOCKER_ACCEPTED_SUPERSEDED_BY_M4A4BAAAA_FINAL` |
| 17 | M4a-4A | Correct fixed runtime source path, source-identity closure, immediate GPU gate and status-aware portable validator; rerun on fresh paths | Credible M4a-4 blocked evidence plus accepted D4B1A source-root contract | Chenyu GPU | `BLOCKED_AFTER_FINAL_CONTROL_FLOW; PARTIAL_EVIDENCE_ONLY` |
| 18 | M4a-4A-A | Independent local audit of corrected run | Complete M4a-4A directory, deterministic tar and external identity | Local | `AUDIT_COMPLETE_PARTIAL_EVIDENCE_SUPERSEDED_BY_M4A4B` |
| 19 | M4a-4B | Correct PyG generated-helper provenance, durable phase-row persistence, full stream capture and actual status-aware validation; rerun on fresh paths | M4a-4A blocked audit and unchanged fixed inputs | Chenyu GPU | `RETURNED_SCIENCE_PASS_PACKAGE_VALIDATOR_NOT_ACCEPTED` |
| 20 | M4a-4B-A | Independent local audit and smoke/benchmark report integration | Complete M4a-4B three-part return | Local | `AUDIT_COMPLETE_SCIENCE_PASS_SUPERSEDED_BY_M4A4BA_VALIDATOR_REPAIR` |
| 21 | M4a-4BA | CPU-only portable-validator, fixed-input-ledger and evidence cross-consistency correction without GPU rerun | M4a-4B canonical evidence and blocked local audit | Chenyu CPU only | `RETURNED_SCIENCE_AND_READY_CHECKS_PASS_PACKAGE_TEST_SEMANTICS_FAIL` |
| 22 | M4a-4BA-A | Independent local audit of corrected validator/evidence package | Complete M4a-4BA three-part return | Local | `AUDIT_COMPLETE_HISTORICAL_SUPERSEDED_BY_M4A4BAA` |
| 23 | M4a-4BAA | Correct portable test execution, blocked-status semantics, executable negative suite and final provenance without GPU rerun | Canonical M4a-4BA return and blocked local audit | Chenyu CPU only | `RETURNED_AND_PREAUDITED_SUPERSEDED_BY_M4A4BAAA` |
| 24 | M4a-4BAA-A | Independently audit final CPU correction directory, tar and external identity | Complete M4a-4BAA three-part return | Local | `DIRECTORY_PREAUDIT_COMPLETE_STATUS_ROW_SEMANTICS_FAIL_TRANSPORT_NOT_NEEDED` |
| 25 | M4a-4BAAA | Enforce strict partial-call, immediate-GPU, packaging-completeness and duplicate-test-evidence semantics without GPU rerun | M4a-4BAA directory pre-audit and unchanged prior canonical inputs | Chenyu CPU only | `RETURNED_AND_PREAUDITED_SUPERSEDED_BY_M4A4BAAAA` |
| 26 | M4a-4BAAA-A | Independently audit the bounded final correction directory, tar and external identity | Complete M4a-4BAAA return | Local | `DIRECTORY_PREAUDIT_COMPLETE_ADVERSARIAL_SEMANTIC_FAIL_TRANSPORT_NOT_NEEDED` |
| 27 | M4a-4BAAAA | Correct remaining adversarial status/transcript semantics without GPU rerun | M4a-4BAAA blocked local audit and unchanged inherited scientific evidence | Chenyu CPU only | `RETURNED_THREE_PART_LOCALLY_ACCEPTED` |
| 28 | M4a-4BAAAA-A | Independently audit the adversarial semantic correction directory, tar and external identity | Complete M4a-4BAAAA three-part return | Local | `LOCALLY_ACCEPTED_FINAL_TRANSPORT_AND_REQUIREMENT_CROSSCHECK` |

The complete A/B/C comparison is deliberately absent from the do-now queue
until `MT-PEND-01` closes. The default v1 count-based ordering has already been
implemented and locally accepted. M4a-4P has proven zero additional local
ADRMATS GPU models and preserved that environmental fact without converting it
to PASS. M4a-4PA remains locally accepted. M4a-4PB runtime evidence is credible.
M4a-4PBA corrected the original negative-CSV and major internal-consistency
defects, and M4a-4PBB then closed the remaining exact-directory and
scope/authorization provenance bypasses. Its local audit accepted the canonical
transport, 57/57 inherited bytes, exact boundary contracts and portable
captured validation. The inherited PB historical raw stdout still contains
negatives only and remains explicitly marked unavailable/not fabricated.
M4a-4A fixed the accepted source root and immediate GPU gate but lost its
in-memory call rows when an over-broad generated-module check failed. M4a-4B
then completed and durably preserved all 305 calls, formal latency/degradation,
6917 memory rows and credible provenance for both PyG-generated helpers. Its
scientific evidence is now immutable inheritable evidence and requires no GPU
rerun. M4a-4BA preserved those scientific bytes, supplied the full fixed-input
ledger and closed all five historical READY-validator bypasses, but its package
still failed local acceptance. M4a-4BAA and M4a-4BAAA were bounded CPU-only
semantic corrections that preserved the inherited scientific bytes, but local
adversarial pre-audits still found validation bypasses. M4a-4BAAAA then closed
the remaining five status/transcript bypasses without a GPU rerun. Its
directory/tar/identity are now locally accepted: manifest 79/79 OK, packaged
validator PASS, positive fixtures 6/6 PASS, negative suite 73/73 PASS, five
independent adversarial rechecks rejected, and the 305 call rows plus 6917
memory rows recompute.

## 5. Consolidated Reply Gate

Prepare the final teacher-facing MetaTraits progress response only after the
available teacher and maintainer replies are saved as authority/evidence. The
response must separate:

```text
teacher decisions received
maintainer facts received
work completed before replies
work revised because of replies
remaining external blockers
M4a requirement-by-requirement closure
explicit M4b/M4c authorization state
```

No pending item may be silently marked complete because related engineering
work passed.

## 6. Consolidated Teacher Decision Packet Register

This is the single teacher-facing question register. The categories must not be
merged because they have different evidence prerequisites.

### 6.1 Ready for teacher reply or review now

| ID | Exact request | Already fixed and not being re-asked | Required reply |
|---|---|---|---|
| `MT-TQ-01` | Define stable A, B and C `OrganismAggregator` comparison formulas, source fields and tie-breaks. The original framework and latest reply assign incompatible meanings to B/C, while A depends on the now-prohibited confidence float. Also disambiguate whether MT-D3 "UID ascending" means numeric NCBI taxon ID ascending or another exact UID field. | V1 default remains supporting-enzyme count descending; the accepted implementation currently uses numeric NCBI taxon ID ascending as the deterministic tie-break because NCBI taxon ID is the teacher-confirmed production key. V1 does not output confidence. | Explicit formula and deterministic tie-break for each A/B/C column, including the exact UID field for MT-D3 B, or explicit permission to omit non-executable columns. |
| `MT-TQ-02` | Review and approve or amend `SNAPSHOT_CONTRACT_DRAFT.md`. | Official versioned snapshot remains production primary; website endpoint remains experimental fallback only. | Approval/amendment of version, update frequency, license display, storage, hash validation and fallback-switch conditions. |
| `MT-TQ-03` | Review `METATRAITS_API_INQUIRY_EMAIL_DRAFT.md` before the teacher sends it. | The message is unsent and no maintainer contact is claimed. | Recipient, signature identity, whether to retain the EnzymeCAGE project name, wording approval and sent-date evidence. |
| `MT-TQ-04` | Select the final checkpoint loading strategy A/B/C. | M4a-4BAAAA now supplies accepted benchmark evidence: 100 sequential warm calls, concurrency-2/4 measurements, and EnzymeCAGE-in-ADRMATS process-memory evidence under startup preload. | Final loading strategy, or instruction to keep startup preload as the production default. |
| `MT-TQ-06` | Decide how the M4a coexistence requirement is to be closed when the pinned ADRMATS commit and Chenyu deployment establish no additional local ADRMATS GPU model. | Accepted portable M4a-4P/PBB evidence shows six remote DashScope names, zero additional local GPU model/checkpoint/load entrypoint, and no pre-existing GPU process. M4a-4BAAAA supplies EnzymeCAGE-in-ADRMATS process-memory evidence only. | Accept proven-zero as an unavailable/not-applicable boundary, or name an exact executable additional local model set and load contract. |
| `MT-TQ-07` | Confirm the strain/species alignment policy between exact UniProt reviewed hosts and metaTraits. Q8EFP8 maps to *Shewanella oneidensis* MR-1 taxon `211586`, while the species-name metaTraits observation query returned both taxon `211586` and species taxon `70863`. | NCBI taxon ID remains the production key; species lookup does not promise strain preservation; every returned tax ID is retained; no sibling strain is currently substituted or selected. This question was identified by the student during design review, not caused by a failed run. | Decide whether only exact-tax-ID records may directly annotate a host; how species/sibling-strain records are labelled when exact records are absent; whether they may affect ranking/filtering; and whether another strain may become a candidate only after independent evidence that it carries the required enzyme. |

### 6.2 Future-stage decisions, not part of current M4a closure

| ID | Future decision | Prerequisite | Current boundary |
|---|---|---|---|
| `MT-TQ-05` | Approve the expert trait hard-constraint allowlist, directions and thresholds, then explicitly authorize M4b. | Teacher-approved snapshot contract, expert list and separate M4b authorization. | M4b/M4c remain unauthorized; current traits are soft/unknown only. |

### 6.3 External maintainer fact request

| ID | Owner | Exact fact request | Teacher role |
|---|---|---|---|
| `MT-EQ-01` | metaTraits maintainers | Confirm whether `/api/v1` is retired, any replacement endpoint, and official versioned bulk snapshot/version/checksum/license metadata. | Teacher reviews and sends the approved inquiry; the maintainer response is preserved verbatim as external evidence. |

The final consolidated teacher message must attach or link the decision request,
snapshot contract draft, approved/sent email evidence when available, M4a smoke
report, benchmark evidence and requirement-to-evidence closure. It must clearly
separate current questions from later evidence-triggered decisions.
