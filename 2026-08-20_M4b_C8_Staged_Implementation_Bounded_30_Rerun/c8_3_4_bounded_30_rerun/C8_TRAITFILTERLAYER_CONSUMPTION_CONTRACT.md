# C8 TraitFilterLayer Consumption Contract

This 30-row rerun is a C8 schema/validator smoke test only.
Future real C8 input must be the upstream enzyme candidate table with fields:
query_id / pollutant / reaction_candidate / enzyme_uid / enzyme_candidate_source / rank.

- Candidate UID without staged asset must fail closed as ASSET_NOT_AVAILABLE.
- One UID with multiple source_signature mappings must keep multiple rows.
- First screen displays F1-F5 priority fields.
- Additional F6-F15 fields are kept for follow-up explanation.
- Observed/predicted/missing/fungi identity-only must be explicitly labelled.
- No trait may hard filter.
- No trait_score or uncalibrated confidence may be used.
- 137 delta sources remain pending teacher decision and outside main C8.
