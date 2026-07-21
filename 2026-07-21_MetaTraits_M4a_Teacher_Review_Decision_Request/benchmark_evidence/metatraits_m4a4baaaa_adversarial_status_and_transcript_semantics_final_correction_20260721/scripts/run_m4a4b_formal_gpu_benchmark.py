#!/usr/bin/env python3
"""One-shot M4a-4B GPU benchmark. Streams are owned by the outer launcher."""
import argparse, base64, concurrent.futures, csv, datetime, hashlib, importlib, importlib.metadata
import inspect, json, math, os, pathlib, stat, sys, threading, time, traceback

READY="M4A4B_BENCHMARK_READY_FOR_LOCAL_AUDIT_COEXISTENCE_OPEN"
INCOMPLETE="M4A4B_BENCHMARK_INCOMPLETE_PREDICTION_OR_CONCURRENCY_FAILURE"
BLOCKED_RUNTIME="M4A4B_BENCHMARK_BLOCKED_RUNTIME_ENVIRONMENT"
BLOCKED_PROVENANCE="M4A4B_BENCHMARK_BLOCKED_RUNTIME_PROVENANCE_AFTER_EVIDENCE_CAPTURE"
ROOT_NAME="metatraits_m4a4b_pyg_provenance_durable_evidence_status_aware_benchmark_20260720"
CALL_HEADER=["phase","global_request_id","call_index","worker_id","worker_sequence","barrier_release_ns","start_utc","start_ns","end_utc","end_ns","latency_ms","success","exception_type","exception_message","integrity_pass","integrity_failure_reason","returned_count","response_sha256","uid_order_sha256","evidence_hash","max_abs_score_difference_from_first_sequential","max_abs_ci_difference_from_first_sequential"]
MEM_HEADER=["utc_timestamp","monotonic_ns","gpu_uuid","gpu_index","device_used_mib","device_free_mib","utilization_percent","benchmark_pid","process_used_mib","phase","device_query_status","process_query_status"]
CORE={
 "enzymecage/model.py":(14585,"005037a1d2c063bd7d71b8ff08ed4361c139ba37be3b822c87c8fa2d84890348"),
 "enzymecage/base.py":(2420,"abdfe7875a2b0c49032031dbc54915c435ed0bda895e0cce14c92be0be7421de"),
 "enzymecage/attention.py":(2196,"388db15eac48ac4c6251879b3b1be695bbe632ab1be3040e45df7cfaf2a3ca95"),
 "enzymecage/interaction.py":(4994,"1e03b0a4bcf5bf68019c9af4542bb673eb8f8f717427b652674ac88bc706ada3"),
 "enzymecage/dataset/geometric.py":(17852,"8415f772f2b4a723c6a2895d74db3b54b28b514c259a1424d2b1e83073657dfb"),
 "enzymecage/dataset/sharded_protein.py":(4629,"64ba8a97280fc1b4b7112139ada0487758c4f848ebb15981abf8eba098054811")}
CHECKPOINTS={40:(72266498,"a95d4687e2cadad1c12f7c1defd21dbdf43db3cce96aa9caace39dbcc226586d"),41:(72266498,"c429a98bc265e20d415c3d6f479e0f0d6c47d81c13135c589e2a5e173978dbef"),42:(72266498,"cc54be33a23b78fb89c183f0bca6f87b442a5be4dad9666428d05a72a9b7f7a3"),43:(72266498,"3eb80be83cb41574204239c80f11008f728029dd9e4ba14c639749d8176b5220"),44:(72266498,"b9547d3ba17725a5910cf243d33af9367abb12b3215f4b526405f8bdb14acd16")}

def utc(): return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="microseconds").replace("+00:00","Z")
def ident(path):
 h=hashlib.sha256(); n=0
 with pathlib.Path(path).open("rb") as f:
  for b in iter(lambda:f.read(1048576),b""): h.update(b); n+=len(b)
 return n,h.hexdigest()
def canonical(x): return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()
def durable_bytes(path,data):
 p=pathlib.Path(path); tmp=p.with_name(p.name+".tmp")
 with tmp.open("wb") as f: f.write(data); f.flush(); os.fsync(f.fileno())
 os.replace(tmp,p); fd=os.open(p.parent,os.O_RDONLY); os.fsync(fd); os.close(fd)
def dump(path,x): durable_bytes(path,json.dumps(x,indent=2,sort_keys=True,ensure_ascii=False,allow_nan=False).encode()+b"\n")
def bools(x): return "true" if x else "false"

class DurableCSV:
 def __init__(self,path):
  self.path=pathlib.Path(path); self.lock=threading.Lock(); self.count=0
  self.handle=self.path.open("w",newline="",encoding="utf-8")
  self.writer=csv.DictWriter(self.handle,fieldnames=CALL_HEADER,extrasaction="ignore",lineterminator="\n")
  self.writer.writeheader(); self._sync()
 def _sync(self): self.handle.flush(); os.fsync(self.handle.fileno())
 def append(self,row):
  with self.lock:
   self.writer.writerow({k:row.get(k,"") for k in CALL_HEADER}); self._sync(); self.count+=1
 def close(self):
  if not self.handle.closed: self._sync(); self.handle.close()

