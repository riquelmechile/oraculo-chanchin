<p align="center">
  <img src="assets/maestro-chanchin.svg" alt="Maestro Chanchín, mascota ficticia de Oráculo Chanchín" width="620">
</p>

# Oráculo Chanchín

**Una skill de lectura simbólica comparada que cruza I Ching, BaZi, observación tradicional de la mano, numerología y yangsheng sin vender humo como ciencia.**

> Antes se llamaba `lectura-comparada`. Ahora vive sola, tiene nombre propio y un guardián bastante más memorable.

Oráculo Chanchín toma procedimientos y vocabulario de **clásicos y tratados tradicionales chinos de distintas épocas**, con un núcleo apoyado en el *Zhou Yi* / *I Ching* (周易), el *Huangdi Neijing* (黄帝内经), *Qiongtong Baojian* (穷通宝鉴), *Di Tian Sui* (滴天髓), *Ma Yi Shen Xiang* (麻衣神相) y *Shen Xiang Quan Bian* (神相全编). No todos esos textos son de la misma época ni tienen el mismo estatus: el proyecto los trata como fuentes histórico-culturales y metodológicas, **no como evidencia científica moderna**.

La numerología y la quiromancia occidental se mantienen como capas comparativas auxiliares; no se presentan como parte del canon chino.

## La leyenda del Maestro Chanchín

**El Maestro Chanchín es un personaje ficticio.** No representa a una persona histórica, una escuela religiosa ni una autoridad espiritual real.

La historia del proyecto cuenta que Chanchín es un viejo lector itinerante que viaja con seis líneas de bambú, un cuaderno lleno de tallos celestes y ramas terrestres, y una regla muy sencilla: *si un símbolo no ayuda a formular una mejor pregunta, no sirve de mucho*.

En vez de prometer “ver el futuro”, Chanchín compara mapas simbólicos, busca coincidencias y contradicciones y devuelve una lectura argumentada. La estética toma inspiración libre de la antigua figura china del **wū (巫)** —término histórico asociado a especialistas rituales y mediadores—, pero la mascota es deliberadamente fantástica y contemporánea.

## Qué hace la skill

- **I Ching / Zhou Yi:** construye hexagramas, identifica líneas mutantes, hexagrama nuclear y resultante.
- **BaZi / Cuatro Pilares:** calcula año, mes, día y hora con tallos celestes, ramas terrestres, cinco fases y relaciones internas.
- **Lectura de manos:** separa observación visual de interpretación y cruza rasgos solo cuando son visibles.
- **Yangsheng (养生):** traduce estaciones y cinco fases a hábitos generales de ritmo, siempre como marco cultural y nunca como medicina.
- **Numerología:** agrega una capa comparativa occidental para detectar convergencias o tensiones.
- **Cruce:** prioriza coincidencias entre sistemas, registra divergencias y evita frases genéricas tipo horóscopo.

## I Ching explicado sin humo

El *I Ching* trabaja con una idea simple: una situación se representa con **seis líneas apiladas de abajo hacia arriba**.

- Línea continua `━━━━━━` = **yang**.
- Línea partida `━━  ━━` = **yin**.
- Tres líneas forman un **trigrama**.
- Hay **8 trigramas** básicos.
- Dos trigramas juntos forman un **hexagrama** de seis líneas.
- Las combinaciones tradicionales producen **64 hexagramas**.

Al consultar con monedas o varillas, algunas líneas pueden salir **mutantes**. La skill entonces distingue:

1. **Hexagrama presente:** cómo está estructurada simbólicamente la situación.
2. **Hexagrama nuclear (互卦):** patrón interno formado a partir de las líneas centrales.
3. **Líneas mutantes:** dónde está la tensión o movimiento.
4. **Hexagrama resultante (之卦):** configuración obtenida al invertir las líneas mutantes.

La implementación de `--metodo varillas` reproduce la **distribución probabilística tradicional** de las líneas del método de tallos de milenrama; no pretende simular físicamente todos los pasos manuales con 49 tallos.

Ejemplo:

```bash
python3 scripts/iching.py --pregunta "¿Acepto esta sociedad?" --metodo varillas
```

O con seis líneas ya obtenidas:

```bash
python3 scripts/iching.py --lineas 7,8,9,8,7,6
```

El programa **no decide por la persona**. Organiza símbolos para leer estructura, tensión y cambio.

## BaZi en simple

