#!/usr/bin/env python3
"""Consulta el catálogo de tratado por tallo o marca de palma."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from glosario import herbs as zh_herbs, patrons as zh_patrons, t as zh
from tratado_salud import PALMA_ENF, ZANGFU, paquete


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Vocabulario de tratado 三命通会 / 食疗")
    p.add_argument("--tallo", help="甲乙丙丁戊己庚辛壬癸")
    p.add_argument("--clima", default="templado")
    p.add_argument("--escaso", default="Agua")
    p.add_argument("--saturado", default="Tierra")
    p.add_argument("--marca", help="clave de PALMA_ENF si la foto verifica")
    p.add_argument("--hexagrama", type=int, help="1-64 capa 医易")
    p.add_argument("--inferior", help="乾兑离震巽坎艮坤")
    p.add_argument("--superior", help="乾兑离震巽坎艮坤")
    p.add_argument("--json", action="store_true")
    args = p.parse_args(argv)

    if args.hexagrama:
        from iching_salud import HEX, paquete_hex
        spec = HEX.get(args.hexagrama)
        if not spec:
            print("hexagrama fuera de 1-64")
            return 1
        # trigramas por defecto desde iching table if not passed
        inf = args.inferior
        sup = args.superior
        if not inf or not sup:
            sys.path.insert(0, str(Path(__file__).resolve().parent))
            import iching as ic
            bits = ic.HEX_LINES[args.hexagrama]
            inf = inf or ic.trigram_info(bits[:3])["nombre"]
            sup = sup or ic.trigram_info(bits[3:])["nombre"]
        pack = paquete_hex(args.hexagrama, inf, sup)
        if args.json:
            print(json.dumps(pack, ensure_ascii=False, indent=2))
            return 0
        print(f"=== Hexagrama {args.hexagrama} {inf}/{sup} ===")
        print("Eje:", pack["eje"])
        print("Enfermedades:")
        for e in pack["enfermedades"]:
            print(" -", e)
        print("Hierbas:", zh_herbs(pack["hierbas"]))
        print("Alimentos:", ", ".join(pack["alimentos"]))
        print("Consejos:")
        for c in pack["consejos"]:
            print(" -", c)
        print(pack["nota"])
        return 0

    if args.marca:
        hits = PALMA_ENF.get(args.marca)
        if not hits:
            print("Marcas conocidas:")
            for k in PALMA_ENF:
                print(" -", k)
            return 1
        print("Marca verificable:", args.marca)
        for h in hits:
            print(" -", h)
        print("ENCUADRE: solo si la foto sostiene la marca. No es diagnóstico.")
        return 0

    if not args.tallo:
        p.error("pasa --tallo o --marca")

    pack = paquete(args.tallo, args.clima, args.escaso, args.saturado)
    if args.json:
        print(json.dumps(pack, ensure_ascii=False, indent=2))
        return 0
    zf = pack["zangfu"]
    print(f"=== {zh(args.tallo)} ===")
    print(f"{zf.get('fu')} / {zf.get('zang')} · {zf.get('tejidos')}")
    print("Patrones:", zh_patrons(pack["patrones"]))
    print("Enfermedades del tratado:")
    for e in pack["enfermedades"]:
        print(" -", e)
    print("Hierbas:", zh_herbs(pack["hierbas"]))
    print("Alimentos:", ", ".join(pack["alimentos"]))
    print("Té:", "; ".join(pack["tes"]))
    print("Evitar:", ", ".join(pack["evitar"]))
    print("Consejos:")
    for c in pack["consejos"]:
        print(" -", c)
    print(pack["nota"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
