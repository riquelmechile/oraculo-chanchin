#!/usr/bin/env python3
"""Vocabulario amplio de tratado: 三命通会 / 黄帝内经 / 穷通宝鉴 / 食疗.

Se nombra. No se dosifica. No es diagnóstico de laboratorio.
"""

from __future__ import annotations

STEMS = list("甲乙丙丁戊己庚辛壬癸")


def _u(*seqs):
    seen = []
    for seq in seqs:
        for x in seq or []:
            if x and x not in seen:
                seen.append(x)
    return seen


ZANGFU = {
    "甲": {
        "fu": "vesícula",
        "zang": "hígado-simbólico (yang)",
        "tejidos": "tendones, cabeza, ojos, costado izquierdo, uñas",
        "emocion": "ira que sale",
        "sentido": "vista",
        "sabor": "ácido",
        "patrones": [
            "肝气郁结", "胆火上炎", "头痛目眩", "肝阳上亢", "风木摇动",
        ],
        "enfermedades_tratado": [
            "jaqueca de sien y coronilla",
            "vértigo de viento-madera",
            "tensión de cuello, hombro y tendón",
            "digestión grasa pesada / amargor de boca",
            "vesícula irritada de patrón fuego",
            "ojo rojo, seco o que lagrimea con viento",
            "hipertensión de patrón hígado (nombre de tratado, no cifra)",
            "insomnio de ira que no baja",
            "costado izquierdo trabado",
            "tinnitus agudo de fuego que sube",
            "uñas estriadas y cutícula irritada",
            "erupción de primavera / picor de viento",
            "calambre al estirar",
            "reflujo cuando se enoja en ayunas",
        ],
    },
    "乙": {
        "fu": "hígado",
        "zang": "hígado-yin / sangre de madera",
        "tejidos": "tendones, uñas, ojos, nervios, ciclo",
        "emocion": "ira contenida",
        "sentido": "vista",
        "sabor": "ácido suave",
        "patrones": [
            "肝血不足", "肝风内动", "抑郁不舒", "血虚生风", "肝肾同源空虚",
        ],
        "enfermedades_tratado": [
            "fatiga visual y ojo seco",
            "visión borrosa al atardecer",
            "espasmo, hormigueo, temblor fino",
            "ciclo irregular de patrón hígado",
            "síndrome premenstrual de pecho trabado",
            "ánimo bajo con suspiro",
            "uñas quebradizas y pálidas",
            "mareo al levantarse",
            "contractura que no suelta",
            "insomnio de sangre que no guarda el shen",
            "sequedad de tendón",
            "caída de pelo de patrón sangre-madera",
            "manos y pies que se duermen",
            "nudo en la garganta (梅核气 de tratado)",
        ],
    },
    "丙": {
        "fu": "intestino delgado",
        "zang": "corazón-yang",
        "tejidos": "vasos, lengua, sudor, cara",
        "emocion": "excitación",
        "sentido": "lengua / habla",
        "sabor": "amargo",
        "patrones": [
            "心火亢盛", "小肠湿热", "失眠烦躁", "火热上炎", "汗出不敛",
        ],
        "enfermedades_tratado": [
            "insomnio de calor que no cierra",
            "palpitación y pulso que se adelanta",
            "aftas, lengua roja, punta de lengua rota",
            "sed y boca amarga",
            "sudor fácil de día",
            "erupción o forúnculo de fuego",
            "orinas oscuras de calor de intestino delgado",
            "cara roja, ojo brillante de más",
            "ansiedad con calor de pecho",
            "hemorroides de patrón calor (nombre popular de tratado)",
            "sangrado de nariz en verano",
            "inflamación de encía",
            "habla rápida que no aterriza",
            "intolerancia al picante y al alcohol",
        ],
    },
    "丁": {
        "fu": "corazón",
        "zang": "corazón-yin / shen",
        "tejidos": "sangre, vasos, lengua, sueño",
        "emocion": "gozo que no cierra",
        "sentido": "lengua",
        "sabor": "amargo suave",
        "patrones": [
            "心阴虚", "心神不宁", "血虚失眠", "虚火扰神", "心肾不交",
        ],
        "enfermedades_tratado": [
            "insomnio fino, se despierta a media noche",
            "memoria corta y palabra que se pierde",
            "ansiedad con calor de palmas y plantas",
            "palpitación de vacío",
            "anemia de patrón sangre (no laboratorio)",
            "boca seca nocturna",
            "sudor nocturno",
            "soñar mucho y despertar cansado",
            "mejillas que se encienden de tarde",
            "circulación irregular de manos frías / pecho caliente",
            "lengua fisurada",
            "pánico breve sin motivo claro",
            "sequedad de piel con calor interno",
            "ciclo escaso de patrón sangre-fuego",
        ],
    },
    "戊": {
        "fu": "estómago",
        "zang": "tierra-yang",
        "tejidos": "músculo, boca, encía, piel gruesa",
        "emocion": "rumia",
        "sentido": "boca",
        "sabor": "dulce",
        "patrones": [
            "胃热", "胃寒", "食积", "胃气上逆", "中焦壅滞",
        ],
        "enfermedades_tratado": [
            "gastritis de calor o de frío según el mes",
            "reflujo y acidez",
            "hinchazón postcomida",
            "mal aliento y encía hinchada",
            "estreñimiento o hambre rara",
            "náusea de estómago que no baja",
            "úlcera de patrón estómago en literatura popular",
            "sed que no se apaga con agua fría",
            "dolor de estómago en ayunas o a las 3 de la tarde",
            "aftas de estómago-fuego",
            "heces secas con olor fuerte",
            "cara hinchada de mañana",
            "intolerancia a crudo y a hielo",
            "comer de pie y luego peso en el centro",
        ],
    },
    "己": {
        "fu": "bazo",
        "zang": "bazo-yin / transporte",
        "tejidos": "carne, labios, pensamiento, párpado",
        "emocion": "preocupación",
        "sentido": "boca",
        "sabor": "dulce suave",
        "patrones": [
            "脾虚湿困", "痰湿", "中气下陷", "湿困思虑", "运化无力",
        ],
        "enfermedades_tratado": [
            "digestión lenta y heces sueltas",
            "edema blando de párpado y tobillo",
            "pesadez de cuerpo y de idea",
            "azúcar inestable de patrón bazo (no cifra)",
            "cansancio que no se va con café",
            "pensamiento que da vueltas y no cierra",
            "flema en garganta al despertar",
            "labios pálidos o bajados",
            "antojo de dulce que empeora la humedad",
            "prolapso de ritmo (cansancio de centro)",
            "regla con flujo pálido y fatiga",
            "moretones fáciles de patrón bazo",
            "hinchazón que empeora con lácteo frío",
            "siesta que deja más pesado",
        ],
    },
    "庚": {
        "fu": "intestino grueso",
        "zang": "pulmón-yang",
        "tejidos": "piel, pelo, nariz, hueso, colon",
        "emocion": "pena seca",
        "sentido": "nariz",
        "sabor": "picante",
        "patrones": [
            "大肠燥结", "肺热", "皮肤干燥", "燥邪伤津", "金实不鸣",
        ],
        "enfermedades_tratado": [
            "estreñimiento seco, hez de cabra",
            "tos seca y garganta raspada",
            "piel agrietada, dermatitis seca",
            "sinusitis de sequedad-calor",
            "dolor óseo de metal calcinado",
            "nariz seca con sangre en costras",
            "voz ronca de calor de pulmón",
            "hemorroides secas de colon",
            "caspa y pelo que se quiebra",
            "asma seca de patrón pulmón (nombre de tratado)",
            "olor corporal metálico / sudor poco",
            "rigidez de hombro y escápula",
            "intolerancia a humo y aire acondicionado",
            "tos que empeora al hablar mucho",
        ],
    },
    "辛": {
        "fu": "pulmón",
        "zang": "pulmón-yin",
        "tejidos": "piel, nariz, voz, poro",
        "emocion": "pena",
        "sentido": "nariz",
        "sabor": "picante suave",
        "patrones": [
            "肺阴虚", "鼻鼽", "金寒水冷", "卫气不固", "燥咳少痰",
        ],
        "enfermedades_tratado": [
            "rinitis, alergia nasal, estornudo al viento",
            "tos crónica de frío o de sequedad",
            "asma de patrón pulmón en literatura popular",
            "voz que se corta",
            "piel pálida que pica",
            "resfrío fácil, poro abierto",
            "sudor espontáneo de wei qi débil",
            "garganta que pica de noche",
            "olfato que baja en estación seca",
            "tristeza que se instala en pecho",
            "tos con poca flema pegajosa",
            "manos que se pelan",
            "intolerancia a luto contenido sin aire",
            "pecho apretado al recoger el otoño",
        ],
    },
    "壬": {
        "fu": "vejiga",
        "zang": "riñón-yang",
        "tejidos": "hueso, oído, pelo, agua del cuerpo, lumbar",
        "emocion": "miedo",
        "sentido": "oído",
        "sabor": "salado",
        "patrones": [
            "肾阳虚", "水湿泛滥", "膀胱气化不利", "命门火衰", "寒水上泛",
        ],
        "enfermedades_tratado": [
            "lumbago frío y rodilla que no entra en calor",
            "edema que deja marca",
            "orina frecuente de noche o trabada de día",
            "impotencia / frigidez de patrón yang débil (nombre de tratado)",
            "vértigo de agua que no baja",
            "sordera o acúfeno grave de riñón",
            "miedo al frío, sobre todo de cintura",
            "diarrea de madrugada (五更泻 de tratado)",
            "infertilidad de patrón yang (nombre de tratado)",
            "pelo que encanece o cae de reserva fría",
            "diente flojo",
            "clarividencia de cansancio: se apaga después del orgasmo o del esfuerzo",
            "humedad en bajo vientre",
            "presión de vejiga con frío de pies",
        ],
    },
    "癸": {
        "fu": "riñón",
        "zang": "riñón-yin / jing",
        "tejidos": "médula, oído, reproductor, dientes, seso",
        "emocion": "miedo fino",
        "sentido": "oído",
        "sabor": "salado suave",
        "patrones": [
            "肾阴虚", "精亏", "虚火上炎", "髓海不足", "水亏火旺",
        ],
        "enfermedades_tratado": [
            "calor de cinco palmas y sudor nocturno",
            "infertilidad de patrón jing (nombre de tratado)",
            "diente flojo, pelo que cae temprano",
            "tinnitus agudo, memoria que falla",
            "sequedad interna con calor fantasma",
            "semen o flujo que se gasta fácil",
            "dolor de talón y de huesos largos",
            "insomnio de vacío con calor de pecho",
            "sequedad vaginal o semen espeso de yin vacío",
            "presión intraoculares de vacío (nombre popular)",
            "encía que recede",
            "vértigo al agacharse",
            "libido que aparece como calor y deja vacío",
            "miedo fino, sobresalto al menor ruido",
        ],
    },
}

