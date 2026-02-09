# Matriz Maestra de Cumplimiento Normativo - CALAIRE-EA

**Creado**: 2026-02-08
**Versión**: 1.0
**Estado**: draft
**Responsable**: TBD

---

## Objetivo

Esta matriz establece la trazabilidad normativa entre los requisitos de ISO/IEC 17025:2017, ISO/IEC 17043:2023 e ISO 13528:2022, y los documentos del sistema de gestión de calidad (SGC) del proyecto CALAIRE-EA, garantizando que cada requisito normativo tiene asignado al menos un documento tipo DG/P/I/F y evidencia de cumplimiento.

---

## Jerarquía Normativa

```
ISO/IEC 17025:2017 (Macro - Sistema de gestión de competencia)
    └── ISO/IEC 17043:2023 (Operativo - Requisitos específicos para PT)
            └── ISO 13528:2022 (Metodológico - Métodos estadísticos)
```

---

## Convenciones

| Columna | Descripción | Valores posibles |
|---------|-------------|------------------|
| **Norma** | Norma de referencia | 17025:2017, 17043:2023, 13528:2022 |
| **Capítulo** | Capítulo de la norma | 4-8 (17025), 7-8 (17043), 4-11 (13528) |
| **Cláusula** | Cláusula específica | 4.1.1, 7.2.1.1, etc. |
| **Título Requisito** | Título del requisito normativo | Texto de la norma |
| **Tipo Documento** | Tipo de documento SGC | DG, P, I, F |
| **Código Documento** | Código del documento | DG-PSEA-##, P-PSEA-##, I-PSEA-##, F-PSEA-## |
| **Título Documento** | Título del documento | Nombre del documento |
| **Versión** | Versión del documento | v1.0, v1.1, etc. |
| **Estado Documento** | Estado del documento | draft, in_review, approved, obsolete |
| **Responsable** | Responsable del cumplimiento | Nombre del rol/persona |
| **Estado Cumplimiento** | Estado de cumplimiento | cumple, no_cumple, parcial, na |
| **Evidencia** | Evidencia de cumplimiento | Referencia a evidencia |
| **Observaciones** | Notas adicionales | Texto libre |

---

## Matriz - ISO/IEC 17025:2017

### Capítulo 4: General Requirements

| Norma | Capítulo | Cláusula | Título Requisito | Tipo Documento | Código Documento | Título Documento | Versión | Estado Documento | Responsable | Estado Cumplimiento | Evidencia | Observaciones |
|-------|----------|----------|------------------|----------------|------------------|------------------|---------|------------------|-------------|---------------------|-----------|---------------|
| 17025:2017 | 4 | 4.1 | Impartiality | DG | DG-PSEA-01 | Manual de Calidad | v1.0 | draft | QMS Coordinator | parcial | TBD | Requiere desarrollo |
| 17025:2017 | 4 | 4.2 | Confidentiality | P | P-PSEA-02 | Procedimiento de Confidencialidad | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 4 | 4.3 | Impartiality policy | DG | DG-PSEA-01 | Manual de Calidad | v1.0 | draft | QMS Coordinator | parcial | TBD | Requiere desarrollo |

### Capítulo 5: Structural Requirements

| Norma | Capítulo | Cláusula | Título Requisito | Tipo Documento | Código Documento | Título Documento | Versión | Estado Documento | Responsable | Estado Cumplimiento | Evidencia | Observaciones |
|-------|----------|----------|------------------|----------------|------------------|------------------|---------|------------------|-------------|---------------------|-----------|---------------|
| 17025:2017 | 5 | 5.1 | Legal entity | DG | DG-PSEA-01 | Manual de Calidad | v1.0 | draft | Project Lead | cumple | TBD | Verificado |
| 17025:2017 | 5 | 5.2 | Management identification | DG | DG-PSEA-01 | Manual de Calidad | v1.0 | draft | Project Lead | cumple | TBD | Verificado |
| 17025:2017 | 5 | 5.3 | Defined PT schemes | P | P-PSEA-01 | Protocolo General EA | v1.0 | in_review | PT Provider Lead | parcial | TBD | Requiere actualización |
| 17025:2017 | 5 | 5.4 | PT activities compliance | P | P-PSEA-01 | Protocolo General EA | v1.0 | in_review | PT Provider Lead | parcial | TBD | Requiere actualización |
| 17025:2017 | 5 | 5.5 | Organization and structure | DG | DG-PSEA-01 | Manual de Calidad | v1.0 | draft | QMS Coordinator | parcial | TBD | Requiere desarrollo |
| 17025:2017 | 5 | 5.6 | Personnel authority | DG | DG-PSEA-01 | Manual de Calidad | v1.0 | draft | QMS Coordinator | parcial | TBD | Requiere desarrollo |
| 17025:2017 | 5 | 5.7 | Management commitment | DG | DG-PSEA-01 | Manual de Calidad | v1.0 | draft | Project Lead | parcial | TBD | Requiere desarrollo |

### Capítulo 6: Resource Requirements

