#!/usr/bin/env python3
"""Execute all inherited and M4a-4BAAA negative tests on temporary copies."""
import argparse, csv, hashlib, importlib.util, json, os, pathlib, shutil, stat, subprocess, sys, tempfile
sys.dont_write_bytecode=True

def ident(p):
 b=pathlib.Path(p).read_bytes(); return len(b),hashlib.sha256(b).hexdigest()
def load(p): return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))
def dump(p,x): pathlib.Path(p).write_text(json.dumps(x,indent=2,sort_keys=True,ensure_ascii=False,allow_nan=True)+"\n",encoding="utf-8")
def tree_identity(root):
 root=pathlib.Path(root); rows=[]
 for p in [root]+sorted(root.rglob("*"),key=lambda x:x.relative_to(root).as_posix()):
  st=p.lstat(); rel="." if p==root else p.relative_to(root).as_posix(); mode=stat.S_IMODE(st.st_mode)
  if stat.S_ISDIR(st.st_mode): rows.append((rel,"directory",mode,0,""))
  elif stat.S_ISREG(st.st_mode): rows.append((rel,"regular_file",mode,*ident(p)))
  elif stat.S_ISLNK(st.st_mode): rows.append((rel,"symlink",mode,0,os.readlink(p)))
  else: rows.append((rel,"other",mode,st.st_size,""))
 return {"entry_count":len(rows),"sha256":hashlib.sha256(json.dumps(rows,separators=(",",":")).encode()).hexdigest()}