SHILIAO = {
    "甲": {
        "alimentos": [
            "hoja verde amarga-ácida", "apio", "brotes", "vinagre en punta",
            "alcachofa", "rúcula", "limón en ensalada", "hígado/vesícula de animal (tradición)",
        ],
        "hierbas": ["薄荷", "菊花", "柴胡", "决明子", "夏枯草", "钩藤", "青皮"],
        "te": "菊花 + 薄荷, corto. No en ayuno largo ni en vacío de bazo.",
        "consejo": "El tratado abre la madera: movimiento, amargo-ácido corto, no freír la ira.",
        "evitar": ["picante de más", "fritura", "alcohol a diario", "ira de estómago vacío", "noche en vela con pantalla"],
    },
    "乙": {
        "alimentos": [
            "espinaca", "mora", "sésamo negro", "naba", "huevo",
            "remolacha", "dátiles rojos en mesura", "gelatina de hueso (tradición)",
        ],
        "hierbas": ["当归", "白芍", "枸杞", "酸枣仁", "玫瑰花", "何首乌", "女贞子"],
        "te": "玫瑰花 + 枸杞 + 白芍. Suave, no amargo extremo.",
        "consejo": "El tratado nutre sangre de madera: dormir, ácido suave, no secar con picante.",
        "evitar": ["picante seco", "noche en vela", "viento en la nuca", "café en ayunas"],
    },
    "丙": {
        "alimentos": [
            "loto", "sandía en mesura", "tomate", "melón amargo",
            "pescado blanco", "pepino", "té verde corto", "clara de huevo",
        ],
        "hierbas": ["莲子", "竹叶", "麦冬", "丹参", "栀子", "连翘", "淡竹叶"],
        "te": "莲子心 + 竹叶 + 麦冬. Corto. No en estómago frío.",
        "consejo": "El tratado baja fuego de corazón: amargo corto, sombra, menos palabra de más.",
        "evitar": ["picante", "alcohol", "siesta al sol", "pantalla hasta tarde", "cordero en verano"],
    },
    "丁": {
        "alimentos": [
            "azufaifo 红枣", "longan", "zanahoria", "arroz",
            "corazón de animal (tradición)", "leche de almendras tibia", "pera cocida",
        ],
        "hierbas": ["酸枣仁", "百合", "龙眼肉", "生地", "阿胶", "柏子仁", "麦冬"],
        "te": "酸枣仁 + 百合 + 龙眼肉 de noche, no a litros.",
        "consejo": "El tratado guarda el shen: yin, dormida real, no más estímulo.",
        "evitar": ["café de noche", "amargo extremo si ya hay vacío", "sexo a destajo según el tratado"],
    },
    "戊": {
        "alimentos": [
            "mijo", "calabaza", "jengibre fresco si el mes es frío",
            "avena", "carne magra", "papa", "sopa de huesos corta",
        ],
        "hierbas": ["生姜", "陈皮", "砂仁", "半夏", "黄连", "竹茹", "麦芽"],
        "te": "陈皮 + 生姜 (mes frío) o 竹叶 + 麦芽 (mes caliente).",
        "consejo": "El tratado baja el centro: comida a horario, cocido, no hielo.",
        "evitar": ["hielo", "crudo de moda", "comer de pie", "tumbarse justo después", "picante + grasa"],
    },
    "己": {
        "alimentos": [
            "ñame 山药", "mijo", "azufaifo", "calabaza", "lenteja",
            "arroz integral en mesura", "poroto adzuki", "jengibre seco en punta si hay frío",
        ],
        "hierbas": ["茯苓", "白术", "山药", "芡实", "薏苡仁", "党参", "甘草"],
        "te": "山药 + 茯苓 + 芡实 (四神汤 casera). No receta de consulta.",
        "consejo": "El tratado seca humedad y levanta el centro: cocido, horario, menos rumia.",
        "evitar": ["lácteo frío", "dulce industrial", "preocuparse comiendo", "fruta helada", "cerveza"],
    },
    "庚": {
        "alimentos": [
            "pera", "miel", "rábano blanco", "arroz", "pollo",
            "sopa de pera y almendra de albaricoque", "espárrago",
        ],
        "hierbas": ["杏仁", "枇杷叶", "麦冬", "玄参", "火麻仁", "桔梗", "瓜蒌"],
        "te": "雪梨 + 麦冬 + 杏仁. No en diarrea.",
        "consejo": "El tratado humecta metal: pera, menos humo, terminar la frase y callar.",
        "evitar": ["picante", "humo", "aire acondicionado en la cara", "hablar a destajo"],
    },
    "辛": {
        "alimentos": [
            "pera", "lirio 百合", "hongo blanco 银耳", "nabo",
            "clara", "pera cocida con miel", "raíz de loto",
        ],
        "hierbas": ["百合", "沙参", "玉竹", "桑叶", "桔梗", "黄芪", "防风"],
        "te": "百合 + 银耳 + 沙参. En frío de piel, 黄芪 + 防风 solo como nombre de tratado.",
        "consejo": "El tratado cierra poro y humecta pulmón: abrigo de cuello, menos pena seca.",
        "evitar": ["humo", "sequedad de calefacción", "llanto contenido sin aire", "viento en la nuca"],
    },
    "壬": {
        "alimentos": [
            "poroto negro", "nuez", "cordero en invierno", "hueso largo",
            "sal en punta", "castaña", "puerro", "canela en comida, no en gramos de consulta",
        ],
        "hierbas": ["肉桂", "杜仲", "菟丝子", "补骨脂", "艾叶", "附子", "鹿茸"],
        "te": "杜仲 + 枸杞 en invierno. No en verano de fuego alto. 附子 y 鹿茸 se nombran, no se indican.",
        "consejo": "El tratado calienta la puerta de la vida: pies, lumbar, comida caliente.",
        "evitar": ["baño helado", "sentarse en frío", "sexo a destajo según el tratado", "crudo de verano en invierno"],
    },
    "癸": {
        "alimentos": [
            "sésamo negro", "mora", "poroto negro", "huevo", "pera",
            "hueso negro / caldo largo (tradición)", "alga en mesura",
        ],
        "hierbas": ["熟地", "枸杞", "女贞子", "墨旱莲", "龟板", "黄精", "山茱萸"],
        "te": "枸杞 + 熟地 en decocción corta, no diaria sin criterio. 龟板 se nombra, no se indica.",
        "consejo": "El tratado guarda jing: dormir, sal justa, no gastar la reserva en vela.",
        "evitar": ["picante que sube fuego vacío", "noche en vela", "sal industrial", "exceso de orgasmo según el tratado"],
    },
}

