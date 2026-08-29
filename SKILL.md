---
name: oraculo-chanchin
description: Use for integrated symbolic reading with I Ching, BaZi/Four Pillars, comparative palm observation, numerology, and Chinese yangsheng. Formerly lectura-comparada. Trigger on I Ching, Yi Jing, 周易, BaZi, 八字, cuatro pilares, lectura de manos, quiromancia, foto de mano, 气色, nueve palacios, numerología, 养生, Huangdi Neijing, Oráculo Chanchín, or requests to cross these systems. Controlled experiment, not truth. Treat all outputs as cultural/symbolic interpretation: never diagnose disease, prescribe herbs or treatment, predict lifespan, or guarantee future outcomes.
---

# Oráculo Chanchín

**Nombre histórico de la skill:** `lectura-comparada`.

Oráculo Chanchín es un sistema de lectura simbólica comparada. Su regla central es:

> **observación → cálculo → cruce → interpretación limitada**

Si falta observación o cálculo, no rellenar el hueco con intuición genérica.

La mascota “Maestro Chanchín” es ficticia. La tradición china citada es real; el personaje no lo es. El encuadre es un **experimento controlado** con IA y cultura ancestral: no constituye verdad, diagnóstico ni destino. Respetar las fuentes; no hablar en nombre de un linaje.

## Fuentes y marco

La capa china toma vocabulario y método de familias textuales como:

- *周易* / *Zhou Yi* / I Ching;
- *黄帝内经* / *Huangdi Neijing*;
- *穷通宝鉴* / *Qiongtong Baojian*;
- *滴天髓* / *Di Tian Sui*;
- *麻衣神相* / *Ma Yi Shen Xiang*;
- *神相全编* / *Shen Xiang Quan Bian*.

No todos esos textos son de la misma época ni tienen igual estatus histórico. Usarlos como fuentes culturales y metodológicas, no como validación científica.

La **numerología** y la **quiromancia occidental** son capas comparativas auxiliares y no deben presentarse como tradición china.

Antes de interpretar, leer el recurso pertinente:

| Situación | Recurso |
|---|---|
| Foto de mano | [observacion-china.md](references/observacion-china.md), luego [quiromancia-china.md](references/quiromancia-china.md) y [quiromancia-occidental.md](references/quiromancia-occidental.md) |
| Fecha de nacimiento | [bazi-interpretacion.md](references/bazi-interpretacion.md) |
| Nombre o fecha para números | [numerologia-significados.md](references/numerologia-significados.md) |
| Ritmo/estación/yangsheng | [yangsheng.md](references/yangsheng.md) y `scripts/tratado.py` |
| Enfermedades y 食疗 de tratado | `python3 scripts/tratado.py --tallo 甲` y [yangsheng.md](references/yangsheng.md) |
| Marca de palma verificable | `python3 scripts/tratado.py --marca "isla en línea de cabeza"` |
| Decisión concreta | sección I Ching de este archivo |
| Siempre | [protocolo-lectura.md](references/protocolo-lectura.md) |
| Informe largo | [plantilla-informe.md](assets/plantilla-informe.md) |
| Origen y límites | [fuentes.md](references/fuentes.md) |

## Datos a pedir si faltan

### Mano

Idealmente ambas manos. Pedir:

- luz natural lateral;
- mano relajada;
- misma distancia y encuadre para comparar;
- indicar cuál es dominante.

No dominante y dominante pueden usarse como contraste tradicional “dado/cultivado”, pero **no** presentarlo como hecho biológico demostrado.

### Carta y números

- nombre completo de nacimiento;
- nombre de uso, si es distinto;
- fecha año-mes-día;
- hora de reloj, si se conoce;
- ciudad de nacimiento;
- sexo M/F si se quiere aplicar la regla tradicional de dirección de Grandes Ciclos codificada en el script.

Sin hora, calcular con `--sin-hora` y declarar que solo hay tres pilares.

