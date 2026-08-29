#!/usr/bin/env python3
"""BaZi (cuatro pilares) con hora solar verdadera y términos solares."""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from glosario import t as zh, stems as zh_stems, patrons as zh_patrons, herbs as zh_herbs
from glosario import ganzhi as zh_gz

STEMS = list("甲乙丙丁戊己庚辛壬癸")
BRANCHES = list("子丑寅卯辰巳午未申酉戌亥")
STEM_ELEM = ["Madera", "Madera", "Fuego", "Fuego", "Tierra", "Tierra",
             "Metal", "Metal", "Agua", "Agua"]
STEM_POL = ["Yang", "Yin"] * 5
BRANCH_ELEM = ["Agua", "Tierra", "Madera", "Madera", "Tierra", "Fuego",
               "Fuego", "Tierra", "Metal", "Metal", "Tierra", "Agua"]
BRANCH_ANIMAL = ["Rata", "Buey", "Tigre", "Conejo", "Dragón", "Serpiente",
                 "Caballo", "Cabra", "Mono", "Gallo", "Perro", "Cerdo"]
ELEM_ES = ["Madera", "Fuego", "Tierra", "Metal", "Agua"]
GEN = {"Madera": "Fuego", "Fuego": "Tierra", "Tierra": "Metal",
       "Metal": "Agua", "Agua": "Madera"}
CTRL = {"Madera": "Tierra", "Fuego": "Metal", "Tierra": "Agua",
        "Metal": "Madera", "Agua": "Fuego"}

# Tallos ocultos (principal primero) y pesos relativos
HIDDEN = {
    0: [(9, 1.0)],
    1: [(5, 0.6), (9, 0.2), (7, 0.2)],
    2: [(0, 0.6), (2, 0.2), (4, 0.2)],
    3: [(1, 1.0)],
    4: [(4, 0.6), (1, 0.2), (9, 0.2)],
    5: [(2, 0.6), (6, 0.2), (4, 0.2)],
    6: [(3, 0.7), (5, 0.3)],
    7: [(5, 0.6), (3, 0.2), (1, 0.2)],
    8: [(6, 0.6), (8, 0.2), (4, 0.2)],
    9: [(7, 1.0)],
    10: [(4, 0.6), (7, 0.2), (3, 0.2)],
    11: [(8, 0.7), (0, 0.3)],
}

GODS = {
    ("same", "same"): "比肩",
    ("same", "opp"): "劫财",
    ("prod", "same"): "食神",
    ("prod", "opp"): "伤官",
    ("ctrl", "same"): "偏财",
    ("ctrl", "opp"): "正财",
    ("ctrl_me", "same"): "七杀",
    ("ctrl_me", "opp"): "正官",
    ("res", "same"): "偏印",
    ("res", "opp"): "正印",
}
GOD_ES = {
    "比肩": "Comparación (compañero)",
    "劫财": "Robo de riqueza (competencia)",
    "食神": "Espíritu de alimento",
    "伤官": "Oficial herido",
    "偏财": "Riqueza indirecta",
    "正财": "Riqueza directa",
    "七杀": "Siete asesinatos",
    "正官": "Oficial directo",
    "偏印": "Sello indirecto",
    "正印": "Sello directo",
}

SEASON_POWER = {
    "Madera": {"Madera": 1.2, "Fuego": 1.0, "Tierra": 0.8, "Metal": 0.6, "Agua": 1.0},
    "Fuego": {"Madera": 1.0, "Fuego": 1.2, "Tierra": 1.0, "Metal": 0.8, "Agua": 0.6},
    "Tierra": {"Madera": 0.6, "Fuego": 1.0, "Tierra": 1.2, "Metal": 1.0, "Agua": 0.8},
    "Metal": {"Madera": 0.8, "Fuego": 0.6, "Tierra": 1.0, "Metal": 1.2, "Agua": 1.0},
    "Agua": {"Madera": 1.0, "Fuego": 0.8, "Tierra": 0.6, "Metal": 1.0, "Agua": 1.2},
}

PILLAR_KEYS = ("year", "month", "day", "hour")
PILLAR_ES = {"year": "Año", "month": "Mes", "day": "Día", "hour": "Hora"}

