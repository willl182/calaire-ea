# F-PSEA-15 — Registro de No Conformidad / CAPA

**Código:** F-PSEA-15  
**Nivel:** 4 — Formato / Registro  
**Estado:** placeholder  
**Oleada:** 2  
**Prioridad:** Oleada 2  

---

## Descripción

Formato para registrar no conformidades detectadas en el SGC del PEA y las acciones correctivas/preventivas (CAPA) asociadas. Incluye: descripción de la NC, clasificación (técnica/gestión), análisis de causa raíz, corrección inmediata, acción correctiva planificada, responsable, plazo, verificación de eficacia y cierre. Soporte documental de P-PSEA-16.

---

## Trazabilidad Normativa

| Norma | Cláusula(s) |
|-------|-------------|
| ISO/IEC 17043:2023 | 8.7 |
| ISO 13528:2022 | — |

**Justificación:** Evidencia del ciclo de no conformidad

> Fuente: `trazabilidad_normativa_sgc.md`

---

## Lecciones Aprendidas — EA-PP2026-R1 (Ronda Simple CO/SO₂)

> Identificadas al cierre de R1. Aplicables a Ronda C (semana 22 de junio de 2026) y rondas siguientes.

### Logística y cronograma

| ID | Lección | Acción requerida | Plazo / Documento |
|----|---------|-----------------|-------------------|
| LA-R1-01 | El ingreso de equipos de medición el mismo día de la ronda genera presión de tiempo. Se requiere que los equipos lleguen el día anterior (martes) para garantizar disponibilidad y preparación oportuna. | Incluir como condición obligatoria en paquete pre-ronda y F-PSEA-11 | Antes de Ronda C |
| LA-R1-02 | La llegada tardía del participante desplaza el inicio de calibración y reduce el margen operativo. | Exigir llegada ≤ 8:00 am en I-PSEA-09 y F-PSEA-05; incluir cláusula de gestión de retraso | Antes de Ronda C |

### Aplicativo y gestión de datos

| ID | Lección | Acción requerida | Plazo / Documento |
|----|---------|-----------------|-------------------|
| LA-R1-03 | El sistema de gestión actual no asigna nombres aleatorios a las entradas, lo que puede comprometer la trazabilidad y objetividad de los registros. | Modificar el aplicativo para que genere identificadores aleatorios por entrada | Antes de Ronda C |
| LA-R1-04 | El proceso de descarga y almacenamiento de datos crudos requiere revisión para asegurar integridad y disponibilidad de los registros originales. | Revisar flujo de descarga y almacenamiento; documentar protocolo en I-PSEA-13 o equivalente | Antes de Ronda C |
| LA-R1-05 | Durante sesiones de trabajo o soporte, se debe compartir tanto la pantalla de trabajo como el código aleatorio generado por el aplicativo, para mantener trazabilidad en tiempo real. | Adoptar como práctica estándar en sesiones de soporte técnico y operativo | Inmediato |

### Técnico — Medición de O₃

| ID | Lección | Acción requerida | Plazo / Documento |
|----|---------|-----------------|-------------------|
| LA-R1-06 | Las condiciones de temperatura ambiental pueden influir significativamente en la precisión de las mediciones de O₃. Es necesario revisar y controlar este parámetro antes y durante la ronda. | Establecer criterio de temperatura ambiental aceptable para medición de O₃ en I-PSEA-03 (Control Ambiental) y en checklist F-PSEA-08 | Antes de Ronda C |

### Recursos críticos

| ID | Lección | Acción requerida | Plazo / Documento |
|----|---------|-----------------|-------------------|
| LA-R1-07 | Se requiere asegurar la disponibilidad de **aire cero exclusivo** para calibración, verificación de equipos de EA y generación de ítems de ensayo. El uso compartido puede afectar la trazabilidad y la calidad del ítem PT. | Verificar y reservar suministro de aire cero exclusivo antes de cada ronda; incluir en F-PSEA-08 y F-PSEA-06 | Antes de Ronda C |

### Procedimental y pendientes

