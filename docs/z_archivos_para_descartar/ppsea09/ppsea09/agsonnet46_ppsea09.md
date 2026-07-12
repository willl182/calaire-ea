# P-PSEA-09 — Planificación y Preparación de Rondas de Ensayo de Aptitud para Gases Contaminantes Criterio

**Código:** P-PSEA-09  
**Versión:** 3.0  
**Fecha de emisión:** 2026-03-22  
**Referencia normativa:** ISO/IEC 17043:2023, ISO 13528:2022  
**Procedimientos relacionados:** P-PSEA-02, P-PSEA-03, P-PSEA-04, P-PSEA-05, P-PSEA-06, P-PSEA-07, P-PSEA-08  

---

## 1. Información general del procedimiento

### 1.1 Objetivo

Establecer las directrices, responsabilidades y actividades para planificar y preparar las rondas de ensayos de aptitud (EA) de gases contaminantes criterio —dióxido de azufre (SO₂), óxidos de nitrógeno (NO/NO₂), monóxido de carbono (CO) y ozono (O₃)— organizadas por el Laboratorio CALAIRE, garantizando el cumplimiento de los requisitos de ISO/IEC 17043:2023 e ISO 13528:2022 y asegurando la validez, imparcialidad y trazabilidad de los resultados.

### 1.2 Alcance

Este procedimiento aplica a todas las etapas de planificación previas al inicio de cada ronda EA: definición de objetivos, diseño del esquema, selección y gestión de participantes, control de calidad de ítems de ensayo, gestión de riesgos, comunicación operativa y criterios de evaluación. Abarca las actividades realizadas en las instalaciones del Laboratorio CALAIRE y las interacciones con participantes y proveedores externos.

### 1.3 Definiciones

| Término | Definición |
|---|---|
| Ensayo de aptitud (EA) | Evaluación del desempeño de un laboratorio mediante comparaciones interlaboratorios, conforme a ISO/IEC 17043:2023. |
| Ítem de ensayo | Atmósfera de gas contaminante criterio generada dinámicamente a partir de mezcla gaseosa certificada, patrón fotométrico o referencia trazable equivalente. |
| Valor asignado (x_pt) | Valor atribuido al mensurando del EA, determinado conforme a P-PSEA-06. |
| σ_pt | Desviación estándar para la evaluación de la aptitud; criterio de dispersión preestablecido contra el cual se juzga el desempeño de cada participante. |
| u(x_pt) | Incertidumbre estándar del valor asignado por la vía de caracterización. |
| u(x_pt,def) | Incertidumbre estándar definitiva del valor asignado, integrada con las contribuciones por homogeneidad y estabilidad: u(x_pt,def) = √[u(x_pt)² + u_hom² + u_stab²]. |
| Participante | Laboratorio que reporta resultados en el EA conforme a los criterios establecidos. |
| p | Número de participantes válidos incluidos en el análisis estadístico definitivo. |

### 1.4 Documentos de referencia

- ISO/IEC 17043:2023 — Requisitos generales para proveedores de ensayos de aptitud.
- ISO 13528:2022 — Métodos estadísticos para EA por comparación interlaboratorio.
- ISO/IEC 17025:2017 — Requisitos generales para laboratorios de ensayo y calibración.
- ISO 6142-1:2015 — Análisis de gases. Preparación de mezclas gaseosas de referencia. Método gravimétrico de presión.
- ISO 17034:2016 — Requisitos generales para la competencia de productores de materiales de referencia.
- P-PSEA-06 — Diseño estadístico para EA: métodos para x_pt, σ_pt, incertidumbre y puntajes.
- P-PSEA-07 — Elaboración de informe de resultados de EA.
- P-PSEA-08 — Gestión de colusión, falsificación y desviaciones de integridad en EA.
- P-PSEA-02 a P-PSEA-05 — Procedimientos operativos por analito (NO/NO₂, CO, O₃, SO₂).
- F-PSEA-01 — Calendario tipo de rondas EA.
- DG-PSEA-01 — Protocolo detallado de participación en EA de gases contaminantes criterio.
- I-PSEA-01 — Instructivo de embalaje, transporte y manipulación del ítem de ensayo.

