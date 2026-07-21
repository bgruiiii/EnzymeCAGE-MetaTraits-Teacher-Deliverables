#!/usr/bin/env python3
"""Portable standard-library M4a-4BAAAA validator and public fixture schema."""
import argparse, base64, csv, hashlib, json, math, os, pathlib, re, shutil, stat, sys

READY="M4A4B_BENCHMARK_READY_FOR_LOCAL_AUDIT_COEXISTENCE_OPEN"
INCOMPLETE="M4A4B_BENCHMARK_INCOMPLETE_PREDICTION_OR_CONCURRENCY_FAILURE"
BLOCKED_GPU="M4A4B_BENCHMARK_BLOCKED_IMMEDIATE_GPU_GATE"
BLOCKED_RUNTIME="M4A4B_BENCHMARK_BLOCKED_RUNTIME_ENVIRONMENT"
BLOCKED_PROVENANCE="M4A4B_BENCHMARK_BLOCKED_RUNTIME_PROVENANCE_AFTER_EVIDENCE_CAPTURE"
BLOCKED_PACKAGING="M4A4B_BENCHMARK_BLOCKED_PACKAGING_OR_TRANSPORT"
STATUSES=(READY,INCOMPLETE,BLOCKED_GPU,BLOCKED_RUNTIME,BLOCKED_PROVENANCE,BLOCKED_PACKAGING)
CORRECTION_TOKEN="M4A4BAAAA_READY_ADVERSARIAL_STATUS_AND_TRANSCRIPT_SEMANTICS_FOR_LOCAL_AUDIT"
CODE_ROOT="/usrdata/EnzymeCAGE_data/EnzymeCAGE-master"
PYG_PREFIX="/usrdata/EnzymeCAGE_envs/enzymecage_py312/lib/python3.12/site-packages/torch_geometric"
FIXED_AUTHORITY={
"ADRMATS_ZIP":(1040341,"dc33c60b6876fed6969dc56a28a688077b17ef2f5a3510fadd78f085e13834b2"),"M4A3A_TAR":(819200,"7f213605f1aed7065bdda256a6b33955e64f8cabb547a597e5ac8e74be766f87"),"D4B1A_TAR":(10874880,"12df378964793561c2d193d92c16276739b14df1761ff34c0e46f426e5cad0f7"),"D4B1A_MANIFEST":(7231,"944fe2d22b6b43808a1d6a6250ad62e652a4b52e7e7b36d91a58a012fecd326d"),"REQUESTS":(6361,"22686730733f2b23ac0a299eec340e0f3a74a26bd0bc18bc17dce9768a379aa6"),"WRAPPER_PREDICTOR":(7616,"b9877649deea4f929778331453a0f1f4b95d0a56c4ab82d3"),"WRAPPER_SCHEMA":(1310,"a27f33adf78bb2c7a9961d4372cfea0f7728ca91eb89e3b0a6cc7a1e6488fc35"),"ASSET_INDEX":(5039,"07dceed083aecb5310ac3b208f0a1bca8e147aeb69897908b529045ba30d7d3c"),"RUNTIME_IDENTITY":(791,"3f4ab3acb6729a57e01aeffcfcbbaa27fa713078dabc0ee3fa31fc44e91fbe54"),"ENVIRONMENT_OVERLAY":(3484,"3a5f877ef24ceeead981ed54445b0d5bd2dc027c31bca8192ac542526ccaa058"),"D4B_RUNNER":(29159,"7f6cfb63c88088125f687e80e9e51ba8eb01dbbd37b3c285c2c1d584e4432904"),"V1_MANIFEST":(4863,"87d884d1dc0ffd46ab54a834dc3a5be3434530ca9b1e9a7bb72819afa12ac426"),"V1_REGISTRY":(601,"19e12926c0909039cab29464ceb2d8eb682711c7ae46f1eefa1d6761a7f0c8ef"),"PBB_TAR":(378880,"e0f84dcaf0bb808c715b4efc7c6b92ffe286ee3fd666ea78d24f63a4b28b6ee0"),"PBB_IDENTITY":(3707,"1fabe52e32a98558b3e3c91614eb1e6b9291e82b135d3da8f903a3d6cc3feac9"),"PBB_OVERLAY_MANIFEST":(18297,"cf470b282352ce4f24d820ac31a3680c265f465f7bc4e14a48fc8b1a6a98a300"),"T3G1A_SOURCE_IDENTITY":(7862,"c12903ec1fe4463905f3e330feb27252cb396cc9acb865ec0640a627cb09cfdf"),"PRIOR_TAR":(1822720,"6c62faa574635c2e5db6d50e9806a2b188eb7f2b7c177b80b74a995e8c606044"),"PRIOR_IDENTITY":(1411,"1a30741ff9da0f88345df2eb7313c9e98b13a31ed298cf7b65aca18a7df3cf09"),"PRIOR_MANIFEST":(4421,"1b2ab7e25ce15f8fa3502be673c141ac182486a1e5d3afd6bf3009d6bc1d0e3e"),
"CHECKPOINT_40":(72266498,"a95d4687e2cadad1c12f7c1defd21dbdf43db3cce96aa9caace39dbcc226586d"),"CHECKPOINT_41":(72266498,"c429a98bc265e20d415c3d6f479e0f0d6c47d81c13135c589e2a5e173978dbef"),"CHECKPOINT_42":(72266498,"cc54be33a23b78fb89c183f0bca6f87b442a5be4dad9666428d05a72a9b7f7a3"),"CHECKPOINT_43":(72266498,"3eb80be83cb41574204239c80f11008f728029dd9e4ba14c639749d8176b5220"),"CHECKPOINT_44":(72266498,"b9547d3ba17725a5910cf243d33af9367abb12b3215f4b526405f8bdb14acd16")}
FIXED_AUTHORITY["WRAPPER_PREDICTOR"]=(7616,"b9877649deea4f929778331453a0f1f4eb73d72529e3f1c4b95d0a56c4ab82d3")
CALL_HEADER=["phase","global_request_id","call_index","worker_id","worker_sequence","barrier_release_ns","start_utc","start_ns","end_utc","end_ns","latency_ms","success","exception_type","exception_message","integrity_pass","integrity_failure_reason","returned_count","response_sha256","uid_order_sha256","evidence_hash","max_abs_score_difference_from_first_sequential","max_abs_ci_difference_from_first_sequential"]
MEM_HEADER=["utc_timestamp","monotonic_ns","gpu_uuid","gpu_index","device_used_mib","device_free_mib","utilization_percent","benchmark_pid","process_used_mib","phase","device_query_status","process_query_status"]
GPU_HEADER=["sample","utc_timestamp","monotonic_ns","gpu_index","gpu_uuid","name","driver","total_mib","used_mib","free_mib","utilization_percent","compute_mode","compute_process_count","compute_process_rows_json"]
PRIOR_FILES=frozenset({
"FINAL_STATUS.txt","M4A4B_FORMAL_GPU_BENCHMARK_REPORT.md","MANIFEST.sha256","inputs/formal_benchmark_contract.json","scripts/run_m4a4b_formal_gpu_benchmark.py","scripts/validate_m4a4b_formal_gpu_benchmark.py",
"outputs/required_input_identity.json","outputs/runtime_source_identity.json","outputs/live_runtime_overlay_gate.json","outputs/gpu_selection_or_block.json","outputs/coexistence_boundary.json","outputs/scope_compliance.json","outputs/benchmark_provenance.json","outputs/benchmark_progress.json","outputs/runtime_preload.json","outputs/warmup_audit.json","outputs/sequential_summary.json","outputs/concurrency_2_summary.json","outputs/concurrency_4_summary.json","outputs/latency_degradation.json","outputs/memory_summary.json","outputs/response_integrity.json","outputs/validator_results.json",
"evidence/runtime_source_tree_before.sha256","evidence/runtime_source_tree_after.sha256","evidence/imported_enzymecage_modules.json","evidence/generated_module_provenance.json","evidence/gpu_gate_samples.csv","evidence/benchmark_process_start.json","evidence/nvidia_smi_memory_samples.csv","evidence/environment.txt","evidence/commands.txt","evidence/warmup_calls.csv","evidence/sequential_100_calls.csv","evidence/concurrency_2_100_calls.csv","evidence/concurrency_4_100_calls.csv","evidence/first_response_warmups.json","evidence/first_response_sequential.json","evidence/first_response_concurrency_2.json","evidence/first_response_concurrency_4.json",
"logs/benchmark.stdout.txt","logs/benchmark.stderr.txt","logs/benchmark.exit_code.txt","logs/validator_negative_tests.csv","logs/validator_negative_tests.stdout.txt"})
PRESERVED=frozenset({"evidence/prior_validate_m4a4b_formal_gpu_benchmark.py","evidence/prior_validator_negative_tests.csv","evidence/prior_validator_negative_tests.stdout.txt","evidence/prior_validator_results.json"})
BA_ADDED=frozenset({"M4A4BA_CORRECTION_REPORT.md","evidence/fixed_input_identity_ledger.json","evidence/inherited_m4a4b_file_identity.json","outputs/correction_provenance.json","outputs/memory_evidence_classification.json","scripts/test_m4a4ba_status_fixtures.py","logs/status_fixture_tests.csv","logs/status_fixture_tests.stdout.txt"})
BAA_ADDED=frozenset({"M4A4BAA_CORRECTION_REPORT.md","evidence/inherited_m4a4ba_file_identity.json","evidence/prior_m4a4ba_correction_provenance.json","evidence/prior_m4a4ba_inherited_m4a4b_file_identity.json","evidence/prior_m4a4ba_status_fixture_runner.py","evidence/prior_m4a4ba_validator_results.json","scripts/run_m4a4baa_validation_suite.py","logs/m4a4baa_validation_suite.csv","logs/m4a4baa_validation_suite.stdout.txt"})
RESULT_FILES=frozenset({"MANIFEST.sha256","logs/validator_negative_tests.csv","logs/validator_negative_tests.stdout.txt","outputs/validator_results.json","logs/status_fixture_tests.csv","logs/status_fixture_tests.stdout.txt","logs/m4a4baa_validation_suite.csv","logs/m4a4baa_validation_suite.stdout.txt"})
BAA_READY_FILES=frozenset(PRIOR_FILES|PRESERVED|BA_ADDED|BAA_ADDED)
BAAA_ADDED=frozenset({"M4A4BAAA_CORRECTION_REPORT.md","evidence/inherited_m4a4baa_file_identity.json","evidence/prior_m4a4baa_validator.py","evidence/prior_m4a4baa_fixture_runner.py","evidence/prior_m4a4baa_negative_runner.py","evidence/prior_m4a4baa_validator_results.json","evidence/prior_m4a4baa_correction_provenance.json"})
BAAAA_ADDED=frozenset({"M4A4BAAAA_CORRECTION_REPORT.md","evidence/inherited_m4a4baaa_file_identity.json","evidence/prior_m4a4baaa_validator.py","evidence/prior_m4a4baaa_fixture_runner.py","evidence/prior_m4a4baaa_negative_runner.py","evidence/prior_m4a4baaa_validator_results.json","evidence/prior_m4a4baaa_correction_provenance.json"})
READY_FILES=frozenset(BAA_READY_FILES|BAAA_ADDED|BAAAA_ADDED)
BASE=frozenset({"FINAL_STATUS.txt","M4A4B_FORMAL_GPU_BENCHMARK_REPORT.md","scripts/validate_m4a4b_formal_gpu_benchmark.py","outputs/coexistence_boundary.json","outputs/scope_compliance.json","outputs/benchmark_provenance.json"})
RAW=frozenset({"evidence/warmup_calls.csv","evidence/sequential_100_calls.csv","evidence/concurrency_2_100_calls.csv","evidence/concurrency_4_100_calls.csv"})
STATUS_FILES={
 READY:READY_FILES,
 INCOMPLETE:BASE|RAW|{"outputs/benchmark_progress.json"},
 BLOCKED_GPU:BASE|{"outputs/gpu_selection_or_block.json","outputs/benchmark_progress.json","evidence/gpu_gate_samples.csv","evidence/benchmark_process_start.json"},
 BLOCKED_RUNTIME:BASE|RAW|{"outputs/benchmark_progress.json"},
 BLOCKED_PROVENANCE:BASE|RAW|{"outputs/benchmark_progress.json","evidence/runtime_source_tree_before.sha256","evidence/runtime_source_tree_after.sha256","evidence/imported_enzymecage_modules.json","evidence/generated_module_provenance.json"},
 BLOCKED_PACKAGING:(BAA_READY_FILES-RESULT_FILES-{"MANIFEST.sha256"})|{"outputs/packaging_failure.json"}}