| Norma | Capítulo | Cláusula | Título Requisito | Tipo Documento | Código Documento | Título Documento | Versión | Estado Documento | Responsable | Estado Cumplimiento | Evidencia | Observaciones |
|-------|----------|----------|------------------|----------------|------------------|------------------|---------|------------------|-------------|---------------------|-----------|---------------|
| 17025:2017 | 6 | 6.1.1 | Access to resources | DG | DG-PSEA-01 | Manual de Calidad | v1.0 | draft | Project Lead | cumple | TBD | Verificado |
| 17025:2017 | 6 | 6.1.2 | Measurement/test requirements | I | I-PSEA-01 | Instructivo de Caracterización | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 6 | 6.1.3 | Reference materials | I | I-PSEA-02 | Instructivo de Producción PT Items | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 6 | 6.2.1 | Competent personnel | DG | DG-PSEA-01 | Manual de Calidad | v1.0 | draft | QMS Coordinator | parcial | TBD | Requiere desarrollo |
| 17025:2017 | 6 | 6.2.2 | Personnel competence | P | P-PSEA-03 | Procedimiento de Gestión de Competencia | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 6 | 6.2.3 | Competence management | P | P-PSEA-03 | Procedimiento de Gestión de Competencia | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 6 | 6.2.4 | Impartial personnel | P | P-PSEA-03 | Procedimiento de Gestión de Competencia | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 6 | 6.2.5 | Documented competence | F | F-PSEA-01 | Formato de Registro de Competencia | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 6 | 6.2.6 | Personnel authorization | P | P-PSEA-03 | Procedimiento de Gestión de Competencia | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 6 | 6.2.7 | Communication of duties | P | P-PSEA-03 | Procedimiento de Gestión de Competencia | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 6 | 6.3.1 | Facilities for PT schemes | DG | DG-PSEA-01 | Manual de Calidad | v1.0 | draft | Project Lead | parcial | TBD | Requiere desarrollo |
| 17025:2017 | 6 | 6.3.2 | Environmental conditions | I | I-PSEA-03 | Instructivo de Control Ambiental | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 6 | 6.3.3 | Environmental monitoring | F | F-PSEA-02 | Formato de Registro Ambiental | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 6 | 6.3.4 | Access control | P | P-PSEA-04 | Procedimiento de Control de Acceso | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 6 | 6.3.5 | Separation of areas | P | P-PSEA-04 | Procedimiento de Control de Acceso | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 6 | 6.4.1 | External provider limitations | P | P-PSEA-05 | Procedimiento de Proveedores Externos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 6 | 6.4.2 | External provider competence | P | P-PSEA-05 | Procedimiento de Proveedores Externos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 6 | 6.4.3 | External provider communication | P | P-PSEA-05 | Procedimiento de Proveedores Externos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 6 | 6.4.4 | External provider records | P | P-PSEA-05 | Procedimiento de Proveedores Externos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 6 | 6.4.5 | External provider requirements | P | P-PSEA-05 | Procedimiento de Proveedores Externos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 6 | 6.4.6 | Responsibility for external providers | P | P-PSEA-05 | Procedimiento de Proveedores Externos | TBD | TBD | TBD | no_cumple | TBD | Por crear |

### Capítulo 7: Process Requirements

| Norma | Capítulo | Cláusula | Título Requisito | Tipo Documento | Código Documento | Título Documento | Versión | Estado Documento | Responsable | Estado Cumplimiento | Evidencia | Observaciones |
|-------|----------|----------|------------------|----------------|------------------|------------------|---------|------------------|-------------|---------------------|-----------|---------------|
| 17025:2017 | 7 | 7.1 | Review of requests | P | P-PSEA-06 | Procedimiento de Revisión de Contratos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 7 | 7.2 | Selection of methods | P | P-PSEA-07 | Procedimiento de Selección de Métodos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 7 | 7.3 | Validation of methods | I | I-PSEA-04 | Instructivo de Validación de Métodos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 7 | 7.4 | Estimation of uncertainty | I | I-PSEA-05 | Instructivo de Estimación de Incertidumbre | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 7 | 7.5 | Traceability | P | P-PSEA-08 | Procedimiento de Trazabilidad | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 7 | 7.6 | Sampling | P | P-PSEA-09 | Procedimiento de Muestreo (si aplica) | TBD | TBD | TBD | na | TBD | No aplica |
| 17025:2017 | 7 | 7.7 | Handling of test items | P | P-PSEA-10 | Procedimiento de Manejo de Items PT | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 7 | 7.8 | Quality control of data | I | I-PSEA-06 | Instructivo de Control de Calidad de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 7 | 7.9 | Reporting of results | P | P-PSEA-11 | Procedimiento de Reporte de Resultados | TBD | TBD | TBD | no_cumple | TBD | Por crear |

### Capítulo 8: Management System Requirements

| Norma | Capítulo | Cláusula | Título Requisito | Tipo Documento | Código Documento | Título Documento | Versión | Estado Documento | Responsable | Estado Cumplimiento | Evidencia | Observaciones |
|-------|----------|----------|------------------|----------------|------------------|------------------|---------|------------------|-------------|---------------------|-----------|---------------|
| 17025:2017 | 8 | 8.1 | Options for management system | DG | DG-PSEA-01 | Manual de Calidad | v1.0 | draft | QMS Coordinator | parcial | TBD | Requiere desarrollo |
| 17025:2017 | 8 | 8.2 | Management system documentation | DG | DG-PSEA-01 | Manual de Calidad | v1.0 | draft | QMS Coordinator | parcial | TBD | Requiere desarrollo |
| 17025:2017 | 8 | 8.3 | Control of documents | P | P-PSEA-12 | Procedimiento de Control Documental | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 8 | 8.4 | Control of records | P | P-PSEA-13 | Procedimiento de Control de Registros | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 8 | 8.5 | Actions to address risks | P | P-PSEA-14 | Procedimiento de Gestión de Riesgos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 8 | 8.6 | Improvements | P | P-PSEA-15 | Procedimiento de Mejora Continua | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 8 | 8.7 | Nonconformities | P | P-PSEA-16 | Procedimiento de No Conformidades | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 8 | 8.8 | Internal audits | P | P-PSEA-17 | Procedimiento de Auditorías Internas | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17025:2017 | 8 | 8.9 | Management review | P | P-PSEA-18 | Procedimiento de Revisión por Dirección | TBD | TBD | TBD | no_cumple | TBD | Por crear |

---

## Matriz - ISO/IEC 17043:2023

### Capítulo 4: General Requirements

