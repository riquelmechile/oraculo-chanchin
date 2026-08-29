#!/usr/bin/env python3
"""Construye dist/oraculo-chanchin.skill como ZIP reproducible."""

from __future__ import annotations

import os
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
OUT = DIST / "oraculo-chanchin.skill"
PACKAGE_ROOT = "oraculo-chanchin"

INCLUDE_DIRS = ("assets", "docs", "references", "scripts")
INCLUDE_FILES = ("SKILL.md", "README.md", "LICENSE", "VERSION")
EXCLUDED_PARTS = {"__pycache__", ".git", ".pytest_cache", ".venv", "venv", "dist"}


def iter_files() -> list[Path]:
    files: list[Path] = []
    for name in INCLUDE_FILES:
        p = ROOT / name
        if p.exists():
            files.append(p)
    for dirname in INCLUDE_DIRS:
        base = ROOT / dirname
        if not base.exists():
            continue
        for p in base.rglob("*"):
            if not p.is_file():
                continue
            if any(part in EXCLUDED_PARTS for part in p.parts):
                continue
            if p.suffix in {".pyc", ".pyo"}:
                continue
            files.append(p)
    return sorted(files, key=lambda p: p.as_posix())


def build() -> Path:
    DIST.mkdir(parents=True, exist_ok=True)
    epoch = (2026, 8, 28, 0, 0, 0)
    with zipfile.ZipFile(OUT, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for src in iter_files():
            rel = src.relative_to(ROOT).as_posix()
            arcname = f"{PACKAGE_ROOT}/{rel}"
            info = zipfile.ZipInfo(arcname, date_time=epoch)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o755 if os.access(src, os.X_OK) else 0o644) << 16
            zf.writestr(info, src.read_bytes())
    return OUT


if __name__ == "__main__":
    path = build()
    print(path)