EXPECTED_FILES_BY_STATUS={k:frozenset(v) for k,v in STATUS_FILES.items()}
NEGATIVE_CASES=(
 ("N01","duplicate_first_uid","first_response_uid_integrity"),("N02","wrong_rank","first_response_rank"),("N03","out_of_pool_uid","first_response_uid_integrity"),("N04","nonfinite_score","nonfinite_value"),("N05","invalid_ci","first_response_ci"),("N06","uid_order_mismatch","uid_order_hash"),("N07","row_evidence_hash","row_evidence_hash"),("N08","duplicate_global_id","global_call_id"),("N09","malformed_global_id","global_call_id"),("N10","warmup_call_index","call_index_or_worker_sequence"),("N11","concurrency_worker_sequence","call_index_or_worker_sequence"),("N12","barrier_cardinality","barrier_cardinality"),("N13","nearest_rank_stat","statistics_recompute"),("N14","degradation_ratio","degradation_recompute"),("N15","fixed_input_authority","fixed_input_authority"),("N16","pyg_path_spec","pyg_helper_path_spec"),("N17","pyg_linkage","pyg_live_linkage_cross_consistency"),("N18","pyg_owner_parent","pyg_owner_parent"),("N19","pyg_version","pyg_environment"),("N20","pyg_root","pyg_environment"),("N21","pyg_template_hash","pyg_generator_source"),("N22","torch_negative","torch_memory_structure"),("N23","torch_nonnumeric","torch_memory_structure"),("N24","torch_peak_below_end","torch_memory_structure"),("N25","memory_missing_phase","memory_phase_coverage"),("N26","memory_query_status","memory_query_status"),("N27","fake_provenance_blocker","provenance_blocker_semantics"),("N28","real_provenance_as_ready","pyg_inventory"),("N29","gpu_block_with_torch_artifact","wrong_file_set"),("N30","runtime_without_traceback","runtime_blocker_semantics"),("N31","packaging_without_blocker","packaging_blocker_semantics"),("N32","coexistence_pass","coexistence_boundary"),("N33","m4b_true","scope_boundary"),("N34","m4c_true","scope_boundary"),("N35","unknown_status","unknown_final_status"),("N36","undeclared_file","wrong_file_set"),("N37","unsafe_mode","unsafe_mode"),("N38","unsafe_link","unsafe_object"),("N39","malformed_utf8","malformed_utf8"),("N40","empty_directory","empty_or_undeclared_directory"),("N41","secret_payload","secret_like_payload"),
 ("N42","default_fixture_runner_writes_package_bytecode_cache","source_tree_changed"),("N43","blocked_provenance_zero_durable_rows","provenance_requires_durable_rows"),("N44","blocked_provenance_generated_imported_rejection_mismatch","provenance_rejection_cross_consistency"),("N45","blocked_gpu_blocker_mismatch_across_files","gpu_blocker_cross_consistency"),("N46","blocked_runtime_blocker_mismatch_across_files","runtime_blocker_semantics"),("N47","blocked_packaging_incomplete_prepackaging_evidence","call_count"),("N48","bogus_inherited_new_manifest_identity","manifest_self_reference"),("N49","preliminary_or_failed_reverse_gate_provenance","final_reverse_provenance"),("N50","fabricated_positive_fixture_rows_transcript","positive_fixture_evidence"),("N51","duplicate_fabricated_negative_rows_transcript","negative_suite_evidence"),("N52","validator_results_reverse_gates_fail","final_reverse_provenance"),("N53","missing_duplicate_expected_test_ids","test_id_set"),
 ("N54","malformed_incomplete_partial_call_row","partial_call_row_semantics"),("N55","malformed_blocked_provenance_durable_success_row","partial_call_row_semantics"),("N56","malformed_blocked_gpu_sample","gpu_sample_semantics"),("N57","duplicate_negative_suite_log_mismatch","duplicate_suite_evidence_mismatch"),("N58","falsified_transcript_details","transcript_cross_consistency"),("N59","blocked_packaging_fixed_input_failure","fixed_input_authority"),("N60","blocked_packaging_fatal_stream","fatal_stream_content"),("N61","blocked_packaging_false_inheritance","m4a4ba_inheritance_identity"),("N62","blocked_provenance_equal_ledgers_inside_root_rejection","provenance_blocker_semantics"),("N63","blocked_gpu_generic_wrong_blocker","gpu_blocker_schema"),("N64","incomplete_generic_wrong_blocker","incomplete_blocker_schema"),("N65","correction_report_boundary_contradiction","correction_report_semantics"),("N66","correction_provenance_boundary_contradiction","correction_provenance_schema"),("N67","validator_results_core_failure","validator_results_schema"),("N68","correction_provenance_core_gate_failure","correction_provenance_schema"),
 ("N69","incomplete_blocker_type_row_mismatch","incomplete_blocker_evidence"),("N70","blocked_provenance_inside_root_rejected_module","provenance_blocker_semantics"),("N71","blocked_gpu_contradictory_threshold_message","gpu_blocker_semantics"),("N72","packaged_transcript_extra_contradictory_line","transcript_cross_consistency"),("N73","ready_call_row_malformed_utc","call_utc"))
POSITIVE_IDS=tuple("F%02d"%i for i in range(1,7))
PHASE_FILES=(("warmups","warmup_calls.csv"),("sequential","sequential_100_calls.csv"),("concurrency_2","concurrency_2_100_calls.csv"),("concurrency_4","concurrency_4_100_calls.csv"))
UTC_RE=re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(?:\.[0-9]{6})?Z")
GPU_UTC_RE=re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(?:\.[0-9]{1,9})?Z")
REPORT_BOUNDARY_BLOCK="""positive fixtures = 6/6 PASS
negative suite = 73/73 PASS
coexistence = OPEN/NOT_ESTABLISHED
coexistence_pass = false
m4b_authorized = false
m4c_authorized = false
formal_m4a_closure = false
gpu/model/prediction work in this correction = false"""

class ValidationError(Exception): pass
def fail(reason,detail="failed"): raise ValidationError(reason+":"+str(detail)[:220].replace("\n"," ").replace("\r"," "))
def strict_json(path,reason="strict_json"):
 try: return json.loads(pathlib.Path(path).read_text(encoding="utf-8"),parse_constant=lambda x:fail("nonfinite_value",x))
 except (UnicodeDecodeError,json.JSONDecodeError) as e: fail(reason,e)
def canonical(x): return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()
def identity(path):
 b=pathlib.Path(path).read_bytes(); return len(b),hashlib.sha256(b).hexdigest()
def finite(v,reason="nonfinite_value"):
 try: x=float(v)
 except (TypeError,ValueError): fail(reason,v)
 if not math.isfinite(x): fail(reason,v)
 return x
def nonnegative(v,reason):
 x=finite(v,reason)
 if x<0: fail(reason,v)
 return x
def read_dict_csv(path,header,reason="csv_header"):
 try:
  with pathlib.Path(path).open(newline="",encoding="utf-8") as f: rd=csv.DictReader(f,strict=True); rows=list(rd); fields=rd.fieldnames
 except (UnicodeDecodeError,csv.Error) as e: fail("strict_csv",e)
 if fields!=header: fail(reason,pathlib.Path(path).name)
 return rows

def expected_files_for_status(status,phase):
 if status not in EXPECTED_FILES_BY_STATUS: fail("unknown_final_status",status)
 result=set(EXPECTED_FILES_BY_STATUS[status])
 if status==READY and phase=="evidence": result-=RESULT_FILES
 if status!=READY and phase=="packaged": result.add("MANIFEST.sha256")
 return frozenset(result)

def scan_tree(root,status,phase):
 expected=expected_files_for_status(status,phase); actual=set(); dirs=set(); secret=re.compile(rb"(?:AKIA[0-9A-Z]{16}|sk-[A-Za-z0-9_-]{16,}|(?:password|api[_-]?key|access[_-]?token)\s*[:=]\s*[^\s\"']+)",re.I)
 s=root.lstat()
 if root.is_symlink() or not stat.S_ISDIR(s.st_mode) or stat.S_IMODE(s.st_mode)!=0o755: fail("package_structure","root")
 for p in root.rglob("*"):
  st=p.lstat(); rel=p.relative_to(root).as_posix()
  if stat.S_ISDIR(st.st_mode):
   if stat.S_IMODE(st.st_mode)!=0o755: fail("unsafe_mode",rel)
   dirs.add(rel); continue
  if stat.S_ISLNK(st.st_mode) or not stat.S_ISREG(st.st_mode) or st.st_nlink!=1: fail("unsafe_object",rel)
  if stat.S_IMODE(st.st_mode)!=(0o755 if rel.startswith("scripts/") else 0o644): fail("unsafe_mode",rel)
  actual.add(rel)
 if actual!=expected: fail("wrong_file_set",f"missing={sorted(expected-actual)} extra={sorted(actual-expected)}")
 needed=set()
 for rel in expected:
  parent=pathlib.PurePosixPath(rel).parent
  while str(parent)!=".": needed.add(str(parent)); parent=parent.parent
 if dirs!=needed: fail("empty_or_undeclared_directory",sorted(dirs^needed))
 for rel in sorted(expected):
  data=(root/rel).read_bytes()
  if secret.search(data): fail("secret_like_payload",rel)
  try: data.decode("utf-8")
  except UnicodeDecodeError: fail("malformed_utf8",rel)
 return expected

def validate_manifest(root,expected):
 rows={}
 for line in (root/"MANIFEST.sha256").read_text(encoding="utf-8").splitlines():
  m=re.fullmatch(r"([0-9a-f]{64})  (.+)",line)
  if not m: fail("manifest_format","line")
  h,rel=m.groups(); pure=pathlib.PurePosixPath(rel)
  if rel in rows or pure.is_absolute() or ".." in pure.parts or "\\" in rel or rel=="MANIFEST.sha256": fail("manifest_format",rel)
  rows[rel]=h
 actual={rel:identity(root/rel)[1] for rel in expected if rel!="MANIFEST.sha256"}
 if rows!=actual: fail("manifest_mismatch","content")

def validate_common(root,status):
 if (root/"FINAL_STATUS.txt").read_text(encoding="utf-8").strip()!=status: fail("final_status","mismatch")
 if status not in (root/"M4A4B_FORMAL_GPU_BENCHMARK_REPORT.md").read_text(encoding="utf-8"): fail("status_cross_consistency","report")
 c=strict_json(root/"outputs/coexistence_boundary.json")
 req={"adrmats_remote_model_names":6,"additional_local_adrmats_gpu_models_proven":0,"coexistence_classification":"COEXISTENCE_LOCAL_MODEL_SET_NOT_ESTABLISHED","coexistence_teacher_requirement":"OPEN_WAIT_TEACHER_INTERPRETATION","coexistence_pass":False}
 if c!=req: fail("coexistence_boundary","mismatch")
 s=strict_json(root/"outputs/scope_compliance.json")
 for key in ("network_api_called","dependency_changed","source_or_overlay_modified","model_modified_or_trained","additional_local_model_loaded","m4b_authorized","m4c_authorized","hard_trait_filter_implemented"):
  if s.get(key) is not False: fail("scope_boundary",key)
 pending={"abc_complete_comparison","snapshot_review","maintainer_inquiry_unsent","strain_species_policy","final_checkpoint_strategy","zero_additional_local_model_coexistence_interpretation","m4a_full_closure"}
 if set(s.get("teacher_pending",[]))!=pending: fail("scope_boundary","teacher_pending")
 p=strict_json(root/"outputs/benchmark_provenance.json")
 if p.get("final_status")!=status: fail("status_cross_consistency","provenance")
 return p

def parse_ledger(text):
 lines=text.splitlines()
 if not lines or lines[0]!="relative_path\tmode\tbytes\tsha256": fail("source_ledger","header")
 out={}
 for line in lines[1:]:
  v=line.split("\t")
  pure=pathlib.PurePosixPath(v[0]) if v else pathlib.PurePosixPath(".")
  if len(v)!=4 or v[0] in out or pure.is_absolute() or ".." in pure.parts or "\\" in v[0] or str(pure) in (".","") or v[1] not in ("0644","0666","0755") or not re.fullmatch(r"[0-9]+",v[2]) or not re.fullmatch(r"[0-9a-f]{64}",v[3]): fail("source_ledger","row")
  out[v[0]]=(v[1],int(v[2]),v[3])
 return out

