# Trazabilidad Normativa del SGC — Propuesta Documental CALAIRE-EA

**Fecha**: 2026-04-07  
**Versión**: 1.0  
**Propósito**: Explicar, justificar y relacionar cada documento propuesto del SGC del PEA frente a los requisitos de ISO/IEC 17043:2023 e ISO 13528:2022.

---

## 1. Alcance y Criterio de Diseño

Este documento demuestra que **cada documento propuesto en la arquitectura del SGC tiene una razón normativa explícita**. Se usa como guía de auditoría interna y como evidencia ante ONAC de que la propuesta documental cubre la totalidad de los requisitos aplicables.

**Criterios de inclusión de un documento:**
1. **Requisito expreso** ("shall/debe") en ISO 17043:2023 o ISO 13528:2022.
2. **Requisito implícito** derivado de un "shall" que exige evidencia documentada.
3. **Buena práctica necesaria** para operar el esquema de EA en el contexto específico (gases criterio, in situ, n bajo).

**Convención de lectura:**
- 🟢 = cubierto por el documento propuesto
- 🟡 = parcialmente cubierto, requiere mejora
- 🔴 = no cubierto aún, brecha

---

## 2. Trazabilidad ISO/IEC 17043:2023 → Documentos Propuestos

### Sección 4 — Requisitos generales

#### 4.1 Imparcialidad

| Subcláusula | Requisito ("shall") | Documento(s) | Justificación |
|---|---|---|---|
| 4.1.1 | Actividades de PT realizadas de forma imparcial y estructurada | DG-PSEA-01 (política), P-PSEA-19 | La política marco establece el compromiso; el procedimiento operacionaliza el monitoreo |
| 4.1.2 | La dirección se compromete con la imparcialidad | DG-PSEA-01 §política de imparcialidad | Declaración firmada de la alta dirección |
| 4.1.3 | No permitir presiones que comprometan la imparcialidad | P-PSEA-19, F-PSEA-22 | El procedimiento define los mecanismos de detección; la matriz registra los riesgos evaluados |
| 4.1.4 | Identificar riesgos a la imparcialidad de forma continua | P-PSEA-19, F-PSEA-22 | Incluye análisis de la dualidad laboratorio de referencia / PEA ("juez y parte") |
| 4.1.5 | Acciones para eliminar o minimizar riesgos identificados | P-PSEA-19, P-PSEA-16 (CAPA si aplica) | Declaraciones anuales del personal, segregación de roles, actas del Comité Técnico Asesor |

#### 4.2 Confidencialidad

| Subcláusula | Requisito | Documento(s) | Justificación |
|---|---|---|---|
| 4.2.1 | Proteger información confidencial de los participantes | P-PSEA-26, DG-PSEA-01 §política de confidencialidad | Política marco + procedimiento operativo con controles de acceso |
| 4.2.2 | Informar al participante sobre qué información será pública | P-PSEA-26, P-PSEA-20 | El procedimiento de comunicación incluye la cláusula de consentimiento |
| 4.2.3 | Codificación de identidad de participantes | P-PSEA-26 | Tabla de codificación cifrada, acceso restringido, RBAC en aplicativo Shiny/R |
| 4.2.4 | Notificar divulgación requerida por ley | P-PSEA-26 | Protocolo de notificación previa al participante |

---

### Sección 5 — Requisitos estructurales

| Subcláusula | Requisito | Documento(s) | Justificación |
|---|---|---|---|
| 5.1 | Entidad legal o parte definida de una entidad legal | DG-PSEA-01 §alcance | Identificación jurídica del PEA dentro de la entidad |
| 5.2 | Identificar la dirección con responsabilidad del SGC | DG-PSEA-01 §estructura organizacional | Organigrama con roles y autoridades del PEA, diferenciado del laboratorio 17025 |
| 5.3 | Alcance de las actividades de PT | DG-PSEA-01 §alcance | Gases criterio: CO, NOx, SO₂, O₃; esquema in situ; simultáneo |
| 5.4 | Estructura que permita cumplir requisitos normativos | DG-PSEA-01 §mapa de procesos | Mapa de procesos del PEA con interrelaciones entre niveles documentales |
| 5.5 | Definir responsabilidades y autoridades | DG-PSEA-01, F-PSEA-21 | La matriz de competencia y autorización asigna roles formales |