| Norma | Capítulo | Cláusula | Título Requisito | Tipo Documento | Código Documento | Título Documento | Versión | Estado Documento | Responsable | Estado Cumplimiento | Evidencia | Observaciones |
|-------|----------|----------|------------------|----------------|------------------|------------------|---------|------------------|-------------|---------------------|-----------|---------------|
| 17043:2023 | 4 | 4.1.1 | Impartial PT activities | DG | DG-PSEA-01 | Manual de Calidad | v1.0 | draft | QMS Coordinator | parcial | TBD | Requiere desarrollo |
| 17043:2023 | 4 | 4.1.2 | Structure for impartiality | DG | DG-PSEA-01 | Manual de Calidad | v1.0 | draft | QMS Coordinator | parcial | TBD | Requiere desarrollo |
| 17043:2023 | 4 | 4.1.3 | Responsibility for impartiality | DG | DG-PSEA-01 | Manual de Calidad | v1.0 | draft | Project Lead | parcial | TBD | Requiere desarrollo |
| 17043:2023 | 4 | 4.1.4 | Monitoring of activities | P | P-PSEA-19 | Procedimiento de Monitoreo de Imparcialidad | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 4 | 4.1.5 | Threat elimination | P | P-PSEA-19 | Procedimiento de Monitoreo de Imparcialidad | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 4 | 4.1.6 | Management commitment | DG | DG-PSEA-01 | Manual de Calidad | v1.0 | draft | Project Lead | parcial | TBD | Requiere desarrollo |
| 17043:2023 | 4 | 4.2.1 | Confidentiality management | P | P-PSEA-02 | Procedimiento de Confidencialidad | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 4 | 4.2.2 | Legal release of information | P | P-PSEA-02 | Procedimiento de Confidencialidad | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 4 | 4.2.3 | Third-party confidentiality | P | P-PSEA-02 | Procedimiento de Confidencialidad | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 4 | 4.2.4 | Personnel confidentiality | P | P-PSEA-02 | Procedimiento de Confidencialidad | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 4 | 4.2.5 | Participant identity confidentiality | P | P-PSEA-02 | Procedimiento de Confidencialidad | TBD | TBD | TBD | no_cumple | TBD | Por crear |

### Capítulo 5: Structural Requirements

| Norma | Capítulo | Cláusula | Título Requisito | Tipo Documento | Código Documento | Título Documento | Versión | Estado Documento | Responsable | Estado Cumplimiento | Evidencia | Observaciones |
|-------|----------|----------|------------------|----------------|------------------|------------------|---------|------------------|-------------|---------------------|-----------|---------------|
| 17043:2023 | 5 | 5.1 | Legal entity | DG | DG-PSEA-01 | Manual de Calidad | v1.0 | draft | Project Lead | cumple | TBD | Verificado |
| 17043:2023 | 5 | 5.2 | Management identification | DG | DG-PSEA-01 | Manual de Calidad | v1.0 | draft | Project Lead | cumple | TBD | Verificado |
| 17043:2023 | 5 | 5.3 | Defined PT schemes | P | P-PSEA-01 | Protocolo General EA | v1.0 | in_review | PT Provider Lead | parcial | TBD | Requiere actualización |
| 17043:2023 | 5 | 5.4 | PT activities compliance | P | P-PSEA-01 | Protocolo General EA | v1.0 | in_review | PT Provider Lead | parcial | TBD | Requiere actualización |
| 17043:2023 | 5 | 5.5 | Organization structure | DG | DG-PSEA-01 | Manual de Calidad | v1.0 | draft | QMS Coordinator | parcial | TBD | Requiere desarrollo |
| 17043:2023 | 5 | 5.6 | Personnel authority | DG | DG-PSEA-01 | Manual de Calidad | v1.0 | draft | QMS Coordinator | parcial | TBD | Requiere desarrollo |
| 17043:2023 | 5 | 5.7 | Management communication | DG | DG-PSEA-01 | Manual de Calidad | v1.0 | draft | Project Lead | parcial | TBD | Requiere desarrollo |

### Capítulo 6: Resource Requirements

| Norma | Capítulo | Cláusula | Título Requisito | Tipo Documento | Código Documento | Título Documento | Versión | Estado Documento | Responsable | Estado Cumplimiento | Evidencia | Observaciones |
|-------|----------|----------|------------------|----------------|------------------|------------------|---------|------------------|-------------|---------------------|-----------|---------------|
| 17043:2023 | 6 | 6.1.1 | Access to resources | DG | DG-PSEA-01 | Manual de Calidad | v1.0 | draft | Project Lead | cumple | TBD | Verificado |
| 17043:2023 | 6 | 6.1.2 | Measurement/test requirements | I | I-PSEA-01 | Instructivo de Caracterización | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 6 | 6.1.3 | Reference materials | I | I-PSEA-02 | Instructivo de Producción PT Items | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 6 | 6.2.1 | Competent personnel | DG | DG-PSEA-01 | Manual de Calidad | v1.0 | draft | QMS Coordinator | parcial | TBD | Requiere desarrollo |
| 17043:2023 | 6 | 6.2.2 | Personnel competence | P | P-PSEA-03 | Procedimiento de Gestión de Competencia | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 6 | 6.2.3 | Competence management | P | P-PSEA-03 | Procedimiento de Gestión de Competencia | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 6 | 6.2.4 | Impartial personnel | P | P-PSEA-03 | Procedimiento de Gestión de Competencia | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 6 | 6.2.5 | Documented competence | F | F-PSEA-01 | Formato de Registro de Competencia | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 6 | 6.2.6 | Personnel authorization | P | P-PSEA-03 | Procedimiento de Gestión de Competencia | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 6 | 6.2.7 | Communication of duties | P | P-PSEA-03 | Procedimiento de Gestión de Competencia | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 6 | 6.3.1 | Facilities for PT schemes | DG | DG-PSEA-01 | Manual de Calidad | v1.0 | draft | Project Lead | parcial | TBD | Requiere desarrollo |
| 17043:2023 | 6 | 6.3.2 | Environmental conditions | I | I-PSEA-03 | Instructivo de Control Ambiental | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 6 | 6.3.3 | Environmental monitoring | F | F-PSEA-02 | Formato de Registro Ambiental | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 6 | 6.3.4 | Access control | P | P-PSEA-04 | Procedimiento de Control de Acceso | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 6 | 6.3.5 | Separation of areas | P | P-PSEA-04 | Procedimiento de Control de Acceso | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 6 | 6.4.1 | External provider limitations | P | P-PSEA-05 | Procedimiento de Proveedores Externos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 6 | 6.4.2 | External provider competence | P | P-PSEA-05 | Procedimiento de Proveedores Externos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 6 | 6.4.3 | External provider communication | P | P-PSEA-05 | Procedimiento de Proveedores Externos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 6 | 6.4.4 | External provider records | P | P-PSEA-05 | Procedimiento de Proveedores Externos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 6 | 6.4.5 | External provider requirements | P | P-PSEA-05 | Procedimiento de Proveedores Externos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 6 | 6.4.6 | Responsibility for external providers | P | P-PSEA-05 | Procedimiento de Proveedores Externos | TBD | TBD | TBD | no_cumple | TBD | Por crear |

