#!/usr/bin/env python3
"""Validaciones de Oráculo Chanchín.

Comprueba que el vocabulario de tratado (zangfu, enfermedades, 食疗) exista
en los scripts y que la salida declare el encuadre de experimento.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    ROOT / "SKILL.md",
    ROOT / "README.md",
    ROOT / "VERSION",
    ROOT / "docs" / "EXPERIMENTO.md",
    ROOT / "docs" / "FOTO-Y-VERIFICACION.md",
    ROOT / "docs" / "SEGURIDAD-Y-LIMITES.md",
    ROOT / "scripts" / "iching.py",
    ROOT / "scripts" / "bazi.py",
    ROOT / "scripts" / "tiaohou_data.py",
    ROOT / "scripts" / "tratado_salud.py",
    ROOT / "scripts" / "tratado.py",
    ROOT / "scripts" / "iching_salud.py",
    ROOT / "scripts" / "cruce.py",
    ROOT / "scripts" / "glosario.py",
]

LIMITS = [
    "No diagnostica enfermedades a partir de la mano, BaZi o I Ching.",
    "No prescribe hierbas, suplementos, dosis ni tratamientos.",
    "No calcula esperanza de vida con la “línea de la vida”.",
    "No afirma que una tradición simbólica esté validada por la ciencia moderna.",
    "No garantiza resultados: pareja, trabajo, dinero, salud o muerte.",
    "No convierte cada marca de la palma en una patología.",
]

REQUIRED_IN_SCRIPTS = {
    "tratado_salud.py": ("ZANGFU", "SHILIAO", "PALMA_ENF", "enfermedades_tratado"),
    "tiaohou_data.py": ("ZANGFU", "SHILIAO"),
    "glosario.py": ("PATRON_ES", "HERBA_ES"),
    "bazi.py": ("zangfu_tratado", "shiliao"),
}


def fail(msg: str) -> None:
    print(f"FALLO: {msg}", file=sys.stderr)
    raise SystemExit(1)


def main() -> int:
    for path in REQUIRED:
        if not path.exists():
            fail(f"falta {path.relative_to(ROOT)}")

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "name: oraculo-chanchin" not in skill:
        fail("SKILL.md no declara name: oraculo-chanchin")
    for line in LIMITS:
        if line not in readme:
            fail(f"README.md perdió el límite-estatuto: {line}")

    for name, tokens in REQUIRED_IN_SCRIPTS.items():
        text = (ROOT / "scripts" / name).read_text(encoding="utf-8")
        for token in tokens:
            if token not in text:
                fail(f"{name} perdió {token}")

    py_files = sorted((ROOT / "scripts").glob("*.py")) + sorted((ROOT / "tools").glob("*.py"))
    subprocess.run([sys.executable, "-m", "py_compile", *map(str, py_files)], cwd=ROOT, check=True)

    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "iching.py"), "--validar"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    if not result.stdout.startswith("OK"):
        fail("validación I Ching no devolvió OK")

    sample = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "bazi.py"),
            "--fecha", "1995-02-12",
            "--hora", "16:30",
            "--sexo", "M",
            "--tz", "America/Santiago",
            "--lon", "-70.65",
        ],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    out = sample.stdout
    for needle in (
        "Enfermedades que nombra el tratado",
        "食疗",
        "Hierbas:",
        "ENCUADRE",
        "vesícula",
    ):
        if needle not in out:
            fail(f"salida de bazi.py no contiene '{needle}'")

    junk = [p for p in ROOT.rglob("*") if "__pycache__" in p.parts and ".git" not in p.parts]
    for path in sorted(junk, reverse=True):
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            try:
                path.rmdir()
            except OSError:
                pass

    print("OK — tratado presente, encuadre presente, I Ching y BaZi validados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
