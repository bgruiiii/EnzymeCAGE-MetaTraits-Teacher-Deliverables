#!/usr/bin/env python3
"""Context-free, standard-library-only, status-aware M4a-4B validator."""
import argparse, base64, csv, hashlib, json, math, pathlib, re, stat, sys

READY="M4A4B_BENCHMARK_READY_FOR_LOCAL_AUDIT_COEXISTENCE_OPEN"
INCOMPLETE="M4A4B_BENCHMARK_INCOMPLETE_PREDICTION_OR_CONCURRENCY_FAILURE"
BLOCKED_GPU="M4A4B_BENCHMARK_BLOCKED_IMMEDIATE_GPU_GATE"
BLOCKED_RUNTIME="M4A4B_BENCHMARK_BLOCKED_RUNTIME_ENVIRONMENT"
BLOCKED_PROVENANCE="M4A4B_BENCHMARK_BLOCKED_RUNTIME_PROVENANCE_AFTER_EVIDENCE_CAPTURE"
BLOCKED_PACKAGING="M4A4B_BENCHMARK_BLOCKED_PACKAGING_OR_TRANSPORT"
CALL_HEADER=["phase","global_request_id","call_index","worker_id","worker_sequence","barrier_release_ns","start_utc","start_ns","end_utc","end_ns","latency_ms","success","exception_type","exception_message","integrity_pass","integrity_failure_reason","returned_count","response_sha256","uid_order_sha256","evidence_hash","max_abs_score_difference_from_first_sequential","max_abs_ci_difference_from_first_sequential"]
COMMON={"FINAL_STATUS.txt","M4A4B_FORMAL_GPU_BENCHMARK_REPORT.md","inputs/formal_benchmark_contract.json","scripts/run_m4a4b_formal_gpu_benchmark.py","scripts/validate_m4a4b_formal_gpu_benchmark.py","outputs/required_input_identity.json","outputs/runtime_source_identity.json","outputs/live_runtime_overlay_gate.json","outputs/gpu_selection_or_block.json","outputs/coexistence_boundary.json","outputs/scope_compliance.json","outputs/benchmark_provenance.json","outputs/benchmark_progress.json","evidence/runtime_source_tree_before.sha256","evidence/runtime_source_tree_after.sha256","evidence/imported_enzymecage_modules.json","evidence/generated_module_provenance.json","evidence/gpu_gate_samples.csv","evidence/benchmark_process_start.json","evidence/nvidia_smi_memory_samples.csv","evidence/environment.txt","evidence/commands.txt","logs/benchmark.stdout.txt","logs/benchmark.stderr.txt","logs/benchmark.exit_code.txt"}
RAW={"evidence/warmup_calls.csv","evidence/sequential_100_calls.csv","evidence/concurrency_2_100_calls.csv","evidence/concurrency_4_100_calls.csv"}
SUCCESS={"outputs/runtime_preload.json","outputs/warmup_audit.json","outputs/sequential_summary.json","outputs/concurrency_2_summary.json","outputs/concurrency_4_summary.json","outputs/latency_degradation.json","outputs/memory_summary.json","outputs/response_integrity.json","evidence/first_response_warmups.json","evidence/first_response_sequential.json","evidence/first_response_concurrency_2.json","evidence/first_response_concurrency_4.json"}
TESTLOG={"logs/validator_negative_tests.csv","logs/validator_negative_tests.stdout.txt","outputs/validator_results.json"}
READY_SET=frozenset(COMMON|RAW|SUCCESS|TESTLOG|{"MANIFEST.sha256"})
# Status maps are deliberately explicit. Runtime/provenance/incomplete packages retain every reached raw/common artifact.
INCOMPLETE_SET=frozenset((COMMON|RAW|{"outputs/runtime_preload.json","outputs/warmup_audit.json","outputs/memory_summary.json","outputs/response_integrity.json"}|TESTLOG|{"MANIFEST.sha256"}))
PROVENANCE_SET=READY_SET
GPU_SET=frozenset({"FINAL_STATUS.txt","M4A4B_FORMAL_GPU_BENCHMARK_REPORT.md","inputs/formal_benchmark_contract.json","scripts/run_m4a4b_formal_gpu_benchmark.py","scripts/validate_m4a4b_formal_gpu_benchmark.py","outputs/required_input_identity.json","outputs/runtime_source_identity.json","outputs/live_runtime_overlay_gate.json","outputs/gpu_selection_or_block.json","outputs/coexistence_boundary.json","outputs/scope_compliance.json","evidence/runtime_source_tree_before.sha256","evidence/gpu_gate_samples.csv","evidence/benchmark_process_start.json","evidence/commands.txt","logs/benchmark.stdout.txt","logs/benchmark.stderr.txt","logs/benchmark.exit_code.txt"}|TESTLOG|{"MANIFEST.sha256"})
RUNTIME_SET=INCOMPLETE_SET
PACKAGING_SET=INCOMPLETE_SET
EXPECTED_FILES_BY_STATUS={READY:READY_SET,INCOMPLETE:INCOMPLETE_SET,BLOCKED_GPU:GPU_SET,BLOCKED_RUNTIME:RUNTIME_SET,BLOCKED_PROVENANCE:PROVENANCE_SET,BLOCKED_PACKAGING:PACKAGING_SET}

