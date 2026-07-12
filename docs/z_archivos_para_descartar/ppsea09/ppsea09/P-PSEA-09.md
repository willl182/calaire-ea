# P-PSEA-09 — Planificación y Preparación de Rondas de Ensayo de Aptitud para Gases Contaminantes Criterio

**Código:** P-PSEA-09  
**Versión:** 3.0  
**Fecha de emisión:** 2026-03-22  
**Referencia normativa:** ISO/IEC 17043:2023, ISO 13528:2022  
**Procedimientos relacionados:** P-PSEA-02, P-PSEA-03, P-PSEA-04, P-PSEA-05, P-PSEA-06, P-PSEA-07, P-PSEA-08  

---

## 1. Información general del procedimiento

### 1.1 Objetivo

Establecer las directrices, responsabilidades y actividades para planificar y preparar las rondas de ensayos de aptitud (EA) de gases contaminantes criterio, garantizando el cumplimiento de ISO/IEC 17043:2023 e ISO 13528:2022 y asegurando la validez, imparcialidad, trazabilidad y consistencia técnica del esquema.

### 1.2 Alcance

Este procedimiento aplica a todas las etapas de planificación previas al inicio de cada ronda EA para dióxido de azufre (SO2), óxidos de nitrógeno (NO/NO2), monóxido de carbono (CO) y ozono (O3). Incluye la definición del esquema, la gestión de participantes y proveedores externos, la preparación y control del ítem de ensayo, la gestión de riesgos, la comunicación operativa y la declaración de los criterios de evaluación. El detalle metodológico para valor asignado, desviación estándar para evaluación de aptitud, incertidumbre y estadísticos de desempeño se define en P-PSEA-06.

### 1.3 Definiciones

| Término | Definición |
|---|---|
| Ensayo de aptitud (EA) | Evaluación del desempeño de un laboratorio mediante comparaciones interlaboratorios, conforme a ISO/IEC 17043:2023. |
| Ítem de ensayo | Atmósfera de gas contaminante criterio generada dinámicamente a partir de mezcla gaseosa certificada, patrón fotométrico o referencia trazable equivalente. |
| Valor asignado (x_pt) | Valor atribuido al mensurando del EA, determinado conforme a P-PSEA-06. |
| σ_pt | Desviación estándar para la evaluación de la aptitud; criterio de dispersión preestablecido contra el cual se juzga el desempeño de cada participante. |
| u(x_pt) | Incertidumbre estándar del valor asignado por la vía de caracterización. |
| u(x_pt,def) | Incertidumbre estándar definitiva del valor asignado, integrada con las contribuciones por homogeneidad y estabilidad: u(x_pt,def) = √[u(x_pt)^2 + u_hom^2 + u_stab^2]. |
| Participante | Laboratorio que reporta resultados en el EA conforme a los criterios establecidos. |
| p | Número de participantes válidos incluidos en el análisis estadístico definitivo. |

### 1.4 Documentos de referencia

- ISO/IEC 17043:2023 — Requisitos generales para proveedores de ensayos de aptitud.
- ISO 13528:2022 — Métodos estadísticos para EA por comparación interlaboratorio.
- ISO/IEC 17025:2017 — Requisitos generales para laboratorios de ensayo y calibración.
- ISO 6142-1:2015 — Análisis de gases. Preparación gravimétrica de mezclas gaseosas de referencia.
- ISO 6145-7 — Preparación de mezclas gaseosas por dilución dinámica.
- ISO 17034:2016 — Requisitos generales para la competencia de productores de materiales de referencia.
- P-PSEA-06 — Diseño estadístico para EA: métodos para x_pt, σ_pt, incertidumbre y puntajes.
- P-PSEA-07 — Elaboración de informe de resultados de EA.
- P-PSEA-08 — Gestión de colusión, falsificación y desviaciones de integridad en EA.
- P-PSEA-02, P-PSEA-03, P-PSEA-04 y P-PSEA-05 — Procedimientos operativos por analito.
- F-PSEA-01 — Calendario tipo de rondas EA.
- DG-PSEA-01 — Protocolo detallado de participación en EA de gases contaminantes criterio.
- I-PSEA-01 — Instructivo de embalaje, transporte y manipulación del ítem de ensayo.