WUXING = {
    "Madera": {
        "zangfu": "hígado / vesícula",
        "enfermedades": [
            "viento interno", "ojo y tendón", "jaqueca de sien",
            "ciclo trabado", "ira que se vuelve nudo",
        ],
        "hierbas": ["柴胡", "白芍", "薄荷", "菊花", "当归"],
        "alimentos": ["ácido suave", "hoja verde", "brote"],
    },
    "Fuego": {
        "zangfu": "corazón / intestino delgado",
        "enfermedades": [
            "insomnio de calor", "lengua y vaso", "afta",
            "sudor que no cierra", "shen inquieto",
        ],
        "hierbas": ["莲子", "丹参", "酸枣仁", "竹叶", "麦冬"],
        "alimentos": ["amargo corto", "loto", "pera"],
    },
    "Tierra": {
        "zangfu": "bazo / estómago",
        "enfermedades": [
            "humedad", "digestión lenta", "edema blando",
            "flema", "pensamiento que no cierra",
        ],
        "hierbas": ["茯苓", "白术", "陈皮", "山药", "薏苡仁"],
        "alimentos": ["mijo", "calabaza", "ñame", "cocido"],
    },
    "Metal": {
        "zangfu": "pulmón / intestino grueso",
        "enfermedades": [
            "sequedad de piel y colon", "tos", "nariz",
            "pena que se instala", "poro abierto",
        ],
        "hierbas": ["百合", "沙参", "杏仁", "桔梗", "麦冬"],
        "alimentos": ["pera", "rábano blanco", "miel", "hongo blanco"],
    },
    "Agua": {
        "zangfu": "riñón / vejiga",
        "enfermedades": [
            "frío de lumbar", "oído", "edema",
            "reserva gastada", "miedo fino",
        ],
        "hierbas": ["熟地", "枸杞", "杜仲", "菟丝子", "山茱萸"],
        "alimentos": ["poroto negro", "sésamo negro", "nuez", "caldo de hueso"],
    },
}