### Capítulo 7: Process Requirements

| Norma | Capítulo | Cláusula | Título Requisito | Tipo Documento | Código Documento | Título Documento | Versión | Estado Documento | Responsable | Estado Cumplimiento | Evidencia | Observaciones |
|-------|----------|----------|------------------|----------------|------------------|------------------|---------|------------------|-------------|---------------------|-----------|---------------|
| 17043:2023 | 7 | 7.1.1.1 | Review of requests | P | P-PSEA-06 | Procedimiento de Revisión de Contratos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.1.1.2 | Review scope | P | P-PSEA-06 | Procedimiento de Revisión de Contratos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.1.1.3 | Records of reviews | P | P-PSEA-06 | Procedimiento de Revisión de Contratos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.1.1.4 | Customer notification | P | P-PSEA-06 | Procedimiento de Revisión de Contratos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.1.1.5 | Contract amendments | P | P-PSEA-06 | Procedimiento de Revisión de Contratos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.1.2.1 | PT scheme information | P | P-PSEA-20 | Procedimiento de Comunicación PT | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.1.2.2 | Change notification | P | P-PSEA-20 | Procedimiento de Comunicación PT | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.1.2.3 | Communication records | P | P-PSEA-20 | Procedimiento de Comunicación PT | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.2.1.1 | Design and planning activities | P | P-PSEA-09 | Procedimiento de Planificación Ronda EA | v1.0 | draft | PT Coordinator | parcial | TBD | Requiere actualización |
| 17043:2023 | 7 | 7.2.1.2 | Significant changes | P | P-PSEA-09 | Procedimiento de Planificación Ronda EA | v1.0 | draft | PT Coordinator | parcial | TBD | Requiere actualización |
| 17043:2023 | 7 | 7.2.1.3 | Documented plan | P | P-PSEA-09 | Procedimiento de Planificación Ronda EA | v1.0 | draft | PT Coordinator | parcial | TBD | Requiere actualización |
| 17043:2023 | 7 | 7.2.2.1 | Statistical design | I | I-PSEA-07 | Instructivo de Diseño Estadístico | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 cap 5 |
| 17043:2023 | 7 | 7.2.2.2 | Documented statistical design | I | I-PSEA-07 | Instructivo de Diseño Estadístico | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 cap 5 |
| 17043:2023 | 7 | 7.2.2.3 | Statistical considerations | I | I-PSEA-07 | Instructivo de Diseño Estadístico | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 cap 5 |
| 17043:2023 | 7 | 7.2.3.1 | Assigned value procedure | I | I-PSEA-08 | Instructivo de Valor Asignado | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 cap 7 |
| 17043:2023 | 7 | 7.2.3.2 | Metrological traceability (calibration) | I | I-PSEA-08 | Instructivo de Valor Asignado | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 cap 7 |
| 17043:2023 | 7 | 7.2.3.3 | Metrological traceability (general) | I | I-PSEA-08 | Instructivo de Valor Asignado | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 cap 7 |
| 17043:2023 | 7 | 7.2.3.4 | Consensus value uncertainty | I | I-PSEA-08 | Instructivo de Valor Asignado | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 cap 7 |
| 17043:2023 | 7 | 7.2.3.5 | Disclosure policy | P | P-PSEA-21 | Procedimiento de Divulgación de Valores | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.3.1.1 | Production procedures | I | I-PSEA-02 | Instructivo de Producción PT Items | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.3.1.2 | Selection and handling | I | I-PSEA-02 | Instructivo de Producción PT Items | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.3.1.3 | Participant instructions | I | I-PSEA-09 | Instructivo de Instrucciones a Participantes | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.3.2.1 | Homogeneity/stability criteria | I | I-PSEA-10 | Instructivo de Homogeneidad y Estabilidad | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 cap 6 |
| 17043:2023 | 7 | 7.3.2.2 | Homogeneity/stability procedures | I | I-PSEA-10 | Instructivo de Homogeneidad y Estabilidad | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 cap 6 |
| 17043:2023 | 7 | 7.3.2.3 | Timing of assessment | I | I-PSEA-10 | Instructivo de Homogeneidad y Estabilidad | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 cap 6 |
| 17043:2023 | 7 | 7.3.2.4 | Assessment methods | I | I-PSEA-10 | Instructivo de Homogeneidad y Estabilidad | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 cap 6 |
| 17043:2023 | 7 | 7.3.2.5 | Stability throughout round | I | I-PSEA-10 | Instructivo de Homogeneidad y Estabilidad | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 cap 6 |
| 17043:2023 | 7 | 7.3.2.6 | Retained items | I | I-PSEA-10 | Instructivo de Homogeneidad y Estabilidad | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 cap 6 |
| 17043:2023 | 7 | 7.3.3.1 | Identification and storage | P | P-PSEA-10 | Procedimiento de Manejo de Items PT | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.3.3.2 | Dispatch and receipt | P | P-PSEA-10 | Procedimiento de Manejo de Items PT | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.3.3.3 | Condition assessment | F | F-PSEA-03 | Formato de Evaluación de Condición | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.3.3.4 | Hazardous items | P | P-PSEA-10 | Procedimiento de Manejo de Items PT | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.3.4.1 | Packaging and labelling | P | P-PSEA-10 | Procedimiento de Manejo de Items PT | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.3.4.2 | Transport conditions | P | P-PSEA-10 | Procedimiento de Manejo de Items PT | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.3.4.3 | Transport instructions | I | I-PSEA-09 | Instructivo de Instrucciones a Participantes | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.3.4.4 | Labelling requirements | P | P-PSEA-10 | Procedimiento de Manejo de Items PT | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.3.4.5 | Delivery confirmation | F | F-PSEA-04 | Formato de Confirmación de Entrega | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.3.5.1 | Advance notice | P | P-PSEA-20 | Procedimiento de Comunicación PT | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.3.5.2 | Participant instructions | I | I-PSEA-09 | Instructivo de Instrucciones a Participantes | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.4.1.1 | Data recording and analysis | I | I-PSEA-11 | Instructivo de Análisis de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 cap 8 |
| 17043:2023 | 7 | 7.4.1.2 | Summary and performance statistics | I | I-PSEA-11 | Instructivo de Análisis de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 cap 8 |
| 17043:2023 | 7 | 7.4.1.3 | Outlier influence minimization | I | I-PSEA-11 | Instructivo de Análisis de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 cap 6 |
| 17043:2023 | 7 | 7.4.1.4 | Different methods treatment | I | I-PSEA-11 | Instructivo de Análisis de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 cap 6 |
| 17043:2023 | 7 | 7.4.1.5 | Inappropriate results | I | I-PSEA-11 | Instructivo de Análisis de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 cap 6 |
| 17043:2023 | 7 | 7.4.1.6 | Unsuitable items | I | I-PSEA-11 | Instructivo de Análisis de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 cap 6 |
| 17043:2023 | 7 | 7.4.2.1 | Valid evaluation methods | I | I-PSEA-12 | Instructivo de Evaluación de Desempeño | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 cap 9 |
| 17043:2023 | 7 | 7.4.2.2 | Expert commentary | I | I-PSEA-12 | Instructivo de Evaluación de Desempeño | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 cap 9 |
| 17043:2023 | 7 | 7.4.3.1 | Report requirements | P | P-PSEA-22 | Procedimiento de Reportes PT | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.4.3.2 | Report content | P | P-PSEA-22 | Procedimiento de Reportes PT | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.4.3.3 | Report timelines | P | P-PSEA-22 | Procedimiento de Reportes PT | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.4.3.4 | Report usage policy | P | P-PSEA-22 | Procedimiento de Reportes PT | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.4.3.5 | Amended reports | P | P-PSEA-22 | Procedimiento de Reportes PT | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.4.3.6 | Subset amended reports | P | P-PSEA-22 | Procedimiento de Reportes PT | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.4.3.7 | Statements of participation | P | P-PSEA-22 | Procedimiento de Reportes PT | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.5.1.1 | Technical records | P | P-PSEA-13 | Procedimiento de Control de Registros | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.5.1.2 | Recording of data | P | P-PSEA-13 | Procedimiento de Control de Registros | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.5.1.3 | Amendments tracking | P | P-PSEA-13 | Procedimiento de Control de Registros | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.5.2.1 | Access to data | P | P-PSEA-23 | Procedimiento de Gestión de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.5.2.2 | System validation | I | I-PSEA-13 | Instructivo de Validación de Sistemas | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.5.2.3 | System requirements | I | I-PSEA-13 | Instructivo de Validación de Sistemas | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 7 | 7.5.2.4 | Off-site systems | P | P-PSEA-23 | Procedimiento de Gestión de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear |

### Capítulo 8: Management System Requirements

| Norma | Capítulo | Cláusula | Título Requisito | Tipo Documento | Código Documento | Título Documento | Versión | Estado Documento | Responsable | Estado Cumplimiento | Evidencia | Observaciones |
|-------|----------|----------|------------------|----------------|------------------|------------------|---------|------------------|-------------|---------------------|-----------|---------------|
| 17043:2023 | 8 | 8.1 | Options for management system | DG | DG-PSEA-01 | Manual de Calidad | v1.0 | draft | QMS Coordinator | parcial | TBD | Requiere desarrollo |
| 17043:2023 | 8 | 8.2 | Management system documentation | DG | DG-PSEA-01 | Manual de Calidad | v1.0 | draft | QMS Coordinator | parcial | TBD | Requiere desarrollo |
| 17043:2023 | 8 | 8.3 | Control of documents | P | P-PSEA-12 | Procedimiento de Control Documental | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 8 | 8.4 | Control of records | P | P-PSEA-13 | Procedimiento de Control de Registros | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 8 | 8.5 | Actions to address risks | P | P-PSEA-14 | Procedimiento de Gestión de Riesgos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 8 | 8.6 | Improvements | P | P-PSEA-15 | Procedimiento de Mejora Continua | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 8 | 8.7 | Nonconformities | P | P-PSEA-16 | Procedimiento de No Conformidades | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 8 | 8.8 | Internal audits | P | P-PSEA-17 | Procedimiento de Auditorías Internas | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 8 | 8.9 | Management review | P | P-PSEA-18 | Procedimiento de Revisión por Dirección | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 8 | 8.10 | Complaints | P | P-PSEA-24 | Procedimiento de Quejas | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 17043:2023 | 8 | 8.11 | Appeals | P | P-PSEA-25 | Procedimiento de Apelaciones | TBD | TBD | TBD | no_cumple | TBD | Por crear |

---

## Matriz - ISO 13528:2022

### Capítulo 4: General Principles

| Norma | Capítulo | Cláusula | Título Requisito | Tipo Documento | Código Documento | Título Documento | Versión | Estado Documento | Responsable | Estado Cumplimiento | Evidencia | Observaciones |
|-------|----------|----------|------------------|----------------|------------------|------------------|---------|------------------|-------------|---------------------|-----------|---------------|
| 13528:2022 | 4 | 4.1.1 | Statistical validity | I | I-PSEA-07 | Instructivo de Diseño Estadístico | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 4 | 4.1.2 | Consistency with objectives | I | I-PSEA-07 | Instructivo de Diseño Estadístico | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 4 | 4.1.3 | Description of methods | I | I-PSEA-07 | Instructivo de Diseño Estadístico | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 4 | 4.1.4 | Software validation | I | I-PSEA-13 | Instructivo de Validación de Sistemas | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 4 | 4.2.1 | Basic model (quantitative) | I | I-PSEA-07 | Instructivo de Diseño Estadístico | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 4 | 4.2.2 | Basic model (qualitative) | I | I-PSEA-07 | Instructivo de Diseño Estadístico | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 4 | 4.3.1 | Evaluation approaches | I | I-PSEA-12 | Instructivo de Evaluación de Desempeño | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 4 | 4.3.2 | Mixed approaches | I | I-PSEA-12 | Instructivo de Evaluación de Desempeño | TBD | TBD | TBD | no_cumple | TBD | Por crear |

### Capítulo 5: Statistical Design