class E(Exception): pass
def fail(reason,detail="failed"): raise E(reason+":"+str(detail)[:180].replace("\n"," "))
def strict_json(p):
 try: return json.loads(p.read_text(encoding="utf-8"),parse_constant=lambda x:fail("nonfinite_value",x))
 except (UnicodeDecodeError,json.JSONDecodeError) as e: fail("strict_json",e)
def ident(p):
 b=p.read_bytes(); return len(b),hashlib.sha256(b).hexdigest()
def rows(p):
 try:
  with p.open(newline="",encoding="utf-8") as f: r=csv.DictReader(f,strict=True); out=list(r); header=r.fieldnames
 except (UnicodeDecodeError,csv.Error) as e: fail("strict_csv",e)
 if header!=CALL_HEADER: fail("call_header",p.name)
 return out
def finite(v,reason="nonfinite_value"):
 try: x=float(v)
 except (TypeError,ValueError): fail(reason,v)
 if not math.isfinite(x): fail(reason,v)
 return x

def expected_for(status,phase):
 expected=set(EXPECTED_FILES_BY_STATUS[status])
 if phase=="evidence": expected-=TESTLOG|{"MANIFEST.sha256"}
 return expected

def scan(root,status,phase):
 expected=expected_for(status,phase); actual=set(); dirs=set(); secret=re.compile(rb"(?:AKIA[0-9A-Z]{16}|sk-[A-Za-z0-9_-]{16,}|(?:password|api[_-]?key|access[_-]?token)\s*[:=]\s*[^\s\"']+)",re.I)
 if root.is_symlink() or not root.is_dir() or stat.S_IMODE(root.stat().st_mode)!=0o755: fail("package_structure","root")
 for p in root.rglob("*"):
  s=p.lstat(); rel=p.relative_to(root).as_posix()
  if stat.S_ISDIR(s.st_mode):
   if stat.S_IMODE(s.st_mode)!=0o755: fail("package_mode",rel)
   dirs.add(rel); continue
  if stat.S_ISLNK(s.st_mode) or not stat.S_ISREG(s.st_mode) or s.st_nlink!=1: fail("unsafe_object",rel)
  desired=0o755 if rel.startswith("scripts/") else 0o644
  if stat.S_IMODE(s.st_mode)!=desired: fail("package_mode",rel)
  data=p.read_bytes();
  if secret.search(data): fail("secret_like_payload",rel)
  try: data.decode("utf-8")
  except UnicodeDecodeError: fail("malformed_utf8",rel)
  actual.add(rel)
 if actual!=expected: fail("status_file_set",f"missing={sorted(expected-actual)} extra={sorted(actual-expected)}")
 needed=set()
 for rel in expected:
  q=pathlib.PurePosixPath(rel).parent
  while str(q)!=".": needed.add(str(q)); q=q.parent
 if dirs!=needed: fail("package_structure",f"directories={sorted(dirs^needed)}")

