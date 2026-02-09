# Diccionario de Documentos SGC - CALAIRE-EA

**Creado**: 2026-02-08
**Versión**: 1.0
**Estado**: draft
**Responsable**: Documentation Manager

---

## Objetivo

Este diccionario proporciona información detallada sobre todos los documentos del Sistema de Gestión de Calidad (SGC) del proyecto CALAIRE-EA, incluyendo sus relaciones, responsabilidades, estado y dependencias.

---

## Convenciones

| Campo | Descripción | Valores posibles |
|-------|-------------|------------------|
| **Código** | Identificador único del documento | DG-PSEA-##, P-PSEA-##, I-PSEA-##, F-PSEA-## |
| **Título** | Nombre del documento | Texto descriptivo |
| **Tipo** | Nivel jerárquico del documento | DG, P, I, F |
| **Versión** | Versión actual del documento | v1.0, v1.1, TBD |
| **Estado** | Estado del documento | draft, in_review, approved, obsolete |
| **Responsable** | Rol o persona responsable | QMS Coordinator, PT Provider Lead, TBD |
| **Normas** | Normas asociadas | 17025:2017, 17043:2023, 13528:2022 |
| **Cláusulas** | Cláusulas normativas asociadas | 4.1, 5.3, 7.2.1, etc. |
| **Dependencias** | Documentos de los que depende | Lista de códigos |
| **Dependientes** | Documentos que dependen de este | Lista de códigos |
| **Prioridad** | Prioridad de creación/actualización | Alta, Media, Baja |
| **Esfuerzo** | Estimación de esfuerzo | Horas estimadas |
| **Estado Cumplimiento** | Estado de cumplimiento con norma | cumple, parcial, no_cumple, na |

---

## Documentos Generales (DG)

### DG-PSEA-01: Protocolo Participación EA Gases Contaminantes Criterio

| Campo | Valor |
|-------|-------|
| **Código** | DG-PSEA-01 |
| **Título** | Protocolo Participación EA Gases Contaminantes Criterio |
| **Tipo** | DG |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | PT Provider Lead |
| **Normas** | 17043:2023, 13528:2022 |
| **Cláusulas** | 17043:2023 4-8, 13528:2022 4-11 |
| **Dependencias** | Ninguna |
| **Dependientes** | P-PSEA-01 al P-PSEA-09 |
| **Prioridad** | Alta |
| **Esfuerzo** | 32 horas |
| **Estado Cumplimiento** | TBD |

**Descripción:** Documento marco del esquema de Ensayo de Aptitud (EA) para gases contaminantes criterio, estableciendo objetivos, alcance, estructura, y procedimientos específicos por gas, conforme a ISO/IEC 17043:2023 e ISO 13528:2022.

**Contenido:**
- Objetivo del esquema EA
- Alcance del esquema
- Gases contaminantes criterio (NO-NO2, CO, O3, SO2)
- Estructura del esquema
- Procedimientos específicos por gas
- Procedimientos generales
- Formatos y registros
- Referencias normativas

**Relaciones:**
- **Hijos:** P-PSEA-01 (Protocolo General EA), P-PSEA-02 al P-PSEA-05 (procedimientos por gas), P-PSEA-06 al P-PSEA-09 (procedimientos generales)
- **Input:** Requisitos de 17043 cap. 4-8 y 13528 cap. 4-11

---

## Procedimientos (P)

### P-PSEA-01: Protocolo General EA

| Campo | Valor |
|-------|-------|
| **Código** | P-PSEA-01 |
| **Título** | Protocolo General EA |
| **Tipo** | P |
| **Versión** | v1.0 |
| **Estado** | in_review |
| **Responsable** | PT Provider Lead |
| **Normas** | 17025:2017, 17043:2023 |
| **Cláusulas** | 17025:2017 5.3, 5.4; 17043:2023 5.3, 5.4, 7.2.1 |
| **Dependencias** | DG-PSEA-01 |
| **Dependientes** | P-PSEA-02 al P-PSEA-05, P-PSEA-09 |
| **Prioridad** | Alta |
| **Esfuerzo** | 16 horas (actualización) |
| **Estado Cumplimiento** | parcial |

**Descripción:** Procedimiento que describe el esquema general de Ensayo de Aptitud (EA) para gases contaminantes criterio, incluyendo objetivos, alcance, y estructura del esquema.

**Contenido:**
- Descripción del esquema EA
- Objetivos y alcance
- Estructura del esquema
- Gases contaminantes criterio (NO-NO2, CO, O3, SO2)
- Procedimientos específicos por gas
- Calendario de rondas
- Criterios de participación

**Relaciones:**
- **Padre:** DG-PSEA-01
- **Hijos:** P-PSEA-02 al P-PSEA-05 (procedimientos por gas), P-PSEA-09 (planificación de rondas)
- **Input:** Requisitos de 17025 cap. 5 y 17043 cap. 5, 7.2

---

### P-PSEA-02: Procedimiento de Ensayo de Aptitud para NO-NO2

| Campo | Valor |
|-------|-------|
| **Código** | P-PSEA-02 |
| **Título** | Procedimiento de Ensayo de Aptitud para NO-NO2 |
| **Tipo** | P |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | PT Coordinator |
| **Normas** | 17043:2023 |
| **Cláusulas** | 17043:2023 7.1-7.4 |
| **Dependencias** | DG-PSEA-01, P-PSEA-01 |
| **Dependientes** | Ninguna |
| **Prioridad** | Alta |
| **Esfuerzo** | 10 horas |
| **Estado Cumplimiento** | TBD |

**Descripción:** Procedimiento específico para el Ensayo de Aptitud de óxidos de nitrógeno (NO-NO2), incluyendo rango de concentraciones, procedimientos de medición, y criterios de evaluación de desempeño.

**Contenido:**
- Descripción específica de NO-NO2
- Rango de concentraciones
- Procedimientos de medición
- Calibración de equipos
- Criterios de evaluación de desempeño
- Interpretación de resultados

**Relaciones:**
- **Padre:** DG-PSEA-01, P-PSEA-01
- **Hermanos:** P-PSEA-03 (CO), P-PSEA-04 (O3), P-PSEA-05 (SO2)
- **Input:** Requisitos de 17043 cap. 7.1-7.4

---

### P-PSEA-03: Procedimiento de Ensayo de Aptitud para CO

| Campo | Valor |
|-------|-------|
| **Código** | P-PSEA-03 |
| **Título** | Procedimiento de Ensayo de Aptitud para CO |
| **Tipo** | P |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | PT Coordinator |
| **Normas** | 17043:2023 |
| **Cláusulas** | 17043:2023 7.1-7.4 |
| **Dependencias** | DG-PSEA-01, P-PSEA-01 |
| **Dependientes** | Ninguna |
| **Prioridad** | Alta |
| **Esfuerzo** | 10 horas |
| **Estado Cumplimiento** | TBD |