---

### Sección 6 — Requisitos de recursos

#### 6.1 Generalidades

| Subcláusula | Requisito | Documento(s) | Justificación |
|---|---|---|---|
| 6.1.1 | Disponibilidad de recursos (personal, equipos, infraestructura) | DG-PSEA-01, P-PSEA-09 | El manual declara los recursos; cada plan de ronda especifica los recursos asignados |
| 6.1.2 | Caracterización de ítems PT | I-PSEA-01 | Instructivo técnico para la caracterización de materiales de gas |

#### 6.2 Personal

| Subcláusula | Requisito | Documento(s) | Justificación |
|---|---|---|---|
| 6.2.1 | Competencia del personal que afecta los resultados | P-PSEA-27, F-PSEA-21 | Procedimiento de competencia + matriz de autorización documentan perfiles, formación y autorización formal |
| 6.2.2 | Acciones para asegurar competencia (formación, supervisión) | P-PSEA-27 | Define el ciclo: detección de necesidad → formación → evaluación → autorización |
| 6.2.3 | Registros de competencia | F-PSEA-21 | Registros de formación, evaluación y autorización para cada rol del PEA |

#### 6.3 Instalaciones y condiciones ambientales

| Subcláusula | Requisito | Documento(s) | Justificación |
|---|---|---|---|
| 6.3.1 | Instalaciones adecuadas para actividades PT | I-PSEA-03 | Instructivo de control ambiental para generación/almacenamiento de gases |
| 6.3.2 | Documentar requisitos de condiciones ambientales | I-PSEA-03, F-PSEA-03 | Condiciones de temperatura, humedad, presión para cilindros y dilución dinámica |

#### 6.4 Proveedores externos

| Subcláusula | Requisito | Documento(s) | Justificación |
|---|---|---|---|
| 6.4.1 | Evaluar y seleccionar proveedores externos | P-PSEA-28, F-PSEA-23 | Procedimiento de evaluación + formato de calificación para CRM, transporte, subcontratados |
| 6.4.2 | Asegurar que proveedores cumplen requisitos | P-PSEA-28 | Criterios de aceptación, seguimiento periódico, reevaluación |
| 6.4.3 | Comunicar requisitos al proveedor | P-PSEA-28 | Especificaciones técnicas de CRM, condiciones de transporte |

---

### Sección 7 — Requisitos del proceso

#### 7.1 Revisión de solicitudes y contratos

| Subcláusula | Requisito | Documento(s) | Justificación |
|---|---|---|---|
| 7.1.1 | Procedimiento para revisión de solicitudes | P-PSEA-20 | Comunicación PT cubre la revisión de solicitudes, capacidad y acuerdos de participación |
| 7.1.2 | Informar al participante sobre el esquema | P-PSEA-20, I-PSEA-09 | Instrucciones pre-ronda, comunicación de cambios, notificaciones |

#### 7.2 Planificación y diseño del esquema

| Subcláusula | Requisito | Documento(s) | Justificación |
|---|---|---|---|
| 7.2.1.1–7.2.1.2 | Planificación documentada antes de operar | P-PSEA-09, F-PSEA-06 | Procedimiento de planificación + formato de plan de ronda |
| 7.2.1.3 a)–u) | 21 elementos obligatorios del plan del esquema | P-PSEA-09 (expandido) | **Cada literal (a–u) debe ser direccionable** en P-PSEA-09. Expansión priorizada en Oleada 1 |
| 7.2.2.1–7.2.2.3 | Diseño estadístico del esquema | P-PSEA-06, I-PSEA-07 | Procedimiento troncal + instructivo detallado de diseño estadístico según ISO 13528 §4–5 |
| 7.2.3.1–7.2.3.4 | Valor asignado, métodos, incertidumbre | P-PSEA-06, I-PSEA-08 | Procedimiento define la jerarquía; instructivo operacionaliza el cálculo de x_pt y u(x_pt) |
| 7.2.3.5 | Política de divulgación del valor asignado | P-PSEA-21 | Procedimiento específico: cuándo, cómo, a quién se comunica el valor asignado |