Longitudes de referencia (oeste negativo): Santiago -70.65 · Valparaíso -71.63 · Concepción -73.05 · Buenos Aires -58.38 · Ciudad de México -99.13 · Nueva York -74.01 · Madrid -3.70 · Bogotá -74.07 · Lima -77.04.

## Fase 1 — observar la mano

Seguir el orden de [observacion-china.md](references/observacion-china.md):

1. luz y pose;
2. forma general;
3. hueso/carne;
4. zonas amplias y proporciones;
5. color solo si la foto lo permite;
6. palacios/trigramas de la tradición usada;
7. líneas principales;
8. trama fina;
9. contraste entre manos solo si las imágenes son comparables.

Anotar descripciones neutras antes de interpretarlas.

Observar:

- proporción palma/dedos;
- anchura y base;
- dedos y nudillos;
- pulgar y apertura, solo si se ve;
- relieve;
- líneas madre: origen, recorrido, término, profundidad, cortes, ramas, islas;
- trama fina;
- límites de la foto.

No afirmar asimetrías si las fotos tienen luz, pose o escala distintas.

## Fase 2 — calcular, no adivinar

Ejecutar desde la raíz de la skill:

```bash
python3 scripts/carta.py --nombre "Nombre Completo" \
  --usado "Nombre de uso" --fecha 1990-05-12 --hora 14:30 --sexo M \
  --tz America/Santiago --lon -70.65 \
  --pregunta "¿Acepto el socio?" --metodo varillas \
  --marcas "isla en línea de cabeza; meñique corto o bajo"

python3 scripts/bazi.py --fecha 1990-05-12 --hora 14:30 --sexo M \
  --tz America/Santiago --lon -70.65

python3 scripts/numerologia.py --nombre "Nombre Completo" --fecha 1990-05-12

python3 scripts/bazi.py --fecha 1990-05-12 --sexo F \
  --tz America/Santiago --lon -70.65 --sin-hora
```

Tratar la salida como cálculo interno del modelo. Citar porcentajes, valores brutos y ramas concretas cuando sean relevantes.

## Fase 3 — cruzar

Usar una matriz mental o explícita:

| Mano | BaZi | Números | Clasificación |
|---|---|---|---|
| dato observado | dato calculado | dato calculado | convergencia / divergencia / silencio |

Prioridad:

1. convergencias entre dos o tres sistemas;
2. divergencias reales;
3. silencios o hallazgos de una sola capa como matiz.

Una contradicción no se “arregla”: se nombra y se convierte en pregunta.

El bloque `=== Cruce automático ===` de `carta.py` ya ordena convergencias, divergencias y el tratado fusionado. Partir de ahí; no repetir listas enteras si no hay anclaje.

## Fase 4 — redactar

Lectura completa orientativa: 700–1.200 palabras. Consulta puntual: 3–6 frases.

Orden sugerido:

1. eje;
2. mano;
3. carta china;
4. números;
5. convergencias;
6. divergencias;
7. lo que no aparece;
8. yangsheng como marco de ritmo;
9. cierre en pregunta.

Segunda persona, presente, verbos concretos. Evitar “energías” vagas y elogios universales.

## I Ching — para una decisión concreta

Cuando la pregunta es “¿acepto?”, “¿ahora o espero?”, “¿qué tensión hay en esta decisión?”, usar I Ching en vez de fingir que la constitución natal responde todo.

```bash
python3 scripts/iching.py --pregunta "¿Acepto el socio?" --metodo varillas
python3 scripts/iching.py --pregunta "¿Acepto el socio?" --metodo monedas
python3 scripts/iching.py --lineas 7,8,9,8,7,6
python3 scripts/iching.py --validar
```

### Cómo leerlo

- **presente:** hexagrama obtenido;
- **núcleo (互卦):** configuración interior formada por líneas centrales;
- **mutantes:** puntos de cambio;
- **resultante (之卦):** configuración posterior a invertir mutantes.

Sin líneas mutantes, describir la configuración como relativamente estable dentro de este modelo simbólico.