def validate_partial_call_rows(root,progress):
 """Shared strict parser for every partial INCOMPLETE/PROVENANCE call row."""
 global_ids=set(); by_phase={}; failed_phases=set(); total=successes=failures=0
 for phase,file in PHASE_FILES:
  rows=read_dict_csv(root/"evidence"/file,CALL_HEADER); by_phase[phase]=rows; indices=set(); barriers=set()
  workers=1 if phase in ("warmups","sequential") else int(phase.rsplit("_",1)[1])
  for row in rows:
   try:
    if row["phase"]!=phase: fail("partial_call_row_semantics","phase")
    gid=row["global_request_id"]; pattern=rf"{re.escape(phase)}-[0-9]{{3}}" if workers==1 else rf"{re.escape(phase)}-w[0-{workers-1}]-s[0-9]{{3}}"
    if not re.fullmatch(pattern,gid) or gid in global_ids: fail("partial_call_row_semantics","global_request_id")
    global_ids.add(gid)
    if not re.fullmatch(r"[1-9][0-9]*",row["call_index"]): fail("partial_call_row_semantics","call_index")
    idx=int(row["call_index"])
    if idx in indices: fail("partial_call_row_semantics","duplicate_call_index")
    indices.add(idx)
    if workers==1:
     if row["worker_id"] or row["worker_sequence"] or row["barrier_release_ns"]: fail("partial_call_row_semantics","single_worker_fields")
    else:
     if not re.fullmatch(r"[0-9]+",row["worker_id"]) or not re.fullmatch(r"[1-9][0-9]*",row["worker_sequence"]) or not re.fullmatch(r"[1-9][0-9]*",row["barrier_release_ns"]): fail("partial_call_row_semantics","worker_fields")
     worker=int(row["worker_id"]); sequence=int(row["worker_sequence"]); barriers.add(int(row["barrier_release_ns"]))
     if worker not in range(workers) or sequence not in range(1,51) or idx!=worker*50+sequence: fail("partial_call_row_semantics","worker_sequence")
    if not UTC_RE.fullmatch(row["start_utc"]) or not UTC_RE.fullmatch(row["end_utc"]): fail("partial_call_row_semantics","utc")
    if not re.fullmatch(r"[0-9]+",row["start_ns"]) or not re.fullmatch(r"[0-9]+",row["end_ns"]): fail("partial_call_row_semantics","monotonic")
    start=int(row["start_ns"]); end=int(row["end_ns"]); latency=nonnegative(row["latency_ms"],"partial_call_row_semantics")
    if end<start or not math.isclose(latency,(end-start)/1e6,rel_tol=0,abs_tol=1e-9): fail("partial_call_row_semantics","latency")
    if row["success"] not in ("true","false") or row["integrity_pass"] not in ("true","false"): fail("partial_call_row_semantics","boolean")
    for field in ("max_abs_score_difference_from_first_sequential","max_abs_ci_difference_from_first_sequential"):
     if row[field]!="": nonnegative(row[field],"partial_call_row_semantics")
    if not re.fullmatch(r"[0-9]+",row["returned_count"]): fail("partial_call_row_semantics","returned_count")
    returned=int(row["returned_count"])
    if row["success"]=="true":
     if row["integrity_pass"]!="true" or row["exception_type"] or row["exception_message"] or row["integrity_failure_reason"] or returned!=100: fail("partial_call_row_semantics","successful_structure")
     if any(not re.fullmatch(r"[0-9a-f]{64}",row[k]) for k in ("response_sha256","uid_order_sha256","evidence_hash")): fail("partial_call_row_semantics","successful_hash")
     successes+=1
    else:
     if not row["exception_type"].strip() or not row["exception_message"].strip() or not 0<=returned<=100: fail("partial_call_row_semantics","failed_structure")
     if (row["integrity_failure_reason"].strip() or "integrity" in row["exception_type"].lower()) and row["integrity_pass"]!="false": fail("partial_call_row_semantics","failed_integrity")
     if any(row[k] for k in ("response_sha256","uid_order_sha256","evidence_hash")): fail("partial_call_row_semantics","failed_promoted_identity")
     failures+=1; failed_phases.add(phase)
   except (ValueError,KeyError,TypeError): fail("partial_call_row_semantics","field")
  if workers>1 and rows and len(barriers)!=1: fail("partial_call_row_semantics","barrier")
  n,h=identity(root/"evidence"/file); q=progress.get("phases",{}).get(phase,{})
  expected={"attempted":len(rows),"success":sum(x["success"]=="true" for x in rows),"failure":sum(x["success"]=="false" for x in rows),"summary_present":False,"file":{"path":"evidence/"+file,"bytes":n,"sha256":h}}
  if q!=expected: fail("partial_progress",phase)
  total+=len(rows)
 if progress.get("forward_call_count")!=total: fail("partial_progress","forward_call_count")
 return by_phase,total,successes,failures,failed_phases

def validate_fixed_ledger(root,args):
 x=strict_json(root/"evidence/fixed_input_identity_ledger.json")
 items=x.get("items",[])
 if x.get("all_pass") is not True or x.get("item_count")!=25 or len(items)!=25 or len({i.get("key") for i in items})!=25: fail("fixed_input_authority","summary")
 if set(FIXED_AUTHORITY)!={i.get("key") for i in items}: fail("fixed_input_authority","authority key set")
 for i in items:
  if (i.get("expected_bytes"),i.get("expected_sha256"))!=FIXED_AUTHORITY[i.get("key")]: fail("fixed_input_authority","authority:"+str(i.get("key")))
  if i.get("result")!="PASS" or i.get("bytes")!=i.get("expected_bytes") and i.get("expected_bytes") is not None or i.get("sha256")!=i.get("expected_sha256"): fail("fixed_input_authority",i.get("key"))
  if i.get("object_type")!="regular_file" or i.get("link_count")!=1 or i.get("mode") not in ("0644","0755"): fail("fixed_input_authority",i.get("key"))
 commands=x.get("commands",{})
 for key in ("pbb_packaged_captured","pbb_packaged_live","prior_validator_historical"):
  q=commands.get(key,{})
  if q.get("exit_code")!=0 or q.get("stderr_bytes")!=0 or q.get("ready_token_count")!=1 or not re.fullmatch(r"[0-9a-f]{64}",q.get("stdout_sha256","") or ""): fail("fixed_input_authority",key)
 if x.get("prior_m4a4b_tar",{}).get("sha256")!="6c62faa574635c2e5db6d50e9806a2b188eb7f2b7c177b80b74a995e8c606044": fail("fixed_input_authority","prior sha")
 if args.runtime_evidence_mode=="live":
  amap={"ADRMATS_ZIP":args.adrmats_zip,"M4A3A_TAR":args.m4a3a_tar,"D4B1A_TAR":args.d4b1a_tar,"D4B1A_MANIFEST":str(pathlib.Path(args.d4b1a_root)/"MANIFEST.sha256"),"REQUESTS":str(pathlib.Path(args.d4b1a_root)/"outputs/smoke_case_requests.json"),"WRAPPER_PREDICTOR":str(pathlib.Path(args.d4b1a_root)/"enzymecage_wrapper/predictor.py"),"WRAPPER_SCHEMA":str(pathlib.Path(args.d4b1a_root)/"enzymecage_wrapper/schema.py"),"ASSET_INDEX":str(pathlib.Path(args.d4b1a_root)/"enzymecage_wrapper/asset_index.py"),"RUNTIME_IDENTITY":str(pathlib.Path(args.d4b1a_root)/"outputs/runtime_identity.json"),"ENVIRONMENT_OVERLAY":str(pathlib.Path(args.d4b1a_root)/"evidence/environment_with_overlay.txt"),"D4B_RUNNER":str(pathlib.Path(args.d4b1a_root)/"scripts/d4b_formal_smoke_runner.py"),"V1_MANIFEST":str(pathlib.Path(args.v1_root)/"MANIFEST.txt"),"V1_REGISTRY":str(pathlib.Path(args.v1_root)/"outputs/frozen_model_registry.json"),"PBB_TAR":args.pbb_tar,"PBB_IDENTITY":args.pbb_identity,"PBB_OVERLAY_MANIFEST":str(pathlib.Path(args.pbb_root)/"evidence/overlay_tree_manifest.sha256"),"T3G1A_SOURCE_IDENTITY":args.t3g1a_source_identity,"PRIOR_TAR":args.prior_tar,"PRIOR_IDENTITY":args.prior_identity,"PRIOR_MANIFEST":str(pathlib.Path(args.prior_tar).with_suffix('')/"MANIFEST.sha256")}
  for seed in range(40,45): amap[f"CHECKPOINT_{seed}"]=str(pathlib.Path(args.v1_root)/f"3b_ensemble/seed_{seed}/best_model.pth")
  by={i["key"]:i for i in items}
  if set(amap)!=set(by): fail("live_fixed_input","path map")
  for key,path in amap.items():
   p=pathlib.Path(path)
   if not p.is_file() or p.is_symlink() or p.stat().st_nlink!=1 or identity(p)!=(by[key]["expected_bytes"],by[key]["expected_sha256"]): fail("live_fixed_input",key)

def validate_inheritance(root,phase):
 x=strict_json(root/"evidence/inherited_m4a4b_file_identity.json"); rec=x.get("files",[])
 if len(rec)!=45 or x.get("prior_regular_file_count")!=45: fail("inheritance_identity","count")
 authorized={"scripts/validate_m4a4b_formal_gpu_benchmark.py","logs/validator_negative_tests.csv","logs/validator_negative_tests.stdout.txt","outputs/validator_results.json","MANIFEST.sha256"}
 preserved_map={"scripts/validate_m4a4b_formal_gpu_benchmark.py":"evidence/prior_validate_m4a4b_formal_gpu_benchmark.py","logs/validator_negative_tests.csv":"evidence/prior_validator_negative_tests.csv","logs/validator_negative_tests.stdout.txt":"evidence/prior_validator_negative_tests.stdout.txt","outputs/validator_results.json":"evidence/prior_validator_results.json"}
 for q in rec:
  rel=q.get("path")
  if rel not in PRIOR_FILES or q.get("classification") not in ("immutable","authorized_replacement") or (rel in authorized)!=(q.get("classification")=="authorized_replacement"): fail("inheritance_identity",rel)
  if rel in preserved_map:
   if identity(root/preserved_map[rel])!=(q["prior_bytes"],q["prior_sha256"]): fail("inheritance_identity","preserved:"+rel)
  elif rel not in authorized and identity(root/rel)!=(q["prior_bytes"],q["prior_sha256"]): fail("inheritance_identity","immutable:"+rel)
  if rel=="MANIFEST.sha256":
   if q.get("new_identity_location")!="EXTERNAL_IDENTITY_ONLY_DUE_TO_SELF_REFERENCE" or q.get("new_bytes") is not None or q.get("new_sha256") is not None: fail("manifest_self_reference","m4a4b ledger")
  elif not (phase=="evidence" and rel in RESULT_FILES):
   if identity(root/rel)!=(q["new_bytes"],q["new_sha256"]): fail("inheritance_identity","new:"+rel)

def validate_baa_inheritance(root,phase):
 x=strict_json(root/"evidence/inherited_m4a4ba_file_identity.json"); rec=x.get("files",[])
 if len(rec)!=57 or x.get("prior_regular_file_count")!=57 or len({q.get("path") for q in rec})!=57: fail("m4a4ba_inheritance_identity","count")
 replaced={"MANIFEST.sha256","evidence/inherited_m4a4b_file_identity.json","logs/status_fixture_tests.csv","logs/status_fixture_tests.stdout.txt","logs/validator_negative_tests.csv","logs/validator_negative_tests.stdout.txt","outputs/correction_provenance.json","outputs/validator_results.json","scripts/test_m4a4ba_status_fixtures.py","scripts/validate_m4a4b_formal_gpu_benchmark.py"}
 historical={
  "outputs/correction_provenance.json":"evidence/prior_m4a4ba_correction_provenance.json",
  "evidence/inherited_m4a4b_file_identity.json":"evidence/prior_m4a4ba_inherited_m4a4b_file_identity.json",
  "scripts/test_m4a4ba_status_fixtures.py":"evidence/prior_m4a4ba_status_fixture_runner.py",
  "outputs/validator_results.json":"evidence/prior_m4a4ba_validator_results.json"}
 if x.get("authorized_replacement_count")!=len(replaced) or x.get("immutable_count")!=47 or x.get("preserved_historical_copy_count")!=4: fail("m4a4ba_inheritance_identity","summary")
 for q in rec:
  rel=q.get("path"); expected="authorized_replacement" if rel in replaced else "immutable"
  if q.get("classification")!=expected or not isinstance(q.get("prior_bytes"),int) or not re.fullmatch(r"[0-9a-f]{64}",q.get("prior_sha256","") or ""): fail("m4a4ba_inheritance_identity",rel)
  if rel in historical and identity(root/historical[rel])!=(q["prior_bytes"],q["prior_sha256"]): fail("m4a4ba_inheritance_identity","historical:"+rel)
  if rel not in replaced and identity(root/rel)!=(q["prior_bytes"],q["prior_sha256"]): fail("m4a4ba_inheritance_identity","immutable:"+rel)
  if rel=="MANIFEST.sha256":
   if q.get("new_identity_location")!="EXTERNAL_IDENTITY_ONLY_DUE_TO_SELF_REFERENCE" or q.get("new_bytes") is not None or q.get("new_sha256") is not None: fail("manifest_self_reference","m4a4ba ledger")
  elif not (phase=="evidence" and rel in RESULT_FILES) and identity(root/rel)!=(q.get("new_bytes"),q.get("new_sha256")): fail("m4a4ba_inheritance_identity","new:"+rel)