def manifest(root,expected):
 p=root/"MANIFEST.sha256"; seen={}
 for line in p.read_text(encoding="utf-8").splitlines():
  m=re.fullmatch(r"([0-9a-f]{64})  (.+)",line)
  if not m: fail("manifest_format","line")
  h,rel=m.groups(); pure=pathlib.PurePosixPath(rel)
  if rel in seen or pure.is_absolute() or ".." in pure.parts or "\\" in rel or rel=="MANIFEST.sha256": fail("manifest_format",rel)
  seen[rel]=h
 actual={rel:ident(root/rel)[1] for rel in expected if rel!="MANIFEST.sha256"}
 if seen!=actual: fail("manifest_mismatch","content")

def validate_boundaries(root):
 c=strict_json(root/"outputs/coexistence_boundary.json")
 required={"adrmats_remote_model_names":6,"additional_local_adrmats_gpu_models_proven":0,"coexistence_classification":"COEXISTENCE_LOCAL_MODEL_SET_NOT_ESTABLISHED","coexistence_teacher_requirement":"OPEN_WAIT_TEACHER_INTERPRETATION","coexistence_pass":False}
 if c!=required: fail("coexistence_boundary","mismatch")
 s=strict_json(root/"outputs/scope_compliance.json")
 for k in ("network_api_called","dependency_changed","source_or_overlay_modified","model_modified_or_trained","additional_local_model_loaded","m4b_authorized","m4c_authorized","hard_trait_filter_implemented"):
  if s.get(k) is not False: fail("scope_boundary",k)
 pending={"abc_complete_comparison","snapshot_review","maintainer_inquiry_unsent","strain_species_policy","final_checkpoint_strategy","zero_additional_local_model_coexistence_interpretation","m4a_full_closure"}
 if set(s.get("teacher_pending",[]))!=pending: fail("scope_boundary","teacher_pending")

def validate_gpu(root):
 with (root/"evidence/gpu_gate_samples.csv").open(newline="",encoding="utf-8") as f: rr=list(csv.DictReader(f,strict=True))
 if len(rr)!=3 or [r["sample"] for r in rr]!=["1","2","3"]: fail("gpu_sample_count","rows")
 ns=[int(r["monotonic_ns"]) for r in rr]
 if any((ns[i]-ns[i-1])/1e9<2 for i in (1,2)): fail("gpu_sample_spacing","below_two")
 if len({r["gpu_uuid"] for r in rr})!=1 or any(int(r["free_mib"])<40000 or r["compute_mode"]!="Default" or int(r["compute_process_count"])!=0 for r in rr): fail("gpu_gate_semantics","mismatch")
 st=strict_json(root/"evidence/benchmark_process_start.json"); gap=(int(st["process_start_monotonic_ns"])-ns[2])/1e9
 if gap<0 or gap>5 or abs(gap-finite(st["launch_gap_seconds"]))>1e-9: fail("gpu_launch_gap","mismatch")

def ledger(text):
 lines=text.splitlines()
 if not lines or lines[0]!="relative_path\tmode\tbytes\tsha256": fail("source_ledger_format","header")
 out={}
 for line in lines[1:]:
  v=line.split("\t")
  if len(v)!=4 or not re.fullmatch(r"[0-9a-f]{64}",v[3]) or v[0] in out: fail("source_ledger_format","row")
  out[v[0]]=(v[1],int(v[2]),v[3])
 return out