---

## 2. Roles, responsabilidades y autorización del personal

### 2.1 Roles y responsabilidades

| Rol | Responsabilidad principal |
|---|---|
| Coordinador EA | Aprueba el diseño del esquema, verifica la disponibilidad de recursos y autoriza la emisión de resultados. Aprueba la continuidad, reprogramación o cancelación de la ronda ante contingencias. |
| Estadístico / Experto técnico | Diseña el plan estadístico conforme a P-PSEA-06, valida los criterios de desempeño y revisa la coherencia técnica del análisis. |
| Ingeniero operativo | Lidera la preparación de ítems, controla las condiciones ambientales y coordina el montaje de la infraestructura de generación. |
| Experto técnico en calidad del aire | Define los rangos de concentración, verifica la trazabilidad metrológica y valida la aplicabilidad de los métodos de referencia o equivalentes. |
| Profesional de calidad | Garantiza el cumplimiento del SGC, la imparcialidad, la confidencialidad y la trazabilidad documental. |
| Profesional de proyectos / Comunicaciones | Gestiona la convocatoria, la comunicación con participantes, el envío de formatos y el seguimiento de reportes. |

### 2.2 Autorización formal del personal (ISO/IEC 17043:2023, §6.2.6)

El Laboratorio CALAIRE mantiene autorización formal y evidencia de competencia documentada para el personal que ejecuta las siguientes actividades críticas:

1. Planificación de esquemas de EA.
2. Evaluación de homogeneidad, estabilidad, valor asignado e incertidumbre.
3. Evaluación del desempeño de participantes.
4. Emisión de opiniones e interpretaciones técnicas.
5. Revisión y autorización de informes EA.

Las autorizaciones se registran individualmente en los perfiles de cargo y se revisan dentro del ciclo de auditoría interna del SGC. Ninguna de estas actividades podrá ser ejecutada por personal sin autorización formal vigente.

### 2.3 Actividades no subcontratables (ISO/IEC 17043:2023, §6.4.1)

Las siguientes actividades son de ejecución interna exclusiva y no pueden ser externalizadas:

- Diseño y planificación del esquema EA.
- Evaluación del desempeño de participantes.
- Selección final del valor asignado y de los criterios de evaluación.
- Revisión y autorización de informes EA.

Las actividades de apoyo que sí puedan subcontratarse, tales como calibraciones especializadas, logística de transporte o suministro de materiales de referencia, se controlan mediante evaluación documentada del proveedor conforme al procedimiento de compras y control de proveedores del SGC. El proveedor del EA permanece responsable ante los participantes por los productos y servicios suministrados externamente.

---

## 3. Planificación específica de la ronda (ISO/IEC 17043:2023, §7.2.1.3)

La planificación de cada ronda EA se documenta antes de su inicio, siguiendo los literales a) a u) del presente apartado, en concordancia con ISO/IEC 17043:2023.

### 3.1 a) Personal involucrado en el diseño y la operación

Se identifican y documentan todos los roles involucrados en cada ronda, con sus nombres, evidencias de competencia y autorización formal vigente conforme a la sección 2.2 de este procedimiento. El expediente de la ronda registra la asignación de responsabilidades y la aceptación formal de los responsables.

### 3.2 b) Actividades de proveedores externos

Las actividades ejecutadas por proveedores externos se documentan con: identificación del proveedor, descripción del servicio subcontratado, evidencia de evaluación de competencia, acuerdos de confidencialidad vigentes y mecanismo de supervisión aplicable. El coordinador EA revisa y aprueba la idoneidad de cada proveedor antes de la contratación. Ninguna de las actividades listadas en la sección 2.3 puede ser objeto de subcontratación.

