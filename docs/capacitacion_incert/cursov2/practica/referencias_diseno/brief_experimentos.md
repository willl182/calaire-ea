# Brief consolidado — Parte práctica cursov2 (incertidumbre O3 / NO-NOx)

Fuente: dos revisiones Opus 5 del curso `docs/capacitacion_incert/cursov2/` y comparación con `contenido/curso_paquete_completo.html`. Fecha: 2026-08-26.

## Diagnóstico
- Las 8 actividades del curso son de escritorio; ninguna toca instrumento. Datasets M5 y M6 sintéticos.
- M4 ya redacta el "plan de reemplazo de filas documentales por evidencia propia" pero nunca lo ejecuta: es el esqueleto de la práctica.
- Estructura horaria (462 min obligatorios) no admite práctica: se añade **Día 2 de laboratorio (6–8 h)**. M7 (entregable evaluado) migra a presupuesto del equipo propio; caso KRISS queda como validación externa/contraste.
- Instrumentos disponibles (contexto red calidad del aire): analizador O3 UV, analizador NOx quimioluminiscencia con convertidor, calibrador-diluidor con generador O3 y GPT, cilindro NO certificado, generador de aire cero, fotómetro patrón / patrón de transferencia certificado.

## Experimentos priorizados

### P1 — jornada mínima viable (Día 2, ~8 h)
- **E1** Ruido y repetibilidad de cero (M3/M4): series 1 s y 1 min en aire cero; s vs s/√n, autocorrelación, u0. 45+20 min.
- **E2** Verificación multipunto O3, 3 ciclos (M5): cero + 6 niveles 20–180 nmol/mol; regresión por ciclo, residuos, estabilidad entre ciclos. 3×60 min.
- **E3** Covarianza medida NO/NOx (M6/M8): ≥60 pares 1 min a NO estable; u(NO2) con ρ=0 vs ρ medido vs s de la diferencia. 60+20 min.
- **E4** GPT y eficiencia de convertidor (M6): titulación 4–5 niveles, 2 días; η y u(η); c_η=−(NOx−NO)/η². 2×90 min. **Niveles a rediseñar** (ver defecto D4).
- **E5** Verificación corrección automática de η en firmware (M6): 30 min.
- **E14** Recorrido documental cadena real (M1): certificados reales SRP/transferencia/analizador. 30 min.
- **E15** Presupuesto híbrido del equipo propio (M7): u(c)=√(u0²+(u_r·c)²) con u0 de E1/E9, u_r de E2/E10; anti-doble-conteo. 90 min. Entregable evaluado.

### P2 — segunda media jornada
- **E6** Transmisión de línea O3 (línea corta patrón vs línea real+filtro). 60 min.
- **E7** Formación NO2 en línea (NO+O3, línea corta/larga/larga caliente). 90 min. Sustituye dataset inverosímil.
- **E9** Calidad de aire cero (3 fuentes). 45 min.
- **E10** Calibración caudales del diluidor contra patrón de flujo. 60 min.
- **E11** Tiempo de respuesta t10/t90 y criterio de estabilización (<1 ppb en 5 min). 30 min.
- **E16** MCM sobre modelo diferencial NO2 con covarianza medida (E3/E4). 30 min.

### P3 — según disponibilidad
- **E8** Deriva cero/span 24 h / 7 d — pasivo, **iniciar ≥7 días antes del curso**. Análisis 30 min en M4.
- **E12** Sensibilidad real a T/P de celda. 40 min.
- **E13** Interferencia de vapor de agua. 60 min.

## Vacíos de protocolo detectados (a resolver en el diseño)
1. Repetibilidad/precisión intermedia sin protocolo: definir réplicas, niveles, promediado, días/operadores, estimador (s pooled/ANOVA).
2. Tiempo de promediado y n de lecturas por punto; n efectivo con autocorrelación (datos 1 min).
3. Orden de puntos multipunto (ascendente/descendente/aleatorio) para separar deriva de falta de ajuste.
4. Purga/acondicionamiento/calentamiento: duraciones y criterio de fin.
5. Verificación de aire cero: procedimiento y especificación.
6. Prueba de fugas y venteo de bypass (advertencia CARB v5 App. C §C.7.2).
7. Prueba de transmisión de línea: montaje, nivel, duración, cálculo de factor.
8. Diferencia sensor–celda de presión.
9. GPT real: exceso de NO, residencia de cámara, estabilización, estabilidad de cilindro; separar eficiencia de selectividad.
10. Falta hoja de registro de campo, checklist de montaje y ficha de seguridad (venteo/destrucción O3, cilindro NO).

## Defectos técnicos a corregir en el material (bloquean práctica)
- **D1 (alto)** `plantilla_presupuesto_nox.R`: suma de 18 filas da u_c=5.61, texto declara 5.5/30.4; discrepancia ~3.5% silenciosa. Añadir nota o corregir.
- **D2 (medio)** M6 §3.4 lista 13 filas; script 18 (faltan presión muestra 0.06, tensión 0.02).
- **D3 (alto)** `plantilla_presupuesto_nox.csv`: c_i=±1 en canales (debe ser ±1/η=±1.031); sin fila de covarianza; `correlacion_grupo` vacía; c_i=104 incoherente en fila eficiencia.
- **D4 (alto)** Diseño GPT del dataset: en N150 el NO residual ≈10 nmol/mol (~6% del inicial) — titulación demasiado profunda. Rediseñar escalera (p.ej. NO 400–450 nmol/mol, NO2 hasta ~80% rango, NO residual holgado).
- **D5 (medio)** `impureza_no2_nmol_mol=0.40` mal dimensionada (típico ~1% del NO ≈400 nmol/mol en cilindro, ~1.6 tras dilución 1:250).
- **D6 (alto)** Dataset línea NOx: NO2 formado ~0.18 nmol/mol vs ~20 nmol/mol según cinética k(NO+O3)≈1.8e−14 cm³/(molécula·s) a 3 s de residencia — ~100× subestimado. Recalcular con cinética de 2.º orden o sustituir por E7.
- **D7 (medio)** Unidades: unificar a nmol/mol (BIPM.QM-K1 §4 desaconseja ppb) en hojas de campo y plantillas.
- **D8 (medio)** Dataset M5 todo conforme con holgura y sin deriva observable: generar al menos un ciclo no conforme para ejercitar la rama de rechazo/estado encontrado.
- **D9 (bajo)** `plantilla_presupuesto_casos.csv`: etiqueta "semiancho/2" errónea (valor 0.05 correcto).
- **D10 (bajo)** M4: k=2 exacto (gl=Inf), no "≈2".

## Criterios/parámetros ya especificados por el curso (reusar)
- Multipunto: 3 ciclos independientes (P1016Y93 §4.4.1/App. A); estabilidad "<1 ppb en 5 min" (USEPA SOP Calibrators §12.3.3.1.7); criterios conformidad: |d|≤1.5 ppb (X≤50), |100d/X|≤3.1% (X>50), pendiente 0.97–1.03, intercepto ±3 ppb, s(pend)<0.0075, s(int)<1.00 ppb.
- Corrección de referencia por certificado X=(I_ref−b)/m antes de comparar; nunca sobrescribir dato crudo.
- Thermo 49i Table 1-1: ruido cero 0.25 ppb RMS (60 s), LDL 0.5, deriva cero <1 ppb/24h, <2 ppb/7d, span <1%/mes, linealidad ±1% FS, 20–30 °C.
- GPT: c_NO,gen = c_cil·q_NO/(q_dil+q_NO); convertidor ~350 °C; cámara ~48 kPa; muestra 0.70 L/min.