| Norma | Capítulo | Cláusula | Título Requisito | Tipo Documento | Código Documento | Título Documento | Versión | Estado Documento | Responsable | Estado Cumplimiento | Evidencia | Observaciones |
|-------|----------|----------|------------------|----------------|------------------|------------------|---------|------------------|-------------|---------------------|-----------|---------------|
| 13528:2022 | 5 | 5.1 | Statistical design introduction | I | I-PSEA-07 | Instructivo de Diseño Estadístico | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 5 | 5.2.1 | Design basis | I | I-PSEA-07 | Instructivo de Diseño Estadístico | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 5 | 5.2.2 | Data types | I | I-PSEA-07 | Instructivo de Diseño Estadístico | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 5 | 5.2.3 | Multiple purposes | I | I-PSEA-07 | Instructivo de Diseño Estadístico | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 5 | 5.3.1 | Statistical distribution | I | I-PSEA-07 | Instructivo de Diseño Estadístico | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 5 | 5.3.2 | Symmetry verification | I | I-PSEA-07 | Instructivo de Diseño Estadístico | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 5 | 5.3.3 | Asymmetry handling | I | I-PSEA-07 | Instructivo de Diseño Estadístico | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 5 | 5.3.4 | Specific distributions | I | I-PSEA-07 | Instructivo de Diseño Estadístico | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 5 | 5.3.5 | Assumption demonstration | I | I-PSEA-07 | Instructivo de Diseño Estadístico | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 5 | 5.4.1 | Small number of participants | I | I-PSEA-07 | Instructivo de Diseño Estadístico | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 5 | 5.4.2 | Minimum participants | I | I-PSEA-07 | Instructivo de Diseño Estadístico | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 5 | 5.5.1.1 | Reporting format requirements | I | I-PSEA-09 | Instructivo de Instrucciones a Participantes | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 5 | 5.5.1.2 | Consistent format | I | I-PSEA-09 | Instructivo de Instrucciones a Participantes | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 5 | 5.5.2 | Replicate measurements | I | I-PSEA-09 | Instructivo de Instrucciones a Participantes | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 5 | 5.5.3.1 | Censored data processing | I | I-PSEA-09 | Instructivo de Instrucciones a Participantes | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 5 | 5.5.3.2 | Censored data options | I | I-PSEA-09 | Instructivo de Instrucciones a Participantes | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 5 | 5.5.3.3 | Consensus statistics with censored data | I | I-PSEA-11 | Instructivo de Análisis de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 5 | 5.5.3.4 | Censored results provisions | I | I-PSEA-11 | Instructivo de Análisis de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 5 | 5.5.4.1 | Significant digits | I | I-PSEA-09 | Instructivo de Instrucciones a Participantes | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 5 | 5.5.4.2 | Rounding error | I | I-PSEA-09 | Instructivo de Instrucciones a Participantes | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 5 | 5.5.4.3 | Specification of digits | I | I-PSEA-09 | Instructivo de Instrucciones a Participantes | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 5 | 5.5.4.4 | Varying significant digits | I | I-PSEA-11 | Instructivo de Análisis de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear |

### Capítulo 6: Initial Review

| Norma | Capítulo | Cláusula | Título Requisito | Tipo Documento | Código Documento | Título Documento | Versión | Estado Documento | Responsable | Estado Cumplimiento | Evidencia | Observaciones |
|-------|----------|----------|------------------|----------------|------------------|------------------|---------|------------------|-------------|---------------------|-----------|---------------|
| 13528:2022 | 6 | 6.1.1 | Homogeneity and stability assurance | I | I-PSEA-10 | Instructivo de Homogeneidad y Estabilidad | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 6 | 6.1.2 | Stability in calibration | I | I-PSEA-10 | Instructivo de Homogeneidad y Estabilidad | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 6 | 6.1.3 | Subset property checking | I | I-PSEA-10 | Instructivo de Homogeneidad y Estabilidad | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 6 | 6.2.1 | Different measurement methods | I | I-PSEA-11 | Instructivo de Análisis de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 6 | 6.2.2 | Different assigned values | I | I-PSEA-11 | Instructivo de Análisis de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 6 | 6.3.1 | Blunder removal | I | I-PSEA-11 | Instructivo de Análisis de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 6 | 6.3.2 | Blunder doubt handling | I | I-PSEA-11 | Instructivo de Análisis de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 6 | 6.4.1 | Visual review | I | I-PSEA-11 | Instructivo de Análisis de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 6 | 6.4.2 | Unexpected variability warning | I | I-PSEA-11 | Instructivo de Análisis de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 6 | 6.5.1 | Robust statistical methods | I | I-PSEA-11 | Instructivo de Análisis de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 anexo C |
| 13528:2022 | 6 | 6.5.2 | Choice of robust methods | I | I-PSEA-11 | Instructivo de Análisis de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 anexo C |
| 13528:2022 | 6 | 6.5.3 | Robust method responsibility | I | I-PSEA-11 | Instructivo de Análisis de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 anexo C |
| 13528:2022 | 6 | 6.6.1 | Outlier techniques | I | I-PSEA-11 | Instructivo de Análisis de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 6 | 6.6.2 | Outlier rejection strategies | I | I-PSEA-11 | Instructivo de Análisis de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear |

### Capítulo 7: Assigned Values

| Norma | Capítulo | Cláusula | Título Requisito | Tipo Documento | Código Documento | Título Documento | Versión | Estado Documento | Responsable | Estado Cumplimiento | Evidencia | Observaciones |
|-------|----------|----------|------------------|----------------|------------------|------------------|---------|------------------|-------------|---------------------|-----------|---------------|
| 13528:2022 | 7 | 7.1 | Introduction to assigned values | I | I-PSEA-08 | Instructivo de Valor Asignado | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 7 | 7.2 | Independent value assignment | I | I-PSEA-08 | Instructivo de Valor Asignado | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 7 | 7.3 | Consensus value assignment | I | I-PSEA-08 | Instructivo de Valor Asignado | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 7 | 7.4 | Consensus value calculation | I | I-PSEA-08 | Instructivo de Valor Asignado | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 7 | 7.5 | Uncertainty of consensus values | I | I-PSEA-08 | Instructivo de Valor Asignado | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 7 | 7.6 | Uncertainty of independent values | I | I-PSEA-08 | Instructivo de Valor Asignado | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 7 | 7.7 | Uncertainty from participants | I | I-PSEA-08 | Instructivo de Valor Asignado | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 7 | 7.8 | Combined uncertainty | I | I-PSEA-08 | Instructivo de Valor Asignado | TBD | TBD | TBD | no_cumple | TBD | Por crear |

