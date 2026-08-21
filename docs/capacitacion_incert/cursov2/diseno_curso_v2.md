# Diseño de curso — Evaluación de incertidumbre en analizadores de O₃ y NOx (9 h + M8 opcional)

**Versión:** v2 para operadores de red · 2026-08-19  
**Audiencia:** personal técnico de laboratorio/red de monitoreo con base en calibración de analizadores de gases; no se asume dominio previo del GUM.  
**Modalidad:** presencial o virtual sincrónica; siete módulos obligatorios, incluido M6 NOx y M7 como taller integrador evaluado. M8 Monte Carlo es opcional y queda fuera de jornada nominal de 9 h.

## Objetivos de aprendizaje

Al finalizar recorrido obligatorio, participante puede:

1. Explicar cadena de trazabilidad del O₃ —SRP NIST/BIPM, patrón de transferencia y analizador de campo— y distinguir error conocido, corrección, incertidumbre residual y falla.
2. Especificar mensurando, frontera del sistema y condiciones de referencia; formular modelo Beer–Lambert y derivar coeficientes de sensibilidad.
3. Elegir evidencia pertinente —certificado, especificación, QC, verificación, validación, intercomparación o experimento—; clasificar evaluación Tipo A/B; justificar PDF y convertir a incertidumbre estándar.
4. Construir y depurar diagrama causal; desarrollar presupuesto bottom-up o híbrido; declarar cobertura de cifras globales; evitar doble conteo; tratar dependencia y covarianza.
5. Interpretar regresión, residuos, repetición entre ciclos, deriva y datos de desempeño como fuentes de incertidumbre, sin confundirlos con criterios de conformidad.
6. Explicar medición por quimioluminiscencia de NO, distinguir NOx y NO₂ calculado, evaluar convertidor y GPT, formular modelo diferencial con eficiencia/covarianza y diagnosticar línea de muestreo.
7. Combinar y expandir incertidumbre; informar resultado según GUM §7 y QUAM cap. 9; declarar cobertura, condiciones, alcance, redondeo y regla de decisión cuando aplique.
8. Proponer dato externo para contrastar presupuesto y transferir flujo metrológico entre O₃ y NOx.
9. Opcional M8: reconocer cuándo validar propagación GUM mediante Monte Carlo e interpretar estabilidad, intervalos y tolerancia numérica.

## Estructura horaria

| # | Módulo | Duración | Carácter | Fuentes principales |
|---:|---|---:|---|---|
| 1 | Metrología O₃ y trazabilidad | 0:35 | obligatorio | GUM-1 §§3–5; EPA Quality Handbook §12.1; NISTIR 6963; QUAM caps. 2–3 |
| 2 | Modelo de medición: fotometría UV y Beer–Lambert | 0:48 | obligatorio | 40 CFR 50 App. D §4; NISTIR 6963; GUM-6 §§5–6; QUAM caps. 4–6 |
| 3 | Conceptos GUM: evidencia, Tipo A/B, PDFs y combinación | 0:54 | obligatorio | JCGM 100 §§2.3, 4–5; QUAM caps. 7–8 y App. E.1/G |
| 4 | Presupuesto de incertidumbre del analizador O₃ | 1:22 | obligatorio | EN 14625; fabricantes; QUAM caps. 6–8, App. D/E.5/G y ejemplos A1/A6 |
| 5 | Patrones de transferencia: calibración multipunto, deriva y verificación | 1:08 | obligatorio | P1016Y93; Calibrators SOP; CARB v5; GUM-6 §10.6; QUAM §§7.7–7.9 y App. E.4 |
| 6 | NO/NO₂/NOx por quimioluminiscencia | 1:30 | obligatorio | BS EN 14211:2012; EPA NO₂ 2002; GUM/GUM-6; Doval Miñarro; Gluck; Pernigotti |
| 7 | Taller integrador: presupuesto, validación y reporte | 1:25 | obligatorio; cierre evaluado | BIPM.QM-K1 App. 1; KRISS 2024; GUM §7; QUAM caps. 5, 8–9 y ejemplos A5/A7 |
| 8 | Monte Carlo y validación del marco GUM | 0:30 | opcional; fuera de 9 h | JCGM 101/102; QUAM App. E.3/F |

Recorrido obligatorio: **462 min (7 h 42 min)**. Jornada nominal: **540 min (9 h)**. Reserva logística: **78 min**. M8 suma 30 min adicionales fuera de jornada.

## Detalle por módulo

### M1 — Metrología del ozono y cadena de trazabilidad (35 min)
- Cadena SRP, patrón de transferencia y analizador.
- QUAM: error, corrección, incertidumbre residual y falla.
- **Producto:** cadena trazable con correcciones, cobertura y controles.