#### 7.3 Operación del esquema

| Subcláusula | Requisito | Documento(s) | Justificación |
|---|---|---|---|
| 7.3.1.1–7.3.1.2 | Producción/selección de ítems PT | I-PSEA-02, P-PSEA-02 a 05 | Instructivo de producción + procedimientos por analito definen la preparación de cilindros/atmósferas |
| 7.3.2.1–7.3.2.4 | Homogeneidad y estabilidad | I-PSEA-10, F-PSEA-09, F-PSEA-10 | Instructivo adaptado a atmósferas generadas + formatos de registro |
| 7.3.3.1–7.3.3.3 | Distribución, empaque, transporte | P-PSEA-10, I-PSEA-01 | Procedimiento de manejo de ítems + instructivo de caracterización (existente) |
| 7.3.4.1–7.3.4.5 | Control de recepción del ítem | P-PSEA-10, F-PSEA-11, F-PSEA-05 | Registro de envío/recepción + confirmación de participación |
| 7.3.5.1–7.3.5.2 | Instrucciones a participantes | I-PSEA-09, P-PSEA-20 | Instructivo de instrucciones + comunicación PT |

#### 7.4 Análisis de datos y evaluación de desempeño

| Subcláusula | Requisito | Documento(s) | Justificación |
|---|---|---|---|
| 7.4.1.1–7.4.1.3 | Análisis de datos (revisión inicial, outliers) | P-PSEA-06, I-PSEA-11, F-PSEA-13 | Procedimiento + instructivo de análisis + hoja de revisión de datos |
| 7.4.2.1–7.4.2.3 | Evaluación de desempeño (scores) | P-PSEA-06, I-PSEA-12, F-PSEA-14 | z, z', ζ, E_n calculados según ISO 13528; hoja de cálculo y aprobación estadística |
| 7.4.3.1–7.4.3.7 | Informes de PT (contenido mínimo) | P-PSEA-22, P-PSEA-07, F-PSEA-04 | Procedimiento de reportes PT (17043) + informe de resultados + formato |
| 7.4.3.8 | Informes enmendados | P-PSEA-22 | Incluye protocolo de enmienda y reemisión |

#### 7.5 Registros y datos

| Subcláusula | Requisito | Documento(s) | Justificación |
|---|---|---|---|
| 7.5.1.1–7.5.1.3 | Registros técnicos (retención, trazabilidad) | P-PSEA-13 | Control de registros del PEA: política de retención ≥ 5 años, respaldo, recuperación |
| 7.5.2.1–7.5.2.4 | Validación de software y sistemas | P-PSEA-23, I-PSEA-13, F-PSEA-20 | Gestión de datos + instructivo de validación + protocolo de validación del aplicativo R/Shiny |
| 7.5.3 | Colusión y falsificación | P-PSEA-08 | Procedimiento para detectar y manejar colusión y falsificación de resultados |

---

### Sección 8 — Requisitos del sistema de gestión