def write_csv(p,header,rows):
 with pathlib.Path(p).open("w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=header,lineterminator="\n"); w.writeheader(); w.writerows(rows)
def mutate_csv(p,fn):
 with pathlib.Path(p).open(newline="",encoding="utf-8") as f: rd=csv.DictReader(f,strict=True); header=rd.fieldnames; rows=list(rd)
 fn(rows); write_csv(p,header,rows)

def refresh_dependencies(root,changed,include_manifest=False):
 root=pathlib.Path(root); changed=set(changed)
 raw={"evidence/warmup_calls.csv":"warmups","evidence/sequential_100_calls.csv":"sequential","evidence/concurrency_2_100_calls.csv":"concurrency_2","evidence/concurrency_4_100_calls.csv":"concurrency_4"}
 if changed & set(raw) and (root/"outputs/benchmark_progress.json").exists():
  q=load(root/"outputs/benchmark_progress.json")
  for rel,phase in raw.items():
   if rel in changed and phase in q.get("phases",{}): q["phases"][phase]["bytes"],q["phases"][phase]["sha256"]=ident(root/rel)
  dump(root/"outputs/benchmark_progress.json",q); changed.add("outputs/benchmark_progress.json")
 b=root/"evidence/inherited_m4a4b_file_identity.json"
 if b.exists():
  x=load(b); touched=False
  for q in x.get("files",[]):
   rel=q["path"]
   if rel in changed and rel!="MANIFEST.sha256" and (root/rel).exists():
    n,h=ident(root/rel); q["new_bytes"],q["new_sha256"]=n,h
    if q.get("classification")=="immutable": q["prior_bytes"],q["prior_sha256"]=n,h
    touched=True
  if touched: dump(b,x); changed.add("evidence/inherited_m4a4b_file_identity.json")
 ba=root/"evidence/inherited_m4a4ba_file_identity.json"
 if ba.exists():
  x=load(ba); touched=False
  for q in x.get("files",[]):
   rel=q["path"]
   if rel in changed and rel!="MANIFEST.sha256" and (root/rel).exists():
    n,h=ident(root/rel); q["new_bytes"],q["new_sha256"]=n,h
    if q.get("classification")=="immutable": q["prior_bytes"],q["prior_sha256"]=n,h
    touched=True
  if touched: dump(ba,x); changed.add("evidence/inherited_m4a4ba_file_identity.json")
 baaa=root/"evidence/inherited_m4a4baa_file_identity.json"
 if baaa.exists():
  x=load(baaa); touched=False
  for q in x.get("files",[]):
   rel=q["path"]
   if rel in changed and rel!="MANIFEST.sha256" and (root/rel).exists():
    n,h=ident(root/rel); q["new_bytes"],q["new_sha256"]=n,h
    if q.get("classification")=="immutable": q["prior_bytes"],q["prior_sha256"]=n,h
    touched=True
  if touched: dump(baaa,x)
 if include_manifest and (root/"MANIFEST.sha256").exists():
  files=sorted(p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file() and p.name!="MANIFEST.sha256")
  (root/"MANIFEST.sha256").write_text("".join(ident(root/r)[1]+"  "+r+"\n" for r in files),encoding="utf-8")

def mutate(module,test_id,root):
 root=pathlib.Path(root); changed=[]; phase="evidence"
 def j(rel,fn):
  x=load(root/rel); fn(x); dump(root/rel,x); changed.append(rel)
 if test_id in {"N01","N02","N03","N04","N05"}:
  rel="evidence/first_response_sequential.json"
  def f(x):
   if test_id=="N01": x["ranked_enzymes"][1]["uid"]=x["ranked_enzymes"][0]["uid"]
   elif test_id=="N02": x["ranked_enzymes"][0]["rank"]=2
   elif test_id=="N03": x["ranked_enzymes"][0]["uid"]="OUT_OF_POOL"
   elif test_id=="N04": x["ranked_enzymes"][0]["score"]=float("nan")
   else: x["ranked_enzymes"][0]["ensemble_ci"]=[0.1]
  j(rel,f)
 elif test_id in {"N06","N07","N08","N09","N10","N11","N12"}:
  rel="evidence/sequential_100_calls.csv"
  if test_id=="N10": rel="evidence/warmup_calls.csv"
  if test_id in {"N11","N12"}: rel="evidence/concurrency_2_100_calls.csv"
  def f(rows):
   if test_id=="N06": rows[0]["uid_order_sha256"]="f"*64
   elif test_id=="N07": rows[0]["evidence_hash"]="f"*64
   elif test_id=="N08": rows[0]["global_request_id"]="warmups-001"
   elif test_id=="N09": rows[0]["global_request_id"]="bad id"
   elif test_id=="N10": rows[0]["call_index"]="2"
   elif test_id=="N11": rows[0]["worker_sequence"]="2"
   else: rows[0]["barrier_release_ns"]=str(int(rows[0]["barrier_release_ns"])+1)
  mutate_csv(root/rel,f); changed.append(rel)
 elif test_id=="N13": j("outputs/sequential_summary.json",lambda x:x.__setitem__("p95_ms",x["p95_ms"]+1))
 elif test_id=="N14": j("outputs/latency_degradation.json",lambda x:x["concurrency_2"].__setitem__("p95_ratio",0))
 elif test_id=="N15": j("evidence/fixed_input_identity_ledger.json",lambda x:x["items"][0].__setitem__("expected_sha256","0"*64))
 elif test_id in {"N16","N17","N18","N19","N20","N21"}:
  def f(x):
   if test_id=="N16": x["generated_helpers"][0]["realpath"]="/outside/helper.py"
   elif test_id=="N17": x["generated_helpers"][0]["owner"]["method_module"]="wrong.module"
   elif test_id=="N18": x["generated_helpers"][0]["owner"]["parent_sha256"]="0"*64
   elif test_id=="N19": x["torch_geometric_version"]="0.0.0"
   elif test_id=="N20": x["torch_geometric_package_root"]="/outside"
   else: x["template_generator_sources"][0]["sha256"]="0"*64
  j("evidence/generated_module_provenance.json",f)
 elif test_id in {"N22","N23","N24","N25"}:
  def f(x):
   if test_id=="N22": x["phases"]["sequential"]["torch_peak_allocated_mib"]=-1
   elif test_id=="N23": x["phases"]["sequential"]["torch_peak_allocated_mib"]="not-a-number"
   elif test_id=="N24": x["phases"]["sequential"]["torch_peak_allocated_mib"]=0
   else: del x["phases"]["final"]
  j("outputs/memory_summary.json",f)
 elif test_id=="N26":
  mutate_csv(root/"evidence/nvidia_smi_memory_samples.csv",lambda rows:rows[0].__setitem__("process_query_status","invalid")); changed.append("evidence/nvidia_smi_memory_samples.csv")
 elif test_id=="N27":
  module.build_status_fixture(root,module.BLOCKED_PROVENANCE,root.parent/"bootstrap/validate_m4a4b_formal_gpu_benchmark.py")
  (root/"evidence/runtime_source_tree_after.sha256").write_bytes((root/"evidence/runtime_source_tree_before.sha256").read_bytes()); dump(root/"evidence/imported_enzymecage_modules.json",[])
 elif test_id=="N28": j("evidence/imported_enzymecage_modules.json",lambda x:x[0].__setitem__("classification","REJECTED_OR_UNKNOWN"))
 elif test_id in {"N29","N30","N31"}:
  status={"N29":module.BLOCKED_GPU,"N30":module.BLOCKED_RUNTIME,"N31":module.BLOCKED_PACKAGING}[test_id]; module.build_status_fixture(root,status,root.parent/"bootstrap/validate_m4a4b_formal_gpu_benchmark.py",root.parent/"ready" if test_id=="N31" else None)
  if test_id=="N29": (root/"evidence/nvidia_smi_memory_samples.csv").write_text("torch_artifact\n",encoding="utf-8")
  elif test_id=="N30": j("outputs/benchmark_provenance.json",lambda x:x["first_blocker"].pop("traceback"))
  else: j("outputs/benchmark_provenance.json",lambda x:x.__setitem__("first_blocker",None))
 elif test_id=="N32": j("outputs/coexistence_boundary.json",lambda x:x.__setitem__("coexistence_pass",True))
 elif test_id=="N33": j("outputs/scope_compliance.json",lambda x:x.__setitem__("m4b_authorized",True))
 elif test_id=="N34": j("outputs/scope_compliance.json",lambda x:x.__setitem__("m4c_authorized",True))
 elif test_id=="N35": (root/"FINAL_STATUS.txt").write_text("UNKNOWN_STATUS\n",encoding="utf-8")
 elif test_id=="N36": (root/"undeclared.txt").write_text("undeclared\n",encoding="utf-8")
 elif test_id=="N37": (root/"outputs/coexistence_boundary.json").chmod(0o600)
 elif test_id=="N38": (root/"unsafe_link").symlink_to("FINAL_STATUS.txt")
 elif test_id=="N39": (root/"M4A4B_FORMAL_GPU_BENCHMARK_REPORT.md").write_bytes(b"\xff")
 elif test_id=="N40": (root/"empty").mkdir()
 elif test_id=="N41": (root/"M4A4B_FORMAL_GPU_BENCHMARK_REPORT.md").write_text("api_"+"key=THIS_IS_A_FORBIDDEN_SECRET_VALUE\n",encoding="utf-8")
 elif test_id in {"N43","N44"}:
  module.build_status_fixture(root,module.BLOCKED_PROVENANCE,root.parent/"bootstrap/validate_m4a4b_formal_gpu_benchmark.py")
  if test_id=="N43":
   mutate_csv(root/"evidence/warmup_calls.csv",lambda rows:rows.clear()); q=load(root/"outputs/benchmark_progress.json"); n,h=ident(root/"evidence/warmup_calls.csv"); q["phases"]["warmups"].update({"attempted":0,"success":0,"failure":0,"file":{"path":"evidence/warmup_calls.csv","bytes":n,"sha256":h}}); q["forward_call_count"]=0; dump(root/"outputs/benchmark_progress.json",q)
  else: j("evidence/generated_module_provenance.json",lambda x:x.__setitem__("rejected_or_unknown_modules",["enzymecage.different"]))
 elif test_id=="N45":
  module.build_status_fixture(root,module.BLOCKED_GPU,root.parent/"bootstrap/validate_m4a4b_formal_gpu_benchmark.py"); j("outputs/gpu_selection_or_block.json",lambda x:x["blocker"].__setitem__("code","DIFFERENT"))
 elif test_id=="N46":
  module.build_status_fixture(root,module.BLOCKED_RUNTIME,root.parent/"bootstrap/validate_m4a4b_formal_gpu_benchmark.py"); j("outputs/benchmark_progress.json",lambda x:x["first_blocker"].__setitem__("code","DIFFERENT"))
 elif test_id=="N47":
  module.build_status_fixture(root,module.BLOCKED_PACKAGING,root.parent/"bootstrap/validate_m4a4b_formal_gpu_benchmark.py",root.parent/"ready"); mutate_csv(root/"evidence/sequential_100_calls.csv",lambda rows:rows.pop())
 elif test_id=="N48": j("evidence/inherited_m4a4ba_file_identity.json",lambda x:x["files"][[q["path"] for q in x["files"]].index("MANIFEST.sha256")].update({"new_identity_location":"INTERNAL_GUESS","new_bytes":1,"new_sha256":"0"*64}))
 elif test_id in {"N49","N50","N51","N52","N53"}:
  phase="packaged"
  if test_id=="N49": j("outputs/correction_provenance.json",lambda x:x.__setitem__("reverse_packaged_validation","PASS_PRELIMINARY"))
  elif test_id=="N50": mutate_csv(root/"logs/status_fixture_tests.csv",lambda rows:rows[0].__setitem__("result","FAIL")); changed.append("logs/status_fixture_tests.csv")
  elif test_id=="N51":
   for rel in ("logs/validator_negative_tests.csv","logs/m4a4baa_validation_suite.csv"): mutate_csv(root/rel,lambda rows:rows[0].__setitem__("result","FAIL")); changed.append(rel)
  elif test_id=="N52": j("outputs/validator_results.json",lambda x:x.__setitem__("reverse_packaged_validation","FAIL"))
  else: mutate_csv(root/"logs/status_fixture_tests.csv",lambda rows:rows[1].__setitem__("fixture_id",rows[0]["fixture_id"])); changed.append("logs/status_fixture_tests.csv")
  for rel,key in (("logs/status_fixture_tests.csv","positive_csv"),("logs/status_fixture_tests.stdout.txt","positive_stdout"),("logs/validator_negative_tests.csv","negative_csv"),("logs/validator_negative_tests.stdout.txt","negative_stdout")):
   if (root/rel).exists():
    val={"bytes":ident(root/rel)[0],"sha256":ident(root/rel)[1]}
    for out in ("outputs/validator_results.json","outputs/correction_provenance.json"):
     x=load(root/out); x.setdefault("test_evidence_identities",{})[key]=val; dump(root/out,x); changed.append(out)
 elif test_id=="N54":
  module.build_status_fixture(root,module.INCOMPLETE,root.parent/"bootstrap/validate_m4a4b_formal_gpu_benchmark.py")
  mutate_csv(root/"evidence/warmup_calls.csv",lambda rows:rows[0].update({"global_request_id":"bad id","start_utc":"not-utc","latency_ms":"NaN","response_sha256":"ABC"})); n,h=ident(root/"evidence/warmup_calls.csv"); q=load(root/"outputs/benchmark_progress.json"); q["phases"]["warmups"]["file"]={"path":"evidence/warmup_calls.csv","bytes":n,"sha256":h}; dump(root/"outputs/benchmark_progress.json",q)
 elif test_id=="N55":
  module.build_status_fixture(root,module.BLOCKED_PROVENANCE,root.parent/"bootstrap/validate_m4a4b_formal_gpu_benchmark.py")
  mutate_csv(root/"evidence/warmup_calls.csv",lambda rows:rows[0].update({"end_ns":"0","latency_ms":"NaN","response_sha256":"UPPER"})); n,h=ident(root/"evidence/warmup_calls.csv"); q=load(root/"outputs/benchmark_progress.json"); q["phases"]["warmups"]["file"]={"path":"evidence/warmup_calls.csv","bytes":n,"sha256":h}; dump(root/"outputs/benchmark_progress.json",q)
 elif test_id=="N56":
  module.build_status_fixture(root,module.BLOCKED_GPU,root.parent/"bootstrap/validate_m4a4b_formal_gpu_benchmark.py")
  mutate_csv(root/"evidence/gpu_gate_samples.csv",lambda rows:rows[0].update({"gpu_uuid":"","total_mib":"1","used_mib":"9","compute_process_count":"1","compute_process_rows_json":"[]"}))
 elif test_id in {"N57","N58","N65","N66","N67","N68"}:
  phase="packaged"
  if test_id=="N57": (root/"logs/m4a4baa_validation_suite.csv").write_bytes((root/"logs/m4a4baa_validation_suite.csv").read_bytes()+b"\n"); changed.append("logs/m4a4baa_validation_suite.csv")
  elif test_id=="N58":
   p=root/"logs/status_fixture_tests.stdout.txt"; p.write_text(p.read_text().replace("token_count=1","token_count=9",1)); changed.append("logs/status_fixture_tests.stdout.txt")
  elif test_id=="N65": (root/"M4A4BAAA_CORRECTION_REPORT.md").write_text((root/"M4A4BAAA_CORRECTION_REPORT.md").read_text()+"coexistence PASS and M4b authorized and M4a closed\n"); changed.append("M4A4BAAA_CORRECTION_REPORT.md")
  elif test_id=="N66": j("outputs/correction_provenance.json",lambda x:x.__setitem__("coexistence_pass",True))
  elif test_id=="N67": j("outputs/validator_results.json",lambda x:x.update({"actual_status_positive":"FAIL","captured_packaged_validation":"FAIL","validator_status_dispatch":False}))
  else: j("outputs/correction_provenance.json",lambda x:x.update({"positive_status_fixtures":"FAIL","cross_consistent_negative_tests":"FAIL"}))
  for rel,key in (("logs/status_fixture_tests.csv","positive_csv"),("logs/status_fixture_tests.stdout.txt","positive_stdout"),("logs/validator_negative_tests.csv","negative_csv"),("logs/validator_negative_tests.stdout.txt","negative_stdout")):
   val={"bytes":ident(root/rel)[0],"sha256":ident(root/rel)[1]}
   for out in ("outputs/validator_results.json","outputs/correction_provenance.json"):
    x=load(root/out); x["test_evidence_identities"][key]=val; dump(root/out,x); changed.append(out)
 elif test_id in {"N59","N60","N61"}:
  module.build_status_fixture(root,module.BLOCKED_PACKAGING,root.parent/"bootstrap/validate_m4a4b_formal_gpu_benchmark.py",root.parent/"ready")
  if test_id=="N59": j("evidence/fixed_input_identity_ledger.json",lambda x:x.update({"all_pass":False}))
  elif test_id=="N60":
   p=root/"logs/benchmark.stderr.txt"; p.write_text(p.read_text()+"\nTraceback: CUDA out of memory prediction exception\n"); changed.append("logs/benchmark.stderr.txt")
  else: j("evidence/inherited_m4a4ba_file_identity.json",lambda x:x["files"][0].__setitem__("prior_sha256","0"*64))
 elif test_id=="N62":
  module.build_status_fixture(root,module.BLOCKED_PROVENANCE,root.parent/"bootstrap/validate_m4a4b_formal_gpu_benchmark.py")
  (root/"evidence/runtime_source_tree_after.sha256").write_bytes((root/"evidence/runtime_source_tree_before.sha256").read_bytes())
  j("evidence/imported_enzymecage_modules.json",lambda x:x[0].__setitem__("realpath",module.CODE_ROOT+"/enzymecage/model.py"))
 elif test_id=="N63":
  module.build_status_fixture(root,module.BLOCKED_GPU,root.parent/"bootstrap/validate_m4a4b_formal_gpu_benchmark.py"); generic={"type":"Fixture","stage":"fixture","message":"generic","code":"GENERIC"}
  for rel,key in (("outputs/benchmark_provenance.json","first_blocker"),("outputs/benchmark_progress.json","first_blocker"),("outputs/gpu_selection_or_block.json","blocker")): j(rel,lambda x,k=key:x.__setitem__(k,generic))
 elif test_id=="N64":
  module.build_status_fixture(root,module.INCOMPLETE,root.parent/"bootstrap/validate_m4a4b_formal_gpu_benchmark.py"); generic={"type":"Fixture","stage":"fixture","message":"generic","code":"GENERIC"}; j("outputs/benchmark_provenance.json",lambda x:x.__setitem__("first_blocker",generic)); j("outputs/benchmark_progress.json",lambda x:x.__setitem__("first_blocker",generic))
 refresh_dependencies(root,changed,include_manifest=phase=="packaged")
 return phase

def reason(stdout):
 for line in stdout.splitlines():
  if line.startswith("M4A4BA_VALIDATION_ERROR:"): return line.split(":",2)[1]
 return "missing_stable_reason"

def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--package-root",required=True); ap.add_argument("--output-csv",required=True); ap.add_argument("--output-stdout",required=True); args=ap.parse_args()
 source=pathlib.Path(args.package_root).resolve(); outs=[pathlib.Path(args.output_csv).resolve(),pathlib.Path(args.output_stdout).resolve()]
 if any(o==source or source in o.parents for o in outs): raise SystemExit("M4A4BAA_SUITE_ERROR:output_inside_tested_tree")
 before=tree_identity(source); rows=[]; transcript=[]
 with tempfile.TemporaryDirectory(prefix="m4a4baa_negative_") as td:
  base=pathlib.Path(td); bootstrap=base/"bootstrap"; bootstrap.mkdir(); validator=bootstrap/"validate_m4a4b_formal_gpu_benchmark.py"; shutil.copy2(source/"scripts/validate_m4a4b_formal_gpu_benchmark.py",validator)
  spec=importlib.util.spec_from_file_location("m4a4baa_validator_bootstrap",validator); module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
  shutil.copytree(source,base/"ready",copy_function=shutil.copy2)
  for tid,mutation,expected in module.NEGATIVE_CASES:
   if tid=="N42":
    fixture=base/tid; module.build_status_fixture(fixture,module.READY,validator,source); prior=tree_identity(fixture); env=os.environ.copy(); env.pop("PYTHONDONTWRITEBYTECODE",None); cp0=subprocess.run([sys.executable,str(source/"evidence/prior_m4a4ba_status_fixture_runner.py"),"--package-root",str(fixture),"--output-csv",str(base/(tid+".csv")),"--output-stdout",str(base/(tid+".txt"))],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,check=False,env=env); post=tree_identity(fixture); observed="source_tree_changed" if prior!=post else "source_tree_unchanged"; cp=subprocess.CompletedProcess(cp0.args,1 if prior!=post else 0,"M4A4BA_VALIDATION_ERROR:"+observed+"\n","")
   else:
    fixture=base/tid
    if tid in {"N27","N29","N30","N43","N44","N45","N46","N54","N55","N56","N62","N63","N64"}: fixture.mkdir()
    elif tid in {"N31","N47","N59","N60","N61"}: pass
    elif tid in {"N49","N50","N51","N52","N53","N57","N58","N65","N66","N67","N68"}: shutil.copytree(source,fixture,copy_function=shutil.copy2)
    else: module.build_status_fixture(fixture,module.READY,validator,source)
    phase=mutate(module,tid,fixture); env=os.environ.copy(); env["PYTHONDONTWRITEBYTECODE"]="1"
    cp=subprocess.run([sys.executable,str(validator),str(fixture),"--validation-phase",phase,"--runtime-evidence-mode","captured"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,check=False,env=env); observed=reason(cp.stdout)
   passed=cp.returncode==1 and cp.stderr=="" and observed==expected
   row={"test_id":tid,"mutation":mutation,"expected_reason":expected,"exit_code":str(cp.returncode),"observed_reason":observed,"stderr_empty":str(cp.stderr=="").lower(),"dependencies_updated":"true","result":"PASS" if passed else "FAIL"}; rows.append(row)
   transcript.append("{test_id}\tmutation={mutation}\texit={exit_code}\texpected={expected_reason}\tobserved={observed_reason}\tstderr_empty={stderr_empty}\tdependencies_updated={dependencies_updated}\tresult={result}\n".format(**row)+cp.stdout)
   if not passed: raise RuntimeError("negative_failed:"+tid+":"+observed+":"+cp.stdout+":"+cp.stderr)
 after=tree_identity(source)
 if before!=after: raise RuntimeError("source_tree_changed")
 for o in outs: o.parent.mkdir(parents=True,exist_ok=True)
 write_csv(outs[0],list(rows[0]),rows); outs[1].write_text("source_tree_before="+json.dumps(before,sort_keys=True,separators=(",",":"))+"\nsource_tree_after="+json.dumps(after,sort_keys=True,separators=(",",":"))+"\n"+"".join(transcript)+"summary=%d/%d_PASS\n"%(len(rows),len(rows)),encoding="utf-8")
 print("M4A4BAA_NEGATIVE_TESTS_%d_OF_%d_PASS"%(len(rows),len(rows)))
if __name__=="__main__": main()
