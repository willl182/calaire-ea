# Documento explicativo CALAIRE-EA: Ensayos de Aptitud para Gases Contaminantes Criterio

**Proyecto:** [[CALAIRE-EA]]  
**Tema:** Ensayos de aptitud para gases contaminantes criterio  
**Alcance técnico:** CO, NO/NO2, SO2 y O3  
**Referencias internas:** [[Prueba Piloto]], [[QMS]], [[CALAIRE-APP]], [[Laboratorios]], [[Equipos]]  
**Normas base:** ISO/IEC 17043:2023 e ISO 13528:2022  

---

## 1. Propósito del documento

Este documento explica de manera integral el enfoque de [[CALAIRE-EA]] para implementar ensayos de aptitud (EA) en gases contaminantes criterio. Su objetivo es consolidar, en un lenguaje técnico y operativo, qué se evalúa, cómo se organiza una ronda, qué controles exige el sistema de gestión de calidad y cómo intervienen los aplicativos digitales del proyecto.

El documento está dirigido a personal técnico, coordinadores de ronda, responsables del sistema de gestión, desarrolladores de los aplicativos y partes interesadas que requieran comprender el modelo de operación del proveedor de ensayos de aptitud. No reemplaza los procedimientos controlados del [[QMS]], pero sirve como guía interpretativa para entender la lógica del servicio.

---

## 2. Concepto general de ensayo de aptitud

Un ensayo de aptitud es una evaluación organizada del desempeño de laboratorios o estaciones de medición mediante la comparación de sus resultados frente a un valor de referencia o valor asignado. En el contexto de gases contaminantes criterio, el ensayo busca verificar si los participantes miden concentraciones de contaminantes atmosféricos de forma técnicamente comparable, trazable y adecuada para el uso previsto de sus datos.

En [[CALAIRE-EA]], el ensayo de aptitud se concibe como un esquema especializado para gases ambientales regulados o de interés para la vigilancia de calidad del aire. Los participantes pueden ser autoridades ambientales, laboratorios universitarios, redes de monitoreo o entidades con analizadores automáticos para contaminantes criterio.

El resultado de una ronda no debe interpretarse únicamente como una calificación aislada. Su valor técnico está en identificar desviaciones, sesgos, problemas de calibración, errores de transcripción, inconsistencias de método, fallas de trazabilidad o necesidades de fortalecimiento técnico en los sistemas de medición de los participantes.

---

## 3. Contaminantes criterio cubiertos

El alcance técnico del proyecto se concentra en gases contaminantes criterio asociados a monitoreo de calidad del aire:

| Contaminante | Forma evaluada | Relevancia operativa |
|---|---|---|
| Monóxido de carbono | CO | Verificación de respuesta instrumental frente a mezclas gaseosas de concentración conocida o asignada. |
| Óxidos de nitrógeno | NO y NO2 | Evaluación de analizadores NOx, conversión, linealidad y consistencia entre especies. |
| Dióxido de azufre | SO2 | Control de desempeño instrumental para medición de concentraciones trazables de gas patrón. |
| Ozono | O3 | Evaluación de respuesta frente a generación o referencia controlada de ozono, con atención especial a estabilidad. |

Cada contaminante tiene consideraciones técnicas propias. CO, NO/NO2 y SO2 suelen apoyarse en mezclas gaseosas y sistemas de dilución o calibración; O3 requiere especial cuidado porque puede generarse dinámicamente y su estabilidad depende de condiciones instrumentales y ambientales. Por esta razón, el SGC mantiene procedimientos técnicos por gas y controles diferenciados para preparación, manejo, medición, registro y análisis.

---

## 4. Términos operativos y prácticos

### 4.1 Esquema

El esquema es el diseño técnico general del ensayo de aptitud. Define qué contaminantes se evalúan, qué tipo de participantes pueden inscribirse, qué ítems o condiciones se usan, cómo se asignan valores, qué criterios de desempeño se aplican y cómo se reportan los resultados.

En términos prácticos, el esquema evita que cada ronda se improvise. La ronda ejecuta un diseño previamente definido y documentado.

### 4.2 Ronda

La ronda es una ejecución concreta del esquema. Tiene fechas, participantes, contaminantes, equipos, responsables, registros, datos y un informe de resultados. En [[Prueba Piloto]], las rondas sirven para validar la operación real del servicio antes de su consolidación documental y técnica.

Una ronda típica incluye planificación, convocatoria, confirmación de participantes, alistamiento de equipos, preparación del ítem o condición de ensayo, recepción de resultados, procesamiento estadístico, revisión técnica e informe.

### 4.3 Participante

El participante es el laboratorio, red o entidad que reporta resultados de medición dentro de la ronda. En el sistema se le asigna un identificador controlado para proteger la confidencialidad y permitir trazabilidad interna.

El participante debe recibir instrucciones claras sobre condiciones de medición, unidades, número de réplicas, plazos, forma de reporte, tratamiento de incertidumbre y restricciones de comunicación durante la ronda.

### 4.4 Ítem de ensayo de aptitud