| Subcláusula | Requisito | Documento(s) | Justificación |
|---|---|---|---|
| 8.1 | Opciones: A (propio SGC) o B (ISO 9001) | DG-PSEA-01 | Se adopta Opción A: SGC propio del PEA, independiente del SGC 17025 |
| 8.2 | Documentación del SGC (política, objetivos, procedimientos) | DG-PSEA-01 + todos los P-PSEA | El manual integra políticas y referencia cruzada a todos los documentos |
| 8.3 | Control de documentos | P-PSEA-12 | Aprobación, distribución, cambios, obsolescencia de documentos del PEA |
| 8.4 | Control de registros | P-PSEA-13 | Identificación, almacenamiento, protección, retención, disposición |
| 8.5 | Riesgos y oportunidades | P-PSEA-14, F-PSEA-22 | Identificación de riesgos, evaluación, plan de tratamiento. La matriz de riesgos de imparcialidad es un subconjunto crítico |
| 8.6 | Mejora | P-PSEA-15 | Mejora continua usando resultados de auditorías, CAPA, revisión por dirección, tendencias |
| 8.7 | No conformidades y acciones correctivas | P-PSEA-16, F-PSEA-15 | Ciclo: detección → análisis causa raíz → corrección → acción correctiva → verificación de eficacia |
| 8.8 | Auditorías internas | P-PSEA-17, F-PSEA-19 | Programa anual, competencia de auditores, informe, seguimiento de hallazgos |
| 8.9 | Revisión por la dirección | P-PSEA-18, F-PSEA-18 | Entradas mínimas (resultados de auditorías, CAPA, tendencias, quejas), periodicidad, acta |
| 8.10 | Quejas | P-PSEA-24, F-PSEA-16 | Recepción, evaluación, resolución, comunicación, plazo (≤30 días) |
| 8.11 | Apelaciones | P-PSEA-25, F-PSEA-17 | Separado de quejas (cambio 2023). Proceso formal con resolución imparcial |

---

## 3. Trazabilidad ISO 13528:2022 → Documentos Propuestos

### Capítulo 4 — Principios generales

| Subcláusula | Requisito | Documento(s) | Justificación |
|---|---|---|---|
| 4.1 | Responsabilidad del coordinador: métodos estadísticos válidos | P-PSEA-06, I-PSEA-07 | El coordinador del esquema es responsable de que los métodos se apliquen correctamente |
| 4.2 | Software adecuadamente validado | I-PSEA-13, F-PSEA-20 | **Requisito expreso.** El protocolo de validación documenta las pruebas funcionales y estadísticas del aplicativo R/Shiny |
| 4.3 | Descripción de métodos estadísticos a participantes | P-PSEA-22, I-PSEA-09 | El informe de PT debe incluir descripción de los métodos usados |

### Capítulo 5 — Diseño estadístico

| Subcláusula | Requisito | Documento(s) | Justificación |
|---|---|---|---|
| 5.1 | Diseño apropiado al tipo de datos | P-PSEA-06, I-PSEA-07 | Define si los datos son cuantitativos continuos (caso de gases) y su distribución esperada |
| 5.2 | Consideración del número de participantes | P-PSEA-06 | Diseño explícito para n variable (2–15+): Algoritmo B si n < 15; valor asignado siempre independiente |
| 5.3 | Selección de estadísticos de desempeño | P-PSEA-06, I-PSEA-12 | z (preferido), z' (si u alta), ζ (complementario), E_n (opcional) |
| 5.4 | Criterio para σ_pt | P-PSEA-06 | σ_pt = δ_E / 3 donde δ_E = max(a% × x_pt, b% × span). Nunca derivado de la dispersión de la ronda |
| 5.5 | Validación del software de cálculo | I-PSEA-13, F-PSEA-20 | Cross-validación de algoritmos con datasets de referencia en R y Python |

### Capítulo 6 — Revisión inicial de datos

| Subcláusula | Requisito | Documento(s) | Justificación |
|---|---|---|---|
| 6.1 | Revisión de datos antes del análisis estadístico | I-PSEA-11, F-PSEA-13 | Hoja de revisión: verificación de unidades, formato, plausibilidad, cifras significativas |
| 6.2 | Detección y tratamiento de valores atípicos | P-PSEA-06, I-PSEA-11 | Algoritmo A reduce influencia; Grubbs marca pero no excluye automáticamente; exclusión solo con evidencia técnica |
| 6.3 | Métodos de outlier | I-PSEA-11 | Grubbs, desviación del consenso robusto, revisión técnica |