**Descripción:** Procedimiento específico para el Ensayo de Aptitud de monóxido de carbono (CO), incluyendo rango de concentraciones, procedimientos de medición, y criterios de evaluación de desempeño.

**Contenido:**
- Descripción específica de CO
- Rango de concentraciones
- Procedimientos de medición
- Calibración de equipos
- Criterios de evaluación de desempeño
- Interpretación de resultados

**Relaciones:**
- **Padre:** DG-PSEA-01, P-PSEA-01
- **Hermanos:** P-PSEA-02 (NO-NO2), P-PSEA-04 (O3), P-PSEA-05 (SO2)
- **Input:** Requisitos de 17043 cap. 7.1-7.4

---

### P-PSEA-04: Procedimiento de Ensayo de Aptitud para O3

| Campo | Valor |
|-------|-------|
| **Código** | P-PSEA-04 |
| **Título** | Procedimiento de Ensayo de Aptitud para O3 |
| **Tipo** | P |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | PT Coordinator |
| **Normas** | 17043:2023 |
| **Cláusulas** | 17043:2023 7.1-7.4 |
| **Dependencias** | DG-PSEA-01, P-PSEA-01 |
| **Dependientes** | Ninguna |
| **Prioridad** | Alta |
| **Esfuerzo** | 10 horas |
| **Estado Cumplimiento** | TBD |

**Descripción:** Procedimiento específico para el Ensayo de Aptitud de ozono (O3), incluyendo rango de concentraciones, procedimientos de medición, y criterios de evaluación de desempeño.

**Contenido:**
- Descripción específica de O3
- Rango de concentraciones
- Procedimientos de medición
- Calibración de equipos
- Criterios de evaluación de desempeño
- Interpretación de resultados

**Relaciones:**
- **Padre:** DG-PSEA-01, P-PSEA-01
- **Hermanos:** P-PSEA-02 (NO-NO2), P-PSEA-03 (CO), P-PSEA-05 (SO2)
- **Input:** Requisitos de 17043 cap. 7.1-7.4

---

### P-PSEA-05: Procedimiento de Ensayo de Aptitud para SO2

| Campo | Valor |
|-------|-------|
| **Código** | P-PSEA-05 |
| **Título** | Procedimiento de Ensayo de Aptitud para SO2 |
| **Tipo** | P |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | PT Coordinator |
| **Normas** | 17043:2023 |
| **Cláusulas** | 17043:2023 7.1-7.4 |
| **Dependencias** | DG-PSEA-01, P-PSEA-01 |
| **Dependientes** | Ninguna |
| **Prioridad** | Alta |
| **Esfuerzo** | 10 horas |
| **Estado Cumplimiento** | TBD |

**Descripción:** Procedimiento específico para el Ensayo de Aptitud de dióxido de azufre (SO2), incluyendo rango de concentraciones, procedimientos de medición, y criterios de evaluación de desempeño.

**Contenido:**
- Descripción específica de SO2
- Rango de concentraciones
- Procedimientos de medición
- Calibración de equipos
- Criterios de evaluación de desempeño
- Interpretación de resultados

**Relaciones:**
- **Padre:** DG-PSEA-01, P-PSEA-01
- **Hermanos:** P-PSEA-02 (NO-NO2), P-PSEA-03 (CO), P-PSEA-04 (O3)
- **Input:** Requisitos de 17043 cap. 7.1-7.4

---

### P-PSEA-06: Procedimiento Diseño Estadístico

| Campo | Valor |
|-------|-------|
| **Código** | P-PSEA-06 |
| **Título** | Procedimiento Diseño Estadístico |
| **Tipo** | P |
| **Versión** | v0 |
| **Estado** | TBD |
| **Responsable** | PT Coordinator |
| **Normas** | 13528:2022, 17043:2023 |
| **Cláusulas** | 13528:2022 cap. 5; 17043:2023 7.2.2 |
| **Dependencias** | DG-PSEA-01 |
| **Dependientes** | Ninguna |
| **Prioridad** | Alta |
| **Esfuerzo** | 16 horas |
| **Estado Cumplimiento** | TBD |

**Descripción:** Procedimiento para diseñar el esquema estadístico del EA conforme a ISO 13528:2022, incluyendo consideraciones sobre distribución de datos, número de participantes, y validación de supuestos.

**Contenido:**
- Diseño estadístico del esquema
- Número de participantes requerido
- Distribución de datos
- Simetría de datos
- Asimetría de datos
- Valores atípicos
- Validación de métodos
- Verificación de supuestos

**Relaciones:**
- **Padre:** DG-PSEA-01
- **Hermanos:** P-PSEA-07 (informe resultados), P-PSEA-08 (colusión/falsificación), P-PSEA-09 (planificación)
- **Input:** Requisitos de 13528 cap. 5 y 17043 cap. 7.2.2

---

### P-PSEA-07: Procedimiento Informe Resultados

| Campo | Valor |
|-------|-------|
| **Código** | P-PSEA-07 |
| **Título** | Procedimiento Informe Resultados |
| **Tipo** | P |
| **Versión** | v0 |
| **Estado** | TBD |
| **Responsable** | PT Coordinator |
| **Normas** | 17043:2023 |
| **Cláusulas** | 17043:2023 7.4.3 |
| **Dependencias** | DG-PSEA-01 |
| **Dependientes** | F-PSEA-04 |
| **Prioridad** | Alta |
| **Esfuerzo** | 12 horas |
| **Estado Cumplimiento** | TBD |

**Descripción:** Procedimiento para generar y emitir informes de resultados del EA a los participantes, incluyendo contenido, plazos, y requisitos de distribución, conforme a ISO/IEC 17043:2023.

**Contenido:**
- Generación de informes
- Plantilla de informe
- Contenido del informe
- Resultados de desempeño
- Valor asignado
- Evaluación estadística
- Plazos de entrega
- Canales de comunicación

**Relaciones:**
- **Padre:** DG-PSEA-01
- **Hijos:** F-PSEA-04 (formato informe resultados)
- **Hermanos:** P-PSEA-06 (diseño estadístico), P-PSEA-08 (colusión/falsificación), P-PSEA-09 (planificación)
- **Input:** Requisitos de 17043 cap. 7.4.3

---

### P-PSEA-08: Proc Colusión Falsificacion

| Campo | Valor |
|-------|-------|
| **Código** | P-PSEA-08 |
| **Título** | Proc Colusión Falsificacion |
| **Tipo** | P |
| **Versión** | v0 |
| **Estado** | TBD |
| **Responsable** | QMS Coordinator |
| **Normas** | 17043:2023 |
| **Cláusulas** | 17043:2023 4.1, 7.1 |
| **Dependencias** | DG-PSEA-01 |
| **Dependientes** | Ninguna |
| **Prioridad** | Alta |
| **Esfuerzo** | 10 horas |
| **Estado Cumplimiento** | TBD |

