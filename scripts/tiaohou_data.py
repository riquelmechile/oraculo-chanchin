#!/usr/bin/env python3
"""Tabla fina 穷通宝鉴 (tallo día × rama mes) + mapa 三命通会 / 食疗.

Las asociaciones de enfermedad son las del tratado, no un diagnóstico.
Las hierbas se nombran; no se dosifican.
"""

STEMS = list("甲乙丙丁戊己庚辛壬癸")

# rama 寅=2 … 丑=1. Clave: (stem_i, branch_i)
# pri = 用神 en orden de prioridad (caracteres de tallo)
QTBJ = {}


def _put(stem, months):
    si = STEMS.index(stem)
    for br, pri, nota in months:
        QTBJ[(si, br)] = {"pri": pri, "nota": nota}


_put("甲", [
    (2, ["丙", "癸"], "寅: 丙 principal, 癸 de apoyo. Clima primero."),
    (3, ["庚", "丙", "丁"], "卯: 庚 para podar. Sin 庚, 丙丁 drenan. No forzar 杀."),
    (4, ["庚", "丁", "壬"], "辰: 庚 solo si hay 丁. Sin 庚, 壬."),
    (5, ["癸", "丁", "庚"], "巳: 癸 de clima. 丁庚 de apoyo."),
    (6, ["癸", "丁", "庚"], "午: madera tostada. 癸 primero; sin 癸, 丁. Madera mucha → 庚."),
    (7, ["癸", "庚", "丁"], "未: primera quincena 癸; segunda 庚丁."),
    (8, ["庚", "丁", "壬"], "申: 庚 luego 丁. 伤官 puede tomar 壬."),
    (9, ["庚", "丁", "丙"], "酉: 庚 principal. 丙丁 de clima."),
    (10, ["庚", "甲", "丁"], "戌: tierra mucha → 甲; madera mucha → 庚."),
    (11, ["庚", "丁", "丙"], "亥: 庚丁, 丙 de clima. Madera mucha → 甲."),
    (0, ["丁", "庚", "丙"], "子: 丁 primero, 庚丙 después. Mejor con 寅巳."),
    (1, ["丁", "庚", "丙"], "丑: 丁 imprescindible. Mejor si 丁 se apoya en 寅巳."),
])
_put("乙", [
    (2, ["丙", "癸"], "寅: 丙 deshiela. 癸 apenas. Fuego mucho → solo 癸."),
    (3, ["丙", "癸"], "卯: 丙 drena, 癸 humedece. Oro fuerte estorba."),
    (4, ["癸", "丙", "戊"], "辰: 癸丙. Agua de ramo → 戊."),
    (5, ["癸"], "巳: 癸 de clima, urgente."),
    (6, ["癸", "丙"], "午: primera quincena 癸; segunda 丙癸."),
    (7, ["癸", "丙"], "未: 癸. Si hay mucho metal-agua, 丙. Evitar 戊己 que enturbian."),
    (8, ["丙", "癸", "己"], "申: 丙癸. 己 de apoyo si hay 庚."),
    (9, ["癸", "丙", "丁"], "酉: primera quincena 癸 luego 丙; segunda al revés."),
    (10, ["癸", "辛"], "戌: 癸 luego 辛."),
    (11, ["丙", "戊"], "亥: 丙. Agua mucha → 戊."),
    (0, ["丙"], "子: solo 丙. 癸 estorba."),
    (1, ["丙"], "丑: valle frío. Solo 丙."),
])
_put("丙", [
    (2, ["壬", "庚"], "寅: 壬 principal, 庚 abre la fuente."),
    (3, ["壬", "己"], "卯: 壬. Agua mucha → 戊/己."),
    (4, ["壬", "甲"], "辰: 壬. Tierra gruesa → 甲."),
    (5, ["壬", "庚", "癸"], "巳: 壬, 庚 de apoyo. Sin 壬, 癸. 戊 enturbia."),
    (6, ["壬", "庚"], "午: 壬庚. Mejor si 庚 se apoya en 申."),
    (7, ["壬", "庚"], "未: igual que 午."),
    (8, ["壬", "戊"], "申: 壬. Tierra mucha → 戊."),
    (9, ["壬", "癸"], "酉: 壬; sin 壬, 癸."),
    (10, ["甲", "壬"], "戌: 甲 primero si la tierra espesa, luego 壬."),
    (11, ["甲", "壬", "戊"], "亥: agua mucha → 甲; fuego alto → 壬."),
    (0, ["壬", "戊", "己"], "子: 壬. Agua mucha → 戊己."),
    (1, ["壬", "甲"], "丑: 壬. Tierra mucha → 甲."),
])
_put("丁", [
    (2, ["甲", "庚"], "寅: 甲 con 庚. No 甲 solo."),
    (3, ["庚", "甲"], "卯: 庚 primero si hay 乙."),
    (4, ["甲", "庚", "戊"], "辰: madera mucha → 庚; agua mucha → 戊."),
    (5, ["甲", "庚"], "巳: madera mucha → 庚 primero."),
    (6, ["壬", "庚", "癸"], "午: 壬庚. Sin 壬, 癸."),
    (7, ["甲", "壬", "庚"], "未: 甲 no va sin 庚."),
    (8, ["甲", "庚", "丙"], "申: 甲庚. Si hay 己 en ramo, 己 puede mandar."),
    (9, ["甲", "庚", "丙"], "酉: 甲庚丙."),
    (10, ["甲", "庚", "戊"], "戌: igual que 酉."),
    (11, ["甲", "庚"], "亥: 甲 principal, 庚 apoyo."),
    (0, ["甲", "庚"], "子: 甲庚."),
    (1, ["甲", "庚"], "丑: 甲庚."),
])
_put("戊", [
    (2, ["丙", "甲", "癸"], "寅: 丙, 甲, 癸. Los tres."),
    (3, ["丙", "甲", "癸"], "卯: igual."),
    (4, ["甲", "丙", "癸"], "辰: tierra de temporada. 甲 primero."),
    (5, ["甲", "丙", "癸"], "巳: 甲丙癸."),
    (6, ["壬", "甲", "丙"], "午: 壬 de clima primero."),
    (7, ["癸", "丙", "甲"], "未: 癸 si no hay 壬 suficiente."),
    (8, ["丙", "癸", "甲"], "申: 丙 de inicio de otoño."),
    (9, ["丙", "癸"], "酉: 丙 manda."),
    (10, ["甲", "丙", "癸"], "戌: si hay juego de metal, 癸 antes que 丙."),
    (11, ["甲", "丙"], "亥: 甲 y 丙, los dos."),
    (0, ["丙", "甲"], "子: 丙 primero."),
    (1, ["丙", "甲"], "丑: 丙甲."),
])
_put("己", [
    (2, ["丙", "庚", "甲"], "寅: 丙庚甲. 壬 con raíz estorba."),
    (3, ["甲", "癸", "丙"], "卯: 甲癸丙."),
    (4, ["丙", "癸", "甲"], "辰: tierra mucha → 甲 primero."),
    (5, ["癸", "丙"], "巳: 癸 de clima."),
    (6, ["癸", "丙"], "午: 癸丙."),
    (7, ["癸", "丙"], "未: 癸丙."),
    (8, ["丙", "癸"], "申: 丙 para cortar el 庚 de temporada."),
    (9, ["丙", "癸"], "酉: 丙癸."),
    (10, ["甲", "丙", "癸"], "戌: tierra fuerte → 甲; si no hay juego de tierra, 丙."),
    (11, ["丙", "甲", "戊"], "亥: 丙 de clima. 壬 fuerte → 戊."),
    (0, ["丙", "甲", "戊"], "子: 丙甲戊."),
    (1, ["丙", "甲", "戊"], "丑: 丙甲戊."),
])
_put("庚", [
    (2, ["戊", "甲", "丙"], "寅: 戊甲丙. Fuego de juego → 壬."),
    (3, ["丁", "甲", "丙"], "卯: 丁. Sin 丁, 丙."),
    (4, ["甲", "丁", "壬"], "辰: fuego de ramo → 癸; fuego de tallo → 壬."),
    (5, ["壬", "丁", "丙"], "巳: si hay juego de metal, 丁 manda."),
    (6, ["壬", "癸"], "午: 壬 urgente. Sin 壬癸, 戊己."),
    (7, ["丁", "甲"], "未: si hay juego de tierra, 甲 luego 丁."),
    (8, ["丁", "甲"], "申: 丁. Sin 甲 no usar 乙 de reemplazo."),
    (9, ["丁", "甲", "丙"], "酉: 丁甲. 丙 mejor en ramo que en tallo."),
    (10, ["甲", "壬"], "戌: 壬 no quiere 己 que enturbia."),
    (11, ["丁", "丙", "甲"], "亥: 丁丙."),
    (0, ["丁", "甲", "丙"], "子: 丙丁 con raíz en 巳午未戌."),
    (1, ["丙", "丁", "甲"], "丑: 丙丁甲."),
])
_put("辛", [
    (2, ["己", "壬", "庚"], "寅: 己 cría el metal. 己 y 壬 no peleen."),
    (3, ["壬", "甲"], "卯: 壬甲. 丁 a la vista estorba."),
    (4, ["壬", "甲"], "辰: 壬甲."),
    (5, ["壬", "甲", "癸"], "巳: 壬甲癸. Sin 戊 es mejor."),
    (6, ["壬", "己", "癸"], "午: 壬己癸."),
    (7, ["壬", "甲"], "未: 壬甲."),
    (8, ["壬", "甲"], "申: 壬甲."),
    (9, ["壬", "甲"], "酉: 壬甲. Metal blanco, agua clara."),
    (10, ["壬", "甲"], "戌: 壬 luego 甲."),
    (11, ["壬", "丙"], "亥: 壬 luego 丙."),
    (0, ["丙", "壬"], "子: 丙 luego 壬."),
    (1, ["丙", "壬"], "丑: 丙 deshiela, 壬 lava. 戊己 de apoyo."),
])
_put("壬", [
    (2, ["庚", "丙"], "寅: 庚 abre fuente, 丙 deshiela."),
    (3, ["戊", "辛"], "卯: 戊 dique, 辛 fuente."),
    (4, ["甲", "庚"], "辰: 甲 afloja tierra, 庚 fuente."),
    (5, ["壬", "辛"], "巳: verano seco. 壬辛."),
    (6, ["庚", "癸"], "午: 庚癸 para no secar el cauce."),
    (7, ["辛", "甲"], "未: 辛甲."),
    (8, ["戊", "丁"], "申: agua de otoño. 戊 dique, 丁."),
    (9, ["甲"], "酉: 甲."),
    (10, ["甲", "丙"], "戌: 甲丙."),
    (11, ["戊", "丙"], "亥: 戊丙."),
    (0, ["戊", "丙"], "子: 戊丙."),
    (1, ["丙", "甲"], "丑: 丙甲."),
])
_put("癸", [
    (2, ["辛", "丙"], "寅: 辛 fuente, 丙 deshiela."),
    (3, ["庚", "辛"], "卯: 庚辛."),
    (4, ["丙", "甲"], "辰: 丙甲."),
    (5, ["辛"], "巳: 辛."),
    (6, ["庚"], "午: 庚."),
    (7, ["庚", "辛", "甲"], "未: 庚辛甲."),
    (8, ["丁"], "申: 丁."),
    (9, ["辛"], "酉: 辛."),
    (10, ["辛", "甲"], "戌: 辛甲."),
    (11, ["庚", "辛"], "亥: 庚辛."),
    (0, ["辛", "丙"], "子: 辛丙."),
    (1, ["丙", "辛"], "丑: 丙辛."),
])

