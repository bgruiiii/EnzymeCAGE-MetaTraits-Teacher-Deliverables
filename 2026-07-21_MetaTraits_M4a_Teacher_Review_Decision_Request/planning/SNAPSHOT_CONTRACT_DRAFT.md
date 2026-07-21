# metaTraits Snapshot Contract Draft

Status: `DRAFT_FOR_TEACHER_REVIEW_NOT_PRODUCTION_APPROVED`

Date: 2026-07-18

Contract draft version: `metatraits-snapshot-contract-v0.1`

Final M4a delivery target after the authoritative ADRMATS code root is pinned:

```text
microbe_crew/SNAPSHOT_CONTRACT_DRAFT.md
```

Authority:

```text
00_Authority_Teacher_Plan/
TEACHER_REPLY_MTD5_ACCEPTED_AND_MTD1_D8_DECISIONS_2026-07-18.md
```

Accepted research evidence:

```text
16_MetaTraits_Integration_Research_2026-07-15/03_Reports/
metatraits_probe_report.md

03_HPC_Returned_Result_Summaries/
metatraits_mt_d5a2_https_handler_and_required_evidence_final_correction_20260716/
```

## 1. Purpose And Non-Claims

This draft defines how a future `MicrobeTraitTool` may consume an official,
versioned metaTraits snapshot as its production-primary data source. It also
defines a separately enabled experimental website fallback.

This document does not:

- assert that the current local downloads carry an official upstream version;
- authorize M4b or M4c implementation;
- authorize porTraits execution, bulk observation scraping or model training;
- promote `/taxon/download` or observation endpoints to a supported production
  API;
- infer a rate-limit threshold or service-level agreement from MT-D5.

## 2. Required Data-Path Hierarchy

The fixed hierarchy is:

```text
1. official versioned snapshot       production-primary path
2. maintainer clarification          parallel governance action
3. website endpoints                 experimental fallback only
```

Production mode defaults to `snapshot_only`. A website endpoint must never be
the sole production dependency. If no valid active snapshot exists, production
must fail closed with a structured `snapshot_unavailable` result rather than
silently switching to website collection.

An explicitly enabled `snapshot_with_experimental_fallback` mode may be used
only for bounded development or teacher-authorized evaluation under the
controls in section 8.

## 3. Snapshot Identity And Version Fields

Every candidate snapshot must have one immutable UTF-8 JSON manifest named:

```text
snapshot_manifest.json
```

Required top-level fields:

```json
{
  "contract_schema_version": "metatraits-snapshot-contract-v0.1",
  "snapshot_id": "metatraits-<upstream_version>-<retrieved_utc>-<content_sha12>",
  "upstream_dataset": "metaTraits",
  "upstream_version": "<official immutable release/version identifier>",
  "upstream_release_date": "<ISO-8601 date or null with explanation>",
  "retrieved_at_utc": "<ISO-8601 timestamp>",
  "source_page": "https://metatraits.embl.de/",
  "license_spdx": "CC-BY-SA-4.0",
  "license_url": "https://creativecommons.org/licenses/by-sa/4.0/",
  "taxonomy_primary_namespace": "NCBI_TAXONOMY",
  "files": [],
  "content_manifest_sha256": "<SHA256 of the canonical files array>",
  "created_by": "<deterministic collector version or manual package identity>",
  "approval_state": "CANDIDATE"
}
```

`upstream_version` is mandatory for production promotion. A retrieval date,
local filename, Git commit or locally invented label is not a substitute for
an official upstream release/version identifier.

If the maintainers confirm that no version field currently exists, the package
must remain:

```text
UNVERSIONED_UPSTREAM_QUARANTINED
```

until the teacher approves a separate immutable local-versioning policy. It
must not be called an official versioned snapshot.

Each `files` item must contain:

```json
{
  "role": "summary_all",
  "relative_path": "ncbi_species_summary_all.tsv.gz",
  "source_url": "<exact upstream URL>",
  "bytes": 0,
  "sha256": "<64 lowercase hexadecimal characters>",
  "media_type": "application/gzip",
  "compression": "gzip",
  "content_schema_id": "<pinned parser/schema identifier>"
}
```

`content_manifest_sha256` is computed over the canonical JSON serialization of
the complete `files` array after sorting by `relative_path`, using UTF-8,
sorted object keys and no insignificant whitespace. `content_sha12` is its
first 12 hexadecimal characters. The value does not hash
`snapshot_manifest.json` itself, so snapshot identity has no circular
dependency.

## 4. Required And Optional Snapshot Members

The minimum candidate inventory is:

| Role | Upstream artifact | Contract role |
|---|---|---|
| `summary_all` | `ncbi_species_summary_all.tsv.gz` | Required primary NCBI species summary, including AI-labelled records where supplied |
| `summary_no_predictions` | `ncbi_species_summary_no_predictions.tsv.gz` | Required companion summary for source-dimension checks and non-AI views |
| `gtdb_to_ncbi_crosswalk` | `GTDB2NCBI.tsv.gz` | Optional; usable only with an official version recorded in the manifest |
| `ncbi_to_gtdb_crosswalk` | `NCBI2GTDB.tsv.gz` | Optional; usable only with an official version recorded in the manifest |

`porTraits` source or model artifacts are not snapshot members and must not be
executed or packaged as production data by this contract.

The snapshot does not silently substitute species summaries for strain-level
observations. NCBI taxon ID is the primary production key. GTDB identifiers
must retain an explicit namespace and may be joined only through a versioned
official crosswalk. Multiple taxon IDs must not be collapsed without a
documented deterministic rule and provenance.

## 5. Current Local Candidate Evidence

The files downloaded on 2026-07-16 are useful candidate evidence but are not
yet a contract-compliant production snapshot because an official upstream
version was not established.

| File | Bytes | SHA256 | Current classification |
|---|---:|---|---|
| `ncbi_species_summary_all.tsv.gz` | 36,900,021 | `9118379f800c5f2d8f0d0787ffd3045cbe3bb84a592657b06723252c13799bcd` | `UNVERSIONED_UPSTREAM_CANDIDATE` |
| `ncbi_species_summary_no_predictions.tsv.gz` | 6,523,019 | `9e16ca57b94819fa591f32bc1cf194c82eae85b0dbbc454a3c1a449257a33873` | `UNVERSIONED_UPSTREAM_CANDIDATE` |
| `GTDB2NCBI.tsv.gz` | 2,937,650 | `892ecf0410091e3f2b4c88e5e129cae3cc43117613b1745aa73f95ccdcfbb9e3` | `UNVERSIONED_CROSSWALK_CANDIDATE` |
| `NCBI2GTDB.tsv.gz` | 2,895,086 | `761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd` | `UNVERSIONED_CROSSWALK_CANDIDATE` |

Their exact URLs, retrieval date, compressed and decompressed identities remain
in `DOWNLOAD_AND_EXTRACTION_MANIFEST_2026-07-16.tsv`. These identities prove
which bytes were downloaded; they do not create an upstream version.

## 6. Local Storage And Activation

Paths are relative to the future authoritative ADRMATS project root:

```text
data/metatraits/
├── incoming/<snapshot_id>/
├── quarantine/<snapshot_id>/
├── snapshots/<snapshot_id>/
│   ├── snapshot_manifest.json
│   ├── LICENSE.txt
│   ├── CITATION.txt
│   └── <manifest-listed data files>
└── active_snapshot.json
```

Rules:

1. Downloads enter `incoming/` and are never parsed as active production data.
2. Any missing version, hash mismatch, schema failure, license omission or
   taxonomy-namespace ambiguity moves the candidate to `quarantine/`.
3. A validated and teacher-approved candidate is copied atomically to
   `snapshots/<snapshot_id>/` as immutable files.
4. `active_snapshot.json` contains only the approved `snapshot_id`, manifest
   SHA256, activation timestamp and approver identity.
5. Activation updates the pointer atomically; it never edits an existing
   snapshot directory.
6. Rollback changes only `active_snapshot.json` to a previously validated
   snapshot.

## 7. Hash, Schema And License Validation

Promotion requires all checks below:

```text
V01 manifest parses as strict UTF-8 JSON
V02 required manifest fields are present and types are exact
V03 upstream_version is nonempty and independently traceable to the maintainer
V04 every listed file exists exactly once and no unlisted regular file exists
V05 file byte sizes and SHA256 values match the manifest
V06 gzip members pass integrity testing before decompression
V07 decompressed SHA256 values are recorded before parsing
V08 pinned headers/schema and required NCBI taxon-ID fields pass validation
V09 duplicate keys, malformed IDs and namespace collisions are reported
V10 license and citation files are present and match manifest metadata
V11 current and candidate row/count/schema deltas are reviewed
V12 a deterministic internal manifest and validator log both pass
```

The publication data-availability statement reports metaTraits under Creative
Commons Attribution-ShareAlike 4.0. The production snapshot must display
`CC BY-SA 4.0`, the license URL, metaTraits attribution, source URL, upstream
version and snapshot ID in:

- `snapshot_manifest.json`;
- `LICENSE.txt` and `CITATION.txt` at the snapshot root;
- any exported API/report metadata derived from the snapshot;
- any user-visible evidence detail that redistributes derived records.

The final maintainer response takes precedence if it clarifies file-specific
licensing or attribution requirements.

## 8. Update Frequency And Promotion

Because the upstream publication cadence is not established, this contract
does not invent one. The local policy is:

```text
discovery check:       every 30 days and upon maintainer release notice
automatic activation: never
promotion trigger:     new official upstream version plus complete validation
emergency review:      upstream correction, withdrawal or license change
retention:             current active plus all previously cited immutable versions
```

A repeated download with identical bytes but no new official version is logged
as a freshness check, not promoted as a new release. A changed body under the
same URL and version is quarantined as `UPSTREAM_MUTATION_UNDER_SAME_VERSION`
until resolved with the maintainers.

Every update report must include old/new snapshot IDs, file hashes, row counts,
schema changes, taxonomy-version changes, added/removed trait records and the
rollback target.

## 9. Experimental Website Fallback

### 9.1 Enablement and switch conditions

The fallback adapter is disabled by default. It may be called only when all of
the following are true:

1. mode is explicitly `snapshot_with_experimental_fallback`;
2. a valid active snapshot remains available as the safe return path;
3. the request is a bounded single-taxon lookup, not bulk export;
4. the snapshot has no matching record or an authorized freshness comparison
   is being performed;
5. the circuit breaker is closed;
6. the request and response will receive complete provenance.

Online data never mutates the active snapshot in place. A successful fallback
response is labelled `experimental_online`, remains outside the snapshot and
cannot be promoted without the full snapshot validation process.

The adapter returns to snapshot-only behavior when:

- three consecutive service failures open the circuit breaker;
- any response fails JSON/schema validation;
- HTTP 429 or a service-directed backoff is observed;
- the minimum request-spacing controller is unavailable;
- provenance persistence fails;
- the configured end-to-end wall-clock deadline is exceeded.

If the snapshot also lacks the requested record, the result is
`insufficient_evidence`; missing data is not converted to an unsuitable trait
or organism decision.

### 9.2 Cache, spacing and retry controls

```text
TTL cache:                  24 hours, keyed by adapter version + exact request
minimum request spacing:    >= 2 seconds globally for the metaTraits host
concurrency:                1 unless a later written contract changes it
consecutive-failure limit:  3, then circuit open and snapshot failover
published rate threshold:   UNKNOWN
bulk observation scraping:  prohibited
```

Retries must honor `Retry-After` when present, use bounded exponential backoff
with jitter, and never bypass the global spacing rule. A cached response must
retain the original retrieval identity and expose `cache_hit=true`; cache use
must not rewrite its retrieval timestamp.

### 9.3 Independent timeout parameters

The future client must configure and record three different controls:

```text
connect_timeout_s
socket_read_timeout_s
end_to_end_wall_clock_timeout_s
```

They must never be described as equivalent. MT-D5 used a 10-second connection
timeout and 30-second per-socket-read timeout, while four large taxon-page
requests exceeded 30 seconds of wall time. Final production values remain a
separate M4b implementation decision; this draft does not convert the D5 probe
settings into an SLA.

### 9.4 Required online provenance

Every attempt, including failures and cache hits, records:

```text
adapter name and version
request ID and parent workflow ID
endpoint role and exact URL
HTTP method and normalized query parameters
requested organism name and requested NCBI taxon ID, when available
request start/end UTC timestamps and elapsed wall time
connect/read/wall timeout settings
attempt number, cache key, cache hit and cache expiry
HTTP status and selected retry/rate headers
response bytes, body SHA256 and content type
parser/schema version and validation result
all returned tax_id values without strain-collapse claims
snapshot_id used for primary lookup or failover
failure class, circuit state and fallback decision
```

Sensitive headers or credentials, if a future official API requires them, are
redacted before persistence.

## 10. Replaceable Adapter Boundary

The future consumer depends on a stable local interface, not website routes:

```text
TraitSourceAdapter.lookup_by_ncbi_taxon_id(...)
TraitSourceAdapter.lookup_by_species_name(...)
TraitSourceAdapter.health_state()
TraitSourceAdapter.provenance()
```

Required implementations are conceptually separate:

```text
SnapshotTraitSourceAdapter             production primary
OfficialApiTraitSourceAdapter          reserved for maintainer-confirmed API
ExperimentalWebsiteTraitSourceAdapter  explicit fallback only
```

Website paths, cookies, pagination and HTML-derived details remain private to
the experimental adapter. Replacing that adapter must not change the trait
record schema consumed by later authorized stages.

## 11. Production Promotion Gate

The snapshot path remains `NO-GO` until all conditions are true:

```text
official upstream version identified
required files and exact source URLs identified
file and decompressed SHA256 identities verified
schema and taxonomy namespace validation passed
license and attribution display complete
update and rollback drill passed
active pointer activation tested atomically
teacher approval recorded
```

M4b remains unauthorized by this draft. Completing this document satisfies
only the M4a snapshot-contract deliverable; it does not itself authorize
`MicrobeTraitTool` or website fallback implementation.
