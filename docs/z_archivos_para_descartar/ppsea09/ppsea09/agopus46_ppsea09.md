# P-PSEA-09 — Planificación y Preparación de Rondas de Ensayo de Aptitud para Gases Contaminantes Criterio

**Código:** P-PSEA-09  
**Versión:** 3.0  
**Fecha de emisión:** 2026-03-22  
**Referencia normativa:** ISO/IEC 17043:2023, ISO 13528:2022  
**Procedimientos relacionados:** P-PSEA-02 a P-PSEA-08  

---

## 1. Información general del procedimiento

### 1.1 Objetivo

Establecer las directrices, responsabilidades y actividades para planificar y preparar las rondas de ensayos de aptitud (EA) de gases contaminantes criterio —dióxido de azufre (SO₂), óxidos de nitrógeno (NO/NO₂), monóxido de carbono (CO) y ozono (O₃)— organizadas por el Laboratorio CALAIRE, garantizando el cumplimiento de los requisitos establecidos en ISO/IEC 17043:2023 e ISO 13528:2022, y asegurando la validez, imparcialidad y trazabilidad de los resultados.

### 1.2 Alcance

Este procedimiento aplica a todas las etapas de planificación previas al inicio de cada ronda EA: definición de objetivos, diseño del esquema, selección y gestión de participantes, control de calidad de ítems de ensayo, gestión de riesgos, comunicación operativa y criterios de evaluación. Abarca las actividades realizadas en las instalaciones del Laboratorio CALAIRE y las interacciones con participantes y proveedores externos.

### 1.3 Definiciones

| Término | Definición |
|---|---|
| Ensayo de aptitud (EA) | Evaluación del desempeño de un laboratorio mediante comparaciones interlaboratorios, conforme a ISO/IEC 17043:2023. |
| Ítem de ensayo | Atmósfera de gas contaminante criterio generada dinámicamente a partir de mezcla gaseosa certificada o referencia fotométrica. |
| Valor asignado (x_pt) | Valor atribuido al mensurando del EA, determinado conforme a P-PSEA-06. |
| σ_pt | Desviación estándar para la evaluación de la aptitud; criterio de dispersión contra el cual se juzga el desempeño. |
| u(x_pt) | Incertidumbre estándar del valor asignado. |
| u(x_pt,def) | Incertidumbre estándar definitiva del valor asignado, integrada con contribuciones por homogeneidad y estabilidad. |
| Participante | Laboratorio que reporta resultados en el EA conforme a los criterios establecidos. |

### 1.4 Documentos de referencia

- ISO/IEC 17043:2023 — Requisitos generales para proveedores de EA.
- ISO 13528:2022 — Métodos estadísticos para EA por comparación interlaboratorio.
- ISO/IEC 17025:2017 — Requisitos generales para laboratorios de ensayo y calibración.
- ISO 6142-1:2015 — Preparación gravimétrica de mezclas gaseosas.
- ISO 6145-7 — Preparación de mezclas gaseosas por dilución dinámica.
- ISO 17034:2016 — Requisitos para productores de materiales de referencia.
- P-PSEA-06 — Diseño estadístico para EA (métodos para x_pt, σ_pt, incertidumbre y puntajes).
- P-PSEA-07 — Elaboración de informe de resultados.
- P-PSEA-08 — Gestión de colusión, falsificación y desviaciones de integridad.
- P-PSEA-02 a P-PSEA-05 — Procedimientos por analito (NO-NO₂, CO, O₃, SO₂).
- F-PSEA-01 — Calendario tipo de rondas EA.
- DG-PSEA-01 — Protocolo detallado de participación (comunicación a participantes).
- I-PSEA-01 — Instructivo de embalaje y transporte.

---

## 2. Roles y responsabilidades

### 2.1 Roles definidos

