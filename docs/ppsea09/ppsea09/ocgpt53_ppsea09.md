# P-PSEA-09 - Planificacion y Preparacion de Rondas de Ensayo de Aptitud

## 1. Informacion general del procedimiento

**Objetivo**  
Establecer las directrices, responsabilidades y actividades para planificar y preparar las rondas de ensayos de aptitud (EA) de gases contaminantes criterio del Laboratorio CALAIRE, en cumplimiento de ISO/IEC 17043:2023 e ISO 13528:2022.

**Alcance**  
Aplica a la etapa previa a la ejecucion de cada ronda EA para SO2, NO/NO2, CO y O3: definicion del esquema, requisitos de participacion, gestion de recursos, riesgos, control del item de ensayo, comunicacion con participantes y criterios de evaluacion.

**Definiciones clave**  
- `x_pt`: valor asignado del mensurando en el EA.  
- `sigma_pt`: desviacion estandar para evaluacion de aptitud.  
- `u(x_pt)`: incertidumbre estandar del valor asignado por caracterizacion estadistica.  
- `u(x_pt,def)`: incertidumbre estandar definitiva del valor asignado, incluyendo homogeneidad y estabilidad.

**Documentos de referencia**  
- ISO/IEC 17043:2023.  
- ISO 13528:2022.  
- P-PSEA-02, P-PSEA-03, P-PSEA-04, P-PSEA-05 (procedimientos por analito).  
- P-PSEA-06 (diseno estadistico).  
- P-PSEA-07 (informe de resultados).  
- P-PSEA-08 (gestion de colusion/falsificacion y desviaciones de integridad).  
- F-PSEA-01 (calendario tipo).  
- I-PSEA-01 (instructivo de embalaje y transporte).  
- DG-PSEA-01 (comunicacion detallada del EA).

## 2. Informacion especifica del procedimiento (ISO/IEC 17043:2023, 7.2.1.3 a-u)

### a) Personal involucrado y autorizacion formal (6.2.6)
Se definen los roles minimos para cada ronda:
- Coordinador EA.
- Estadistico/experto tecnico.
- Ingeniero operativo.
- Experto tecnico en calidad del aire.
- Profesional de calidad.
- Profesional de proyectos/comunicaciones.

Toda persona que intervenga en actividades criticas debe contar con autorizacion formal, vigente y trazable para:
1. Planificar esquemas de EA.
2. Evaluar homogeneidad, estabilidad, valor asignado e incertidumbre.
3. Evaluar desempeno de participantes.
4. Emitir opiniones e interpretaciones tecnicas.
5. Revisar y autorizar informes EA.

### b) Actividades de proveedores externos
Las actividades subcontratables (por ejemplo, calibraciones especificas, transporte, logistica especializada o suministro de MRC) se controlan por evaluacion y aprobacion previa del proveedor.  
No se subcontratan decisiones nucleo del esquema: planificacion tecnica, definicion de criterios de evaluacion, seleccion final del valor asignado, evaluacion de desempeno y autorizacion del informe.

### c) Criterios de participacion
Cada convocatoria define y solicita evidencia de:
- Metodo de medicion aplicable al alcance del EA.
- Competencia tecnica del personal operador.
- Equipos calibrados y en estado operativo.
- Capacidad de reporte en unidades y formatos establecidos.
- Incertidumbre de medicion cuando aplique al estadistico de desempeno seleccionado.

### d) Numero y tipo de participantes
La capacidad operativa por ronda se define por infraestructura y seguridad del laboratorio.  
Para esquemas por consenso, se considera como referencia minima `p >= 12` para robustez estadistica; para el criterio `u(x_pt) <= 0.3 sigma_pt`, la referencia operativa es `p >= 17` cuando `s* ~= sigma_pt`.  
En `p < 12`, se prioriza valor asignado externo y `sigma_pt` prescriptiva; la evaluacion se ejecuta con estadisticos que incorporen incertidumbre (`z'`, `zeta` o `En`) segun P-PSEA-06.

### e) Actividades y resultados esperados
El plan de ronda incluye:
- instalacion y verificacion operativa,
- ejecucion de mediciones,
- recepcion de resultados y metadatos,
- validacion tecnica y estadistica,
- emision de informe.

El resultado esperado es un conjunto de datos validos y trazables que permita una evaluacion tecnicamente defendible.

### f) Rango esperado de valores
Se definen rangos generales por analito para la planificacion logistica.  
Las concentraciones objetivo de cada ronda se fijan en DG-PSEA-01 y en la comunicacion especifica, con respaldo de resultados de homogeneidad/estabilidad del lote.