CLIMA_ENF = {
    "frio": {
        "enfermedades": [
            "frío de centro y de lumbar", "digestión que se apaga",
            "orina clara frecuente", "dolor que mejora con calor",
        ],
        "hierbas": ["生姜", "肉桂", "艾叶", "杜仲"],
        "consejo": "Calor de ritmo: sol de mañana, comida caliente, pies cubiertos.",
    },
    "frio-humedo": {
        "enfermedades": [
            "humedad-frío de bazo", "pesadez", "heces sueltas",
            "rodilla que duele con lluvia",
        ],
        "hierbas": ["生姜", "茯苓", "薏苡仁", "苍术"],
        "consejo": "Calor seco de ritmo: cocido, movimiento, no crudo.",
    },
    "calido": {
        "enfermedades": [
            "calor de corazón y de estómago", "insomnio de verano",
            "afta", "sudor que agota el yin",
        ],
        "hierbas": ["竹叶", "菊花", "麦冬", "莲子"],
        "consejo": "Frescura de ritmo: sombra, agua, menos picante, dormir de verdad.",
    },
    "calido-humedo": {
        "enfermedades": [
            "humedad-calor de centro e intestino", "piel que suda y pica",
            "heces pegajosas", "boca pastosa",
        ],
        "hierbas": ["薏苡仁", "藿香", "佩兰", "黄连"],
        "consejo": "Frescura que no empape: movimiento, comida ligera, no hielo a destajo.",
    },
    "humedo": {
        "enfermedades": [
            "bazo atrapado", "edema", "flema", "pensamiento lento",
        ],
        "hierbas": ["茯苓", "白术", "陈皮", "砂仁"],
        "consejo": "Secar con ritmo: caminar después de comer, menos crudo.",
    },
    "seco": {
        "enfermedades": [
            "pulmón y colon secos", "tos", "piel agrietada", "estreñimiento",
        ],
        "hierbas": ["麦冬", "沙参", "百合", "火麻仁"],
        "consejo": "Humectar de ritmo: pera, menos picante, recoger el día temprano.",
    },
    "templado": {
        "enfermedades": [
            "sin urgencia climática: mandan el tallo y el elemento escaso/saturado",
        ],
        "hierbas": [],
        "consejo": "Sin urgencia de clima. Mandan el elemento escaso y el saturado.",
    },
}

