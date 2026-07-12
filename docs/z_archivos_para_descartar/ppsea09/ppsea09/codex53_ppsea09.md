# P-PSEA-09 - Planificación y Preparación de Rondas de Ensayo de Aptitud

## 1. Información general del procedimiento

**Objetivo**  
Establecer las directrices, responsabilidades y actividades para planificar y preparar las rondas de ensayos de aptitud (EA) de gases contaminantes criterio del Laboratorio CALAIRE, en cumplimiento de ISO/IEC 17043:2023 e ISO 13528:2022.

**Alcance**  
Aplica a la etapa previa a la ejecución de cada ronda EA para SO2, NO/NO2, CO y O3: definición del esquema, requisitos de participación, gestión de recursos, riesgos, control del ítem de ensayo, comunicación con participantes y criterios de evaluación.

**Definiciones clave**  
- `x_pt`: valor asignado del mensurando en el EA.  
- `sigma_pt`: desviación estándar para evaluación de aptitud.  
- `u(x_pt)`: incertidumbre estándar del valor asignado por caracterización estadística.  
- `u(x_pt,def)`: incertidumbre estándar definitiva del valor asignado, incluyendo homogeneidad y estabilidad.

**Documentos de referencia**  
- ISO/IEC 17043:2023.  
- ISO 13528:2022.  
- P-PSEA-02, P-PSEA-03, P-PSEA-04, P-PSEA-05 (procedimientos por analito).  
- P-PSEA-06 (diseño estadístico).  
- P-PSEA-07 (informe de resultados).  
- P-PSEA-08 (gestión de colusión/falsificación y desviaciones de integridad).  
- F-PSEA-01 (calendario tipo).  
- I-PSEA-01 (instructivo de embalaje y transporte).  
- DG-PSEA-01 (comunicación detallada del EA).

## 2. Información específica del procedimiento (ISO/IEC 17043:2023, 7.2.1.3 a-u)

### a) Personal involucrado y autorización formal (6.2.6)
Se definen los roles mínimos para cada ronda:
- Coordinador EA.
- Estadístico/experto técnico.
- Ingeniero operativo.
- Experto técnico en calidad del aire.
- Profesional de calidad.
- Profesional de proyectos/comunicaciones.

Toda persona que intervenga en actividades críticas debe contar con autorización formal, vigente y trazable para:
1. Planificar esquemas de EA.
2. Evaluar homogeneidad, estabilidad, valor asignado e incertidumbre.
3. Evaluar desempeño de participantes.
4. Emitir opiniones e interpretaciones técnicas.
5. Revisar y autorizar informes EA.

### b) Actividades de proveedores externos
Las actividades subcontratables (p. ej., calibraciones específicas, transporte, logística especializada o suministro de MRC) se controlan por evaluación y aprobación previa del proveedor.  
No se subcontratan decisiones núcleo del esquema: planificación técnica, definición de criterios de evaluación, selección final del valor asignado, evaluación de desempeño y autorización del informe.

### c) Criterios de participación
Cada convocatoria define y solicita evidencia de:
- Método de medición aplicable al alcance del EA.
- Competencia técnica del personal operador.
- Equipos calibrados y en estado operativo.
- Capacidad de reporte en unidades y formatos establecidos.
- Incertidumbre de medición cuando aplique al estadístico de desempeño seleccionado.

### d) Número y tipo de participantes
La capacidad operativa por ronda se define por infraestructura y seguridad del laboratorio.  
Para esquemas por consenso, se considera como referencia mínima `p >= 12` para robustez estadística; para el criterio `u(x_pt) <= 0.3 sigma_pt`, la referencia operativa es `p >= 17` cuando `s* ≈ sigma_pt`.  
En `p < 12`, se prioriza valor asignado externo y `sigma_pt` prescriptiva; la evaluación se ejecuta con estadísticos que incorporen incertidumbre (`z'`, `zeta` o `En`) según P-PSEA-06.

### e) Actividades y resultados esperados
El plan de ronda incluye:
- instalación y verificación operativa,
- ejecución de mediciones,
- recepción de resultados y metadatos,
- validación técnica y estadística,
- emisión de informe.

El resultado esperado es un conjunto de datos válidos y trazables que permita una evaluación técnicamente defendible.

### f) Rango esperado de valores
Se definen rangos generales por analito para la planificación logística.  
Las concentraciones objetivo de cada ronda se fijan en DG-PSEA-01 y en la comunicación específica, con respaldo de resultados de homogeneidad/estabilidad del lote.

