#!/usr/bin/env python3
"""Execute the six exact M4a-4BAA positive status fixtures without side effects."""
import argparse, csv, hashlib, importlib.util, json, os, pathlib, shutil, stat, subprocess, sys, tempfile

sys.dont_write_bytecode = True

def tree_identity(root):
 root=pathlib.Path(root); rows=[]
 for p in [root]+sorted(root.rglob("*"),key=lambda x:x.relative_to(root).as_posix()):
  st=p.lstat(); rel="." if p==root else p.relative_to(root).as_posix(); mode=stat.S_IMODE(st.st_mode)
  if stat.S_ISDIR(st.st_mode): rows.append((rel,"directory",mode,0,""))
  elif stat.S_ISREG(st.st_mode):
   data=p.read_bytes(); rows.append((rel,"regular_file",mode,len(data),hashlib.sha256(data).hexdigest()))
  elif stat.S_ISLNK(st.st_mode): rows.append((rel,"symlink",mode,0,os.readlink(p)))
  else: rows.append((rel,"other",mode,st.st_size,""))
 blob=json.dumps(rows,separators=(",",":"),ensure_ascii=False).encode()
 return {"entry_count":len(rows),"sha256":hashlib.sha256(blob).hexdigest()}

def load_json(p): return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))

def defining_condition(module,status,fixture):
 p=load_json(fixture/"outputs/benchmark_provenance.json")
 if p.get("final_status")!=status: return False
 if status==module.READY: return p.get("first_blocker") is None
 if status==module.INCOMPLETE:
  q=load_json(fixture/"outputs/benchmark_progress.json"); return q["phases"]["warmups"]["failure"]==1
 if status==module.BLOCKED_GPU:
  g=load_json(fixture/"outputs/gpu_selection_or_block.json"); s=load_json(fixture/"evidence/benchmark_process_start.json"); return g["observed_min_free_mib"]<g["minimum_free_mib"] and all(s[k] is False for k in ("launched","torch_imported","model_initialized","checkpoint_loaded","prediction_executed"))
 if status==module.BLOCKED_RUNTIME:
  q=load_json(fixture/"outputs/benchmark_progress.json"); return str(p["first_blocker"]["traceback"]).startswith("Traceback") and (q["initialize_call_count"],q["checkpoint_load_count"],q["forward_call_count"])==(1,0,0)
 if status==module.BLOCKED_PROVENANCE:
  q=load_json(fixture/"outputs/benchmark_progress.json"); gp=load_json(fixture/"evidence/generated_module_provenance.json"); return sum(x["attempted"] for x in q["phases"].values())>=1 and gp["rejected_or_unknown_modules"]==p["first_blocker"]["rejected_modules"]
 if status==module.BLOCKED_PACKAGING:
  q=load_json(fixture/"outputs/benchmark_progress.json"); pe=load_json(fixture/"outputs/packaging_failure.json"); return q["completed_scientific_calls"]==305 and pe["scientific_evidence_complete"] is True and pe["first_blocker"]==p["first_blocker"]
 return False

def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--package-root",required=True); ap.add_argument("--output-csv",required=True); ap.add_argument("--output-stdout",required=True); args=ap.parse_args()
 root=pathlib.Path(args.package_root).resolve(); out_csv=pathlib.Path(args.output_csv).resolve(); out_stdout=pathlib.Path(args.output_stdout).resolve()
 for out in (out_csv,out_stdout):
  if out==root or root in out.parents: raise SystemExit("M4A4BAA_FIXTURE_ERROR:output_inside_tested_tree")
 before=tree_identity(root); results=[]; transcript=[]
 with tempfile.TemporaryDirectory(prefix="m4a4baa_positive_") as td:
  base=pathlib.Path(td); bootstrap=base/"bootstrap"; bootstrap.mkdir(); validator=bootstrap/"validate_m4a4b_formal_gpu_benchmark.py"; shutil.copy2(root/"scripts/validate_m4a4b_formal_gpu_benchmark.py",validator)
  spec=importlib.util.spec_from_file_location("m4a4baa_validator_bootstrap",validator); module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
  for index,status in enumerate(module.STATUSES,1):
   fixture=base/("fixture_%02d"%index); module.build_status_fixture(fixture,status,validator,root if status in (module.READY,module.BLOCKED_PACKAGING) else None)
   env=os.environ.copy(); env["PYTHONDONTWRITEBYTECODE"]="1"
   cp=subprocess.run([sys.executable,str(fixture/"scripts/validate_m4a4b_formal_gpu_benchmark.py"),str(fixture),"--validation-phase","evidence","--runtime-evidence-mode","captured"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,check=False,env=env)
   token_count=cp.stdout.splitlines().count(status); condition=defining_condition(module,status,fixture); passed=cp.returncode==0 and cp.stderr=="" and token_count==1 and condition
   row={"fixture_id":"F%02d"%index,"status":status,"exit_code":str(cp.returncode),"stderr_empty":str(cp.stderr=="").lower(),"token_count":str(token_count),"defining_condition":"PASS" if condition else "FAIL","result":"PASS" if passed else "FAIL"}; results.append(row)
   transcript.append("{fixture_id}\tstatus={status}\texit={exit_code}\tstderr_empty={stderr_empty}\ttoken_count={token_count}\tdefining_condition={defining_condition}\tresult={result}\n".format(**row)+cp.stdout)
   if not passed: raise RuntimeError("fixture_failed:"+status+":"+cp.stdout+":"+cp.stderr)
 after=tree_identity(root)
 if before!=after: raise RuntimeError("source_tree_changed")
 out_csv.parent.mkdir(parents=True,exist_ok=True); out_stdout.parent.mkdir(parents=True,exist_ok=True)
 with out_csv.open("w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=list(results[0]),lineterminator="\n"); w.writeheader(); w.writerows(results)
 out_stdout.write_text("source_tree_before="+json.dumps(before,sort_keys=True,separators=(",",":"))+"\nsource_tree_after="+json.dumps(after,sort_keys=True,separators=(",",":"))+"\n"+"".join(transcript)+"summary=6/6_PASS\n",encoding="utf-8")
 print("M4A4BAA_STATUS_FIXTURES_6_OF_6_PASS")

if __name__=="__main__": main()
