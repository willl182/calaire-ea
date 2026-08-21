# Evaluación de la propuesta del curso de incertidumbre

## Veredicto 1 — Opus 5

Veredicto: demasiado técnico para audiencia no experta — y además no agnóstico respecto a O₃. Nivel real: posgrado/especialista en metrología.

- No agnóstico: O₃ está en el esqueleto. M1 = jerarquía SRP/NISTIR 6963/EPA QA Handbook; M2 = fotometría UV completa (x = −k_B·T·ln(D)/(σ·L·P), 40 CFR Part 50 App. D); M5 = P1016Y93/CARB App. C; M7 = BIPM.QM-K1/KRISS-SRP5 vs BIPM-SRP27. Solo M3 y partes de M6 transferibles.
- Dificultad: M7 (crítico: 19 min para presupuesto BIPM + covarianza negativa + Welch–Satterthwaite + dos reportes GUM; irrealizable para no expertos) > M2 (derivadas parciales de 5 variables, salto abrupto tras M1) > M6 (validación GUF–MCM, concepto de segundo orden a las 4.5 h de jornada) > M3 (44 min con autocorrelación, arcoseno, covarianza, doble conteo) > M4 > M5 (el mejor calibrado).
- Síntomas transversales: densidad de fuentes abrumadora para aula, prerrequisitos en cascada (M1 dice "sin GUM previo", M7 exige 8 competencias), ejercicios sin margen (M4 pide calcular Y auditar), notación matemática constante sin versión sin fórmulas, cero andamiaje visual.
- Lo que funciona: secciones "Errores frecuentes" (modelo de tono), transiciones entre módulos, honestidad metodológica (SUPUESTO marcados).
- Recomendaciones: definir audiencia primero (para operadores de red sobra ~40%); M7 reducir a un nivel o fijar k=2 o entregar hoja medio resuelta; M2 sustituir derivación por tabla de sensibilidades relativas; M6 mover al final como opcional; agnosticismo: núcleo genérico = M3 + andamiaje M4, resto como "vía O₃".

## Veredicto 2 — claude-gpt

Veredicto: demasiado técnico para audiencia no experta; equilibrado para personal técnico con base cuantitativa previa. Bien estructurado y riguroso; problema es densidad conceptual/matemática para 6 horas introductorias, sobre todo desde M3.

- M1 accesible y adecuado (buena entrada, actividad visual, poca matemática).
- M2 primer salto fuerte: Beer–Lambert molecular, derivadas de 5 variables, comportamiento cerca de D=1; presupone álgebra, logaritmos, cálculo.
- M3 alta densidad: Tipo A/B, s/√n, grados de libertad, autocorrelación, 4-5 PDFs, sensibilidad, covarianza, doble conteo en 44 min. Sobrecarga.
- M4 equilibrado en método, pesado en ejecución: 8 operaciones en 31 min; riesgo de seguir plantilla sin comprender.
- M5 especializado: 3 regresiones + certificados + residuos + 6 criterios en 20 min; depende de prerrequisitos no declarados.
- M6 muy especializado pero mitigado (demo del facilitador); riesgo de que audiencia concluya "GUM falló".
- M7 punto más difícil: covarianza negativa, Welch–Satterthwaite, dos reportes GUM en 19 min. Exigente incluso para curso intermedio.
- Handout (734 líneas): sirve como referencia posterior, no como material introductorio; presentar en dos capas.
- Orden de dificultad: M7 > M6 > M5 > M3 > M2 > M4 > M1.
- No agnóstico: O₃ domina títulos, modelo, SRP, manuales Thermo/HORIBA, BIPM–KRISS, datasets, casos.
- Conclusión: no necesita volverse básico; necesita reducir objetivos obligatorios. Simplificar M7 a completar/interpretar presupuesto ya calculado; dejar derivación completa, autocorrelación, arcoseno, covarianza, W–S y validación GUF–MCM como opcional; ampliar tiempo práctico M3–M5. Con eso pasaría a "equilibrado".

## Conclusión consolidada

Ambos evaluadores convergen: demasiado técnico para no expertos y no agnóstico de O₃. Dificultad concentrada en M7 > M6 > M5/M2 > M3. M1 y M5 mejor calibrados según evaluador; "Errores frecuentes" es la parte más accesible. Recomendaciones convergentes: (1) simplificar M7 a interpretar presupuesto precalculado o fijar k=2; (2) M2 tabla de sensibilidades en vez de derivación; (3) M6 como demo/opcional; (4) handout en dos capas; (5) decisión previa: definir audiencia — metrólogos: sirve tal cual; operadores de red: sobra ~40%.

Decisión posterior del propietario (2026-08-18): crear cursov2 para operadores de red de calidad de aire, sin aplicar agnosticismo (se mantiene O₃); simplificar M7, revaluar M3 (enfocar solo distribuciones/conceptos realmente usados), M6 y M2 se dejan igual.