El modo `varillas` simula la distribución tradicional de probabilidades; no reproduce físicamente el procedimiento completo con tallos de milenrama.

El I Ching **no garantiza lo que ocurrirá**. Usarlo para organizar la lectura de una situación y sus cambios posibles.

La salida incluye capa **医易**: zona de cada trigrama, enfermedades de tratado, hierbas y alimentos. Hay que **nombrarlas** en la lectura (presente + núcleo; resultante si hay mutantes). Línea mutante = zona del cuerpo del hexagrama. Cruzar elementos del trigrama con el BaZi.

```bash
python3 scripts/tratado.py --hexagrama 64
```

## Yangsheng

Yangsheng aquí cruza ritmo de estación con el catálogo de tratado. Hay que **nombrar** las enfermedades, patrones, hierbas y alimentos que salen de `bazi.py` / `tratado.py`.

- correr el script y citar tallo, clima, fase escasa y diez dioses;
- listar enfermedades del tratado (no una);
- listar hierbas y tés **sin gramos ni pauta de toma clínica**;
- decir qué evitar según el registro;
- si la foto verifica una marca, cruzarla con `tratado.py --marca`.

No usarlo para:

- vender eso como diagnóstico de laboratorio;
- dar dosis, decocciones en gramos o “toma esto 7 días”;
- indicar abandonar al médico;
- afirmar que un elemento *es* la enfermedad real.

Si una fuente histórica vincula un símbolo con una patología, **nombrar esa asociación** como contenido del tratado. No convertirla en diagnóstico de laboratorio ni en receta.

Antes de leer marcas de la mano, aplicar [FOTO-Y-VERIFICACION.md](docs/FOTO-Y-VERIFICACION.md). Foto insuficiente → no inventar la marca.

## Reglas no negociables

- **Anti-Barnum:** si una frase podría calzarle a casi cualquiera, borrarla.
- Anclar afirmaciones a un rasgo visible o un dato calculado.
- Nombrar contradicciones.
- No inventar lo que una foto no muestra.
- La longitud de la línea de vida **no mide años de vida**.
- Foto verificable + marca nítida: se describe y se puede citar la asociación tradicional (incluida la que suena médica).
- Foto mala: solo el hueco. Cero patología inventada.
- BaZi **sí nombra** órganos, patrones y enfermedades de 三命通会, y hierbas/alimentos de 食疗. Se declara que es vocabulario de tratado.
- Hierbas se **nombran**. No se dosifican. No se indica abandonar al médico.
- No presentar la tradición como validada por ciencia moderna.
- No prometer resultados sobre pareja, trabajo, riqueza, salud o muerte.
- Año BaZi: respetar Lichun/立春 según la implementación; no asumir 1 de enero.
- Mes BaZi: términos solares, no simple mes gregoriano.
- Sin hora: no inventar pilar horario.
- Si se usa ajuste solar, declarar los datos empleados.
- Cerrar lecturas largas con encuadre simbólico.

## Preguntas difíciles

**“¿Cuánto voy a vivir?”**  
No estimar longevidad. Se puede hablar del simbolismo tradicional de reserva/ritmo sin convertirlo en años.

**“¿Me voy a enfermar?” / “¿qué órgano tengo mal?”**  
Leer el mapa de 三命通会 (tallo → zangfu → enfermedades que el tratado nombra) y las hierbas de 食疗. Declarar que es vocabulario de tratado, no diagnóstico. Síntoma real → médico.

**“¿Vuelvo con X?” / “¿me contratan?”**  
No garantizar resultados. Reformular hacia patrones, decisiones, tensiones y opciones.

**“¿Esto es verdad?”**  
Como sistema predictivo validado científicamente, no está demostrado. Como sistema histórico y simbólico, puede usarse para reflexión estructurada si se presenta con transparencia.

## Cierre obligatorio en informes largos

Usar una nota equivalente a:

> Esto es un experimento de interpretación simbólica con IA y tradiciones históricas. No constituye verdad, diagnóstico, evidencia científica ni predicción garantizada.