Cuando un proveedor externo realice mediciones relevantes para la caracterización del ítem de ensayo, debe demostrar competencia técnica y trazabilidad metrológica, preferiblemente bajo un sistema alineado con ISO/IEC 17025.

### 3.3 c) Criterios de participación

La convocatoria EA define y solicita evidencia previa de los siguientes criterios para admitir la participación:

1. Método de medición aplicable al alcance del EA, conforme a EN 14211, EN 14212, EN 14625 o EN 14626, o método equivalente US-EPA debidamente declarado.
2. Competencia técnica del personal operador, demostrada mediante formación documentada.
3. Equipos calibrados y en estado operativo, con certificados vigentes y trazabilidad metrológica demostrable.
4. Capacidad de reporte en las unidades, formatos y plazos establecidos en DG-PSEA-01.
5. Declaración de incertidumbre de medición cuando aplique al estadístico de desempeño seleccionado conforme a P-PSEA-06.

Los criterios se comunican en la convocatoria formal y en DG-PSEA-01, junto con las condiciones de confidencialidad y de aceptación de datos.

### 3.4 d) Número y tipo de participantes esperados

La capacidad operativa de cada ronda se define según la infraestructura disponible, las condiciones de seguridad del laboratorio y la regla de un instrumento por participante. El diseño estadístico establece en P-PSEA-06 el número mínimo viable según el método seleccionado para x_pt y σ_pt.

| Número de participantes válidos (p) | Enfoque estadístico aplicable |
|---|---|
| p ≥ 17 | Consenso robusto con mayor suficiencia para verificar u(x_pt) ≤ 0,3σ_pt cuando s* ≈ σ_pt. |
| 12 ≤ p < 17 | Consenso robusto viable, sujeto a verificación de la incertidumbre del valor asignado antes de usar z. |
| 6 ≤ p < 12 | Se prioriza valor asignado externo o independiente y σ_pt prescriptiva; los métodos robustos solo se emplean como diagnóstico complementario. |
| p < 6 | No se utiliza consenso como base principal del desempeño. Se aplica valor asignado externo, σ_pt prescriptiva y estadísticos que incorporen incertidumbre. |

Cuando el número esperado o definitivo sea inferior a 12 participantes, la planificación debe documentar y comunicar el enfoque alternativo de evaluación. En estos casos no debe asumirse consenso automático para x_pt ni para σ_pt.

### 3.5 e) Actividades y resultados esperados de los participantes

El plan de ronda define, como mínimo, las siguientes actividades esperadas de los participantes:

1. Instalación y verificación operativa del instrumento conforme a I-PSEA-01 y DG-PSEA-01.
2. Ejecución de mediciones dentro de la ventana establecida en F-PSEA-01.
3. Reporte de resultados en el formato y las unidades definidas.
4. Declaración de incertidumbre asociada cuando el estadístico de desempeño lo requiera.
5. Registro del método utilizado y de las observaciones técnicas pertinentes.

El resultado esperado del esquema es un conjunto de datos válidos, trazables y comparables que permita evaluar el desempeño de cada participante con sustento técnico.

### 3.6 f) Rango esperado de valores

Se definen rangos generales de concentración por analito para la planificación logística de la ronda:

| Analito | Rango de concentración | Observaciones |
|---|---|---|
| SO2 | 10-100 ug/m3 (~4-40 nmol/mol) | Cubre valores de fondo a niveles de alerta |
| NO/NO2 | 10-200 ug/m3 (~5-100 nmol/mol) | Incluye niveles de fondo, urbano y tráfico |
| CO | 0,5-10 mg/m3 (~0,4-9 umol/mol) | Cubre condiciones normales y episodios |
| O3 | 20-200 ug/m3 (~10-100 nmol/mol) | Desde fondo a episodios fotoquímicos |