SHISHEN_ENF = {
    "比肩": {
        "enfermedades": ["estancamiento de mismo elemento", "tensión de competencia con iguales", "dolor de hombro y mandíbula"],
        "consejo": "El tratado lee exceso de yo: moverse, no empujar el mismo clavo.",
    },
    "劫财": {
        "enfermedades": ["gasto de sangre/jing por sobrecarga", "insomnio de pelea", "digestión que se salta"],
        "consejo": "El tratado lee saqueo de reserva: comer sentado, no heroísmo.",
    },
    "食神": {
        "enfermedades": ["flema-humedad de buen vivir", "sobrepeso de patrón bazo", "siesta pesada"],
        "consejo": "El tratado lee exceso de alimento-espíritu: menos dulce, más paseo.",
    },
    "伤官": {
        "enfermedades": ["fuego de hígado-corazón", "jaqueca de palabra", "piel que se inflama", "reflujo de crítica"],
        "consejo": "El tratado lee oficial herido: bajar el filo, no tragar la frase caliente.",
    },
    "偏财": {
        "enfermedades": ["estómago irregular", "hígado de horario roto", "sueño de más o de menos"],
        "consejo": "El tratado lee riqueza indirecta en el cuerpo: horario, no picoteo.",
    },
    "正财": {
        "enfermedades": ["preocupación de bazo", "gastritis de cuenta", "cuello rígido de carga"],
        "consejo": "El tratado lee riqueza directa: un frente menos, comida simple.",
    },
    "七杀": {
        "enfermedades": [
            "presión de hígado-yang", "hipertensión de patrón tratado",
            "bruxismo", "insomnio de amenaza",
        ],
        "consejo": "El tratado lee filo: soltar mandíbula, no dormir con la guerra.",
    },
    "正官": {
        "enfermedades": ["pecho trabado de norma", "estreñimiento de contención", "dolor de sien de cargo"],
        "consejo": "El tratado lee oficial: un no limpio vale más que aguantar.",
    },
    "偏印": {
        "enfermedades": ["flema de esquema", "insomnio de idea", "estómago que se cierra pensando"],
        "consejo": "El tratado lee sello chueco: tierra en el plato, menos atajo mental.",
    },
    "正印": {
        "enfermedades": ["humedad de estudio", "párpado pesado", "resfrío de quien no se mueve"],
        "consejo": "El tratado lee sello: caminar el conocimiento, no empacharse.",
    },
}