**Descripción:** Procedimiento para prevenir, detectar y manejar casos de colusión y falsificación de resultados en el esquema de EA, asegurando la imparcialidad y validez de los resultados.

**Contenido:**
- Prevención de colusión
- Compromiso de no colusión
- Procedimientos de separación
- Monitoreo de interacciones
- Prevención de falsificación
- Verificación de datos
- Detección de patrones sospechosos
- Validación cruzada
- Tratamiento de anomalías
- Protocolo de acción
- Investigación de anomalías
- Documentación de casos

**Relaciones:**
- **Padre:** DG-PSEA-01
- **Hermanos:** P-PSEA-06 (diseño estadístico), P-PSEA-07 (informe resultados), P-PSEA-09 (planificación)
- **Input:** Requisitos de 17043 cap. 4.1, 7.1

---

### P-PSEA-09: Procedimiento de Planificación Ronda EA

| Campo | Valor |
|-------|-------|
| **Código** | P-PSEA-09 |
| **Título** | Procedimiento de Planificacion Ronda EA |
| **Tipo** | P |
| **Versión** | v1.0 |
| **Estado** | draft |
| **Responsable** | PT Coordinator |
| **Normas** | 17043:2023 |
| **Cláusulas** | 17043:2023 7.2.1 |
| **Dependencias** | DG-PSEA-01, P-PSEA-01 |
| **Dependientes** | F-PSEA-01, F-PSEA-02, F-PSEA-03 |
| **Prioridad** | Alta |
| **Esfuerzo** | 12 horas (expansión) |
| **Estado Cumplimiento** | parcial |

**Descripción:** Procedimiento para planificar cada ronda del esquema de EA, incluyendo cronograma, calendario operativo, asignación de recursos, y actividades de la ronda.

**Contenido:**
- Planificación de rondas
- Cronograma de actividades
- Diseño de la ronda
- Calendario operativo (F-PSEA-01)
- Cronograma detallado (F-PSEA-02)
- Personal asignado
- Equipos requeridos
- Items PT disponibles
- Registro de planificación (F-PSEA-03)

**Relaciones:**
- **Padre:** DG-PSEA-01, P-PSEA-01
- **Hijos:** F-PSEA-01 (calendario tipo), F-PSEA-02 (cronograma detallado), F-PSEA-03 (registro planificación)
- **Input:** Requisitos de 17043 cap. 7.2.1

---

### P-PSEA-10: Procedimiento de Manejo de Items PT

| Campo | Valor |
|-------|-------|
| **Código** | P-PSEA-10 |
| **Título** | Procedimiento de Manejo de Items PT |
| **Tipo** | P |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | PT Coordinator |
| **Normas** | 17025:2017, 17043:2023 |
| **Cláusulas** | 17025:2017 7.7; 17043:2023 7.3.3.1-7.3.4.5 |
| **Dependencias** | DG-PSEA-01, P-PSEA-01, I-PSEA-02 |
| **Dependientes** | F-PSEA-03, F-PSEA-04 |
| **Prioridad** | Alta |
| **Esfuerzo** | 12 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Procedimiento para el manejo seguro y trazable de los items (cilindros de gas) del esquema de EA, desde la producción hasta la entrega a participantes.

**Contenido:**
- Identificación y almacenamiento
- Despacho y recepción
- Evaluación de condición
- Items peligrosos
- Embalaje y etiquetado
- Condiciones de transporte
- Instrucciones de transporte
- Confirmación de entrega

**Relaciones:**
- **Padre:** DG-PSEA-01, P-PSEA-01
- **Hermanos:** P-PSEA-09 (planificación), I-PSEA-02 (producción)
- **Hijos:** F-PSEA-03 (evaluación de condición), F-PSEA-04 (confirmación de entrega)
- **Input:** Requisitos de 17025 cap. 7.7 y 17043 cap. 7.3.3-7.3.4

---

### P-PSEA-11: Procedimiento de Reporte de Resultados

| Campo | Valor |
|-------|-------|
| **Código** | P-PSEA-11 |
| **Título** | Procedimiento de Reporte de Resultados |
| **Tipo** | P |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | PT Coordinator |
| **Normas** | 17025:2017 |
| **Cláusulas** | 17025:2017 7.9 |
| **Dependencias** | DG-PSEA-01 |
| **Dependientes** | Ninguna |
| **Prioridad** | Media |
| **Esfuerzo** | 8 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Procedimiento para reportar resultados de ensayo, asegurando claridad, precisión y cumplimiento con requisitos normativos.

**Contenido:**
- Formato de reportes
- Contenido de resultados
- Criterios de emisión
- Revisión de reportes
- Aprobación de reportes

**Relaciones:**
- **Padre:** DG-PSEA-01
- **Hermanos:** P-PSEA-22 (reportes PT)
- **Input:** Requisitos de 17025 cap. 7.9

---

### P-PSEA-12: Procedimiento de Control Documental

| Campo | Valor |
|-------|-------|
| **Código** | P-PSEA-12 |
| **Título** | Procedimiento de Control Documental |
| **Tipo** | P |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | QMS Coordinator |
| **Normas** | 17025:2017, 17043:2023 |
| **Cláusulas** | 17025:2017 8.3; 17043:2023 8.3 |
| **Dependencias** | DG-PSEA-01 |
| **Dependientes** | Ninguna |
| **Prioridad** | Alta |
| **Esfuerzo** | 10 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Procedimiento para controlar todos los documentos del SGC, incluyendo aprobación, distribución, cambios y actualizaciones.

**Contenido:**
- Control de documentos
- Aprobación de documentos
- Distribución de documentos
- Cambios a documentos
- Versión de documentos
- Control de documentos obsoletos
- Acceso a documentos

**Relaciones:**
- **Padre:** DG-PSEA-01
- **Hermanos:** P-PSEA-13 (control de registros)
- **Input:** Requisitos de 17025 cap. 8.3 y 17043 cap. 8.3

---

### P-PSEA-13: Procedimiento de Control de Registros

| Campo | Valor |
|-------|-------|
| **Código** | P-PSEA-13 |
| **Título** | Procedimiento de Control de Registros |
| **Tipo** | P |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | QMS Coordinator |
| **Normas** | 17025:2017, 17043:2023 |
| **Cláusulas** | 17025:2017 8.4; 17043:2023 7.5.1.1-7.5.1.3, 8.4 |
| **Dependencias** | DG-PSEA-01 |
| **Dependientes** | Ninguna |
| **Prioridad** | Alta |
| **Esfuerzo** | 10 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Procedimiento para controlar todos los registros del SGC, incluyendo identificación, almacenamiento, protección, recuperación, retención y disposición.

**Contenido:**
- Control de registros
- Registros técnicos
- Registro de datos
- Seguimiento de enmiendas
- Almacenamiento de registros
- Retención de registros
- Disposición de registros