### Capítulo 8: Performance Evaluation

| Norma | Capítulo | Cláusula | Título Requisito | Tipo Documento | Código Documento | Título Documento | Versión | Estado Documento | Responsable | Estado Cumplimiento | Evidencia | Observaciones |
|-------|----------|----------|------------------|----------------|------------------|------------------|---------|------------------|-------------|---------------------|-----------|---------------|
| 13528:2022 | 8 | 8.1 | Introduction to performance evaluation | I | I-PSEA-12 | Instructivo de Evaluación de Desempeño | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 8 | 8.2 | Z-score evaluation | I | I-PSEA-12 | Instructivo de Evaluación de Desempeño | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 cap 9 |
| 13528:2022 | 8 | 8.3 | Zeta score evaluation | I | I-PSEA-12 | Instructivo de Evaluación de Desempeño | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 cap 9 |
| 13528:2022 | 8 | 8.4 | Proportion of allowed limit | I | I-PSEA-12 | Instructivo de Evaluación de Desempeño | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 cap 9 |
| 13528:2022 | 8 | 8.5 | Combined score evaluation | I | I-PSEA-12 | Instructivo de Evaluación de Desempeño | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 cap 9 |
| 13528:2022 | 8 | 8.6 | Qualitative evaluation | I | I-PSEA-12 | Instructivo de Evaluación de Desempeño | TBD | TBD | TBD | no_cumple | TBD | Por crear - 13528 cap 11 |

### Capítulo 9: Score Calculation

| Norma | Capítulo | Cláusula | Título Requisito | Tipo Documento | Código Documento | Título Documento | Versión | Estado Documento | Responsable | Estado Cumplimiento | Evidencia | Observaciones |
|-------|----------|----------|------------------|----------------|------------------|------------------|---------|------------------|-------------|---------------------|-----------|---------------|
| 13528:2022 | 9 | 9.1 | Z-score calculation | I | I-PSEA-12 | Instructivo de Evaluación de Desempeño | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 9 | 9.2 | Zeta score calculation | I | I-PSEA-12 | Instructivo de Evaluación de Desempeño | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 9 | 9.3 | Proportion of allowed limit | I | I-PSEA-12 | Instructivo de Evaluación de Desempeño | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 9 | 9.4 | Combined scores | I | I-PSEA-12 | Instructivo de Evaluación de Desempeño | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 9 | 9.5 | Interpretation of scores | I | I-PSEA-12 | Instructivo de Evaluación de Desempeño | TBD | TBD | TBD | no_cumple | TBD | Por crear |

### Capítulo 10: Graphical Display

| Norma | Capítulo | Cláusula | Título Requisito | Tipo Documento | Código Documento | Título Documento | Versión | Estado Documento | Responsable | Estado Cumplimiento | Evidencia | Observaciones |
|-------|----------|----------|------------------|----------------|------------------|------------------|---------|------------------|-------------|---------------------|-----------|---------------|
| 13528:2022 | 10 | 10.1 | Introduction to graphical display | I | I-PSEA-14 | Instructivo de Visualización de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 10 | 10.2 | Histograms | I | I-PSEA-14 | Instructivo de Visualización de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 10 | 10.3 | Kernel density plots | I | I-PSEA-14 | Instructivo de Visualización de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 10 | 10.4 | Box plots | I | I-PSEA-14 | Instructivo de Visualización de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 10 | 10.5 | Youden plots | I | I-PSEA-14 | Instructivo de Visualización de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 10 | 10.6 | Other displays | I | I-PSEA-14 | Instructivo de Visualización de Datos | TBD | TBD | TBD | no_cumple | TBD | Por crear |

### Capítulo 11: Qualitative PT

| Norma | Capítulo | Cláusula | Título Requisito | Tipo Documento | Código Documento | Título Documento | Versión | Estado Documento | Responsable | Estado Cumplimiento | Evidencia | Observaciones |
|-------|----------|----------|------------------|----------------|------------------|------------------|---------|------------------|-------------|---------------------|-----------|---------------|
| 13528:2022 | 11 | 11.1 | Introduction to qualitative PT | I | I-PSEA-12 | Instructivo de Evaluación de Desempeño | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 11 | 11.2 | Binary data analysis | I | I-PSEA-12 | Instructivo de Evaluación de Desempeño | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 11 | 11.3 | Nominal data analysis | I | I-PSEA-12 | Instructivo de Evaluación de Desempeño | TBD | TBD | TBD | no_cumple | TBD | Por crear |
| 13528:2022 | 11 | 11.4 | Ordinal data analysis | I | I-PSEA-12 | Instructivo de Evaluación de Desempeño | TBD | TBD | TBD | no_cumple | TBD | Por crear |

---

## Resumen de Estado

| Norma | Total Requisitos | Cumple | Parcial | No Cumple | No Aplica | Porcentaje Cumple |
|-------|------------------|---------|---------|-----------|-----------|-------------------|
| 17025:2017 | TBD | TBD | TBD | TBD | TBD | TBD |
| 17043:2023 | TBD | TBD | TBD | TBD | TBD | TBD |
| 13528:2022 | TBD | TBD | TBD | TBD | TBD | TBD |
| **Total** | TBD | TBD | TBD | TBD | TBD | TBD |

---

## Documentos del SGC Mapeados

