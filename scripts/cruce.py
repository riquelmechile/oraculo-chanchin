#!/usr/bin/env python3
"""Cruce automático: BaZi × I Ching × numerología × marcas de palma.

Marca convergencia, divergencia y silencio. No inventa clínica.
"""

from __future__ import annotations

from tratado_salud import PALMA_ENF, WUXING, paquete as paquete_bazi
from iching_salud import paquete_hex

ELEM_NUM = {
    1: "Agua",
    2: "Tierra",
    3: "Madera",
    4: "Madera",
    5: "Tierra",
    6: "Metal",
    7: "Metal",
    8: "Tierra",
    9: "Fuego",
    11: "Agua",
    22: "Tierra",
    33: "Fuego",
}

REL = {
    "Madera": {"genero": "Fuego", "controla": "Tierra", "lo_controla": "Metal", "me_genera": "Agua"},
    "Fuego": {"genero": "Tierra", "controla": "Metal", "lo_controla": "Agua", "me_genera": "Madera"},
    "Tierra": {"genero": "Metal", "controla": "Agua", "lo_controla": "Madera", "me_genera": "Fuego"},
    "Metal": {"genero": "Agua", "controla": "Madera", "lo_controla": "Fuego", "me_genera": "Tierra"},
    "Agua": {"genero": "Madera", "controla": "Fuego", "lo_controla": "Tierra", "me_genera": "Metal"},
}


def _reduce(n: int) -> int:
    if n in (11, 22, 33):
        return n
    while n > 9:
        n = sum(int(d) for d in str(n))
        if n in (11, 22, 33):
            return n
    return n


def fase_numero(n: int | None) -> str | None:
    if n is None:
        return None
    return ELEM_NUM.get(_reduce(int(n)))