El ítem de ensayo de aptitud es el objeto técnico que permite evaluar el desempeño. En gases contaminantes criterio puede corresponder a una mezcla gaseosa, una condición de generación controlada, una secuencia de concentración, un cilindro patrón, una línea de calibración, una configuración instrumental o un conjunto de datos trazable según el diseño de la ronda.

La característica clave del ítem es que debe ser apto para evaluar desempeño. Esto exige control sobre preparación, identificación, estabilidad, homogeneidad, transporte, almacenamiento, conexión, uso y disposición final cuando aplique.

### 4.5 Valor asignado

El valor asignado es el valor de referencia contra el cual se comparan los resultados de los participantes. Puede derivarse de una referencia trazable, una preparación controlada, un laboratorio de referencia, consenso de expertos o consenso de participantes, según el diseño estadístico aprobado.

En gases contaminantes criterio, el valor asignado debe interpretarse con trazabilidad metrológica y con incertidumbre asociada cuando sea pertinente. Una evaluación de aptitud no es defendible si el valor de referencia no está técnicamente justificado.

### 4.6 Desviación estándar para evaluación de aptitud

La desviación estándar para evaluación de aptitud, usualmente `sigma_pt`, define el criterio de dispersión permitido para evaluar los resultados. Su selección determina qué tan exigente será la ronda.

En el proyecto se ha discutido un enfoque de aptitud para el uso, donde `sigma_pt` puede definirse post-ronda mediante un modelo técnico documentado, en lugar de depender automáticamente de la variabilidad observada entre participantes. Esta decisión es crítica porque evita que una ronda con pocos participantes o con desempeño heterogéneo genere criterios artificialmente permisivos.

### 4.7 Homogeneidad y estabilidad

La homogeneidad evalúa si los ítems o condiciones entregadas a los participantes son suficientemente equivalentes entre sí. La estabilidad evalúa si el ítem o condición conserva su valor durante el periodo relevante de la ronda.

En gases, estos controles pueden incluir verificación de cilindros, líneas, generadores, analizadores de referencia, condiciones ambientales, tiempos de estabilización, presión, flujo, humedad, transporte y secuencia de medición. Si la homogeneidad o estabilidad aporta incertidumbre significativa, debe considerarse en el análisis.

### 4.8 Scores de desempeño

Los scores permiten transformar la diferencia entre el resultado del participante y el valor asignado en una señal de desempeño. Los indicadores más relevantes para el proyecto son:

| Indicador | Uso principal |
|---|---|
| `z` | Comparación frente a `sigma_pt`. |
| `z'` | Variante que considera la incertidumbre del valor asignado. |
| `zeta` | Comparación que incorpora incertidumbre del participante y del valor asignado. |
| `En` | Error normalizado, útil cuando se comparan resultados con incertidumbres expandidas. |

La interpretación debe estar predefinida. Un resultado satisfactorio, una advertencia o una señal de acción deben conducir a respuestas técnicas coherentes, no solo a una marca en el informe.

---

## 5. Operación detallada de las rondas

El esquema no debe describirse como una ronda genérica. La operación cambia según el número de analitos, la posibilidad de medir gases en forma simultánea, la cantidad de equipos instalados, la duración de las corridas, los tiempos de estabilización y la complejidad de captura de datos. Para CALAIRE-EA, la planeación debe distinguir entre rondas de alcance reducido, rondas intermedias y rondas completas.

| Alcance operativo | Analitos típicos | Complejidad principal | Control dominante |
|---|---|---|---|
| Ronda de un analito | Un contaminante aislado | Validar preparación, estabilización, medición y reporte para un solo gas. | Trazabilidad del valor asignado y estabilidad durante la ventana de medición. |
| Ronda de dos analitos simultáneos | CO + SO2 | Operar dos analizadores o respuestas en una misma ventana de generación/medición. | Coordinación de líneas, gases, unidades y captura sincronizada. |
| Ronda secuencial de varios analitos | O3 + NO + NO2, o combinaciones equivalentes | Encadenar bloques de medición con estabilización, cero/span y niveles por contaminante. | Cronograma, estabilidad, personal por turnos y separación de datos por analito. |
| Ronda completa | CO + SO2 + O3 + NO + NO2 | Integrar todos los gases criterio en una ventana operativa extendida. | Gestión de tiempos, trazabilidad, datos, revisión en caliente y contingencia. |

La ronda debe planificarse como una cadena técnica completa: confirmación de alcance, alistamiento documental, preparación de ítem o condición de ensayo, instalación, calibración, cero/span, corridas de medición, control de estabilidad, captura de datos, preprocesamiento, análisis estadístico, informe y cierre.

### 5.1 Flujo operativo general

El patrón operativo recomendado es:

