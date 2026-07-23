# EnzymeCAGE MetaTraits MT-D5A2 Accepted Return Local Audit

Date: 2026-07-16

Accepted return forms:

```text
03_HPC_Returned_Result_Summaries/
metatraits_mt_d5a2_https_handler_and_required_evidence_final_correction_20260716/
metatraits_mt_d5a2_https_handler_and_required_evidence_final_correction_20260716.tar
metatraits_mt_d5a2_https_handler_and_required_evidence_final_correction_20260716.tar.identity.txt
```

Directory content preaudit:

```text
04_Local_Review_Audits/
ENZYMECAGE_METATRAITS_MT_D5A2_DIRECTORY_PREAUDIT_2026-07-16.md
```

## Final Decision

The D5A2 directory, deterministic tar and external identity pass independent
local audit. R16 is complete. The bounded teacher MT-D5 pre-research evidence
is accepted and may now be used to draft teacher-facing feedback.

```text
MT_D5A2_DIRECTORY_CONTENT_PASS
MT_D5A2_TAR_SAFETY_AND_IDENTITY_PASS
MT_D5A2_DETERMINISTIC_BYTE_REBUILD_PASS
MT_D5A2_PORTABLE_VALIDATOR_WITH_TRANSPORT_EXIT_0
MT_D5_R01_R16_EVIDENCE_CLOSED
MT_D5_ACCEPTED_FOR_TEACHER_FEEDBACK
```

The accepted status token is:

```text
MT_D5A2_READY_FOR_LOCAL_AUDIT_DOCUMENTED_API_UNAVAILABLE
```

The token preserves the evidence boundary: the documented `/api/v1` routes
were unavailable at probe time, while the bounded website summary and
observation surfaces were working. It does not claim production readiness.

## External Identity

The local tar and directory independently reproduce every binding identity
field:

```text
tar bytes
3952640

tar SHA256
b5e97d92fcbcd2f09a5709af9abc886fc654fa83107ded21868138a0fc2ffe2f

MANIFEST.sha256 bytes
10600

MANIFEST.sha256 SHA256
d6d2a44d20b2631faa1cbe33c6d7ef6d5c9cfe103a5cc77b7afd755b271460c2

regular file count
95

top-level member
metatraits_mt_d5a2_https_handler_and_required_evidence_final_correction_20260716
```

`final_token`, tar bytes/hash, manifest bytes/hash, regular-file count and
top-level member all exactly match the external identity file. No identity
field mismatch was found.

## Tar Member Safety

Independent direct tar-header inspection gives:

```text
total members                         118
directories                            23
regular files                          95
unique top-level directories            1
duplicate members                        0
absolute or parent-traversal paths       0
links or special members                 0
body mismatches                           0
tar-only files                            0
directory-only files                      0
```

All member names are sorted. Every member has `uid=0`, `gid=0` and `mtime=0`.
Directories and Python files under a `scripts` directory have mode `0755`;
ordinary files have mode `0644`. Every file body is byte-identical to the
accepted local directory.

Long paths use deterministic PAX `path` records. No PAX timestamp, ownership or
other nondeterministic header is present. This is a standard safe use of the
PAX format and is required for member names longer than the legacy header
limit.

## Deterministic Rebuild

An independent temporary tar was rebuilt from the accepted directory using the
binding sorted-member, PAX-format, zero-mtime, zero-owner and normalized-mode
rules. It was not copied from the return tar.

```text
returned tar SHA256
b5e97d92fcbcd2f09a5709af9abc886fc654fa83107ded21868138a0fc2ffe2f

independent rebuilt tar SHA256
b5e97d92fcbcd2f09a5709af9abc886fc654fa83107ded21868138a0fc2ffe2f

cmp result
byte-identical
```

This proves that the return tar is reproducible from the accepted directory,
not merely self-consistent with its identity text.

## Final Validator Gate

The packaged validator was run locally with all five explicit roots/forms:

```text
--package-root   accepted D5A2 directory
--inherited-d5   actual accepted D5 directory
--inherited-d5a1 actual audited D5A1 directory
--return-tar     returned D5A2 tar
--tar-identity   returned external identity
```

Result:

```text
MT_D5A2_VALIDATION_OK
exit code 0
```

This transport-aware run rechecks inherited identities, HTTPS-handler
preflight, the 16-row request ledger, five summaries, two bounded observations,
three stability repeats, rate semantics, `tax_id`, mapping separation, trait
calculations, R01--R16 meanings/statuses, scope, manifest, tar and identity.

The five baseline-first mutation tests remain 5/5 rejected with their expected
diagnostics.

## Accepted Scientific Findings

The final accepted bounded evidence is:

```text
fixed P0 probe UIDs                         10
UniProt accession exact/missing           10/0
KEGG single/missing/multiple               7/1/2
documented API probes HTTP 404            16/16
current summary HTTP-200 strict JSON        5/5
bounded observation pages                   2/2
successful stability repeats                3/3
current summary records                      597
No robust majority                      43/597
No robust majority percentage         7.202680%
D5A2 HTTP responses                          15
D5A2 transient network exceptions             1
D5A2 local programming exceptions             0
D5A2 observed HTTP 429                        0
rate-limit threshold                    UNKNOWN
```

The three successful repeat bodies are byte-identical. The one transient TLS
handshake timeout was recorded and followed by one allowed successful retry.
The two current Shewanella observation bodies contain 69 and 9 rows and expose
real `tax_id` values `70863` and `211586`.

The scientific interpretation remains bounded:

- trait-record presence is not organism suitability;
- missing coverage is unknown, not unsuitable;
- species queries do not prove strain preservation;
- zero observed 429 does not prove an unlimited interface;
- the five-sample probe does not establish production-wide coverage;
- documented API HTTP 404 does not make saved website JSON evidence invalid;
- no production implementation, training or inference was authorized.

## Residual Nonblocking Boundary

The research client implements a 10-second connection timeout and a 30-second
per-socket-read timeout. It does not prove a 30-second end-to-end wall-clock
deadline; four large taxon-page requests exceeded 30 seconds. This is not a
blocker for the completed bounded teacher D5 evidence, but must remain explicit
if a production client is designed later.

## Closure

```text
MT_D5_ORIGINAL_AND_D5A1_BLOCKED_PACKAGES_PRESERVED
MT_D5A2_ALL_THREE_RETURN_FORMS_LOCALLY_VERIFIED
MT_D5_R01_R16_CLOSED
MT_D5_BOUNDED_PRERESEARCH_ACCEPTED
MT_D5_TEACHER_FEEDBACK_AUTHORIZED
GPU_MODEL_INFERENCE_TRAINING_PORTRAITS_BULK_AND_IMPLEMENTATION_NOT_RUN
```