**Relaciones:**
- **Padre:** DG-PSEA-01
- **Hermanos:** P-PSEA-12 (control documental)
- **Input:** Requisitos de 17025 cap. 8.4 y 17043 cap. 7.5.1, 8.4

---

### P-PSEA-14: Procedimiento de Gestión de Riesgos

| Campo | Valor |
|-------|-------|
| **Código** | P-PSEA-14 |
| **Título** | Procedimiento de Gestión de Riesgos |
| **Tipo** | P |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | QMS Coordinator |
| **Normas** | 17025:2017, 17043:2023 |
| **Cláusulas** | 17025:2017 8.5; 17043:2023 8.5 |
| **Dependencias** | DG-PSEA-01 |
| **Dependientes** | Ninguna |
| **Prioridad** | Alta |
| **Esfuerzo** | 12 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Procedimiento para identificar, evaluar y tratar riesgos que puedan afectar la validez de los resultados del esquema de EA o la imparcialidad del proveedor de PT.

**Contenido:**
- Identificación de riesgos
- Evaluación de riesgos
- Tratamiento de riesgos
- Revisión de riesgos
- Comunicación de riesgos
- Registros de riesgos

**Relaciones:**
- **Padre:** DG-PSEA-01
- **Hermanos:** P-PSEA-15 (mejora continua), P-PSEA-16 (no conformidades)
- **Input:** Requisitos de 17025 cap. 8.5 y 17043 cap. 8.5

---

### P-PSEA-15: Procedimiento de Mejora Continua

| Campo | Valor |
|-------|-------|
| **Código** | P-PSEA-15 |
| **Título** | Procedimiento de Mejora Continua |
| **Tipo** | P |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | QMS Coordinator |
| **Normas** | 17025:2017, 17043:2023 |
| **Cláusulas** | 17025:2017 8.6; 17043:2023 8.6 |
| **Dependencias** | DG-PSEA-01 |
| **Dependientes** | Ninguna |
| **Prioridad** | Alta |
| **Esfuerzo** | 8 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Procedimiento para mejorar continuamente la eficacia del SGC mediante el uso de política de calidad, objetivos, resultados de auditorías, análisis de datos, acciones correctivas y revisiones por la dirección.

**Contenido:**
- Mejora continua
- Oportunidades de mejora
- Acciones preventivas
- Análisis de tendencias
- Revisión de mejora
- Registros de mejora

**Relaciones:**
- **Padre:** DG-PSEA-01
- **Hermanos:** P-PSEA-14 (gestión de riesgos), P-PSEA-16 (no conformidades)
- **Input:** Requisitos de 17025 cap. 8.6 y 17043 cap. 8.6

---

### P-PSEA-16: Procedimiento de No Conformidades

| Campo | Valor |
|-------|-------|
| **Código** | P-PSEA-16 |
| **Título** | Procedimiento de No Conformidades |
| **Tipo** | P |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | QMS Coordinator |
| **Normas** | 17025:2017, 17043:2023 |
| **Cláusulas** | 17025:2017 8.7; 17043:2023 8.7 |
| **Dependencias** | DG-PSEA-01 |
| **Dependientes** | Ninguna |
| **Prioridad** | Alta |
| **Esfuerzo** | 10 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Procedimiento para manejar no conformidades, incluyendo la identificación, evaluación, corrección, acción correctiva y verificación de eficacia.

**Contenido:**
- Identificación de no conformidades
- Evaluación de no conformidades
- Corrección de no conformidades
- Acciones correctivas
- Verificación de eficacia
- Registros de no conformidades

**Relaciones:**
- **Padre:** DG-PSEA-01
- **Hermanos:** P-PSEA-15 (mejora continua), P-PSEA-17 (auditorías internas)
- **Input:** Requisitos de 17025 cap. 8.7 y 17043 cap. 8.7

---

### P-PSEA-17: Procedimiento de Auditorías Internas

| Campo | Valor |
|-------|-------|
| **Código** | P-PSEA-17 |
| **Título** | Procedimiento de Auditorías Internas |
| **Tipo** | P |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | QMS Coordinator |
| **Normas** | 17025:2017, 17043:2023 |
| **Cláusulas** | 17025:2017 8.8; 17043:2023 8.8 |
| **Dependencias** | DG-PSEA-01 |
| **Dependientes** | Ninguna |
| **Prioridad** | Alta |
| **Esfuerzo** | 12 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Procedimiento para planificar y realizar auditorías internas del SGC, asegurando que el sistema es conforme a los requisitos de 17025/17043 y es efectivamente implementado.

**Contenido:**
- Programa de auditorías
- Planificación de auditorías
- Ejecución de auditorías
- Competencia de auditores
- Informe de auditoría
- Acciones de seguimiento
- Registros de auditorías

**Relaciones:**
- **Padre:** DG-PSEA-01
- **Hermanos:** P-PSEA-16 (no conformidades), P-PSEA-18 (revisión por dirección)
- **Input:** Requisitos de 17025 cap. 8.8 y 17043 cap. 8.8

---

### P-PSEA-18: Procedimiento de Revisión por Dirección

| Campo | Valor |
|-------|-------|
| **Código** | P-PSEA-18 |
| **Título** | Procedimiento de Revisión por Dirección |
| **Tipo** | P |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | Project Lead |
| **Normas** | 17025:2017, 17043:2023 |
| **Cláusulas** | 17025:2017 8.9; 17043:2023 8.9 |
| **Dependencias** | DG-PSEA-01 |
| **Dependientes** | Ninguna |
| **Prioridad** | Alta |
| **Esfuerzo** | 8 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Procedimiento para que la dirección revise el SGC a intervalos planificados, asegurando su continua adecuación, suficiencia y eficacia.

**Contenido:**
- Revisión por dirección
- Frecuencia de revisión
- Entradas de revisión
- Salidas de revisión
- Registros de revisión
- Seguimiento de decisiones

**Relaciones:**
- **Padre:** DG-PSEA-01
- **Hermanos:** P-PSEA-17 (auditorías internas)
- **Input:** Requisitos de 17025 cap. 8.9 y 17043 cap. 8.9

---

### P-PSEA-19: Procedimiento de Monitoreo de Imparcialidad

| Campo | Valor |
|-------|-------|
| **Código** | P-PSEA-19 |
| **Título** | Procedimiento de Monitoreo de Imparcialidad |
| **Tipo** | P |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | QMS Coordinator |
| **Normas** | 17043:2023 |
| **Cláusulas** | 17043:2023 4.1.4-4.1.5 |
| **Dependencias** | DG-PSEA-01 |
| **Dependientes** | Ninguna |
| **Prioridad** | Alta |
| **Esfuerzo** | 8 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Procedimiento para monitorear las actividades del esquema de EA y eliminar amenazas a la imparcialidad del proveedor de PT.

**Contenido:**
- Monitoreo de actividades
- Identificación de amenazas
- Eliminación de amenazas
- Registros de monitoreo
- Comunicación de imparcialidad

