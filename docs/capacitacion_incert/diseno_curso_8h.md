# Diseño de curso — Evaluación de incertidumbre en analizadores de ozono y patrones de transferencia (6 h)

**Versión:** borrador v2 (agnóstico) · 2026-08-17
**Audiencia:** personal técnico de laboratorio/red de monitoreo con base en calibración de analizadores de gases; no se asume dominio previo del GUM.
**Modalidad:** presencial o virtual sincrónica; 6 módulos + taller integrador. Cada módulo combina exposición corta y ejercicio guiado.

---

## Objetivos de aprendizaje

Al finalizar, el participante puede:

1. Explicar la cadena de trazabilidad del O₃ (SRP NIST/BIPM → patrón de transferencia → analizador de campo) y por qué el O₃ no admite cilindros certificados.
2. Formular el modelo de medición de fotometría UV (Beer–Lambert) y derivar sus coeficientes de sensibilidad.
3. Evaluar componentes Tipo A (repetibilidad, autocorrelación) y Tipo B (especificaciones de fabricante, certificados, aire cero, deriva) asignando la PDF adecuada.
4. Construir un presupuesto de incertidumbre completo para un analizador y para un patrón de transferencia, combinarlo, expandirlo (selección de k) y reportarlo según GUM.
5. Interpretar certificados de calibración y aplicar criterios de calificación, verificación y recertificación de patrones de transferencia (EPA, EN 14625, BIPM).
6. Validar el marco GUM con Monte Carlo en un caso no lineal (demostración).

---

## Estructura horaria (6 h)

| # | Módulo | Duración | Fuentes principales |
|---|--------|----------|---------------------|
| 1 | Metrología del O₃ y cadena de trazabilidad | 0:30 | GUM-1:2023 §§2–4; USEPA Quality Handbook §12.1; NISTIR 6963 |
| 2 | Modelo de medición: fotometría UV y Beer–Lambert | 0:40 | EPA 2023 rule (40 CFR 50 App. D §4); NISTIR 6963 §11; GUM-6 §§5–6 |
| 3 | Conceptos GUM: Tipo A/B, PDFs, sensibilidad | 1:00 | ISO/IEC Guide 98-3 §§4.2–4.3, 5.1–5.2; handout teórico fusionado |
| 4 | Presupuesto del analizador (laboratorio y campo) | 1:10 | Thermo 49i Table 1-1 + Cap. 4; APOA-370 §10.2; EN 14625 (presupuestos tipo lab/campo) |
| 5 | Patrones de transferencia: calibración multipunto, deriva, verificación | 1:00 | P1016Y93 §§4–5, App. A; Calibrators SOP §12; CARB v5apxc §§C.7–C.9; GUM-6 §10.6 |
| 6 | Monte Carlo y validación del GUF (demostración) | 0:30 | Handout teórico; JCGM 102 §§7–8 |
| 7 | Taller integrador: presupuesto de un patrón de transferencia + reporte | 1:10 | BIPM.QM-K1 protocolo App. 1; caso KRISS 2024; GUM §7 |

Total lectivo: 6:00 (descansos aparte: 15 min tras módulo 3, almuerzo tras módulo 4 si jornada completa).

---

## Detalle por módulo

### M1 — Metrología del O₃ y trazabilidad (0:30)
- Por qué O₃ es distinto: inestable, generación dinámica in situ, sin cilindros certificados.
- Jerarquía: SRP (Nivel 1) → patrón de transferencia Nivel 2/3 → analizador de estación.
- Distinción clave: incertidumbre del analizador vs incertidumbre del patrón vs incertidumbre del valor de calibración transferido.
- **Actividad (7 min):** dibujar la cadena de trazabilidad de la propia red y ubicar cada instrumento con su nivel.

### M2 — Modelo de medición (0:40)
- Ecuación Beer–Lambert del fotómetro UV; coeficiente de absorción 304.39 atm⁻¹cm⁻¹ (u = 0.31 %, regla EPA 2023).
- Coeficientes de sensibilidad por derivación directa (L, T, P, D, σ); componentes constante vs proporcional a la concentración.
- Fuentes físicas: pérdida de ozono en líneas, gradientes de temperatura, exactitud de presión, resolución del cociente de intensidades.
- **Ejercicio (10 min):** calcular sensibilidad de x a T y P; discutir signo y magnitud relativa.