### Capítulo 7 — Valor asignado

| Subcláusula | Requisito | Documento(s) | Justificación |
|---|---|---|---|
| 7.1 | Métodos para determinar el valor asignado | P-PSEA-06, I-PSEA-08 | Jerarquía: (1) cálculo metrológico CRM + dilución; (2) lab. referencia; (3) consenso robusto (solo verificación) |
| 7.2 | Valor de consenso (Algoritmos A, B, C) | I-PSEA-08, I-PSEA-07 | Algoritmo A/B implementados en R/Shiny. El Algoritmo B es preferido con n < 15 |
| 7.3 | Valor asignado formulado/certificado | I-PSEA-08 | Para esquema in situ: x_pt por CRM + dilución dinámica |
| 7.4 | Incertidumbre del valor asignado | I-PSEA-08, P-PSEA-06 | u(x_pt) = √(u²_char + u²_hom + u²_stab); condición: u(x_pt) ≤ 0,3 × σ_pt |

### Capítulo 8 — Evaluación de desempeño mediante z-scores

| Subcláusula | Requisito | Documento(s) | Justificación |
|---|---|---|---|
| 8.1–8.2 | Cálculo de z-score, interpretación | P-PSEA-06, I-PSEA-12 | z = (x_i − x_pt) / σ_pt. Señales: \|z\| ≤ 2 ✓, 2 < \|z\| < 3 ⚠️, \|z\| ≥ 3 ✗ |
| 8.3 | Criterio para σ_pt (externo) | P-PSEA-06 | Definido por aptitud para el uso, no por dispersión de la ronda |
| 8.4 | z'-score cuando u(x_pt) no es despreciable | I-PSEA-12 | σ'_pt = √(σ²_pt + u²_ref) |

### Capítulo 9 — Evaluación mediante ζ y E_n

| Subcláusula | Requisito | Documento(s) | Justificación |
|---|---|---|---|
| 9.1 | ζ-score (considera incertidumbre del participante) | I-PSEA-12, P-PSEA-06 | ζ = (x_i − x_pt) / √(u²_i + u²_ref). Complementario al z |
| 9.2 | E_n (número de error normalizado) | I-PSEA-12 | E_n = (x_i − x_ref) / √(U²_i + U²_ref). Opcional para calibración |

### Capítulo 10 — Presentación gráfica

| Subcláusula | Requisito | Documento(s) | Justificación |
|---|---|---|---|
| 10.1–10.3 | Gráficos de resultados, z-scores, histogramas | I-PSEA-14, P-PSEA-22 | Instructivo de visualización define los gráficos estándar; el informe PT los incluye |
| 10.4 | Diagrama de Mandel | I-PSEA-14 | Para análisis de consistencia inter/intra-laboratorio |

### Anexo B — Homogeneidad y estabilidad

| Subcláusula | Requisito | Documento(s) | Justificación |
|---|---|---|---|
| B.1–B.3 | Estudios de homogeneidad y estabilidad | I-PSEA-10, F-PSEA-09, F-PSEA-10 | Adaptado a atmósferas generadas in situ: ≥ 10 atmósferas, réplicas ≥ 2, criterio s_hom ≤ 0,3 × σ_pt |

### Anexo C — Algoritmos robustos

| Subcláusula | Requisito | Documento(s) | Justificación |
|---|---|---|---|
| C.1 | Algoritmo A (media/s robustas Huber-tipo) | P-PSEA-06, I-PSEA-07, Aplicativo R | Implementado y parcialmente validado. Expediente completo en I-PSEA-13 |
| C.2 | Algoritmo B (mediana/NIQR) | P-PSEA-06, I-PSEA-07, Aplicativo R | Preferido con n < 15 |
| C.3 | Algoritmo C (basado en rangos) | I-PSEA-07 | Disponible como fallback |

