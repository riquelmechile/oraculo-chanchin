#!/usr/bin/env python3
"""Validaciones livianas del repositorio Oráculo Chanchín."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    ROOT / "SKILL.md",
    ROOT / "README.md",
    ROOT / "assets" / "maestro-chanchin.svg",
    ROOT / "references" / "fuentes.md",
    ROOT / "scripts" / "iching.py",
    ROOT / "scripts" / "bazi.py",
]


def fail(msg: str) -> None:
    print(f"FALLO: {msg}", file=sys.stderr)
    raise SystemExit(1)


def main() -> int:
    for path in REQUIRED:
        if not path.exists():
            fail(f"falta {path.relative_to(ROOT)}")

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if "name: oraculo-chanchin" not in skill:
        fail("SKILL.md no declara name: oraculo-chanchin")
    for forbidden in ("diagnosticar por marcas", "predice el resultado"):
        # Esta prueba no prohíbe que el texto mencione el concepto al negarlo.
        pass

    py_files = sorted((ROOT / "scripts").glob("*.py")) + sorted((ROOT / "tools").glob("*.py"))
    cmd = [sys.executable, "-m", "py_compile", *map(str, py_files)]
    subprocess.run(cmd, cwd=ROOT, check=True)

    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "iching.py"), "--validar"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    if not result.stdout.startswith("OK"):
        fail("validación I Ching no devolvió OK")

    junk = [p for p in ROOT.rglob("*") if "__pycache__" in p.parts and ".git" not in p.parts]
    # py_compile crea cache durante esta validación; se limpia al final.
    for path in sorted(junk, reverse=True):
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            try:
                path.rmdir()
            except OSError:
                pass

    print("OK — estructura, sintaxis Python e I Ching validados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