**Relaciones:**
- **Padre:** DG-PSEA-01
- **Hermanos:** P-PSEA-02 (confidencialidad)
- **Input:** Requisitos de 17043 cap. 4.1.4-4.1.5

---

### P-PSEA-20: Procedimiento de Comunicación PT

| Campo | Valor |
|-------|-------|
| **Código** | P-PSEA-20 |
| **Título** | Procedimiento de Comunicación PT |
| **Tipo** | P |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | PT Provider Lead |
| **Normas** | 17043:2023 |
| **Cláusulas** | 17043:2023 7.1.2.1-7.1.2.3, 7.3.5.1-7.3.5.2 |
| **Dependencias** | DG-PSEA-01, P-PSEA-01 |
| **Dependientes** | I-PSEA-09 |
| **Prioridad** | Media |
| **Esfuerzo** | 8 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Procedimiento para comunicar información sobre el esquema de EA a los participantes, incluyendo notificación de cambios e instrucciones.

**Contenido:**
- Información del esquema de EA
- Notificación de cambios
- Registros de comunicación
- Notificación anticipada
- Instrucciones a participantes

**Relaciones:**
- **Padre:** DG-PSEA-01, P-PSEA-01
- **Hijos:** I-PSEA-09 (instrucciones a participantes)
- **Input:** Requisitos de 17043 cap. 7.1.2, 7.3.5

---

### P-PSEA-21: Procedimiento de Divulgación de Valores

| Campo | Valor |
|-------|-------|
| **Código** | P-PSEA-21 |
| **Título** | Procedimiento de Divulgación de Valores |
| **Tipo** | P |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | PT Coordinator |
| **Normas** | 17043:2023 |
| **Cláusulas** | 17043:2023 7.2.3.5 |
| **Dependencias** | DG-PSEA-01, P-PSEA-01, I-PSEA-08 |
| **Dependientes** | Ninguna |
| **Prioridad** | Media |
| **Esfuerzo** | 6 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Procedimiento para establecer la política de divulgación del valor asignado a los participantes del esquema de EA.

**Contenido:**
- Política de divulgación
- Criterios de confidencialidad
- Momento de divulgación
- Registros de divulgación

**Relaciones:**
- **Padre:** DG-PSEA-01, P-PSEA-01
- **Hermanos:** I-PSEA-08 (valor asignado)
- **Input:** Requisitos de 17043 cap. 7.2.3.5

---

### P-PSEA-22: Procedimiento de Reportes PT

| Campo | Valor |
|-------|-------|
| **Código** | P-PSEA-22 |
| **Título** | Procedimiento de Reportes PT |
| **Tipo** | P |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | PT Coordinator |
| **Normas** | 17043:2023 |
| **Cláusulas** | 17043:2023 7.4.3.1-7.4.3.7 |
| **Dependencias** | DG-PSEA-01, P-PSEA-01, I-PSEA-11, I-PSEA-12 |
| **Dependientes** | Ninguna |
| **Prioridad** | Alta |
| **Esfuerzo** | 12 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Procedimiento para generar y emitir reportes de resultados del esquema de EA a los participantes, incluyendo contenido, plazos y requisitos de uso.

**Contenido:**
- Requisitos de reporte
- Contenido del reporte
- Plazos de reporte
- Política de uso del reporte
- Reportes enmendados
- Reportes enmendados de subconjuntos
- Declaraciones de participación

**Relaciones:**
- **Padre:** DG-PSEA-01, P-PSEA-01
- **Hermanos:** I-PSEA-11 (análisis de datos), I-PSEA-12 (evaluación de desempeño)
- **Input:** Requisitos de 17043 cap. 7.4.3

---

### P-PSEA-23: Procedimiento de Gestión de Datos

| Campo | Valor |
|-------|-------|
| **Código** | P-PSEA-23 |
| **Título** | Procedimiento de Gestión de Datos |
| **Tipo** | P |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | PT Coordinator |
| **Normas** | 17043:2023 |
| **Cláusulas** | 17043:2023 7.5.2.1-7.5.2.4 |
| **Dependencias** | DG-PSEA-01, I-PSEA-13 |
| **Dependientes** | Ninguna |
| **Prioridad** | Media |
| **Esfuerzo** | 8 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Procedimiento para controlar el acceso a los datos del esquema de EA, incluyendo sistemas externos y validación de sistemas.

**Contenido:**
- Acceso a datos
- Sistemas externos
- Seguridad de datos
- Respaldo de datos

**Relaciones:**
- **Padre:** DG-PSEA-01
- **Hermanos:** I-PSEA-13 (validación de sistemas)
- **Input:** Requisitos de 17043 cap. 7.5.2

---

### P-PSEA-24: Procedimiento de Quejas

| Campo | Valor |
|-------|-------|
| **Código** | P-PSEA-24 |
| **Título** | Procedimiento de Quejas |
| **Tipo** | P |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | QMS Coordinator |
| **Normas** | 17043:2023 |
| **Cláusulas** | 17043:2023 8.10 |
| **Dependencias** | DG-PSEA-01 |
| **Dependientes** | Ninguna |
| **Prioridad** | Alta |
| **Esfuerzo** | 10 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Procedimiento para manejar quejas de los participantes relacionadas con el esquema de EA, incluyendo recepción, evaluación, resolución y comunicación.

**Contenido:**
- Recepción de quejas
- Evaluación de quejas
- Resolución de quejas
- Comunicación de quejas
- Registros de quejas
- Seguimiento de quejas

**Relaciones:**
- **Padre:** DG-PSEA-01
- **Hermanos:** P-PSEA-25 (apelaciones)
- **Input:** Requisitos de 17043 cap. 8.10

---

### P-PSEA-25: Procedimiento de Apelaciones

| Campo | Valor |
|-------|-------|
| **Código** | P-PSEA-25 |
| **Título** | Procedimiento de Apelaciones |
| **Tipo** | P |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | QMS Coordinator |
| **Normas** | 17043:2023 |
| **Cláusulas** | 17043:2023 8.11 |
| **Dependencias** | DG-PSEA-01 |
| **Dependientes** | Ninguna |
| **Prioridad** | Alta |
| **Esfuerzo** | 10 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Procedimiento para manejar apelaciones de los participantes relacionadas con el esquema de EA, incluyendo recepción, evaluación, resolución y comunicación.

**Contenido:**
- Recepción de apelaciones
- Evaluación de apelaciones
- Resolución de apelaciones
- Comunicación de apelaciones
- Registros de apelaciones
- Seguimiento de apelaciones

**Relaciones:**
- **Padre:** DG-PSEA-01
- **Hermanos:** P-PSEA-24 (quejas)
- **Input:** Requisitos de 17043 cap. 8.11

---

### P-PSEA-26 al P-PSEA-30: Procedimientos Duplicados