---

## 2. Roles, responsabilidades y autorización del personal

### 2.1 Roles y responsabilidades

| Rol | Responsabilidad principal |
|---|---|
| Coordinador EA | Aprueba el diseño del esquema, verifica la disponibilidad de recursos y autoriza la emisión de resultados. Aprueba toda continuidad, reprogramación o cancelación ante contingencia. |
| Estadístico / Experto técnico | Diseña el plan estadístico conforme a P-PSEA-06, valida los criterios de desempeño y revisa la coherencia técnica de los resultados. |
| Ingeniero operativo | Lidera la preparación de ítems, controla las condiciones ambientales y coordina el montaje de la infraestructura de generación. |
| Experto técnico en calidad del aire | Define los rangos de concentración, verifica la trazabilidad metrológica y valida la aplicabilidad de los métodos de referencia. |
| Profesional de calidad | Garantiza el cumplimiento del SGC, la imparcialidad, la confidencialidad y la trazabilidad documental. |
| Profesional de proyectos / Comunicaciones | Gestiona la comunicación con participantes, la convocatoria, el envío de formatos y el seguimiento de reportes. |

### 2.2 Autorización formal del personal (ISO/IEC 17043:2023, §6.2.6)

El Laboratorio CALAIRE mantiene autorización formal y evidencia de competencia documentada para el personal que ejecuta las siguientes actividades críticas:

1. Planificación de esquemas de EA.
2. Evaluación de homogeneidad, estabilidad, valor asignado e incertidumbre.
3. Evaluación del desempeño de participantes.
4. Emisión de opiniones e interpretaciones técnicas.
5. Revisión y autorización de informes EA.

Las autorizaciones se registran individualmente en los perfiles de cargo y se revisan en cada ciclo de auditoría interna del SGC. Ninguna de estas actividades podrá ser ejecutada por personal sin autorización formal vigente.

### 2.3 Actividades no subcontratables (ISO/IEC 17043:2023, §6.4.1)

Las siguientes actividades son de ejecución interna exclusiva y no pueden ser externalizadas en ninguna circunstancia:

- Diseño y planificación del esquema EA.
- Evaluación del desempeño de participantes.
- Selección final del valor asignado y criterios de evaluación.
- Revisión y autorización de informes EA.

Las actividades subcontratables (calibraciones especializadas, logística de transporte, suministro de mezclas gaseosas por proveedores evaluados) se controlan mediante evaluación documentada del proveedor conforme al procedimiento de compras y control de proveedores del SGC, y están sujetas a acuerdos de confidencialidad legalmente vinculantes.

---

## 3. Planificación específica de la ronda (ISO/IEC 17043:2023, §7.2.1.3)

La planificación de cada ronda EA se documenta antes de su inicio, siguiendo los literales a) a u) del presente apartado, en concordancia con el §7.2.1.3 de ISO/IEC 17043:2023.

### 3.1 a) Personal involucrado en el diseño y la operación

Se identifican y documentan todos los roles involucrados en cada ronda, con sus nombres, evidencias de competencia y autorización formal vigente conforme a la sección 2.2 de este procedimiento. El expediente de la ronda registra las firmas de aceptación de responsabilidades de cada involucrado.

### 3.2 b) Actividades de proveedores externos

Las actividades ejecutadas por proveedores externos se documentan con: identificación del proveedor, descripción del servicio subcontratado, evidencia de evaluación de competencia, acuerdos de confidencialidad vigentes y mecanismo de supervisión aplicable. El coordinador EA revisa y aprueba la idoneidad de cada proveedor antes de la contratación. Ninguna de las actividades listadas en la sección 2.3 puede ser objeto de subcontratación.

### 3.3 c) Criterios de participación

La convocatoria EA define y solicita evidencia previa de los siguientes criterios para admitir la participación:

1. Método de medición aplicable al alcance del EA, conforme a normas de referencia EN 14211, EN 14212, EN 14625 o EN 14626, o método equivalente US-EPA debidamente declarado.
2. Competencia técnica del personal operador, demostrada mediante formación documentada.
3. Equipos calibrados y en estado operativo, con certificados de calibración vigentes y trazabilidad metrológica demostrable.
4. Capacidad de reporte en las unidades y formatos establecidos en DG-PSEA-01.
5. Declaración de incertidumbre de medición cuando aplique al estadístico de desempeño seleccionado conforme a P-PSEA-06.

Los criterios se comunican en la convocatoria formal (DG-PSEA-01) junto con la política de confidencialidad del laboratorio.

### 3.4 d) Número y tipo de participantes esperados

La capacidad operativa de cada ronda se define según la infraestructura disponible en las instalaciones del Laboratorio CALAIRE. El diseño estadístico establece en P-PSEA-06 el número mínimo viable según el método seleccionado para x_pt y σ_pt.

**Guía numérica de suficiencia:**

| Número de participantes válidos (p) | Enfoque estadístico aplicable |
|---|---|
| p ≥ 17 | Consenso robusto (Algoritmo A); u(x_pt) ≤ 0,3 σ_pt verificable con s* ≈ σ_pt. |
| 12 ≤ p < 17 | Consenso robusto viable; verificar que u(x_pt) ≤ 0,3 σ_pt antes de usar z. |
| 6 ≤ p < 12 | Contingencia estadística: valor asignado externo o prescriptivo; σ_pt prescriptiva; puntaje z', ζ o En. |
| p < 6 | No se aplica consenso como base de desempeño. Valor asignado externo, σ_pt prescriptiva y estadístico En o z'. |

La planificación registra la justificación técnica del número esperado y los criterios de continuidad ante inscripción inferior al mínimo viable. En todos los escenarios con p < 12, se aplican las reglas definidas en el §8 de P-PSEA-06.

### 3.5 e) Actividades y resultados esperados de los participantes

El plan de ronda incluye la secuencia de actividades esperadas de los participantes:

1. Instalación y verificación operativa de los instrumentos conforme a I-PSEA-01.
2. Ejecución de mediciones dentro de la ventana de reporte establecida en F-PSEA-01.
3. Reporte de resultados en el formato y las unidades definidas en DG-PSEA-01.
4. Declaración de incertidumbre asociada, cuando el estadístico de desempeño lo requiera.
5. Asistencia a la reunión de aclaraciones previa, cuando esté programada.

El resultado esperado es un conjunto de datos válidos, trazables y comparables que permita una evaluación técnicamente defendible del desempeño de cada participante.

### 3.6 f) Rango esperado de valores

Se definen rangos generales de concentración por analito para la planificación logística. Las concentraciones objetivo específicas se fijan en DG-PSEA-01 y se ajustan en función de los resultados de los estudios de homogeneidad y estabilidad del lote.

Los rangos se seleccionan considerando:

- Los umbrales de evaluación establecidos en la normativa ambiental aplicable (Directiva 2008/50/CE, estándares IDEAM).
- Las concentraciones típicas de la red de monitoreo.
- Los rangos operativos de los métodos de referencia EN 14211, EN 14212, EN 14625 y EN 14626.

Las concentraciones máximas del ítem de ensayo son orientativas. La comunicación detallada con las concentraciones objetivo específicas se realiza a través de DG-PSEA-01.

### 3.7 g) Fuentes potenciales de error y gestión de riesgos

La planificación integra la gestión de riesgos del SGC en cumplimiento de ISO/IEC 17043:2023 §7.2.1.2. Se identifican y evalúan las siguientes fuentes potenciales de error antes de cada ronda:

| Fuente de error | Tipo de riesgo | Control de mitigación |
|---|---|---|
| Inestabilidad o heterogeneidad del ítem de ensayo | Técnico | Estudios de homogeneidad y estabilidad previos a la ronda conforme a P-PSEA-06. |
| Fugas o alteraciones neumáticas | Técnico | Pruebas de hermeticidad; líneas de teflón inerte sin fugas. |
| Errores de calibración o verificación de equipos | Técnico | Certificados vigentes; verificación con patrón de transferencia trazable. |
| Fallas ambientales (temperatura, humedad, presión) | Operativo | Monitoreo continuo; protocolos de contingencia y equipos de respaldo. |
| Errores de transcripción o reporte | Operativo | Validación de datos en recepción; formato controlado. |
| Colusión o falsificación de resultados | Ético / Estadístico | Codificación única; segregación de información; P-PSEA-08. |
| Número insuficiente de participantes | Estadístico | Criterios de continuidad; valor asignado externo; σ_pt prescriptiva (P-PSEA-06). |

**Control de cambios significativos:** Todo cambio significativo en el diseño, la operación o los criterios de evaluación de una ronda exige la evaluación documentada de riesgos y la aprobación explícita del coordinador EA antes de su implementación (ISO/IEC 17043:2023, §7.2.1.2).

### 3.8 h) Requisitos técnicos y de control

Se exigen los siguientes requisitos técnicos para la preparación y control de los ítems de ensayo:

1. Uso de mezclas gaseosas de referencia o materiales de referencia con trazabilidad metrológica demostrable al SI.
2. Hojas de vida y certificados de calibración vigentes de los equipos críticos utilizados en la generación y verificación del ítem de ensayo.
3. Control de condiciones ambientales y operativas (temperatura, humedad, presión y flujo) conforme a los límites establecidos en los procedimientos operativos.
4. Generadores de ozono con fotómetro de nivel 2 y manómetros calibrados; manifold y líneas de teflón inertes.
5. Evidencias trazables de las pruebas de homogeneidad y estabilidad del lote, ejecutadas conforme a P-PSEA-06.
6. Conservación de registros primarios y reportes técnicos de cada ronda como parte del expediente.

El aplicativo estadístico de CALAIRE constituye la evidencia institucional de las pruebas de homogeneidad y estabilidad. Cada ronda genera un informe técnico que referencia los datos y resultados de dichas pruebas.

### 3.9 i) Prevención de colusión y falsificación

Se aplican los siguientes controles de integridad en cada ronda:

1. Asignación de un código único e irrepetible a cada participante, cuya correspondencia se mantiene en reserva bajo custodia exclusiva del profesional de calidad.
2. Segregación de la información sensible: los participantes no acceden a la identidad de los demás ni a los resultados ajenos durante el período de mediciones.
3. Restricción de la interacción no controlada entre participantes; los displays de los instrumentos solo son visibles desde sala externa mediante escritorio remoto gestionado por el coordinador.
4. Declaración escrita de confidencialidad y no colusión, firmada por cada participante y sus representantes en DG-PSEA-01.
5. Revisión de patrones estadísticos sospechosos por parte del estadístico, conforme a los criterios de P-PSEA-06.

Ante sospecha fundada de colusión o falsificación, se activa el procedimiento P-PSEA-08.

### 3.10 j) Información a suministrar y cronograma

Antes del inicio de la ronda, el Laboratorio CALAIRE entrega a cada participante a través de DG-PSEA-01 los siguientes documentos:

1. Calendario tipo (F-PSEA-01) con fechas de envío/acceso, ventanas de medición y fecha límite de reporte.
2. Comunicación técnica detallada (DG-PSEA-01) con: objetivos, alcance, analito(s), concentraciones objetivo orientativas, método(s) admisibles, condiciones operativas, requisitos de reporte e incertidumbre, y criterios de evaluación de desempeño.
3. Instructivo de embalaje y transporte (I-PSEA-01) con instrucciones de manipulación, conexión y condiciones de seguridad.
4. Declaración de la política de confidencialidad, acuerdo de no colusión y condiciones de retención documental.

La duración típica de la etapa de medición es de 3 a 4 días hábiles, incluyendo instalación, calibraciones y mediciones.

### 3.11 k) Frecuencia y plazos de reporte

La frecuencia de rondas y las ventanas de reporte se definen en el programa anual y se formalizan en F-PSEA-01. Los plazos específicos comunicados a los participantes incluyen:

- Fecha estimada de disponibilidad del ítem de ensayo.
- Fecha de envío o acceso al ítem.
- Fecha límite de recepción de resultados.
- Fecha prevista de emisión del informe preliminar y del informe final.

### 3.12 l) Métodos y procedimientos

Se especifican los métodos admisibles por analito:

| Analito | Norma de método | Técnica de medición |
|---|---|---|
| NO/NO₂ | EN 14211:2012 | Quimioluminiscencia |
| SO₂ | EN 14212:2012 | Fluorescencia UV |
| O₃ | EN 14625:2012 | Fotometría UV |
| CO | EN 14626:2012 | Espectroscopia infrarroja no dispersiva (NDIR) |

El ensayo de aptitud se diseña para métodos US-EPA y europeos equivalentes. No aplica para métodos manuales ni métodos de la Unión Europea cuya equivalencia con los métodos de referencia no haya sido demostrada. Las condiciones operativas mínimas, los criterios de aceptación de datos y los requisitos de incertidumbre se establecen en DG-PSEA-01 e I-PSEA-01.

### 3.13 m) Pruebas de homogeneidad y estabilidad

Las pruebas de homogeneidad y estabilidad se ejecutan y documentan conforme a ISO 13528:2022 §6.1 y P-PSEA-06, posterior al envasado o acondicionamiento final de los ítems de ensayo y antes de la consolidación del análisis estadístico de desempeño.

Los criterios de aceptación, en función de la σ_pt del esquema, son:

- **Homogeneidad:** la desviación estándar entre unidades (s_s) debe satisfacer s_s < 0,3 σ_pt.
- **Estabilidad:** el cambio absoluto (δ) entre el valor inicial y el final de la ventana de ronda debe satisfacer |δ| < 0,3 σ_pt.

Cuando alguno de estos criterios no se cumple, la contribución correspondiente se incorpora a u(x_pt,def) mediante u_hom o u_stab conforme a P-PSEA-06. El detalle del modelo de cálculo se establece en dicho procedimiento.

### 3.14 n) Formatos de reporte

El registro de resultados se realiza en el formato controlado establecido para la ronda. El formato debe contener como mínimo:

1. Código de identificación del participante.
2. Resultado reportado con la unidad de medida normalizada (nmol/mol, μmol/mol, ppb o ppm).
3. Incertidumbre declarada cuando aplique al estadístico de desempeño seleccionado.
4. Método de medición declarado.
5. Fecha de medición.
6. Observaciones de validez técnica.

El formato es validado técnicamente antes de su emisión. El reporte se realiza mediante plantillas electrónicas controladas, en cumplimiento de P-PSEA-07.

### 3.15 o) Análisis estadístico

El plan estadístico de cada ronda declara, conforme a P-PSEA-06:

1. **Jerarquía de selección del valor asignado (x_pt):** valor formulado (1.°) > material de referencia certificado (2.°) > laboratorio de referencia (3.°) > consenso de expertos (4.°) > consenso de participantes (5.°, solo si p ≥ 12). Véase §3.4 de P-PSEA-06.
2. **Jerarquía de selección de σ_pt:** prescriptivo/regulatorio (1.°) > aptitud para el propósito (2.°) > datos históricos robustos (3.°) > modelo predictivo (4.°) > modelo metrológico (5.°) > estimación robusta de participantes (6.°, solo si p ≥ 12). Véase §3.5 de P-PSEA-06.
3. **Regla de selección del estadístico de desempeño:** árbol de decisión basado en u(x_pt) ≤ 0,3 σ_pt y en si los participantes declaran incertidumbre. El estadístico seleccionado es z, z', ζ o En conforme al §5 de P-PSEA-06.
4. **Criterios de exclusión y tratamiento de resultados no válidos:** véase §6 de P-PSEA-06.

El detalle metodológico completo se establece en la versión vigente de P-PSEA-06. El plan de la ronda registra la versión de P-PSEA-06 aplicable y el método seleccionado para x_pt y σ_pt.

### 3.16 p) Trazabilidad e incertidumbre del valor asignado

La trazabilidad del valor asignado se establece por una de las siguientes vías, en orden de preferencia:

1. **Valor formulado gravimétricamente:** mezcla gaseosa preparada conforme a ISO 6142-1, con trazabilidad a patrones de masa del SI.
2. **Material de referencia certificado (MRC):** valor certificado con trazabilidad a un NMI o laboratorio de referencia acreditado (ISO 17034).
3. **Laboratorio de referencia:** valor de un laboratorio competente con trazabilidad demostrada al SI.

La incertidumbre definitiva del valor asignado integra todas las contribuciones:

`u(x_pt,def) = √[ u(x_pt)² + u_hom² + u_stab² ]`

Cada componente —u(x_pt), u_hom y u_stab— se calcula conforme a P-PSEA-06. El presupuesto completo de incertidumbre se documenta en el expediente de la ronda.

### 3.17 q) Tratamiento de diferentes métodos de medición

Cuando la ronda incluya participantes que utilizan diferentes métodos de medición, la planificación define de antemano si la evaluación será:

- **Conjunta:** cuando los métodos son técnicamente equivalentes y se espera que produzcan resultados comparables. Se utiliza un único x_pt y σ_pt para todos los participantes.
- **Segmentada:** cuando los métodos producen resultados que no son comparables entre sí. Se define x_pt, σ_pt y evaluación independiente por familia metodológica.

La decisión y su justificación técnica se registran en el expediente de la ronda antes del inicio de las mediciones.

### 3.18 r) Criterios de desempeño

