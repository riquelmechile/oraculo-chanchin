# Changelog

## 1.5.1 — 2026-08-29

- README reconstruido con identidad narrativa y visual mística del Maestro Chanchín.
- La documentación principal refleja todas las capacidades reales de la rama 1.5.x.
- Sin cambios en la lógica de cálculo respecto de 1.5.0.

## 1.5.0 — 2026-08-29

- Cruce automático BaZi × I Ching × numerología × marcas de palma.
- `carta.py` queda como consulta única (opcional `--pregunta`, `--lineas`, `--marcas`).
- Tratado fusionado prioriza convergencias. Más marcas de palma verificables.


## 1.4.0 — 2026-08-29

- Capa 医易: 8 trigramas y 64 hexagramas con zona, órganos, enfermedades, hierbas y 食疗.
- Líneas mutantes mapean zona del cuerpo del hexagrama.
- `iching.py` imprime presente + núcleo + resultante. `tratado.py --hexagrama N`.


## 1.3.0 — 2026-08-29

- Catálogo ancho de tratado: ~14 enfermedades por tallo, capas de fase, clima y diez dioses.
- 食疗 expandida: más hierbas, tés, alimentos, evitar y consejos de escuela (sin dosis).
- Marcas de palma verificables en `PALMA_ENF` + `scripts/tratado.py --marca`.
- La carta BaZi fusiona tallo + 用神 faltante + elemento escaso + clima + dioses.


## 1.2.0 — 2026-08-29

- Se restaura el vocabulario completo de tratado: zangfu, patrones, enfermedades de 三命通会 y 食疗 (hierbas/alimentos nombrados, no dosificados).
- Los seis “no” quedan como estatuto de verdad (no clínica, no receta, no años de vida, no ciencia moderna, no garantía, no cada marca = patología), no como tijera de contenido.
- Foto verificable: `docs/FOTO-Y-VERIFICACION.md`. Marca nítida se lee; marca no verificable se calla.
- Encuadre de experimento (IA + cultura ancestral, no constituye verdad) se mantiene en README, skill y salida de BaZi.

## 1.1.0 — 2026-08-29

- Primer intento de aplicar límites en código. Quedó corto: recortó el vocabulario que el proyecto necesita.

## 1.0.0

- Lanzamiento público de Oráculo Chanchín (antes `lectura-comparada`).