| ID | Lección / Pendiente | Acción requerida | Responsable |
|----|---------------------|-----------------|-------------|
| LA-R1-08 | Reunión pendiente con César para discutir y validar los cuatro analitos en consideración para el esquema. | Agendar y ejecutar reunión; documentar acuerdos | `[POR DEFINIR]` |
| LA-R1-09 | Evaluar la actualización del sistema ENVIDAS en un momento posterior, considerando las implicaciones derivadas de la actualización del sistema operativo. | Diferir la actualización; registrar evaluación cuando el contexto de SO esté definido | `[POR DEFINIR]` |

### Planificación — Ronda C

| Campo | Dato |
|-------|------|
| **Denominación** | Ronda C (pendiente asignación de código formal EA-PP2026-RX) |
| **Semana programada** | 22 de junio de 2026 |
| **Criterio de selección** | Semana sin días festivos — minimiza interrupciones |
| **Participantes previstos** | Por definir; incluir UPB (diferido de R2) |
| **Analitos previstos** | Por definir según reunión con César |

---

## Registros de No Conformidad — EA-PP2026-R2

### NC-R2-01 — Fallo de repuestos del generador de O₃

| Campo | Detalle |
|-------|---------|
| **Fecha** | 2026-04-29/30 (ejecución R2) |
| **Ronda** | EA-PP2026-R2 — Fase 1 |
| **Analito afectado** | O₃ |
| **Descripción** | Los repuestos disponibles en el laboratorio para el generador de O₃ no funcionaron. Causaron pérdida de tiempo operativo durante la jornada de medición. |
| **Corrección inmediata** | El equipo fue ajustado y la medición pudo continuar. |
| **Causa raíz (preliminar)** | Repuestos no compatibles o en mal estado; stock de laboratorio no verificado previo a la ronda. |
| **Acción correctiva propuesta** | Verificar estado y compatibilidad de repuestos críticos del generador de O₃ como parte del checklist pre-ronda (F-PSEA-08). Mantener al menos un repuesto validado y probado antes de cada ronda. |
| **Responsable** | `[POR DEFINIR]` |
| **Plazo** | Antes de la siguiente ronda con O₃ |
| **Estado** | Abierta — acción correctiva pendiente de implementación |

---

### NC-R2-02 — GPT de NOx fuera de ajuste

| Campo | Detalle |
|-------|---------|
| **Fecha** | 2026-04-29/30 (ejecución R2) |
| **Ronda** | EA-PP2026-R2 — Fase 1 |
| **Analito afectado** | NO, NO₂ |
| **Descripción** | El convertidor fotolítico (GPT) utilizado para la generación del nivel de NO₂ se encontraba fuera de ajuste al inicio de la jornada de medición. |
| **Corrección inmediata** | El GPT fue ajustado durante la jornada y la medición pudo continuar. |
| **Causa raíz (preliminar)** | Ausencia de verificación funcional del GPT en el protocolo pre-ronda o deriva no detectada entre la última verificación y la jornada de operación. |
| **Acción correctiva propuesta** | Incluir verificación del ajuste del GPT en el checklist pre-ronda (F-PSEA-08). Establecer criterio de aceptación documentado antes de iniciar mediciones con NOx. |
| **Responsable** | `[POR DEFINIR]` |
| **Plazo** | Antes de la siguiente ronda con NOx |
| **Estado** | Abierta — acción correctiva pendiente de implementación |

---

### OBS-R2-01 — Llegada tardía del participante; inicio de ronda desplazado

| Campo | Detalle |
|-------|---------|
| **Fecha** | 2026-04-29/30 (ejecución R2) |
| **Ronda** | EA-PP2026-R2 — Fase 1 |
| **Tipo** | Observación operativa (no conformidad menor) |
| **Descripción** | P1 (SIATA) no llegó a la hora requerida para iniciar calibración. Las mediciones comenzaron alrededor de las 9:00 am, reduciendo el margen operativo de la jornada. |
| **Corrección inmediata** | La ronda se ejecutó con el tiempo disponible. |
| **Acción preventiva propuesta** | Establecer como condición formal en el paquete pre-ronda (I-PSEA-09 y F-PSEA-05) que la llegada del participante no debe ser posterior a las **8:00 am** en jornadas de medición con O₃/NOx. Incluir cláusula de gestión de retraso (inicio forzado o reprogramación). |
| **Responsable** | Coordinación EA |
| **Plazo** | Antes de la siguiente ronda |
| **Estado** | Abierta — acción preventiva pendiente |