| Rol | Responsabilidad |
|---|---|
| Coordinador EA | Aprueba el diseño del esquema, verifica disponibilidad de recursos y autoriza la emisión de resultados. Responsable de la gestión integral de la ronda. |
| Estadístico / Experto técnico | Diseña el plan estadístico conforme a P-PSEA-06, valida criterios de desempeño y revisa coherencia técnica. Autorizado para evaluar datos y determinar valores asignados, incertidumbres y σ_pt. |
| Ingeniero operativo | Lidera la preparación de ítems, control de condiciones ambientales y montaje de la infraestructura de generación. Responsable de la producción, caracterización, homogeneidad y estabilidad. |
| Experto técnico en calidad del aire | Define los rangos de concentración, verifica trazabilidad metrológica y valida la aplicabilidad de los métodos de referencia. Autorizado para evaluar la adecuación del diseño estadístico a los objetivos técnicos. |
| Profesional de calidad | Garantiza el cumplimiento del SGC, la imparcialidad, la confidencialidad y la trazabilidad documental. Responsable del control documental y de registros. |
| Profesional de proyectos / Comunicaciones | Gestiona la comunicación con participantes, la convocatoria, el envío de formatos y el seguimiento. Responsable de la gestión de quejas y apelaciones. |

### 2.2 Autorización formal del personal (ISO/IEC 17043:2023, 6.2.6)

El Laboratorio CALAIRE mantiene autorización formal y evidencia de competencia documentada para las siguientes actividades críticas:

1. Planificación de esquemas de EA.
2. Evaluación de homogeneidad, estabilidad, valor asignado e incertidumbre.
3. Evaluación del desempeño de participantes.
4. Emisión de opiniones e interpretaciones técnicas.
5. Revisión y autorización de informes EA.

Las autorizaciones se registran en los perfiles de cargo individuales y se revisan en cada ciclo de auditoría interna del SGC. Solo el personal autorizado puede ejecutar las actividades correspondientes, y la evidencia de competencia se mantiene actualizada conforme al procedimiento de gestión de personal del laboratorio.

### 2.3 Actividades no subcontratables (ISO/IEC 17043:2023, 6.4.1)

Las siguientes actividades son de ejecución interna exclusiva y no pueden externalizarse:

- Diseño y planificación del esquema EA.
- Evaluación del desempeño de participantes.
- Selección final del valor asignado y criterios de evaluación.
- Revisión y autorización de informes EA.

Las actividades subcontratables (calibraciones especializadas, logística de transporte, suministro de mezclas gaseosas por proveedores evaluados) se controlan mediante evaluación documentada del proveedor conforme al procedimiento de compras y control de proveedores del SGC. El proveedor del EA permanece responsable ante los participantes por los productos y servicios suministrados externamente.

---

## 3. Información específica del procedimiento (ISO/IEC 17043:2023, 7.2.1.3)

### 3.1 a) Personal involucrado en el diseño y la operación

Se identifican y documentan todos los roles involucrados en cada ronda. Cada persona cuenta con autorización formal vigente conforme a la sección 2.2 de este procedimiento. El expediente de la ronda registra la identificación de responsables, sus firmas de aceptación y la evidencia de competencia.

### 3.2 b) Actividades de proveedores externos

Las actividades ejecutadas por proveedores externos se documentan con los datos de contacto del proveedor, la descripción del servicio subcontratado, la evidencia de evaluación de competencia y los acuerdos de confidencialidad vigentes. El coordinador EA revisa y aprueba la idoneidad de cada proveedor antes de la contratación. Los servicios subcontratados no incluyen ninguna de las actividades listadas en 2.3.

Se requiere que todo proveedor externo que realice mediciones relevantes para la caracterización del ítem cumpla con los requisitos de ISO/IEC 17025 y cuente con trazabilidad metrológica demostrable. Toda subcontratación se documenta con contrato o registro técnico, en cumplimiento del numeral 6.4.1 de ISO/IEC 17043:2023.

### 3.3 c) Criterios de participación