| Momento | Actividad | Resultado esperado | Registro asociado |
|---|---|---|---|
| T-14 | Envío de instrucciones y calendario preliminar | Participantes conocen alcance, condiciones, requisitos y plazos. | Comunicaciones controladas, I-PSEA-09 |
| T-7 | Confirmación de participantes, equipos y personal | Se cierran contactos, equipos, analitos y requisitos de ingreso. | F-PSEA-05, F-PSEA-05A, F-PSEA-07 |
| T-3 | Verificación documental final | Se revisan documentos, recursos críticos, aplicativos, permisos y cambios. | F-PSEA-06, F-PSEA-04 |
| T-1 | Confirmación logística | Se validan punto de encuentro, horarios, disponibilidad técnica y canales de soporte. | F-PSEA-06, comunicaciones |
| Día 0 | Recepción, instalación y acondicionamiento | Equipos instalados, puertos asignados, condiciones iniciales documentadas. | F-PSEA-04, F-PSEA-11 |
| Calibración | Calibración multipunto y verificación cero/span | Respuesta instrumental preparada antes de iniciar corridas. | F-PSEA-07, F-PSEA-11 |
| Medición | Ejecución de corridas por contaminante, nivel y ventana | Resultados capturados con hora, nivel, unidad, incertidumbre y observaciones. | F-PSEA-08, F-PSEA-12 |
| Post-ronda | Desmontaje, retiro y cierre de registros | Equipos liberados, datos bloqueados, incidentes documentados. | F-PSEA-11, F-PSEA-14 si aplica |
| T+1 a T+5 | Preprocesamiento, análisis e informe | Datos oficiales revisados, scores calculados, informe revisado y autorizado. | F-PSEA-09, F-PSEA-10, F-PSEA-12, F-PSEA-13 |

### 5.2 Controles técnicos por analito

Cada gas requiere controles específicos:

| Analito | Control operativo clave | Error que debe prevenirse |
|---|---|---|
| CO | Verificar gas patrón, dilución, respuesta del analizador, unidades y linealidad en los niveles seleccionados. | Reportar en unidad incorrecta, usar setpoint no documentado o perder trazabilidad del gas de referencia. |
| SO2 | Controlar gas patrón, adsorción en líneas, tiempo de estabilización y respuesta instrumental. | Subestimar pérdidas por línea, registrar lecturas antes de estabilización o mezclar niveles. |
| O3 | Confirmar generación o referencia controlada, tiempo de estabilización, limpieza de línea y lectura estable. | Reportar antes de estabilización, perder trazabilidad del generador o mezclar condiciones de referencia. |
| NO | Verificar gas patrón, dilución, respuesta del analizador y consistencia de cero/span. | Confundir NO con NOx, usar unidad incorrecta o registrar nivel equivocado. |
| NO2 | Controlar conversión, relación NO/NO2 y consistencia del método del participante. | Reportar resultados no comparables por diferencias de conversión o tratamiento instrumental. |

El preprocesamiento debe detectar si un valor fue cargado al participante equivocado, si una repetición corresponde a otro analito, si la incertidumbre se reportó en otra unidad, si se mezclaron datos de NO, NO2 y NOx, o si un resultado corresponde a una condición no estabilizada.

### 5.3 Paquete operativo mínimo por ronda

Cada ronda requiere copias de trabajo de los formatos F-PSEA-05 a F-PSEA-14. Estos formatos no son accesorios administrativos; son la evidencia mínima para demostrar que la ronda fue ejecutada y que sus datos son analizables.

| Formato | Uso operativo |
|---|---|
| F-PSEA-05 Confirmación de Participación | Aceptación formal de alcance, analitos y condiciones. |
| F-PSEA-06 Plan de Ronda EA | Diseño operativo aprobado de la ronda. |
| F-PSEA-07 Lista Maestra de Participantes | Codificación, contactos y estado de participación. |
| F-PSEA-08 Registro de Preparación del Ítem | Setpoints, gases, dilución, condiciones y responsables. |
| F-PSEA-09 Datos exportados para análisis | Archivo oficial desde `calaire-app` hacia `pt_app`. |
| F-PSEA-10 Registro de preprocesamiento | Revisión de estructura, unidades, completitud y plausibilidad. |
| F-PSEA-11 Homogeneidad y estabilidad | Evidencia técnica de aptitud del ítem o condición. |
| F-PSEA-12 Datos oficiales consolidados | Dataset aprobado para evaluación. |
| F-PSEA-13 Informe final de resultados | Informe emitido, revisado y autorizado. |
| F-PSEA-14 Registro de queja o NC | Uso bajo demanda si hay desviación, queja o no conformidad. |

Además, F-PSEA-05A debe usarse antes de la ronda para levantar información del participante, equipos, personal autorizado y condiciones de contacto. F-PSEA-15 a F-PSEA-17 se activan si aparecen no conformidades, quejas o apelaciones; F-PSEA-20 soporta validación de software; F-PSEA-21 a F-PSEA-23 cubren competencia, imparcialidad y proveedores críticos.

### 5.4 Flujo operativo diario

El flujo práctico de ejecución debe manejarse como una secuencia de puntos de control:

1. **Apertura de jornada:** confirmar responsables presentes, equipos disponibles, documentos vigentes, condiciones de seguridad, estado de `calaire-app` y comunicación con participantes.
2. **Recepción o verificación de equipos:** registrar participante, analito, número de serie, configuración, accesorios, certificados disponibles y condición física.
3. **Instalación:** verificar ubicación, conexiones, líneas, caudales, fugas, alimentación eléctrica, estabilización y compatibilidad con la secuencia de medición.
4. **Cero/span o verificación inicial:** documentar respuesta instrumental inicial y cualquier ajuste permitido por instrucciones.
5. **Generación o suministro de condición de ensayo:** registrar setpoint, gas, dilución, referencia, condiciones ambientales y responsable.
6. **Medición del participante:** capturar resultados, repeticiones, incertidumbre si aplica, método, observaciones y hora de medición.
7. **Control de estabilidad:** confirmar que la condición no cambió de forma material durante la ventana de medición.
8. **Cierre de jornada:** bloquear o cerrar envíos, respaldar datos, registrar incidentes, confirmar equipos pendientes y preparar transición.
9. **Revisión post-jornada:** verificar completitud, coherencia de unidades, duplicados, valores faltantes y trazabilidad equipo-participante-analito.

La disciplina diaria es especialmente importante cuando aumenta la cantidad de equipos y analitos. Los errores más probables son código equivocado, campo incompleto, unidad inconsistente, resultado cargado al analito incorrecto o incertidumbre reportada sin cobertura clara.

### 5.5 Puntos de decisión antes, durante y después

Antes de iniciar una ronda, el coordinador debe poder responder afirmativamente:

- ¿Está aprobado el plan de ronda?
- ¿Están confirmados participantes, contactos, equipos y analitos?
- ¿Están habilitados los formularios correctos en `calaire-app`?
- ¿Está definido el valor asignado o el método para determinarlo?
- ¿Está definido `sigma_pt` o el criterio para fijarlo?
- ¿Está disponible la evidencia de trazabilidad de gases, calibradores o generadores?
- ¿Están definidos responsables de operación, estadística, SGC y revisión técnica?

Durante la ejecución, debe detenerse o escalarse la ronda si:

- no se puede garantizar identificación de participante, equipo o analito;
- la condición de ensayo no estabiliza;
- se detecta fuga, falla de calibrador, error de gas o incompatibilidad instrumental;
- `calaire-app` no permite capturar datos de forma trazable;
- un participante recibe información distinta a otro en una condición equivalente;
- se compromete confidencialidad o imparcialidad.

Después de la ejecución, no debe pasar a informe hasta que:

- los datos estén completos y bloqueados;
- el archivo exportado tenga estructura validada;
- las unidades y cifras significativas estén revisadas;
- homogeneidad y estabilidad estén evaluadas o justificadas;
- valor asignado, incertidumbre y `sigma_pt` estén documentados;
- los scores estén reproducidos o revisados;
- el informe tenga revisión técnica y autorización.

### 5.6 Análisis estadístico e informe

El análisis estadístico consolida el valor asignado, la incertidumbre asociada, `sigma_pt`, los scores de desempeño, estudios de homogeneidad y estabilidad cuando aplican, y la interpretación de resultados.

En [[CALAIRE-APP]], el procesamiento estadístico se apoya en `pt_app` y `ptcalc`, con métodos alineados a ISO 13528. La cadena esperada incluye preprocesamiento, cálculo robusto cuando aplique, evaluación de homogeneidad y estabilidad, estimación de incertidumbres y generación de puntajes. Para rondas con pocos participantes, la lógica estadística debe evitar una dependencia indebida del consenso de participantes y debe privilegiar valores asignados y criterios técnicamente justificados.

El informe debe presentar resultados de manera clara, trazable y útil para la mejora técnica. Debe incluir alcance, participantes codificados, metodología, valor asignado, criterio de desempeño, resultados individuales, interpretación, limitaciones, desviaciones relevantes, revisión técnica y autorización.

El cierre de ronda debe conservar registros, resolver quejas o apelaciones si se presentan, documentar no conformidades, identificar lecciones aprendidas y alimentar la mejora del SGC.

### 5.7 Equipos de referencia

Para soportar el valor asignado bajo modalidad de laboratorio de referencia, el esquema debe identificar qué equipo se usa por contaminante, su trazabilidad, estado de calibración/verificación, condiciones de uso y vínculo con los datos oficiales de la ronda.

| Contaminante | Equipo de referencia documentado |
|---|---|
| SO2 | HORIBA APSA-370 |
| CO | Teledyne T300 |
| O3 | Thermo 49i |
| NO/NO2 | HORIBA APSA-370 |

Estos equipos no son simplemente inventario. En el flujo del EA, sostienen la asignación de valor, la comparación metrológica y la defensa técnica del informe.

### 5.8 Duración operativa estimada según número de analitos

Las secuencias operativas disponibles permiten estimar tiempos realistas para planificar una ronda desde un solo analito hasta el alcance completo de cinco analitos. El cálculo debe distinguir entre **analitos secuenciales** y **analitos simultáneos**:

- CO y SO2 pueden ejecutarse como bloque simultáneo CO/SO2.
- O3, NO y NO2 se tratan como bloques secuenciales.
- La instalación se registra como una actividad inicial de 1 hora, pero en una ronda con varios participantes puede crecer por duplicación de equipos.
- La calibración multipunto fue de 3 horas para CO/SO2 y 4 horas para O3-NO/NO2.
- El cero/span tomó 30 minutos antes de la secuencia de corridas.
- Las corridas de nivel distinto de cero tomaron 3 horas por nivel.

Con base en esos supuestos operativos, los bloques base son:

| Bloque operativo | Analitos cubiertos | Instalación | Calibración + cero/span | Corridas | Tiempo técnico aproximado |
|---|---|---:|---:|---:|---:|
| Bloque CO/SO2 | CO y SO2 simultáneos | 1:00 | 3:30 | 13:30 | 18:00 |
| Bloque O3 | O3 | Incluida en ronda | 4:30 compartida con NO/NO2 | 13:30 | 18:00 si se ejecuta solo |
| Bloque NO | NO | Incluida en ronda | Calibración compartida | 13:00 con cero NO/NO2 | 13:00 adicional |
| Bloque NO2 | NO2 | Incluida en ronda | Calibración compartida | 12:00 si usa cero compartido | 12:00 adicional |
| Bloque O3-NO-NO2 | O3, NO y NO2 secuenciales | 1:00 | 4:30 | 38:30 | 44:00 |

Una tabla práctica de planeación queda así:

| Alcance de ronda | Analitos incluidos | Supuesto de ejecución | Tiempo técnico mínimo | Lectura calendario recomendada |
|---|---|---|---:|---|
| 1 analito | Un gas aislado | Instalación + calibración/cero + 1 cero + 4 niveles. | 17:30 a 19:00 | 2 días operativos: instalación y una jornada extendida de medición. |
| 2 analitos simultáneos | CO + SO2 | Bloque simultáneo, misma ventana de generación/medición. | 18:00 | 3 días calendario: instalación, medición extendida y devolución. |
| 2 analitos secuenciales | Dos gases no simultáneos | Primer gas completo + segundo gas con niveles propios. | 30:00 a 32:00 | 2 a 3 días operativos, con posible operación nocturna. |
| 3 analitos secuenciales | O3 + NO + NO2 | Bloque secuencial O3-NO-NO2. | 44:00 | 4 días calendario: instalación, calibración/medición y cierre en madrugada o día siguiente. |
| 4 analitos | O3 + NO + NO2 + un gas adicional | Bloque O3-NO-NO2 + bloque parcial adicional. | 57:00 a 60:00 | 4 a 5 días calendario con turnos extendidos. |
| 5 analitos | O3 + NO + NO2 + CO + SO2 | Bloque O3-NO-NO2 + bloque simultáneo CO/SO2. | 62:00 aprox. | 5 a 6 días calendario; requiere buffers, personal por turnos y control reforzado de estabilidad. |

El valor de 62 horas para los cinco analitos no debe interpretarse como duración fija universal. Es una estimación operativa: 44 horas para O3-NO-NO2 más 18 horas para CO/SO2, asumiendo que no se repite instalación completa ni se generan retrasos por estabilización adicional. Si participan dos o más laboratorios, el tiempo de medición puede no duplicarse, pero sí aumenta el tiempo de instalación, verificación, trazabilidad de equipos, resolución de desviaciones y revisión de datos.

Para efectos de planeación, CALAIRE-EA debería usar tres bandas de duración:

| Banda | Condición | Uso recomendado |
|---|---|---|
| Ronda corta | 1 a 2 analitos simultáneos, 1 participante | Ventana mínima de 3 días calendario. |
| Ronda intermedia | 2 analitos secuenciales o 3 analitos con 1 participante | Ventana de 4 días calendario. |
| Ronda completa | 5 analitos o más de un participante | Ventana de 5 a 6 días calendario, con contingencia formal. |

La contingencia no es opcional. La calibración y estabilización de analizadores puede consumir más tiempo que el estimado inicialmente. Por tanto, el cronograma de una ronda completa debe reservar tiempo para estabilización prolongada, repetición de cero/span, revisión de datos en caliente y recuperación ante fallas de conexión o generación.

---

## 6. Sistema de gestión de calidad

### 6.1 Función del SGC

El sistema de gestión de calidad de [[QMS]] asegura que el ensayo de aptitud sea competente, imparcial, trazable, técnicamente válido y reproducible. Su función no es solo producir documentos; debe controlar decisiones y evidencias que afecten la validez de la evaluación.

El SGC debe demostrar que el proveedor tiene autoridad definida, personal competente, controles documentales, reglas de confidencialidad, gestión de riesgos, control de registros, auditoría, mejora y capacidad técnica para operar el esquema.

### 6.2 Arquitectura documental

La arquitectura documental vigente se organiza en cuatro niveles:

| Nivel | Contenido | Función |
|---|---|---|
| Documentos marco | Protocolos generales y documentos base | Definen alcance, política técnica y estructura del programa. |
| Procedimientos | Procesos operativos y de gestión | Indican cómo se planifica, ejecuta, analiza, comunica y cierra una ronda. |
| Instructivos | Instrucciones específicas de trabajo | Guían tareas concretas en aplicativos, preprocesamiento, administración y participación. |
| Formatos y registros | Evidencia controlada | Demuestran qué ocurrió, quién lo hizo, cuándo, con qué datos y bajo qué revisión. |

Esta estructura evita mezclar documentos maestros con copias operativas de una ronda. Un formato usado en prueba piloto puede ser evidencia útil, pero no equivale automáticamente a una versión maestra controlada.

### 6.3 Controles de imparcialidad y confidencialidad

La imparcialidad exige que las decisiones técnicas no estén sesgadas por presiones comerciales, institucionales, personales o contractuales. En la práctica, esto implica identificar conflictos de interés, separar funciones cuando sea necesario, documentar decisiones críticas y proteger la independencia de la evaluación.

La confidencialidad exige proteger identidad de participantes, resultados individuales, accesos a aplicativos, valores sensibles, datos crudos, informes preliminares y comunicaciones. La codificación de participantes y el control de accesos en aplicativos son componentes centrales de este control.

### 6.4 Competencia y autorización

El SGC debe definir perfiles de competencia para quienes planifican rondas, preparan ítems, operan equipos, administran aplicativos, revisan datos, ejecutan análisis estadísticos, interpretan resultados y autorizan informes.

La competencia debe estar evidenciada mediante formación, experiencia, entrenamiento, evaluación, autorización y seguimiento. En un servicio de gases contaminantes criterio, la competencia metrológica, estadística e instrumental es tan importante como la competencia documental.

### 6.5 Control documental y registros

Los documentos controlados establecen cómo debe ejecutarse el proceso. Los registros demuestran cómo se ejecutó realmente. Esta distinción es fundamental para auditoría y trazabilidad.

Los registros críticos incluyen plan de ronda, cronograma, confirmación de participantes, anexos técnicos de equipos, datos reportados, datos exportados, registro de preprocesamiento, homogeneidad, estabilidad, datos oficiales consolidados, informe final, comunicaciones, desviaciones, quejas, apelaciones y acciones correctivas.

### 6.6 Gestión de riesgos

Los riesgos del esquema pueden ser técnicos, operativos, documentales, informáticos o de gestión. Algunos riesgos relevantes son:

- número bajo de participantes;
- fallas de estabilidad del gas o condición de ensayo;
- errores de unidad o formato de datos;
- pérdida de trazabilidad metrológica;
- divulgación indebida de valores sensibles;
- uso de versiones no controladas de documentos;
- errores de cálculo en aplicativos;
- acceso incorrecto a datos de participantes;
- criterios estadísticos no justificados;
- sustitución de procedimientos originales por versiones generadas no controladas.

Cada riesgo debe tener tratamiento proporcional: prevención, verificación, revisión técnica, controles de acceso, validación de software, respaldo documental o acciones correctivas.

### 6.7 Trabajo no conforme, quejas y apelaciones

El SGC debe prever qué ocurre cuando una actividad no cumple los requisitos. Un trabajo no conforme puede originarse en fallas de equipo, errores de registro, desviaciones del procedimiento, problemas de estabilidad, cálculos incorrectos o emisión de un informe con errores.

Las quejas y apelaciones deben gestionarse con independencia, trazabilidad, tiempos definidos y respuesta técnica. Un participante debe poder cuestionar un resultado sin que esto comprometa la imparcialidad ni la confidencialidad del resto de participantes.

---

## 7. Aplicativos del ecosistema CALAIRE

### 7.1 Función general de los aplicativos

Los aplicativos no son elementos accesorios. En [[CALAIRE-APP]], el ecosistema digital sostiene trazabilidad, captura de datos, administración de rondas, preprocesamiento, análisis estadístico e informe. Por tanto, deben tratarse como parte del SGC y estar sujetos a validación, control de cambios, control de acceso y documentación.

El proyecto distingue dos componentes principales:

- `calaire-app`: portal web de gestión operativa de rondas, participantes y captura de datos.
- `pt_app` + `ptcalc`: motor estadístico para procesamiento de datos, evaluación de aptitud e informes.

### 7.2 calaire-app

`calaire-app` gestiona la capa operativa de la ronda. Su función es permitir que el coordinador administre rondas, asigne participantes, controle accesos, capture resultados y exporte datos estructurados hacia el motor estadístico.

Sus funciones esperadas incluyen:

- creación y administración de rondas;
- asignación de contaminantes y participantes;
- autenticación y control de roles;
- formularios de captura para participantes;
- cierre formal de envíos;
- visualización administrativa de datos;
- exportación de archivos compatibles con `pt_app`;
- trazabilidad de fechas, responsables y estados.

Desde la perspectiva del SGC, `calaire-app` debe garantizar que los datos capturados correspondan al participante correcto, que los campos obligatorios estén controlados, que el cierre de envío sea trazable y que la exportación no altere el significado técnico de los resultados.