# Clima del mes BaZi (rama). 调候 aproximado, no tabla fina de 穷通宝鉴 por día.
CLIMA_MES = {
    11: "frio", 0: "frio", 1: "frio-humedo",       # 亥子丑
    2: "templado", 3: "templado",                   # 寅卯
    4: "humedo",                                    # 辰
    5: "calido", 6: "calido", 7: "calido-humedo",   # 巳午未
    8: "seco", 9: "seco",                           # 申酉
    10: "seco",                                     # 戌
}
HABITO_CLIMA = {
    "frio": "Calor de ritmo: sol de mañana, comida caliente, no madrugar a oscuras, no baño helado.",
    "frio-humedo": "Calor seco de ritmo: cocido, movimiento, no crudo ni humedad acumulada.",
    "calido": "Frescura de ritmo: sombra, agua, menos picante, dormir de verdad.",
    "calido-humedo": "Frescura que no empape: movimiento, comida ligera, no hielo a destajo ni siesta húmeda larga.",
    "humedo": "Secar con ritmo: caminar después de comer, no picar, menos crudo.",
    "seco": "Humectar de ritmo: agua, menos picante, recoger el día temprano.",
    "templado": "Sin urgencia de clima. Mandan el elemento escaso y el saturado.",
}
HABITO_ESCASO = {
    "Madera": "Caminar, estirar, no aplazarse. El brote pide paso, no más plan.",
    "Fuego": "Sol de mañana y trato. No aislarse en seco.",
    "Tierra": "Horario fijo de comida. Un frente menos, no más rumia.",
    "Metal": "Respirar, terminar, decir no. El corte limpio vale más que otro proyecto.",
    "Agua": "Dormir, calor en pies y cintura, menos heroísmo nocturno.",
}
HABITO_SATURA = {
    "Madera": "No pelear cada borde. Cortar estímulos.",
    "Fuego": "Menos pantalla y menos picante. El brillo se apaga durmiendo.",
    "Tierra": "Moverse después de comer. La rumia no digestiona.",
    "Metal": "No podar de más. Humectar el corte.",
    "Agua": "Movimiento y calor moderado. La reserva que no se usa se estanca.",
}
ESTACION_NEIJING = {
    "primavera": "Acostarse más tarde, levantarse temprano, caminar, no reprimir el brote.",
    "verano": "No odiar el sol, no montar en ira, dejar salir. Dormir igual cuenta.",
    "otono": "Acostarse y levantarse temprano. Recoger el shen. Humectar.",
    "invierno": "Acostarse temprano, levantarse tarde, esperar la luz. No gastar la piel.",
}


def julian_day(dt: datetime) -> float:
    """JD a partir de datetime timezone-aware convertido a UTC."""
    utc = dt.astimezone(ZoneInfo("UTC"))
    y, m = utc.year, utc.month
    d = utc.day + (utc.hour + utc.minute / 60 + utc.second / 3600) / 24
    if m <= 2:
        y -= 1
        m += 12
    a = y // 100
    b = 2 - a + a // 4
    return int(365.25 * (y + 4716)) + int(30.6001 * (m + 1)) + d + b - 1524.5


def solar_longitude(jd: float) -> float:
    n = jd - 2451545.0
    L = (280.460 + 0.98564736 * n) % 360
    g = math.radians((357.528 + 0.98560028 * n) % 360)
    lam = L + 1.915 * math.sin(g) + 0.020 * math.sin(2 * g)
    return lam % 360


def equation_of_time_minutes(jd: float) -> float:
    n = jd - 2451545.0
    # Aproximación suficiente para corrección de minutos
    D = math.radians((360.0 / 365.24) * (n + 1))
    return (9.87 * math.sin(2 * D) - 7.53 * math.cos(D) - 1.5 * math.sin(D))