La selección del estadístico de desempeño (z, z', ζ o En) se realiza conforme al árbol de decisión del §5 de P-PSEA-06, en función del tipo de valor asignado y de la incertidumbre asociada. La interpretación institucional es la siguiente:

| Estadístico | Resultado | Clasificación | Acción recomendada |
|---|---|---|---|
| z, z', ζ | \|score\| ≤ 2 | Satisfactorio | Ninguna intervención requerida. |
| z, z', ζ | 2 < \|score\| < 3 | Cuestionable | Investigación preliminar de posibles causas; seguimiento documentado. |
| z, z', ζ | \|score\| ≥ 3 | No satisfactorio | Investigación obligatoria, acciones correctivas documentadas y seguimiento. |
| En | \|En\| ≤ 1 | Satisfactorio | Compatibilidad metrológica demostrada. |
| En | \|En\| > 1 | No satisfactorio | Incompatibilidad metrológica; requiere investigación y acciones correctivas. |

El criterio de selección del estadístico depende de si u(x_pt) ≤ 0,3 σ_pt y de si los participantes declaran incertidumbre expandida, conforme a P-PSEA-06 §5.

### 3.19 s) Informes y comunicación de resultados

La emisión del informe preliminar, la gestión del período de comentarios y la emisión del informe final se ejecutan conforme a P-PSEA-07. El informe incluye los elementos obligatorios establecidos en ISO/IEC 17043:2023 §7.4.3.2 e ISO 13528:2022, incluyendo: conjunto de datos consolidado, valor asignado con incertidumbre, puntajes de desempeño por participante (clasificación individual), gráficos de desempeño y análisis estadístico descriptivo.

### 3.20 t) Publicación y confidencialidad

La identidad y los resultados individuales de los participantes se manejan bajo la política de confidencialidad del SGC, en cumplimiento de ISO/IEC 17043:2023 §4.2. Las obligaciones de confidencialidad abarcan:

- Todos los datos individuales de los participantes, incluyendo resultados e incertidumbres.
- La identidad de los participantes en la publicación agregada.
- La información técnica del esquema hasta la finalización de la ronda.

La política de confidencialidad y las condiciones de retención documental se comunican a los participantes en DG-PSEA-01 y se formalizan mediante acuerdo escrito previo a la participación. El Laboratorio CALAIRE mantiene acuerdos de confidencialidad con todo el personal y los proveedores involucrados.

La comunicación externa de resultados agregados se realiza codificada, sin identificación individual, salvo obligación legal o regulatoria documentada (por ejemplo, remisión al IDEAM o al organismo acreditador competente).

### 3.21 u) Contingencias

La planificación define los siguientes escenarios de contingencia y las acciones de continuidad aplicables:

| Evento | Acción de continuidad |
|---|---|
| Falla o inestabilidad del ítem de ensayo | Descartar el ítem afectado; gestionar reposición del lote o reprogramar la ronda. Activar la regla de gestión de riesgos §7.2.1.2. |
| Indisponibilidad de equipos críticos | Evaluar impacto técnico; activar equipos de respaldo o reprogramar si es necesario. |
| Alteraciones de seguridad o infraestructura | Suspender actividades; asegurar integridad de datos, registros y muestras. |
| Envío tardío de resultados por un participante | Evaluar conforme a P-PSEA-06 §6 si el resultado puede incluirse; gestionar exclusión documentada si no aplica. |
| Número insuficiente de participantes (p < mínimo viable) | Activar las reglas de P-PSEA-06 §8: valor asignado externo, σ_pt prescriptiva, puntaje z' o En. Documentar las implicaciones estadísticas en el informe. |
| Sospecha de colusión o falsificación | Activar P-PSEA-08. Suspender la emisión de resultados hasta la resolución. |

Toda contingencia genera un registro documentado en el expediente de la ronda, con la evaluación de impacto, la decisión formal y las acciones tomadas. El coordinador EA aprueba formalmente la continuidad, reprogramación o cancelación de la ronda en cada caso.

---

## 4. Control documental

### 4.1 Expediente de la ronda

Cada ronda EA genera un expediente que incluye:

- Plan de la ronda (documento de planificación interno) con fecha de aprobación por el coordinador EA.
- F-PSEA-01 y DG-PSEA-01 emitidos.
- Evidencias de autorización del personal involucrado y evaluación de proveedores.
- Resultados y reportes técnicos de los estudios de homogeneidad y estabilidad (P-PSEA-06).
- Base de datos cruda y base de datos depurada con control de cambios trazable.
- Selección documentada de x_pt y σ_pt con justificación de la jerarquía aplicada.
- Presupuesto de incertidumbre [u(x_pt), u_hom, u_stab, u(x_pt,def)].
- Tabla de puntajes con clasificación por participante.
- Informe preliminar y comentarios recibidos durante el período de revisión.
- Informe final (P-PSEA-07).
- Registro de contingencias, si las hubo.

### 4.2 Control de cambios

Los cambios a este procedimiento se gestionan conforme al sistema de control documental del SGC. Todo cambio significativo en el diseño de un esquema EA en ejecución requiere la evaluación documentada de riesgos y la aprobación formal del coordinador EA, conforme a ISO/IEC 17043:2023 §7.2.1.2.

---

## 5. Referencias cruzadas

| Procedimiento / Documento | Relación funcional |
|---|---|
| P-PSEA-06 | Procedimiento estadístico maestro. Define la metodología para x_pt, σ_pt, incertidumbre y puntajes de desempeño. P-PSEA-09 declara qué se planifica; P-PSEA-06 define cómo se sustenta estadísticamente. |
| P-PSEA-07 | Elabora y emite el informe de resultados con base en los criterios definidos en la planificación. |
| P-PSEA-08 | Se activa ante sospecha o evidencia de colusión, falsificación u otra desviación de integridad. |
| F-PSEA-01 | Formaliza el calendario tipo de cada ronda EA. |
| DG-PSEA-01 | Comunicado detallado a participantes con objetivos, criterios, requisitos de reporte y política de confidencialidad. |
| I-PSEA-01 | Instructivo de embalaje, transporte y manipulación del ítem de ensayo. |
| ISO/IEC 17043:2023 | Norma de referencia primaria para requisitos del proveedor de EA: diseño, planificación, personal, confidencialidad, subcontratación y evaluación. |
| ISO 13528:2022 | Base normativa para todos los métodos estadísticos aplicados en P-PSEA-06. |

---

| REVISÓ |   | APROBÓ |   |
| --- | :--- | :--- | :--- |
| **ROL** |   | **ROL** |   |
| **FECHA** |   | **FECHA** |   |