def validate_baaa_inheritance(root,phase):
 x=strict_json(root/"evidence/inherited_m4a4baa_file_identity.json"); rec=x.get("files",[])
 replaced={"MANIFEST.sha256","scripts/validate_m4a4b_formal_gpu_benchmark.py","scripts/test_m4a4ba_status_fixtures.py","scripts/run_m4a4baa_validation_suite.py","logs/status_fixture_tests.csv","logs/status_fixture_tests.stdout.txt","logs/validator_negative_tests.csv","logs/validator_negative_tests.stdout.txt","logs/m4a4baa_validation_suite.csv","logs/m4a4baa_validation_suite.stdout.txt","outputs/correction_provenance.json","outputs/validator_results.json","evidence/inherited_m4a4ba_file_identity.json","evidence/inherited_m4a4b_file_identity.json"}
 historical={"scripts/validate_m4a4b_formal_gpu_benchmark.py":"evidence/prior_m4a4baa_validator.py","scripts/test_m4a4ba_status_fixtures.py":"evidence/prior_m4a4baa_fixture_runner.py","scripts/run_m4a4baa_validation_suite.py":"evidence/prior_m4a4baa_negative_runner.py","outputs/validator_results.json":"evidence/prior_m4a4baa_validator_results.json","outputs/correction_provenance.json":"evidence/prior_m4a4baa_correction_provenance.json"}
 if len(rec)!=66 or x.get("prior_regular_file_count")!=66 or len({q.get("path") for q in rec})!=66 or {q.get("path") for q in rec}!=set(BAA_READY_FILES): fail("m4a4baa_inheritance_identity","count_or_set")
 if x.get("immutable_count")!=52 or x.get("authorized_replacement_count")!=14 or x.get("preserved_historical_copy_count")!=5 or x.get("added_path_count")!=7: fail("m4a4baa_inheritance_identity","summary")
 for q in rec:
  rel=q.get("path"); expected="authorized_replacement" if rel in replaced else "immutable"
  if q.get("classification")!=expected or not isinstance(q.get("prior_bytes"),int) or not re.fullmatch(r"[0-9a-f]{64}",q.get("prior_sha256","") or ""): fail("m4a4baa_inheritance_identity",rel)
  if rel in historical and identity(root/historical[rel])!=(q["prior_bytes"],q["prior_sha256"]): fail("m4a4baa_inheritance_identity","historical:"+rel)
  if rel not in replaced and identity(root/rel)!=(q["prior_bytes"],q["prior_sha256"]): fail("m4a4baa_inheritance_identity","immutable:"+rel)
  if rel=="MANIFEST.sha256":
   if q.get("new_identity_location")!="EXTERNAL_IDENTITY_ONLY_DUE_TO_SELF_REFERENCE" or q.get("new_bytes") is not None or q.get("new_sha256") is not None: fail("manifest_self_reference","m4a4baa ledger")
  elif not (phase=="evidence" and rel in RESULT_FILES) and identity(root/rel)!=(q.get("new_bytes"),q.get("new_sha256")): fail("m4a4baa_inheritance_identity","new:"+rel)

def validate_baaaa_inheritance(root,phase):
 x=strict_json(root/"evidence/inherited_m4a4baaa_file_identity.json"); rec=x.get("files",[])
 replaced={"MANIFEST.sha256","scripts/validate_m4a4b_formal_gpu_benchmark.py","scripts/test_m4a4ba_status_fixtures.py","scripts/run_m4a4baa_validation_suite.py","logs/status_fixture_tests.csv","logs/status_fixture_tests.stdout.txt","logs/validator_negative_tests.csv","logs/validator_negative_tests.stdout.txt","logs/m4a4baa_validation_suite.csv","logs/m4a4baa_validation_suite.stdout.txt","outputs/correction_provenance.json","outputs/validator_results.json","evidence/inherited_m4a4baa_file_identity.json","evidence/inherited_m4a4ba_file_identity.json","evidence/inherited_m4a4b_file_identity.json"}
 historical={"scripts/validate_m4a4b_formal_gpu_benchmark.py":"evidence/prior_m4a4baaa_validator.py","scripts/test_m4a4ba_status_fixtures.py":"evidence/prior_m4a4baaa_fixture_runner.py","scripts/run_m4a4baa_validation_suite.py":"evidence/prior_m4a4baaa_negative_runner.py","outputs/validator_results.json":"evidence/prior_m4a4baaa_validator_results.json","outputs/correction_provenance.json":"evidence/prior_m4a4baaa_correction_provenance.json"}
 if len(rec)!=73 or x.get("prior_regular_file_count")!=73 or len({q.get("path") for q in rec})!=73 or {q.get("path") for q in rec}!=set(BAA_READY_FILES|BAAA_ADDED): fail("m4a4baaa_inheritance_identity","count_or_set")
 if x.get("immutable_count")!=58 or x.get("authorized_replacement_count")!=15 or x.get("preserved_historical_copy_count")!=5 or x.get("added_path_count")!=7: fail("m4a4baaa_inheritance_identity","summary")
 for q in rec:
  rel=q.get("path"); expected="authorized_replacement" if rel in replaced else "immutable"
  if q.get("classification")!=expected or not isinstance(q.get("prior_bytes"),int) or not re.fullmatch(r"[0-9a-f]{64}",q.get("prior_sha256","") or ""): fail("m4a4baaa_inheritance_identity",rel)
  if rel in historical and identity(root/historical[rel])!=(q["prior_bytes"],q["prior_sha256"]): fail("m4a4baaa_inheritance_identity","historical:"+rel)
  if rel not in replaced and identity(root/rel)!=(q["prior_bytes"],q["prior_sha256"]): fail("m4a4baaa_inheritance_identity","immutable:"+rel)
  if rel=="MANIFEST.sha256":
   if q.get("new_identity_location")!="EXTERNAL_IDENTITY_ONLY_DUE_TO_SELF_REFERENCE" or q.get("new_bytes") is not None or q.get("new_sha256") is not None: fail("manifest_self_reference","m4a4baaa ledger")
  elif not (phase=="evidence" and rel in RESULT_FILES) and identity(root/rel)!=(q.get("new_bytes"),q.get("new_sha256")): fail("m4a4baaa_inheritance_identity","new:"+rel)