La convocatoria EA define y solicita evidencia de los siguientes requisitos para admitir la participación de un laboratorio:

1. Método de medición aplicable al alcance del EA, conforme a la norma EN correspondiente (EN 14211, EN 14212, EN 14625 o EN 14626) o métodos equivalentes demostrados.
2. Competencia técnica del personal operador, demostrada mediante formación documentada.
3. Equipos calibrados y en estado operativo, con certificados de calibración vigentes y trazabilidad metrológica demostrable.
4. Capacidad de reporte en unidades y formatos establecidos en DG-PSEA-01.
5. Declaración de incertidumbre de medición, cuando aplique al estadístico de desempeño seleccionado conforme a P-PSEA-06.

Los criterios de participación se comunican de manera clara antes del inicio de la ronda, incluyendo la especificación del número mínimo de participantes requerido para la validez estadística del esquema.

### 3.4 d) Número y tipo de participantes esperados

La capacidad operativa por ronda se define según la infraestructura y las condiciones de seguridad del laboratorio. El diseño estadístico define el número mínimo viable conforme a P-PSEA-06.

Las reglas de dimensionamiento estadístico son las siguientes:

| Condición | Enfoque estadístico |
|---|---|
| p ≥ 12 | Puede emplearse consenso robusto con robustez estadística adecuada. Para el criterio u(x_pt) ≤ 0,3σ_pt, la referencia operativa es p ≥ 17 cuando s* ≈ σ_pt. |
| 6 ≤ p < 12 | Se prioriza valor asignado externo y σ_pt prescriptiva. Métodos robustos se utilizan con cautela y solo como diagnóstico complementario. |
| p < 6 | No se utiliza consenso como base principal de desempeño. Se aplica valor asignado externo, σ_pt prescriptiva y estadístico En o ζ. |

Cuando el número esperado sea inferior a 12 participantes, el proveedor debe documentar y comunicar a los participantes los enfoques alternativos que se utilizarán para evaluar el desempeño (ISO/IEC 17043:2023, 7.2.2.3).

La planificación registra la justificación técnica del número esperado de participantes y los criterios de continuidad si el número inscrito es inferior al mínimo viable.

### 3.5 e) Actividades y resultados esperados de los participantes

El plan de ronda incluye la descripción secuencial de actividades:

1. Instalación y verificación operativa de los sistemas de generación de mezcla gaseosa.
2. Ejecución de mediciones por los participantes, conforme a I-PSEA-01 y DG-PSEA-01.
3. Recepción de resultados y metadatos dentro de la ventana de reporte establecida.
4. Validación técnica y estadística de los datos recibidos.
5. Emisión del informe de resultados conforme a P-PSEA-07.

Los resultados a reportar deben incluir: valor de concentración, incertidumbre expandida o estándar (según especificación), fecha de medición, método de medición, y cualquier observación relevante sobre condiciones de análisis.

El resultado esperado es un conjunto de datos válidos y trazables que permita una evaluación técnicamente defendible del desempeño de cada participante.

### 3.6 f) Rango esperado de valores

Se definen rangos generales de concentración por analito para la planificación logística de la ronda:

| Analito | Rango de concentración | Observaciones |
|---|---|---|
| SO₂ | 10–100 μg/m³ (~4–40 nmol/mol) | Cubre valores de fondo a niveles de alerta |
| NO/NO₂ | 10–200 μg/m³ (~5–100 nmol/mol) | Incluye niveles de fondo, urbano y tráfico |
| CO | 0,5–10 mg/m³ (~0,4–9 μmol/mol) | Cubre condiciones normales y episodios |
| O₃ | 20–200 μg/m³ (~10–100 nmol/mol) | Desde fondo a episodios fotoquímicos |

Las concentraciones objetivo específicas de cada ronda se fijan en DG-PSEA-01 y se sustentan en los resultados de los estudios de homogeneidad y estabilidad del lote.

Los rangos se seleccionan considerando:

- Los valores límite y umbrales de evaluación establecidos en la normativa ambiental aplicable (Directiva 2008/50/CE).
- Las concentraciones típicas de la red de monitoreo.
- Los rangos operativos de los métodos de referencia EN 14211, EN 14212, EN 14625 y EN 14626.

### 3.7 g) Fuentes potenciales de error y gestión de riesgos

La planificación integra la gestión de riesgos del SGC (ISO/IEC 17043:2023, cláusulas 7.2.1.2 y 8.5). Se identifican y evalúan las siguientes fuentes potenciales de error:

| Fuente de error | Tipo de riesgo | Control mitigante |
|---|---|---|
| Inestabilidad o heterogeneidad del ítem de ensayo | Técnico | Estudios de homogeneidad/estabilidad previos a la ronda |
| Fugas o alteraciones neumáticas | Técnico | Pruebas de hermeticidad previas al envío |
| Fallas eléctricas o ambientales | Operativo | Protocolos de contingencia y equipos de respaldo |
| Sesgos instrumentales | Técnico | Calibración vigente y verificación con patrón de transferencia |
| Interferencias químicas y efectos de matriz | Técnico | Selección de métodos de referencia validados |
| Errores de transcripción o reporte | Operativo | Validación de datos en recepción, formatos estandarizados |
| Colusión o falsificación de resultados | Ético | Codificación, segregación de información, controles de P-PSEA-08 |
| Número insuficiente de participantes | Estadístico | Criterios de continuidad y uso de valor asignado externo (P-PSEA-06) |
| Condiciones ambientales adversas (humedad, temperatura) | Técnico | Monitoreo continuo de condiciones durante medición |

Todo cambio significativo en el diseño, la operación o la evaluación de la ronda exige la evaluación documentada de riesgos y la aprobación del coordinador EA antes de su implementación (ISO/IEC 17043:2023, 7.2.1.2). Esta evaluación debe considerar las fuentes de error identificadas y establecer controles mitigantes con responsables asignados.

### 3.8 h) Requisitos técnicos y de control

**Producción de mezclas gaseosas:**

- Las mezclas primarias se preparan mediante dilución dinámica o preparación gravimétrica conforme a ISO 6142-1 o ISO 6145-7, con trazabilidad a Institutos Nacionales de Metrología.
- Para contaminantes donde existen MRC gaseosos disponibles (CO, NO, SO₂), se utilizarán cilindros certificados con trazabilidad a NMI.
- Para O₃ y NO₂ donde no existen MRC estables, se generan in-situ mediante sistemas de generación dinámica (GPT, permeación) trazables a fotómetros de referencia estándar (SRP).

**Control de calidad:**

1. Hojas de vida y certificados de calibración vigentes de los equipos críticos utilizados en la generación y verificación del ítem de ensayo.
2. Verificación de trazabilidad metrológica de calibraciones de equipos utilizados en producción y caracterización.
3. Control de condiciones ambientales y operativas (temperatura, humedad, presión, flujo) conforme a los límites establecidos en los procedimientos operativos.
4. Evidencias de las pruebas de homogeneidad y estabilidad del lote, ejecutadas conforme a P-PSEA-06.
5. Conservación de registros primarios y reportes técnicos de cada ronda.
6. El aplicativo CALAIRE-APP se utilizará como evidencia de caracterización de ítems cuando sea aplicable.

**Almacenamiento y distribución:**

- Cilindros almacenados en condiciones que preserven estabilidad (temperatura controlada, protección de luz solar para O₃ fotolítico).
- Cumplimiento de normativas para transporte de mercancías peligrosas (cilindros a presión, gases tóxicos).
- Control de temperatura durante transporte (loggers de temperatura cuando aplique).
- Confirmación de entrega a participantes con registro de condiciones de recepción.

### 3.9 i) Prevención de colusión y falsificación

Se aplican los siguientes controles de integridad:

1. Codificación única e irrepetible de cada participante, cuya correspondencia se mantiene en reserva bajo custodia del profesional de calidad.
2. Segregación de la información sensible: los participantes no acceden a la identidad de los demás durante la ejecución de la ronda. Se restringe la visibilidad de displays durante las mediciones.
3. Restricción de la interacción no controlada entre participantes durante el período de mediciones. Se establecen ventanas cortas de medición que reducen oportunidades de intercambio de resultados.
4. Declaración escrita de confidencialidad y no colusión, firmada por cada participante en DG-PSEA-01.
5. Revisión de patrones estadísticos sospechosos por el estadístico, conforme a P-PSEA-06. Se verifica la coherencia entre resultados reportados y capacidades declaradas.

Ante sospecha de colusión o falsificación se activa P-PSEA-08, que puede incluir auditoría in-situ y suspensión de participación en futuras rondas.

### 3.10 j) Información a suministrar y cronograma

Antes de la ejecución, el Laboratorio CALAIRE entrega a cada participante, a través de DG-PSEA-01 (ISO/IEC 17043:2023, 7.1.2.1):

1. Objetivos y alcance del esquema.
2. Criterios para participar.
3. El calendario tipo (F-PSEA-01) con fechas de envío, ventanas de medición y fecha límite de reporte.
4. La comunicación técnica detallada (DG-PSEA-01) con concentraciones objetivo, método(s) admisible(s), condiciones operativas y requisitos de reporte.
5. El instructivo de embalaje y transporte (I-PSEA-01) con las instrucciones de manipulación, conexión y condiciones de seguridad.
6. Los criterios de evaluación y la indicación del estadístico de desempeño aplicable, conforme a P-PSEA-06.
7. Arreglos de confidencialidad.
8. Honorarios de participación (si aplica).

**Cronograma típico de una ronda:**

| Momento | Actividad |
|---|---|
| T-4 semanas | Cierre de inscripciones y definición final del diseño |
| T-3 semanas | Producción de ítems, estudios de homogeneidad y estabilidad |
| T-2 semanas | Envío/acceso de ítems a participantes |
| T-2 a T-1 semanas | Ventana de medición |
| T-1 semana | Fecha límite de envío de resultados |
| T0 a T+2 semanas | Análisis estadístico y evaluación de desempeño |
| T+3 semanas | Emisión de informe preliminar (si aplica) |
| T+4 a T+6 semanas | Gestión de quejas y apelaciones |
| T+7 semanas | Emisión de informe final |

### 3.11 k) Frecuencia y plazos de reporte

La frecuencia de rondas y las ventanas de reporte se definen en el programa anual y se formalizan en F-PSEA-01. Los EA se realizan con frecuencia anual para cada grupo de analitos. Cada convocatoria EA comunica los plazos específicos de:

- Fecha estimada de disponibilidad del ítem de ensayo.
- Fecha de envío o acceso.
- Fecha límite de recepción de resultados.
- Fecha prevista de emisión del informe preliminar.
- Fecha de emisión del informe final.

### 3.12 l) Métodos y procedimientos

Se especifican los métodos admisibles por analito, que corresponden a los métodos de referencia europeos:

| Analito | Norma de método | Técnica de medición |
|---|---|---|
| NO/NO₂ | EN 14211:2012 | Quimioluminiscencia |
| SO₂ | EN 14212:2012 | Fluorescencia UV |
| O₃ | EN 14625:2012 | Fotometría UV |
| CO | EN 14626:2012 | Espectroscopia infrarroja no dispersiva (NDIR) |

Se aceptan otros métodos equivalentes cuando el laboratorio demuestre competencia para el método declarado. Los participantes deben:

- Usar sus métodos rutinarios de medición y calibración, salvo especificación contraria en el protocolo.
- Reportar el método utilizado cuando se requiera análisis por subgrupos.
- Realizar calibración multipunto y verificación de cero/span antes del EA.
- Cumplir con las condiciones operativas mínimas, los criterios de aceptación de datos y los requisitos de incertidumbre establecidos en DG-PSEA-01 e I-PSEA-01.