# 渊海子平 / 三命通会: tallo → fu, órgano, patrones, enfermedades nombradas por el tratado
ZANGFU = {
    "甲": {
        "fu": "vesícula", "zang": "hígado-simbólico (yang)",
        "tejidos": "tendones, cabeza, ojos, costado izquierdo",
        "emocion": "ira",
        "patrones": ["肝气郁结", "胆火上炎", "头痛目眩"],
        "enfermedades_tratado": [
            "jaqueca y vértigo",
            "tensión en tendones y cuello",
            "problemas de vesícula y digestión grasa",
            "hipertensión de patrón hígado (no cifra de consultorio)",
            "ojo seco o rojo de patrón viento-madera",
        ],
    },
    "乙": {
        "fu": "hígado", "zang": "hígado-yin",
        "tejidos": "tendones, uñas, ojos, nervios",
        "emocion": "ira contenida",
        "patrones": ["肝血不足", "肝风内动", "抑郁不舒"],
        "enfermedades_tratado": [
            "fatiga visual y ojo seco",
            "espasmo, hormigueo, temblor menor",
            "ciclo irregular de patrón hígado",
            "ánimo bajo con pecho trabado",
            "uñas quebradizas",
        ],
    },
    "丙": {
        "fu": "intestino delgado", "zang": "corazón-yang",
        "tejidos": "vasos, lengua, sudor",
        "emocion": "excitación",
        "patrones": ["心火亢盛", "小肠湿热", "失眠烦躁"],
        "enfermedades_tratado": [
            "insomnio y palpitación de calor",
            "aftas, lengua roja, sed",
            "sudor fácil",
            "inflamación de intestino delgado de patrón calor",
            "erupción o forúnculo de fuego",
        ],
    },
    "丁": {
        "fu": "corazón", "zang": "corazón-yin / shen",
        "tejidos": "sangre, vasos, lengua",
        "emocion": "gozo que no cierra",
        "patrones": ["心阴虚", "心神不宁", "血虚失眠"],
        "enfermedades_tratado": [
            "insomnio fino, memoria corta",
            "ansiedad con calor de palmas",
            "circulación irregular, palpitación",
            "anemia de patrón sangre (no laboratorio)",
            "boca seca nocturna",
        ],
    },
    "戊": {
        "fu": "estómago", "zang": "tierra-yang",
        "tejidos": "músculo, boca, piel gruesa",
        "emocion": "rumia",
        "patrones": ["胃热", "胃寒", "食积"],
        "enfermedades_tratado": [
            "gastritis de patrón calor o frío según mes",
            "reflujo, hinchazón, mal aliento",
            "estreñimiento o hambre rara",
            "úlcera de patrón estómago en la literatura popular",
            "encía hinchada",
        ],
    },
    "己": {
        "fu": "bazo", "zang": "bazo-yin",
        "tejidos": "carne, labios, pensamiento",
        "emocion": "preocupación",
        "patrones": ["脾虚湿困", "痰湿", "中气下陷"],
        "enfermedades_tratado": [
            "digestión lenta, heces sueltas",
            "edema blando, pesadez",
            "azúcar inestable de patrón bazo (no cifra)",
            "cansancio que no se va con café",
            "pensamiento que da vueltas y no cierra",
        ],
    },
    "庚": {
        "fu": "intestino grueso", "zang": "pulmón-yang",
        "tejidos": "piel, pelo, nariz, hueso",
        "emocion": "pena seca",
        "patrones": ["大肠燥结", "肺热", "皮肤干燥"],
        "enfermedades_tratado": [
            "estreñimiento seco",
            "tos seca, garganta irritada",
            "piel agrietada, dermatitis seca",
            "sinusitis de patrón sequedad-calor",
            "dolor óseo de metal calcinado",
        ],
    },
    "辛": {
        "fu": "pulmón", "zang": "pulmón-yin",
        "tejidos": "piel, nariz, voz",
        "emocion": "pena",
        "patrones": ["肺阴虚", "鼻鼽", "金寒水冷"],
        "enfermedades_tratado": [
            "rinitis, sinusitis, alergia nasal",
            "tos crónica de frío o de sequedad",
            "asma de patrón pulmón en la literatura popular",
            "voz que se corta",
            "piel pálida que pica",
        ],
    },
    "壬": {
        "fu": "vejiga", "zang": "riñón-yang",
        "tejidos": "hueso, oído, pelo, agua del cuerpo",
        "emocion": "miedo",
        "patrones": ["肾阳虚", "水湿泛滥", "膀胱气化不利"],
        "enfermedades_tratado": [
            "lumbago frío, rodilla fría",
            "edema, orina frecuente o trabada",
            "impotencia / frigidez de patrón yang débil (nombre de tratado)",
            "vértigo de agua que no baja",
            "sordera o acúfeno de riñón",
        ],
    },
    "癸": {
        "fu": "riñón", "zang": "riñón-yin / jing",
        "tejidos": "médula, oído, reproductor, dientes",
        "emocion": "miedo fino",
        "patrones": ["肾阴虚", "精亏", "虚火上炎"],
        "enfermedades_tratado": [
            "calor de cinco palmas, sudor nocturno",
            "infertilidad de patrón jing (nombre de tratado)",
            "diente flojo, pelo que cae temprano",
            "tinnitus, memoria que falla",
            "sequedad interna con calor fantasma",
        ],
    },
}