| Tipo | Código | Título | Versión | Estado | Normas Asociadas |
|------|--------|--------|---------|--------|------------------|
| DG | DG-PSEA-01 | Manual de Calidad | v1.0 | draft | 17025:2017, 17043:2023 |
| P | P-PSEA-01 | Protocolo General EA | v1.0 | in_review | 17025:2017 5.3, 17043:2023 7.2 |
| P | P-PSEA-02 | Procedimiento de Confidencialidad | TBD | TBD | 17025:2017 4.2, 17043:2023 4.2 |
| P | P-PSEA-03 | Procedimiento de Gestión de Competencia | TBD | TBD | 17025:2017 6.2, 17043:2023 6.2 |
| P | P-PSEA-04 | Procedimiento de Control de Acceso | TBD | TBD | 17025:2017 6.3, 17043:2023 6.3 |
| P | P-PSEA-05 | Procedimiento de Proveedores Externos | TBD | TBD | 17025:2017 6.4, 17043:2023 6.4 |
| P | P-PSEA-06 | Procedimiento de Revisión de Contratos | TBD | TBD | 17025:2017 7.1, 17043:2023 7.1 |
| P | P-PSEA-07 | Procedimiento de Selección de Métodos | TBD | TBD | 17025:2017 7.2 |
| P | P-PSEA-08 | Procedimiento de Trazabilidad | TBD | TBD | 17025:2017 7.5 |
| P | P-PSEA-09 | Procedimiento de Planificación Ronda EA | v1.0 | draft | 17043:2023 7.2 |
| P | P-PSEA-10 | Procedimiento de Manejo de Items PT | TBD | TBD | 17025:2017 7.7, 17043:2023 7.3 |
| P | P-PSEA-11 | Procedimiento de Reporte de Resultados | TBD | TBD | 17025:2017 7.9 |
| P | P-PSEA-12 | Procedimiento de Control Documental | TBD | TBD | 17025:2017 8.3, 17043:2023 8.3 |
| P | P-PSEA-13 | Procedimiento de Control de Registros | TBD | TBD | 17025:2017 8.4, 17043:2023 7.5 |
| P | P-PSEA-14 | Procedimiento de Gestión de Riesgos | TBD | TBD | 17025:2017 8.5, 17043:2023 8.5 |
| P | P-PSEA-15 | Procedimiento de Mejora Continua | TBD | TBD | 17025:2017 8.6, 17043:2023 8.6 |
| P | P-PSEA-16 | Procedimiento de No Conformidades | TBD | TBD | 17025:2017 8.7, 17043:2023 8.7 |
| P | P-PSEA-17 | Procedimiento de Auditorías Internas | TBD | TBD | 17025:2017 8.8, 17043:2023 8.8 |
| P | P-PSEA-18 | Procedimiento de Revisión por Dirección | TBD | TBD | 17025:2017 8.9, 17043:2023 8.9 |
| P | P-PSEA-19 | Procedimiento de Monitoreo de Imparcialidad | TBD | TBD | 17043:2023 4.1 |
| P | P-PSEA-20 | Procedimiento de Comunicación PT | TBD | TBD | 17043:2023 7.1 |
| P | P-PSEA-21 | Procedimiento de Divulgación de Valores | TBD | TBD | 17043:2023 7.2 |
| P | P-PSEA-22 | Procedimiento de Reportes PT | TBD | TBD | 17043:2023 7.4 |
| P | P-PSEA-23 | Procedimiento de Gestión de Datos | TBD | TBD | 17043:2023 7.5 |
| P | P-PSEA-24 | Procedimiento de Quejas | TBD | TBD | 17043:2023 8.10 |
| P | P-PSEA-25 | Procedimiento de Apelaciones | TBD | TBD | 17043:2023 8.11 |
| I | I-PSEA-01 | Instructivo de Caracterización | TBD | TBD | 17025:2017 6.1, 17043:2023 6.1 |
| I | I-PSEA-02 | Instructivo de Producción PT Items | TBD | TBD | 17025:2017 6.1, 17043:2023 7.3 |
| I | I-PSEA-03 | Instructivo de Control Ambiental | TBD | TBD | 17025:2017 6.3, 17043:2023 6.3 |
| I | I-PSEA-04 | Instructivo de Validación de Métodos | TBD | TBD | 17025:2017 7.3 |
| I | I-PSEA-05 | Instructivo de Estimación de Incertidumbre | TBD | TBD | 17025:2017 7.4 |
| I | I-PSEA-06 | Instructivo de Control de Calidad de Datos | TBD | TBD | 17025:2017 7.8 |
| I | I-PSEA-07 | Instructivo de Diseño Estadístico | TBD | TBD | 17043:2023 7.2, 13528:2022 cap 5 |
| I | I-PSEA-08 | Instructivo de Valor Asignado | TBD | TBD | 17043:2023 7.2, 13528:2022 cap 7 |
| I | I-PSEA-09 | Instructivo de Instrucciones a Participantes | TBD | TBD | 17043:2023 7.3, 13528:2022 cap 5 |
| I | I-PSEA-10 | Instructivo de Homogeneidad y Estabilidad | TBD | TBD | 17043:2023 7.3, 13528:2022 cap 6 |
| I | I-PSEA-11 | Instructivo de Análisis de Datos | TBD | TBD | 17043:2023 7.4, 13528:2022 cap 6 |
| I | I-PSEA-12 | Instructivo de Evaluación de Desempeño | TBD | TBD | 17043:2023 7.4, 13528:2022 cap 8-11 |
| I | I-PSEA-13 | Instructivo de Validación de Sistemas | TBD | TBD | 17043:2023 7.5, 13528:2022 4.1 |
| I | I-PSEA-14 | Instructivo de Visualización de Datos | TBD | TBD | 13528:2022 cap 10 |
| F | F-PSEA-01 | Formato de Registro de Competencia | TBD | TBD | 17025:2017 6.2, 17043:2023 6.2 |
| F | F-PSEA-02 | Formato de Registro Ambiental | TBD | TBD | 17025:2017 6.3, 17043:2023 6.3 |
| F | F-PSEA-03 | Formato de Evaluación de Condición | TBD | TBD | 17043:2023 7.3 |
| F | F-PSEA-04 | Formato de Confirmación de Entrega | TBD | TBD | 17043:2023 7.3 |

---

## Referencias

- `logs/plans/260208_1903_plan_ajuste-sistema-gestion-documental-17025-17043-13528.md` - Plan de ajuste del sistema de gestión documental
- `docs/referencias/iso 13528_2022.md` - Referencia normativa ISO 13528:2022
- `docs/referencias/iso 17043_2023.md` - Referencia normativa ISO/IEC 17043:2023
- `docs/referencias/bs-en-iso 17025_2017.pdf` - Referencia normativa ISO/IEC 17025:2017
- `pages/QMS.md` - MOC del Sistema de Gestión de Calidad