def cruzar(chart, nums: dict | None = None, iching: dict | None = None,
           marcas: list[str] | None = None) -> dict:
    dm = chart.day_master
    elems = chart.elements
    scarce = min(elems, key=elems.get)
    top = max(elems, key=elems.get)
    th = chart.tiaohou
    clima = th.get("clima_mes", "templado")
    faltan = th.get("yongshen_faltan") or []
    dioses = (th.get("capas_tratado") or {}).get("dioses") or []

    capas: dict[str, list[str]] = {
        "bazi": [dm["elemento"], scarce, top],
        "iching": [],
        "numeros": [],
        "mano": [],
    }

    conv: list[str] = []
    div: list[str] = []
    sil: list[str] = []

    # I Ching
    salud = None
    if iching:
        pres = iching.get("presente") or {}
        salud = iching.get("salud_presente")
        inf_e = (pres.get("inferior") or {}).get("elemento")
        sup_e = (pres.get("superior") or {}).get("elemento")
        nuc = iching.get("presente") and (iching.get("nucleo") or {})
        nuc_e = []
        if nuc:
            nuc_e = [
                (nuc.get("inferior") or {}).get("elemento"),
                (nuc.get("superior") or {}).get("elemento"),
            ]
        for e in [inf_e, sup_e, *nuc_e]:
            if e:
                capas["iching"].append(e)

        if inf_e == dm["elemento"]:
            conv.append(
                f"Convergencia constitución: trigrama inferior {pres['inferior']['nombre']} "
                f"({inf_e}) = Amo del Día {dm['tallo']} {dm['elemento']}."
            )
        if sup_e == dm["elemento"]:
            conv.append(
                f"Convergencia manifestación: trigrama superior {pres['superior']['nombre']} "
                f"({sup_e}) coincide con el Amo."
            )
        if inf_e == scarce or sup_e == scarce:
            conv.append(
                f"El hexagrama insiste en {scarce}, que en la carta está escaso "
                f"({elems[scarce]}%). El tratado lee carencia, no sobra."
            )
        if inf_e == top or sup_e == top:
            div.append(
                f"El hexagrama muestra {top}, que en la carta ya satura "
                f"({elems[top]}%). Insistir ahí es echar más de lo que sobra."
            )
        if inf_e and REL.get(dm["elemento"], {}).get("lo_controla") == inf_e:
            div.append(
                f"El trigrama inferior ({inf_e}) controla al Amo ({dm['elemento']}). "
                f"Tensión de base: el cuerpo del hexagrama aprieta la constitución."
            )
        if sup_e and REL.get(dm["elemento"], {}).get("lo_controla") == sup_e:
            div.append(
                f"El trigrama superior ({sup_e}) controla al Amo. "
                f"La situación aparente presiona al día."
            )
        if inf_e and REL.get(dm["elemento"], {}).get("me_genera") == inf_e:
            conv.append(
                f"El inferior ({inf_e}) genera al Amo. El hexagrama ofrece sostén de reserva."
            )
        nucleo_n = (iching.get("nucleo") or {}).get("numero")
        pres_n = pres.get("numero")
        if nucleo_n and pres_n and nucleo_n != pres_n:
            sil.append(
                f"Núcleo {nucleo_n} ≠ presente {pres_n}: lo interior no es lo que se ve. "
                f"En salud de tratado, priorizar el núcleo si contradice."
            )
        if iching.get("lineas_mutantes"):
            sil.append(
                "Hay líneas mutantes: la zona del cuerpo del hexagrama es palanca, no sentencia."
            )

    # Numerología
    camino = None
    if nums:
        camino = nums.get("camino_de_vida", {}).get("final")
        exp = nums.get("nacimiento", {}).get("expresion", {}).get("final")
        alma = nums.get("nacimiento", {}).get("alma", {}).get("final")
        pers = nums.get("nacimiento", {}).get("personalidad", {}).get("final")
        for n in (camino, exp, alma, pers):
            f = fase_numero(n)
            if f:
                capas["numeros"].append(f)
        f_cam = fase_numero(camino)
        if f_cam == dm["elemento"]:
            conv.append(f"Camino {camino} ({f_cam}) = elemento del Amo. Eje reforzado.")
        elif f_cam == scarce:
            conv.append(f"Camino {camino} apunta a la fase escasa {scarce}. El número pide lo que falta.")
        elif f_cam == top:
            div.append(f"Camino {camino} ({f_cam}) coincide con lo saturado. Riesgo de insistir.")
        if f_cam and f_cam not in (dm["elemento"], scarce, top):
            sil.append(f"Camino {camino} ({f_cam}) no calza con Amo/escaso/saturado. Queda como matiz.")

    # Palma
    marcas = marcas or []
    for m in marcas:
        hits = PALMA_ENF.get(m)
        if not hits:
            sil.append(f"Marca «{m}» no está en el catálogo. Describirla cruda, no traducirla.")
            continue
        capas["mano"].append(m)
        texto = " / ".join(hits)
        bajo = texto.lower()
        if scarce.lower() in bajo or (WUXING.get(scarce) or {}).get("zangfu", "").split("/")[0].strip() in bajo:
            conv.append(f"Marca verificable «{m}» dialoga con la fase escasa {scarce}: {texto}")
        elif top.lower() in bajo:
            div.append(f"Marca «{m}» habla de {top}, que ya satura: {texto}")
        else:
            sil.append(f"Marca verificable «{m}»: {texto}")

    # Paquete de tratado priorizando convergencias
    pack = paquete_bazi(dm["tallo"], clima, scarce, top, dioses, faltan)
    if salud:
        pack = {
            **pack,
            "enfermedades": list(dict.fromkeys(pack["enfermedades"] + salud.get("enfermedades", [])))[:24],
            "hierbas": list(dict.fromkeys(pack["hierbas"] + salud.get("hierbas", [])))[:18],
            "alimentos": list(dict.fromkeys(pack["alimentos"] + salud.get("alimentos", [])))[:16],
            "consejos": list(dict.fromkeys(pack["consejos"] + salud.get("consejos", [])))[:10],
        }

    if not conv:
        sil.append("Sin convergencia fuerte entre capas. No forzar un eje único.")

    return {
        "capas": capas,
        "convergencias": conv,
        "divergencias": div,
        "silencios": sil,
        "paquete": pack,
        "amo": dm,
        "escaso": scarce,
        "saturado": top,
        "clima": clima,
        "nota": (
            "Cruce automático de este modelo. Convergencia ≠ destino. "
            "Vocabulario de tratado, no verdad clínica."
        ),
    }


def render_cruce(c: dict) -> str:
    lines = ["=== Cruce automático (BaZi × I Ching × números × mano) ==="]
    lines.append(
        f"Amo {c['amo']['tallo']} {c['amo']['elemento']} · "
        f"escaso {c['escaso']} · saturado {c['saturado']} · clima {c['clima']}"
    )
    lines += ["", "Convergencias:"]
    lines += [f"  - {x}" for x in (c["convergencias"] or ["(ninguna forzada)"])]
    lines += ["", "Divergencias:"]
    lines += [f"  - {x}" for x in (c["divergencias"] or ["(ninguna nombrada)"])]
    lines += ["", "Silencios / matices:"]
    lines += [f"  - {x}" for x in (c["silencios"] or ["(nada en silencio)"])]
    pack = c["paquete"]
    lines += ["", "=== Tratado fusionado (prioriza convergencia) ==="]
    lines.append("Enfermedades de tratado:")
    lines += [f"  - {e}" for e in pack.get("enfermedades") or []]
    from glosario import herbs as zh_herbs
    lines.append("Hierbas: " + zh_herbs(pack.get("hierbas") or []))
    lines.append("Alimentos: " + ", ".join(pack.get("alimentos") or []))
    lines.append("Consejos:")
    lines += [f"  - {x}" for x in pack.get("consejos") or []]
    lines += ["", c["nota"]]
    lines.append("ENCUADRE: experimento. No diagnóstico, no receta, no predicción.")
    return "\n".join(lines)