# 食疗 + hierbas nombradas. Sin gramos de tratamiento.
SHILIAO = {
    "甲": {
        "alimentos": ["verdura de hoja verde", "apio", "brotes", "vinagre en punta", "hígado/vesícula de animal (tradición)"],
        "hierbas": ["薄荷", "菊花", "柴胡", "决明子", "夏枯草"],
        "te": "菊花 + 枸杞, corto. No en ayuno largo.",
        "evitar": ["picante de más", "fritura", "alcohol a diario", "ira de estómago vacío"],
    },
    "乙": {
        "alimentos": ["espinaca", "mora", "sésamo negro", "naba", "huevo"],
        "hierbas": ["当归", "白芍", "枸杞", "酸枣仁", "玫瑰花"],
        "te": "玫瑰花 + 枸杞.",
        "evitar": ["picante seco", "noche en vela", "viento en la nuca"],
    },
    "丙": {
        "alimentos": ["loto", "sandía en mesura", "tomate", "amargo corto (melón amargo)", "pescado blanco"],
        "hierbas": ["莲子", "竹叶", "麦冬", "丹参", "栀子"],
        "te": "莲子 + 麦冬.",
        "evitar": ["picante, alcohol, siesta al sol, pantalla hasta tarde"],
    },
    "丁": {
        "alimentos": ["azufaifo 红枣", "longan", "zanahoria", "corazón de animal (tradición)", "arroz"],
        "hierbas": ["酸枣仁", "百合", "龙眼肉", "生地", "阿胶"],
        "te": "酸枣仁 + 百合.",
        "evitar": ["café de noche", "amargo extremo si ya hay vacío"],
    },
    "戊": {
        "alimentos": ["mijo", "calabaza", "jengibre fresco si el mes es frío", "avena", "carne magra"],
        "hierbas": ["生姜", "陈皮", "砂仁", "半夏", "黄连"],
        "te": "陈皮 + 生姜 (mes frío) o 竹叶 (mes caliente).",
        "evitar": ["hielo, crudo de moda, comer de pie, tumbarse justo después"],
    },
    "己": {
        "alimentos": ["ñame 山药", "mijo", "azufaifo", "calabaza", "lenteja"],
        "hierbas": ["茯苓", "白术", "山药", "芡实", "薏苡仁"],
        "te": "山药 + 茯苓 + 芡实 (四神汤 casera, no receta de consulta).",
        "evitar": ["lácteo frío", "dulce industrial", "preocuparse comiendo"],
    },
    "庚": {
        "alimentos": ["pera", "miel", "rábano blanco", "arroz", "pollo"],
        "hierbas": ["杏仁", "枇杷叶", "麦冬", "玄参", "火麻仁"],
        "te": "雪梨 + 麦冬.",
        "evitar": ["picante, humo, aire acondicionado en la cara"],
    },
    "辛": {
        "alimentos": ["pera", "lirio 百合", "hongo blanco 银耳", "nabo", "clara"],
        "hierbas": ["百合", "沙参", "玉竹", "桑叶", "桔梗"],
        "te": "百合 + 银耳.",
        "evitar": ["humo, sequedad de calefacción, llanto contenido sin aire"],
    },
    "壬": {
        "alimentos": ["poroto negro", "nuez", "cordero en invierno", "hueso largo", "sal en punta"],
        "hierbas": ["肉桂", "杜仲", "菟丝子", "补骨脂", "艾叶"],
        "te": "杜仲 + 枸杞 (invierno). No en verano de fuego alto.",
        "evitar": ["baño helado", "sentarse en frío", "sexo a destajo según el tratado"],
    },
    "癸": {
        "alimentos": ["sésamo negro", "mora", "poroto negro", "huevo", "pera"],
        "hierbas": ["熟地", "枸杞", "女贞子", "墨旱莲", "龟板"],
        "te": "枸杞 + 熟地 en decocción corta, no diaria sin criterio.",
        "evitar": ["picante que sube fuego vacío", "noche en vela", "sal industrial"],
    },
}

ELEM_SHILIAO = {
    "Madera": SHILIAO["乙"],
    "Fuego": SHILIAO["丁"],
    "Tierra": SHILIAO["己"],
    "Metal": SHILIAO["辛"],
    "Agua": SHILIAO["癸"],
}

ELEM_ZANG = {
    "Madera": ZANGFU["乙"],
    "Fuego": ZANGFU["丁"],
    "Tierra": ZANGFU["己"],
    "Metal": ZANGFU["辛"],
    "Agua": ZANGFU["癸"],
}
