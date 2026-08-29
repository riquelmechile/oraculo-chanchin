#!/usr/bin/env python3
"""Consulta integrada: BaZi + numerología + I Ching + cruce + marcas."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import bazi  # noqa: E402
import iching  # noqa: E402
import numerologia  # noqa: E402
from cruce import cruzar, render_cruce  # noqa: E402


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Carta integrada Oráculo Chanchín")
    p.add_argument("--nombre", required=True)
    p.add_argument("--usado", default=None)
    p.add_argument("--fecha", required=True)
    p.add_argument("--hora", default=None)
    p.add_argument("--sexo", required=True, choices=["M", "F", "m", "f"])
    p.add_argument("--tz", default="America/Santiago")
    p.add_argument("--lon", type=float, default=-70.65)
    p.add_argument("--sin-hora", action="store_true")
    p.add_argument("--anio", type=int, default=None)
    p.add_argument("--pregunta", default=None, help="si hay pregunta, se tira I Ching")
    p.add_argument("--metodo", choices=["varillas", "monedas"], default="varillas")
    p.add_argument("--lineas", default=None, help="seis valores 6-9, abajo→arriba")
    p.add_argument(
        "--marcas",
        default=None,
        help="marcas de palma verificables, separadas por ;",
    )
    p.add_argument("--json", action="store_true")
    return p


def _iching(args):
    if not args.pregunta and not args.lineas:
        return None
    if args.lineas:
        vals = [int(x.strip()) for x in args.lineas.split(",")]
        if len(vals) != 6 or any(v not in (6, 7, 8, 9) for v in vals):
            raise SystemExit("Usa seis valores 6,7,8 o 9.")
        return iching.interpret(vals, args.pregunta or "(líneas dadas)", "manual")
    vals = iching.cast(args.metodo, args.pregunta)
    return iching.interpret(vals, args.pregunta, args.metodo)


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    chart = bazi.compute(args.fecha, args.hora, args.sexo, args.tz, args.lon, args.sin_hora)
    nums = numerologia.compute(args.nombre, args.fecha, args.usado, args.anio)
    gua = _iching(args)
    marcas = [m.strip() for m in (args.marcas or "").split(";") if m.strip()]
    cruce = cruzar(chart, nums, gua, marcas)

    if args.json:
        print(json.dumps({
            "bazi": chart.as_dict(),
            "numerologia": nums,
            "iching": gua,
            "marcas": marcas,
            "cruce": cruce,
        }, ensure_ascii=False, indent=2, default=str))
        return 0

    print(bazi.render_text(chart))
    print()
    print(numerologia.render_text(nums))
    if gua:
        print()
        print(iching.render_text(gua))
    if marcas:
        print()
        print("=== Marcas declaradas (solo si la foto las verifica) ===")
        for m in marcas:
            print(" -", m)
    print()
    print(render_cruce(cruce))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