BaZi (八字, “ocho caracteres”) representa un nacimiento mediante **cuatro pilares**:

| Pilar | Dos caracteres |
|---|---|
| Año | tallo celeste + rama terrestre |
| Mes | tallo celeste + rama terrestre |
| Día | tallo celeste + rama terrestre |
| Hora | tallo celeste + rama terrestre |

Eso da ocho caracteres en total. La skill calcula además cinco fases, relaciones respecto del Amo del Día, tallos ocultos, fuerza aproximada y ciclos. El año y el mes se tratan según **términos solares**, no simplemente con el calendario gregoriano.

```bash
python3 scripts/bazi.py \
  --fecha 1995-02-12 \
  --hora 16:30 \
  --sexo M \
  --tz America/Santiago \
  --lon -70.65
```

Sin hora conocida:

```bash
python3 scripts/bazi.py --fecha 1995-02-12 --sexo M --tz America/Santiago --lon -70.65 --sin-hora
```

## Por qué “comparada”

La skill no acepta una afirmación solo porque “suena bien”. Usa una matriz de cruce:

| Mano | BaZi | Números | Lectura |
|---|---|---|---|
| rasgo visible | dato calculado | dato calculado | convergencia / divergencia / silencio |

Una idea fuerte debería aparecer en más de una capa o estar anclada a un dato concreto. Si una frase podría aplicarle a casi cualquiera, se descarta.

## Fuentes tradicionales

El proyecto parte de textos y familias de textos como:

- **周易 (*Zhou Yi* / I Ching):** tradición de trigramas, hexagramas y cambio.
- **黄帝内经 (*Huangdi Neijing*):** correspondencias estacionales y el marco de yangsheng.
- **穷通宝鉴 (*Qiongtong Baojian*):** lectura climática/estacional dentro de BaZi.
- **滴天髓 (*Di Tian Sui*):** balance y dinámica de cinco fases en tradición de destino.
- **麻衣神相 (*Ma Yi Shen Xiang*):** tradición fisiognómica atribuida a la escuela de Ma Yi.
- **神相全编 (*Shen Xiang Quan Bian*):** compilación de observación de forma, cinco fases y qi/color.

Hay referencias ampliadas en [`docs/FUENTES-CLASICAS.md`](docs/FUENTES-CLASICAS.md) y [`references/fuentes.md`](references/fuentes.md).

## Lo que deliberadamente NO hace

- No diagnostica enfermedades a partir de la mano, BaZi o I Ching.
- No prescribe hierbas, suplementos, dosis ni tratamientos.
- No calcula esperanza de vida con la “línea de la vida”.
- No afirma que una tradición simbólica esté validada por la ciencia moderna.
- No garantiza resultados: pareja, trabajo, dinero, salud o muerte.
- No convierte cada marca de la palma en una patología.

Si una fuente histórica contiene asociaciones médicas o fatalistas, se pueden mencionar **solo como contexto histórico del texto**, no como una afirmación personalizada sobre alguien.

## Instalación como skill

La carpeta raíz ya tiene formato de skill. Para generar el paquete distribuible:

```bash
python3 tools/build_skill.py
```

Salida:

```text
dist/oraculo-chanchin.skill
```

Para validar antes de empaquetar:

```bash
python3 tools/validate.py
python3 scripts/iching.py --validar
```

## Uso recomendado

Una consulta completa puede incluir:

- nombre completo;
- fecha de nacimiento;
- hora de nacimiento si se conoce;
- ciudad de nacimiento;
- sexo requerido por el cálculo tradicional de ciclos;
- foto clara de una o ambas manos;
- una pregunta concreta si se quiere usar I Ching.

La skill separa **observación**, **cálculo** e **interpretación** para que cada conclusión tenga rastreo.

## Estructura

```text
oraculo-chanchin/
├── SKILL.md
├── README.md
├── assets/
│   ├── maestro-chanchin.svg
│   └── plantilla-informe.md
├── docs/
│   ├── COMO-FUNCIONA.md
│   ├── FUENTES-CLASICAS.md
│   └── SEGURIDAD-Y-LIMITES.md
├── references/
├── scripts/
├── tools/
│   ├── build_skill.py
│   └── validate.py
└── dist/
```

## Licencia

Código y documentación propia: MIT. Los títulos clásicos citados pertenecen a sus respectivas tradiciones y ediciones; este repositorio no redistribuye traducciones modernas protegidas completas.