# 手诊 / 麻衣-adjacent: solo si la foto verifica la marca.
PALMA_ENF = {
    "isla en línea de cabeza": [
        "congestion de pensamiento (tratado de mano)",
        "insomnio de idea si además hay fuego o 伤官",
    ],
    "isla en línea de corazón": [
        "ritmo afectivo quebrado",
        "shen que no guarda si el Amo es fuego",
    ],
    "quiebre en línea de vida": [
        "interrupción de ritmo/vigor, no años de muerte",
        "reserva que se gasta por tramos",
    ],
    "cadena en línea de vida": [
        "digestión y centro inestables si Tierra está débil",
    ],
    "米字 en monte de Venus / thenar": [
        "手诊 popular: vaso-corazón. Solo si la marca es nítida. No es infarto de consultorio.",
    ],
    "cruz en 明堂": [
        "centro de palma trabado: estómago-bazo de tratado si la foto muestra hundido o cruz real",
    ],
    "monte de Luna hinchado": [
        "humedad-flema, sueño pesado, riñón-vejiga de imagen",
    ],
    "meñique corto o bajo": [
        "Metal débil de gesto: voz, cierre, pecho. Cruzar con % de Metal, no diagnosticar pulmón.",
    ],
    "índice que se tuerce a Júpiter": [
        "madera que empuja: hígado-vesícula de imagen + ira de tratado",
    ],
    "trama muy roja": [
        "calor de fuego o de estómago, solo con luz natural. Flash no cuenta.",
    ],
    "trama muy pálida": [
        "vacío de sangre o de yang, solo con luz natural.",
    ],
    "isla en línea de destino": [
        "interrupción de oficio o de eje, cruzar con 伤官 o Metal",
    ],
    "doble línea de vida": [
        "reserva duplicada de tratado: vigor que se reparte, no años extra",
    ],
    "monte de Júpiter alto": [
        "madera que empuja: hígado-vesícula de imagen + mando",
    ],
    "monte de Saturno hundido": [
        "eje de destino flojo: Tierra o riñón de ritmo, no sentencia",
    ],
    "cruz de preocupaciones bajo índice": [
        "rumia de bazo si la foto es nítida",
    ],
    "reja en muñeca": [
        "pulso de reserva: tres rejas nítidas = ritmo, no longevidad",
    ],
}