### g) Fuentes potenciales de error y gestion de riesgos
La planificacion integra la gestion de riesgos del SGC y considera, como minimo:
- inestabilidad/homogeneidad insuficiente del item,
- fugas o alteraciones neumaticas,
- fallas electricas o ambientales,
- sesgos instrumentales,
- errores de transcripcion o reporte,
- riesgos de imparcialidad e integridad de datos.

Todo cambio significativo en diseno, operacion o evaluacion exige evaluacion de riesgos y aprobacion documentada antes de su implementacion.

### h) Requisitos tecnicos y de control
Se exige:
- uso de materiales/equipos de referencia con trazabilidad demostrable,
- hojas de vida y certificados vigentes de equipos criticos,
- control de condiciones ambientales y operativas,
- evidencias de pruebas de homogeneidad y estabilidad,
- conservacion de registros primarios y reportes tecnicos.

### i) Prevencion de colusion
Se aplican controles de integridad:
- codificacion unica de participantes,
- segregacion de informacion sensible,
- restriccion de interaccion no controlada durante mediciones,
- declaracion de confidencialidad y no colusion.

Ante sospecha de colusion o falsificacion se activa P-PSEA-08.

### j) Informacion a suministrar y cronograma
Antes de la ejecucion se entrega:
- cronograma F-PSEA-01,
- comunicacion tecnica DG-PSEA-01,
- instructivo I-PSEA-01,
- requisitos de reporte y criterios de evaluacion.

### k) Frecuencia y plazos de reporte
La frecuencia de rondas y las ventanas de reporte se definen por el programa anual y se formalizan en F-PSEA-01 y DG-PSEA-01.

### l) Metodos y procedimientos
Se especifican los metodos admisibles por analito, condiciones operativas minimas y criterios de aceptacion de datos, con referencia a P-PSEA-02..05 e I-PSEA-01.

### m) Pruebas de homogeneidad y estabilidad
Se ejecutan y documentan conforme a ISO 13528:2022 y P-PSEA-06 antes de consolidar la evaluacion del desempeno.

### n) Formatos e informes
El registro de resultados se realiza en formatos controlados y debe contener:
- resultado reportado,
- unidad de medida,
- incertidumbre (cuando aplique),
- metodo declarado,
- observaciones de validez tecnica.

### o) Analisis estadistico
La planificacion estadistica debe declarar:
- jerarquia de seleccion de `x_pt`,
- jerarquia de seleccion de `sigma_pt`,
- regla de seleccion de estadistico de desempeno (`z`, `z'`, `zeta`, `En`),
- criterios de exclusion y tratamiento de resultados no validos.

El detalle metodologico se establece en P-PSEA-06.

### p) Trazabilidad e incertidumbre
La trazabilidad del valor asignado se establece por referencia externa o modelo metrologico justificable.  
La incertidumbre definitiva se consolida como:

`u(x_pt,def) = sqrt( u(x_pt)^2 + u_hom^2 + u_stab^2 )`

### q) Tratamiento de diferentes metodos de medicion
Cuando participen metodos distintos, se define previamente si la evaluacion sera:
- conjunta (metodos equivalentes), o
- segmentada por familias metodologicas.

La decision y su justificacion deben quedar registradas en el expediente de ronda.

### r) Criterios de desempeno
La seleccion del estadistico sigue P-PSEA-06. Interpretacion institucional:
- `|z|, |z'|, |zeta| <= 2`: satisfactorio.
- `2 < |score| < 3`: cuestionable.
- `|score| >= 3`: no satisfactorio.
- `|En| <= 1`: satisfactorio.
- `|En| > 1`: no satisfactorio.

### s) Informes y comunicacion de resultados
La emision del informe borrador y final se ejecuta segun P-PSEA-07, incluyendo trazabilidad de versiones, resolucion de comentarios y cierre tecnico.

### t) Publicacion y confidencialidad
La identidad y los resultados individuales se manejan bajo politica de confidencialidad del SGC.  
La comunicacion externa de resultados se realiza de forma codificada o agregada, salvo obligacion legal o regulatoria documentada.

### u) Contingencias
La planificacion define escenarios de contingencia para:
- falla del item,
- indisponibilidad de equipos criticos,
- alteraciones de seguridad o infraestructura,
- desviaciones mayores del plan.

Toda contingencia genera registro, evaluacion de impacto y decision formal de continuidad, repeticion o cancelacion de la ronda.

## 3. Referencia cruzada con P-PSEA-06

P-PSEA-09 define **que** debe planificarse y controlarse en la ronda.  
P-PSEA-06 define **como** se ejecuta la base estadistica para `x_pt`, `sigma_pt`, incertidumbre y evaluacion de desempeno.
