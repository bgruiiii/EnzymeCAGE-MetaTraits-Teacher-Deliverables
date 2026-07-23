# MetaTraits Task 6 Project-Name Disclosure Removal Local Audit

Date: 2026-07-23

Task scope: latest teacher reply MT-TQ-03 and Section 6.2.3 item 6 only.

## 1. Authority And Objective

Latest authority:

```text
00_Authority_Teacher_Plan/
TEACHER_REPLY_M3_P1_UNLOCK_CASE1_REBOUND_AND_METATRAITS_M4A_ADJUDICATION_2026-07-21.md
SHA256 57699b8a92ba6b555c96c0216c3961af0e80299d150b21979cb4fa7a19a18d57
```

Teacher requirement:

```text
Remove the "EnzymeCAGE" project name from outward-facing documentation, logs
and query context associated with Enzyme2OrganismTool and OrganismAggregator.
Use general bioinformatics / enzyme-to-microorganism mapping wording instead.
```

This task does not authorize a repository-wide rename. Historical authority,
accepted audits, frozen HPC returns, technical Python package names and exact
runtime provenance must remain truthful and unchanged.

## 2. Verdict

```text
TASK6_LOCAL_ACTIVE_DOCUMENT_CORRECTION_PASS
OUTWARD_EMAIL_PROJECT_NAME_REMOVAL_PASS
ACTIVE_DECISION_QUEUE_SUPERSESSION_PASS
RUNTIME_QUERY_CONTEXT_ALREADY_GENERIC_PASS
RUNTIME_LOG_DISCLOSURE_NOT_PRESENT_PASS
ACCEPTED_HPC_RETURN_UNCHANGED_PASS
NO_HPC_RERUN_OR_SOURCE_PATCH_REQUIRED
EMAIL_REMAINS_UNSENT_PASS
GITHUB_CORRECTION_COMMIT_PENDING
TASK7_NOT_STARTED_PASS
M4B_M4C_NOT_STARTED_PASS
```

The locally controlled active documents now implement the teacher's naming
decision. The prior public teacher-review packet remains unchanged at its
historical commit and still requires a new non-destructive correction commit
or dated follow-up delivery before Task 6 can be called remotely synchronized.

## 3. Bounded Change Set

Only two active planning documents were changed:

| File | Pre-change SHA256 | Post-change SHA256 |
|---|---|---|
| `METATRAITS_API_INQUIRY_EMAIL_DRAFT.md` | `a3a9c20964044a537c73fa0b81eda315a97e71fa4eee281a61dbc795ac2fc3c7` | `14d2b1e9b6cc63c24007251fc7bb96eccb0795dd3a833dad437024da3b385ee9` |
| `METATRAITS_PENDING_DECISIONS_AND_PREPARATION_QUEUE_2026-07-18.md` | `8702565117f767aa1365f0191438099d1e89f165d249fab19bb9572d4f935429` | `1306c3f832eddd7a6c817ef94fda2770d1660d4d219f84790e3c4c0ebf837034` |

The email draft now:

```text
states that it was revised under MT-TQ-03;
uses "academic bioinformatics enzyme-to-microorganism mapping study";
contains no case-insensitive "EnzymeCAGE" occurrence;
keeps recipient and teacher signature placeholders unresolved;
remains explicitly unsent.
```

The active decision queue now:

```text
records the 2026-07-21 document as the latest authority;
marks project-name removal as decided rather than re-asking it;
retains recipient, signature, final-wording and sent-date review as pending;
does not claim that the maintainer has been contacted.
```

## 4. Runtime Query And Log Review

Canonical accepted M4a-3A source inspected read-only:

```text
03_HPC_Returned_Result_Summaries/
metatraits_m4a3a_portable_validator_transport_final_correction_20260720/
source/microbe_crew/
```

Relevant source identities:

| File | SHA256 |
|---|---|
| `tools/enzyme2organism_tool.py` | `b632bc8ed97de11816b8b8ebaa0bed3b13d36a9f0c79bfa5d35e0b43add3be3b` |
| `tools/organism_aggregator.py` | `931f9742fc221755ca07e26def75ae71b2f6f579d6e9030e5458866efce45f72` |

Read-only findings:

```text
case-insensitive "EnzymeCAGE" occurrences in both tool files          0
HTTP User-Agent   ADRMATS-MicrobeCrew-Enzyme2Organism/1.0
outbound targets  UniProt REST and KEGG REST only
custom logging / logger / print disclosure in either tool             0
OrganismAggregator outbound requests                                   0
```

The actual third-party query identity was already generic. No algorithm,
schema, URL, retry policy, result field or aggregation rule required a Task 6
change, so an HPC run or private-ADRMATS source patch would add no evidence.

The accepted source copy also contains internal technical references such as
the real `enzymecage_wrapper` import and a frozen wrapper path in its smoke
report. These are package/provenance facts, not third-party query context.
They were not altered, because changing an accepted return would corrupt its
manifest and audit identity.

## 5. GitHub And Historical-Evidence Boundary

Known repositories:

```text
enzyme-side teacher delivery:
  https://github.com/bgruiiii/EnzymeCAGE-Teacher-Deliverables

microbial-side teacher delivery:
  https://github.com/bgruiiii/EnzymeCAGE-MetaTraits-Teacher-Deliverables

private implementation source:
  https://github.com/Water-Quality-Risk-Control-Engineering/ADRMATS
```

Task 6 belongs only to the microbial track. The enzyme-side delivery repository
must not be changed for this task.

Read-only remote verification found the microbial teacher-delivery repository
still at:

```text
65bbd2d459591f068340467740e972a4a689a42d
Add MetaTraits M4a teacher review packet
```

That historical packet contains the pre-decision email wording. It must not be
force-pushed, rebased away or silently overwritten. The corrected active email
and this audit should be added by a new commit, preferably in a dated Task 6 or
later consolidated delivery folder. No GitHub write was performed in this
local task.

## 6. Verification

```text
corrected email exact project-name scan                         0  PASS
obsolete "whether to retain project name" queue scan            0  PASS
accepted tool-source exact project-name scan                    0  PASS
generic User-Agent present                                      1  PASS
email unsent state preserved                                       PASS
accepted HPC source bytes unchanged                                PASS
historical teacher and audit evidence unchanged                    PASS
M4b/M4c implementation absent from this task                       PASS
```

## 7. Task State

```text
Task 5: LOCALLY AUDITED PASS; waiting for teacher adjudication
Task 6 local correction and audit: PASS
Task 6 GitHub synchronization: PENDING NEW NON-DESTRUCTIVE COMMIT
Task 6 HPC action: NOT REQUIRED by current evidence
Task 7 and later: NOT STARTED
```