def paquete(dm: str | None, clima: str, scarce: str, top: str,
            dioses: list[str] | None = None,
            yongshen_faltan: list[str] | None = None) -> dict:
    zf = ZANGFU.get(dm or "", {})
    sl = SHILIAO.get(dm or "", {})
    wx_sc = WUXING.get(scarce, {})
    wx_top = WUXING.get(top, {})
    cl = CLIMA_ENF.get(clima, CLIMA_ENF["templado"])
    dioses = [d for d in (dioses or []) if d in SHISHEN_ENF]
    enf_dios = []
    cons_dios = []
    for d in dioses:
        enf_dios.extend(SHISHEN_ENF[d]["enfermedades"])
        cons_dios.append(f"{d}: {SHISHEN_ENF[d]['consejo']}")

    hierbas = _u(
        sl.get("hierbas"),
        wx_sc.get("hierbas"),
        cl.get("hierbas"),
        *[SHILIAO.get(s, {}).get("hierbas") for s in (yongshen_faltan or [])],
    )
    alimentos = _u(
        sl.get("alimentos"),
        wx_sc.get("alimentos"),
        *[SHILIAO.get(s, {}).get("alimentos") for s in (yongshen_faltan or [])],
    )
    enfermedades = _u(
        zf.get("enfermedades_tratado"),
        wx_sc.get("enfermedades"),
        cl.get("enfermedades"),
        enf_dios,
    )
    patrones = _u(zf.get("patrones"))
    evitar = _u(sl.get("evitar"))
    tes = _u([sl.get("te")], [SHILIAO.get(s, {}).get("te") for s in (yongshen_faltan or [])])
    consejos = _u(
        [sl.get("consejo")],
        [cl.get("consejo")],
        [f"Fase escasa {scarce}: priorizar {', '.join(wx_sc.get('alimentos') or [])}"],
        [f"Fase saturada {top}: no insistir en {wx_top.get('zangfu', top)}"],
        cons_dios,
        [SHILIAO.get(s, {}).get("consejo") for s in (yongshen_faltan or [])],
    )
    return {
        "zangfu": zf,
        "enfermedades": enfermedades,
        "patrones": patrones,
        "hierbas": hierbas,
        "alimentos": alimentos,
        "tes": [t for t in tes if t],
        "evitar": evitar,
        "consejos": [c for c in consejos if c],
        "fase_escasa": scarce,
        "fase_saturada": top,
        "clima": clima,
        "dioses": dioses,
        "nota": (
            "Vocabulario de 三命通会 × 黄帝内经 × 穷通宝鉴 × 食疗. "
            "Se nombra. No se dosifica. No es verdad clínica."
        ),
    }
