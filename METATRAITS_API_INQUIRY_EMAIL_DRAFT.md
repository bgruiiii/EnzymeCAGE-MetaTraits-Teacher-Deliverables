# metaTraits API And Bulk Download Inquiry Email Draft

Status: `UNSENT_GENERIC_INQUIRY_DRAFT_PENDING_RECIPIENT_AND_SIGNATURE_REVIEW`

Date: 2026-07-18

Last revised: 2026-07-23 under teacher decision MT-TQ-03.

Final M4a delivery target after the authoritative ADRMATS code root is pinned:

```text
microbe_crew/METATRAITS_API_INQUIRY_EMAIL_DRAFT.md
```

The recipient address must be verified by the teacher against the official
metaTraits contact page before sending.

---

To: metaTraits maintainers

Subject: Clarification on the metaTraits API and official versioned bulk downloads

Dear metaTraits team,

We are evaluating metaTraits for an academic workflow that links reviewed
UniProt enzyme records to organism-level microbial trait evidence. We intend to
use only publicly released data under the applicable attribution and
share-alike terms, and we would like to follow the access route recommended by
the maintainers rather than rely on undocumented website behavior.

During a small, serial interface check on 16 July 2026, 16 bounded requests to
the documented `/api/v1` route family returned HTTP 404. In the same check,
taxon summary downloads on the public website returned JSON for five test
organisms. We understand that this limited observation does not establish that
the API has been permanently retired, nor does it establish a production
service contract.

Could you please clarify the following three points?

1. Has the documented `/api/v1` API been retired, moved, or temporarily taken
   offline?
2. If it has been replaced, is there a current official endpoint and
   documentation for programmatic access, including authentication, versioning
   and rate-limit guidance?
3. Is there an official versioned bulk download or snapshot that you recommend
   for reproducible local use? In particular, are
   `ncbi_species_summary_all.tsv.gz`,
   `ncbi_species_summary_no_predictions.tsv.gz`, `GTDB2NCBI.tsv.gz` and
   `NCBI2GTDB.tsv.gz` the recommended distribution files, and where can we find
   their release/version identifier, release date, checksums and file-specific
   license or attribution metadata?

We do not plan to bulk-scrape observation pages. Until an official route is
confirmed, we will treat website endpoints only as a bounded experimental
fallback and will keep a versioned, hash-validated local snapshot as the
intended primary data path.

Thank you for your guidance and for making metaTraits publicly available.

Best regards,

<Teacher name and affiliation>

On behalf of an academic bioinformatics enzyme-to-microorganism mapping study

---

## Teacher Review Checklist

- verify the official recipient address;
- replace the name and affiliation placeholder;
- confirm the generic academic bioinformatics / enzyme-to-microorganism wording;
- approve the factual date and `16 HTTP 404` wording;
- approve the four filenames in question 3;
- send only after teacher approval.
