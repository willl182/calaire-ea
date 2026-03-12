# Plan: Implementación Ajustes CALAIRE-APP (minimax25_plan)

**Fecha:** 2026-03-06  
**Origen:** Informe de Revisión No. 2 (César Yate, 2026-02-23)  
**Alcance:** Ajustes funcionales y técnicos del aplicativo estadístico

---

## 1. Resumen Ejecutivo

El aplicativo CALAIRE-APP presenta errores bloqueantes en cálculos de homogeneidad y métodos robustos, además de deficiencias de usabilidad que comprometen la validación externa. El presente plan establece las fases de corrección sin acceso al código fuente.

---

## 2. Hallazgos Críticos a Resolver

| # | Hallazgo | Severidad | Origen |
|---|----------|-----------|--------|
| 1 | Fórmula B.10 no maneja radicando negativo | **Bloqueante** | Lógica aritmética |
| 2 | MADe utiliza datos de homogeneidad | **Bloqueante** | Mezcla de datasets |
| 3 | Selector n ≥ 12 no activa Algoritmo A | **Bloqueante** | Lógica de decisión |
| 4 | Mezcla de zonas de carga | Media | UX/UI |
| 5 | CSV de salida poco legible | Media | Exportación |
| 6 | Tablas de cálculos intermedias ocultas | Media | Visualización |

---

## 3. Fases del Plan

### Fase 1: Correcciones Estadísticas Fundamentales

**Objetivo:** Eliminar errores matemáticos que invalidan resultados.

| # | Tarea | Entregable | Criterio de Éxito |
|---|-------|------------|-------------------|
| 1.1 | Corregir fórmula B.10 para radicandos negativos | Lógica documentada | Si `radicando < 0`, `ss = 0` |
| 1.2 | Aislar cálculo MADe a dataset de participantes | Especificación técnica | No referenciar datos de homogeneidad |
| 1.3 | Implementar switch n < 12 / n ≥ 12 | Regla de negocio documentada | n=11 → MADe/nIQR; n=12 → Algoritmo A |
| 1.4 | Validar cálculos de nIQR y Estabilidad | Verificación | Confirmar funcionamiento correcto |

### Fase 2: Arquitectura de Datos y Trazabilidad

**Objetivo:** Eliminar ambigüedad en origen de datos y garantizar auditabilidad.

| # | Tarea | Entregable | Criterio de Éxito |
|---|-------|------------|-------------------|
| 2.1 | Definir esquema de entrada con campo obligatorio de origen | Especificación | Campo `origen_dato` en estructura de entrada |
| 2.2 | Establecer reglas para series DATOS 1 / DATOS 2 | Documento de lógica | Selección explícita con registro |
| 2.3 | Definir metadatos de corrida | Especificación | Timestamp, versión, dataset fuente por resultado |

### Fase 3: Usabilidad e Interfaz

**Objetivo:** Mejorar experiencia de usuario y facilitar validación externa.

| # | Tarea | Entregable | Criterio de Éxito |
|---|-------|------------|-------------------|
| 3.1 | Separar zonas de carga | Diseño de UI | Tres áreas independientes: homogeneidad, estabilidad, participantes |
| 3.2 | Exponer tablas intermedias | Prototipo visual | Datos de entrada + resultados parciales visibles |
| 3.3 | Rediseñar exportación CSV | Especificación de formato | Archivo legible, reproducible en Excel |

### Fase 4: Validación Técnica

**Objetivo:** Confirmar equivalencia con cálculos de referencia y cerrar hallazgos.

| # | Tarea | Entregable | Criterio de Éxito |
|---|-------|------------|-------------------|
| 4.1 | Construir casos de prueba dorados | Set de datos de validación | n=11, n=12, extremos, NA, series múltiples |
| 4.2 | Comparar resultados app vs Excel manual | Acta de comparación | Diferencias dentro de tolerancia |
| 4.3 | Consolidar evidencia de validación | Informe técnico | Decisión aceptación/rechazo por caso |
| 4.4 | Completar checklist de cierre | Checklist firmado | Todos los items en estado "cerrado" |

---

## 4. Reglas Técnicas Obligatorias

1. **Homogeneidad B.10:** si el radicando es negativo, forzar `ss = 0`
2. **MADe/nIQR/Algoritmo A:** calcular exclusivamente con datos de participantes
3. **Switch por tamaño muestral:** `n < 12` usa MADe/nIQR; `n >= 12` usa Algoritmo A
4. **Trazabilidad mínima:** dataset fuente, serie usada, timestamp y versión de algoritmo

---

## 5. Normativa Referenciada

- ISO 13528:2022 (Anexo B, Sección 9)
- ISO 17043:2023
- NTC ISO/IEC 17025:2017

---

## 6. Dependencias Externas

- Acceso al repositorio del aplicativo (R/Shiny) para implementación de correcciones
- Validación cruzada con César Yate para cierre técnico

---

## 7. Productos Esperados

- `minimax25_plan.md` (este documento)
- Especificaciones técnicas por módulo (Fases 1-3)
- Casos de prueba dorados (Fase 4)
- Acta de validación técnica (Fase 4)