---

## 4. Cobertura Inversa: Documentos → Cláusulas

Esta tabla permite verificar que **ningún documento existe sin justificación normativa**.

| Código | Título | ISO 17043:2023 | ISO 13528:2022 | Justificación |
|---|---|---|---|---|
| **DG-PSEA-01** | Manual del SGC para EA | 4.1, 4.2, 5, 8.1, 8.2 | — | Marco político, estructural y de gobernanza del PEA |
| **P-PSEA-01** | Protocolo General EA | 7.2.1 (marco) | — | Marco operativo general para participantes |
| **P-PSEA-02** | Procedimiento NO-NO₂ | 7.3.1 | — | Especificaciones técnicas del analito: preparación, niveles, método |
| **P-PSEA-03** | Procedimiento CO | 7.3.1 | — | Ídem para CO |
| **P-PSEA-04** | Procedimiento O₃ | 7.3.1 | — | Ídem para O₃. Incluye consideraciones de estabilidad reactiva |
| **P-PSEA-05** | Procedimiento SO₂ | 7.3.1 | — | Ídem para SO₂ |
| **P-PSEA-06** | Diseño Estadístico | 7.2.2, 7.2.3, 7.4.1, 7.4.2 | 4, 5, 6, 7, 8, 9 | **Troncal.** Cubre diseño, valor asignado, σ_pt, scoring, outliers |
| **P-PSEA-07** | Informe de Resultados | 7.4.3 | 10 | Contenido, plazos, formato, enmiendas |
| **P-PSEA-08** | Colusión y Falsificación | 7.5.3 | — | Detección y protocolo de actuación ante resultados fraudulentos |
| **P-PSEA-09** | Planificación de Ronda | 7.2.1.3 a)–u) | 5.1–5.2 | 21 elementos obligatorios del plan del esquema |
| **P-PSEA-10** | Manejo de Items PT | 7.3.3, 7.3.4 | — | Producción, almacenamiento, despacho, recepción de cilindros/atmósferas |
| **P-PSEA-11** | Reporte de Resultados | 7.4.3 (17025: 7.9) | — | Complementa P-PSEA-22 para reportes bajo 17025 |
| **P-PSEA-12** | Control Documental | 8.3 | — | Gobernanza: aprobación, distribución, cambios de documentos del PEA |
| **P-PSEA-13** | Control de Registros | 7.5.1, 8.4 | — | Retención, respaldo, trazabilidad de registros técnicos |
| **P-PSEA-14** | Gestión de Riesgos | 8.5 | — | Pensamiento basado en riesgos; sustituye acciones preventivas |
| **P-PSEA-15** | Mejora Continua | 8.6 | — | Ciclo de mejora usando auditorías, tendencias, CAPA |
| **P-PSEA-16** | No Conformidades/CAPA | 8.7 | — | Detección → causa raíz → corrección → acción correctiva → verificación |
| **P-PSEA-17** | Auditorías Internas | 8.8 | — | Programa, competencia de auditores, informe, seguimiento |
| **P-PSEA-18** | Revisión por Dirección | 8.9 | — | Entradas mínimas, periodicidad, acta con decisiones |
| **P-PSEA-19** | Monitoreo Imparcialidad | 4.1.4, 4.1.5 | — | Exclusivo EA: segregación laboratorio/PEA, declaraciones, Comité Técnico |
| **P-PSEA-20** | Comunicación PT | 7.1, 7.3.5 | — | Revisión de solicitudes, acuerdos, instrucciones, notificación de cambios |
| **P-PSEA-21** | Divulgación de Valores | 7.2.3.5 | — | Política de cuándo/cómo se comparte el valor asignado |
| **P-PSEA-22** | Reportes PT | 7.4.3.1–7.4.3.7 | 10 | Contenido mínimo del informe PT per §7.4.3 |
| **P-PSEA-23** | Gestión de Datos | 7.5.2 | 4.2 | Control de acceso, sistemas externos, respaldo, seguridad |
| **P-PSEA-24** | Quejas | 8.10 | — | Proceso formal: recepción → evaluación → resolución → comunicación |
| **P-PSEA-25** | Apelaciones | 8.11 | — | Separado de quejas (cambio 2023); resolución imparcial |
| **P-PSEA-26** | Confidencialidad | 4.2 | — | Codificación, NDA, RBAC, notificación de divulgación |
| **P-PSEA-27** | Competencia/Autorización | 6.2 | — | Perfiles, formación, evaluación, autorización formal |
| **P-PSEA-28** | Proveedores Externos | 6.4 | — | Evaluación, seguimiento, reevaluación de proveedores de CRM/transporte |
| **I-PSEA-01** | Caracterización | 6.1.2 | — | Caracterización técnica de ítems PT |
| **I-PSEA-02** | Producción PT Items | 7.3.1 | — | Especificaciones de producción de cilindros/atmósferas |
| **I-PSEA-03** | Control Ambiental | 6.3 | — | Condiciones de generación y almacenamiento de gases |
| **I-PSEA-04** | Validación de Métodos | 7.3 (vía 17025) | — | Validación de métodos de ensayo del esquema |
| **I-PSEA-05** | Estimación de Incertidumbre | 7.4 (vía 17025) | 7.3, 7.4 | Incertidumbre del valor asignado y de las mediciones |
| **I-PSEA-06** | Control Calidad de Datos | 7.8 (vía 17025) | 6 | QC de datos: blancos, duplicados, tendencias |
| **I-PSEA-07** | Diseño Estadístico | 7.2.2 | 4, 5 | Operacionaliza los requisitos de diseño de ISO 13528 §4–5 |
| **I-PSEA-08** | Valor Asignado | 7.2.3 | 7 | Cálculo detallado de x_pt y u(x_pt) |
| **I-PSEA-09** | Instrucciones a Participantes | 7.3.5 | 5.3 | Instrucciones pre-ronda: qué reportar, formato, plazos |
| **I-PSEA-10** | Homogeneidad y Estabilidad | 7.3.2 | Anexo B | Adaptado a atmósferas generadas in situ |
| **I-PSEA-11** | Análisis de Datos | 7.4.1 | 6 | Revisión inicial, outliers, limpieza de datos |
| **I-PSEA-12** | Evaluación de Desempeño | 7.4.2 | 8, 9 | Cálculo de z, z', ζ, E_n; interpretación; clasificación |
| **I-PSEA-13** | Validación de Software | 7.5.2 | 4.2, 5.5 | Validación del aplicativo R/Shiny con datasets de referencia |
| **I-PSEA-14** | Visualización de Datos | — | 10 | Especificaciones de gráficos: tornado, histograma, Mandel |
| **F-PSEA-01** | Calendario Tipo | 7.2.1.3 a) | — | Cronograma general del programa anual |
| **F-PSEA-02** | Cronograma Detallado | 7.2.1.3 b) | — | Cronograma operativo de cada ronda |
| **F-PSEA-03** | Registro Planificación | 7.2.1 | — | Evidencia de la planificación pre-ronda |
| **F-PSEA-04** | Formato Informe | 7.4.3 | 10 | Plantilla del informe de resultados PT |
| **F-PSEA-05** | Confirmación Participación | 7.1, 7.3.4 | — | Registro de aceptación/acuerdo del participante |
| **F-PSEA-06** | Plan de Ronda | 7.2.1.3 | 5 | Registro del plan aprobado de cada ronda |
| **F-PSEA-07** | Lista Participantes | 7.2.1.3 d) | — | Registro maestro de participantes codificados |
| **F-PSEA-08** | Registro Preparación | 7.3.1 | — | Trazabilidad de la preparación del ítem |
| **F-PSEA-09** | Registro Homogeneidad | 7.3.2 | Anexo B | Evidencia del estudio de homogeneidad |
| **F-PSEA-10** | Registro Estabilidad | 7.3.2 | Anexo B | Evidencia del estudio de estabilidad |
| **F-PSEA-11** | Registro Envío/Recepción | 7.3.3, 7.3.4 | — | Trazabilidad del despacho y recepción |
| **F-PSEA-12** | Reporte Participante | 7.3.5, 7.4.1 | 5.3 | Formato para que el participante reporte sus resultados |
| **F-PSEA-13** | Hoja Revisión Datos | 7.4.1 | 6 | Evidencia de la revisión pre-análisis |
| **F-PSEA-14** | Hoja Cálculo Estadística | 7.4.2 | 7, 8, 9 | Registro de cálculos: x_pt, σ_pt, z, decisión estadística |
| **F-PSEA-15** | Registro NC/CAPA | 8.7 | — | Evidencia del ciclo de no conformidad |
| **F-PSEA-16** | Registro Quejas | 8.10 | — | Evidencia del proceso de quejas |
| **F-PSEA-17** | Registro Apelaciones | 8.11 | — | Evidencia del proceso de apelaciones |
| **F-PSEA-18** | Acta Revisión Dirección | 8.9 | — | Evidencia de la revisión por dirección |
| **F-PSEA-19** | Lista Verificación Auditoría | 8.8 | — | Herramienta para auditoría interna |
| **F-PSEA-20** | Protocolo Validación Software | 7.5.2 | 4.2, 5.5 | Evidencia de validación del aplicativo R/Shiny |
| **F-PSEA-21** | Matriz Competencia | 6.2 | — | Registro de perfiles, formación, autorización |
| **F-PSEA-22** | Matriz Riesgos Imparcialidad | 4.1, 8.5 | — | Evaluación de amenazas a la imparcialidad |
| **F-PSEA-23** | Evaluación Proveedores | 6.4 | — | Registro de evaluación y seguimiento de proveedores |