### M3 — Conceptos GUM (1:00)
- Tipo A: media, desviación estándar, grados de libertad; efecto de observaciones autocorrelacionadas sobre n efectivo.
- Tipo B: rectangular, normal, t, arcoseno (ciclos térmicos), trapecio curvilíneo (límites redondeados).
- Máxima entropía como criterio de asignación.
- Doble conteo (GUM §4.3.10) y correlación (introducción).
- **Ejercicio (16 min):** convertir specs de un patrón de transferencia comercial (Sabio 2030: ruido 0.6 ppb RMS, deriva <1 ppb/24 h, linealidad ±1 % FS, generador ±1 % setpoint) a incertidumbres estándar con PDF justificada.

### M4 — Presupuesto del analizador (1:10)
- Presupuesto tipo EN 14625: laboratorio (repetibilidad, falta de ajuste, influencias, interferentes) vs campo (añade deriva a cero/span, pureza de aire cero, reproducibilidad).
- Lectura crítica de especificaciones: ruido RMS vs deriva vs linealidad; specs de fabricante ≠ incertidumbres verificadas.
- **Ejercicio central (31 min):** presupuesto Tipo B del Thermo 49i a 120 nmol/mol con specs Table 1-1; comparar contra APOA-370; ranking de contribuciones a la varianza; discusión de qué componentes exigen medición propia (Tipo A) en lugar de spec.

### M5 — Patrones de transferencia: verificación y deriva (1:00)
- Regresión multipunto: pendiente/intercepto, residuos, falta de ajuste (GUM H.3), incertidumbre de predicción.
- Criterios EPA de calificación/verificación/recertificación (P1016Y93); requisitos de repetibilidad entre ciclos.
- Transporte y estabilidad: caso KRISS 2024 (cambio de pendiente pre/post transporte).
- Deriva como componente faltante habitual (GUM-6 §10.6); riesgo de sobre-ajuste (Quality Handbook §12.4).
- Auditoría de campo (CARB): corrección por certificado, % diferencia, límites de aceptación.
- **Ejercicio (20 min):** dataset de verificación multipunto (6 niveles × 3 ciclos + ceros pre/post) → pendiente, residuos, decisión de conformidad.

### M6 — Monte Carlo y validación (0:30)
- GUF vs MCM: cuándo la linealización falla (modelo no lineal, PDFs asimétricas).
- Procedimiento: M trials, muestreo de PDFs, ordenamiento, intervalo de cobertura más corto; procedimiento adaptativo.
- Validación GUF↔MCM con tolerancia numérica δ (JCGM 102 §8).
- **Demostración en vivo (10 min):** script sobre el modelo Beer–Lambert; no es ejercicio individual.

### M7 — Taller integrador (1:10)
- Presupuesto completo de un patrón de transferencia comparado contra un patrón de referencia, siguiendo BIPM.QM-K1 App. 1: componentes constante y proporcional, covarianzas, regresión con incertidumbre en ambos ejes (concepto).
- Datos del caso KRISS 2024 como material de trabajo (comparación real publicada, no propietaria).
- Combinación → U (k según grados efectivos de libertad, Welch–Satterthwaite en versión simplificada) a nivel bajo y alto de concentración.
- **Entregable:** hoja de presupuesto completa + enunciado de reporte conforme GUM §7 (estimado, u, U, k, cobertura).

---

## Materiales a preparar

1. **Handout teórico único**: fusionar `TGuide...` + `Technical Guide_...` (solapan ~70 %); corregir citas normativas (separar JCGM 100 / JCGM 101), matizar afirmaciones ("MCM superior", 10⁶ trials fijos, Wichmann–Hill), validar algoritmo de muestreo t.
2. **Dataset sintético de ejercicios**: cero + 6 niveles × 3 ciclos, ceros pre/post, T, P, flujo, pendiente/intercepto de certificado. Generado para el curso; sin datos operativos de ningún esquema.
3. **Plantilla de presupuesto** (hoja de cálculo o R): componentes, PDF, divisor, c_i, contribución, ranking.
4. **Script de demostración MCM** (módulo 6).
5. **Extracto del caso KRISS 2024** para el taller (tablas de presupuesto y regresión).

## Vacíos identificados (pendientes)

- Documento sectorial vigente sobre certificación de patrones de transferencia de O₃ aplicable localmente (p. ej. normativa nacional de acreditación) — no está en el corpus; el curso cita EPA/EN/BIPM como marcos.
- Covarianzas entre niveles que comparten calibración (JCGM 102 §9.5.3): módulo avanzado opcional, no cabe en 6 h.

## Evaluación del curso

- Ejercicios M3–M5 calificables en sitio (rúbrica simple).
- Entregable M7 = evidencia de competencia.
- Quiz corto final (10 preguntas, conceptos M1–M3) opcional para certificado de asistencia con aprovechamiento.