### 3.13 m) Pruebas de homogeneidad y estabilidad

Las pruebas de homogeneidad y estabilidad se ejecutan y documentan conforme a ISO 13528:2022 y P-PSEA-06, después del envasado final de los ítems de ensayo y antes de la consolidación de la evaluación del desempeño.

Los criterios de aceptación se establecen en función de la σ_pt del esquema:

- **Homogeneidad:** La desviación estándar entre unidades (s_s) debe ser inferior a 0,3 σ_pt.
- **Estabilidad:** El efecto de la inestabilidad entre el inicio y el cierre de la ventana de la ronda debe ser inferior a 0,3 σ_pt.
- Se utiliza un método de ensayo con repetibilidad adecuada (σ_an / σ_pt < 0,5).

Cuando la inestabilidad o heterogeneidad supere estos criterios, la contribución se incorpora a la incertidumbre del valor asignado (u_hom o u_stab) conforme a P-PSEA-06.

**Consideraciones específicas por analito:**

- **CO, NO, SO₂ en N₂:** Se confía en datos históricos de estabilidad del proveedor de MRC. Si se requiere confirmación, se analizan muestras de retención al inicio y final de la ronda.
- **NO₂ en aire, O₃:** Se realizan estudios específicos en cada ronda o se establecen condiciones estrictas de control (tiempo de uso, temperatura, presión de almacenamiento).

### 3.14 n) Formatos de reporte

El registro de resultados se realiza en el formato controlado establecido. Se preparan formatos estandarizados para:

**Formato de reporte del participante:** debe contener como mínimo:

1. Código de identificación del participante.
2. Resultado reportado, con la unidad de medida normalizada.
3. Incertidumbre declarada (expandida o estándar, según especificación), con factor de cobertura y nivel de confianza.
4. Método de medición declarado.
5. Fecha de medición.
6. Observaciones de validez técnica.

**Formato de reporte del esquema al participante:** incluye datos del participante, valor asignado, σ_pt, estadísticos de desempeño, interpretación y gráficos.

Los formatos se diseñan para minimizar errores de transcripción y se validan técnicamente antes de su emisión.

### 3.15 o) Análisis estadístico

La planificación estadística de cada ronda debe declarar, conforme a P-PSEA-06:

1. La jerarquía de selección del valor asignado (x_pt) — 5 métodos en orden de independencia.
2. La jerarquía de selección de la desviación estándar para la evaluación de aptitud (σ_pt) — 6 métodos conforme a ISO 13528:2022 §8.
3. La regla de selección del estadístico de desempeño (z, z', ζ o En), basada en el criterio u(x_pt) ≤ 0,3σ_pt.
4. Los criterios de exclusión y el tratamiento de resultados no válidos.

La selección del método estadístico se basa en el número de participantes, la disponibilidad de valores de referencia independientes y los objetivos del esquema. Para poblaciones reducidas (p < 12), se utilizan valores asignados independientes y σ_pt prescriptivo, con estadísticos z' o ζ cuando u(x_pt) > 0,3 × σ_pt.

El detalle metodológico se establece en P-PSEA-06. El plan de ronda registra la referencia a la versión vigente de P-PSEA-06 que aplica.

### 3.16 p) Trazabilidad e incertidumbre del valor asignado

La trazabilidad del valor asignado se establece por una de las siguientes vías, en orden de prelación:

1. Valor formulado a partir de mezcla gaseosa gravimétricamente preparada (ISO 6142-1), con trazabilidad a patrones de masa del SI.
2. Valor de material de referencia certificado, con trazabilidad a un instituto nacional de metrología o laboratorio de referencia acreditado.
3. Valor de laboratorio de referencia con trazabilidad demostrada al SI.

La trazabilidad metrológica se demuestra mediante cadena documentada de calibraciones hasta patrones nacionales o internacionales.

La incertidumbre definitiva del valor asignado se calcula integrando las contribuciones por caracterización, homogeneidad y estabilidad:

`u(x_pt,def) = √[ u(x_pt)² + u_hom² + u_stab² ]`

Cada componente se determina conforme a P-PSEA-06.

### 3.17 q) Tratamiento de diferentes métodos de medición

Cuando la ronda incluya participantes que utilizan diferentes métodos de medición, la planificación debe definir de antemano si la evaluación será:

- **Conjunta:** cuando los métodos son técnicamente equivalentes y se espera que produzcan resultados comparables. Se utiliza un único x_pt y σ_pt.
- **Segmentada:** cuando los métodos producen resultados no comparables. Se define x_pt, σ_pt y evaluación independiente por familia metodológica.

Se realiza análisis preliminar para identificar diferencias sistemáticas entre métodos. Si se evidencian diferencias significativas, se evalúa la necesidad de estratificar por métodos. La decisión y su justificación se registran en el expediente de la ronda.

### 3.18 r) Criterios de desempeño

La selección del estadístico de desempeño se realiza conforme a P-PSEA-06. La interpretación institucional es la siguiente:

| Estadístico | Satisfactorio | Cuestionable | No satisfactorio |
|---|---|---|---|
| z, z', ζ | \|score\| ≤ 2 | 2 < \|score\| < 3 | \|score\| ≥ 3 |
| En | \|En\| ≤ 1 | — | \|En\| > 1 |

El criterio de selección del estadístico (z, z', ζ o En) depende de:
- La incertidumbre del valor asignado frente a σ_pt (criterio 0,3σ_pt).
- Si los participantes declaran incertidumbre.
- El tipo de valor asignado (externo vs. consenso).
- El número de participantes.

Para poblaciones reducidas (p < 12), se prefieren z' o ζ. El estadístico En es más adecuado para comparaciones metrológicas de alta precisión cuando se dispone de incertidumbres expandidas.

### 3.19 s) Informes y comunicación de resultados

La emisión del informe se ejecuta conforme a P-PSEA-07. Se proporciona a los participantes:

1. **Informe preliminar** (opcional): resultados preliminares antes de cierre definitivo, permitiendo verificación de datos.
2. **Informe final:** resultados completos con valor asignado, σ_pt, estadísticos de desempeño, interpretación y gráficos de desempeño.
3. Información sobre la posición relativa del laboratorio en la distribución de resultados.
4. Oportunidad para solicitar aclaraciones o presentar apelaciones.

El informe incluye los elementos obligatorios establecidos en ISO/IEC 17043:2023 (cláusula 7.4.3.2) e ISO 13528:2022.

### 3.20 t) Publicación y confidencialidad

La identidad y los resultados individuales de los participantes se manejan bajo la política de confidencialidad del SGC (ISO/IEC 17043:2023, cláusula 4.2). Se establecen las siguientes directrices:

1. Los resultados individuales solo se comparten con el propio laboratorio participante, identificado por código.
2. La comunicación externa de resultados agregados se realiza de forma codificada, sin identificación individual, salvo obligación legal o regulatoria documentada.
3. El proveedor puede publicar informes resumidos o anónimos para fines académicos o de mejora, siempre que no permitan la identificación de participantes.
4. Cualquier publicación de resultados individuales requiere autorización explícita del participante.

La política de confidencialidad y retención documental se comunica a los participantes en DG-PSEA-01. El Laboratorio CALAIRE mantiene acuerdos de confidencialidad legalmente vinculantes con todo el personal y los proveedores externos involucrados.

### 3.21 u) Contingencias

La planificación define escenarios de contingencia para las siguientes situaciones:

| Evento | Acción de continuidad |
|---|---|
| Falla del ítem de ensayo | Se envía ítem de reemplazo si hay disponibilidad; se evalúa reprogramación de la ronda. Se extiende plazo de reporte si es necesario. |
| Indisponibilidad de equipos críticos | Evaluar impacto técnico; reprogramar si es necesario. |
| Alteraciones de seguridad o infraestructura | Suspender actividades; asegurar integridad de datos y registros. |
| Ítem dañado en transporte | El participante reporta inmediatamente; se evalúa causa y se envía reemplazo si es posible. De lo contrario, retiro sin penalización. |
| Envío tardío de resultados por un participante | Evaluar si el resultado puede incluirse conforme a P-PSEA-06; gestionar exclusión documentada. |
| Número insuficiente de participantes (< mínimo viable) | Activar reglas de continuidad y criterios de valor asignado externo de P-PSEA-06. Documentar justificación técnica. |

Toda contingencia genera un registro en el expediente de la ronda, con la evaluación de impacto, la decisión formal y las acciones tomadas. El coordinador EA aprueba la continuidad, reprogramación o cancelación de la ronda. Todos los incidentes se analizan como parte del sistema de gestión de riesgos del proveedor.

---

## 4. Gestión de riesgos por cambios en el diseño (ISO/IEC 17043:2023, 7.2.1.2)

Cualquier cambio significativo en el diseño, la operación o la evaluación de una ronda EA requiere evaluación documentada de riesgos antes de su implementación. Se consideran cambios significativos:

1. Modificación del valor asignado o del método de obtención.
2. Cambio en el estadístico de desempeño.
3. Cambio en la σ_pt o en el método de determinación.
4. Cambio en el número de participantes que implique transición entre escenarios de P-PSEA-06.
5. Cambio en el ítem de ensayo, método de generación o condiciones de estabilidad.

La evaluación de riesgos se documenta con la identificación del cambio, el análisis de impacto, los controles mitigantes propuestos y la aprobación del coordinador EA.

---

## 5. Control documental

### 5.1 Expediente de la ronda

Cada ronda EA genera un expediente que incluye:

- Plan de la ronda (documento de planificación interno).
- F-PSEA-01 y DG-PSEA-01 emitidos.
- Evidencias de autorización del personal involucrado.
- Resultados de los estudios de homogeneidad y estabilidad.
- Base de datos cruda y base depurada.
- Informe preliminar y comentarios recibidos.
- Informe final (P-PSEA-07).
- Registro de contingencias, si las hubo.
- Evaluación de riesgos, si hubo cambios significativos en el diseño.

### 5.2 Control de cambios

Los cambios a este procedimiento se gestionan conforme al sistema de control documental del SGC. Todo cambio significativo en el diseño de un esquema EA requiere la evaluación de riesgos documentada conforme a la sección 4 de este procedimiento.

---

## 6. Referencias cruzadas

| Documento | Relación |
|---|---|
| P-PSEA-06 | Define la metodología estadística para x_pt, σ_pt, incertidumbre y puntajes de desempeño. P-PSEA-09 declara **qué** se planifica y P-PSEA-06 define **cómo** se sustenta estadísticamente. |
| P-PSEA-07 | Genera el informe de resultados conforme a los criterios definidos en la planificación. |
| P-PSEA-08 | Se activa ante sospecha de colusión o falsificación. |
| P-PSEA-02 a P-PSEA-05 | Procedimientos operativos por analito (NO-NO₂, CO, O₃, SO₂). |
| F-PSEA-01 | Establece el calendario tipo de la ronda. |
| DG-PSEA-01 | Comunicado detallado a participantes con objetivos, criterios y requisitos. |
| I-PSEA-01 | Instructivo de embalaje, transporte y manipulación del ítem. |

---

| REVISÓ |  | APROBÓ |  |
| --- | :--- | :--- | :--- |
| **ROL** | Profesional de Calidad | **ROL** | Coordinador EA |
| **FECHA** |  | **FECHA** |  |