---

## 5. Cláusulas sin Documento Dedicado (Cubiertas Transversalmente)

Las siguientes cláusulas **no requieren un documento separado** porque se cumplen transversalmente:

| Cláusula | Requisito | Cómo se cubre | Dónde |
|---|---|---|---|
| 4.1.2 | Compromiso de la dirección con la imparcialidad | Declaración en la política de imparcialidad | DG-PSEA-01 |
| 5.1 | Entidad legal | Identificación jurídica | DG-PSEA-01 §1 |
| 6.1.1 | Disponibilidad general de recursos | Asignación por ronda | P-PSEA-09, F-PSEA-06 |
| 8.1 | Opción A o B del SGC | Declaración expresa | DG-PSEA-01 (Opción A) |
| 8.2 | Documentación general del SGC | Referencia cruzada | DG-PSEA-01 + árbol documental |

---

## 6. Conclusión

La propuesta documental del SGC para el PEA CALAIRE-EA:

1. **Cubre el 100% de los "shall" de ISO/IEC 17043:2023** (Secciones 4–8) con al menos un documento asignado.
2. **Cubre el 100% de los requisitos estadísticos de ISO 13528:2022** (Capítulos 4–10, Anexos B y C) mediante P-PSEA-06 como procedimiento troncal, I-PSEA-07 a I-PSEA-14 como instructivos detallados, y F-PSEA-09/10/13/14/20 como evidencia objetiva.
3. **No contiene documentos sin justificación normativa.** Cada P-PSEA, I-PSEA y F-PSEA tiene al menos una cláusula asociada.
4. **Separa los temas que requieren procedimiento propio del PEA** (imparcialidad, confidencialidad, competencia, proveedores) de los que pueden generalizarse con el SGC 17025 (DG-PSEA-01 + Nivel 2).
5. **Prioriza lo técnico-operativo** (Nivel 3 + 4) para habilitar la ronda piloto antes de completar la gobernanza.