### 7.3 pt_app y ptcalc

`pt_app` y el paquete interno `ptcalc` gobiernan el procesamiento estadístico. Su función es transformar datos reportados y datos de referencia en resultados de evaluación de desempeño, aplicando reglas alineadas con ISO 13528.

El flujo técnico esperado incluye:

1. recepción del archivo exportado desde `calaire-app`;
2. preprocesamiento y validación de estructura;
3. consolidación de datos oficiales;
4. cálculo de valor asignado y criterios de desempeño;
5. evaluación de homogeneidad y estabilidad;
6. estimación de incertidumbres;
7. cálculo de `z`, `z'`, `zeta` y `En` cuando aplique;
8. generación de tablas, gráficos e informe final.

La validación del motor estadístico debe conservar evidencia de pruebas con datos conocidos, comparación cruzada, revisión de fórmulas, control de versiones y tratamiento de casos límite.

### 7.4 Contrato de datos entre aplicativos

El contrato de datos es el acuerdo técnico que define cómo `calaire-app` entrega información a `pt_app`. Debe especificar columnas, tipos de dato, unidades, códigos de participante, contaminante, nivel, repetición, resultado, incertidumbre cuando aplique y reglas de identificación.

Un contrato de datos estable evita errores silenciosos. Si una columna cambia de nombre, una unidad se mezcla o un campo se interpreta de forma diferente, el análisis estadístico puede producir resultados formalmente correctos pero técnicamente inválidos.

### 7.5 Validación y control de software

El software usado para capturar, transferir, calcular o reportar resultados debe validarse en proporción a su impacto. Los controles mínimos esperados son:

- control de versiones;
- pruebas funcionales de flujos críticos;
- datos de prueba con resultados esperados;
- revisión de fórmulas y métodos;
- trazabilidad de cambios;
- control de accesos;
- respaldo de datos;
- registro de errores y correcciones;
- documentación de limitaciones conocidas.

En el SGC, una falla del aplicativo puede convertirse en una no conformidad si afecta integridad de datos, confidencialidad, evaluación de desempeño o informe final.

---

## 8. Relación entre operación, SGC y aplicativos

El servicio de ensayos de aptitud funciona correctamente solo si las tres capas se mantienen coherentes:

| Capa | Pregunta que responde | Evidencia principal |
|---|---|---|
| Operación práctica | ¿La ronda se puede ejecutar de forma controlada? | Cronograma, equipos, participantes, registros de ejecución, comunicaciones. |
| Sistema de gestión | ¿La ejecución cumple requisitos de competencia, imparcialidad y trazabilidad? | Procedimientos, instructivos, formatos, registros, auditorías, acciones correctivas. |
| Aplicativos | ¿Los datos se capturan, procesan y reportan sin pérdida de integridad? | Trazabilidad digital, exportaciones, scripts, validaciones, informes. |

La coherencia entre capas debe revisarse continuamente. Un formato documental puede estar correcto, pero si el aplicativo no captura el campo requerido, el registro real queda incompleto. De igual forma, el aplicativo puede calcular un score correctamente, pero si el criterio `sigma_pt` no fue aprobado ni comunicado, la evaluación queda débil frente a ISO 17043.

---

## 9. Ciclo de evidencias de una ronda

El ciclo documental y digital esperado puede resumirse así:

1. **Planificación:** calendario, cronograma, plan de ronda, ficha digital y matriz de responsables.
2. **Participación:** invitación, confirmación, registro del participante e instrucciones.
3. **Equipos e ítem:** anexo técnico de equipos, preparación y control del ítem, certificados y verificaciones.
4. **Captura de datos:** resultados reportados por participante en `calaire-app`.
5. **Exportación:** archivo oficial para análisis estadístico.
6. **Preprocesamiento:** revisión de estructura, unidades, consistencia y completitud.
7. **Análisis:** homogeneidad, estabilidad, valor asignado, incertidumbres y scores.
8. **Consolidación:** datos oficiales y revisión técnica.
9. **Informe:** emisión, autorización, entrega y control de versión.
10. **Cierre:** quejas, apelaciones, no conformidades, lecciones aprendidas y mejora.

Este ciclo permite reconstruir la ronda completa ante una auditoría, una apelación o una revisión técnica posterior.

---

## 10. Criterios de calidad técnica para gases contaminantes criterio

Los ensayos de aptitud en gases criterio requieren controles técnicos específicos:

- **Trazabilidad metrológica:** los patrones, calibradores y mediciones de referencia deben estar vinculados a referencias reconocidas.
- **Estabilidad del gas:** se debe controlar degradación, adsorción, reactividad, dilución, generación y tiempos de estabilización.
- **Compatibilidad instrumental:** los analizadores de participantes deben operar dentro de rangos y condiciones comparables.
- **Unidades y condiciones de referencia:** las concentraciones deben expresarse bajo unidades y condiciones claramente definidas.
- **Linealidad y niveles:** la ronda puede requerir niveles de concentración que evalúen respuesta en diferentes puntos operativos.
- **Control de interferencias:** cuando aplique, se deben considerar interferentes, humedad, presión, flujo y condiciones ambientales.
- **Registro de incertidumbre:** la incertidumbre declarada por participante debe tratarse de manera coherente si se usan `zeta` o `En`.
- **Revisión de datos extremos:** los valores atípicos deben tratarse con método definido, sin exclusión arbitraria.

