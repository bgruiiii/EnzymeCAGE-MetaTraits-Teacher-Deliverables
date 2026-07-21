#!/usr/bin/env python3
"""Run six positive status fixtures using the validator's public schema builder."""
import argparse, csv, hashlib, importlib.util, pathlib, subprocess, sys, tempfile
def ident(p): b=pathlib.Path(p).read_bytes(); return hashlib.sha256(b).hexdigest()
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--package-root',required=True); ap.add_argument('--output-csv',required=True); ap.add_argument('--output-stdout',required=True); args=ap.parse_args()
 root=pathlib.Path(args.package_root).resolve(); validator=root/'scripts/validate_m4a4b_formal_gpu_benchmark.py'; before=ident(validator)
 spec=importlib.util.spec_from_file_location('m4a4ba_validator_public_schema',validator); module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
 results=[]; transcript=[]
 with tempfile.TemporaryDirectory(prefix='m4a4ba_status_fixtures_') as td:
  base=pathlib.Path(td)
  for index,status in enumerate(module.STATUSES,1):
   fixture=base/f'fixture_{index}'; module.build_status_fixture(fixture,status,validator,root if status==module.READY else None)
   cp=subprocess.run([sys.executable,str(fixture/'scripts/validate_m4a4b_formal_gpu_benchmark.py'),str(fixture),'--validation-phase','evidence','--runtime-evidence-mode','captured'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,check=False)
   token_count=cp.stdout.splitlines().count(status); passed=cp.returncode==0 and cp.stderr=='' and token_count==1
   results.append({'fixture_id':f'F{index:02d}','status':status,'exit_code':cp.returncode,'stderr_empty':str(not cp.stderr).lower(),'token_count':token_count,'defining_condition':'present','result':'PASS' if passed else 'FAIL'})
   transcript.append(f"F{index:02d}\tstatus={status}\texit={cp.returncode}\tstderr_empty={not cp.stderr}\ttoken_count={token_count}\tresult={'PASS' if passed else 'FAIL'}\n{cp.stdout}")
   if not passed: raise RuntimeError('fixture failed '+status+' stdout='+cp.stdout+' stderr='+cp.stderr)
 after=ident(validator)
 if before!=after: raise RuntimeError('validator changed during fixtures')
 with pathlib.Path(args.output_csv).open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=list(results[0]),lineterminator='\n'); w.writeheader(); w.writerows(results)
 pathlib.Path(args.output_stdout).write_text('validator_sha256_before='+before+'\nvalidator_sha256_after='+after+'\n'+''.join(transcript)+'summary=6/6_PASS\n',encoding='utf-8')
 print('M4A4BA_STATUS_FIXTURES_6_OF_6_PASS')
if __name__=='__main__': main()
