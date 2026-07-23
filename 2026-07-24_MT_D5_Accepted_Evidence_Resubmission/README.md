# MT-D5 Accepted Evidence Resubmission

Date of resubmission: 2026-07-24

Original work and final D5A2 evidence date: 2026-07-16

Status:

```text
BYTE_IDENTICAL_RESUBMISSION_OF_ALREADY_ACCEPTED_MT_D5_EVIDENCE
NO_NEW_PROBE
NO_NEW_NETWORK_REQUEST
NO_NEW_SCIENTIFIC_CLAIM
```

## 1. Why This Is Being Resubmitted

The 2026-07-24 teacher supplement lists the D5 pre-research report and five
raw sample JSON bodies as the highest-priority prerequisite for the next
round.

This work already existed:

1. the final D5A2 evidence package and report were completed on 2026-07-16;
2. the package passed the independent local audit copied under `audits/`;
3. the teacher accepted MT-D5 and marked it closed in
   `TEACHER_REPLY_MTD5_ACCEPTED_AND_MTD1_D8_DECISIONS_2026-07-18.md`
   (document body date 2026-07-16).

Accordingly, this delivery does not repeat the probe. It returns the accepted
bytes and makes their time, source and paths explicit.

## 2. Teacher Entry Points

Final report, placed at repository root for direct visibility:

```text
../metatraits_probe_report.md
SHA256 d263ec486d7def2516633d1ac1785175202ae0cc51eca42b3332e71ab949dfa5
```

Five original summary bodies:

| Enzyme UID / organism query | Resubmitted path | Records | SHA256 |
|---|---|---:|---|
| Q8EFP8 / *Shewanella oneidensis* | `raw/metatraits/samples/01_Q8EFP8/summary.json` | 146 | `0d0eeecd9b5cd6314d71e680119b5fd155fac2980f59581436501ed2f42d0604` |
| Q12WS1 / *Methanococcoides burtonii* | `raw/metatraits/samples/02_Q12WS1/summary.json` | 134 | `c3da972bb5214ef65f9631b48882dbd8eec96e2ebe0edb38901856ae96ec9e6b` |
| A0A0H3C8X0 / *Caulobacter vibrioides* | `raw/metatraits/samples/03_A0A0H3C8X0/summary.json` | 161 | `99ca0fb51622ba9d30eba9befabe6e90f96750eac96f1af31f8638807479a0e5` |
| Q6BQK1 / *Debaryomyces hansenii* | `raw/metatraits/samples/05_Q6BQK1/summary.json` | 9 | `28b4e749f70dafba8ad5ccf5c1948ce9ce8623709959687c4ebfd718ca1f8735` |
| P71875 / *Mycobacterium tuberculosis* | `raw/metatraits/samples/06_P71875/summary.json` | 147 | `414606627724f0ada3dcbc5be618291d94378fa60b0756e9dd62741fd4faa202` |

Complete accepted transport:

```text
accepted_package/
  metatraits_mt_d5a2_https_handler_and_required_evidence_final_correction_20260716.tar
  metatraits_mt_d5a2_https_handler_and_required_evidence_final_correction_20260716.tar.identity.txt

tar bytes  3952640
tar SHA256 b5e97d92fcbcd2f09a5709af9abc886fc654fa83107ded21868138a0fc2ffe2f
```

Audit and original acceptance authority:

```text
audits/
  ENZYMECAGE_METATRAITS_MT_D5A2_ACCEPTED_RETURN_LOCAL_AUDIT_2026-07-16.md

authority_reference/
  TEACHER_REPLY_MTD5_ACCEPTED_AND_MTD1_D8_DECISIONS_2026-07-18.md
```

The current resubmission audit is:

```text
audits/
  METATRAITS_MT_D5_ACCEPTED_EVIDENCE_RESUBMISSION_AUDIT_2026-07-24.md
```

All current delivery identities are listed in:

```text
DELIVERABLE_SHA256SUMS.txt
```

## 3. Original Local Source Paths

Final report:

```text
16_MetaTraits_Integration_Research_2026-07-15/
03_Reports/metatraits_probe_report.md
```

Final accepted D5A2 package:

```text
03_HPC_Returned_Result_Summaries/
metatraits_mt_d5a2_https_handler_and_required_evidence_final_correction_20260716/
```

Original deterministic tar and external identity:

```text
03_HPC_Returned_Result_Summaries/
metatraits_mt_d5a2_https_handler_and_required_evidence_final_correction_20260716.tar
metatraits_mt_d5a2_https_handler_and_required_evidence_final_correction_20260716.tar.identity.txt
```

Original independent audit:

```text
04_Local_Review_Audits/
ENZYMECAGE_METATRAITS_MT_D5A2_ACCEPTED_RETURN_LOCAL_AUDIT_2026-07-16.md
```

## 4. Previously Accepted Bounded Findings

```text
fixed P0 enzyme UIDs                      10
UniProt exact/missing                   10/0
KEGG single/missing/multiple            7/1/2
documented /api/v1 probes HTTP 404      16/16
current summary strict JSON               5/5
bounded observation pages                 2/2
successful stability repeats              3/3
summary records                            597
No robust majority                      43/597
No robust majority percentage        7.202680%
observed HTTP 429                            0
published rate-limit threshold        UNKNOWN
```

Wastewater-related coverage in the fixed five-sample probe was:
oxygen/atmosphere 5/5, temperature 5/5, pH 5/5, salinity 5/5,
biofilm 0/5, safety/pathogenicity 4/5 and wastewater metabolism 4/5.

These are bounded probe findings, not population estimates and not evidence
that an organism is suitable for wastewater treatment.

## 5. Boundary

This resubmission:

```text
does not rerun D5
does not contact an API or website
does not replace the accepted JSON bodies with current downloads
does not start M4b or M4c
does not implement MicrobeTraitTool or TraitFilterLayer
does not claim production API stability or a known rate limit
```

The purpose is solely to satisfy the 2026-07-24 prerequisite by making the
already accepted D5 evidence directly visible and byte-auditable in the
teacher-deliverables repository.