def validate_provenance(root,status):
 a=(root/"evidence/runtime_source_tree_before.sha256").read_text(); b=(root/"evidence/runtime_source_tree_after.sha256").read_text(); la=ledger(a); lb=ledger(b)
 if status==READY and la!=lb: fail("source_ledger_mismatch","ready")
 inv=strict_json(root/"evidence/imported_enzymecage_modules.json"); gp=strict_json(root/"evidence/generated_module_provenance.json")
 if not isinstance(inv,list) or not inv: fail("imported_inventory","empty")
 by={x.get("module"):x for x in inv}
 if len(by)!=len(inv): fail("imported_inventory","duplicate")
 unknown=[x for x in inv if x.get("classification")=="REJECTED_OR_UNKNOWN"]
 if status==READY and unknown: fail("unknown_outside_module","accepted ready")
 if sorted(gp.get("accepted_static_modules",[]))!=sorted(x["module"] for x in inv if x.get("classification")=="ACCEPTED_STATIC_ENZYMECAGE_MODULE"): fail("imported_inventory","static crosscheck")
 helpers=gp.get("generated_helpers",[])
 if status==READY and not helpers: fail("generated_class_linkage","none")
 for g in helpers:
  try: data=base64.b64decode(g["source_base64"],validate=True)
  except Exception: fail("generated_source_hash","base64")
  if len(data)!=g.get("bytes") or hashlib.sha256(data).hexdigest()!=g.get("sha256"): fail("generated_source_hash",g.get("module"))
  checks=g.get("checks",{})
  required={"live_class_method_module_exact","module_spec_name_exact","module_spec_origin_realpath_exact","regular_single_link_temporary_python_source","owning_parent_below_code_root","owning_parent_unchanged_contract","generated_dir_absent_from_sys_path","package_agrees"}
  if set(checks)!=required or not all(checks.values()): fail("generated_class_linkage",g.get("module"))
  owner=g.get("owner",{}); rel=owner.get("parent_relative_path")
  if rel not in la or la[rel][1:]!=(owner.get("parent_bytes"),owner.get("parent_sha256")): fail("generated_class_linkage","parent ledger")
  rec=by.get(g.get("module"))
  if not rec or rec.get("classification")!="PYG_GENERATED_MESSAGE_PASSING_HELPER" or rec.get("sha256")!=g.get("sha256"): fail("generated_class_linkage","inventory")
 if status==READY and (gp.get("rejected_or_unknown_modules") or gp.get("untrusted_sys_path_insertion_detected") is not False): fail("unknown_outside_module","provenance")

def recompute_summary(rr,out,reason):
 good=[finite(r["latency_ms"]) for r in rr if r["success"]=="true" and r["integrity_pass"]=="true"]
 if len(good)!=100: fail("call_failure",reason)
 s=sorted(good); expected={"min_ms":s[0],"mean_ms":sum(s)/100,"max_ms":s[-1],"p50_ms":s[49],"p95_ms":s[94],"p99_ms":s[98]}
 for k,v in expected.items():
  if not math.isclose(finite(out.get(k)),v,rel_tol=1e-12,abs_tol=1e-12): fail("percentile_recomputation",reason+":"+k)
 return expected

