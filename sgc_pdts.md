# Procedimientos y Formatos Pendientes del SGC PEA

Este documento detalla el estado de desarrollo de los procedimientos, formatos e instructivos del Sistema de Gestión de Calidad (SGC) del Proveedor de Ensayos de Aptitud (PEA) de **CALAIRE-EA**, de acuerdo con las decisiones arquitectónicas consolidadas a junio de 2026.

---

## 1. Documentos a Elaborar desde Cero (Estado: *Elaborar*)
Estos elementos representan necesidades operativas críticas del flujo digital (`calaire-app` $\rightarrow$ `pt_app`) y de gobernanza que aún no cuentan con un borrador desarrollado.

### 📋 Procedimientos (`P-PSEA`)
*   [P-PSEA-07](file:///home/w182/w421/calaire-ea/docs/documentacion_sgc/01_bloque_general/02_procedimientos/P-PSEA-07%20Procedimiento%20Informe%20Resultados_v0.docx) — **Procedimiento de generación/emisión del informe de resultados**: Gobierna la generación y emisión automática del informe de resultados final desde `pt_app`. Absorbe al antiguo *P-PSEA-22*.
*   [P-PSEA-10](file:///home/w182/w421/calaire-ea/docs/documentacion_sgc/02_prueba_piloto_rondas/00_planificacion/P-PSEA-10%20Procedimiento%20de%20Manejo%20de%20Items%20PT.md) — **Preparación y control del ítem de ensayo gaseoso**: Enfocado en la generación dinámica de concentraciones usando cilindros y calibradores dinámicos.
*   [P-PSEA-12](file:///home/w182/w421/calaire-ea/docs/documentacion_sgc/01_bloque_general/06_procedimientos_gestion/P-PSEA-12%20Control%20Documental%20del%20PEA.md) — **Matriz documental del PEA**: Estructura la matriz de control maestro de todos los códigos y estados del PEA.
*   [P-PSEA-13](file:///home/w182/w421/calaire-ea/docs/documentacion_sgc/01_bloque_general/06_procedimientos_gestion/P-PSEA-13%20Control%20de%20Registros%20del%20PEA.md) — **Matriz de registros y evidencias del PEA**: Registro operativo que lista las evidencias reales generadas por ronda o evento.
*   [P-PSEA-23](file:///home/w182/w421/calaire-ea/docs/documentacion_sgc/01_bloque_general/06_procedimientos_gestion/P-PSEA-23%20Gestión%20de%20Datos.md) — **Flujo técnico de datos digitales del PEA**: Mapeo completo del tratamiento de datos.

### 📊 Formatos y Registros (`F-PSEA`)
*   [F-PSEA-07](file:///home/w182/w421/calaire-ea/docs/documentacion_sgc/02_prueba_piloto_rondas/00_planificacion/F-PSEA-07%20Lista%20Maestra%20de%20Participantes.md) — **Ficha digital de ronda EA**: Insumo exportable desde `calaire-app` con la planificación de la ronda (incluye matriz/nota A-U de ISO/IEC 17043).
*   [F-PSEA-10](file:///home/w182/w421/calaire-ea/docs/documentacion_sgc/02_prueba_piloto_rondas/00_planificacion/F-PSEA-10%20Registro%20de%20Estabilidad.md) — **Registro de preprocesamiento de datos**: Evidencia de ejecución del script preprocesador (ref: `preprocesamiento_log.csv`).
*   **F-PSEA-13A** — **Datos preprocesados de homogeneidad** (Salida de `pt_app`).
*   **F-PSEA-13B** — **Datos preprocesados de estabilidad** (Salida de `pt_app`).
*   **F-PSEA-13C** — **Resultados de homogeneidad** (Salida de `pt_app`).
*   **F-PSEA-13D** — **Resultados de estabilidad** (Salida de `pt_app`).
*   [F-PSEA-14](file:///home/w182/w421/calaire-ea/docs/documentacion_sgc/02_prueba_piloto_rondas/00_planificacion/F-PSEA-14%20Hoja%20de%20Cálculo%20y%20Aprobación%20Estadística.md) — **Datos oficiales consolidados para evaluación de aptitud**: Dataset definitivo (`ronda_<n>_completa.csv`).

### 🛠️ Instructivos (`I-PSEA`)
*   **I-PSEA-17** — **Uso del preprocesador de datos de `pt_app`**: Guía operativa para ejecutar el preprocesamiento digital.
*   **I-PSEA-18** — **Uso del módulo de análisis PT de `pt_app`**: Guía operativa para ejecutar el análisis estadístico e informe.

---

## 2. Documentos en Estado "Placeholder" (Pendientes de Redacción Final)
Estos elementos existen actualmente como plantillas base o fichas resumen que delimitan su alcance y relaciones en el flujo digital, pero requieren redacción técnica detallada.

### 📋 Procedimientos de Gestión (`P-PSEA`)
*   [P-PSEA-16](file:///home/w182/w421/calaire-ea/docs/documentacion_sgc/01_bloque_general/06_procedimientos_gestion/P-PSEA-16%20No%20Conformidades%20y%20Acciones%20Correctivas%20del%20PEA.md) — **Trabajo no conforme, no conformidades y acciones correctivas (CAPA)**.
*   [P-PSEA-20](file:///home/w182/w421/calaire-ea/docs/documentacion_sgc/02_prueba_piloto_rondas/00_planificacion/P-PSEA-20%20Comunicación%20PT.md) — **Comunicaciones del PEA** (Canales de comunicación oficiales mediante aplicativo y correo).
*   [P-PSEA-21](file:///home/w182/w421/calaire-ea/docs/documentacion_sgc/01_bloque_general/06_procedimientos_gestion/P-PSEA-21%20Divulgación%20de%20Valores.md) — **Divulgación y control de valores sensibles** (Políticas para manejo de $x_{pt}$, $\sigma_{pt}$, etc.).
*   [P-PSEA-24](file:///home/w182/w421/calaire-ea/docs/documentacion_sgc/01_bloque_general/06_procedimientos_gestion/P-PSEA-24%20Quejas%20del%20PEA.md) — **Quejas del PEA** (Gestión de quejas en `calaire-app`).
*   [P-PSEA-25](file:///home/w182/w421/calaire-ea/docs/documentacion_sgc/01_bloque_general/06_procedimientos_gestion/P-PSEA-25%20Apelaciones%20del%20PEA.md) — **Apelaciones del PEA** (Gestión de apelaciones vía correo formal).
*   [P-PSEA-26](file:///home/w182/w421/calaire-ea/docs/documentacion_sgc/01_bloque_general/06_procedimientos_gestion/P-PSEA-26%20Confidencialidad.md) — **Confidencialidad operativa interna del PEA** (Control de códigos de participantes).
*   [P-PSEA-27](file:///home/w182/w421/calaire-ea/docs/documentacion_sgc/01_bloque_general/06_procedimientos_gestion/P-PSEA-27%20Competencia%20y%20Autorización%20del%20Personal%20del%20PEA.md) — **Competencia y autorización operativa del PEA** (Perfiles del personal técnico).
*   [P-PSEA-28](file:///home/w182/w421/calaire-ea/docs/documentacion_sgc/01_bloque_general/06_procedimientos_gestion/P-PSEA-28%20Proveedores%20Externos%20del%20PEA.md) — **Proveedores críticos del PEA** (Evaluación de CRM y calibraciones externas).

### 📊 Formatos de Soporte (Estado: *Revisar / Actualizar*)
*   [F-PSEA-16](file:///home/w182/w421/calaire-ea/docs/documentacion_sgc/02_prueba_piloto_rondas/00_planificacion/F-PSEA-16%20Registro%20de%20Quejas.md) — **Registro/caso de queja o no conformidad**.
*   [F-PSEA-17](file:///home/w182/w421/calaire-ea/docs/documentacion_sgc/02_prueba_piloto_rondas/00_planificacion/F-PSEA-17%20Registro%20de%20Apelaciones.md) — **Registro de apelaciones**.
*   [F-PSEA-21](file:///home/w182/w421/calaire-ea/docs/documentacion_sgc/02_prueba_piloto_rondas/00_planificacion/F-PSEA-21%20Matriz%20de%20Competencia%20y%20Autorización.md) — **Matriz de competencia y autorización**.
*   [F-PSEA-23](file:///home/w182/w421/calaire-ea/docs/documentacion_sgc/02_prueba_piloto_rondas/00_planificacion/F-PSEA-23%20Evaluación%20de%20Proveedores%20Externos.md) — **Evaluación de proveedores críticos**.

---

## 3. Documentos Excluidos o Retirados (No Pendientes)
*   **Procedimientos Retirados** (gestionados fuera del PEA por el SGC macro institucional):
    *   *P-PSEA-17* (Auditorías internas/externas)
    *   *P-PSEA-18* (Revisión por la dirección)
    *   *P-PSEA-19* (Monitoreo de Imparcialidad)
*   **Procedimientos Absorbidos**:
    *   *P-PSEA-22* (Reportes PT) - Su contenido operativo se consolida directamente en **P-PSEA-07**.
*   **Baja Prioridad / Diferidos**:
    *   *P-PSEA-14* (Riesgos generales del PEA) y *P-PSEA-15* (Mejora continua del PEA) - Quedan retenidos como marcadores en el mapa documental para posteriores etapas, pero no se intervendrán en el corto plazo.
