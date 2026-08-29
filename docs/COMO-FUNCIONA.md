# Cómo funciona Oráculo Chanchín

## 1. Separar dato de interpretación

El proyecto usa tres pasos obligatorios:

1. **Observación:** qué se ve realmente en una imagen o qué datos entregó la persona.
2. **Cálculo:** resultados reproducibles de scripts, fechas y reglas declaradas.
3. **Cruce:** lectura simbólica de convergencias y contradicciones.

La lectura pierde calidad cuando se salta el primer o segundo paso.

## 2. I Ching

El I Ching representa una situación con seis líneas construidas desde abajo hacia arriba.

- yin: línea partida;
- yang: línea continua;
- 3 líneas = trigrama;
- 2 trigramas = hexagrama;
- 8 trigramas básicos;
- 64 hexagramas tradicionales.

Los valores 6, 7, 8 y 9 permiten distinguir líneas estables y mutantes:

| Valor | Tipo | Estado |
|---:|---|---|
| 6 | yin | mutante |
| 7 | yang | estable |
| 8 | yin | estable |
| 9 | yang | mutante |

Cuando una línea muta cambia de yin a yang o de yang a yin para formar la configuración resultante.

### Métodos disponibles

```bash
python3 scripts/iching.py --pregunta "Pregunta" --metodo monedas
python3 scripts/iching.py --pregunta "Pregunta" --metodo varillas
python3 scripts/iching.py --lineas 7,8,9,8,7,6
```

`varillas` usa la distribución probabilística tradicional del método de milenrama (6=1/16, 7=5/16, 8=7/16, 9=3/16). Es una simulación matemática de la distribución, no una representación física del ritual completo.

## 3. BaZi

BaZi organiza año, mes, día y hora en pares de tallos celestes y ramas terrestres.

La implementación toma en cuenta:

- calendario por términos solares;
- cambio de año alrededor de Lichun (立春), no el 1 de enero;
- hora local y ajuste solar cuando se entrega longitud;
- tallos ocultos;
- cinco fases;
- Diez Dioses como relaciones simbólicas respecto del Amo del Día;
- ciclos de diez años según las reglas codificadas.

Los porcentajes y clasificaciones se tratan como resultados de **este modelo**, no como mediciones físicas.

## 4. Mano

La observación de mano parte por calidad de foto y forma general. Recién después pasa a relieves y líneas.

Orden resumido:

1. luz y pose;
2. forma;
3. hueso/carne;
4. zonas amplias;
5. color solo si la iluminación lo permite;
6. palacios/trigramas de la tradición usada;
7. líneas principales;
8. trama fina;
9. comparación entre manos solo si las fotos son comparables.

La skill no acepta equivalencias del tipo “marca X = enfermedad Y”.

## 5. Numerología

La numerología está incluida como **capa comparativa occidental**. No se disfraza de tradición china. Su función dentro del proyecto es aumentar o disminuir la fuerza de una hipótesis simbólica al cruzarla con los otros registros.

## 6. Yangsheng

Yangsheng se usa aquí en sentido cultural: ritmos, estaciones, descanso y moderación. No se usa para diagnosticar ni tratar.

## 7. Regla anti-Barnum

Una lectura debe explicar de dónde salió cada afirmación. Frases que podrían servir para casi cualquier persona se eliminan.

Formato recomendado:

```text
Dato observado/calculado → interpretación limitada → contraste con otra capa
```

No:

```text
"Eres una persona profunda que a veces duda, pero tiene gran potencial."
```