def validate_ready(root):
 progress=strict_json(root/"outputs/benchmark_progress.json"); phase_rows={}
 specs={"warmups":("warmup_calls.csv",5),"sequential":("sequential_100_calls.csv",100),"concurrency_2":("concurrency_2_100_calls.csv",100),"concurrency_4":("concurrency_4_100_calls.csv",100)}
 gids=[]
 for phase,(file,count) in specs.items():
  rr=rows(root/"evidence"/file); phase_rows[phase]=rr
  if len(rr)!=count or any(r["phase"]!=phase for r in rr): fail("durable_row_count",phase)
  for r in rr:
   if r["global_request_id"] in gids: fail("call_ids","duplicate")
   gids.append(r["global_request_id"]); sn=int(r["start_ns"]); en=int(r["end_ns"])
   if en<sn or not math.isclose(finite(r["latency_ms"]),(en-sn)/1e6,rel_tol=1e-12,abs_tol=1e-9): fail("call_timestamps",phase)
   if r["success"]!="true" or r["integrity_pass"]!="true" or r["exception_type"] or r["exception_message"] or r["integrity_failure_reason"]: fail("call_failure",phase)
   if int(r["returned_count"])!=100 or not re.fullmatch(r"[0-9a-f]{64}",r["response_sha256"]) or not re.fullmatch(r"[0-9a-f]{64}",r["uid_order_sha256"]): fail("response_integrity",phase)
  pr=progress.get("phases",{}).get(phase,{})
  n,h=ident(root/"evidence"/file)
  if pr.get("durable_rows")!=count or pr.get("attempted")!=count or pr.get("success")!=count or pr.get("integrity_pass")!=count or pr.get("exception")!=0 or pr.get("bytes")!=n or pr.get("sha256")!=h: fail("progress_count",phase)
 if sorted(int(r["call_index"]) for r in phase_rows["sequential"])!=list(range(1,101)): fail("call_ids","sequential")
 for phase,workers,each in (("concurrency_2",2,50),("concurrency_4",4,25)):
  dist={str(w):sum(r["worker_id"]==str(w) for r in phase_rows[phase]) for w in range(workers)}
  if dist!={str(w):each for w in range(workers)}: fail("concurrency_worker_split",phase)
  for w in range(workers):
   if sorted(int(r["worker_sequence"]) for r in phase_rows[phase] if r["worker_id"]==str(w))!=list(range(1,each+1)): fail("concurrency_worker_split",phase)
 seq=recompute_summary(phase_rows["sequential"],strict_json(root/"outputs/sequential_summary.json"),"sequential")
 c2=recompute_summary(phase_rows["concurrency_2"],strict_json(root/"outputs/concurrency_2_summary.json"),"concurrency_2")
 c4=recompute_summary(phase_rows["concurrency_4"],strict_json(root/"outputs/concurrency_4_summary.json"),"concurrency_4")
 deg=strict_json(root/"outputs/latency_degradation.json")
 for phase,vals in (("concurrency_2",c2),("concurrency_4",c4)):
  for q in (50,95,99):
   if not math.isclose(finite(deg[phase][f"p{q}_ratio"]),vals[f"p{q}_ms"]/seq[f"p{q}_ms"],rel_tol=1e-12,abs_tol=1e-12): fail("degradation_ratio",phase)
 if progress.get("forward_call_count")!=305 or progress.get("checkpoint_load_count")!=1 or progress.get("initialize_call_count")!=2: fail("progress_count","global")
 pre=strict_json(root/"outputs/runtime_preload.json"); ri=strict_json(root/"outputs/response_integrity.json")
 if pre.get("checkpoint_load_count")!=1 or pre.get("initialize_call_count")!=2 or len(pre.get("model_object_ids",[]))!=5 or not pre.get("singleton_same_five_models"): fail("preload_singleton","mismatch")
 if ri.get("forward_call_count_actual")!=305 or not ri.get("all_305_calls_successful") or not ri.get("all_response_integrity_pass") or not ri.get("same_runtime_and_models_after_all_calls"): fail("response_integrity","summary")
 # First responses independently canonical-hash to a durable row in their phase.
 for phase in specs:
  obj=strict_json(root/f"evidence/first_response_{phase}.json"); h=hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
  if h not in {r["response_sha256"] for r in phase_rows[phase]}: fail("first_response_hash",phase)
 validate_memory(root)
 validate_provenance(root,READY)