### g) Fuentes potenciales de error y gestión de riesgos
La planificación integra la gestión de riesgos del SGC y considera, como mínimo:
- inestabilidad/homogeneidad insuficiente del ítem,
- fugas o alteraciones neumáticas,
- fallas eléctricas o ambientales,
- sesgos instrumentales,
- errores de transcripción o reporte,
- riesgos de imparcialidad e integridad de datos.

Todo cambio significativo en diseño, operación o evaluación exige evaluación de riesgos y aprobación documentada antes de su implementación.

### h) Requisitos técnicos y de control
Se exige:
- uso de materiales/equipos de referencia con trazabilidad demostrable,
- hojas de vida y certificados vigentes de equipos críticos,
- control de condiciones ambientales y operativas,
- evidencias de pruebas de homogeneidad y estabilidad,
- conservación de registros primarios y reportes técnicos.

### i) Prevención de colusión
Se aplican controles de integridad:
- codificación única de participantes,
- segregación de información sensible,
- restricción de interacción no controlada durante mediciones,
- declaración de confidencialidad y no colusión.

Ante sospecha de colusión o falsificación se activa P-PSEA-08.

### j) Información a suministrar y cronograma
Antes de la ejecución se entrega:
- cronograma F-PSEA-01,
- comunicación técnica DG-PSEA-01,
- instructivo I-PSEA-01,
- requisitos de reporte y criterios de evaluación.

### k) Frecuencia y plazos de reporte
La frecuencia de rondas y las ventanas de reporte se definen por el programa anual y se formalizan en F-PSEA-01 y DG-PSEA-01.

### l) Métodos y procedimientos
Se especifican los métodos admisibles por analito, condiciones operativas mínimas y criterios de aceptación de datos, con referencia a P-PSEA-02..05 e I-PSEA-01.

### m) Pruebas de homogeneidad y estabilidad
Se ejecutan y documentan conforme a ISO 13528:2022 y P-PSEA-06 antes de consolidar la evaluación del desempeño.

### n) Formatos e informes
El registro de resultados se realiza en formatos controlados y debe contener:
- resultado reportado,
- unidad de medida,
- incertidumbre (cuando aplique),
- método declarado,
- observaciones de validez técnica.

### o) Análisis estadístico
La planificación estadística debe declarar:
- jerarquía de selección de `x_pt`,
- jerarquía de selección de `sigma_pt`,
- regla de selección de estadístico de desempeño (`z`, `z'`, `zeta`, `En`),
- criterios de exclusión y tratamiento de resultados no válidos.

El detalle metodológico se establece en P-PSEA-06.

### p) Trazabilidad e incertidumbre
La trazabilidad del valor asignado se establece por referencia externa o modelo metrológico justificable.  
La incertidumbre definitiva se consolida como:

`u(x_pt,def) = sqrt( u(x_pt)^2 + u_hom^2 + u_stab^2 )`

### q) Tratamiento de diferentes métodos de medición
Cuando participen métodos distintos, se define previamente si la evaluación será:
- conjunta (métodos equivalentes), o
- segmentada por familias metodológicas.

La decisión y su justificación deben quedar registradas en el expediente de ronda.

### r) Criterios de desempeño
La selección del estadístico sigue P-PSEA-06. Interpretación institucional:
- `|z|, |z'|, |zeta| <= 2`: satisfactorio.
- `2 < |score| < 3`: cuestionable.
- `|score| >= 3`: no satisfactorio.
- `|En| <= 1`: satisfactorio.
- `|En| > 1`: no satisfactorio.

### s) Informes y comunicación de resultados
La emisión del informe borrador y final se ejecuta según P-PSEA-07, incluyendo trazabilidad de versiones, resolución de comentarios y cierre técnico.

### t) Publicación y confidencialidad
La identidad y los resultados individuales se manejan bajo política de confidencialidad del SGC.  
La comunicación externa de resultados se realiza de forma codificada o agregada, salvo obligación legal o regulatoria documentada.

### u) Contingencias
La planificación define escenarios de contingencia para:
- falla del ítem,
- indisponibilidad de equipos críticos,
- alteraciones de seguridad o infraestructura,
- desviaciones mayores del plan.

Toda contingencia genera registro, evaluación de impacto y decisión formal de continuidad, repetición o cancelación de la ronda.

## 3. Referencia cruzada con P-PSEA-06

P-PSEA-09 define **qué** debe planificarse y controlarse en la ronda.  
P-PSEA-06 define **cómo** se ejecuta la base estadística para `x_pt`, `sigma_pt`, incertidumbre y evaluación de desempeño.