Las concentraciones objetivo específicas de cada ronda se fijan en DG-PSEA-01 y se sustentan en los resultados de los estudios de homogeneidad y estabilidad del lote.

Los rangos se seleccionan considerando:

- Los umbrales de evaluación establecidos en la normativa ambiental aplicable y en los requerimientos técnicos del esquema.
- Las concentraciones típicas de la red de monitoreo.
- Los rangos operativos de los métodos de referencia EN 14211, EN 14212, EN 14625 y EN 14626.

### 3.7 g) Fuentes potenciales de error y gestión de riesgos

La planificación integra la gestión de riesgos del SGC en cumplimiento de ISO/IEC 17043:2023 §7.2.1.2. Antes de cada ronda se identifican y evalúan, como mínimo, las siguientes fuentes potenciales de error:

| Fuente de error | Tipo de riesgo | Control de mitigación |
|---|---|---|
| Inestabilidad o heterogeneidad del ítem de ensayo | Técnico | Estudios de homogeneidad y estabilidad previos a la ronda conforme a P-PSEA-06 |
| Fugas o alteraciones neumáticas | Técnico | Pruebas de hermeticidad y verificación de líneas y conexiones |
| Errores de calibración o verificación de equipos | Técnico | Certificados vigentes y verificación con patrones de transferencia |
| Fallas ambientales (temperatura, humedad, presión) | Operativo | Monitoreo continuo y protocolos de contingencia |
| Errores de transcripción o reporte | Operativo | Formato controlado y validación de datos en recepción |
| Colusión o falsificación de resultados | Ético / Estadístico | Codificación, segregación de información y aplicación de P-PSEA-08 |
| Número insuficiente de participantes | Estadístico | Criterios de continuidad y aplicación de valor asignado externo o σ_pt prescriptiva |

Todo cambio significativo en el diseño, la operación o los criterios de evaluación de una ronda exige evaluación documentada de riesgos y aprobación explícita del coordinador EA antes de su implementación.

### 3.8 h) Requisitos técnicos y de control

Se exigen los siguientes requisitos técnicos para la preparación y control de los ítems de ensayo:

1. Uso de mezclas gaseosas de referencia o materiales de referencia con trazabilidad metrológica demostrable.
2. Hojas de vida y certificados de calibración vigentes de los equipos críticos utilizados en la generación y verificación del ítem.
3. Control de condiciones ambientales y operativas (temperatura, humedad, presión y flujo) conforme a los límites establecidos en los procedimientos operativos.
4. Generadores de ozono con fotómetro de referencia y manifold o líneas inertes que minimicen adsorción o pérdidas.
5. Evidencias trazables de las pruebas de homogeneidad y estabilidad del lote, ejecutadas conforme a P-PSEA-06.
6. Conservación de registros primarios y reportes técnicos de cada ronda como parte del expediente.

El aplicativo CALAIRE-APP podrá utilizarse como herramienta de cálculo y evidencia operativa, pero no reemplaza la obligación de conservar datos fuente, registros y reporte técnico de homogeneidad y estabilidad.

### 3.9 i) Prevención de colusión y falsificación

Se aplican los siguientes controles de integridad:

1. Codificación única e irrepetible de cada participante, cuya correspondencia se mantiene bajo custodia del profesional de calidad.
2. Segregación de la información sensible: los participantes no acceden a la identidad ni a los resultados de los demás durante la ejecución de la ronda.
3. Restricción de la interacción no controlada entre participantes durante el periodo de medición.
4. Declaración escrita de confidencialidad y no colusión incorporada en DG-PSEA-01.
5. Revisión de patrones estadísticos sospechosos por parte del estadístico, conforme a P-PSEA-06.

Ante sospecha de colusión o falsificación se activa P-PSEA-08.

### 3.10 j) Información a suministrar y cronograma

Antes de la ejecución de la ronda, el Laboratorio CALAIRE suministra a cada participante:

1. Objetivos y alcance del esquema.
2. Criterios para participar.
3. El calendario tipo (F-PSEA-01) con fechas de envío, ventana de medición y fecha límite de reporte.
4. La comunicación técnica detallada (DG-PSEA-01) con concentraciones objetivo, métodos admisibles, condiciones operativas y requisitos de reporte.
5. El instructivo de embalaje y transporte (I-PSEA-01) con las instrucciones de manipulación, conexión y seguridad.
6. Los criterios de evaluación y la indicación del estadístico de desempeño aplicable conforme a P-PSEA-06.
7. Las disposiciones de confidencialidad y, si aplica, los honorarios de participación.

| Momento | Actividad |
|---|---|
| T-4 semanas | Cierre de inscripciones y definición final del diseño |
| T-3 semanas | Producción de ítems y estudios de homogeneidad y estabilidad |
| T-2 semanas | Envío o acceso de ítems a participantes |
| T-2 a T-1 semanas | Ventana de medición |
| T-1 semana | Fecha límite de envío de resultados |
| T0 a T+2 semanas | Análisis estadístico y evaluación de desempeño |
| T+3 semanas | Emisión de informe preliminar, si aplica |
| T+4 a T+6 semanas | Gestión de comentarios, quejas o apelaciones |
| T+7 semanas | Emisión de informe final |

### 3.11 k) Frecuencia y plazos de reporte

La frecuencia de las rondas y las ventanas de reporte se definen en el programa anual y se formalizan en F-PSEA-01. Cada convocatoria comunica los plazos específicos para:

- Disponibilidad del ítem de ensayo.
- Envío o acceso al ítem.
- Recepción de resultados.
- Emisión de informe preliminar, si aplica.
- Emisión de informe final.

Los resultados tardíos, incompletos o formalmente inválidos podrán ser excluidos del análisis principal, dejando la trazabilidad y justificación correspondiente en el expediente de la ronda.

### 3.12 l) Métodos y procedimientos

Se especifican los métodos admisibles por analito:

| Analito | Norma de método | Técnica de medición |
|---|---|---|
| NO/NO2 | EN 14211:2012 | Quimioluminiscencia |
| SO2 | EN 14212:2012 | Fluorescencia UV |
| O3 | EN 14625:2012 | Fotometría UV |
| CO | EN 14626:2012 | Espectroscopia infrarroja no dispersiva (NDIR) |

Se aceptan métodos equivalentes cuando el laboratorio participante demuestre competencia para el método declarado y su pertinencia técnica para el esquema. Los participantes deben usar sus métodos rutinarios salvo especificación contraria en el protocolo.

### 3.13 m) Pruebas de homogeneidad y estabilidad

Las pruebas de homogeneidad y estabilidad se ejecutan y documentan conforme a ISO 13528:2022 y P-PSEA-06, después de la preparación final del ítem de ensayo y antes de la consolidación de la evaluación del desempeño.

Los criterios de aceptación se establecen en función de σ_pt del esquema:

- Homogeneidad: la desviación estándar entre unidades debe ser inferior a 0,3 σ_pt.
- Estabilidad: el efecto de la inestabilidad dentro de la ventana de la ronda debe ser inferior a 0,3 σ_pt.
- El método de ensayo empleado en H&E debe tener repetibilidad adecuada para el objetivo del estudio.

Cuando alguno de estos criterios no se cumple, la contribución correspondiente se incorpora a u(x_pt,def) mediante u_hom o u_stab conforme a P-PSEA-06.

### 3.14 n) Formatos de reporte

El registro de resultados se realiza en un formato controlado. El formato de reporte del participante debe contener como mínimo:

1. Código de identificación del participante.
2. Resultado reportado con la unidad normalizada.
3. Incertidumbre declarada, expandida o estándar según la especificación del esquema, con su factor de cobertura cuando aplique.
4. Método de medición declarado.
5. Fecha de medición.
6. Observaciones de validez técnica.

