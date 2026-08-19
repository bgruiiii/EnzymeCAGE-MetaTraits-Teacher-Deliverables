# MetaTraits bulk TSV validation report

- task_id: `metatraits_bulk_tsv_landed_chenyu_20260818`
- official_base_url: https://www.bork.embl.de/~robbani/metatraits
- data_dir: `/usrdata/EnzymeCAGE_data/data/metatraits/incoming/metatraits_bulk_tsv_snapshot_20260818`
- return_dir: `/usrdata/EnzymeCAGE_data/EnzymeCAGE-master/HPC_Returned_Result_Summaries/metatraits_bulk_tsv_landed_chenyu_20260818`

| metric | value |
|---|---|
| required_summary_expected_count | 12 |
| required_summary_downloaded_count | 12 |
| required_summary_validated_count | 12 |
| companion_crosswalk_expected_count | 2 |
| companion_crosswalk_downloaded_count | 2 |
| companion_crosswalk_validated_count | 2 |
| all_required_summary_present | true |
| all_required_summary_gzip_test_pass | true |
| all_required_summary_sha256_present | true |
| all_companion_crosswalk_present | true |
| all_companion_crosswalk_gzip_test_pass | true |

## Final status

```
METATRAITS_BULK_TSV_LANDED_CHENYU_COMPLETE
```

## Boundaries

- boundary_no_api_call: true
- boundary_no_prediction_run: true
- boundary_no_production_mutation: true

## Per-file outcome

| file | role | download | gzip | validation | size | sha256 (8) |
|---|---|---|---|---|---|---|
| gtdb_family_summary_all.tsv.gz | bulk_summary | PASS | PASS | PASS | 10368529 | 99e81b30 |
| gtdb_family_summary_no_predictions.tsv.gz | bulk_summary | PASS | PASS | PASS | 1513013 | 4d1e47be |
| gtdb_genus_summary_all.tsv.gz | bulk_summary | PASS | PASS | PASS | 40283136 | a361dcea |
| gtdb_genus_summary_no_predictions.tsv.gz | bulk_summary | PASS | PASS | PASS | 4965442 | 82c6418e |
| gtdb_species_summary_all.tsv.gz | bulk_summary | PASS | PASS | PASS | 141667681 | 8eb08ea0 |
| gtdb_species_summary_no_predictions.tsv.gz | bulk_summary | PASS | PASS | PASS | 12570522 | e676d4cd |
| ncbi_family_summary_all.tsv.gz | bulk_summary | PASS | PASS | PASS | 2636007 | 783e8d46 |
| ncbi_family_summary_no_predictions.tsv.gz | bulk_summary | PASS | PASS | PASS | 913932 | 7f3549e8 |
| ncbi_genus_summary_all.tsv.gz | bulk_summary | PASS | PASS | PASS | 9907786 | 69a25f39 |
| ncbi_genus_summary_no_predictions.tsv.gz | bulk_summary | PASS | PASS | PASS | 2431808 | 59a06549 |
| ncbi_species_summary_all.tsv.gz | bulk_summary | PASS | PASS | PASS | 36900021 | 9118379f |
| ncbi_species_summary_no_predictions.tsv.gz | bulk_summary | PASS | PASS | PASS | 6523019 | 9e16ca57 |
| GTDB2NCBI.tsv.gz | companion_crosswalk | PASS | PASS | PASS | 2937650 | 892ecf04 |
| NCBI2GTDB.tsv.gz | companion_crosswalk | PASS | PASS | PASS | 2895086 | 761d5537 |