**Nota:** Los procedimientos P-PSEA-26, P-PSEA-27, P-PSEA-28, P-PSEA-29 y P-PSEA-30 son duplicados de procedimientos existentes (confidencialidad, gestión de competencia, control de acceso, proveedores externos). Estos deben ser eliminados del inventario.

---

## Instructivos (I)

### I-PSEA-01: Instructivo de Caracterización

| Campo | Valor |
|-------|-------|
| **Código** | I-PSEA-01 |
| **Título** | Instructivo de Caracterización |
| **Tipo** | I |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | PT Coordinator |
| **Normas** | 17025:2017, 17043:2023 |
| **Cláusulas** | 17025:2017 6.1.2; 17043:2023 6.1.2 |
| **Dependencias** | P-PSEA-03 |
| **Dependientes** | Ninguna |
| **Prioridad** | Media |
| **Esfuerzo** | 6 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Instructivo técnico para realizar la caracterización de items PT (cilindros de gas), incluyendo especificaciones técnicas y criterios de aceptación.

**Relaciones:**
- **Padre:** P-PSEA-03 (gestión de competencia)
- **Input:** Requisitos de 17025 cap. 6.1.2 y 17043 cap. 6.1.2

---

### I-PSEA-02: Instructivo de Producción PT Items

| Campo | Valor |
|-------|-------|
| **Código** | I-PSEA-02 |
| **Título** | Instructivo de Producción PT Items |
| **Tipo** | I |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | PT Coordinator |
| **Normas** | 17025:2017, 17043:2023 |
| **Cláusulas** | 17025:2017 6.1.3; 17043:2023 6.1.3, 7.3.1.1-7.3.1.2 |
| **Dependencias** | P-PSEA-05 |
| **Dependientes** | P-PSEA-10 |
| **Prioridad** | Alta |
| **Esfuerzo** | 10 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Instructivo técnico para producir items PT (cilindros de gas) con concentraciones certificadas, incluyendo procedimientos de selección y manejo.

**Relaciones:**
- **Padre:** P-PSEA-05 (proveedores externos)
- **Hijo:** P-PSEA-10 (manejo de items PT)
- **Input:** Requisitos de 17025 cap. 6.1.3 y 17043 cap. 6.1.3, 7.3.1

---

### I-PSEA-03: Instructivo de Control Ambiental

| Campo | Valor |
|-------|-------|
| **Código** | I-PSEA-03 |
| **Título** | Instructivo de Control Ambiental |
| **Tipo** | I |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | QMS Coordinator |
| **Normas** | 17025:2017, 17043:2023 |
| **Cláusulas** | 17025:2017 6.3.2; 17043:2023 6.3.2 |
| **Dependencias** | P-PSEA-04 |
| **Dependientes** | F-PSEA-02 |
| **Prioridad** | Media |
| **Esfuerzo** | 6 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Instructivo técnico para controlar las condiciones ambientales en las instalaciones donde se realizan actividades del esquema de EA.

**Relaciones:**
- **Padre:** P-PSEA-04 (control de acceso)
- **Hijo:** F-PSEA-02 (formato de registro ambiental)
- **Input:** Requisitos de 17025 cap. 6.3.2 y 17043 cap. 6.3.2

---

### I-PSEA-04: Instructivo de Validación de Métodos

| Campo | Valor |
|-------|-------|
| **Código** | I-PSEA-04 |
| **Título** | Instructivo de Validación de Métodos |
| **Tipo** | I |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | PT Coordinator |
| **Normas** | 17025:2017 |
| **Cláusulas** | 17025:2017 7.3 |
| **Dependencias** | P-PSEA-07 |
| **Dependientes** | Ninguna |
| **Prioridad** | Media |
| **Esfuerzo** | 8 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Instructivo técnico para validar métodos de ensayo utilizados en el esquema de EA.

**Relaciones:**
- **Padre:** P-PSEA-07 (selección de métodos)
- **Input:** Requisitos de 17025 cap. 7.3

---

### I-PSEA-05: Instructivo de Estimación de Incertidumbre

| Campo | Valor |
|-------|-------|
| **Código** | I-PSEA-05 |
| **Título** | Instructivo de Estimación de Incertidumbre |
| **Tipo** | I |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | PT Coordinator |
| **Normas** | 17025:2017 |
| **Cláusulas** | 17025:2017 7.4 |
| **Dependencias** | DG-PSEA-01 |
| **Dependientes** | I-PSEA-08 |
| **Prioridad** | Alta |
| **Esfuerzo** | 10 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Instructivo técnico para estimar la incertidumbre de mediciones en el esquema de EA.

**Relaciones:**
- **Padre:** DG-PSEA-01
- **Hijo:** I-PSEA-08 (valor asignado)
- **Input:** Requisitos de 17025 cap. 7.4

---

### I-PSEA-06: Instructivo de Control de Calidad de Datos

| Campo | Valor |
|-------|-------|
| **Código** | I-PSEA-06 |
| **Título** | Instructivo de Control de Calidad de Datos |
| **Tipo** | I |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | PT Coordinator |
| **Normas** | 17025:2017 |
| **Cláusulas** | 17025:2017 7.8 |
| **Dependencias** | DG-PSEA-01 |
| **Dependientes** | I-PSEA-11 |
| **Prioridad** | Alta |
| **Esfuerzo** | 8 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Instructivo técnico para controlar la calidad de los datos generados en el esquema de EA.

**Relaciones:**
- **Padre:** DG-PSEA-01
- **Hijo:** I-PSEA-11 (análisis de datos)
- **Input:** Requisitos de 17025 cap. 7.8

---

### I-PSEA-07: Instructivo de Diseño Estadístico

| Campo | Valor |
|-------|-------|
| **Código** | I-PSEA-07 |
| **Título** | Instructivo de Diseño Estadístico |
| **Tipo** | I |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | PT Coordinator |
| **Normas** | 13528:2022, 17043:2023 |
| **Cláusulas** | 13528:2022 cap. 4-5; 17043:2023 7.2.2.1-7.2.2.3 |
| **Dependencias** | P-PSEA-09, I-PSEA-05, I-PSEA-06 |
| **Dependientes** | I-PSEA-08 al I-PSEA-12 |
| **Prioridad** | Alta |
| **Esfuerzo** | 16 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Instructivo técnico para diseñar el esquema estadístico del EA conforme a ISO 13528:2022, incluyendo consideraciones sobre distribución de datos, simetría, asimetría, y número de participantes.

**Relaciones:**
- **Padre:** P-PSEA-09 (planificación ronda EA), I-PSEA-05 (incertidumbre), I-PSEA-06 (control de calidad)
- **Hijos:** I-PSEA-08 (valor asignado), I-PSEA-09 (instrucciones participantes), I-PSEA-10 (homogeneidad), I-PSEA-11 (análisis datos), I-PSEA-12 (evaluación desempeño)
- **Input:** Requisitos de 13528 cap. 4-5 y 17043 cap. 7.2.2

---

