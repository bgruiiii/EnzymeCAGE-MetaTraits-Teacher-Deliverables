#!/usr/bin/env python3
"""Run semantic mutations against the M4a-2C fixture validator."""

from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Callable


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rewrite_fixture_hash(root: Path) -> None:
    manifest = root / "FIXTURE_MANIFEST.sha256"
    lines = []
    for line in manifest.read_text(encoding="utf-8").splitlines():
        digest, relative_path = line.split("  ", 1)
        if relative_path == "host_mapping_cases.json":
            digest = sha256(root / relative_path)
        lines.append(f"{digest}  {relative_path}")
    manifest.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def mutate_json(root: Path, mutation: Callable[[dict[str, object]], None]) -> None:
    path = root / "host_mapping_cases.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    mutation(data)
    path.write_text(
        json.dumps(data, indent=2, sort_keys=True, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    rewrite_fixture_hash(root)


def run_case(
    source_root: Path,
    validator: Path,
    name: str,
    expected_code: str,
    mutation: Callable[[dict[str, object]], None],
) -> None:
    with tempfile.TemporaryDirectory(prefix=f"m4a2c_{name}_") as temporary:
        root = Path(temporary) / "fixture"
        shutil.copytree(source_root, root)
        mutate_json(root, mutation)
        result = subprocess.run(
            [sys.executable, str(validator), str(root)],
            text=True,
            capture_output=True,
            check=False,
        )
        combined = result.stdout + result.stderr
        if result.returncode == 0 or f"INVALID:{expected_code}" not in combined:
            raise RuntimeError(
                f"negative test {name} failed: exit={result.returncode} output={combined!r}"
            )
        print(f"PASS:{name}:INVALID:{expected_code}")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: run_negative_tests.py FIXTURE_ROOT", file=sys.stderr)
        return 2
    source_root = Path(sys.argv[1]).resolve()
    validator = (Path(__file__).resolve().parent / "validate_fixtures.py").resolve()

    run_case(
        source_root,
        validator,
        "confidence_injection",
        "FORBIDDEN_CONFIDENCE_FIELD",
        lambda data: data["cases"][0]["expected"].update({"organism_confidence": 1.0}),
    )
    run_case(
        source_root,
        validator,
        "unreviewed_inclusion",
        "UNREVIEWED_CASE",
        lambda data: data["cases"][0]["expected"]["uniprot"].update({"reviewed": False}),
    )
    run_case(
        source_root,
        validator,
        "kegg_multiple_collapsed",
        "KEGG_GENE_IDS_RAW_MISMATCH",
        lambda data: data["cases"][7]["expected"]["kegg"].update(
            {"gene_ids": ["eco:b1449"], "multiplicity": 1, "state": "single"}
        ),
    )
    run_case(
        source_root,
        validator,
        "uid_identity_changed",
        "UID_ORDER_OR_MEMBERSHIP_MISMATCH",
        lambda data: data["cases"][0].update({"uid": "NOT_A_REAL_UID"}),
    )
    print("PASS:M4A2C_NEGATIVE_TESTS:4/4")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