def true_solar_datetime(local: datetime, lon: float) -> tuple[datetime, float]:
    """Devuelve datetime en hora solar verdadera y corrección total en minutos."""
    utc = local.astimezone(ZoneInfo("UTC"))
    jd = julian_day(local)
    eot = equation_of_time_minutes(jd)
    mean_solar_offset_min = lon * 4.0  # 4 min por grado; lon oeste negativa
    utc_offset_min = local.utcoffset().total_seconds() / 60
    # Hora media local de huso = UTC + utc_offset
    # Hora media del meridiano real = UTC + lon*4 min
    # Diferencia huso vs meridiano = lon*4 - utc_offset
    corr = mean_solar_offset_min - utc_offset_min + eot
    solar = local + timedelta(minutes=corr)
    return solar, corr


def year_pillar_index(year: int) -> tuple[int, int]:
    return (year - 4) % 10, (year - 4) % 12


def solar_year_and_month(solar: datetime) -> tuple[int, int, float]:
    """Año BaZi (tras 立春) y rama de mes (寅=2 … 丑=1) según longitud solar."""
    jd = julian_day(solar)
    lon = solar_longitude(jd)
    # 立春 = 315°. Si lon >= 315 o el día está después del paso.
    year = solar.year
    if lon < 315 and solar.month <= 2:
        year -= 1
    # Meses solares: 寅 starts at 315, then every 30°
    # Map longitude to branch: 315-345 寅(2), 345-15 卯(3), 15-45 辰(4), ...
    shifted = (lon - 315) % 360
    month_ord = int(shifted // 30)  # 0=寅
    month_branch = (2 + month_ord) % 12
    return year, month_branch, lon


def month_stem(year_stem: int, month_branch: int) -> int:
    # 五虎遁: 寅 month stem from year stem
    bases = {0: 2, 1: 4, 2: 6, 3: 8, 4: 0, 5: 2, 6: 4, 7: 6, 8: 8, 9: 0}
    yin_stem = bases[year_stem]
    offset = (month_branch - 2) % 12
    return (yin_stem + offset) % 10


def day_pillar(solar: datetime) -> tuple[int, int]:
    """Pilar día. Ancla: 2000-01-01 civil UTC mediodía ≈ 戊午."""
    jd = julian_day(solar.replace(hour=12, minute=0, second=0, microsecond=0)
                    if solar.tzinfo else solar)
    # Usar JD a medianoche solar local (hora solar ya aplicada)
    local_midnight = solar.replace(hour=0, minute=0, second=0, microsecond=0)
    jd0 = julian_day(local_midnight)
    # 1 ene 2000 = 戊午. JD 2451544.5 es 1 ene 2000 00:00 UTC
    # Calibración empírica sobre ancla 戊午
    day_num = int(math.floor(jd0 + 0.5))
    # 2451545 = 1 ene 2000 12:00 TT ≈ día 戊午
    # 戊=4, 午=6
    stem = (day_num + 9) % 10  # se ajusta abajo con ancla
    branch = (day_num + 3) % 12
    # Recalibrar con offset para que 2000-01-01 dé 戊午
    # Probamos offsets en runtime via constante medida
    stem = (day_num - 2451545 + 4) % 10
    branch = (day_num - 2451545 + 6) % 12
    return stem, branch


def hour_branch(hour: int, minute: int) -> int:
    # 23:00-00:59 → 子 (0). Cada 2 horas.
    total = hour + minute / 60.0
    if total >= 23 or total < 1:
        return 0
    return int((total + 1) // 2) % 12


def hour_stem(day_stem: int, h_branch: int) -> int:
    # 五鼠遁
    bases = {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 0, 6: 2, 7: 4, 8: 6, 9: 8}
    return (bases[day_stem] + h_branch) % 10


def ten_god(day_stem: int, other_stem: int) -> str:
    de, oe = STEM_ELEM[day_stem], STEM_ELEM[other_stem]
    same_pol = (day_stem % 2) == (other_stem % 2)
    pol = "same" if same_pol else "opp"
    if oe == de:
        rel = "same"
    elif GEN[de] == oe:
        rel = "prod"
    elif CTRL[de] == oe:
        rel = "ctrl"
    elif GEN[oe] == de:
        rel = "res"
    else:
        rel = "ctrl_me"
    return GODS[(rel, pol)]


def pillar_label(stem: int, branch: int) -> str:
    return f"{STEMS[stem]}{BRANCHES[branch]}"


@dataclass
class Chart:
    local: datetime
    solar: datetime
    corr_min: float
    tz: str
    lon: float
    sex: str
    has_hour: bool
    pillars: dict
    elements: dict
    day_master: dict
    strength: dict
    luck: list
    notes: list
    tiaohou: dict

    def as_dict(self) -> dict:
        return {
            "local": self.local.isoformat(),
            "solar": self.solar.isoformat(),
            "correccion_min": round(self.corr_min, 1),
            "tz": self.tz,
            "lon": self.lon,
            "sexo": self.sex,
            "tiene_hora": self.has_hour,
            "pilares": self.pillars,
            "elementos": self.elements,
            "amo_del_dia": self.day_master,
            "fuerza": self.strength,
            "grandes_ciclos": self.luck,
            "tiaohou": self.tiaohou,
            "notas": self.notes,
        }


def _element_tally(pillars: dict, has_hour: bool) -> dict[str, float]:
    scores = {e: 0.0 for e in ELEM_ES}
    keys = ("year", "month", "day") + (("hour",) if has_hour else ())
    for k in keys:
        p = pillars[k]
        scores[STEM_ELEM[p["stem_i"]]] += 1.0
        for hs, w in HIDDEN[p["branch_i"]]:
            scores[STEM_ELEM[hs]] += w
        # Rama del mes pesa más (comando)
        if k == "month":
            scores[BRANCH_ELEM[p["branch_i"]]] += 0.6
    total = sum(scores.values()) or 1.0
    return {e: round(100.0 * scores[e] / total, 1) for e in ELEM_ES}


def _strength(day_stem: int, pillars: dict, has_hour: bool) -> dict:
    de = STEM_ELEM[day_stem]
    month_e = BRANCH_ELEM[pillars["month"]["branch_i"]]
    season = SEASON_POWER[month_e][de]
    support = 0.0
    drain = 0.0
    keys = ("year", "month", "day") + (("hour",) if has_hour else ())
    for k in keys:
        p = pillars[k]
        se = STEM_ELEM[p["stem_i"]]
        if k != "day":
            if se == de:
                support += 1.0
            elif GEN[se] == de:  # recurso
                support += 0.8
            elif GEN[de] == se:  # salida
                drain += 0.7
            elif CTRL[de] == se:  # riqueza
                drain += 0.5
            else:
                drain += 0.6  # oficial
        be = BRANCH_ELEM[p["branch_i"]]
        weight = 1.2 if k == "month" else 0.7
        if be == de or GEN[be] == de:
            support += weight
        else:
            drain += weight * 0.5
    score = season * 40 + support * 12 - drain * 8
    if score >= 55:
        label = "fuerte"
    elif score >= 40:
        label = "media-fuerte"
    elif score >= 28:
        label = "media-débil"
    else:
        label = "débil"
    return {
        "etiqueta": label,
        "puntaje_interno": round(score, 1),
        "temporada": month_e,
        "factor_estacional": season,
        "apoyo": round(support, 2),
        "drenaje": round(drain, 2),
        "lectura": (
            f"Amo {STEMS[day_stem]} ({de} {STEM_POL[day_stem % 2]}) en temporada "
            f"de {month_e}, factor {season}. Apoyo {support:.1f} / drenaje {drain:.1f} → {label}."
        ),
    }


def _next_term_jd(jd_start: float, forward: bool) -> float:
    lon0 = solar_longitude(jd_start)
    target_base = math.floor(lon0 / 30) * 30
    if forward:
        target = (target_base + 30) % 360
    else:
        target = target_base % 360
        if abs(((lon0 - target + 180) % 360) - 180) < 0.05:
            target = (target - 30) % 360
    # buscar por pasos de 0.25 día
    step = 0.25 if forward else -0.25
    jd = jd_start
    for _ in range(200):
        jd += step
        lon = solar_longitude(jd)
        if forward:
            if (lon - target) % 360 < 30 and abs(((lon - target + 180) % 360) - 180) < 2:
                break
        else:
            if (target - lon) % 360 < 30 and abs(((lon - target + 180) % 360) - 180) < 2:
                break
    # refine
    for _ in range(20):
        lon = solar_longitude(jd)
        err = ((lon - target + 180) % 360) - 180
        jd -= err / 0.9856
    return jd


def _luck_pillars(solar: datetime, year_stem: int, month_stem_i: int,
                  month_branch_i: int, sex: str) -> list:
    yang_year = year_stem % 2 == 0
    male = sex.upper().startswith("M")
    forward = (yang_year and male) or (not yang_year and not male)
    jd_birth = julian_day(solar)
    jd_term = _next_term_jd(jd_birth, forward)
    days = abs(jd_term - jd_birth)
    start_age = max(0.0, days / 3.0)
    out = []
    for i in range(8):
        delta = i + 1
        if forward:
            s = (month_stem_i + delta) % 10
            b = (month_branch_i + delta) % 12
        else:
            s = (month_stem_i - delta) % 10
            b = (month_branch_i - delta) % 12
        age0 = start_age + i * 10
        out.append({
            "orden": i + 1,
            "pilar": pillar_label(s, b),
            "tallo": STEMS[s],
            "rama": BRANCHES[b],
            "elemento_tallo": STEM_ELEM[s],
            "edad_inicio": round(age0, 1),
            "edad_fin": round(age0 + 10, 1),
            "direccion": "adelante" if forward else "atrás",
        })
    return out


def _estacion_solar(lon_deg: float) -> str:
    s = (lon_deg - 315) % 360
    if s < 90:
        return "primavera"
    if s < 180:
        return "verano"
    if s < 270:
        return "otono"
    return "invierno"


def _stems_in_chart(pillars: dict, has_hour: bool) -> set[str]:
    keys = ("year", "month", "day") + (("hour",) if has_hour else ())
    seen = set()
    for k in keys:
        p = pillars.get(k) if pillars else None
        if not p:
            continue
        seen.add(p["tallo"])
        for o in p.get("ocultos") or []:
            seen.add(o["tallo"])
    return seen


def _tiaohou(month_branch: int, elements: dict, lon: float, tz: str,
             day_stem: int | None = None, pillars: dict | None = None,
             has_hour: bool = False) -> dict:
    """Clima 穷通宝鉴 + vocabulario de tratado 三命通会 / 食疗. No es clínica."""
    clima = CLIMA_MES.get(month_branch, "templado")
    fire = elements.get("Fuego", 0)
    water = elements.get("Agua", 0)
    scarce = min(elements, key=elements.get)
    top = max(elements, key=elements.get)
    pide: list[str] = []
    if clima.startswith("frio") and fire < 15:
        pide.append("Fuego")
    if clima.startswith("calido") and water < 15:
        pide.append("Agua")
    if clima in ("humedo", "calido-humedo", "frio-humedo"):
        pide.append("movimiento/seco")
    if clima == "seco" and water < 18:
        pide.append("Agua")
    if not pide:
        pide.append("sin urgencia de clima")

    now = datetime.now(ZoneInfo(tz))
    slon_now = solar_longitude(julian_day(now))
    est_norte = _estacion_solar(slon_now)
    sur = lon < -20
    inv = {"primavera": "otono", "verano": "invierno", "otono": "primavera", "invierno": "verano"}
    est_local = inv[est_norte] if sur else est_norte

    from tiaohou_data import QTBJ, STEMS as TH_STEMS
    from tratado_salud import paquete as paquete_salud

    row = QTBJ.get((day_stem, month_branch)) if day_stem is not None else None
    presentes = _stems_in_chart(pillars, has_hour) if pillars else set()
    yongshen = []
    faltan = []
    if row:
        for stem in row["pri"]:
            item = {"tallo": stem, "presente": stem in presentes}
            yongshen.append(item)
            if stem not in presentes:
                faltan.append(stem)

    dm_char = TH_STEMS[day_stem] if day_stem is not None else None
    dioses = []
    if pillars:
        keys = ("year", "month", "day") + (("hour",) if has_hour else ())
        for k in keys:
            p = pillars.get(k) or {}
            g = p.get("dios_tallo")
            if g and g != "日主":
                dioses.append(g)
            for o in p.get("ocultos") or []:
                if o.get("dios") and o["dios"] != "日主":
                    dioses.append(o["dios"])
    # únicos, priorizando los que más salen
    rank = {}
    for g in dioses:
        rank[g] = rank.get(g, 0) + 1
    dioses_top = sorted(rank, key=lambda g: -rank[g])[:4]

    pack = paquete_salud(dm_char, clima, scarce, top, dioses_top, faltan)
    zf = pack["zangfu"]
    sl_hierbas = pack["hierbas"]
    sl_alim = pack["alimentos"]

    parrafo = (
        f"Tabla {zh('穷通宝鉴')}: {zh(dm_char or '')} en mes {zh(BRANCHES[month_branch])} ({clima}). "
        f"Dios útil (用神): {zh_stems(row['pri']) if row else '—'}. "
        f"{'Nota: ' + row['nota'] if row else ''} "
        f"En la carta están {zh_stems(x['tallo'] for x in yongshen if x['presente']) or 'ninguno'}. "
        f"Faltan {zh_stems(faltan) or 'ninguno'}. "
        f"Vocabulario {zh('三命通会')} del Amo: {zf.get('fu')}/{zf.get('zang')}; "
        f"patrones: {zh_patrons(pack['patrones'])}; "
        f"enfermedades que nombra el tratado: {', '.join(pack['enfermedades'])}. "
        f"{zh('食疗')} (se nombra, no se dosifica): hierbas {zh_herbs(sl_hierbas)}; "
        f"té {'; '.join(pack['tes']) or '—'}; alimentos {', '.join(sl_alim)}. "
        f"Consejos de tratado: {' | '.join(pack['consejos'][:4])}. "
        f"{HABITO_CLIMA[clima]} "
        f"Estación local ({'sur' if sur else 'norte'} {est_local}): {ESTACION_NEIJING[est_local]} "
        "ENCUADRE: vocabulario de tratado + cálculo interno, no verdad clínica ni receta."
    )
    return {
        "rama_mes": BRANCHES[month_branch],
        "clima_mes": clima,
        "pide": pide,
        "tabla": "穷通宝鉴",
        "amo": dm_char,
        "yongshen": yongshen,
        "yongshen_nota": row["nota"] if row else "",
        "yongshen_faltan": faltan,
        "zangfu_tratado": {
            "fu": zf.get("fu"),
            "zang": zf.get("zang"),
            "tejidos": zf.get("tejidos"),
            "emocion": zf.get("emocion"),
            "sentido": zf.get("sentido"),
            "sabor": zf.get("sabor"),
            "patrones": pack["patrones"],
            "enfermedades_tratado": pack["enfermedades"],
            "nota": "Vocabulario de tratado. No es diagnóstico de laboratorio.",
        },
        "shiliao": {
            "alimentos": sl_alim,
            "hierbas": sl_hierbas,
            "te": "; ".join(pack["tes"]),
            "evitar": pack["evitar"],
            "consejos": pack["consejos"],
            "nota": "Se nombra. No se dosifica. No sustituye a un herbolario titulado.",
        },
        "capas_tratado": {
            "fase_escasa": scarce,
            "fase_saturada": top,
            "clima": clima,
            "dioses": dioses_top,
            "yongshen_faltan": faltan,
        },
        "fuego_pct": fire,
        "agua_pct": water,
        "escaso": scarce,
        "escaso_pct": elements[scarce],
        "saturado": top,
        "saturado_pct": elements[top],
        "habito_clima": HABITO_CLIMA[clima],
        "habito_escaso": HABITO_ESCASO[scarce],
        "habito_saturado": HABITO_SATURA[top],
        "estacion_solar_norte_ahora": est_norte,
        "estacion_local_ahora": est_local,
        "hemisferio": "sur" if sur else "norte",
        "habito_estacion_ahora": ESTACION_NEIJING[est_local],
        "parrafo": parrafo,
        "aproximacion": False,
        "fuente": "穷通宝鉴 × 三命通会 × 食疗 × 黄帝内经. Experimento simbólico: se nombra el tratado, no se diagnostica ni se receta.",
    }


def compute(fecha: str, hora: str | None, sexo: str, tz: str, lon: float,
            sin_hora: bool = False) -> Chart:
    notes = []
    tzinfo = ZoneInfo(tz)
    if sin_hora or not hora:
        local = datetime.fromisoformat(fecha).replace(hour=12, minute=0, tzinfo=tzinfo)
        has_hour = False
        notes.append("Sin hora de reloj: se trabaja con tres pilares. Pilar horario omitido.")
    else:
        local = datetime.fromisoformat(f"{fecha}T{hora}").replace(tzinfo=tzinfo)
        has_hour = True
    solar, corr = true_solar_datetime(local, lon)
    notes.append(
        f"Hora de reloj {local.strftime('%Y-%m-%d %H:%M')} ({tz}). "
        f"Hora solar verdadera {solar.strftime('%H:%M')} (corrección {corr:+.1f} min, lon {lon})."
    )
    byear, month_br, slon = solar_year_and_month(solar)
    ys, yb = year_pillar_index(byear)
    ms = month_stem(ys, month_br)
    ds, db = day_pillar(solar)
    pillars = {}
    for key, s, b in (("year", ys, yb), ("month", ms, month_br), ("day", ds, db)):
        pillars[key] = {
            "ganzhi": pillar_label(s, b),
            "tallo": STEMS[s],
            "rama": BRANCHES[b],
            "stem_i": s,
            "branch_i": b,
            "elemento_tallo": STEM_ELEM[s],
            "polaridad": STEM_POL[s % 2],
            "elemento_rama": BRANCH_ELEM[b],
            "animal": BRANCH_ANIMAL[b],
        }
    if has_hour:
        hb = hour_branch(solar.hour, solar.minute)
        hs = hour_stem(ds, hb)
        pillars["hour"] = {
            "ganzhi": pillar_label(hs, hb),
            "tallo": STEMS[hs],
            "rama": BRANCHES[hb],
            "stem_i": hs,
            "branch_i": hb,
            "elemento_tallo": STEM_ELEM[hs],
            "polaridad": STEM_POL[hs % 2],
            "elemento_rama": BRANCH_ELEM[hb],
            "animal": BRANCH_ANIMAL[hb],
        }
        notes.append(
            f"Rama horaria tomada de la hora solar {solar.strftime('%H:%M')}, no del reloj."
        )
    else:
        pillars["hour"] = None

    for k, p in pillars.items():
        if not p:
            continue
        p["dios_tallo"] = "日主" if k == "day" else ten_god(ds, p["stem_i"])
        p["dios_tallo_es"] = "Amo del Día" if k == "day" else GOD_ES[p["dios_tallo"]]
        p["ocultos"] = [
            {
                "tallo": STEMS[h],
                "elemento": STEM_ELEM[h],
                "dios": ten_god(ds, h),
                "dios_es": GOD_ES[ten_god(ds, h)],
                "peso": w,
            }
            for h, w in HIDDEN[p["branch_i"]]
        ]

    elems = _element_tally(pillars, has_hour)
    dm = {
        "tallo": STEMS[ds],
        "elemento": STEM_ELEM[ds],
        "polaridad": STEM_POL[ds % 2],
        "ganzhi_dia": pillar_label(ds, db),
        "longitud_solar_deg": round(slon, 2),
        "anio_bazi": byear,
    }
    strength = _strength(ds, pillars, has_hour)
    luck = _luck_pillars(solar, ys, ms, month_br, sexo)
    for lp in luck:
        lp["dios"] = ten_god(ds, STEMS.index(lp["tallo"]))
        lp["dios_es"] = GOD_ES[lp["dios"]]
    notes.append(
        f"Año BaZi {byear} (立春 cuando la longitud solar pasa 315°; ahora {slon:.1f}°)."
    )
    tiaohou = _tiaohou(month_br, elems, lon, tz, ds, pillars, has_hour)
    return Chart(local, solar, corr, tz, lon, sexo.upper()[0], has_hour,
                 pillars, elems, dm, strength, luck, notes, tiaohou)


def render_text(c: Chart) -> str:
    lines = ["=== BaZi ===", *c.notes, "", "Pilares:"]
    for k in PILLAR_KEYS:
        p = c.pillars[k]
        if not p:
            lines.append(f"  {PILLAR_ES[k]:<6} — (sin hora)")
            continue
        occ = ", ".join(f"{zh(o['tallo'])} {zh(o['dios'])}" for o in p["ocultos"])
        lines.append(
            f"  {PILLAR_ES[k]:<6} {zh_gz(p['ganzhi'])}  "
            f"tallo {zh(p['tallo'])} {p['elemento_tallo']} {p['polaridad']}"
            f" ({zh(p['dios_tallo'])}) · rama {zh(p['rama'])} {p['animal']} {p['elemento_rama']} · ocultos {occ}"
        )
    lines += ["", "Reparto elemental (%):"]
    for e in ELEM_ES:
        bar = "█" * int(round(c.elements[e] / 4)) + "░" * (25 - int(round(c.elements[e] / 4)))
        lines.append(f"  {e:<8} {c.elements[e]:5.1f}%  {bar}")
    dm = c.day_master
    lines += [
        "",
        f"Amo del Día: {zh(dm['tallo'])} ({dm['elemento']} {dm['polaridad']}) — {zh_gz(dm['ganzhi_dia'])}",
        c.strength["lectura"],
        "",
        f"Grandes Ciclos (sexo {c.sex}, dirección {c.luck[0]['direccion']}):",
    ]
    for lp in c.luck:
        lines.append(
            f"  {lp['edad_inicio']:>5.1f}–{lp['edad_fin']:<5.1f}  {lp['pilar']}  "
            f"{lp['elemento_tallo']}  {zh(lp['dios'])}"
        )
    th = c.tiaohou
    zf = th.get("zangfu_tratado", {})
    sl = th.get("shiliao", {})
    lines += [
        "",
        "=== Ajuste climático (调候 / 穷通宝鉴) ===",
        f"Amo {zh(th.get('amo') or '')} en mes {zh(th['rama_mes'])} · clima {th['clima_mes']}",
        th.get("yongshen_nota") or "",
        "Dios útil (用神): " + ", ".join(
            f"{zh(y['tallo'])}{' presente' if y['presente'] else ' ausente'}"
            for y in th.get("yongshen") or []
        ),
        "Faltan: " + (zh_stems(th.get("yongshen_faltan") or []) or "ninguno"),
        "",
        "=== Vocabulario de tratado (三命通会 × 黄帝内经) ===",
        f"Correspondencia: {zf.get('fu')} / {zf.get('zang')} ({zf.get('tejidos', '')})",
        f"Emoción: {zf.get('emocion') or '—'} · sentido {zf.get('sentido') or '—'} · sabor {zf.get('sabor') or '—'}",
        "Patrones: " + zh_patrons(zf.get("patrones") or []),
        "Enfermedades que nombra el tratado:",
        *[f"  - {e}" for e in (zf.get("enfermedades_tratado") or [])],
        "",
        "=== 食疗 ancestral (se nombra, no se dosifica) ===",
        "Hierbas: " + zh_herbs(sl.get("hierbas") or []),
        f"Té tradicional: {sl.get('te') or '—'}",
        "Alimentos: " + ", ".join(sl.get("alimentos") or []),
        "Evitar según el registro: " + ", ".join(sl.get("evitar") or []),
        "Consejos de tratado:",
        *[f"  - {c}" for c in (sl.get("consejos") or [])],
        "",
        f"Estación local ({th['hemisferio']}, {th['estacion_local_ahora']}): {th['habito_estacion_ahora']}",
        f"Hábito de clima: {th.get('habito_clima', '')}",
        "ENCUADRE: experimento con IA y tradición ancestral. Vocabulario de tratado, no verdad clínica, no receta, no años de vida.",
    ]
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Cálculo BaZi")
    p.add_argument("--fecha", required=True, help="YYYY-MM-DD")
    p.add_argument("--hora", default=None, help="HH:MM hora de reloj")
    p.add_argument("--sexo", required=True, choices=["M", "F", "m", "f"])
    p.add_argument("--tz", default="America/Santiago")
    p.add_argument("--lon", type=float, default=-70.65)
    p.add_argument("--sin-hora", action="store_true")
    p.add_argument("--json", action="store_true")
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    chart = compute(args.fecha, args.hora, args.sexo, args.tz, args.lon, args.sin_hora)
    if args.json:
        print(json.dumps(chart.as_dict(), ensure_ascii=False, indent=2))
    else:
        print(render_text(chart))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
