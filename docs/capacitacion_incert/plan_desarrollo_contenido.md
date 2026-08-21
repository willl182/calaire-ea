# Plan de desarrollo de contenido — Curso 8h Incertidumbre O₃

**Versión:** v1 · 2026-08-17
**Base:** `diseno_curso_8h.md` (v2 agnóstico) + evaluaciones `assess_{guides,manuals,normative}.md`

---

## Entregables y estructura de carpetas

```
docs/capacitacion_incert/contenido/
├── handout/
│   └── handout_teorico_gum_o3.md          (T1)
├── datasets/
│   ├── dataset_verificacion_multipunto.csv (T2)
│   ├── dataset_metadata.md                 (T2)
│   └── generar_dataset.R                   (T2)
├── plantillas/
│   ├── plantilla_presupuesto.xlsx          (T3)
│   └── plantilla_presupuesto.R             (T3)
├── scripts/
│   └── demo_mcm_beer_lambert.R             (T4)
├── casos/
│   └── extracto_kriss_2024.md              (T5)
└── modulos/
    ├── M1_trazabilidad.md … M7_taller.md   (T6, uno por módulo)
    └── soluciones/                          (T7, solucionarios instructor)
```

---

## Tareas

### T1 — Handout teórico único
- **Insumos:** `TGuide...md`, `Technical Guide_...md`, hallazgos de `assess_guides.md`.
- **Trabajo:** fusionar (~70 % solape); estructura: conceptos → PDFs → propagación GUF → MCM → validación → reporte. Correcciones obligatorias:
  - Separar citas JCGM 100 (GUM clásico) vs JCGM 101 (Suplemento 1 / MCM) vs JCGM 102.
  - Matizar: "MCM metrológicamente superior" → "preferible cuando modelo no lineal o PDFs asimétricas"; 10⁶ trials fijos → procedimiento adaptativo; Wichmann–Hill → "cualquier generador validado".
  - Validar/corregir algoritmo de muestreo t (verificar contra JCGM 101 §6.4.9).
  - Eliminar oferta de spreadsheet y referencias PT.
- **Ejecutor:** subagente `claude-gpt` #1.
- **Verificación (hilo principal):** revisar citas normativas contra los PDF JCGM del corpus.

### T2 — Dataset sintético
- **Estructura:** cero + 6 niveles (~20/40/70/100/140/180 ppb) × 3 ciclos, ceros pre/post por ciclo, columnas: nivel_nominal, ciclo, lectura_ref, lectura_uut, T_celda (K), P_celda (kPa), flujo (L/min), timestamp. Certificado simulado: pendiente 1.003, intercepto −0.4 ppb, U(X)=a·X+b.
- **Trabajo:** script R generador con semilla fija (reproducible); ruido realista tomado de specs 49i (0.25 ppb RMS), deriva leve inyectada entre ciclos; un residuo de falta de ajuste visible a nivel alto (didáctico).
- **Ejecutor:** hilo principal (R local); no requiere subagente.
- **Verificación:** correr script, comprobar que ejercicios M5/M7 dan resultados "limpios" pedagógicamente.

### T3 — Plantilla de presupuesto
- **Columnas:** componente, descripción, valor, PDF asignada, divisor, u estándar, unidad, c_i, contribución u_i(y), varianza %, ranking. Filas precargadas para caso analizador (M4) y caso patrón (M7). Suma cuadrática, u_c, ν_eff (Welch–Satterthwaite), k, U.
- **Ejecutor:** hilo principal — versión R/csv primero; xlsx con skill `xlsx` después.
- **Verificación:** reproducir presupuesto EN 14625 de ejemplo (u_c=4.3 nmol/mol) como test.

### T4 — Script demo MCM (módulo 6)
- **Contenido:** modelo Beer–Lambert con entradas σ (normal), L (rectangular), T, P (rectangular), D (triangular); GUF analítico vs MCM (M adaptativo); comparación de intervalos con tolerancia δ; gráfico de PDF de salida.
- **Ejecutor:** subagente `claude-gpt` #2 (borrador) + hilo principal corre y valida en R local.

### T5 — Extracto caso KRISS 2024
- **Insumos:** `BIPM.QM-K1_KRISS_2024_copia.pdf` (§§12.4–12.7 presupuestos, §14–15 regresión GLS, §16 estabilidad transporte) + protocolo `BIPM.QM-K1_2.protocol_copia.pdf` App. 1.
- **Trabajo:** extraer tablas de presupuesto (BIPM y KRISS), resultados pendiente/intercepto, cambio pre/post transporte; redactar guía de lectura de 2 páginas para taller M7 con preguntas dirigidas.
- **Ejecutor:** subagente `claude-gpt` #3 (lee PDFs).
- **Verificación:** contrastar cifras extraídas contra el PDF.

### T6 — Guiones de módulo (M1–M7)
- Un archivo por módulo: objetivos específicos, guion de exposición con tiempos, referencias exactas (documento + sección + página según `assess_manuals.md`), enunciado del ejercicio, materiales necesarios.
- **Dependencias:** M3/M6 dependen de T1; M4 de T3; M5 de T2; M6 de T4; M7 de T2+T3+T5.
- **Ejecutor:** hilo principal (requiere coherencia global; no delegar).

### T7 — Solucionarios de instructor
- Solución trabajada de cada ejercicio (M2–M5, M7) usando dataset T2 y plantilla T3.
- **Ejecutor:** hilo principal, tras cerrar T2/T3.

---

## Asignación de subagentes `claude-gpt`

| Subagente | Tarea | Entrada | Salida |
|-----------|-------|---------|--------|
| #1 | T1 handout fusionado | 2 guías .md + assess_guides + PDFs JCGM para citas | `handout_teorico_gum_o3.md` |
| #2 | T4 borrador script MCM | especificación T4 | `demo_mcm_beer_lambert.R` |
| #3 | T5 extracto KRISS | 2 PDFs BIPM | `extracto_kriss_2024.md` |

Paralelos entre sí. Hilo principal: T2, T3, T6, T7 + verificación de todo lo delegado.

## Secuencia

```
Fase 1 (paralelo): subagentes #1, #2, #3  +  hilo principal T2, T3
Fase 2: verificación de #1–#3; correr y ajustar T4; validar dataset/plantilla
Fase 3: T6 guiones M1–M7 (integra todo)
Fase 4: T7 solucionarios + revisión final cruzada contra diseño v2
```

## Criterios de cierre

- Toda cita normativa verificada contra PDF del corpus (JCGM 100/101/102, GUM-6, EN 14625 vía fuentes secundarias marcada como tal).
- Dataset + plantilla + solucionario mutuamente consistentes (mismos números).
- Script MCM corre en R base + 1 dependencia máx.
- Ningún contenido referencia esquemas PT ni datos operativos propietarios.
