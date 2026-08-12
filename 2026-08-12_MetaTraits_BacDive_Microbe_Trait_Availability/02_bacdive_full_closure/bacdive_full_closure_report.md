# BacDive Full-Table Closure Report
Date: 2026-08-12
Scope: BacDive-only evidence closure for 2,478 source_signatures (145,607 rows)

## 1. Background

本次评估基于已完成的 BacDive 全表 2,478 source_signature 物种验证结果，执行闭合分析以完善 designation 证据分箱、对 candidate_unvalidated 行实施保守式 rescue、重计算多策略覆盖率，并与 MetaTraits 物种级覆盖率进行重叠/互补分析。
This is still an availability/evidence audit task; BacDive and MetaTraits traits are kept separate.

## 2. Task A — Exact Designation Confidence Binning

| Confidence Level | Count |
|---|---|
| designation_strong | 25 |
| designation_medium | 12 |
| designation_weak_short_token | 5 |
| Total exact_designation | 42 |

Designation evidence was binned into three tiers:
- **designation_strong**: overlapping token length >= 4, or culture token overlap, or taxid match
- **designation_medium**: overlapping token length == 3, no stronger evidence
- **designation_weak_short_token**: overlapping token length <= 2, no stronger evidence

Weak designation rows are excluded from the conservative and hard exact-strain policies.

## 3. Task B — Conservative Rescue for candidate_unvalidated

| Metric | Count |
|---|---|
| Total candidate_unvalidated (original) | 56 |
| Rescued to validated species | 21 |
| Remains candidate_unvalidated | 35 |

Rescue rules applied in priority order:
1. **5.1 Parenthetical synonym**: organism_name contains a parenthetical binomial matching BacDive species
2. **5.2 NCBI TaxID match**: source TaxID matches a BacDive candidate's NCBI TaxID
3. **5.3 Curated synonym rules**: documented taxonomy renames from LPSN

Curated synonym rules file: `bacdive_candidate_rescue_synonym_rules.csv` (42 rules)

Rescued rows:

| source_signature | rule | evidence |
|---|---|---|
| proteome:UP000008545 | 5.3_curated_synonym_self | Source species matches BacDive species after strain-level resolution; BacDive re |
| proteome:UP000002565 | 5.3_curated_synonym_self | Source species matches BacDive species after strain-level resolution; BacDive re |
| proteome:UP000002719 | 5.3_curated_synonym_self | Source species matches BacDive species after strain-level resolution; BacDive re |
| proteome:UP000000540 | 5.3_curated_synonym_self | Source species matches BacDive species after strain-level resolution; BacDive re |
| proteome:UP000007104 | 5.3_curated_synonym_self | Source species matches BacDive species after strain-level resolution; BacDive re |
| taxon:28064|organism:heliobacterium mobile (heliob | 5.2_taxid_match | NCBI TaxID 28064 matches BacDive candidate 6118 (species: Heliobacillus mobilis) |
| taxon:839|organism:xylanibacter ruminicola (prevot | 5.2_taxid_match | NCBI TaxID 839 matches BacDive candidate 165980 (species: Prevotella ruminicola) |
| taxon:316|organism:stutzerimonas stutzeri (pseudom | 5.2_taxid_match | NCBI TaxID 316 matches BacDive candidate 177898 (species: Pseudomonas stutzeri) |
| taxon:1149133|organism:metapseudomonas furukawaii  | 5.2_taxid_match | NCBI TaxID 1149133 matches BacDive candidate 12966 (species: Pseudomonas furukaw |
| taxon:29518|organism:borreliella afzelii (borrelia | 5.2_taxid_match | NCBI TaxID 29518 matches BacDive candidate 14306 (species: Borrelia afzelii) |
| taxon:145261|organism:methanothermobacter wolfeii  | 5.2_taxid_match | NCBI TaxID 145261 matches BacDive candidate 6894 (species: Methanothermobacter w |
| taxon:145262|organism:methanothermobacter thermaut | 5.2_taxid_match | NCBI TaxID 145262 matches BacDive candidate 6887 (species: Methanothermobacter w |
| proteome:UP000002484 | 5.2_taxid_match | NCBI TaxID 298654 matches BacDive candidate 132738 (species: Frankia inefficax) |
| taxon:1556|organism:clostridium acidurici (gottsch | 5.2_taxid_match | NCBI TaxID 1556 matches BacDive candidate 2580 (species: Gottschalkia acidurici) |
| proteome:UP000062255 | 5.2_taxid_match | NCBI TaxID 134601 matches BacDive candidate 154031 (species: Mycobacterium goodi |
| taxon:188|organism:paramagnetospirillum magnetotac | 5.2_taxid_match | NCBI TaxID 188 matches BacDive candidate 13943 (species: Magnetospirillum magnet |
| taxon:39687|organism:mycolicibacterium austroafric | 5.2_taxid_match | NCBI TaxID 39687 matches BacDive candidate 8515 (species: Mycobacterium austroaf |
| taxon:80869|organism:paracidovorax citrulli (acido | 5.2_taxid_match | NCBI TaxID 80869 matches BacDive candidate 157282 (species: Acidovorax citrulli) |
| proteome:UP000543174 | 5.2_taxid_match | NCBI TaxID 412384 matches BacDive candidate 175296 (species: Bacillus aryabhatta |
| proteome:UP000037660 | 5.2_taxid_match | NCBI TaxID 1547922 matches BacDive candidate 140803 (species: Ideonella sakaiens |
| taxon:134601|organism:mycolicibacterium goodii (my | 5.2_taxid_match | NCBI TaxID 134601 matches BacDive candidate 154031 (species: Mycobacterium goodi |

Remaining unvalidated rows: 35

## 4. Task C — Coverage Policies

| Policy | Source Signatures | Fraction | Row-Weighted | Fraction |
|---|---|---|---|---|
| exact_strain_main | 597/2478 | 24.1% | 52455/145607 | 36.0% |
| exact_strain_conservative | 592/2478 | 23.9% | 51941/145607 | 35.7% |
| exact_strain_hard | 555/2478 | 22.4% | 46661/145607 | 32.0% |
| validated_species_or_better_main | 1725/2478 | 69.6% | 120271/145607 | 82.6% |
| validated_species_or_better_excluding_weak_designation | 1720/2478 | 69.4% | 119757/145607 | 82.2% |
| validated_species_or_better_hard_exact_only | 1683/2478 | 67.9% | 114477/145607 | 78.6% |
| validated_species_or_better_after_candidate_rescue | 1746/2478 | 70.5% | 121243/145607 | 83.3% |

Policy definitions:
- **exact_strain_main**: exact_genome + exact_culture_collection + all exact_designation
- **exact_strain_conservative**: exact_genome + exact_culture_collection + designation_strong + designation_medium
- **exact_strain_hard**: exact_genome + exact_culture_collection only
- **validated_species_or_better_main**: exact_strain_main + species_exact_name_match + species_taxid_or_synonym_match
- **validated_species_or_better_excluding_weak_designation**: exact_strain_conservative + species_exact + species_taxid_synonym
- **validated_species_or_better_hard_exact_only**: exact_strain_hard + species_exact + species_taxid_synonym
- **validated_species_or_better_after_candidate_rescue**: validated_species_or_better_main + rescued candidates

## 5. Task D — Trait Coverage Recomputation

| Policy Bin | Source Signatures | Row-Weighted | Unique Traits |
|---|---|---|---|
| exact_strain_hard | 555 | 46661 | 12 |
| exact_strain_conservative | 592 | 51941 | 12 |
| exact_strain_main | 597 | 52455 | 12 |
| validated_species_level | 1128 | 67816 | 12 |
| validated_species_or_better_main | 1725 | 120271 | 12 |
| validated_species_or_better_after_candidate_rescue | 1746 | 121243 | 12 |
| candidate_unvalidated_remaining | 35 | 2616 | 12 |
| not_found | 269 | 13751 | 0 |
| non_scope | 428 | 7997 | 0 |

Trait interpretation:
- exact strain traits = strain-level evidence
- validated species traits = species-level context only
- candidate_unvalidated traits = diagnostic only

## 6. Task E — BacDive vs MetaTraits Overlap

MetaTraits coverage column: `union_in_ncbi_all`
MetaTraits coverage file rows: 3234
MetaTraits overlap status: `computed`

BacDive has 2478 source_signatures; MetaTraits coverage file has 3234. Match by source_signature. 2478 BacDive signatures found in MetaTraits file.

### Source Signature-Level Overlap

| Policy | Both Covered | BacDive Only | MetaTraits Only | Neither |
|---|---|---|---|---|
| Main | 1508 | 238 | 130 | 602 |
| Conservative | 472 | 120 | 1166 | 720 |

### Row-Weighted Overlap

| Policy | Both Covered | BacDive Only | MetaTraits Only | Neither |
|---|---|---|---|---|
| Main | 107812 | 13431 | 6513 | 17851 |
| Conservative | 43898 | 8043 | 70427 | 23239 |

### Group-Level Overlap (Main Policy)

| Taxonomy Group | Resolution Level | Total | Both | BacDive Only | MetaTraits Only | Neither |
|---|---|---|---|---|---|---|
| target_archaea | proteome | 113 | 37 | 58 | 11 | 7 |
| target_archaea | taxon_organism | 40 | 14 | 24 | 1 | 1 |
| target_bacteria | proteome | 950 | 731 | 90 | 82 | 47 |
| target_bacteria | taxon_organism | 947 | 726 | 66 | 36 | 119 |
| target_fungi | proteome | 170 | 0 | 0 | 0 | 170 |
| target_fungi | taxon_organism | 258 | 0 | 0 | 0 | 258 |

## 7. Audit Results

| # | Check | Result |
|---|-------|--------|
| 1 | input BacDive rows == 2478 | PASS |
| 2 | row_count sum == 145607 | PASS |
| 3 | all original BacDive rows preserved | PASS |
| 4 | every exact_designation row has designation_confidence != empty | PASS |
| 5 | every weak designation row is excluded from conservative exact policy | PASS |
| 6 | no candidate rescue lacks candidate_rescue_evidence | PASS |
| 7 | no rescued candidate is based only on same genus | PASS |
| 8 | candidate_unvalidated remaining count is reported | PASS |
| 9 | summary counts equal JSONL counts | PASS |
| 10 | row-weighted total sums to 145607 | PASS |
| 11 | MetaTraits overlap input rows match source_signature universe or mismatch is reported | PASS |
| 12 | MetaTraits is not used as fallback to alter BacDive trait fields | PASS |
| 13 | final report contains no casual audience-specific wording | PASS |

**Overall: ALL PASS**

## 8. 解释边界

综合判断：

- BacDive 覆盖率在 main policy 下达到 70.5% (source_signature-level) 和 83.3% (row-weighted)。
- Conservative policy 排除了 weak designation 后，覆盖率略降，为 69.4% (source_signature-level) 和 82.2% (row-weighted)。
- Hard exact policy（仅 genome + culture collection）覆盖率为 22.4% (source_signature-level)。
- Candidate rescue 将部分 taxonomy rename 行从 unvalidated 提升为 validated species，共 rescue 21 行。
- MetaTraits 覆盖率在 source_signature-level 约为 1638/2478 = 66.1%。
- BacDive 覆盖率（main policy）约为 1746/2478 = 70.5%。
- 两者重叠覆盖（both covered）为 1508 source_signatures。

## 9. 建议下一步

1. 对 remains_candidate_unvalidated 的行，考虑在后续版本中扩展 curated synonym rules 或通过 NCBI Taxonomy 查询验证。
2. 对于 weak designation 行，考虑在后续版本中引入 culture collection 交叉验证以提升证据强度。
3. 基于 overlap 分析结果，设计 BacDive+MetaTraits 合并 pipeline 的优先级策略：BacDive covered 优先使用 BacDive traits；MetaTraits only 行使用 MetaTraits 作为补充。
4. 本次闭合结果可作为正式报告更新的依据。

## 10. Output Files

| File | Description |
|---|---|
| bacdive_full_closure_results.jsonl | All 2,478 rows with closure fields |
| bacdive_full_closure_summary.json | Summary with all policy counts |
| bacdive_full_closure_trait_coverage.csv | Trait coverage by policy bin |
| bacdive_full_designation_confidence.csv | Designation confidence details |
| bacdive_candidate_rescue_review.csv | Candidate rescue review |
| bacdive_candidate_rescue_synonym_rules.csv | Curated synonym rules |
| bacdive_metatraits_overlap_by_source_signature.csv | Overlap by source_signature |
| bacdive_metatraits_overlap_summary.json | Overlap summary |
| bacdive_metatraits_overlap_by_group.csv | Overlap by taxonomy group |
| bacdive_metatraits_overlap_examples.csv | Overlap examples (bacdive_only, metatraits_only) |
| bacdive_full_closure_audit.md | Audit checks |
| bacdive_full_closure_report.md | This report |

This closure keeps BacDive-only evidence separate from MetaTraits, adds confidence-aware exact-designation handling, and provides the overlap table needed for a final report update.
