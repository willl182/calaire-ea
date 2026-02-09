# Backlog Priorizado de Documentos SGC - CALAIRE-EA

**Creado**: 2026-02-08
**Versión**: 1.0
**Estado**: draft
**Responsable**: Documentation Manager

---

## Objetivo

Este backlog prioriza los documentos del Sistema de Gestión de Calidad (SGC) según la criticidad de los requisitos normativos de ISO/IEC 17025:2017, ISO/IEC 17043:2023 e ISO 13528:2022, proporcionando estimaciones de esfuerzo y criterios de aceptación para cada documento.

---

## Convenciones

| Columna | Descripción | Valores posibles |
|---------|-------------|------------------|
| **Prioridad** | Nivel de prioridad | P1 (Alta crítica), P2 (Alta), P3 (Media), P4 (Baja) |
| **Esfuerzo** | Estimación de tiempo en horas | Creación + Revisión técnica |
| **Complejidad** | Nivel de complejidad | Alta, Media, Baja |
| **Dependencias** | Documentos predecesores | Códigos de documentos |
| **Normas** | Normas asociadas | 17025:2017, 17043:2023, 13528:2022 |
| **Criterio Aceptación** | Criterios para considerar el documento aprobado | Lista verificable |

---

## Backlog de Documentos - Oleada 1 (P1 - Crítica)

### P1-1: DG-PSEA-01 Manual de Calidad

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P1 |
| **Tipo** | DG |
| **Código** | DG-PSEA-01 |
| **Título** | Manual de Calidad - CALAIRE-EA |
| **Estado Actual** | v1.0 draft |
| **Acción** | Completar desarrollo |
| **Esfuerzo** | 8 horas |
| **Complejidad** | Alta |
| **Dependencias** | Ninguna |
| **Normas** | 17025:2017 cap. 4-8, 17043:2023 cap. 4-8 |
| **Responsable** | QMS Coordinator |

**Brechas que cubre:**
- ISO 17025:2017 4.1, 4.3, 5.5, 5.6, 5.7, 6.2.1, 8.1, 8.2
- ISO 17043:2023 4.1.1-4.1.3, 4.1.6, 5.5, 6.2.1, 8.1, 8.2

**Criterios de Aceptación:**
- [ ] Incluye política de imparcialidad y estructura organizacional (4.1)
- [ ] Define claramente la estructura de autoridad y responsabilidad (5.5-5.7)
- [ ] Establece el enfoque de gestión documental (8.1-8.2)
- [ ] Describe los procesos de mejora continua (8.6)
- [ ] Incluye referencias cruzadas a todos los procedimientos P-PSEA
- [ ] Aprobado por Dirección y revisado por consultor ISO 17043

---

### P1-2: P-PSEA-01 Protocolo General EA (Actualización)

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P1 |
| **Tipo** | P |
| **Código** | P-PSEA-01 |
| **Título** | Protocolo General de Ensayos de Aptitud |
| **Estado Actual** | v1.0 in_review |
| **Acción** | Actualizar con ISO 17043:2023 |
| **Esfuerzo** | 6 horas |
| **Complejidad** | Media |
| **Dependencias** | DG-PSEA-01 |
| **Normas** | 17025:2017 5.3-5.4, 17043:2023 5.3-5.4, 7.2-7.4 |
| **Responsable** | PT Provider Lead |

**Brechas que cubre:**
- ISO 17025:2017 5.3, 5.4
- ISO 17043:2023 5.3, 5.4, 7.1, 7.2, 7.4

**Criterios de Aceptación:**
- [ ] Actualiza definiciones de esquemas PT con ISO 17043:2023 (5.3-5.4)
- [ ] Incluye requisitos de comunicación PT (7.1)
- [ ] Describe flujo completo de planificación de rondas (7.2)
- [ ] Establece requisitos de reportes de resultados (7.4)
- [ ] Referencia procedimientos P-PSEA-02 al P-PSEA-05 por gas
- [ ] Aprobado por PT Provider Lead

---