### M2 — Modelo de medición: fotometría UV y Beer–Lambert (48 min)
- Mensurando fotométrico frente a resultado operacional de estación.
- Beer–Lambert, sensibilidades y fuentes físicas.
- **Producto:** frase completa de mensurando y frontera del sistema.

### M3 — Conceptos GUM: evidencia, Tipo A/B, PDFs y combinación (54 min)
- Selección de evidencia; Tipo A/B; PDFs; cobertura de cifras globales.
- Dependencia, combinación y doble conteo.
- **Producto:** conversiones justificadas y análisis de cobertura.

### M4 — Presupuesto de incertidumbre del analizador O₃ (82 min)
- Diagrama causal depurado y presupuesto documental como primera iteración.
- Modelo `u(c)=sqrt(u0²+(ur·c)²)` y plan híbrido con QC.
- **Producto:** presupuesto, mapa causal y plan de reemplazo experimental.

### M5 — Patrones de transferencia: calibración multipunto, deriva y verificación (68 min)
- Diseño multipunto, regresión, residuos, incertidumbre de predicción y deriva.
- Uso separado de datos para conformidad y para cuantificar incertidumbre.
- **Producto:** decisión documentada y matriz de cobertura.

### M6 — NO/NO₂/NOx por quimioluminiscencia (90 min)
- Detector responde a NO; NO₂ se calcula desde canales NOx y NO.
- Modelo `c(NO₂)=(c(NOx)-c(NO))/ηc`, eficiencia y selectividad del convertidor, GPT, interferencias, línea y covarianza.
- Presupuesto informativo EN 14211 a 104 nmol/mol y caso sintético reproducible.
- **Producto:** tabla GPT/eficiencia, presupuesto NOx, diagnóstico de línea y conclusión.

### M7 — Taller integrador: presupuesto, validación y reporte (85 min)
- Caso KRISS/BIPM a 100 nmol/mol; términos constantes/proporcionales y covarianza.
- Flujo completo: especificar, identificar, cuantificar, depurar, combinar, expandir, informar y revisar.
- Checklist GUM §7 + QUAM cap. 9; validación externa y alcance.
- **Entregable evaluado:** presupuesto + reporte + validación externa + transferencia breve a NOx.

### M8 — Monte Carlo (30 min, opcional)
- Derivadas, perturbación y MCM como métodos complementarios.
- Procedimiento adaptativo, intervalos y validación GUF–MCM.
- Alerta cerca de cero según QUAM App. F.
- **Demostración:** script Beer–Lambert; sin entregable ni requisito de aprobación.

## Materiales

1. `handout/handout_teorico_gum_o3.md` y `handout/handout_no_nox.md`.
2. Dataset multipunto O₃, dataset GPT/convertidor NOx y dataset de línea NOx, con metadata y semillas.
3. Plantillas de presupuesto O₃ y NOx; plantilla NOx soporta covarianza y eficiencia.
4. Caso público KRISS 2024 para M7.
5. Script MCM para M8.
6. Solucionarios M1–M7 para instructor.

## Evaluación del curso

Ejercicios M1–M6 generan evidencia formativa. M7 aporta evidencia de competencia. Rúbrica de 10 puntos:

| Criterio | Puntos |
|---|---:|
| Mensurando, unidad, nivel, condiciones y alcance completos | 1.5 |
| Modelo y vínculo trazable entre fuente, efecto y evidencia | 1.5 |
| Conversión y combinación correctas | 1.5 |
| Cobertura de cifras globales y ausencia de doble conteo | 1.5 |
| Dependencias/covarianza tratadas con signo y justificación | 1.5 |
| Reporte coherente con presupuesto, `u_c`, `U`, `k`, cobertura y redondeo | 1.5 |
| Validación externa y transferencia a NOx pertinentes | 1.0 |
| **Total** | **10.0** |

M8 no afecta aprobación. Cuestionario corto final puede usarse para certificado de asistencia con aprovechamiento.

## Fuentes y control documental

- **QUAM 2012:** guía práctica complementaria; no reemplaza GUM ni crea requisitos EPA/EN. Citas usan páginas editoriales; PDF suma seis páginas preliminares.
- **BS EN 14211:2012:** principio y ejemplo NO₂; anexos E/F/G informativos. Criterio europeo de 15 % se presenta solo en contexto correspondiente.
- **EPA NO₂, febrero de 2002:** guía histórica para GPT y QA/QC; no se presenta como requisito universal vigente.
- **Artículos:** Doval Miñarro et al. (2011), Gluck et al. (2003), Pernigotti et al. (2013). Contextos y límites de transferencia se declaran.
- **APOA-370:** equipo O₃ UV, descartado como fuente instrumental NOx. El manual local APNA-370 (HORIBA Ambient NOx Monitor, 2021) está disponible; el operador debe verificar si corresponde al equipo realmente instalado antes de transferir especificaciones comerciales.