### I-PSEA-08: Instructivo de Valor Asignado

| Campo | Valor |
|-------|-------|
| **Código** | I-PSEA-08 |
| **Título** | Instructivo de Valor Asignado |
| **Tipo** | I |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | PT Coordinator |
| **Normas** | 13528:2022, 17043:2023 |
| **Cláusulas** | 13528:2022 cap. 7; 17043:2023 7.2.3.1-7.2.3.4 |
| **Dependencias** | P-PSEA-08, P-PSEA-09, I-PSEA-07 |
| **Dependientes** | P-PSEA-21, P-PSEA-22, I-PSEA-12 |
| **Prioridad** | Alta |
| **Esfuerzo** | 14 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Instructivo técnico para asignar valores a los items PT del esquema de EA, incluyendo métodos independientes (MRC) y consenso estadístico, conforme a ISO 13528:2022.

**Relaciones:**
- **Padre:** P-PSEA-08 (trazabilidad), P-PSEA-09 (planificación ronda EA), I-PSEA-07 (diseño estadístico)
- **Hermanos:** I-PSEA-05 (incertidumbre)
- **Hijos:** P-PSEA-21 (divulgación valores), P-PSEA-22 (reportes PT), I-PSEA-12 (evaluación desempeño)
- **Input:** Requisitos de 13528 cap. 7 y 17043 cap. 7.2.3

---

### I-PSEA-09: Instructivo de Instrucciones a Participantes

| Campo | Valor |
|-------|-------|
| **Código** | I-PSEA-09 |
| **Título** | Instructivo de Instrucciones a Participantes |
| **Tipo** | I |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | PT Coordinator |
| **Normas** | 17043:2023, 13528:2022 |
| **Cláusulas** | 17043:2023 7.3.1.3, 7.3.4.3, 7.3.5.2; 13528:2022 5.5.1.1-5.5.4.4 |
| **Dependencias** | P-PSEA-20, I-PSEA-07 |
| **Dependientes** | Ninguna |
| **Prioridad** | Alta |
| **Esfuerzo** | 8 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Instructivo técnico para generar instrucciones detalladas a los participantes del esquema de EA, incluyendo formato de reporte de resultados, mediciones replicadas, datos censurados y cifras significativas.

**Relaciones:**
- **Padre:** P-PSEA-20 (comunicación PT), I-PSEA-07 (diseño estadístico)
- **Input:** Requisitos de 17043 cap. 7.3.1-7.3.5 y 13528 cap. 5.5

---

### I-PSEA-10: Instructivo de Homogeneidad y Estabilidad

| Campo | Valor |
|-------|-------|
| **Código** | I-PSEA-10 |
| **Título** | Instructivo de Homogeneidad y Estabilidad |
| **Tipo** | I |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | PT Coordinator |
| **Normas** | 13528:2022, 17043:2023 |
| **Cláusulas** | 13528:2022 cap. 6; 17043:2023 7.3.2.1-7.3.2.6 |
| **Dependencias** | P-PSEA-09, I-PSEA-07, I-PSEA-02 |
| **Dependientes** | Ninguna |
| **Prioridad** | Alta |
| **Esfuerzo** | 12 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Instructivo técnico para realizar pruebas de homogeneidad y estabilidad de items PT, incluyendo criterios, procedimientos, cronograma y métodos de evaluación, conforme a ISO 13528:2022.

**Relaciones:**
- **Padre:** P-PSEA-09 (planificación ronda EA), I-PSEA-07 (diseño estadístico)
- **Hermanos:** I-PSEA-02 (producción PT items)
- **Input:** Requisitos de 13528 cap. 6 y 17043 cap. 7.3.2

---

### I-PSEA-11: Instructivo de Análisis de Datos

| Campo | Valor |
|-------|-------|
| **Código** | I-PSEA-11 |
| **Título** | Instructivo de Análisis de Datos |
| **Tipo** | I |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | PT Coordinator |
| **Normas** | 13528:2022, 17043:2023 |
| **Cláusulas** | 13528:2022 cap. 6; 17043:2023 7.4.1.1-7.4.1.6 |
| **Dependencias** | I-PSEA-06, I-PSEA-07, I-PSEA-10 |
| **Dependientes** | I-PSEA-12, P-PSEA-22 |
| **Prioridad** | Alta |
| **Esfuerzo** | 14 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Instructivo técnico para analizar datos de participantes del esquema de EA, incluyendo registro y análisis, estadísticas de desempeño, métodos robustos, y tratamiento de valores atípicos, conforme a ISO 13528:2022.

**Relaciones:**
- **Padre:** I-PSEA-06 (control de calidad), I-PSEA-07 (diseño estadístico)
- **Hermanos:** I-PSEA-10 (homogeneidad y estabilidad)
- **Hijos:** I-PSEA-12 (evaluación desempeño), P-PSEA-22 (reportes PT)
- **Input:** Requisitos de 13528 cap. 6 y 17043 cap. 7.4.1

---

### I-PSEA-12: Instructivo de Evaluación de Desempeño

| Campo | Valor |
|-------|-------|
| **Código** | I-PSEA-12 |
| **Título** | Instructivo de Evaluación de Desempeño |
| **Tipo** | I |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | PT Coordinator |
| **Normas** | 13528:2022, 17043:2023 |
| **Cláusulas** | 13528:2022 cap. 8-11; 17043:2023 7.4.2.1-7.4.2.2 |
| **Dependencias** | I-PSEA-07, I-PSEA-08, I-PSEA-11 |
| **Dependientes** | P-PSEA-22, I-PSEA-14 |
| **Prioridad** | Alta |
| **Esfuerzo** | 16 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Instructivo técnico para evaluar el desempeño de participantes del esquema de EA, incluyendo z-score, zeta score, proporción de límite permitido, y análisis cualitativo, conforme a ISO 13528:2022.

**Relaciones:**
- **Padre:** I-PSEA-07 (diseño estadístico), I-PSEA-08 (valor asignado), I-PSEA-11 (análisis de datos)
- **Hijos:** P-PSEA-22 (reportes PT), I-PSEA-14 (visualización de datos)
- **Input:** Requisitos de 13528 cap. 8-11 y 17043 cap. 7.4.2

---

### I-PSEA-13: Instructivo de Validación de Sistemas

| Campo | Valor |
|-------|-------|
| **Código** | I-PSEA-13 |
| **Título** | Instructivo de Validación de Sistemas |
| **Tipo** | I |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | PT Coordinator |
| **Normas** | 17043:2023, 13528:2022 |
| **Cláusulas** | 17043:2023 7.5.2.1-7.5.2.4; 13528:2022 4.1.4 |
| **Dependencias** | DG-PSEA-01 |
| **Dependientes** | P-PSEA-23 |
| **Prioridad** | Media |
| **Esfuerzo** | 8 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Instructivo técnico para validar sistemas informáticos utilizados en el esquema de EA, incluido CALAIRE-APP.