def validate_request_calls(root):
 contract=strict_json(root/"inputs/formal_benchmark_contract.json"); request=contract.get("request",{}); uids=request.get("enzyme_pool_uids",[])
 if len(uids)!=100 or len(set(uids))!=100 or request.get("top_k")!=100 or request.get("return_ci") is not True: fail("request_integrity","shape")
 req_sha=hashlib.sha256(canonical(request)).hexdigest()
 if req_sha!=contract.get("request_canonical_sha256") or req_sha!="a46aa80fd0f00cf2cd177f39910971b5b746b744cc24748c8858e6f98b2173c4": fail("request_integrity","sha")
 evidence=hashlib.sha256((request["reaction_smiles"]+"\n"+"\n".join(sorted(uids))+"\n"+"v1_20260714").encode()).hexdigest()
 specs={"warmups":("warmup_calls.csv",5,1),"sequential":("sequential_100_calls.csv",100,1),"concurrency_2":("concurrency_2_100_calls.csv",100,2),"concurrency_4":("concurrency_4_100_calls.csv",100,4)}
 progress=strict_json(root/"outputs/benchmark_progress.json"); allrows={}; gids=set(); fixed_order=None
 for phase,(file,count,workers) in specs.items():
  rr=read_dict_csv(root/"evidence"/file,CALL_HEADER); allrows[phase]=rr
  if len(rr)!=count: fail("call_count",phase)
  expected_indices=set(range(1,count+1)); indices=set()
  barriers=set()
  for row in rr:
   if row["phase"]!=phase: fail("call_phase",phase)
   gid=row["global_request_id"]
   pattern=rf"{re.escape(phase)}-[0-9]{{3}}" if workers==1 else rf"{re.escape(phase)}-w[0-{workers-1}]-s[0-9]{{3}}"
   if not re.fullmatch(pattern,gid) or gid in gids: fail("global_call_id",gid)
   if not UTC_RE.fullmatch(row["start_utc"]) or not UTC_RE.fullmatch(row["end_utc"]): fail("call_utc",gid)
   gids.add(gid); idx=int(row["call_index"]); indices.add(idx)
   sn=int(row["start_ns"]); en=int(row["end_ns"])
   if sn>en or not math.isclose(finite(row["latency_ms"]),(en-sn)/1e6,rel_tol=0,abs_tol=1e-9): fail("call_timestamps",gid)
   if row["success"]!="true" or row["integrity_pass"]!="true" or row["exception_type"] or row["exception_message"] or row["integrity_failure_reason"] or int(row["returned_count"])!=100: fail("call_success_integrity",gid)
   if row["evidence_hash"]!=evidence: fail("row_evidence_hash",gid)
   if not re.fullmatch(r"[0-9a-f]{64}",row["response_sha256"]) or not re.fullmatch(r"[0-9a-f]{64}",row["uid_order_sha256"]): fail("response_hash",gid)
   fixed_order=fixed_order or row["uid_order_sha256"]
   if row["uid_order_sha256"]!=fixed_order: fail("uid_order_hash",gid)
   nonnegative(row["max_abs_score_difference_from_first_sequential"],"response_difference"); nonnegative(row["max_abs_ci_difference_from_first_sequential"],"response_difference")
   if workers>1:
    w=int(row["worker_id"]); seq=int(row["worker_sequence"]); barriers.add(int(row["barrier_release_ns"]))
    if w not in range(workers) or seq not in range(1,count//workers+1) or idx!=w*(count//workers)+seq: fail("call_index_or_worker_sequence",phase)
   elif row["worker_id"] or row["worker_sequence"] or row["barrier_release_ns"] or idx<1: fail("call_index_or_worker_sequence",phase)
  if indices!=expected_indices: fail("call_index_or_worker_sequence",phase)
  if workers>1 and len(barriers)!=1: fail("barrier_cardinality",phase)
  pr=progress.get("phases",{}).get(phase,{}); n,h=identity(root/"evidence"/file)
  if any(pr.get(k)!=v for k,v in {"bytes":n,"sha256":h,"durable_rows":count,"attempted":count,"success":count,"exception":0,"integrity_pass":count}.items()): fail("progress_cross_consistency",phase)
  first=strict_json(root/f"evidence/first_response_{phase}.json"); ranked=first.get("ranked_enzymes",[]); fu=[x.get("uid") for x in ranked]
  if len(ranked)!=100 or len(set(fu))!=100 or set(fu)!=set(uids): fail("first_response_uid_integrity",phase)
  if [x.get("rank") for x in ranked]!=list(range(1,101)): fail("first_response_rank",phase)
  for item in ranked:
   finite(item.get("score"),"first_response_score"); ci=item.get("ensemble_ci")
   if not isinstance(ci,list) or len(ci)!=2: fail("first_response_ci",phase)
   finite(ci[0],"first_response_ci"); finite(ci[1],"first_response_ci")
  if first.get("evidence_hash")!=evidence: fail("first_response_evidence_hash",phase)
  rh=hashlib.sha256(canonical(first)).hexdigest(); oh=hashlib.sha256(canonical(fu)).hexdigest(); matches=[x for x in rr if x["response_sha256"]==rh]
  if len(matches)!=1: fail("first_response_row_link",phase)
  if matches[0]["uid_order_sha256"]!=oh or oh!=fixed_order: fail("first_response_uid_order",phase)
 if len(gids)!=305 or progress.get("forward_call_count")!=305 or progress.get("initialize_call_count")!=2 or progress.get("checkpoint_load_count")!=1: fail("progress_cross_consistency","global")
 return allrows,evidence,fixed_order

def summary_values(rows):
 vals=[finite(r["latency_ms"]) for r in rows]; s=sorted(vals)
 return {"min_ms":s[0],"max_ms":s[-1],"mean_ms":sum(s)/100,"p50_ms":s[49],"p95_ms":s[94],"p99_ms":s[98]}
def validate_statistics(root,allrows):
 sums={}
 for phase in ("sequential","concurrency_2","concurrency_4"):
  out=strict_json(root/f"outputs/{phase}_summary.json"); exp=summary_values(allrows[phase]); sums[phase]=exp
  for k,v in exp.items():
   if not math.isclose(finite(out.get(k)),v,rel_tol=1e-14,abs_tol=1e-12): fail("statistics_recompute",phase+":"+k)
  start=int(out.get("phase_start_ns")); end=int(out.get("phase_end_ns")); elapsed=finite(out.get("elapsed_seconds"))
  if end<=start or not math.isclose(elapsed,(end-start)/1e9,rel_tol=0,abs_tol=1e-12) or start>min(int(r["start_ns"]) for r in allrows[phase]) or end<max(int(r["end_ns"]) for r in allrows[phase]): fail("phase_envelope",phase)
  if phase.startswith("concurrency"):
   if not math.isclose(finite(out.get("bounded_observed_throughput_per_second")),100/elapsed,rel_tol=1e-14): fail("throughput_recompute",phase)
 deg=strict_json(root/"outputs/latency_degradation.json")
 for phase in ("concurrency_2","concurrency_4"):
  for q in (50,95,99):
   v=sums[phase][f"p{q}_ms"]/sums["sequential"][f"p{q}_ms"]
   if not math.isclose(finite(deg[phase][f"p{q}_ratio"]),v,rel_tol=1e-14): fail("degradation_recompute",phase)
 text=(root/"M4A4B_FORMAL_GPU_BENCHMARK_REPORT.md").read_text().lower()
 if "production qps" in text and "not production qps" not in text: fail("unsupported_production_claim","report")

def validate_preload_source(root,evidence):
 pre=strict_json(root/"outputs/runtime_preload.json"); checks={40:"a95d4687e2cadad1c12f7c1defd21dbdf43db3cce96aa9caace39dbcc226586d",41:"c429a98bc265e20d415c3d6f479e0f0d6c47d81c13135c589e2a5e173978dbef",42:"cc54be33a23b78fb89c183f0bca6f87b442a5be4dad9666428d05a72a9b7f7a3",43:"3eb80be83cb41574204239c80f11008f728029dd9e4ba14c639749d8176b5220",44:"b9547d3ba17725a5910cf243d33af9367abb12b3215f4b526405f8bdb14acd16"}
 rows=pre.get("checkpoints",[])
 if len(rows)!=5 or {x.get("seed") for x in rows}!=set(checks) or any(x.get("bytes")!=72266498 or x.get("sha256")!=checks[x.get("seed")] for x in rows): fail("checkpoint_records","mismatch")
 if pre.get("initialize_call_count")!=2 or pre.get("checkpoint_load_count")!=1 or not pre.get("singleton_same_runtime") or not pre.get("singleton_same_five_models") or len(pre.get("model_object_ids",[]))!=5 or len(set(pre["model_object_ids"]))!=5 or pre.get("visible_device_count")!=1: fail("preload_identity","mismatch")
 ri=strict_json(root/"outputs/response_integrity.json")
 if not all((ri.get("all_305_calls_successful"),ri.get("all_response_integrity_pass"),ri.get("same_runtime_and_models_after_all_calls"))) or ri.get("forward_call_count_actual")!=305 or ri.get("fixed_evidence_hash")!=evidence or ri.get("request_canonical_sha256_before")!=ri.get("request_canonical_sha256_after"): fail("preload_identity","response")
 a=(root/"evidence/runtime_source_tree_before.sha256").read_text(); b=(root/"evidence/runtime_source_tree_after.sha256").read_text(); la=parse_ledger(a); lb=parse_ledger(b)
 if la!=lb or len(la)!=17: fail("source_ledger","before_after")
 si=strict_json(root/"outputs/runtime_source_identity.json")
 if si.get("code_root")!=CODE_ROOT or not si.get("source_tree_before_after_equal") or si.get("source_tree_py_file_count")!=17 or si.get("source_tree_before_sha256")!=hashlib.sha256(a.encode()).hexdigest() or si.get("source_tree_after_sha256")!=hashlib.sha256(b.encode()).hexdigest(): fail("source_identity","summary")
 core={"enzymecage/model.py":(14585,"005037a1d2c063bd7d71b8ff08ed4361c139ba37be3b822c87c8fa2d84890348"),"enzymecage/base.py":(2420,"abdfe7875a2b0c49032031dbc54915c435ed0bda895e0cce14c92be0be7421de"),"enzymecage/attention.py":(2196,"388db15eac48ac4c6251879b3b1be695bbe632ab1be3040e45df7cfaf2a3ca95"),"enzymecage/interaction.py":(4994,"1e03b0a4bcf5bf68019c9af4542bb673eb8f8f717427b652674ac88bc706ada3"),"enzymecage/dataset/geometric.py":(17852,"8415f772f2b4a723c6a2895d74db3b54b28b514c259a1424d2b1e83073657dfb"),"enzymecage/dataset/sharded_protein.py":(4629,"64ba8a97280fc1b4b7112139ada0487758c4f848ebb15981abf8eba098054811")}
 if {(x["relative_path"]):(x["bytes"],x["sha256"]) for x in si.get("accepted_core_sources",[])}!=core or any(la.get(k,(None,))[1:]!=v for k,v in core.items()): fail("source_identity","core")
 return la

def validate_memory(root):
 rr=read_dict_csv(root/"evidence/nvidia_smi_memory_samples.csv",MEM_HEADER,"memory_header")
 if len(rr)!=6917: fail("memory_row_count",len(rr))
 ns=[]; uuids=set(); indices=set(); pids=set(); phases=[]
 allowed_process={"0","not_present"}
 for row in rr:
  n=int(row["monotonic_ns"]); ns.append(n); uuids.add(row["gpu_uuid"]); indices.add(row["gpu_index"]); pids.add(row["benchmark_pid"]); phases.append(row["phase"])
  nonnegative(row["device_used_mib"],"memory_numeric"); nonnegative(row["device_free_mib"],"memory_numeric"); nonnegative(row["utilization_percent"],"memory_numeric")
  if row["process_used_mib"]: nonnegative(row["process_used_mib"],"memory_numeric")
  if row["device_query_status"]!="0" or row["process_query_status"] not in allowed_process: fail("memory_query_status",row["process_query_status"])
 if any(b<=a for a,b in zip(ns,ns[1:])) or len(uuids)!=1 or len(indices)!=1 or len(pids)!=1: fail("memory_chronology_identity","mismatch")
 expected_order=["baseline","preload","warmups","sequential","concurrency_2","concurrency_4","final"]
 compressed=[]
 for x in phases:
  if not compressed or compressed[-1]!=x: compressed.append(x)
 if compressed!=expected_order: fail("memory_phase_coverage",compressed)
 out=strict_json(root/"outputs/memory_summary.json")
 if set(out.get("phases",{}))!=set(expected_order) or out.get("sampling_interval_target_ms")!=150 or not out.get("sampler_started_before_torch_import"): fail("memory_phase_coverage","summary")
 for phase in expected_order:
  sub=[x for x in rr if x["phase"]==phase]; s=out["phases"][phase]; dv=[float(x["device_used_mib"]) for x in sub]; pv=[float(x["process_used_mib"]) for x in sub if x["process_used_mib"]]
  if s.get("row_count")!=len(sub) or s.get("device_peak_used_mib")!=max(dv) or s.get("process_peak_used_mib")!=(max(pv) if pv else None): fail("memory_peak_recompute",phase)
  keys=("torch_peak_allocated_mib","torch_peak_reserved_mib","torch_end_allocated_mib","torch_end_reserved_mib")
  vals={k:nonnegative(s.get(k),"torch_memory_structure") for k in keys}
  if vals["torch_peak_allocated_mib"]<vals["torch_end_allocated_mib"] or vals["torch_peak_reserved_mib"]<vals["torch_end_reserved_mib"] or vals["torch_peak_reserved_mib"]<vals["torch_peak_allocated_mib"] or vals["torch_end_reserved_mib"]<vals["torch_end_allocated_mib"]: fail("torch_memory_structure",phase)
 c=strict_json(root/"outputs/memory_evidence_classification.json")
 required={"device_process_rows_and_peaks":"raw_and_independently_recomputable","torch_phase_boundary_values":"captured_only_and_structurally_validated","simultaneous_additional_local_adrmats_model":"measured_none_present","raw_memory_row_count":6917}
 if any(c.get(k)!=v for k,v in required.items()): fail("memory_classification","mismatch")

def validate_pyg(root,ledger):
 inv=strict_json(root/"evidence/imported_enzymecage_modules.json"); gp=strict_json(root/"evidence/generated_module_provenance.json")
 if len(inv)!=12 or len({x.get("module") for x in inv})!=12: fail("pyg_inventory","count")
 by={x["module"]:x for x in inv}; statics=[x for x in inv if x.get("classification")=="ACCEPTED_STATIC_ENZYMECAGE_MODULE"]; generated=[x for x in inv if x.get("classification")=="PYG_GENERATED_MESSAGE_PASSING_HELPER"]
 if len(statics)!=10 or len(generated)!=2 or any(x.get("classification") not in ("ACCEPTED_STATIC_ENZYMECAGE_MODULE","PYG_GENERATED_MESSAGE_PASSING_HELPER") for x in inv) or gp.get("rejected_or_unknown_modules")!=[]: fail("pyg_inventory","classification")
 for x in statics:
  rp=pathlib.PurePosixPath(x.get("realpath",""));
  try: rel=rp.relative_to(CODE_ROOT).as_posix()
  except ValueError: fail("static_module_crosscheck",x["module"])
  if x.get("file")!=x.get("realpath") or x.get("spec_origin")!=x.get("realpath") or x.get("bytes")!=ledger.get(rel,(None,None,None))[1] or x.get("sha256")!=ledger.get(rel,(None,None,None))[2] or x.get("loader_class")!="SourceFileLoader" or x.get("spec_loader_class")!="SourceFileLoader" or not x.get("regular_file") or x.get("hardlink_count")!=1 or x.get("symlink") is not False: fail("static_module_crosscheck",x["module"])
 if sorted(gp.get("accepted_static_modules",[]))!=sorted(x["module"] for x in statics): fail("static_module_crosscheck","list")
 if gp.get("torch_geometric_version")!="2.8.0" or gp.get("torch_geometric_package_root")!=PYG_PREFIX or gp.get("untrusted_sys_path_insertion_detected") is not False: fail("pyg_environment","root/version")
 sources=[gp.get("message_passing_source",{})]+gp.get("template_generator_sources",[]); paths=[]
 for x in sources:
  path=pathlib.PurePosixPath(x.get("path",""));
  try: path.relative_to(PYG_PREFIX)
  except ValueError: fail("pyg_generator_source","outside root")
  if x.get("bytes",-1)<1 or not re.fullmatch(r"[0-9a-f]{64}",x.get("sha256","") or ""): fail("pyg_generator_source","identity")
  paths.append(str(path))
 authority={PYG_PREFIX+"/nn/conv/message_passing.py":(44377,"66e4ef4afa1d1b2d46c805b8987b6ea0c52ec5c95a9beee8a62758358e481e6f"),PYG_PREFIX+"/nn/conv/collect.jinja":(5752,"7a42629d53c35e2b20e149cfee360e8bdc946ea85feff31c80f8209e4eaacd42"),PYG_PREFIX+"/nn/conv/propagate.jinja":(7374,"b0c6eb39a67bfe917c4d11217e359fdee279cd839a00d95c64d1c79ec69b87ed"),PYG_PREFIX+"/template.py":(1060,"aea8c35a07120204c2895e1b90e8d644f68ee0fa54742fd15e2833c7106a02ef")}
 observed={(x["path"]):(x["bytes"],x["sha256"]) for x in sources}
 if observed!=authority or paths.count(PYG_PREFIX+"/nn/conv/message_passing.py")!=2 or len(set(paths))!=len(paths)-1: fail("pyg_generator_source","authority")
 helpers=gp.get("generated_helpers",[])
 if len(helpers)!=2 or {x.get("module") for x in helpers}!={x["module"] for x in generated}: fail("pyg_helper","set")
 for g in helpers:
  module=g.get("module"); owner=g.get("owner",{}); expected_module=owner.get("class_module")+"_"+owner.get("class_name")+"_"+owner.get("method_name")
  if module!=expected_module or owner.get("method_module")!=module or owner.get("method_name")!="propagate" or "torch_geometric.nn.conv.message_passing.MessagePassing" not in owner.get("mro",[]): fail("pyg_live_linkage_cross_consistency",module)
  rp=pathlib.PurePosixPath(g.get("realpath","")); pattern=r"/tmp/"+re.escape(module)+r"_[A-Za-z0-9]+\.py"
  if not re.fullmatch(pattern,str(rp)) or ".." in rp.parts or pathlib.PurePosixPath(g.get("spec_origin","")).as_posix()!=rp.as_posix() or g.get("loader_class")!="SourceFileLoader" or g.get("spec_loader_class")!="SourceFileLoader" or g.get("package")!=module.rpartition('.')[0]: fail("pyg_helper_path_spec",module)
  try: data=base64.b64decode(g.get("source_base64",""),validate=True)
  except Exception: fail("pyg_generated_hash",module)
  if len(data)!=g.get("bytes") or hashlib.sha256(data).hexdigest()!=g.get("sha256"): fail("pyg_generated_hash",module)
  try: text=data.decode("utf-8")
  except UnicodeDecodeError: fail("pyg_generated_hash","utf8")
  if not re.search(r"from\s+"+re.escape(owner.get("class_module"))+r"\s+import\s+\*",text): fail("pyg_owner_import",module)
  rel=owner.get("parent_relative_path"); expected_path=CODE_ROOT+"/"+rel
  if owner.get("parent_path")!=expected_path or rel not in ledger or ledger[rel][1:]!=(owner.get("parent_bytes"),owner.get("parent_sha256")): fail("pyg_owner_parent",module)
  ix=by[module]
  if ix.get("realpath")!=str(rp) or ix.get("spec_origin")!=str(rp) or ix.get("bytes")!=g.get("bytes") or ix.get("sha256")!=g.get("sha256") or ix.get("loader_class")!="SourceFileLoader" or ix.get("spec_loader_class")!="SourceFileLoader": fail("pyg_inventory_helper_crosscheck",module)
  checks=g.get("checks",{})
  if set(checks)!={"generated_dir_absent_from_sys_path","live_class_method_module_exact","module_spec_name_exact","module_spec_origin_realpath_exact","owning_parent_below_code_root","owning_parent_unchanged_contract","package_agrees","regular_single_link_temporary_python_source"} or not all(checks.values()): fail("pyg_live_linkage_cross_consistency",module)

def validate_warnings(root):
 out=root/"logs/benchmark.stdout.txt"; err=root/"logs/benchmark.stderr.txt"; text=err.read_text(encoding="utf-8")
 if text.count("Mean of empty slice")!=1525 or text.count("invalid value encountered in scalar divide")!=1513: fail("warning_counts","mismatch")
 if any(x.lower() in text.lower() for x in ("Traceback","CUDA out of memory","prediction exception")): fail("fatal_stream_content","stderr")
 if (root/"logs/benchmark.exit_code.txt").read_text().strip()!="0": fail("benchmark_exit","nonzero")
 cp=strict_json(root/"outputs/correction_provenance.json")
 streams=cp.get("benchmark_streams",{})
 for key,p in (("stdout",out),("stderr",err)):
  n,h=identity(p)
  if streams.get(key)!={"bytes":n,"sha256":h}: fail("stream_identity",key)
 w=cp.get("warning_classification",{})
 if w.get("mean_of_empty_slice")!=1525 or w.get("invalid_scalar_divide")!=1513 or w.get("classification")!="metric_only_auc_warnings_all_zero_synthetic_labels" or w.get("warning_free") is not False: fail("warning_counts","classification")

def validate_correction_report(root):
 text=(root/"M4A4BAAAA_CORRECTION_REPORT.md").read_text(encoding="utf-8")
 expected="# M4a-4BAAAA Adversarial Status And Transcript Semantics Final Correction\n\nNo GPU benchmark rerun was performed. Scientific benchmark bytes are inherited unchanged from M4a-4B through M4a-4BAAA.\n\nClosed local bypasses: A01 incomplete blocker type/row mismatch, A02 inside-root provenance rejection, A03 contradictory GPU threshold message, A04 contradictory packaged transcript line, A05 malformed READY call UTC.\n\nMACHINE_CHECKABLE_BOUNDARIES_BEGIN\n"+REPORT_BOUNDARY_BLOCK+"\nfive local bypasses closed = true\nnew adversarial regressions = 5/5 REJECTED\nMACHINE_CHECKABLE_BOUNDARIES_END\n\nCoexistence remains open. M4b/M4c remain unauthorized. Teacher decisions remain pending. Independent local audit remains the next gate; this correction does not claim formal M4a closure.\n"
 if text!=expected: fail("correction_report_semantics","exact report")

def validate_correction_provenance(root):
 cp=strict_json(root/"outputs/correction_provenance.json")
 keys={"added_path_count","authorized_replacement_count","benchmark_streams","captured_evidence_validation","captured_packaged_validation","checkpoint_loaded","coexistence","coexistence_pass","correction_stage","cross_consistent_negative_tests","dependency_changed","deterministic_tar_reconstruction","formal_m4a_closure","gpu_queried_or_used","immutable_path_count","m4b_authorized","m4c_authorized","model_modified_or_trained","network_api_called","new_adversarial_regressions","positive_status_fixtures","prediction_executed","preserved_historical_copy_count","prior_identity_bytes","prior_identity_sha256","prior_manifest_bytes","prior_manifest_sha256","prior_tar_bytes","prior_tar_sha256","reverse_negative_tests","reverse_packaged_validation","reverse_positive_status_fixtures","source_or_overlay_modified","source_tree_unchanged_by_test_runners","teacher_pending","test_evidence_identities","torch_imported","warning_classification"}
 if set(cp)!=keys: fail("correction_provenance_schema","keys")
 pending=["abc_complete_comparison","snapshot_review","maintainer_inquiry_unsent","strain_species_policy","final_checkpoint_strategy","zero_additional_local_model_coexistence_interpretation","m4a_full_closure"]
 finals={"deterministic_tar_reconstruction":"PASS_FINAL","reverse_packaged_validation":"PASS_FINAL","reverse_positive_status_fixtures":"6/6_PASS_FINAL","reverse_negative_tests":"ALL_PASS_FINAL","source_tree_unchanged_by_test_runners":"PASS_FINAL"}
 if any(cp.get(k)!=v for k,v in finals.items()): fail("final_reverse_provenance","correction provenance")
 expected={"correction_stage":"M4a-4BAAAA","prior_tar_bytes":2201600,"prior_tar_sha256":"afa7bbfbc69cbf93181a6162a68c88e7e48a96180df67c62b4e1df3e3e680da2","prior_identity_bytes":3057,"prior_identity_sha256":"236aa7c825fe20e5cf380a895f00db6da0af14f5c476adafa635a5a920fae2d0","prior_manifest_bytes":7433,"prior_manifest_sha256":"a7a71fd421a2d1f5e63ce3f7bae20b768e05ca005fd2e86b5efd7d5e3f962f40","immutable_path_count":58,"authorized_replacement_count":15,"preserved_historical_copy_count":5,"added_path_count":7,"network_api_called":False,"dependency_changed":False,"source_or_overlay_modified":False,"model_modified_or_trained":False,"gpu_queried_or_used":False,"torch_imported":False,"checkpoint_loaded":False,"prediction_executed":False,"m4b_authorized":False,"m4c_authorized":False,"formal_m4a_closure":False,"coexistence":"OPEN/NOT_ESTABLISHED","coexistence_pass":False,"teacher_pending":pending,"captured_evidence_validation":"PASS","positive_status_fixtures":"6/6_PASS","cross_consistent_negative_tests":"73/73_PASS","new_adversarial_regressions":"5/5_REJECTED",**finals}
 if any(cp.get(k)!=v for k,v in expected.items()): fail("correction_provenance_schema","value")
 command=cp.get("captured_packaged_validation")
 if set(command or {})!={"exit_code","stderr_bytes","token_count"} or command!={"exit_code":0,"stderr_bytes":0,"token_count":1}: fail("correction_provenance_schema","captured command")
 return cp

def validate_validator_results(root):
 vr=strict_json(root/"outputs/validator_results.json")
 keys={"actual_status_positive","actual_status_token","captured_evidence_validation","captured_packaged_validation","coexistence","coexistence_pass","cross_consistent_negative_tests","deterministic_tar_reconstruction","formal_m4a_closure","gpu_queried_or_used","m4b_authorized","m4c_authorized","model_modified_or_trained","negative_tests_skipped","new_adversarial_regressions","positive_status_fixtures","prediction_executed","reverse_negative_tests","reverse_packaged_validation","reverse_positive_status_fixtures","source_tree_unchanged_by_test_runners","teacher_pending","test_evidence_identities","torch_imported","validator_status_dispatch"}
 if set(vr)!=keys: fail("validator_results_schema","keys")
 pending=["abc_complete_comparison","snapshot_review","maintainer_inquiry_unsent","strain_species_policy","final_checkpoint_strategy","zero_additional_local_model_coexistence_interpretation","m4a_full_closure"]
 finals={"deterministic_tar_reconstruction":"PASS_FINAL","reverse_packaged_validation":"PASS_FINAL","reverse_positive_status_fixtures":"6/6_PASS_FINAL","reverse_negative_tests":"ALL_PASS_FINAL","source_tree_unchanged_by_test_runners":"PASS_FINAL"}
 if any(vr.get(k)!=v for k,v in finals.items()): fail("final_reverse_provenance","validator results")
 expected={"actual_status_positive":"PASS","actual_status_token":READY,"captured_evidence_validation":"PASS","captured_packaged_validation":"PASS","coexistence":"OPEN/NOT_ESTABLISHED","coexistence_pass":False,"m4b_authorized":False,"m4c_authorized":False,"formal_m4a_closure":False,"gpu_queried_or_used":False,"torch_imported":False,"model_modified_or_trained":False,"prediction_executed":False,"teacher_pending":pending,"validator_status_dispatch":True,"positive_status_fixtures":"6/6_PASS","cross_consistent_negative_tests":"73/73_PASS","new_adversarial_regressions":"5/5_REJECTED","negative_tests_skipped":[],**finals}
 if any(vr.get(k)!=v for k,v in expected.items()): fail("validator_results_schema","value")
 return vr

def parse_positive_transcript(text,rows):
 lines=text.splitlines()
 if len(lines)<3 or not lines[0].startswith("source_tree_before=") or not lines[1].startswith("source_tree_after=") or lines[-1]!="summary=6/6_PASS": fail("transcript_cross_consistency","positive envelope")
 if any(re.search(r"(M4A4BA_VALIDATION_ERROR|Traceback|CONTRADICTORY)",line) for line in lines): fail("transcript_cross_consistency","positive forbidden line")
 try: before=json.loads(lines[0].split("=",1)[1]); after=json.loads(lines[1].split("=",1)[1])
 except json.JSONDecodeError: fail("transcript_cross_consistency","positive tree json")
 if before!=after or set(before)!={"entry_count","sha256"} or not isinstance(before["entry_count"],int) or not re.fullmatch(r"[0-9a-f]{64}",before["sha256"]): fail("transcript_cross_consistency","positive tree")
 pattern=re.compile(r"(F[0-9]{2})\tstatus=([^\t]+)\texit=([^\t]+)\tstderr_empty=([^\t]+)\ttoken_count=([^\t]+)\tdefining_condition=([^\t]+)\tresult=([^\t]+)")
 body=lines[2:-1]
 if len(body)!=4*len(rows): fail("transcript_cross_consistency","positive block count")
 for n,row in enumerate(rows):
  block=body[n*4:n*4+4]; m=pattern.fullmatch(block[0])
  if not m or dict(zip(("fixture_id","status","exit_code","stderr_empty","token_count","defining_condition","result"),m.groups()))!=row: fail("transcript_cross_consistency",row.get("fixture_id"))
  if block[1]!="validation_phase=evidence" or block[2]!="runtime_evidence_mode=captured" or block[3]!=row["status"]: fail("transcript_cross_consistency",row.get("fixture_id"))

def parse_negative_transcript(text,rows):
 lines=text.splitlines()
 if len(lines)<3 or not lines[0].startswith("source_tree_before=") or not lines[1].startswith("source_tree_after=") or lines[-1]!="summary=%d/%d_PASS"%(len(rows),len(rows)): fail("transcript_cross_consistency","negative envelope")
 try: before=json.loads(lines[0].split("=",1)[1]); after=json.loads(lines[1].split("=",1)[1])
 except json.JSONDecodeError: fail("transcript_cross_consistency","negative tree json")
 if before!=after or set(before)!={"entry_count","sha256"} or not re.fullmatch(r"[0-9a-f]{64}",before.get("sha256","") or ""): fail("transcript_cross_consistency","negative tree")
 pattern=re.compile(r"(N[0-9]{2})\tmutation=([^\t]+)\texit=([^\t]+)\texpected=([^\t]+)\tobserved=([^\t]+)\tstderr_empty=([^\t]+)\tdependencies_updated=([^\t]+)\tresult=([^\t]+)")
 keys=("test_id","mutation","exit_code","expected_reason","observed_reason","stderr_empty","dependencies_updated","result")
 body=lines[2:-1]
 if len(body)!=2*len(rows): fail("transcript_cross_consistency","negative block count")
 for n,row in enumerate(rows):
  block=body[n*2:n*2+2]; m=pattern.fullmatch(block[0])
  if not m or dict(zip(keys,m.groups()))!=row: fail("transcript_cross_consistency",row.get("test_id"))
  if not (block[1].startswith("M4A4BA_VALIDATION_ERROR:"+row["observed_reason"]+":") or block[1]=="M4A4BA_VALIDATION_ERROR:"+row["observed_reason"]): fail("transcript_cross_consistency","reason:"+row["test_id"])

def validate_ready(root,args):
 p=validate_common(root,READY)
 if p.get("first_blocker") is not None: fail("ready_has_blocker","provenance")
 validate_fixed_ledger(root,args); rows,evidence,_=validate_request_calls(root); validate_statistics(root,rows); ledger=validate_preload_source(root,evidence); validate_memory(root); validate_pyg(root,ledger); validate_warnings(root); validate_inheritance(root,args.validation_phase); validate_baa_inheritance(root,args.validation_phase); validate_baaa_inheritance(root,args.validation_phase); validate_baaaa_inheritance(root,args.validation_phase); cp=validate_correction_provenance(root); validate_correction_report(root)
 if args.validation_phase=="packaged":
  with (root/"logs/status_fixture_tests.csv").open(newline="",encoding="utf-8") as f: rd=csv.DictReader(f,strict=True); pos=list(rd); pf=rd.fieldnames
  if pf!=["fixture_id","status","exit_code","stderr_empty","token_count","defining_condition","result"]: fail("positive_fixture_evidence","header")
  if [x.get("fixture_id") for x in pos]!=list(POSITIVE_IDS) or [x.get("status") for x in pos]!=list(STATUSES): fail("test_id_set","positive")
  if any(x.get("exit_code")!="0" or x.get("stderr_empty")!="true" or x.get("token_count")!="1" or x.get("defining_condition")!="PASS" or x.get("result")!="PASS" for x in pos): fail("positive_fixture_evidence","rows")
  ptxt=(root/"logs/status_fixture_tests.stdout.txt").read_text(encoding="utf-8")
  parse_positive_transcript(ptxt,pos)
  if (root/"logs/validator_negative_tests.csv").read_bytes()!=(root/"logs/m4a4baa_validation_suite.csv").read_bytes() or (root/"logs/validator_negative_tests.stdout.txt").read_bytes()!=(root/"logs/m4a4baa_validation_suite.stdout.txt").read_bytes(): fail("duplicate_suite_evidence_mismatch","negative copies")
  with (root/"logs/validator_negative_tests.csv").open(newline="",encoding="utf-8") as f: rd=csv.DictReader(f,strict=True); neg=list(rd); nf=rd.fieldnames
  if nf!=["test_id","mutation","expected_reason","exit_code","observed_reason","stderr_empty","dependencies_updated","result"]: fail("negative_suite_evidence","header")
  expected=[{"test_id":i,"mutation":m,"expected_reason":r} for i,m,r in NEGATIVE_CASES]
  if [x.get("test_id") for x in neg]!=[x["test_id"] for x in expected]: fail("test_id_set","negative")
  for row,exp in zip(neg,expected):
   if any(row.get(k)!=v for k,v in exp.items()) or row.get("exit_code")!="1" or row.get("observed_reason")!=exp["expected_reason"] or row.get("stderr_empty")!="true" or row.get("dependencies_updated")!="true" or row.get("result")!="PASS": fail("negative_suite_evidence",row.get("test_id"))
  ntxt=(root/"logs/validator_negative_tests.stdout.txt").read_text(encoding="utf-8")
  parse_negative_transcript(ntxt,neg)
  vr=validate_validator_results(root)
  for rel,key in (("logs/status_fixture_tests.csv","positive_csv"),("logs/status_fixture_tests.stdout.txt","positive_stdout"),("logs/validator_negative_tests.csv","negative_csv"),("logs/validator_negative_tests.stdout.txt","negative_stdout")):
   n,h=identity(root/rel); expected_identity={"bytes":n,"sha256":h}
   if vr.get("test_evidence_identities",{}).get(key)!=expected_identity or cp.get("test_evidence_identities",{}).get(key)!=expected_identity: fail("validator_test_results_identity",key)

def validate_incomplete(root,args):
 p=validate_common(root,INCOMPLETE); progress=strict_json(root/"outputs/benchmark_progress.json"); by,total,successes,failures,failed_phases=validate_partial_call_rows(root,progress)
 contract={"warmups":5,"sequential":100,"concurrency_2":100,"concurrency_4":100}; incomplete={phase for phase,rows in by.items() if len(rows)<contract[phase]}
 if failures==0 and not incomplete: fail("incomplete_defining_failure","absent")
 b=p.get("first_blocker"); codes={"PredictionFailure":"PREDICTION_FAILURE","IntegrityFailure":"INTEGRITY_FAILURE","ConcurrencyFailure":"CONCURRENCY_FAILURE"}
 if not isinstance(b,dict) or set(b)!={"type","stage","message","code"} or b.get("type") not in codes or b.get("code")!=codes[b["type"]] or b.get("stage") not in contract or not str(b.get("message","")).strip(): fail("incomplete_blocker_schema","mismatch")
 if str(b.get("message","")).strip().lower() in {"generic","failure","failed","error","fixture"}: fail("incomplete_blocker_schema","generic message")
 if progress.get("first_blocker")!=b: fail("blocker_cross_consistency","incomplete")
 if b["stage"] not in failed_phases|incomplete: fail("incomplete_blocker_evidence","stage")
 if b["type"]=="IntegrityFailure" and not any(x["success"]=="false" and (x["integrity_failure_reason"] or "integrity" in x["exception_type"].lower()) for x in by[b["stage"]]): fail("incomplete_blocker_evidence","integrity")
 if b["type"]=="PredictionFailure":
  def prediction_evidence(row):
   text=(row["exception_type"]+" "+row["exception_message"]).lower()
   return row["success"]=="false" and any(term in text for term in ("prediction","model","runtime","forward","cuda","out of memory","oom")) and not (row["integrity_failure_reason"] or ("integrity" in text and not any(term in text for term in ("prediction","model","runtime","forward"))))
  if not any(prediction_evidence(x) for x in by[b["stage"]]): fail("incomplete_blocker_evidence","prediction")
 if b["type"]=="ConcurrencyFailure":
  if b["stage"] in incomplete: return
  def concurrency_evidence(row):
   text=(row["exception_type"]+" "+row["exception_message"]).lower()
   return row["success"]=="false" and any(term in text for term in ("concurrency","barrier","worker","thread","process","deadlock","timeout"))
  if not any(concurrency_evidence(x) for x in by[b["stage"]]): fail("incomplete_blocker_evidence","concurrency")
def validate_blocked_gpu(root,args):
 p=validate_common(root,BLOCKED_GPU); g=strict_json(root/"outputs/gpu_selection_or_block.json"); ps=strict_json(root/"evidence/benchmark_process_start.json"); progress=strict_json(root/"outputs/benchmark_progress.json"); rr=read_dict_csv(root/"evidence/gpu_gate_samples.csv",GPU_HEADER); b=p.get("first_blocker")
 if g.get("gate")!="BLOCKED" or g.get("blocker")!=b or progress.get("first_blocker")!=b or not rr: fail("gpu_blocker_cross_consistency","mismatch")
 if not isinstance(b,dict) or set(b)!={"type","stage","message","code","observed_min_free_mib","minimum_free_mib"} or b.get("type")!="ImmediateGpuGateBlocker" or b.get("stage")!="immediate_gpu_gate" or b.get("code")!="GPU_FREE_MEMORY_BELOW_THRESHOLD" or not str(b.get("message","")).strip(): fail("gpu_blocker_schema","mismatch")
 msg=str(b.get("message","")).lower()
 if any(term in msg for term in ("above threshold","enough to launch","safe to launch","sufficient memory","can launch")): fail("gpu_blocker_semantics","contradictory message")
 if b.get("message")!="observed free memory below required threshold": fail("gpu_blocker_schema","message")
 observed=[]; previous=0
 for index,row in enumerate(rr,1):
  try:
   if row["sample"]!=str(index) or not GPU_UTC_RE.fullmatch(row["utc_timestamp"]) or not re.fullmatch(r"[1-9][0-9]*",row["monotonic_ns"]): fail("gpu_sample_semantics","index/time")
   mono=int(row["monotonic_ns"])
   if mono<=previous: fail("gpu_sample_semantics","monotonic")
   previous=mono
   if not re.fullmatch(r"[0-9]+",row["gpu_index"]) or not row["gpu_uuid"].strip() or not row["name"].strip() or not row["driver"].strip() or not row["compute_mode"].strip(): fail("gpu_sample_semantics","identity")
   total=nonnegative(row["total_mib"],"gpu_sample_semantics"); used=nonnegative(row["used_mib"],"gpu_sample_semantics"); free=nonnegative(row["free_mib"],"gpu_sample_semantics")
   if not math.isclose(used+free,total,rel_tol=0,abs_tol=1.0): fail("gpu_sample_semantics","memory sum")
   util=finite(row["utilization_percent"],"gpu_sample_semantics")
   if not 0<=util<=100 or not re.fullmatch(r"[0-9]+",row["compute_process_count"]): fail("gpu_sample_semantics","util/process count")
   count=int(row["compute_process_count"]); procs=json.loads(row["compute_process_rows_json"])
   if not isinstance(procs,list) or len(procs)!=count: fail("gpu_sample_semantics","process list")
   for proc in procs:
    if not isinstance(proc,dict) or set(proc)!={"pid","name","used_memory_mib"} or not isinstance(proc["pid"],int) or proc["pid"]<=0 or not isinstance(proc["name"],str) or not proc["name"].strip() or nonnegative(proc["used_memory_mib"],"gpu_sample_semantics")<0: fail("gpu_sample_semantics","process row")
   observed.append(free)
  except (ValueError,TypeError,json.JSONDecodeError): fail("gpu_sample_semantics","field")
 threshold=finite(g.get("minimum_free_mib"),"gpu_threshold")
 if threshold<=0: fail("gpu_threshold","nonpositive")
 if min(observed)>=threshold or g.get("observed_min_free_mib")!=min(observed) or b.get("observed_min_free_mib")!=g.get("observed_min_free_mib") or b.get("minimum_free_mib")!=g.get("minimum_free_mib"): fail("gpu_blocker_semantics","threshold")
 required={"launched":False,"torch_imported":False,"model_initialized":False,"checkpoint_loaded":False,"prediction_executed":False,"call_count":0}
 if any(ps.get(k)!=v for k,v in required.items()) or any(progress.get(k)!=v for k,v in {"initialize_call_count":0,"checkpoint_load_count":0,"forward_call_count":0,"attempted_call_count":0}.items()): fail("gpu_no_launch_proof","mismatch")
def validate_blocked_runtime(root,args):
 p=validate_common(root,BLOCKED_RUNTIME); progress=strict_json(root/"outputs/benchmark_progress.json"); b=p.get("first_blocker")
 if not isinstance(b,dict) or b.get("type")!="RuntimeEnvironmentBlocker" or not b.get("message") or not str(b.get("traceback","")).startswith("Traceback") or progress.get("first_blocker")!=b: fail("runtime_blocker_semantics","mismatch")
 if (progress.get("initialize_call_count"),progress.get("checkpoint_load_count"),progress.get("forward_call_count"))!=(1,0,0): fail("runtime_progress_counts","mismatch")
 for phase,file in (("warmups","warmup_calls.csv"),("sequential","sequential_100_calls.csv"),("concurrency_2","concurrency_2_100_calls.csv"),("concurrency_4","concurrency_4_100_calls.csv")):
  rr=read_dict_csv(root/"evidence"/file,CALL_HEADER)
  if rr or progress.get("phases",{}).get(phase)!={"attempted":0,"success":0,"failure":0,"summary_present":False,"file":{"path":"evidence/"+file,"bytes":identity(root/"evidence"/file)[0],"sha256":identity(root/"evidence"/file)[1]}}: fail("runtime_reached_artifacts",phase)
def validate_blocked_provenance(root,args):
 p=validate_common(root,BLOCKED_PROVENANCE); b=p.get("first_blocker"); progress=strict_json(root/"outputs/benchmark_progress.json"); a=parse_ledger((root/"evidence/runtime_source_tree_before.sha256").read_text()); z=parse_ledger((root/"evidence/runtime_source_tree_after.sha256").read_text()); inv=strict_json(root/"evidence/imported_enzymecage_modules.json"); gp=strict_json(root/"evidence/generated_module_provenance.json")
 rejected=[x for x in inv if x.get("classification")=="REJECTED_OR_UNKNOWN"]
 if not isinstance(b,dict) or set(b)!={"type","stage","message","code","rejected_modules"} or b.get("type")!="RuntimeProvenanceBlock" or b.get("stage")!="post_evidence_runtime_provenance" or b.get("code")!="REJECTED_OUTSIDE_ROOT_MODULE" or not b.get("message"): fail("provenance_blocker_semantics","blocker schema")
 outside=[]
 for item in rejected:
  rp=pathlib.PurePosixPath(item.get("realpath","") or "")
  if not rp.is_absolute() or ".." in rp.parts or str(rp)!=item.get("realpath"): fail("provenance_rejected_path","unsafe")
  inside=False
  for accepted in (pathlib.PurePosixPath(CODE_ROOT),pathlib.PurePosixPath(PYG_PREFIX),pathlib.PurePosixPath("/tmp")):
   try: rp.relative_to(accepted); inside=True
   except ValueError: pass
  if inside: fail("provenance_blocker_semantics","inside rejected module")
  outside.append(item)
 if not rejected or len(outside)!=len(rejected): fail("provenance_blocker_semantics","no outside rejected module")
 if progress.get("first_blocker")!=b: fail("provenance_blocker_semantics","cross consistency")
 names=[x.get("module") for x in rejected]
 if names!=b.get("rejected_modules") or gp.get("rejected_or_unknown_modules")!=names or gp.get("first_blocker")!=b: fail("provenance_rejection_cross_consistency","mismatch")
 by,total,successes,failures,failed_phases=validate_partial_call_rows(root,progress); durable=[row for rows in by.values() for row in rows]
 if failures: fail("provenance_durable_row_structure","failed row")
 if not durable: fail("provenance_requires_durable_rows","zero")
def validate_blocked_packaging(root,args):
 p=validate_common(root,BLOCKED_PACKAGING); b=p.get("first_blocker"); progress=strict_json(root/"outputs/benchmark_progress.json")
 pe=strict_json(root/"outputs/packaging_failure.json")
 if not isinstance(b,dict) or b.get("type")!="PackagingBlocker" or not b.get("message") or progress.get("first_blocker")!=b or pe.get("first_blocker")!=b: fail("packaging_blocker_semantics","mismatch")
 validate_fixed_ledger(root,args); rows,evidence,_=validate_request_calls(root); validate_statistics(root,rows); ledger=validate_preload_source(root,evidence); validate_memory(root); validate_pyg(root,ledger); validate_warnings(root); validate_inheritance(root,"evidence"); validate_baa_inheritance(root,"evidence"); cp=validate_correction_provenance(root)
 if progress.get("completed_scientific_calls")!=305 or pe.get("scientific_evidence_complete") is not True: fail("packaging_requires_complete_evidence","mismatch")

SEMANTIC_VALIDATORS_BY_STATUS={READY:validate_ready,INCOMPLETE:validate_incomplete,BLOCKED_GPU:validate_blocked_gpu,BLOCKED_RUNTIME:validate_blocked_runtime,BLOCKED_PROVENANCE:validate_blocked_provenance,BLOCKED_PACKAGING:validate_blocked_packaging}

def write_json(path,value): pathlib.Path(path).write_text(json.dumps(value,indent=2,sort_keys=True,ensure_ascii=False,allow_nan=False)+"\n",encoding="utf-8")
def base_scope(): return {"network_api_called":False,"dependency_changed":False,"source_or_overlay_modified":False,"model_modified_or_trained":False,"additional_local_model_loaded":False,"m4b_authorized":False,"m4c_authorized":False,"hard_trait_filter_implemented":False,"teacher_pending":["abc_complete_comparison","snapshot_review","maintainer_inquiry_unsent","strain_species_policy","final_checkpoint_strategy","zero_additional_local_model_coexistence_interpretation","m4a_full_closure"]}
def base_coexist(): return {"adrmats_remote_model_names":6,"additional_local_adrmats_gpu_models_proven":0,"coexistence_classification":"COEXISTENCE_LOCAL_MODEL_SET_NOT_ESTABLISHED","coexistence_teacher_requirement":"OPEN_WAIT_TEACHER_INTERPRETATION","coexistence_pass":False}
def build_status_fixture(target,status,validator_source,ready_source=None):
 """Build one exact, independently meaningful positive status fixture."""
 target=pathlib.Path(target)
 if status in (READY,BLOCKED_PACKAGING):
  if ready_source is None: raise ValueError("ready_source required")
  shutil.copytree(ready_source,target,copy_function=shutil.copy2)
  for rel in RESULT_FILES|((BAAA_ADDED|BAAAA_ADDED) if status==BLOCKED_PACKAGING else frozenset()):
   p=target/rel
   if p.exists(): p.unlink()
  if status==READY: return
  blocker={"type":"PackagingBlocker","stage":"deterministic_tar_construction","message":"safe benchmark evidence complete; tar transport construction failed","code":"USTAR_CONSTRUCTION_FAILURE"}
  (target/"FINAL_STATUS.txt").write_text(status+"\n",encoding="utf-8")
  (target/"M4A4B_FORMAL_GPU_BENCHMARK_REPORT.md").write_text("Status: `"+status+"`\nComplete scientific evidence was safely captured before packaging failure.\n",encoding="utf-8")
  provenance=strict_json(target/"outputs/benchmark_provenance.json"); provenance["final_status"]=status; provenance["first_blocker"]=blocker; write_json(target/"outputs/benchmark_provenance.json",provenance)
  progress=strict_json(target/"outputs/benchmark_progress.json"); progress["first_blocker"]=blocker; progress["completed_scientific_calls"]=305; write_json(target/"outputs/benchmark_progress.json",progress)
  write_json(target/"outputs/packaging_failure.json",{"first_blocker":blocker,"scientific_evidence_complete":True,"failed_artifact":"deterministic_uncompressed_posix_ustar"})
  changed={"FINAL_STATUS.txt","M4A4B_FORMAL_GPU_BENCHMARK_REPORT.md","outputs/benchmark_provenance.json","outputs/benchmark_progress.json"}
  inherited=strict_json(target/"evidence/inherited_m4a4b_file_identity.json")
  for q in inherited["files"]:
   if q["path"] in changed:
    q["prior_bytes"],q["prior_sha256"]=identity(target/q["path"]); q["new_bytes"],q["new_sha256"]=identity(target/q["path"])
  write_json(target/"evidence/inherited_m4a4b_file_identity.json",inherited); changed.add("evidence/inherited_m4a4b_file_identity.json")
  inherited=strict_json(target/"evidence/inherited_m4a4ba_file_identity.json")
  for q in inherited["files"]:
   if q["path"] in changed:
    q["new_bytes"],q["new_sha256"]=identity(target/q["path"])
    if q["classification"]=="immutable": q["prior_bytes"],q["prior_sha256"]=identity(target/q["path"])
  write_json(target/"evidence/inherited_m4a4ba_file_identity.json",inherited)
  for p in target.rglob("*"): p.chmod(0o755 if p.is_dir() or p.parent.name=="scripts" else 0o644)
  return
 for rel in expected_files_for_status(status,"evidence"):
  p=target/rel; p.parent.mkdir(parents=True,exist_ok=True)
 target.mkdir(parents=True,exist_ok=True)
 shutil.copy2(validator_source,target/"scripts/validate_m4a4b_formal_gpu_benchmark.py")
 (target/"FINAL_STATUS.txt").write_text(status+"\n"); (target/"M4A4B_FORMAL_GPU_BENCHMARK_REPORT.md").write_text("Status: `"+status+"`\n")
 write_json(target/"outputs/coexistence_boundary.json",base_coexist()); write_json(target/"outputs/scope_compliance.json",base_scope())
 blocker={"type":"IntegrityFailure","stage":"warmups","message":"one prediction failed integrity validation","code":"INTEGRITY_FAILURE"}
 if status==BLOCKED_GPU: blocker={"type":"ImmediateGpuGateBlocker","stage":"immediate_gpu_gate","message":"observed free memory below required threshold","code":"GPU_FREE_MEMORY_BELOW_THRESHOLD","observed_min_free_mib":29140.0,"minimum_free_mib":30000.0}
 if status==BLOCKED_RUNTIME: blocker={"type":"RuntimeEnvironmentBlocker","stage":"model_initialize","message":"runtime initialization failed before checkpoint load","code":"RUNTIME_INITIALIZE_FAILURE","traceback":"Traceback (most recent call last):\nRuntimeError: fixture initialization failure"}
 if status==BLOCKED_PROVENANCE: blocker={"type":"RuntimeProvenanceBlock","stage":"post_evidence_runtime_provenance","message":"rejected module outside approved roots","code":"REJECTED_OUTSIDE_ROOT_MODULE","rejected_modules":["enzymecage.unknown"]}
 write_json(target/"outputs/benchmark_provenance.json",{"final_status":status,"first_blocker":blocker})
 if status==BLOCKED_GPU:
  write_json(target/"outputs/gpu_selection_or_block.json",{"gate":"BLOCKED","blocker":blocker,"minimum_free_mib":30000.0,"observed_min_free_mib":29140.0}); write_json(target/"evidence/benchmark_process_start.json",{"launched":False,"torch_imported":False,"model_initialized":False,"checkpoint_loaded":False,"prediction_executed":False,"call_count":0})
  write_json(target/"outputs/benchmark_progress.json",{"first_blocker":blocker,"initialize_call_count":0,"checkpoint_load_count":0,"forward_call_count":0,"attempted_call_count":0})
  with (target/"evidence/gpu_gate_samples.csv").open("w",newline="") as f: w=csv.DictWriter(f,fieldnames=GPU_HEADER,lineterminator="\n"); w.writeheader(); w.writerow({"sample":1,"utc_timestamp":"2026-07-20T00:00:00.000000000Z","monotonic_ns":1,"gpu_index":0,"gpu_uuid":"GPU-fixture","name":"fixture","driver":"fixture","total_mib":49140,"used_mib":20000,"free_mib":29140,"utilization_percent":0,"compute_mode":"Default","compute_process_count":0,"compute_process_rows_json":"[]"})
 else:
  progress={"checkpoint_load_count":0,"forward_call_count":1 if status in (INCOMPLETE,BLOCKED_PROVENANCE) else 0,"initialize_call_count":1 if status==BLOCKED_RUNTIME else 0,"phases":{},"first_blocker":blocker}; write_json(target/"outputs/benchmark_progress.json",progress)
  if status in (INCOMPLETE,BLOCKED_RUNTIME,BLOCKED_PROVENANCE):
   for phase,file in (("warmups","warmup_calls.csv"),("sequential","sequential_100_calls.csv"),("concurrency_2","concurrency_2_100_calls.csv"),("concurrency_4","concurrency_4_100_calls.csv")):
    rows=[]
    with (target/"evidence"/file).open("w",newline="") as f:
     w=csv.DictWriter(f,fieldnames=CALL_HEADER,lineterminator="\n"); w.writeheader()
     if status==INCOMPLETE and phase=="warmups":
      row={k:"" for k in CALL_HEADER}; row.update({"phase":phase,"global_request_id":"warmups-001","call_index":1,"start_utc":"2026-07-20T00:00:00Z","start_ns":1,"end_utc":"2026-07-20T00:00:00.001000Z","end_ns":1000001,"latency_ms":1,"success":"false","exception_type":"IntegrityFailure","exception_message":"fixture integrity failure","integrity_pass":"false","integrity_failure_reason":"fixture","returned_count":0}); rows=[row]; w.writerow(row)
     if status==BLOCKED_PROVENANCE and phase=="warmups":
      row={k:"" for k in CALL_HEADER}; row.update({"phase":phase,"global_request_id":"warmups-001","call_index":1,"start_utc":"2026-07-20T00:00:00Z","start_ns":1,"end_utc":"2026-07-20T00:00:00.001000Z","end_ns":1000001,"latency_ms":1,"success":"true","integrity_pass":"true","returned_count":100,"response_sha256":"1"*64,"uid_order_sha256":"2"*64,"evidence_hash":"3"*64,"max_abs_score_difference_from_first_sequential":0,"max_abs_ci_difference_from_first_sequential":0}); rows=[row]; w.writerow(row)
    fp=target/"evidence"/file; n,h=identity(fp); progress["phases"][phase]={"attempted":len(rows),"success":sum(x["success"]=="true" for x in rows),"failure":sum(x["success"]!="true" for x in rows),"summary_present":False,"file":{"path":"evidence/"+file,"bytes":n,"sha256":h}}
   write_json(target/"outputs/benchmark_progress.json",progress)
  if status==BLOCKED_PROVENANCE:
   before="relative_path\tmode\tbytes\tsha256\nenzymecage/model.py\t0644\t1\t"+"0"*64+"\n"; after="relative_path\tmode\tbytes\tsha256\nenzymecage/model.py\t0644\t2\t"+"1"*64+"\n"; (target/"evidence/runtime_source_tree_before.sha256").write_text(before); (target/"evidence/runtime_source_tree_after.sha256").write_text(after)
   write_json(target/"evidence/imported_enzymecage_modules.json",[{"module":"enzymecage.unknown","classification":"REJECTED_OR_UNKNOWN","realpath":"/outside/enzymecage/unknown.py"}]); write_json(target/"evidence/generated_module_provenance.json",{"generated_helpers":[],"rejected_or_unknown_modules":["enzymecage.unknown"],"first_blocker":blocker})
 for p in target.rglob("*"): p.chmod(0o755 if p.is_dir() or p.parent.name=="scripts" else 0o644)
 target.chmod(0o755)

def parse_args():
 ap=argparse.ArgumentParser(); ap.add_argument("root"); ap.add_argument("--validation-phase",choices=("evidence","packaged"),required=True); ap.add_argument("--runtime-evidence-mode",choices=("captured","live"),required=True)
 for name in ("adrmats_zip","m4a3a_tar","d4b1a_root","d4b1a_tar","v1_root","pbb_root","pbb_tar","pbb_identity","t3g1a_source_identity","prior_tar","prior_identity","code_root","overlay_root","live_python"): ap.add_argument("--"+name.replace("_","-"),dest=name)
 return ap.parse_args()
def main():
 args=parse_args(); root=pathlib.Path(args.root).resolve()
 try: status=(root/"FINAL_STATUS.txt").read_text(encoding="utf-8").strip()
 except Exception as e: fail("final_status",e)
 if status not in SEMANTIC_VALIDATORS_BY_STATUS: fail("unknown_final_status",status)
 expected=scan_tree(root,status,args.validation_phase)
 if args.validation_phase=="packaged": validate_manifest(root,expected)
 if args.runtime_evidence_mode=="live" and status==READY:
  if any(getattr(args,x) is None for x in ("adrmats_zip","m4a3a_tar","d4b1a_root","d4b1a_tar","v1_root","pbb_root","pbb_tar","pbb_identity","t3g1a_source_identity","prior_tar","prior_identity","code_root","overlay_root","live_python")): fail("live_fixed_input","missing explicit path")
  if args.code_root!=CODE_ROOT or args.overlay_root!="/usrdata/EnzymeCAGE_runs/metatraits_m4a4pb_pydantic_overlay_20260720" or args.live_python!="/usrdata/EnzymeCAGE_envs/enzymecage_py312/bin/python": fail("live_fixed_input","fixed path")
 SEMANTIC_VALIDATORS_BY_STATUS[status](root,args)
 print("validation_phase="+args.validation_phase); print("runtime_evidence_mode="+args.runtime_evidence_mode); print(status)
if __name__=="__main__":
 try: main()
 except (ValidationError,OSError,ValueError,KeyError,TypeError) as e:
  reason=str(e) if isinstance(e,ValidationError) else e.__class__.__name__.lower()+":"+str(e)[:180].replace("\n"," ")
  print("M4A4BA_VALIDATION_ERROR:"+reason); raise SystemExit(1)
