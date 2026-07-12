# I-PSEA-11 — Análisis de Datos

**Código:** I-PSEA-11  
**Nivel:** 3b — Instructivo Técnico  
**Estado:** placeholder  
**Cláusulas ISO/IEC 17043:2023:** 7.4.1; ISO 13528:2022 §6  
**Oleada:** 1  
**Prioridad:** 🟠 Alta  

---

## Descripción

Instructivo paso a paso para el análisis de datos de cada ronda de EA. Define la secuencia: (1) revisión de unidades/formato/cifras significativas, (2) gráfico exploratorio (boxplot, densidad kernel), (3) detección de errores groseros (blunders) → exclusión solo con evidencia documentada, (4) Algoritmo A si distribución simétrica razonable, (5) Algoritmo B si n < 15 o asimetría alta, (6) prueba de Grubbs (solo para marcar, nunca para excluir automáticamente). Incluye interfaz con el aplicativo R/Shiny.

---

## Trazabilidad Normativa

| Norma | Cláusula(s) |
|-------|-------------|
| ISO/IEC 17043:2023 | 7.4.1 |
| ISO 13528:2022 | 6 |

**Justificación:** Revisión inicial, outliers, limpieza de datos

> Fuente: `trazabilidad_normativa_sgc.md`