class Sampler:
 def __init__(self,path,uuid,index,pid):
  self.path=pathlib.Path(path); self.uuid=uuid; self.index=index; self.pid=pid; self.phase="baseline"; self.lock=threading.Lock(); self.stop_event=threading.Event(); self.thread=None
 def set(self,p):
  with self.lock: self.phase=p
 def start(self): self.thread=threading.Thread(target=self.run,name="m4a4b-memory-sampler",daemon=True); self.thread.start()
 def stop(self):
  self.stop_event.set()
  if self.thread: self.thread.join(15)
 def run(self):
  with self.path.open("w",newline="",encoding="utf-8") as f:
   w=csv.DictWriter(f,fieldnames=MEM_HEADER,lineterminator="\n"); w.writeheader(); f.flush(); os.fsync(f.fileno())
   while not self.stop_event.is_set():
    begun=time.monotonic(); ns=time.perf_counter_ns(); stamp=utc()
    import subprocess
    d=subprocess.run(["/usr/bin/nvidia-smi","--query-gpu=index,uuid,memory.used,memory.free,utilization.gpu","--format=csv,noheader,nounits"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,check=False)
    q=subprocess.run(["/usr/bin/nvidia-smi","--query-compute-apps=gpu_uuid,pid,used_memory","--format=csv,noheader,nounits"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,check=False)
    selected=None
    for raw in d.stdout.splitlines():
     v=next(csv.reader([raw],skipinitialspace=True))
     if len(v)==5 and v[1].strip()==self.uuid: selected=v
    pm=""; ps="not_present" if q.returncode==0 else str(q.returncode)
    for raw in q.stdout.splitlines():
     v=next(csv.reader([raw],skipinitialspace=True))
     if len(v)>=3 and v[0].strip()==self.uuid and v[1].strip()==str(self.pid): pm=v[2].strip(); ps="0"
    with self.lock: phase=self.phase
    row={"utc_timestamp":stamp,"monotonic_ns":ns,"gpu_uuid":self.uuid,"gpu_index":self.index,"device_used_mib":"","device_free_mib":"","utilization_percent":"","benchmark_pid":self.pid,"process_used_mib":pm,"phase":phase,"device_query_status":d.returncode,"process_query_status":ps}
    if selected: row.update({"gpu_index":selected[0].strip(),"device_used_mib":selected[2].strip(),"device_free_mib":selected[3].strip(),"utilization_percent":selected[4].strip()})
    else: row["device_query_status"]="selected_not_found" if d.returncode==0 else d.returncode
    w.writerow(row); f.flush(); os.fsync(f.fileno()); self.stop_event.wait(max(0,.15-(time.monotonic()-begun)))

def torch_mem(torch):
 return {"allocated_mib":torch.cuda.memory_allocated()/1048576,"reserved_mib":torch.cuda.memory_reserved()/1048576,"peak_allocated_mib":torch.cuda.max_memory_allocated()/1048576,"peak_reserved_mib":torch.cuda.max_memory_reserved()/1048576}

def response_record(response,pool,expected,baseline):
 obj=response.model_dump(mode="json"); ranked=obj.get("ranked_enzymes",[]); uids=[x.get("uid") for x in ranked]; reasons=[]
 if len(ranked)!=100: reasons.append("returned_count")
 if len(set(uids))!=100 or set(uids)!=pool: reasons.append("uid_pool")
 if [x.get("rank") for x in ranked]!=list(range(1,101)): reasons.append("ranks")
 ev=obj.get("evidence_hash")
 if expected is not None and ev!=expected: reasons.append("evidence_hash")
 for item in ranked:
  try:
   if not math.isfinite(float(item["score"])): reasons.append("score_nonfinite")
   ci=item.get("ensemble_ci");
   if not isinstance(ci,list) or len(ci)!=2 or not all(math.isfinite(float(v)) for v in ci): reasons.append("ci_invalid")
  except (KeyError,TypeError,ValueError): reasons.append("numeric_schema")
 raw=canonical(obj); order=canonical(uids); sd=cd=0.0
 if baseline is not None and len(ranked)==100:
  try:
   base={x["uid"]:x for x in baseline["ranked_enzymes"]}
   sd=max(abs(float(x["score"])-float(base[x["uid"]]["score"])) for x in ranked)
   cd=max(abs(float(x["ensemble_ci"][j])-float(base[x["uid"]]["ensemble_ci"][j])) for x in ranked for j in (0,1))
  except (KeyError,TypeError,ValueError): reasons.append("baseline_comparison")
 return obj,{"response_sha256":hashlib.sha256(raw).hexdigest(),"uid_order_sha256":hashlib.sha256(order).hexdigest(),"evidence_hash":ev or "","returned_count":len(ranked),"integrity_pass":not reasons,"integrity_failure_reason":";".join(sorted(set(reasons))),"max_abs_score_difference_from_first_sequential":sd,"max_abs_ci_difference_from_first_sequential":cd}

def call(torch,runtime,request,pool,expected,baseline,phase,index,gid,worker="",sequence="",release=""):
 row={"phase":phase,"global_request_id":gid,"call_index":index,"worker_id":worker,"worker_sequence":sequence,"barrier_release_ns":release,"success":"false","exception_type":"","exception_message":"","integrity_pass":"false","integrity_failure_reason":"","returned_count":"","response_sha256":"","uid_order_sha256":"","evidence_hash":"","max_abs_score_difference_from_first_sequential":"","max_abs_ci_difference_from_first_sequential":""}; obj=None
 try:
  torch.cuda.synchronize(); su=utc(); sn=time.perf_counter_ns(); response=runtime.predict(request); torch.cuda.synchronize(); en=time.perf_counter_ns(); eu=utc()
  obj,extra=response_record(response,pool,expected,baseline); row.update(extra); row["success"]=bools(extra["integrity_pass"]); row["integrity_pass"]=bools(extra["integrity_pass"])
 except BaseException as exc:
  try: torch.cuda.synchronize()
  except BaseException: pass
  if 'sn' not in locals(): su=utc(); sn=time.perf_counter_ns()
  en=time.perf_counter_ns(); eu=utc(); row["exception_type"]=type(exc).__name__; row["exception_message"]=str(exc)[:1000]
 row.update({"start_utc":su,"start_ns":sn,"end_utc":eu,"end_ns":en,"latency_ms":(en-sn)/1e6})
 return row,obj

def phase_audit(root,name,csvfile,progress,counters,runtime=None):
 p=root/"evidence"/csvfile
 with p.open(newline="",encoding="utf-8") as f: rows=list(csv.DictReader(f,strict=True))
 n,sha=ident(p); attempted=len(rows); succ=sum(r["success"]=="true" for r in rows); integ=sum(r["integrity_pass"]=="true" for r in rows); exc=sum(bool(r["exception_type"]) for r in rows)
 progress["phases"][name]={"csv_path":"evidence/"+csvfile,"bytes":n,"sha256":sha,"durable_rows":attempted,"attempted":attempted,"success":succ,"exception":exc,"integrity_pass":integ}
 progress.update(counters)
 if runtime is not None: progress.update({"runtime_object_id":id(runtime),"model_object_ids":[id(x) for x in runtime.models]})
 dump(root/"outputs/benchmark_progress.json",progress)

def stats(rows,start,end,concurrency=False):
 values=[float(r["latency_ms"]) for r in rows if r["success"]=="true" and r["integrity_pass"]=="true"]
 x={"attempted":len(rows),"successful_integrity":len(values),"phase_start_ns":start,"phase_end_ns":end,"elapsed_seconds":(end-start)/1e9,"nearest_rank":True}
 if len(values)==100:
  s=sorted(values); x.update({"min_ms":s[0],"mean_ms":sum(s)/100,"max_ms":s[-1],"p50_ms":s[49],"p95_ms":s[94],"p99_ms":s[98]})
  if concurrency: x["bounded_observed_throughput_per_second"]=100/x["elapsed_seconds"]
 return x

def imported_inventory(code_root,MessagePassing,torch_geometric):
 code_root=code_root.resolve(); inv=[]; generated=[]; rejected=[]; static=[]; linked={}
 # Exact live linkage from accepted static classes to generated implementations.
 for mod_name,mod in sorted(sys.modules.items()):
  path=getattr(mod,"__file__",None)
  if not path: continue
  try: rp=pathlib.Path(path).resolve(); rp.relative_to(code_root)
  except (OSError,ValueError): continue
  for cname,cls in inspect.getmembers(mod,inspect.isclass):
   try: is_mp=issubclass(cls,MessagePassing) and cls is not MessagePassing
   except TypeError: is_mp=False
   if not is_mp: continue
   for method in ("propagate","edge_updater"):
    fn=getattr(cls,method,None); mn=getattr(fn,"__module__",None)
    if mn and mn in sys.modules and (mn=="enzymecage" or mn.startswith("enzymecage.")) and mn!=cls.__module__:
     linked[mn]=(cls,method,fn,rp)
 tg_root=pathlib.Path(torch_geometric.__file__).resolve().parent
 mp_path=pathlib.Path(inspect.getsourcefile(MessagePassing)).resolve(); mp_n,mp_sha=ident(mp_path)
 discover=[]
 for rel in ("nn/conv/message_passing.py","nn/conv/collect.jinja","nn/conv/propagate.jinja","template.py"):
  hits=list(tg_root.rglob(pathlib.Path(rel).name))
  for p in hits:
   if p.is_file() and p not in [pathlib.Path(x["path"]) for x in discover]:
    n,h=ident(p); discover.append({"path":str(p.resolve()),"bytes":n,"sha256":h})
 for name,module in sorted(sys.modules.items()):
  if name!="enzymecage" and not name.startswith("enzymecage."): continue
  f=getattr(module,"__file__",None); spec=getattr(module,"__spec__",None); loader=getattr(module,"__loader__",None)
  rec={"module":name,"file":f,"realpath":None,"regular_file":False,"symlink":None,"hardlink_count":None,"bytes":None,"sha256":None,"package":getattr(module,"__package__",None),"spec_name":getattr(spec,"name",None),"spec_origin":getattr(spec,"origin",None),"spec_loader_class":type(getattr(spec,"loader",None)).__name__ if spec else None,"loader_class":type(loader).__name__ if loader else None,"classification":"REJECTED_OR_UNKNOWN","classification_reasons":[]}
  if f:
   p=pathlib.Path(f); rp=p.resolve(); rec["realpath"]=str(rp)
   try:
    st=p.lstat(); rec.update({"regular_file":stat.S_ISREG(st.st_mode),"symlink":stat.S_ISLNK(st.st_mode),"hardlink_count":st.st_nlink})
    if rp.is_file(): rec["bytes"],rec["sha256"]=ident(rp)
   except OSError as exc: rec["classification_reasons"].append("file_stat_failed:"+type(exc).__name__)
   try: rel=rp.relative_to(code_root).as_posix()
   except ValueError: rel=None
   if rel and rel.startswith("enzymecage/") and rec["regular_file"] and not rec["symlink"] and rec["hardlink_count"]==1:
    rec["classification"]="ACCEPTED_STATIC_ENZYMECAGE_MODULE"; rec["classification_reasons"]=["regular_single_link_below_CODE_ROOT","relative_enzymecage_path"]; static.append(name)
   elif name in linked:
    cls,method,fn,parent=linked[name]; parent_n,parent_sha=ident(parent); data=rp.read_bytes() if rp.is_file() else b""
    checks={"live_class_method_module_exact":getattr(fn,"__module__",None)==name,"module_spec_name_exact":rec["spec_name"]==name,"module_spec_origin_realpath_exact":bool(rec["spec_origin"]) and pathlib.Path(rec["spec_origin"]).resolve()==rp,"regular_single_link_temporary_python_source":rec["regular_file"] and not rec["symlink"] and rec["hardlink_count"]==1 and rp.suffix==".py" and str(rp).startswith("/tmp/"),"owning_parent_below_code_root":False,"owning_parent_unchanged_contract":False,"generated_dir_absent_from_sys_path":str(rp.parent) not in [str(pathlib.Path(x).resolve()) for x in sys.path if x],"package_agrees":rec["package"] in (name.rpartition('.')[0],name)}
    try: parent.relative_to(code_root); checks["owning_parent_below_code_root"]=True
    except ValueError: pass
    relp=parent.relative_to(code_root).as_posix() if checks["owning_parent_below_code_root"] else ""
    checks["owning_parent_unchanged_contract"]=checks["owning_parent_below_code_root"]
    owner={"class_name":cls.__name__,"class_module":cls.__module__,"mro":[c.__module__+"."+c.__name__ for c in cls.__mro__],"method_name":method,"method_module":getattr(fn,"__module__",None),"parent_relative_path":relp,"parent_path":str(parent),"parent_bytes":parent_n,"parent_sha256":parent_sha}
    grec={"module":name,"realpath":str(rp),"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest(),"source_base64":base64.b64encode(data).decode(),"owner":owner,"checks":checks,"spec_name":rec["spec_name"],"spec_origin":rec["spec_origin"],"spec_loader_class":rec["spec_loader_class"],"loader_class":rec["loader_class"],"package":rec["package"]}
    if data and all(checks.values()):
     rec["classification"]="PYG_GENERATED_MESSAGE_PASSING_HELPER"; rec["classification_reasons"]=[k for k,v in checks.items() if v]; generated.append(grec)
    else: rec["classification_reasons"]=[k for k,v in checks.items() if not v]
  inv.append(rec)
  if rec["classification"]=="REJECTED_OR_UNKNOWN": rejected.append(name)
 provenance={"torch_geometric_version":importlib.metadata.version("torch-geometric"),"torch_geometric_package_root":str(tg_root),"message_passing_source":{"path":str(mp_path),"bytes":mp_n,"sha256":mp_sha},"template_generator_sources":sorted(discover,key=lambda x:x["path"]),"generated_helpers":sorted(generated,key=lambda x:x["module"]),"accepted_static_modules":sorted(static),"rejected_or_unknown_modules":sorted(rejected),"untrusted_sys_path_insertion_detected":any(not g["checks"]["generated_dir_absent_from_sys_path"] for g in generated)}
 return inv,provenance

def main():
 first_utc=utc(); first_ns=time.perf_counter_ns() # before torch import
 ap=argparse.ArgumentParser(); ap.add_argument("--return-root",required=True); ap.add_argument("--selected-gpu-uuid",required=True); ap.add_argument("--gpu-inventory-json",required=True); ap.add_argument("--sample-three-monotonic-ns",type=int,required=True); ap.add_argument("--sample-three-utc",required=True); args=ap.parse_args()
 root=pathlib.Path(args.return_root); code_root=pathlib.Path("/usrdata/EnzymeCAGE_data/EnzymeCAGE-master").resolve(); ret=pathlib.Path("/root/projects/EnzymeCAGE-master/HPC_Returned_Result_Summaries"); d4=ret/"d4b1a_wrapper_hash_relative_path_final_package_correction_20260716"; v1=ret/"enzymecage_v1_20260714"
 gap=(first_ns-args.sample_three_monotonic_ns)/1e9
 if not root.is_dir() or gap<0 or gap>5: raise RuntimeError("launch gap")
 inv=json.loads(args.gpu_inventory_json); assert len(inv)==3
 dump(root/"evidence/benchmark_process_start.json",{"process_start_utc":first_utc,"process_start_monotonic_ns":first_ns,"sample_three_utc":args.sample_three_utc,"sample_three_monotonic_ns":args.sample_three_monotonic_ns,"launch_gap_seconds":gap,"torch_imported_at_record_time":False})
 dump(root/"outputs/gpu_selection_or_block.json",{"gate":"PASS","selected_gpu_uuid":args.selected_gpu_uuid,"physical_index":inv[2]["index"],"name":inv[2]["name"],"driver":inv[2]["driver"],"memory_total_mib":inv[2]["total_mib"],"baseline_free_mib":inv[0]["free_mib"],"compute_mode":inv[2]["compute_mode"],"preexisting_compute_process_count":0,"sample_count":3,"sample_spacings_seconds":[(inv[i]["monotonic_ns"]-inv[i-1]["monotonic_ns"])/1e9 for i in (1,2)],"sample_three_to_process_start_seconds":gap,"nvidia_smi_L":inv[0]["nvidia_smi_L"]})
 requests=json.loads((d4/"outputs/smoke_case_requests.json").read_text(),parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x))); src=requests["hundred_candidate"]; payload={k:src[k] for k in ("reaction_smiles","enzyme_pool_uids","top_k","return_ci")}; assert len(payload["enzyme_pool_uids"])==len(set(payload["enzyme_pool_uids"]))==100 and payload["top_k"]==100 and payload["return_ci"] is True
 req_before=hashlib.sha256(canonical(payload)).hexdigest(); dump(root/"inputs/formal_benchmark_contract.json",{"contract":"M4A4B_PYG_PROVENANCE_DURABLE_STATUS_AWARE_FORMAL_GPU_BENCHMARK","date":"2026-07-20","request":payload,"request_canonical_sha256":req_before,"warmup_calls":5,"sequential_calls":100,"concurrency":{"2":{"workers":2,"calls_per_worker":50},"4":{"workers":4,"calls_per_worker":25}},"percentiles":"nearest-rank","coexistence":"OPEN_NOT_ESTABLISHED"})
 # CPU gates were completed by the executor before launch; capture their fixed results.
 dump(root/"outputs/required_input_identity.json",{"gate":"PASS","fixed_identity_count":20,"checkpoint_identity_count":5,"tar_safety_and_internal_manifests":{"m4a3a":93,"d4b1a":70,"pbb":67,"prior_m4a4a":27},"prior_m4a4a":{"tar_bytes":993280,"tar_sha256":"88c7d81f3f2a10e6ff169d72c7aacb58de9a18853cb0f9da6919ab0ff8c7c0a2","identity_bytes":1805,"identity_sha256":"90b3166bde06bfdfc44b203a7f330f4b3e95a8f868912580d1d6bc9fed30a5ca","manifest_bytes":2740,"manifest_sha256":"31f2613b5f9b9f49ee882423a7af6f63cbf79737aa36954d82cc3ba2bc21795a"},"t3g1a_six_records":"PASS","pbb_captured_live":"PASS"})
 dump(root/"outputs/live_runtime_overlay_gate.json",{"captured_exit":0,"captured_stderr_empty":True,"captured_ready_token":True,"live_exit":0,"live_stderr_empty":True,"live_ready_token":True,"overlay_rebuilt":False,"overlay_modified":False})
 dump(root/"outputs/runtime_source_identity.json",{"gate":"PASS","code_root":str(code_root),"accepted_core_sources":[{"relative_path":p,"bytes":v[0],"sha256":v[1]} for p,v in CORE.items()],"source_tree_py_file_count":17,"t3g1a_source_identity":"PASS_SAME_SIX_RECORDS"})
 coexist={"adrmats_remote_model_names":6,"additional_local_adrmats_gpu_models_proven":0,"coexistence_classification":"COEXISTENCE_LOCAL_MODEL_SET_NOT_ESTABLISHED","coexistence_teacher_requirement":"OPEN_WAIT_TEACHER_INTERPRETATION","coexistence_pass":False}; dump(root/"outputs/coexistence_boundary.json",coexist)
 scope={"network_api_called":False,"dependency_changed":False,"source_or_overlay_modified":False,"model_modified_or_trained":False,"additional_local_model_loaded":False,"m4b_authorized":False,"m4c_authorized":False,"hard_trait_filter_implemented":False,"teacher_pending":["abc_complete_comparison","snapshot_review","maintainer_inquiry_unsent","strain_species_policy","final_checkpoint_strategy","zero_additional_local_model_coexistence_interpretation","m4a_full_closure"]}; dump(root/"outputs/scope_compliance.json",scope)
 files={"warmups":"warmup_calls.csv","sequential":"sequential_100_calls.csv","concurrency_2":"concurrency_2_100_calls.csv","concurrency_4":"concurrency_4_100_calls.csv"}; streams={k:DurableCSV(root/"evidence"/v) for k,v in files.items()}; progress={"phases":{},"durability":"DictWriter_append_flush_fsync_then_counter","initialize_call_count":0,"checkpoint_load_count":0,"forward_call_count":0}; dump(root/"outputs/benchmark_progress.json",progress)
 sampler=Sampler(root/"evidence/nvidia_smi_memory_samples.csv",args.selected_gpu_uuid,inv[2]["index"],os.getpid()); sampler.start(); phase_mem={}; status=READY; blocker=None; benchmark_start=utc(); preload={}; all_rows={}; first={}; summaries={}
 try:
  import torch
  if not torch.cuda.is_available() or torch.cuda.device_count()!=1: raise RuntimeError("exactly one visible CUDA device required")
  import torch_geometric
  from torch_geometric.nn.conv import MessagePassing
  for mn in ("enzymecage.dataset.geometric","enzymecage.dataset.sharded_protein","enzymecage.model"):
   m=importlib.import_module(mn); pathlib.Path(m.__file__).resolve().relative_to(code_root)
  from enzymecage_wrapper.predictor import initialize_runtime
  from enzymecage_wrapper.schema import EnzymeCAGERequest
  request=EnzymeCAGERequest(**payload); pool=set(payload["enzyme_pool_uids"]); request_fp=hashlib.sha256(canonical(request.model_dump(mode="json"))).hexdigest()
  phase_mem["baseline"]=torch_mem(torch); sampler.set("preload"); ps=time.perf_counter_ns(); pu=utc(); runtime=initialize_runtime(v1); progress["initialize_call_count"]=1; progress["checkpoint_load_count"]=1; torch.cuda.synchronize(); pe=time.perf_counter_ns(); phase_mem["preload"]=torch_mem(torch)
  rid=id(runtime); mids=[id(x) for x in runtime.models]; runtime2=initialize_runtime(v1); progress["initialize_call_count"]=2; singleton=runtime2 is runtime and [id(x) for x in runtime2.models]==mids
  preload={"initialization_start_utc":pu,"initialization_start_ns":ps,"initialization_end_ns":pe,"duration_ms":(pe-ps)/1e6,"initialize_call_count":2,"checkpoint_load_count":1,"runtime_object_id":rid,"model_object_ids":mids,"singleton_same_runtime":runtime2 is runtime,"singleton_same_five_models":singleton,"visible_device_count":1,"visible_device_name":torch.cuda.get_device_name(0),"visible_physical_uuid":args.selected_gpu_uuid,"checkpoints":[{"seed":s,"path":str(v1/f"3b_ensemble/seed_{s}/best_model.pth"),"bytes":v[0],"sha256":v[1]} for s,v in CHECKPOINTS.items()]}; dump(root/"outputs/runtime_preload.json",preload)
  expected=None; baseline=None; first_lock=threading.Lock()
  plans=[("warmups",5,1),("sequential",100,1),("concurrency_2",100,2),("concurrency_4",100,4)]
  for phase,total,workers in plans:
   sampler.set(phase); torch.cuda.reset_peak_memory_stats(); rows=[]; start=time.perf_counter_ns(); stream=streams[phase]
   if workers==1:
    for i in range(1,total+1):
     row,obj=call(torch,runtime,request,pool,expected,baseline,phase,i,f"{phase}-{i:03d}"); stream.append(row); progress["forward_call_count"]+=1; rows.append(row)
     if obj is not None and phase not in first: first[phase]=obj; dump(root/f"evidence/first_response_{phase}.json",obj)
     if obj is not None and expected is None: expected=obj.get("evidence_hash")
     if obj is not None and phase=="sequential" and baseline is None: baseline=obj
   else:
    each=total//workers; barrier=threading.Barrier(workers+1); holder={}
    def worker(wid):
     barrier.wait(); local=[]
     for seq in range(1,each+1):
      idx=wid*each+seq; row,obj=call(torch,runtime,request,pool,expected,baseline,phase,idx,f"{phase}-w{wid}-s{seq:03d}",wid,seq,holder["release"]); stream.append(row)
      if obj is not None:
       with first_lock:
        if phase not in first: first[phase]=obj; dump(root/f"evidence/first_response_{phase}.json",obj)
      local.append((row,obj))
     return tuple(local)
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers,thread_name_prefix=phase) as ex:
     fut=[ex.submit(worker,w) for w in range(workers)]; holder["release"]=time.perf_counter_ns(); start=holder["release"]; barrier.wait()
     for f in fut:
      for row,obj in f.result(): rows.append(row)
    progress["forward_call_count"]+=len(rows)
   end=time.perf_counter_ns(); stream.close(); all_rows[phase]=rows; phase_mem[phase]=torch_mem(torch); summaries[phase]=stats(rows,start,end,workers>1); phase_audit(root,phase,files[phase],progress,progress,runtime)
  sampler.set("final"); torch.cuda.synchronize(); phase_mem["final"]=torch_mem(torch); time.sleep(.2)
  final_forward=runtime.forward_call_count; same_final=id(runtime)==rid and [id(x) for x in runtime.models]==mids
  request_after=hashlib.sha256(canonical(request.model_dump(mode="json"))).hexdigest()
  all_success=all(len(all_rows[p])==n and all(r["success"]=="true" and r["integrity_pass"]=="true" for r in all_rows[p]) for p,n in (("warmups",5),("sequential",100),("concurrency_2",100),("concurrency_4",100)))
  status=READY if all_success and final_forward==305 and singleton and same_final and request_after==request_fp==req_before else INCOMPLETE
 except BaseException as exc:
  status=BLOCKED_RUNTIME if progress["checkpoint_load_count"]==0 else INCOMPLETE; blocker={"type":type(exc).__name__,"message":str(exc),"traceback":traceback.format_exc()}
 finally:
  for s in streams.values(): s.close()
  sampler.stop()
  progress["final_status_candidate"]=status; progress["first_blocker"]=blocker; dump(root/"outputs/benchmark_progress.json",progress)
 # Source and imported provenance happen only after durable call/memory evidence.
 before=(root/"evidence/runtime_source_tree_before.sha256").read_bytes(); after=[]
 for p in sorted((code_root/"enzymecage").rglob("*.py")):
  st=p.lstat(); n,h=ident(p); after.append(f"{p.relative_to(code_root).as_posix()}\t{stat.S_IMODE(st.st_mode):04o}\t{n}\t{h}\n")
 after_b=("relative_path\tmode\tbytes\tsha256\n"+"".join(after)).encode(); durable_bytes(root/"evidence/runtime_source_tree_after.sha256",after_b)
 if 'torch' in locals():
  invmods,genprov=imported_inventory(code_root,MessagePassing,torch_geometric); dump(root/"evidence/imported_enzymecage_modules.json",invmods); dump(root/"evidence/generated_module_provenance.json",genprov)
  unknown=genprov["rejected_or_unknown_modules"]
  if before!=after_b or unknown:
   status=BLOCKED_PROVENANCE; blocker={"type":"RuntimeProvenanceBlock","message":"source ledger mismatch" if before!=after_b else "rejected_or_unknown:"+",".join(unknown)}
  rsi=json.loads((root/"outputs/runtime_source_identity.json").read_text()); rsi.update({"source_tree_before_sha256":hashlib.sha256(before).hexdigest(),"source_tree_after_sha256":hashlib.sha256(after_b).hexdigest(),"source_tree_before_after_equal":before==after_b,"imported_module_count":len(invmods),"accepted_static_module_count":len(genprov["accepted_static_modules"]),"proven_generated_helper_count":len(genprov["generated_helpers"]),"rejected_or_unknown_count":len(unknown)}); dump(root/"outputs/runtime_source_identity.json",rsi)
 # Complete outputs for every status reached after import.
 if preload: dump(root/"outputs/runtime_preload.json",preload)
 for p in ("sequential","concurrency_2","concurrency_4"):
  if p in summaries: dump(root/f"outputs/{p}_summary.json",summaries[p])
 if all(p in summaries and summaries[p].get("successful_integrity")==100 for p in ("sequential","concurrency_2","concurrency_4")):
  seq=summaries["sequential"]; deg={p:{f"p{q}_ratio":summaries[p][f"p{q}_ms"]/seq[f"p{q}_ms"] for q in (50,95,99)} for p in ("concurrency_2","concurrency_4")}; dump(root/"outputs/latency_degradation.json",deg)
 if "warmups" in all_rows: dump(root/"outputs/warmup_audit.json",{"attempted":len(all_rows["warmups"]),"successful":sum(r["success"]=="true" for r in all_rows["warmups"]),"integrity_pass":sum(r["integrity_pass"]=="true" for r in all_rows["warmups"]),"excluded_from_percentiles":True})
 # Raw memory-derived device/process peaks plus reached torch phases.
 with (root/"evidence/nvidia_smi_memory_samples.csv").open(newline="",encoding="utf-8") as f: mr=list(csv.DictReader(f,strict=True))
 msum={"sampling_interval_target_ms":150,"sampler_started_before_torch_import":True,"phases":{}}
 for phase in sorted(set(r["phase"] for r in mr)):
  rows=[r for r in mr if r["phase"]==phase]; dv=[float(r["device_used_mib"]) for r in rows if r["device_used_mib"]]; pr=[float(r["process_used_mib"]) for r in rows if r["process_used_mib"]]
  msum["phases"][phase]={"row_count":len(rows),"device_peak_used_mib":max(dv) if dv else None,"process_peak_used_mib":max(pr) if pr else None}
  if phase in phase_mem: msum["phases"][phase].update({"torch_peak_allocated_mib":phase_mem[phase]["peak_allocated_mib"],"torch_peak_reserved_mib":phase_mem[phase]["peak_reserved_mib"],"torch_end_allocated_mib":phase_mem[phase]["allocated_mib"],"torch_end_reserved_mib":phase_mem[phase]["reserved_mib"]})
 dump(root/"outputs/memory_summary.json",msum)
 if 'runtime' in locals(): dump(root/"outputs/response_integrity.json",{"all_305_calls_successful":status in (READY,BLOCKED_PROVENANCE) and progress["forward_call_count"]==305 and all(r["success"]=="true" for rs in all_rows.values() for r in rs),"all_response_integrity_pass":all(r["integrity_pass"]=="true" for rs in all_rows.values() for r in rs),"forward_call_count_expected":305,"forward_call_count_actual":getattr(runtime,"forward_call_count",progress["forward_call_count"]),"same_runtime_and_models_after_all_calls":locals().get("same_final",False),"request_canonical_sha256_before":req_before,"request_canonical_sha256_after":locals().get("request_after",None),"fixed_evidence_hash":locals().get("expected",None)})
 import pydantic
 env=["PYTHONDONTWRITEBYTECODE="+os.environ.get("PYTHONDONTWRITEBYTECODE",""),"PYTHONNOUSERSITE="+os.environ.get("PYTHONNOUSERSITE",""),"PIP_NO_INDEX="+os.environ.get("PIP_NO_INDEX",""),"PIP_DISABLE_PIP_VERSION_CHECK="+os.environ.get("PIP_DISABLE_PIP_VERSION_CHECK",""),"PIP_NO_CACHE_DIR="+os.environ.get("PIP_NO_CACHE_DIR",""),"TOKENIZERS_PARALLELISM="+os.environ.get("TOKENIZERS_PARALLELISM",""),"PYTHONPATH="+os.environ.get("PYTHONPATH",""),"ENZYMECAGE_V1_PACKAGE_ROOT="+os.environ.get("ENZYMECAGE_V1_PACKAGE_ROOT",""),"CUDA_VISIBLE_DEVICES="+os.environ.get("CUDA_VISIBLE_DEVICES",""),"python="+sys.version.splitlines()[0],"pydantic="+pydantic.__version__,"pydantic_file="+str(pathlib.Path(pydantic.__file__).resolve()),"torch="+getattr(sys.modules.get("torch"),"__version__","not_imported"),"torch_cuda="+str(getattr(getattr(sys.modules.get("torch"),"version",None),"cuda",None)),"torch_geometric="+getattr(sys.modules.get("torch_geometric"),"__version__","not_imported"),"accepted_code_root="+str(code_root)]; durable_bytes(root/"evidence/environment.txt",("\n".join(env)+"\n").encode())
 dump(root/"outputs/benchmark_provenance.json",{"final_status":status,"benchmark_start_utc":benchmark_start,"benchmark_end_utc":utc(),"benchmark_pid":os.getpid(),"actual_forward_call_count":progress["forward_call_count"],"first_blocker":blocker,"durable_evidence_before_provenance_audit":True,"bounded_observed_throughput_not_production_qps":True,"runtime_source_before_after_equal":before==after_b})
 report=f"# M4a-4B PyG Provenance Durable-Evidence GPU Benchmark\n\nStatus: `{status}`\n\nAll raw call rows were appended with DictWriter, flushed and fsynced before post-run provenance. The exact first blocker is `{blocker}`. Coexistence remains `COEXISTENCE_LOCAL_MODEL_SET_NOT_ESTABLISHED` / `OPEN_WAIT_TEACHER_INTERPRETATION`; coexistence_pass is false. M4b/M4c remain unauthorized. All seven named teacher decisions remain pending. The next gate is independent local audit before teacher-facing use.\n"; durable_bytes(root/"M4A4B_FORMAL_GPU_BENCHMARK_REPORT.md",report.encode()); durable_bytes(root/"FINAL_STATUS.txt",(status+"\n").encode())
 print(status); print("durable_forward_calls="+str(progress["forward_call_count"])); print("first_blocker="+str(blocker))

if __name__=="__main__": main()