### P1-3: P-PSEA-06 Procedimiento Diseño Estadístico (v0)

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P1 |
| **Tipo** | P |
| **Código** | P-PSEA-06 |
| **Título** | Procedimiento de Diseño Estadístico de Ensayos de Aptitud |
| **Estado Actual** | v0 (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 8 horas |
| **Complejidad** | Alta |
| **Dependencias** | P-PSEA-01 |
| **Normas** | 13528:2022 cap. 5, 17043:2023 7.2.2 |
| **Responsable** | Estadístico Principal |

**Brechas que cubre:**
- ISO 13528:2022 cap. 5 (Statistical Design)
- ISO 17043:2023 7.2.2 (Statistical design)

**Criterios de Aceptación:**
- [ ] Define tipos de datos y distribuciones (5.2.2, 5.3)
- [ ] Establece criterios para número mínimo de participantes (5.4)
- [ ] Describe procedimientos para datos censurados (5.5.3)
- [ ] Define manejo de dígitos significativos y redondeo (5.5.4)
- [ ] Incluye métodos robustos para outliers (6.5)
- [ ] Referencia ISO 13528 anexos A, B, C
- [ ] Aprobado por consultor ISO 17043 y validado por estadístico

---

### P1-4: P-PSEA-07 Procedimiento Informe Resultados (v0)

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P1 |
| **Tipo** | P |
| **Código** | P-PSEA-07 |
| **Título** | Procedimiento de Elaboración de Informes de Resultados EA |
| **Estado Actual** | v0 (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 6 horas |
| **Complejidad** | Media |
| **Dependencias** | P-PSEA-06 |
| **Normas** | 17043:2023 7.4.3, 13528:2022 cap. 9 |
| **Responsable** | PT Coordinator |

**Brechas que cubre:**
- ISO 17043:2023 7.4.3 (Reporting)
- ISO 13528:2022 cap. 9 (Score Calculation)

**Criterios de Aceptación:**
- [ ] Define contenido mínimo del informe de resultados (7.4.3.2)
- [ ] Establece plazos de entrega de informes (7.4.3.3)
- [ ] Describe procedimiento de informes corregidos (7.4.3.5-7.4.3.6)
- [ ] Incluye procedimiento para declaraciones de participación (7.4.3.7)
- [ ] Define política de uso de informes (7.4.3.4)
- [ ] Alineado con plantilla de informe de CALAIRE-APP
- [ ] Aprobado por PT Coordinator

---

### P1-5: P-PSEA-08 Procedimiento de Colusión y Falsificación (v0)

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P1 |
| **Tipo** | P |
| **Código** | P-PSEA-08 |
| **Título** | Procedimiento de Detección y Gestión de Colusión y Falsificación |
| **Estado Actual** | v0 (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 4 horas |
| **Complejidad** | Media |
| **Dependencias** | P-PSEA-01 |
| **Normas** | 17043:2023 4.1, 7.1 |
| **Responsable** | QMS Coordinator |

**Brechas que cubre:**
- ISO 17043:2023 4.1 (Impartiality)
- ISO 17043:2023 7.1 (Review of requests, contracts)

**Criterios de Aceptación:**
- [ ] Define indicadores de posible colusión entre participantes
- [ ] Establece procedimientos de investigación de sospechas
- [ ] Define medidas disciplinarias aplicables
- [ ] Incluye requisitos de confidencialidad en investigaciones
- [ ] Describe procedimiento de exclusión de participantes
- [ ] Aprobado por QMS Coordinator y revisión legal

---

### P1-6: P-PSEA-09 Procedimiento de Planificación Ronda EA (Expansión)

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P1 |
| **Tipo** | P |
| **Código** | P-PSEA-09 |
| **Título** | Procedimiento de Planificación de Rondas de Ensayo de Aptitud |
| **Estado Actual** | v1.0 draft (tabla, requiere expansión) |
| **Acción** | Expandir con requisitos detallados |
| **Esfuerzo** | 6 horas |
| **Complejidad** | Media |
| **Dependencias** | P-PSEA-01, P-PSEA-06 |
| **Normas** | 17043:2023 7.2.1 |
| **Responsable** | PT Coordinator |

**Brechas que cubre:**
- ISO 17043:2023 7.2.1 (Design and planning)

**Criterios de Aceptación:**
- [ ] Incluye todos los literales a) a u) de 7.2.1.3
- [ ] Define cronograma de hitos de la ronda
- [ ] Establece procedimientos para cambios significativos (7.2.1.2)
- [ ] Describe plan documentado de la ronda (7.2.1.3)
- [ ] Incluye matrices de responsabilidad por fase
- [ ] Alineado con formatos F-PSEA-01 al F-PSEA-04
- [ ] Aprobado por PT Coordinator

---

### P1-7: P-PSEA-16 Procedimiento de No Conformidades

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P1 |
| **Tipo** | P |
| **Código** | P-PSEA-16 |
| **Título** | Procedimiento de Gestión de No Conformidades |
| **Estado Actual** | TBD (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 4 horas |
| **Complejidad** | Media |
| **Dependencias** | DG-PSEA-01 |
| **Normas** | 17025:2017 8.7, 17043:2023 8.7 |
| **Responsable** | QMS Coordinator |

**Brechas que cubre:**
- ISO 17025:2017 8.7 (Nonconformities)
- ISO 17043:2023 8.7 (Nonconformities)

**Criterios de Aceptación:**
- [ ] Define proceso de identificación de no conformidades
- [ ] Establece sistema de evaluación de gravedad
- [ ] Describe acciones correctivas inmediatas
- [ ] Define plazos de resolución según gravedad
- [ ] Incluye requisitos de seguimiento y verificación
- [ ] Integra con procedimiento de mejora continua (P-PSEA-15)
- [ ] Aprobado por QMS Coordinator

---

### P1-8: P-PSEA-17 Procedimiento de Auditorías Internas

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P1 |
| **Tipo** | P |
| **Código** | P-PSEA-17 |
| **Título** | Procedimiento de Auditorías Internas del SGC |
| **Estado Actual** | TBD (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 4 horas |
| **Complejidad** | Media |
| **Dependencias** | DG-PSEA-01 |
| **Normas** | 17025:2017 8.8, 17043:2023 8.8 |
| **Responsable** | Auditor Interno |

**Brechas que cubre:**
- ISO 17025:2017 8.8 (Internal audits)
- ISO 17043:2023 8.8 (Internal audits)

**Criterios de Aceptación:**
- [ ] Define programa anual de auditorías
- [ ] Establece criterios de competencia de auditores
- [ ] Describe proceso de planificación de auditorías
- [ ] Incluye lista de verificación por tipo de documento
- [ ] Define proceso de reporte de hallazgos
- [ ] Establece seguimiento de acciones correctivas
- [ ] Aprobado por Auditor Interno

---

### P1-9: P-PSEA-18 Procedimiento de Revisión por Dirección

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P1 |
| **Tipo** | P |
| **Código** | P-PSEA-18 |
| **Título** | Procedimiento de Revisión por la Dirección |
| **Estado Actual** | TBD (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 4 horas |
| **Complejidad** | Media |
| **Dependencias** | P-PSEA-15, P-PSEA-16, P-PSEA-17 |
| **Normas** | 17025:2017 8.9, 17043:2023 8.9 |
| **Responsable** | QMS Coordinator |

**Brechas que cubre:**
- ISO 17025:2017 8.9 (Management review)
- ISO 17043:2023 8.9 (Management review)

**Criterios de Aceptación:**
- [ ] Define periodicidad de revisiones (mínimo anual)
- [ ] Establece agenda de revisión según ISO 17025:2017 8.9
- [ ] Incluye entradas: cambios normativos, resultados de auditorías, NC, quejas
- [ ] Define salidas: acciones, recursos, mejora continua
- [ ] Establece sistema de seguimiento de decisiones
- [ ] Aprobado por Dirección

---

### P1-10: P-PSEA-22 Procedimiento de Reportes PT

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P1 |
| **Tipo** | P |
| **Código** | P-PSEA-22 |
| **Título** | Procedimiento de Emisión de Reportes de Ensayos de Aptitud |
| **Estado Actual** | TBD (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 6 horas |
| **Complejidad** | Media |
| **Dependencias** | P-PSEA-07 |
| **Normas** | 17043:2023 7.4.3 |
| **Responsable** | PT Coordinator |

**Brechas que cubre:**
- ISO 17043:2023 7.4.3 (Reporting)

**Criterios de Aceptación:**
- [ ] Define requisitos de contenido de reportes (7.4.3.1-7.4.3.2)
- [ ] Establece plazos de emisión según tipo de ronda (7.4.3.3)
- [ ] Describe procedimiento de reportes corregidos (7.4.3.5-7.4.3.6)
- [ ] Incluye emisión de declaraciones de participación (7.4.3.7)
- [ ] Define política de distribución y uso de reportes (7.4.3.4)
- [ ] Integra con CALAIRE-APP para generación automatizada
- [ ] Aprobado por PT Coordinator

---

## Backlog de Documentos - Oleada 2 (P2 - Alta)

### P2-1: P-PSEA-02 Procedimiento de Ensayo de Aptitud para NO-NO2

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P2 |
| **Tipo** | P |
| **Código** | P-PSEA-02 |
| **Título** | Procedimiento de Ensayo de Aptitud para Contaminante NO-NO2 |
| **Estado Actual** | TBD (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 6 horas |
| **Complejidad** | Media |
| **Dependencias** | P-PSEA-01, P-PSEA-06 |
| **Normas** | 17043:2023 cap. 7 |
| **Responsable** | Especialista NO-NO2 |

**Criterios de Aceptación:**
- [ ] Define rangos operacionales específicos para NO-NO2
- [ ] Establece métodos de producción de gases patrón
- [ ] Describe procedimientos de homogeneidad y estabilidad para NO-NO2
- [ ] Incluye criterios específicos de evaluación de desempeño
- [ ] Referencia procedimientos genéricos P-PSEA-06, P-PSEA-07
- [ ] Aprobado por Especialista NO-NO2 y PT Provider Lead

---

### P2-2: P-PSEA-03 Procedimiento de Ensayo de Aptitud para CO

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P2 |
| **Tipo** | P |
| **Código** | P-PSEA-03 |
| **Título** | Procedimiento de Ensayo de Aptitud para Contaminante CO |
| **Estado Actual** | TBD (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 6 horas |
| **Complejidad** | Media |
| **Dependencias** | P-PSEA-01, P-PSEA-06 |
| **Normas** | 17043:2023 cap. 7 |
| **Responsable** | Especialista CO |

**Criterios de Aceptación:**
- [ ] Define rangos operacionales específicos para CO
- [ ] Establece métodos de producción de gases patrón
- [ ] Describe procedimientos de homogeneidad y estabilidad para CO
- [ ] Incluye criterios específicos de evaluación de desempeño
- [ ] Referencia procedimientos genéricos P-PSEA-06, P-PSEA-07
- [ ] Aprobado por Especialista CO y PT Provider Lead

---

### P2-3: P-PSEA-04 Procedimiento de Ensayo de Aptitud para O3

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P2 |
| **Tipo** | P |
| **Código** | P-PSEA-04 |
| **Título** | Procedimiento de Ensayo de Aptitud para Contaminante O3 |
| **Estado Actual** | TBD (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 6 horas |
| **Complejidad** | Media |
| **Dependencias** | P-PSEA-01, P-PSEA-06 |
| **Normas** | 17043:2023 cap. 7 |
| **Responsable** | Especialista O3 |

**Criterios de Aceptación:**
- [ ] Define rangos operacionales específicos para O3
- [ ] Establece métodos de producción de gases patrón
- [ ] Describe procedimientos de homogeneidad y estabilidad para O3
- [ ] Incluye criterios específicos de evaluación de desempeño
- [ ] Referencia procedimientos genéricos P-PSEA-06, P-PSEA-07
- [ ] Aprobado por Especialista O3 y PT Provider Lead

---

### P2-4: P-PSEA-05 Procedimiento de Ensayo de Aptitud para SO2

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P2 |
| **Tipo** | P |
| **Código** | P-PSEA-05 |
| **Título** | Procedimiento de Ensayo de Aptitud para Contaminante SO2 |
| **Estado Actual** | TBD (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 6 horas |
| **Complejidad** | Media |
| **Dependencias** | P-PSEA-01, P-PSEA-06 |
| **Normas** | 17043:2023 cap. 7 |
| **Responsable** | Especialista SO2 |

**Criterios de Aceptación:**
- [ ] Define rangos operacionales específicos para SO2
- [ ] Establece métodos de producción de gases patrón
- [ ] Describe procedimientos de homogeneidad y estabilidad para SO2
- [ ] Incluye criterios específicos de evaluación de desempeño
- [ ] Referencia procedimientos genéricos P-PSEA-06, P-PSEA-07
- [ ] Aprobado por Especialista SO2 y PT Provider Lead

---

### P2-5: P-PSEA-15 Procedimiento de Mejora Continua

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P2 |
| **Tipo** | P |
| **Código** | P-PSEA-15 |
| **Título** | Procedimiento de Mejora Continua del SGC |
| **Estado Actual** | TBD (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 4 horas |
| **Complejidad** | Media |
| **Dependencias** | P-PSEA-16, P-PSEA-17 |
| **Normas** | 17025:2017 8.6, 17043:2023 8.6 |
| **Responsable** | QMS Coordinator |

**Criterios de Aceptación:**
- [ ] Define proceso de identificación de oportunidades de mejora
- [ ] Establece sistema de evaluación de impacto de cambios
- [ ] Integra hallazgos de auditorías, NC, quejas y apelaciones
- [ ] Define proceso de implementación de mejoras
- [ ] Incluye requisitos de seguimiento y medición de efectividad
- [ ] Aprobado por QMS Coordinator

---

### P2-6: P-PSEA-19 Procedimiento de Monitoreo de Imparcialidad

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P2 |
| **Tipo** | P |
| **Código** | P-PSEA-19 |
| **Título** | Procedimiento de Monitoreo de Imparcialidad |
| **Estado Actual** | TBD (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 4 horas |
| **Complejidad** | Media |
| **Dependencias** | DG-PSEA-01 |
| **Normas** | 17043:2023 4.1 |
| **Responsable** | QMS Coordinator |

**Criterios de Aceptación:**
- [ ] Define riesgos a la imparcialidad para proveedor PT
- [ ] Establece procedimientos de identificación de amenazas
- [ ] Describe mecanismos de monitoreo continuo
- [ ] Define acciones para eliminar o mitigar amenazas
- [ ] Incluye requisitos de confidencialidad en investigaciones
- [ ] Aprobado por QMS Coordinator

---

### P2-7: P-PSEA-20 Procedimiento de Comunicación PT

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P2 |
| **Tipo** | P |
| **Código** | P-PSEA-20 |
| **Título** | Procedimiento de Comunicación con Participantes PT |
| **Estado Actual** | TBD (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 4 horas |
| **Complejidad** | Baja |
| **Dependencias** | P-PSEA-01 |
| **Normas** | 17043:2023 7.1.2, 7.3.5 |
| **Responsable** | PT Coordinator |

**Criterios de Aceptación:**
- [ ] Define canales de comunicación con participantes
- [ ] Establece procedimientos de notificación de cambios (7.1.2.2)
- [ ] Describe proceso de aviso anticipado de rondas (7.3.5.1)
- [ ] Incluye requisitos de registro de comunicaciones (7.1.2.3)
- [ ] Define tiempos de respuesta a consultas
- [ ] Aprobado por PT Coordinator

---

### P2-8: P-PSEA-21 Procedimiento de Divulgación de Valores

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P2 |
| **Tipo** | P |
| **Código** | P-PSEA-21 |
| **Título** | Procedimiento de Divulgación de Valores Asignados |
| **Estado Actual** | TBD (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 4 horas |
| **Complejidad** | Media |
| **Dependencias** | P-PSEA-06 |
| **Normas** | 17043:2023 7.2.3.5 |
| **Responsable** | PT Coordinator |

**Criterios de Aceptación:**
- [ ] Define política de divulgación de valores asignados (7.2.3.5)
- [ ] Establece criterios de confidencialidad pre-informe
- [ ] Define plazos de divulgación post-informe
- [ ] Describe proceso de comunicación a participantes
- [ ] Incluye manejo de valores asignados parciales
- [ ] Aprobado por PT Coordinator

---

### P2-9: P-PSEA-23 Procedimiento de Gestión de Datos

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P2 |
| **Tipo** | P |
| **Código** | P-PSEA-23 |
| **Título** | Procedimiento de Gestión de Datos PT |
| **Estado Actual** | TBD (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 6 horas |
| **Complejidad** | Media |
| **Dependencias** | P-PSEA-13 |
| **Normas** | 17043:2023 7.5.2 |
| **Responsable** | Administrador de Datos |

**Criterios de Aceptación:**
- [ ] Define acceso y seguridad de datos (7.5.2.1)
- [ ] Establece procedimientos de validación de sistemas (7.5.2.2-7.5.2.3)
- [ ] Describe manejo de sistemas fuera de sitio (7.5.2.4)
- [ ] Incluye procedimientos de backup y recuperación
- [ ] Define roles y permisos de acceso
- [ ] Integra con CALAIRE-APP
- [ ] Aprobado por Administrador de Datos

---

### P2-10: P-PSEA-27 Procedimiento de Confidencialidad

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P2 |
| **Tipo** | P |
| **Código** | P-PSEA-27 |
| **Título** | Procedimiento de Gestión de Confidencialidad |
| **Estado Actual** | TBD (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 4 horas |
| **Complejidad** | Baja |
| **Dependencias** | DG-PSEA-01 |
| **Normas** | 17025:2017 4.2, 17043:2023 4.2 |
| **Responsable** | QMS Coordinator |

**Criterios de Aceptación:**
- [ ] Define política de confidencialidad (4.2.1)
- [ ] Establece procedimientos de liberación legal de información (4.2.2)
- [ ] Describe manejo de información de terceros (4.2.3)
- [ ] Incluye requisitos de confidencialidad del personal (4.2.4)
- [ ] Define protección de identidad de participantes (4.2.5)
- [ ] Aprobado por QMS Coordinator

---

## Backlog de Documentos - Oleada 3 (P3 - Media)

### P3-1: P-PSEA-28 Procedimiento de Gestión de Competencia

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P3 |
| **Tipo** | P |
| **Código** | P-PSEA-28 |
| **Título** | Procedimiento de Gestión de Competencia del Personal |
| **Estado Actual** | TBD (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 4 horas |
| **Complejidad** | Media |
| **Dependencias** | DG-PSEA-01 |
| **Normas** | 17025:2017 6.2, 17043:2023 6.2 |
| **Responsable** | QMS Coordinator |

**Criterios de Aceptación:**
- [ ] Define roles y responsabilidades del personal
- [ ] Establece criterios de competencia por rol
- [ ] Describe procedimientos de evaluación de competencia
- [ ] Incluye requisitos de capacitación continua
- [ ] Define proceso de autorización de personal
- [ ] Integra con formato F-PSEA-01 Registro de Competencia
- [ ] Aprobado por QMS Coordinator

---

### P3-2: P-PSEA-29 Procedimiento de Control de Acceso

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P3 |
| **Tipo** | P |
| **Código** | P-PSEA-29 |
| **Título** | Procedimiento de Control de Acceso a Instalaciones |
| **Estado Actual** | TBD (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 3 horas |
| **Complejidad** | Baja |
| **Dependencias** | DG-PSEA-01 |
| **Normas** | 17025:2017 6.3, 17043:2023 6.3 |
| **Responsable** | Coordinador de Instalaciones |

**Criterios de Aceptación:**
- [ ] Define áreas restringidas y niveles de acceso
- [ ] Establece procedimientos de control ambiental (6.3.2)
- [ ] Describe procedimientos de monitoreo ambiental (6.3.3)
- [ ] Incluye requisitos de separación de áreas (6.3.5)
- [ ] Integra con formato F-PSEA-02 Registro Ambiental
- [ ] Aprobado por Coordinador de Instalaciones

---

### P3-3: P-PSEA-30 Procedimiento de Proveedores Externos

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P3 |
| **Tipo** | P |
| **Código** | P-PSEA-30 |
| **Título** | Procedimiento de Gestión de Proveedores Externos |
| **Estado Actual** | TBD (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 4 horas |
| **Complejidad** | Media |
| **Dependencias** | DG-PSEA-01 |
| **Normas** | 17025:2017 6.4, 17043:2023 6.4 |
| **Responsable** | Compras |

**Criterios de Aceptación:**
- [ ] Define criterios de evaluación de proveedores
- [ ] Establece requisitos de competencia de proveedores
- [ ] Describe procedimientos de selección y calificación
- [ ] Incluye requisitos de comunicación con proveedores
- [ ] Define registros de proveedores aprobados
- [ ] Aprobado por Compras y QMS Coordinator

---

### P3-4: P-PSEA-10 Procedimiento de Manejo de Items PT

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P3 |
| **Tipo** | P |
| **Código** | P-PSEA-10 |
| **Título** | Procedimiento de Manejo de Items de Ensayo de Aptitud |
| **Estado Actual** | TBD (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 4 horas |
| **Complejidad** | Media |
| **Dependencias** | P-PSEA-01 |
| **Normas** | 17025:2017 7.7, 17043:2023 7.3.3-7.3.4 |
| **Responsable** | Coordinador de Logística PT |

**Criterios de Aceptación:**
- [ ] Define procedimientos de identificación y almacenamiento (7.3.3.1)
- [ ] Establece procedimientos de despacho y recepción (7.3.3.2)
- [ ] Describe procedimientos de embalaje y etiquetado (7.3.4.1)
- [ ] Incluye requisitos de condiciones de transporte (7.3.4.2)
- [ ] Define procedimientos de evaluación de condición (7.3.3.3)
- [ ] Integra con formatos F-PSEA-03 y F-PSEA-04
- [ ] Aprobado por Coordinador de Logística PT

---

### P3-5: P-PSEA-12 Procedimiento de Control Documental

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P3 |
| **Tipo** | P |
| **Código** | P-PSEA-12 |
| **Título** | Procedimiento de Control Documental |
| **Estado Actual** | TBD (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 4 horas |
| **Complejidad** | Baja |
| **Dependencias** | DG-PSEA-01 |
| **Normas** | 17025:2017 8.3, 17043:2023 8.3 |
| **Responsable** | QMS Coordinator |

**Criterios de Aceptación:**
- [ ] Define procedimientos de aprobación de documentos
- [ ] Establece sistema de control de versiones
- [ ] Describe procedimientos de distribución y acceso
- [ ] Incluye requisitos de revisiones periódicas
- [ ] Define proceso de obsolescencia y retiro
- [ ] Aprobado por QMS Coordinator

---

### P3-6: P-PSEA-13 Procedimiento de Control de Registros

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P3 |
| **Tipo** | P |
| **Código** | P-PSEA-13 |
| **Título** | Procedimiento de Control de Registros Técnicos y de Calidad |
| **Estado Actual** | TBD (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 4 horas |
| **Complejidad** | Baja |
| **Dependencias** | P-PSEA-12 |
| **Normas** | 17025:2017 8.4, 17043:2023 7.5.1, 8.4 |
| **Responsable** | QMS Coordinator |

**Criterios de Aceptación:**
- [ ] Define tipos de registros y tiempos de retención
- [ ] Establece requisitos de identificación de registros
- [ ] Describe procedimientos de almacenamiento y protección
- [ ] Incluye procedimientos de control de cambios (7.5.1.3)
- [ ] Define procedimientos de acceso y recuperación
- [ ] Aprobado por QMS Coordinator

---

### P3-7: P-PSEA-14 Procedimiento de Gestión de Riesgos

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P3 |
| **Tipo** | P |
| **Código** | P-PSEA-14 |
| **Título** | Procedimiento de Gestión de Riesgos y Oportunidades |
| **Estado Actual** | TBD (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 4 horas |
| **Complejidad** | Media |
| **Dependencias** | DG-PSEA-01 |
| **Normas** | 17025:2017 8.5, 17043:2023 8.5 |
| **Responsable** | QMS Coordinator |

**Criterios de Aceptación:**
- [ ] Define proceso de identificación de riesgos
- [ ] Establece metodología de evaluación de riesgos
- [ ] Describe procedimientos de tratamiento de riesgos
- [ ] Incluye seguimiento y revisión de riesgos
- [ ] Integra con procedimiento de mejora continua
- [ ] Aprobado por QMS Coordinator

---

### P3-8: P-PSEA-24 Procedimiento de Quejas

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P3 |
| **Tipo** | P |
| **Código** | P-PSEA-24 |
| **Título** | Procedimiento de Gestión de Quejas |
| **Estado Actual** | TBD (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 3 horas |
| **Complejidad** | Baja |
| **Dependencias** | DG-PSEA-01 |
| **Normas** | 17043:2023 8.10 |
| **Responsable** | QMS Coordinator |

**Criterios de Aceptación:**
- [ ] Define proceso de recepción de quejas
- [ ] Establece tiempos de respuesta
- [ ] Describe procedimientos de investigación
- [ ] Incluye sistema de seguimiento y cierre
- [ ] Integra con procedimiento de mejora continua
- [ ] Aprobado por QMS Coordinator

---

### P3-9: P-PSEA-25 Procedimiento de Apelaciones

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P3 |
| **Tipo** | P |
| **Código** | P-PSEA-25 |
| **Título** | Procedimiento de Gestión de Apelaciones |
| **Estado Actual** | TBD (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 3 horas |
| **Complejidad** | Baja |
| **Dependencias** | DG-PSEA-01 |
| **Normas** | 17043:2023 8.11 |
| **Responsable** | QMS Coordinator |

**Criterios de Aceptación:**
- [ ] Define proceso de recepción de apelaciones
- [ ] Establece procedimientos de evaluación
- [ ] Describe proceso de notificación de decisiones
- [ ] Incluye requisitos de confidencialidad
- [ ] Integra con procedimiento de mejora continua
- [ ] Aprobado por QMS Coordinator y revisión legal

---

### P3-10: F-PSEA-01 Calendario Tipo

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P3 |
| **Tipo** | F |
| **Código** | F-PSEA-01 |
| **Título** | Calendario Tipo de Ensayos de Aptitud |
| **Estado Actual** | v0 (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 2 horas |
| **Complejidad** | Baja |
| **Dependencias** | P-PSEA-09 |
| **Normas** | 17043:2023 7.2.1 |
| **Responsable** | PT Coordinator |

**Criterios de Aceptación:**
- [ ] Define estructura de calendario anual de rondas
- [ ] Incluye fechas clave por ronda (planificación, envío, informe)
- [ ] Establece formatos para gases NO-NO2, CO, O3, SO2
- [ ] Integra con P-PSEA-09 Procedimiento de Planificación
- [ ] Aprobado por PT Coordinator

---

## Backlog de Documentos - Oleada 4 (P4 - Baja)

### P4-1: F-PSEA-02 Cronograma Detallado

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P4 |
| **Tipo** | F |
| **Código** | F-PSEA-02 |
| **Título** | Cronograma Detallado de Ronda EA |
| **Estado Actual** | v0 (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 2 horas |
| **Complejidad** | Baja |
| **Dependencias** | P-PSEA-09 |
| **Normas** | 17043:2023 7.2.1 |
| **Responsable** | PT Coordinator |

**Criterios de Aceptación:**
- [ ] Define estructura de cronograma por fase de ronda
- [ ] Incluye hitos y responsables por actividad
- [ ] Establece formatos para tracking de avance
- [ ] Integra con P-PSEA-09 Procedimiento de Planificación
- [ ] Aprobado por PT Coordinator

---

### P4-2: F-PSEA-03 Registro Planificación Ronda EA

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P4 |
| **Tipo** | F |
| **Código** | F-PSEA-03 |
| **Título** | Registro de Planificación de Ronda de Ensayo de Aptitud |
| **Estado Actual** | TBD (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 2 horas |
| **Complejidad** | Baja |
| **Dependencias** | P-PSEA-09 |
| **Normas** | 17043:2023 7.2.1 |
| **Responsable** | PT Coordinator |

**Criterios de Aceptación:**
- [ ] Define campos para registrar parámetros de ronda
- [ ] Incluye fecha de diseño estadístico, valor asignado, H/E
- [ ] Establece formato para aprobación de planificación
- [ ] Integra con P-PSEA-09 Procedimiento de Planificación
- [ ] Aprobado por PT Coordinator

---

### P4-3: F-PSEA-04 Formato Informe Resultados

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P4 |
| **Tipo** | F |
| **Código** | F-PSEA-04 |
| **Título** | Formato de Informe de Resultados EA |
| **Estado Actual** | v0 (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 3 horas |
| **Complejidad** | Baja |
| **Dependencias** | P-PSEA-07 |
| **Normas** | 17043:2023 7.4.3 |
| **Responsable** | PT Coordinator |

**Criterios de Aceptación:**
- [ ] Define estructura estándar de informe de resultados
- [ ] Incluye secciones requeridas por 7.4.3.2
- [ ] Establece formatos para tablas de resultados, z-scores, zeta-scores
- [ ] Integra con P-PSEA-07 Procedimiento de Informe Resultados
- [ ] Alineado con plantillas de CALAIRE-APP
- [ ] Aprobado por PT Coordinator

---

### P4-4: F-PSEA-01 Formato de Registro de Competencia

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P4 |
| **Tipo** | F |
| **Código** | F-PSEA-01 |
| **Título** | Formato de Registro de Competencia del Personal |
| **Estado Actual** | TBD (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 2 horas |
| **Complejidad** | Baja |
| **Dependencias** | P-PSEA-28 |
| **Normas** | 17025:2017 6.2, 17043:2023 6.2 |
| **Responsable** | QMS Coordinator |

**Criterios de Aceptación:**
- [ ] Define campos para registrar competencias por rol
- [ ] Incluye formación, experiencia, evaluaciones, autorizaciones
- [ ] Establece formato para seguimiento de capacitación
- [ ] Integra con P-PSEA-28 Procedimiento de Gestión de Competencia
- [ ] Aprobado por QMS Coordinator

---

### P4-5: F-PSEA-02 Formato de Registro Ambiental

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P4 |
| **Tipo** | F |
| **Código** | F-PSEA-02 |
| **Título** | Formato de Registro de Condiciones Ambientales |
| **Estado Actual** | TBD (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 2 horas |
| **Complejidad** | Baja |
| **Dependencias** | P-PSEA-29 |
| **Normas** | 17025:2017 6.3, 17043:2023 6.3 |
| **Responsable** | Coordinador de Instalaciones |

**Criterios de Aceptación:**
- [ ] Define campos para registrar temperatura, humedad, presión
- [ ] Incluye frecuencia de monitoreo por área
- [ ] Establece formato para alertas de desviaciones
- [ ] Integra con P-PSEA-29 Procedimiento de Control de Acceso
- [ ] Aprobado por Coordinador de Instalaciones

---

### P4-6: F-PSEA-03 Formato de Evaluación de Condición

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P4 |
| **Tipo** | F |
| **Código** | F-PSEA-03 |
| **Título** | Formato de Evaluación de Condición de Items PT |
| **Estado Actual** | TBD (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 2 horas |
| **Complejidad** | Baja |
| **Dependencias** | P-PSEA-10 |
| **Normas** | 17043:2023 7.3.3.3 |
| **Responsable** | Coordinador de Logística PT |

**Criterios de Aceptación:**
- [ ] Define campos para evaluar condición de items al recepcionar
- [ ] Incluye criterios de aceptación/rechazo
- [ ] Establece formato para registro de incidencias
- [ ] Integra con P-PSEA-10 Procedimiento de Manejo de Items PT
- [ ] Aprobado por Coordinador de Logística PT

---

### P4-7: F-PSEA-04 Formato de Confirmación de Entrega

| Atributo | Valor |
|----------|-------|
| **Prioridad** | P4 |
| **Tipo** | F |
| **Código** | F-PSEA-04 |
| **Título** | Formato de Confirmación de Entrega de Items PT |
| **Estado Actual** | TBD (por crear) |
| **Acción** | Crear |
| **Esfuerzo** | 2 horas |
| **Complejidad** | Baja |
| **Dependencias** | P-PSEA-10 |
| **Normas** | 17043:2023 7.3.4.5 |
| **Responsable** | Coordinador de Logística PT |

**Criterios de Aceptación:**
- [ ] Define campos para confirmar entrega al participante
- [ ] Incluye firma de recepción y condiciones de transporte
- [ ] Establece formato para registro de envíos
- [ ] Integra con P-PSEA-10 Procedimiento de Manejo de Items PT
- [ ] Aprobado por Coordinador de Logística PT

---

## Resumen del Backlog

### Por Prioridad

| Prioridad | Cantidad | Esfuerzo Total (horas) |
|-----------|----------|------------------------|
| P1 (Crítica) | 10 documentos | 52 horas |
| P2 (Alta) | 10 documentos | 44 horas |
| P3 (Media) | 10 documentos | 34 horas |
| P4 (Baja) | 7 documentos | 17 horas |
| **Total** | **37 documentos** | **147 horas** |

### Por Tipo de Documento

| Tipo | Cantidad | Esfuerzo Total (horas) |
|------|----------|------------------------|
| DG | 1 | 8 horas |
| P | 28 documentos | 128 horas |
| F | 8 formatos | 11 horas |
| **Total** | **37 documentos** | **147 horas** |

### Por Oleada de Implementación

| Oleada | Documentos | Prioridad | Esfuerzo (horas) | Duración Estimada |
|--------|-----------|-----------|-----------------|-------------------|
| Oleada 1 | 10 | P1 | 52 | 2-3 semanas |
| Oleada 2 | 10 | P2 | 44 | 2 semanas |
| Oleada 3 | 10 | P3 | 34 | 1-2 semanas |
| Oleada 4 | 7 | P4 | 17 | 1 semana |
| **Total** | **37** | **P1-P4** | **147** | **6-8 semanas** |

---

## Referencias

- `docs/docs_sgc/Matriz Maestra de Cumplimiento Normativo.md` - Matriz de trazabilidad normativa
- `docs/docs_sgc/Inventario Documental del SGC.md` - Inventario de documentos existentes
- `logs/plans/260208_1932_plan_ajuste-sgc-17025-17043-13528.md` - Plan de ajuste del SGC
- `docs/referencias/iso 17025_2017.md` - ISO/IEC 17025:2017
- `docs/referencias/iso 17043_2023.md` - ISO/IEC 17043:2023
- `docs/referencias/iso 13528_2022.md` - ISO 13528:2022

---

**Fin del Backlog Priorizado**