Estos criterios conectan la metrología de gases con la estadística de desempeño. La ronda no evalúa únicamente si un número coincide con otro; evalúa si el sistema de medición del participante produce datos confiables bajo condiciones controladas.

---

## 11. Roles operativos recomendados

| Rol | Responsabilidad principal |
|---|---|
| Coordinador de ronda | Planifica, comunica, controla cronograma, gestiona participantes y asegura cierre documental. |
| Responsable técnico de gases | Controla preparación, equipos, condiciones de ensayo, trazabilidad y criterios técnicos por contaminante. |
| Responsable estadístico | Define o verifica diseño estadístico, valor asignado, `sigma_pt`, scores e interpretación. |
| Responsable SGC | Controla documentos, registros, no conformidades, quejas, apelaciones, auditoría y mejora. |
| Administrador de aplicativos | Asegura operación de `calaire-app`, exportaciones, accesos y soporte funcional. |
| Revisor técnico | Verifica coherencia de datos, análisis e informe antes de emisión. |
| Autorizador de informe | Aprueba la emisión formal del informe final de resultados. |

La segregación de roles fortalece imparcialidad y reduce errores. En estructuras pequeñas, una persona puede cubrir varias funciones, pero las responsabilidades y revisiones deben quedar explícitas.

---

## 12. Salidas esperadas del servicio

Las salidas de una ronda de ensayo de aptitud incluyen:

- informe final de resultados;
- resultados individuales codificados;
- evaluación de desempeño por contaminante y nivel;
- análisis de homogeneidad y estabilidad cuando aplique;
- trazabilidad del valor asignado y criterio de evaluación;
- registros de datos reportados y datos oficiales consolidados;
- registros de revisión técnica y autorización;
- lecciones aprendidas;
- acciones correctivas o de mejora cuando correspondan.

Para el participante, la salida principal es una evaluación clara de su desempeño y una base técnica para investigar desviaciones. Para el proveedor, la salida también incluye evidencia de competencia, trazabilidad, control de riesgos y mejora del sistema.

---

## 13. Puntos críticos de control

Los puntos críticos que requieren atención permanente son:

1. Definición documentada del valor asignado y su incertidumbre.
2. Justificación de `sigma_pt` y criterios de desempeño.
3. Control de homogeneidad y estabilidad del ítem o condición de ensayo.
4. Claridad de instrucciones a participantes.
5. Protección de confidencialidad y códigos de participante.
6. Validación del contrato de datos entre `calaire-app` y `pt_app`.
7. Revisión de unidades, formatos y resultados antes del análisis.
8. Validación del software estadístico y trazabilidad de versiones.
9. Revisión técnica independiente antes de emitir informes.
10. Gestión documentada de desviaciones, quejas, apelaciones y no conformidades.

Estos puntos deben tratarse como controles de validez. Si fallan, la ronda puede perder defendibilidad aunque el informe haya sido generado correctamente.

---

## 14. Lectura integrada para CALAIRE-EA

El proyecto [[CALAIRE-EA]] puede entenderse como la integración de cuatro componentes:

- **Componente metrológico:** define gases, equipos, preparación, trazabilidad, estabilidad, medición e incertidumbre.
- **Componente estadístico:** define valor asignado, `sigma_pt`, scores, criterios de interpretación y tratamiento de datos.
- **Componente de gestión:** asegura imparcialidad, confidencialidad, competencia, documentos, registros, auditoría y mejora.
- **Componente digital:** soporta captura, transferencia, procesamiento, trazabilidad e informe mediante `calaire-app`, `pt_app` y `ptcalc`.

La madurez del servicio depende de que estos componentes operen como un solo sistema. La prueba piloto permite verificar esa integración bajo condiciones reales, identificar brechas y ajustar procedimientos antes de consolidar el servicio como oferta técnica estable.

---

## 15. Referencias internas sugeridas

- [[CALAIRE-EA]]: visión general del proyecto.
- [[Prueba Piloto]]: coordinación operativa de rondas.
- [[QMS]]: sistema de gestión de calidad y arquitectura documental.
- [[CALAIRE-APP]]: ecosistema de aplicativos.
- [[Laboratorios]]: participantes y entidades vinculadas.
- [[Equipos]]: inventario de analizadores, calibradores y elementos asociados.
- `docs/docs_sgc/sgc_17043.md`: guía conceptual ISO/IEC 17043.
- `docs/docs_sgc/sgc_13528.md`: guía conceptual ISO 13528.
- `docs/documentacion_sgc/sgc_res.md`: estado actualizado del SGC PEA.