**Relaciones:**
- **Padre:** DG-PSEA-01
- **Hijo:** P-PSEA-23 (gestión de datos)
- **Input:** Requisitos de 17043 cap. 7.5.2 y 13528 cap. 4.1.4

---

### I-PSEA-14: Instructivo de Visualización de Datos

| Campo | Valor |
|-------|-------|
| **Código** | I-PSEA-14 |
| **Título** | Instructivo de Visualización de Datos |
| **Tipo** | I |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | PT Coordinator |
| **Normas** | 13528:2022 |
| **Cláusulas** | 13528:2022 cap. 10 |
| **Dependencias** | I-PSEA-12 |
| **Dependientes** | Ninguna |
| **Prioridad** | Baja |
| **Esfuerzo** | 8 horas |
| **Estado Cumplimiento** | no_cumple |

**Descripción:** Instructivo técnico para generar visualizaciones gráficas de datos del esquema de EA, incluyendo histogramas, kernel density plots, box plots, y Youden plots, conforme a ISO 13528:2022.

**Relaciones:**
- **Padre:** I-PSEA-12 (evaluación de desempeño)
- **Input:** Requisitos de 13528 cap. 10

---

## Formatos (F)

### F-PSEA-01: Calendario Tipo

| Campo | Valor |
|-------|-------|
| **Código** | F-PSEA-01 |
| **Título** | Calendario Tipo |
| **Tipo** | F |
| **Versión** | v0 |
| **Estado** | TBD |
| **Responsable** | PT Coordinator |
| **Normas** | 17043:2023 |
| **Cláusulas** | 17043:2023 7.2.1 |
| **Dependencias** | P-PSEA-09 |
| **Dependientes** | F-PSEA-02 |
| **Prioridad** | Alta |
| **Esfuerzo** | 4 horas |
| **Estado Cumplimiento** | TBD |

**Descripción:** Formato (Excel) para establecer el calendario tipo de rondas del esquema de EA, incluyendo semanas de ronda, fechas límite, y criterios de asignación.

**Relaciones:**
- **Padre:** P-PSEA-09 (planificación ronda EA)
- **Hijo:** F-PSEA-02 (cronograma detallado)
- **Input:** Requisitos de 17043 cap. 7.2.1

---

### F-PSEA-02: Cronograma Detallado

| Campo | Valor |
|-------|-------|
| **Código** | F-PSEA-02 |
| **Título** | Cronograma Detallado |
| **Tipo** | F |
| **Versión** | v0 |
| **Estado** | TBD |
| **Responsable** | PT Coordinator |
| **Normas** | 17043:2023 |
| **Cláusulas** | 17043:2023 7.2.1 |
| **Dependencias** | P-PSEA-09, F-PSEA-01 |
| **Dependientes** | F-PSEA-03 |
| **Prioridad** | Alta |
| **Esfuerzo** | 4 horas |
| **Estado Cumplimiento** | TBD |

**Descripción:** Formato (Excel) para desglose detallado de actividades de la ronda, incluyendo actividades por fase, responsables por actividad, duración de cada actividad, y hitos críticos.

**Relaciones:**
- **Padre:** P-PSEA-09 (planificación ronda EA), F-PSEA-01 (calendario tipo)
- **Hijo:** F-PSEA-03 (registro planificación)
- **Input:** Requisitos de 17043 cap. 7.2.1

---

### F-PSEA-03: Registro Planificacion Ronda EA

| Campo | Valor |
|-------|-------|
| **Código** | F-PSEA-03 |
| **Título** | Registro Planificacion Ronda EA |
| **Tipo** | F |
| **Versión** | TBD |
| **Estado** | TBD |
| **Responsable** | PT Coordinator |
| **Normas** | 17043:2023 |
| **Cláusulas** | 17043:2023 7.2.1 |
| **Dependencias** | P-PSEA-09 |
| **Dependientes** | Ninguna |
| **Prioridad** | Alta |
| **Esfuerzo** | 4 horas |
| **Estado Cumplimiento** | TBD |

**Descripción:** Formato (Excel) para registrar los datos de la ronda y las decisiones de planificación, incluyendo versiones de planificación y documentación de cambios.

**Relaciones:**
- **Padre:** P-PSEA-09 (planificación ronda EA)
- **Input:** Requisitos de 17043 cap. 7.2.1

---

### F-PSEA-04: Formato Informe Resultados

| Campo | Valor |
|-------|-------|
| **Código** | F-PSEA-04 |
| **Título** | Formato Informe Resultados |
| **Tipo** | F |
| **Versión** | v0 |
| **Estado** | TBD |
| **Responsable** | PT Coordinator |
| **Normas** | 17043:2023 |
| **Cláusulas** | 17043:2023 7.4.3 |
| **Dependencias** | P-PSEA-07 |
| **Dependientes** | Ninguna |
| **Prioridad** | Alta |
| **Esfuerzo** | 6 horas |
| **Estado Cumplimiento** | TBD |

**Descripción:** Formato (plantilla Word/Rmd) para generar informes de resultados del EA, incluyendo secciones para resumen ejecutivo, resultados de desempeño, valor asignado, y evaluación estadística.

**Relaciones:**
- **Padre:** P-PSEA-07 (informe resultados)
- **Input:** Requisitos de 17043 cap. 7.4.3

---

## Resumen de Relaciones por Tipo de Documento

### Documentos Generales (DG)
- **DG-PSEA-01** es el documento raíz del SGC
- Todos los procedimientos (P-PSEA-01 al P-PSEA-09) dependen de DG-PSEA-01

### Procedimientos (P)
- **Procedimiento general:** P-PSEA-01 (Protocolo General EA)
- **Procedimientos específicos por gas:** P-PSEA-02 (NO-NO2), P-PSEA-03 (CO), P-PSEA-04 (O3), P-PSEA-05 (SO2)
- **Procedimientos operativos:** P-PSEA-06 (Diseño Estadístico), P-PSEA-07 (Informe Resultados), P-PSEA-08 (Colusión Falsificación), P-PSEA-09 (Planificación Ronda EA)

### Formatos (F)
- **Formatos de planificación:** F-PSEA-01 (Calendario Tipo), F-PSEA-02 (Cronograma Detallado), F-PSEA-03 (Registro Planificación Ronda EA)
- **Formatos de resultados:** F-PSEA-04 (Formato Informe Resultados)

---

## Referencias

- `docs/docs_sgc/Matriz Maestra de Cumplimiento Normativo.md` - Matriz de mapeo normativo
- `docs/docs_sgc/Inventario Documental del SGC.md` - Inventario de documentos existentes
- `docs/docs_sgc/Árbol Maestro PSEA.md` - Estructura jerárquica del SGC
- `logs/plans/260208_1932_plan_ajuste-sgc-17025-17043-13528.md` - Plan de trabajo

---

**Fin del Diccionario de Documentos SGC**