Los formatos se diseñan para minimizar errores de transcripción y se validan técnicamente antes de su emisión.

### 3.15 o) Análisis estadístico

La planificación estadística de cada ronda debe declarar, conforme a P-PSEA-06:

1. La jerarquía de selección del valor asignado (x_pt).
2. La jerarquía de selección de la desviación estándar para evaluación de aptitud (σ_pt).
3. La regla de selección del estadístico de desempeño (z, z', ζ o En), basada en el criterio u(x_pt) ≤ 0,3σ_pt cuando corresponda.
4. Los criterios de exclusión y el tratamiento de resultados no válidos.

Para poblaciones reducidas (p < 12), se utilizan valores asignados independientes y σ_pt prescriptiva o definida por aptitud para el uso. En esos escenarios se prefieren estadísticos que incorporen incertidumbre, según la información disponible.

### 3.16 p) Trazabilidad e incertidumbre del valor asignado

La trazabilidad del valor asignado se establece por una de las siguientes vías, en orden de prelación:

1. Valor formulado a partir de mezcla gaseosa gravimétricamente preparada o por dilución dinámica con trazabilidad metrológica.
2. Valor de material de referencia certificado.
3. Valor de laboratorio de referencia con trazabilidad demostrada.
4. Valor de un grupo de laboratorios expertos, cuando esté técnicamente justificado.
5. Consenso de participantes, únicamente cuando el diseño del esquema lo permita y exista suficiencia técnica para ello.

La incertidumbre definitiva del valor asignado se calcula integrando las contribuciones por caracterización, homogeneidad y estabilidad:

`u(x_pt,def) = √[ u(x_pt)^2 + u_hom^2 + u_stab^2 ]`

Cada componente se determina conforme a P-PSEA-06.

### 3.17 q) Tratamiento de diferentes métodos de medición

Cuando la ronda incluya participantes que utilizan diferentes métodos de medición, la planificación debe definir anticipadamente si la evaluación será:

- Conjunta: cuando los métodos son técnicamente equivalentes y producen resultados comparables.
- Segmentada: cuando los métodos o configuraciones generan sesgos sistemáticos que justifican evaluación separada.

La decisión y su justificación se registran en el expediente de la ronda antes del análisis de resultados.

### 3.18 r) Criterios de desempeño

La selección del estadístico de desempeño se realiza conforme a P-PSEA-06. La interpretación institucional es la siguiente:

| Estadístico | Satisfactorio | Cuestionable | No satisfactorio |
|---|---|---|---|
| z, z', ζ | \|score\| ≤ 2 | 2 < \|score\| < 3 | \|score\| ≥ 3 |
| En | \|En\| ≤ 1 | — | \|En\| > 1 |

El criterio de selección del estadístico depende de:

- La incertidumbre del valor asignado frente a σ_pt.
- La disponibilidad y calidad de las incertidumbres declaradas por los participantes.
- El tipo de valor asignado utilizado.
- El número de participantes válidos.

### 3.19 s) Informes y comunicación de resultados

La emisión del informe se ejecuta conforme a P-PSEA-07. Se podrá emitir un informe preliminar para verificación de datos antes del cierre definitivo. El informe final incluye, como mínimo:

1. Conjunto de datos consolidado y codificado.
2. Valor asignado con su incertidumbre.
3. σ_pt y estadísticos de desempeño por participante.
4. Interpretación de resultados y gráficos de desempeño.
5. Comentarios técnicos, limitaciones de interpretación y, cuando aplique, referencia a quejas o apelaciones.

### 3.20 t) Publicación y confidencialidad

La identidad y los resultados individuales de los participantes se manejan bajo la política de confidencialidad del SGC. Se establecen las siguientes directrices:

1. Los resultados individuales solo se comunican al participante correspondiente, identificado por código.
2. La comunicación externa de resultados agregados se realiza sin identificación individual, salvo obligación legal o regulatoria documentada.
3. La política de confidencialidad y la retención documental se comunican a los participantes en DG-PSEA-01.
4. Todo el personal y los proveedores externos involucrados deben operar bajo compromisos de confidencialidad vigentes.

### 3.21 u) Contingencias

La planificación define escenarios de contingencia para las siguientes situaciones:

| Evento | Acción de continuidad |
|---|---|
| Falla del ítem de ensayo | Evaluar reposición del ítem o reprogramación de la ronda |
| Indisponibilidad de equipos críticos | Evaluar impacto técnico y reprogramar si es necesario |
| Alteraciones de seguridad o infraestructura | Suspender actividades y asegurar la integridad de datos y registros |
| Ítem dañado en transporte | Analizar causa, gestionar reemplazo si es posible o retirar sin penalización |
| Envío tardío de resultados | Evaluar inclusión conforme a P-PSEA-06 o gestionar exclusión documentada |
| Número insuficiente de participantes | Activar reglas de continuidad y criterios de valor asignado externo definidos en P-PSEA-06 |

Toda contingencia genera registro en el expediente de la ronda, con la evaluación de impacto, la decisión formal y las acciones tomadas.

---

## 4. Gestión de riesgos por cambios en el diseño

Cualquier cambio significativo en el diseño, la operación o la evaluación de una ronda EA requiere evaluación documentada de riesgos antes de su implementación. Se consideran cambios significativos, entre otros:

1. Modificación del valor asignado o de su método de obtención.
2. Cambio en el estadístico de desempeño.
3. Cambio en σ_pt o en su método de determinación.
4. Cambio en el número de participantes que implique transición entre escenarios de P-PSEA-06.
5. Cambio en el ítem de ensayo, método de generación o condiciones de estabilidad.

La evaluación de riesgos se documenta con la identificación del cambio, el análisis de impacto, los controles propuestos y la aprobación del coordinador EA.

---

## 5. Control documental

### 5.1 Expediente de la ronda

Cada ronda EA genera un expediente que incluye como mínimo:

- Plan de la ronda.
- F-PSEA-01 y DG-PSEA-01 emitidos.
- Evidencias de autorización del personal involucrado.
- Resultados de homogeneidad y estabilidad.
- Base de datos cruda y base depurada.
- Informe preliminar y comentarios recibidos, si aplica.
- Informe final emitido conforme a P-PSEA-07.
- Registro de contingencias y evaluación de riesgos por cambios, cuando aplique.

### 5.2 Control de cambios

Los cambios a este procedimiento se gestionan conforme al sistema de control documental del SGC. Todo cambio significativo en el diseño de un esquema EA requiere evaluación de riesgos documentada conforme a la sección 4 de este procedimiento.

---

## 6. Referencias cruzadas

| Documento | Relación |
|---|---|
| P-PSEA-06 | Define la metodología estadística para x_pt, σ_pt, incertidumbre y puntajes de desempeño. P-PSEA-09 declara qué se planifica y P-PSEA-06 define cómo se sustenta estadísticamente. |
| P-PSEA-07 | Genera el informe de resultados conforme a los criterios definidos en la planificación. |
| P-PSEA-08 | Se activa ante sospecha de colusión o falsificación. |
| P-PSEA-02, P-PSEA-03, P-PSEA-04 y P-PSEA-05 | Procedimientos operativos por analito. |
| F-PSEA-01 | Establece el calendario tipo de la ronda. |
| DG-PSEA-01 | Comunicado detallado a participantes con objetivos, criterios y requisitos. |
| I-PSEA-01 | Instructivo de embalaje, transporte y manipulación del ítem. |

---

| REVISÓ |  | APROBÓ |  |
| --- | :--- | :--- | :--- |
| **ROL** | Profesional de Calidad | **ROL** | Coordinador EA |
| **FECHA** |  | **FECHA** |  |
