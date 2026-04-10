Sí. Arranco con una propuesta base ya utilizable para tu investigación y, al final, te dejo las preguntas que realmente necesito para aterrizarla a tu caso.

Hoy la base normativa vigente para un proveedor de ensayos de aptitud es **ISO/IEC 17043:2023** como norma de competencia, imparcialidad y operación coherente del proveedor, y **ISO 13528:2022** como norma de métodos estadísticos para diseñar el esquema, analizar datos y evaluar el desempeño. En las páginas oficiales de ISO, las ediciones anteriores **ISO/IEC 17043:2010** e **ISO 13528:2015** aparecen como retiradas. Además, ILAC mantiene vigente **ILAC P9:01/2024** y comunicó una transición de tres años para pasar a ISO/IEC 17043:2023, con fecha límite **31 de mayo de 2026**; como estamos en marzo de 2026, conviene diseñar todo directamente contra la edición 2023\. ([ISO](https://www.iso.org/standard/80864.html))

Tomaré también como base los textos de las dos normas que subiste, porque ahí está el detalle técnico que necesitamos para estructurar el sistema y el modelo estadístico.

## **Propuesta de sistema de gestión de calidad para ensayos de aptitud**

La forma más sólida de diseñarlo es separar el sistema en **tres capas**:

### **1\) Capa de gobierno**

Aquí vive lo que asegura que el proveedor sea confiable y auditable:

* política de calidad;  
* política de imparcialidad;  
* política de confidencialidad;  
* definición del alcance del proveedor de ensayos de aptitud;  
* estructura organizacional y autoridades;  
* revisión por la dirección;  
* gestión de riesgos y oportunidades;  
* seguimiento de objetivos e indicadores.

ISO/IEC 17043:2023 exige un sistema de gestión documentado que incluya, como mínimo, políticas, responsabilidades, documentación del sistema, control documental, control de registros, acciones sobre riesgos y oportunidades, mejora, acciones correctivas, auditorías internas y revisión por la dirección. También permite apoyarse en un sistema tipo ISO 9001 siempre que ese sistema demuestre el cumplimiento consistente de los requisitos de 17043\.

### **2\) Capa operativa**

Es el “core” del proveedor. Yo lo diseñaría como este mapa de procesos:

* revisión de solicitudes, contratos y objetivos del esquema;  
* diseño y planificación del esquema de EA;  
* definición del modelo estadístico;  
* producción, selección o adquisición del ítem de ensayo;  
* evaluación de homogeneidad y estabilidad;  
* asignación del valor asignado y su incertidumbre;  
* embalaje, distribución, trazabilidad logística y confirmación de entrega;  
* instrucciones a participantes;  
* recepción, validación y protección de resultados;  
* análisis estadístico y evaluación del desempeño;  
* emisión del informe;  
* tratamiento de trabajo no conforme;  
* gestión de quejas y apelaciones.

ISO/IEC 17043 pide que el proveedor comunique a participantes los objetivos, criterios de participación, criterios para el valor asignado y la evaluación, cronograma, confidencialidad y forma de aplicación; además, prohíbe externalizar el diseño y planificación del esquema, la evaluación del desempeño y la autorización de informes. También exige procedimientos documentados para quejas, apelaciones y trabajo no conforme.

### **3\) Capa de soporte**

Aquí entran los habilitadores del sistema:

* gestión de competencia del personal;  
* autorización formal de funciones críticas;  
* control de proveedores externos;  
* validación de software y hojas de cálculo;  
* control ambiental;  
* trazabilidad metrológica;  
* seguridad de la información;  
* control de documentos y registros;  
* programa de auditoría interna;  
* CAPA y mejora.

La norma también exige que los ensayos o mediciones usados para caracterizar ítems, o para evaluar homogeneidad y estabilidad, se realicen bajo los requisitos pertinentes de **ISO/IEC 17025**; y si el ítem califica como material de referencia, su producción debe cumplir los requisitos pertinentes de **ISO 17034**.

## **Núcleo estadístico que debe incorporar el sistema**

Aquí es donde entra ISO 13528\. Mi recomendación es que tu sistema no trate la estadística como un anexo, sino como un **subproceso formal** con entradas, reglas, responsables, validaciones y registros.

### **A. Diseño estadístico del esquema**

Antes de lanzar cualquier ronda, el sistema debe obligar a responder estas decisiones:

* objetivo del esquema;  
* tipo de datos: cuantitativos, cualitativos, ordinales;  
* número esperado de participantes;  
* si habrá uno o varios métodos de medición;  
* si la comparación será contra referencia externa, consenso o incertidumbre declarada;  
* criterio de evaluación: σpt, error máximo permitido, o ambos;  
* manejo de poblaciones pequeñas o heterogéneas.

ISO 13528 deja claro que el diseño estadístico debe depender del objetivo, del tipo de dato, de las suposiciones estadísticas, de la naturaleza del error y del número esperado de resultados. También señala que puede ser necesario separar grupos de participantes cuando diferentes métodos no sean comparables.

### **B. Valor asignado y su incertidumbre**

Tu procedimiento debe establecer una jerarquía clara para asignar el valor:

1. formulación o preparación gravimétrica;  
2. material de referencia certificado;  
3. laboratorio de referencia;  
4. consenso de laboratorios expertos;  
5. consenso de participantes.

Además, el sistema debe obligar a estimar la incertidumbre del valor asignado considerando caracterización, homogeneidad, transporte y estabilidad. ISO 13528 trata esto como una parte central del esquema, no como un detalle opcional.

### **C. Homogeneidad y estabilidad**

Este bloque merece procedimiento propio, plan de muestreo, criterios de aceptación y registro de evidencia.

Como criterio base, ISO 13528 usa que el efecto de la falta de homogeneidad o de la inestabilidad no debe comprometer la evaluación del desempeño; en sus anexos propone criterios prácticos como comparar el componente entre ítems con **0,3 σpt** o **0,1 δE**, y para estabilidad compara el cambio pre/post distribución con esos mismos umbrales.

### **D. Revisión inicial de resultados**

Tu sistema debe exigir, antes del cálculo final:

* detección de errores groseros obvios;  
* revisión visual de la distribución;  
* revisión de asimetría o multimodalidad;  
* decisión documentada sobre separación por método;  
* decisión documentada sobre tratamiento de datos censurados;  
* revisión de número mínimo de resultados válidos.

ISO 13528 recomienda la revisión visual por personal con competencia técnica y estadística, el uso preferente de métodos robustos y cautela con las pruebas clásicas de outliers.

### **E. Cálculo y reglas de decisión**

El sistema debe definir, por tipo de esquema, qué estadístico se usará:

* **D / D% / PA** cuando el criterio se basa en error permitido;  
* **z** cuando el desempeño se compara con σpt;  
* **z’** cuando la incertidumbre del valor asignado no es despreciable;  
* **ζ** cuando interesa contrastar el resultado contra la incertidumbre estándar declarada;  
* **En** sobre todo en calibración, cuando se trabaja con incertidumbres expandidas.

ISO 13528 considera aceptable la interpretación clásica de **|z| \< 2** como satisfactorio, **2 a 3** como advertencia y **\> 3** como señal de acción, y además indica que cuando la incertidumbre del valor asignado no es pequeña frente a σpt conviene pasar a z’. También describe ζ y En como herramientas para evaluar la coherencia entre resultado e incertidumbre reportada.

## **Documentación mínima que yo exigiría en tu SGC**

No haría un “manual gigante”. Haría una arquitectura corta, auditable y modular:

* Manual del sistema o mapa maestro del SGC.  
* Procedimiento de imparcialidad y conflicto de interés.  
* Procedimiento de confidencialidad y codificación de participantes.  
* Procedimiento de revisión de solicitudes/contratos.  
* Procedimiento de diseño y planificación de esquemas.  
* Procedimiento de control de proveedores externos.  
* Procedimiento de producción/selección del ítem.  
* Procedimiento de homogeneidad y estabilidad.  
* Procedimiento de asignación del valor e incertidumbre.  
* Procedimiento de recepción, validación y análisis de resultados.  
* Procedimiento de evaluación estadística y emisión de informes.  
* Procedimiento de trabajo no conforme.  
* Procedimiento de quejas y apelaciones.  
* Procedimiento CAPA.  
* Procedimiento de auditoría interna.  
* Procedimiento de revisión por la dirección.  
* Procedimiento de control documental y de registros.  
* Matriz de competencias y autorizaciones.  
* Plan maestro de validación de software estadístico.

Esto es coherente con la estructura exigida por ISO/IEC 17043 y con la necesidad, remarcada por ISO 13528, de contar con pericia estadística y software validado para el análisis del esquema.

## **Indicadores que deberían quedar dentro de la investigación**

Para que tu investigación no quede solo normativa, yo incluiría estos KPI:

* % de rondas emitidas a tiempo;  
* % de ítems que pasan homogeneidad a la primera;  
* % de rondas con estabilidad aceptable;  
* % de rondas donde u(xpt) es despreciable frente a σpt;  
* tasa de quejas por ronda;  
* tiempo medio de cierre de CAPA;  
* errores de transcripción o carga de datos;  
* % de participantes con resultados recibidos completos y en formato correcto;  
* % de acciones correctivas repetitivas;  
* satisfacción de participantes.

## **Ruta de implementación que te propongo**

Como diseño de investigación aplicada, yo lo estructuraría en 6 fases:

1. **Diagnóstico de brecha** contra ISO/IEC 17043:2023 e ISO 13528:2022.  
2. **Definición del alcance**: disciplina, measurandos, participantes, frecuencia y tipo de ronda.  
3. **Diseño documental y estadístico** del esquema.  
4. **Piloto** de una ronda real o simulada.  
5. **Validación** de cálculos, software, formatos y tiempos.  
6. **Cierre gerencial** con auditoría interna y revisión por la dirección.

Como contexto de acreditación, esto tiene sentido hacerlo ya con la edición 2023 de 17043, porque el marco internacional de ILAC para esa transición está en su fase final. ([ILAC – ILAC Live Site](https://ilac.org/latest_ilac_news/publication-of-iso-iec-170432023/?utm_source=chatgpt.com))

## **Las preguntas que necesito para pulir tu investigación**

Respóndeme estas preguntas en el orden que prefieras:

1. **¿Tu investigación busca diseño académico, implementación real, preparación para acreditación, o las tres cosas?**  
2. **¿En qué sector técnico estará el esquema?** Química, microbiología, calibración, alimentos, ambiental, clínica, construcción, forense, otro.  
3. **¿Tus resultados serán cuantitativos, cualitativos, ordinales o mixtos?**  
4. **¿Qué tipo de participantes tendrás?** Laboratorios de ensayo, calibración, inspección, muestreo, individuos expertos.  
5. **¿Cuántos participantes esperas por ronda y con qué frecuencia?**  
6. **¿El esquema será simultáneo, secuencial, de ronda única o continuo?**  
7. **¿Cómo piensas obtener el valor asignado?** CRM, formulación, laboratorio de referencia, expertos, consenso de participantes.  
8. **¿Los participantes podrán usar distintos métodos?** Si sí, ¿hay métodos que sabes de antemano que no son comparables entre sí?  
9. **¿Vas a pedir incertidumbre de medición a los participantes?** Esto define si conviene usar solo z, o además z’, ζ o En.  
10. **¿Qué tipo de ítem de ensayo usarás?** Material estable, perecedero, artefacto, patrón, muestra ambiental, muestra clínica, datos/imágenes.  
11. **¿Tienes laboratorio propio o aliado para caracterización, homogeneidad y estabilidad bajo 17025?**  
12. **¿Qué funciones quedarán internas y cuáles externas?** Recuerda que diseño del esquema, evaluación del desempeño y autorización del informe no conviene externalizarlas bajo 17043\.  
13. **¿Ya tienes un sistema existente?** ISO 9001, ISO/IEC 17025, BPM, nada formal.  
14. **¿Qué software usarás para estadística y control documental?** Excel, R, Python, LIMS, SharePoint, otro.  
15. **¿Con qué organismo de acreditación o en qué país piensas operar?** Esto importa por el contexto ILAC y criterios locales. ([ILAC – ILAC Live Site](https://ilac.org/publications-and-resources/ilac-policy-series/?utm_source=chatgpt.com))  
16. **¿Qué entregable final necesitas de esta investigación?** Tesis, manual del SGC, matriz de cumplimiento, procedimientos, plan de implementación, o expediente de acreditación.

Respóndeme esas 16 y te lo convierto en una versión mucho más fina: mapa de procesos, matriz cláusula–procedimiento–registro, estructura documental y modelo estadístico aterrizado a tu tipo de ensayo de aptitud.

Perfecto. Con lo que me diste ya se puede aterrizar una propuesta **realmente implementable** para un **Proveedor de Ensayos de Aptitud (PEA)** en **calidad de aire – gases contaminantes (CO, NOx, SO2, O3)**, orientada a **acreditación ONAC** y construida directamente sobre **ISO/IEC 17043:2023** e **ISO 13528:2022**.

Además, por contexto regulatorio, te conviene diseñarlo **ya** con la versión **ISO/IEC 17043:2023**: ONAC informó la transición de tres años desde la publicación de la nueva norma, con fecha límite **31 de mayo de 2026**; también indicó que desde **16 de septiembre de 2024** las nuevas acreditaciones y ampliaciones para PEA se evalúan con la edición 2023\. ONAC también señaló la eliminación de su documento previo CEA-3.0-16 V4 para este tema. ([ONAC](https://onac.org.co/?jet_download=201f7cb27044e824237f790b8247c7acca803cac))

## **Conclusión clave para tu caso**

Tu investigación no debe plantearse como un “manual genérico”, sino como el **diseño documental y operativo de un PEA especializado en gases criterio**, con estas decisiones base:

* **Tipo de esquema:** cuantitativo, para laboratorios de ensayo, de ejecución **simultánea**.  
* **Matriz/ítem:** atmósfera de gas diluida en aire sintético mediante **controlador de flujo másico**.  
* **Valor asignado:** por **CRM** y/o **laboratorio de referencia**, no por consenso de participantes.  
* **Contexto de acreditación:** **ONAC**, bajo **ISO/IEC 17043:2023**.  
* **Base técnica existente:** ya tienes **ISO/IEC 17025**, lo cual es una ventaja enorme para trazabilidad, incertidumbre, calibración y competencia del personal.  
* **Software crítico:** aplicativo web **Shiny en R**, que deberá tratarse como **software validado** dentro del sistema.

La base estadística de ISO 13528 exige que el diseño responda al objetivo, al tipo de dato, a los supuestos estadísticos, a la naturaleza del error y al número esperado de resultados. Además, el proveedor debe describir los métodos de cálculo, la interpretación general y las limitaciones, y asegurar que el software esté adecuadamente validado.

---

## **1\) Qué esquema te conviene y por qué**

Tú elegiste **simultáneo**, y para gases en aire eso es una buena decisión inicial.

Según ISO 13528, un esquema:

* **simultáneo** distribuye o pone a disposición los ítems para medición concurrente en un periodo definido;  
* **secuencial** los circula o aplica por turnos;  
* **single occasion** ocurre una sola vez;  
* **continuo** se repite a intervalos regulares.

### **Recomendación para tu investigación**

Plantea el sistema así:

* **Fase 1:** esquema **simultáneo** para implementación inicial y acreditación.  
* **Fase 2:** arquitectura preparada para migrar a esquema **continuo** cuando definas frecuencia y consolides suficientes rondas para análisis de tendencia.

### **Cómo explicaría los otros tipos en tu investigación**

El texto puede quedar así:

* **Simultáneo:** todos los participantes miden dentro de una misma ventana de tiempo. Es el más apropiado cuando se quiere minimizar deriva temporal y comparar laboratorios bajo condiciones controladas.  
* **Secuencial:** útil cuando se usa un mismo artefacto o sistema que pasa por varios participantes; exige mayor control de estabilidad y deriva.  
* **Single occasion:** útil para pilotos, validaciones iniciales o estudios puntuales.  
* **Continuo:** adecuado para programas maduros, porque permite seguimiento del desempeño en el tiempo, gráficos de tendencia y mayor utilidad para organismos de acreditación.

---

## **2\) La decisión más importante: con 2 participantes no debes usar consenso como base principal**

Este es el punto más delicado de tu diseño.

ISO 13528 dice que, cuando hay **pocos participantes**, el valor asignado debería determinarse idealmente con un procedimiento metrológicamente válido e **independiente de los participantes**, por ejemplo mediante **formulación**, **CRM** o **laboratorio de referencia**. También advierte que, con pocos participantes, la evaluación basada en los propios resultados puede ser poco fiable.

Y además la norma señala que el diseño debe prever qué hacer si **no se alcanza el número mínimo** de participantes esperado.

### **Para tu caso, la política correcta es:**

* **Valor asignado principal:** externo e independiente.  
* **Criterio de evaluación principal:** externo y basado en aptitud para el uso.  
* **Nunca** basar la desviación estándar para evaluación de aptitud de una ronda en los resultados de solo 2 participantes.

### **Entonces, tu esquema debe quedar así**

**Jerarquía de asignación del valor:**

1. **CRM \+ cálculo de dilución dinámica**  
2. **Confirmación por laboratorio de referencia interno**  
3. **Verificación complementaria por estudio independiente interno bajo 17025**

ISO 13528 admite tanto la **formulación** como el uso de **CRM** y también el uso de un **laboratorio** con método de referencia para asignar valor.

---

## **3\) Modelo técnico recomendado para tu PEA de gases**

## **3.1 Alcance técnico propuesto**

**Proveedor de ensayos de aptitud para laboratorios de ensayo que realizan medición de gases contaminantes en aire**, inicialmente para:

* CO  
* NOx  
* SO2  
* O3

usando métodos **US-EPA validados** y atmósferas patrón diluidas en aire sintético mediante controladores de flujo másico.

## **3.2 Tipo de ítem de ensayo**

Tu ítem no es una “muestra convencional” líquida o sólida. En realidad, tu PT item es una **atmósfera generada**. Por eso, en tu sistema debes redefinir el concepto de homogeneidad/estabilidad de manera operativa:

* **homogeneidad** \= equivalencia entre atmósferas generadas bajo el mismo setpoint/condición;  
* **estabilidad** \= capacidad de mantener el valor asignado durante la ventana de medición y, si aplica, durante el transporte o la exposición.

Eso sigue siendo totalmente coherente con ISO 13528, que exige demostrar que los ítems son suficientemente homogéneos y estables para el propósito del esquema.

---

## **4\) Cómo debe quedar el modelo estadístico**

## **4.1 Objetivo estadístico del esquema**

Para tu caso el objetivo principal no debe ser “ver qué promedio sale”, sino:

**evaluar el desempeño de laboratorios frente a un valor asignado independiente y metrológicamente trazable, con criterios predefinidos de aptitud.**

Eso encaja con el enfoque de ISO 13528 para esquemas cuantitativos con valor de referencia externo.

## **4.2 Valor asignado**

Tu procedimiento debe dejar escrito:

* fuente del CRM;  
* trazabilidad metrológica;  
* ecuación de dilución;  
* correcciones aplicables;  
* verificación con laboratorio de referencia;  
* incertidumbre del valor asignado.

ISO 13528 exige declarar el método de asignación y la incertidumbre asociada, y propone el modelo general:

\[  
x\_{pt}=x\_{char}+\\delta\_{hom}+\\delta\_{trans}+\\delta\_{stab}  
\]

y

\[  
u(x\_{pt})=\\sqrt{u^2\_{char}+u^2\_{hom}+u^2\_{trans}+u^2\_{stab}}  
\]

## **4.3 Homogeneidad**

Para un estudio de homogeneidad, ISO 13528 recomienda seleccionar un número de ítems finales envasados o preparados, con **g \> 10** cuando aplique, usar **m ≥ 2** réplicas, y que el método usado para comprobar homogeneidad tenga una repetibilidad suficientemente pequeña, idealmente con **sr/σpt \< 0,5**.

Como criterio de aceptación, el componente entre ítems debe cumplir:

\[  
s\_s \\le 0.3\\sigma\_{pt}  
\]

o equivalente respecto a un error máximo permitido.

### **Adaptación a tu caso**

Como trabajas con atmósferas generadas, yo propondría documentarlo así:

* para cada analito y nivel nominal, generar múltiples atmósferas independientes bajo el mismo setpoint;  
* medirlas con método de referencia bajo condiciones repetibles;  
* estimar la variabilidad entre generaciones;  
* aceptar la condición solo si el componente entre generaciones cumple el criterio de ISO 13528\.

## **4.4 Estabilidad**

ISO 13528 propone un esquema before/after round: medir un grupo antes de distribuir o ejecutar la ronda y otro grupo al final, con el mismo laboratorio y método, y considerar estable el material si:

\[  
|\\bar y\_1 \- \\bar y\_2| \\le 0.3\\sigma\_{pt}  
\]

o equivalente con δE.

### **Adaptación a gases**

Tu procedimiento de estabilidad debería tener tres modalidades:

* **estabilidad intrajornada** del sistema generador;  
* **estabilidad durante la ventana de medición del esquema**;  
* **estabilidad por transporte**, solo si el esquema implica envío o circulación.

Para **O3**, yo sería más exigente en el plan de control porque es el analito más problemático por reactividad y deriva. Eso ya no sale literalmente de la norma, pero es una inferencia técnica razonable para tu campo.

## **4.5 Métodos de medición**

ISO 13528 dice que, si todos reportan el mismo mensurando, normalmente debe haber **un mismo valor asignado**, pero si diferentes métodos no son comparables puede ser necesario asignar valores por subgrupo de método.

Como me dijiste que todos usan **métodos US-EPA validados**, tu política base debe ser:

* **un único valor asignado por analito y nivel**,  
* pero el sistema debe exigir registrar **código de método**, equipo y principio de medición,  
* y dejar prevista la regla de partición por método si aparece bimodalidad o sesgo sistemático por familia instrumental.

## **4.6 Revisión inicial de datos**

Antes de puntuar, ISO 13528 recomienda:

* revisar visualmente los datos;  
* detectar errores groseros;  
* investigar anomalías como bimodalidad;  
* usar preferentemente métodos robustos.

Entonces tu procedimiento estadístico debe obligar a hacer:

1. revisión de unidades y formato;  
2. revisión de cifras significativas;  
3. histograma y/o densidad kernel;  
4. revisión por método;  
5. decisión documentada sobre blunders;  
6. cálculo final.

## **4.7 Qué puntuaciones usar**

Para tu caso, la combinación más sólida sería esta:

### **Principal**

* **z** cuando (u(x\_{pt})) sea despreciable.  
* **z’** cuando la incertidumbre del valor asignado no sea despreciable.

La interpretación convencional del z es:

* (|z| \< 2): satisfactorio  
* (2 \\le |z| \< 3): advertencia  
* (|z| \\ge 3): acción

### **Complementaria**

* **ζ (zeta)** para revisar la coherencia entre el resultado y la **incertidumbre estándar** reportada.  
* **En** como índice opcional cuando el objetivo sea evaluar si el resultado cae dentro de la **incertidumbre expandida** declarada respecto al valor asignado.

ISO 13528 indica que **ζ** y **En** son opciones útiles cuando se recogen incertidumbres, incluso en laboratorios de ensayo, y que pedir la incertidumbre puede ser muy valioso aunque no sea la base única del scoring.

### **Mi recomendación concreta**

* **Scoring oficial del programa:** z o z’  
* **Scoring complementario:** ζ  
* **En:** opcional, no como único criterio

---

## **5\) Sí, debes pedir incertidumbre normal y expandida, incluido el factor k**

Tu decisión aquí fue correcta.

ISO 13528 contempla explícitamente esquemas donde la comparación usa la incertidumbre del participante y reconoce utilidad en pedir incertidumbre incluso en ensayos, no solo en calibración.

### **Entonces, el formulario de reporte debe pedir:**

* resultado (x\_i)  
* unidad  
* incertidumbre estándar (u(x\_i))  
* incertidumbre expandida (U(x\_i))  
* factor de cobertura (k)  
* nivel de confianza declarado  
* método US-EPA  
* equipo/principio de medición  
* fecha y hora de medición

---

## **6\) Diseño documental del sistema de gestión de calidad**

Como tu entregable final es **la documentación del SGC**, te propongo una arquitectura de 4 niveles.

## **Nivel 1: documentos marco**

1. **Manual del SGC del PEA**  
2. **Política de calidad**  
3. **Política de imparcialidad**  
4. **Política de confidencialidad**  
5. **Mapa de procesos**  
6. **Matriz de alcance del PEA**

## **Nivel 2: procedimientos obligatorios/estructurales**

1. Control de documentos  
2. Control de registros  
3. Gestión de riesgos y oportunidades  
4. Gestión de imparcialidad  
5. Gestión de confidencialidad  
6. Revisión de solicitudes, ofertas y contratos  
7. Diseño y planificación de ensayos de aptitud  
8. Gestión de personal, competencia y autorizaciones  
9. Gestión de equipos, patrones y trazabilidad metrológica  
10. Gestión de proveedores externos  
11. Control del sistema informático y validación de software  
12. Gestión de trabajo no conforme  
13. Quejas  
14. Apelaciones  
15. Acciones correctivas y mejora  
16. Auditorías internas  
17. Revisión por la dirección

## **Nivel 3: procedimientos técnicos del esquema de gases**

1. Preparación de atmósferas patrón por dilución dinámica  
2. Uso y verificación de controladores de flujo másico  
3. Gestión de cilindros CRM y aire cero  
4. Asignación del valor y cálculo de incertidumbre  
5. Homogeneidad de atmósferas generadas  
6. Estabilidad del sistema generador durante la ronda  
7. Ejecución del esquema simultáneo  
8. Recepción y validación de resultados de participantes  
9. Tratamiento estadístico según ISO 13528  
10. Emisión de informes individuales y globales

## **Nivel 4: formatos y registros**

* ficha maestra del programa  
* matriz de riesgos del esquema  
* plan estadístico por ronda  
* registro de trazabilidad de CRM y MFC  
* hoja de cálculo del valor asignado  
* registro de homogeneidad  
* registro de estabilidad  
* lista codificada de participantes  
* formulario electrónico de reporte  
* revisión técnica de resultados  
* acta de decisión estadística  
* informe individual  
* informe consolidado  
* registro de quejas y apelaciones  
* matriz de competencias  
* expediente de validación de Shiny/R

---

## **7\) Mapa de procesos propuesto**

Yo dejaría el sistema con este mapa:

### **Estratégicos**

* Dirección estratégica del PEA  
* Gestión de imparcialidad  
* Gestión de riesgos y oportunidades  
* Revisión por la dirección

### **Misionales**

* Revisión de solicitud y diseño del esquema  
* Preparación/generación del ítem  
* Asignación del valor  
* Homogeneidad y estabilidad  
* Ejecución del esquema simultáneo  
* Recepción y validación de datos  
* Análisis estadístico  
* Emisión de informe

### **Soporte**

* Talento humano y competencia  
* Metrología y calibración  
* Infraestructura y ambiente  
* TIC / Shiny / seguridad de la información  
* Gestión documental  
* Compras y proveedores  
* CAPA y mejora

---

## **8\) Qué debe decir tu manual del SGC**

Tu manual no debe ser enorme. Debe dejar claro:

* objeto y alcance del PEA;  
* estructura organizacional;  
* roles y autoridades;  
* relación entre ISO/IEC 17043:2023, ISO 13528:2022 e ISO/IEC 17025;  
* mapa de procesos;  
* control documental;  
* matriz de interacción entre procesos;  
* referencia a los procedimientos y registros aplicables.

Y debes aprovechar que ya tienes 17025 para no duplicar lo que ya existe. Lo correcto es hacer un **sistema integrado**, donde:

* 17025 soporte el laboratorio de referencia, calibraciones, trazabilidad y competencia técnica;  
* 17043 gobierne la condición de **proveedor de ensayos de aptitud**;  
* 13528 gobierne el componente estadístico.

---

## **9\) Qué debe pasar con Shiny en R**

Este punto es crítico para acreditación.

ISO 13528 exige software adecuadamente validado. Y, para un PEA, además el sistema de información usado para recibir, procesar, almacenar y reportar datos debe estar bajo control y validación.

### **Tu expediente de validación del aplicativo debería incluir:**

* especificación funcional;  
* control de versiones;  
* usuarios y perfiles;  
* trazabilidad de cambios;  
* pruebas de captura de datos;  
* pruebas de cálculos estadísticos;  
* pruebas de redondeo;  
* pruebas de bloqueo por unidad incorrecta;  
* pruebas de codificación anónima de participantes;  
* respaldo y recuperación;  
* integridad de base de datos;  
* evidencia de aprobación antes de uso.

### **Pruebas mínimas que yo exigiría**

* cálculo correcto de (x\_{pt}), (u(x\_{pt})), z, z’, ζ, En;  
* manejo de cifras significativas;  
* bloqueo de datos fuera de rango;  
* separación por analito y nivel;  
* trazabilidad de quién cargó, revisó y liberó;  
* generación correcta de informe individual y consolidado.

---

## **10\) Propuesta de reglas documentadas para tu programa**

Tu sistema debería fijar por escrito reglas como estas:

### **Regla 1\. Valor asignado**

“El valor asignado será determinado a partir de CRM y/o laboratorio de referencia con trazabilidad metrológica documentada; no se usará consenso de participantes como base principal en rondas con baja participación.”

### **Regla 2\. Número mínimo de participantes**

“Cuando el número de participantes sea reducido, la evaluación seguirá siendo válida solo si el valor asignado y el criterio de aptitud son externos e independientes de los resultados de los participantes.”

### **Regla 3\. Criterio de aptitud**

“La desviación estándar para evaluación de aptitud (\\sigma\_{pt}) se establecerá por aptitud para el uso, desempeño esperado del método o criterio técnico predefinido; no se derivará de la dispersión de una ronda con escasa participación.”

### **Regla 4\. Incertidumbre reportada**

“Los participantes deberán reportar resultado, incertidumbre estándar, incertidumbre expandida y factor k.”

### **Regla 5\. Datos anómalos**

“Los errores groseros evidentes serán tratados según procedimiento aprobado; la exclusión de resultados no impedirá la evaluación del participante.”

### **Regla 6\. Métodos**

“Todos los participantes reportarán el método US-EPA aplicado. Se podrá subdividir el análisis por método cuando existan evidencias técnicas o estadísticas de no comparabilidad.”

---

## **11\) Qué criterio usar para σpt en tu caso**

Este es otro punto que tu investigación debe resolver bien.

ISO 13528 permite varias formas de definir (\\sigma\_{pt}): por criterio externo, juicio experto, experiencia previa o modelo general.

### **Para tu caso, el orden recomendado es:**

1. **criterio de aptitud para el uso/regulatorio**  
2. **desempeño esperado del método**  
3. **experiencia histórica de rondas previas**  
4. **nunca** la dispersión de dos participantes

### **Redacción recomendada para tu tesis/proyecto**

“Durante la fase inicial del programa, la desviación estándar para evaluación de aptitud se definirá por criterio externo de aptitud para el uso y/o por especificación técnica del método, dado que el número inicial de participantes no permite una estimación robusta y fiable basada en consenso.”

---

## **12\) Relación con ONAC e ILAC**

ONAC reconoce la acreditación de PEA bajo **ISO/IEC 17043**, y su marco público para PEA remite a esa norma como base del servicio de acreditación. ([ONAC](https://onac.org.co/servicios/proveedores-de-ensayo-de-aptitud/))  
Además, ILAC mantiene vigente **ILAC P9:01/2024**, que es la política aplicable a los organismos de acreditación para el uso de actividades de ensayos de aptitud en acreditación. ([ILAC – ILAC Live Site](https://ilac.org/publications-and-resources/ilac-policy-series/))

Para tu investigación, eso significa que tu documentación debe quedar preparada no solo para “operar”, sino para que ONAC pueda revisar:

* competencia del proveedor;  
* imparcialidad;  
* diseño estadístico;  
* trazabilidad del valor asignado;  
* control del software;  
* competencia del personal autorizado;  
* validez del informe emitido.

---

## **13\) Qué entregable final te sugiero construir**

Yo estructuraría tu investigación en 6 productos documentales:

### **Producto 1**

**Manual del SGC del PEA para gases en aire**

### **Producto 2**

**Matriz de correspondencia requisito–documento–evidencia**

* ISO/IEC 17043:2023  
* ISO 13528:2022  
* evidencia documental

### **Producto 3**

**Paquete de procedimientos del sistema**  
al menos 15–20 procedimientos

### **Producto 4**

**Plan estadístico maestro del programa**

* valor asignado  
* incertidumbre  
* homogeneidad  
* estabilidad  
* scoring  
* reglas de decisión

### **Producto 5**

**Especificación y validación del aplicativo Shiny**

* URS  
* casos de prueba  
* resultados esperados  
* aprobación

### **Producto 6**

**Modelo de informes**

* informe individual  
* informe general  
* anexos gráficos

---

## **14\) Recomendación de estructura del plan estadístico maestro**

Ese documento debe existir sí o sí. Yo lo dejaría así:

1. objeto  
2. alcance por analito  
3. niveles de concentración  
4. fuente del valor asignado  
5. ecuaciones de cálculo  
6. modelo de incertidumbre  
7. plan de homogeneidad  
8. plan de estabilidad  
9. criterio para (\\sigma\_{pt}) o (\\delta\_E)  
10. criterio para uso de z / z’ / ζ / En  
11. tratamiento de blunders  
12. revisión visual y robusta  
13. tratamiento de resultados censurados, si aplica  
14. reglas de redondeo  
15. reglas para subgrupos por método  
16. contenido mínimo del informe

---

## **15\) Las preguntas que todavía necesito para dejarlo casi en versión final**

Ya no necesito 16 preguntas. Solo estas **5** son realmente críticas:

1. **¿El esquema será in situ con generación dinámica frente al laboratorio participante, o planeas enviar cilindros/preparaciones a los participantes?**  
2. **¿Qué rangos de concentración y unidades vas a cubrir para CO, NOx, SO2 y O3?**  
3. **¿Quieres arrancar con los 4 analitos a la vez o prefieres una implementación por fases?**  
4. **¿Cuál será el criterio de aptitud para (\\sigma\_{pt}): regulatorio, desempeño del método, incertidumbre objetivo, o combinación?**  
5. **¿La evaluación la emitirás por laboratorio, por analito y nivel, o también por método/equipo?**

Respóndeme esas 5 y te lo convierto en una versión todavía más fina: **índice completo del manual**, **lista maestra de procedimientos y formatos**, y una **matriz cláusula–documento–registro** lista para desarrollo documental.

Perfecto. Con esto el diseño ya quedó **casi cerrado** para un **PEA in situ** de **CO, NOx, SO2 y O3** orientado a **acreditación ONAC**. Además, como vas por ONAC, conviene documentarlo ya sobre **ISO/IEC 17043:2023**: ONAC publicó la transición a esa edición y la eliminación del CEA-3.0-16 V4, en línea con el plazo internacional de ILAC que vence el **31 de mayo de 2026**. ([ONAC](https://onac.org.co/documentos/nte-3-3-73/?utm_source=chatgpt.com))

## **Lo que no estaba claro: qué era el criterio del punto 4**

En tu caso, **σpt** no es “la desviación estándar que salga de los laboratorios”.  
**σpt** es el **criterio de evaluación del desempeño**: el ancho estadístico contra el que comparas el error de cada laboratorio para decidir si su resultado es satisfactorio o no. ISO 13528 lo define como la “standard deviation for proficiency assessment”, y deja claro que no todos los esquemas la derivan de la dispersión observada; además, para pocos participantes recomienda usar **valor asignado independiente** y **criterio externo**, no la dispersión de una sola ronda.

En términos simples:

* **xpt** \= valor asignado  
* **xi** \= resultado del laboratorio  
* **D \= xi \- xpt** \= error frente al valor asignado  
* **σpt** \= tolerancia estadística para juzgar ese error  
* **z \= (xi \- xpt) / σpt**

ISO 13528 también permite trabajar con **δE** como criterio de error permitido, y allí la lógica práctica es equivalente: comparas el error del laboratorio con un límite predefinido de aptitud para el uso.

## **Cómo te recomiendo definir ese criterio en tu esquema**

Para tu programa, con **mínimo 2 laboratorios**, el criterio debe ser **externo y predefinido**. No debes calcular σpt a partir de la dispersión de la ronda.

La forma más sólida de documentarlo es esta:

\[  
\\delta\_E \= \\max (a% \\cdot x\_{pt},\\ b% \\cdot \\text{span})  
\]

y luego:

\[  
\\sigma\_{pt} \= \\delta\_E / 3  
\]

Eso te da un sistema estable y defendible, porque:

* el término **a % de xpt** controla el error relativo al nivel real;  
* el término **b % del span** evita que los niveles bajos queden con tolerancias absurdamente pequeñas;  
* al fijarlo antes de la ronda, tu evaluación no depende del número de participantes.

Esa fórmula no viene escrita así en la norma; es la forma práctica en que yo la dejaría documentada para un programa real de gases. La base normativa es que ISO 13528 permite evaluar con **criterio externo de aptitud para el uso** y compara el error del laboratorio con **δE** o con **σpt**.

## **Ejemplo para que se entienda**

Supón que en una ronda para CO:

* valor asignado: **40 ppm**  
* criterio definido por el programa: **δE \= ±10 % del valor asignado**  
* entonces **δE \= ±4 ppm**  
* equivalente: **σpt \= 4/3 \= 1,33 ppm**

Si un laboratorio reporta **42 ppm**:

* (D \= 42 \- 40 \= 2\) ppm  
* (z \= 2 / 1,33 \= 1,5)

Ese resultado sería satisfactorio bajo la interpretación usual de z. ISO 13528 usa la convención de señales de advertencia y acción con los valores 2 y 3 para z y también admite usar z’, ζ y En cuando la incertidumbre es relevante.

## **Qué te recomiendo específicamente para tu caso**

### **1\) Tipo de esquema**

Tu esquema queda como:

**PEA cuantitativo, simultáneo, in situ, para laboratorios de ensayo de calidad de aire, con evaluación por laboratorio–analito–nivel.** La propia ISO 13528 reconoce los esquemas simultáneos y define el ensayo de aptitud como evaluación del desempeño frente a criterios preestablecidos.

### **2\) Ítem de ensayo**

Tu “ítem” no será un cilindro enviado, sino una **atmósfera generada in situ** a partir de:

* gas fuente CRM,  
* aire sintético / aire cero,  
* controlador(es) de flujo másico,  
* sistema de dilución dinámica,  
* laboratorio de referencia interno para verificación.

Eso encaja muy bien con que el valor asignado sea **independiente de los participantes**, usando CRM y laboratorio de referencia. ISO 13528 contempla valor asignado por **formulación**, por **CRM** y por resultados de laboratorio(s) expertos o de referencia.

### **3\) Valor asignado**

Para ti, la jerarquía correcta es:

1. **cálculo metrológico de la dilución dinámica**,  
2. **trazabilidad al CRM**,  
3. **confirmación por el laboratorio de referencia interno**,  
4. **incertidumbre del valor asignado**.

ISO 13528 pide que el método de asignación y su incertidumbre estén descritos y reportados, y usa el modelo general:

\[  
x\_{pt}=x\_{char}+\\delta\_{hom}+\\delta\_{trans}+\\delta\_{stab}  
\]

\[  
u(x\_{pt})=\\sqrt{u\_{char}^2+u\_{hom}^2+u\_{trans}^2+u\_{stab}^2}  
\]

Además, como tu esquema es **in situ**, el término de transporte puede ser justificadamente **nulo o despreciable** si no hay envío del ítem; la estabilidad durante la ventana de medición sí debe evaluarse.

### **4\) Niveles de concentración**

Aquí hay una corrección importante: no debes dejar el diseño como “el rango de calibración que tenga cada instrumento”.  
Eso hace que cada participante termine evaluado en condiciones distintas.

Lo correcto es que **el PEA defina niveles nominales comunes** por analito, y el laboratorio participa solo si su rango rutinario cubre esos niveles. Yo lo dejaría así:

* **Nivel 0:** aire cero / verificación de cero  
* **Nivel 1:** bajo, alrededor de 20–30 % del rango objetivo  
* **Nivel 2:** medio, alrededor de 50–60 %  
* **Nivel 3:** alto, alrededor de 80–90 %

Así el programa compara a todos en los mismos puntos metrológicos. ISO 13528 insiste en que el diseño estadístico debe responder al objetivo, al tipo de dato y al número esperado de resultados.

### **5\) Métodos**

Como todos usan **métodos US-EPA validados**, tu política base puede ser:

* **un solo valor asignado por analito y nivel**,  
* y solo separar subgrupos si aparece evidencia técnica o estadística de poblaciones distintas.

ISO 13528 prevé subpoblaciones por método cuando sea necesario.

### **6\) Incertidumbre**

Sí debes pedir:

* resultado,  
* incertidumbre estándar,  
* incertidumbre expandida,  
* factor (k),  
* nivel de confianza,  
* método,  
* equipo,  
* fecha/hora.

ISO 13528 considera útil pedir incertidumbre incluso cuando no sea el criterio principal de puntuación, y permite usar **ζ** y **En** para revisar la coherencia del resultado con la incertidumbre declarada.

### **7\) Estadístico oficial**

Yo lo dejaría así:

* **oficial:** z o z’  
* **complementario:** ζ  
* **opcional:** En

Y aplicaría esta regla:

* si (u(x\_{pt}) \< 0,3\\sigma\_{pt}) o (u(x\_{pt}) \< 0,1\\delta\_E), usas **z**;  
* si no se cumple, pasas a **z’** o complementas con **ζ**.

Eso está directamente alineado con ISO 13528\.

### **8\) Unidad de evaluación**

Tu decisión de evaluar **por laboratorio, analito y nivel** es correcta.  
No te recomiendo un “score global único” para los 4 gases, porque ISO 13528 advierte que los puntajes combinados entre distintos mensurandos pueden ocultar sesgos importantes. Lo mejor es:

* resultado individual por analito–nivel,  
* resumen del laboratorio con conteo de señales satisfactorias/advertencia/acción.

---

## **Así quedaría la documentación del SGC**

Yo lo estructuraría en 3 bloques.

### **A. Documentos marco**

1. Manual del SGC del PEA  
2. Política de calidad  
3. Política de imparcialidad  
4. Política de confidencialidad  
5. Alcance del PEA  
6. Mapa de procesos  
7. Matriz de roles, autoridades y suplencias

### **B. Procedimientos del sistema**

1. Control documental y de registros  
2. Gestión de riesgos y oportunidades  
3. Competencia, formación y autorizaciones  
4. Compras y control de proveedores  
5. Trabajo no conforme  
6. Quejas y apelaciones  
7. CAPA y mejora  
8. Auditorías internas  
9. Revisión por la dirección

### **C. Procedimientos técnicos del esquema in situ**

1. Diseño y planificación del esquema de EA  
2. Selección de analitos, niveles y cronograma  
3. Gestión de CRM, aire cero y MFC  
4. Generación dinámica de atmósferas in situ  
5. Asignación del valor y cálculo de incertidumbre  
6. Homogeneidad / equivalencia del sistema generador  
7. Estabilidad durante la ronda  
8. Recepción y validación de resultados  
9. Evaluación estadística según ISO 13528  
10. Emisión de informes individuales y globales  
11. Validación y control del aplicativo Shiny/R

## **Registros que te conviene crear desde ya**

* plan maestro del programa,  
* ficha de cada ronda,  
* registro de trazabilidad de CRM,  
* registro de calibración/verificación de MFC,  
* hoja de cálculo del valor asignado,  
* estudio de incertidumbre de xpt,  
* registro de estabilidad,  
* bitácora de visita in situ,  
* formato de resultados del participante,  
* revisión técnica de datos,  
* acta de decisión estadística,  
* informe individual,  
* informe consolidado,  
* expediente de validación de Shiny.

ISO 13528 exige métodos estadísticos válidos, descripción de los métodos de cálculo a los participantes y software adecuadamente validado.

---

## **Punto delicado: con 2 participantes**

Con solo 2 laboratorios, tu esquema puede funcionar **siempre que**:

* el valor asignado sea independiente,  
* el criterio de aceptación sea externo,  
* no uses la dispersión de los 2 laboratorios como σpt.

Eso es exactamente lo que más te conviene hacer en la fase inicial.