def validate_memory(root):
 with (root/"evidence/nvidia_smi_memory_samples.csv").open(newline="",encoding="utf-8") as f: rr=list(csv.DictReader(f,strict=True))
 m=strict_json(root/"outputs/memory_summary.json")
 for phase,out in m.get("phases",{}).items():
  x=[r for r in rr if r["phase"]==phase]
  if len(x)!=out.get("row_count"): fail("memory_peak",phase+":count")
  dv=[finite(r["device_used_mib"]) for r in x if r["device_used_mib"]]; pr=[finite(r["process_used_mib"]) for r in x if r["process_used_mib"]]
  if (max(dv) if dv else None)!=out.get("device_peak_used_mib") or (max(pr) if pr else None)!=out.get("process_peak_used_mib"): fail("memory_peak",phase)

def validate_incomplete(root):
 validate_memory(root); validate_provenance(root,INCOMPLETE)
 p=strict_json(root/"outputs/benchmark_progress.json")
 if p.get("forward_call_count",0)>=305 and all(v.get("success")==v.get("attempted") for v in p.get("phases",{}).values()): fail("status_semantics","incomplete has full success")
def validate_blocked_gpu(root):
 # The exact small file set and no memory/imported files prove no torch launch.
 g=strict_json(root/"outputs/gpu_selection_or_block.json")
 if g.get("gate")!="BLOCKED": fail("status_semantics","gpu")
def validate_blocked_runtime(root):
 p=strict_json(root/"outputs/benchmark_progress.json")
 if not p.get("first_blocker"): fail("status_semantics","runtime traceback")
 validate_memory(root); validate_provenance(root,BLOCKED_RUNTIME)
def validate_blocked_provenance(root):
 validate_ready(root)
 # READY semantics above rejects blockers; provenance status instead requires all call semantics plus a real provenance blocker.
def validate_blocked_packaging(root):
 p=strict_json(root/"outputs/benchmark_progress.json")
 if not p.get("first_blocker"): fail("status_semantics","packaging")

SEMANTIC_VALIDATORS_BY_STATUS={READY:validate_ready,INCOMPLETE:validate_incomplete,BLOCKED_GPU:validate_blocked_gpu,BLOCKED_RUNTIME:validate_blocked_runtime,BLOCKED_PROVENANCE:validate_blocked_provenance,BLOCKED_PACKAGING:validate_blocked_packaging}

def main():
 ap=argparse.ArgumentParser(); ap.add_argument("root"); ap.add_argument("--validation-phase",choices=("evidence","packaged"),required=True); ap.add_argument("--runtime-evidence-mode",choices=("captured","live"),required=True); args=ap.parse_args(); root=pathlib.Path(args.root).resolve()
 try: status=(root/"FINAL_STATUS.txt").read_text(encoding="utf-8").strip()
 except Exception as e: fail("final_status",e)
 if status not in EXPECTED_FILES_BY_STATUS: fail("unknown_final_status",status)
 scan(root,status,args.validation_phase); validate_boundaries(root); validate_gpu(root)
 if args.validation_phase=="packaged": manifest(root,expected_for(status,args.validation_phase))
 SEMANTIC_VALIDATORS_BY_STATUS[status](root)
 prov=strict_json(root/"outputs/benchmark_provenance.json")
 if prov.get("final_status")!=status: fail("status_semantics","provenance")
 report=(root/"M4A4B_FORMAL_GPU_BENCHMARK_REPORT.md").read_text(encoding="utf-8")
 if status not in report: fail("status_semantics","report")
 print("validation_phase="+args.validation_phase); print("runtime_evidence_mode="+args.runtime_evidence_mode); print(status)

if __name__=="__main__":
 try: main()
 except (E,OSError,ValueError,KeyError,TypeError) as e:
  reason=str(e) if isinstance(e,E) else e.__class__.__name__.lower()+":"+str(e)[:180].replace("\n"," ")
  print("M4A4B_BENCHMARK_VALIDATION_ERROR:"+reason); raise SystemExit(1)
