Evaluación de la "Comunicación Detallada" (Fuente 1\) frente a los requisitos establecidos en la norma ISO/IEC 17043:2023.

El documento analizado es técnicamente sólido y **cumple satisfactoriamente con la mayoría de los requisitos críticos** de comunicación e instrucciones a los participantes establecidos en la cláusula 7 de la norma. A continuación, presento la auditoría detallada desglosada por requisitos normativos.

### 1\. Instrucciones a los Participantes (Cláusula 7.3.5)

La norma exige instrucciones documentadas y detalladas para garantizar la validez de los resultados.

* **Tratamiento como muestra de rutina (7.3.5.2 a):**  
* *Evaluación:* **CUMPLE.**  
* *Evidencia:* El documento instruye explícitamente: "Se espera que los participantes analicen los ítems de ensayo... de la misma manera que analizan sus muestras rutinarias, utilizando sus procedimientos operativos estándar" 1\.  
* **Factores que influyen en la medición (7.3.5.2 b):**  
* *Evaluación:* **CUMPLE.**  
* *Evidencia:* Se detallan los niveles de concentración, los rangos relevantes (nmol/mol y/o umol/mol) 2 y la naturaleza dinámica de la generación de la muestra 3\.  
* **Condiciones ambientales y preparación (7.3.5.2 c, e):**  
* *Evaluación:* **CUMPLE.**  
* *Evidencia:* Se define un protocolo estricto de "Día 1 – Instalación y Calibración" y "Día 2-3 – Traslado al laboratorio", especificando condiciones de estabilización ("equipos quedan encendidos") y suministro eléctrico (110V AC) 4, 5\.  
* **Registro y reporte de resultados (7.3.5.2 f):**  
* *Evaluación:* **CUMPLE.**  
* *Evidencia:* Se especifica el reporte de mediciones "promedio horaria" con "tres (3) cifras decimales" y la remisión de datos crudos 1\. Además, se hace mandatorio el reporte de la incertidumbre expandida ($k=2$), lo cual es crítico para el cálculo del *En-score* 6\.

### 2\. Diseño Estadístico y Evaluación del Desempeño (Cláusula 7.2.2 y 7.4)

El proveedor debe comunicar los criterios de evaluación y el diseño estadístico.

* **Determinación del Valor Asignado (7.2.3):**  
* *Evaluación:* **CUMPLE (Con Observación).**  
* *Evidencia:* Se indica que el valor asignado es determinado por CALAIRE mediante generación dinámica trazable a estándares internacionales (MRC y fotómetro nivel 2 para ozono) 3, 5\.  
* *Observación:* La norma ISO 13528 sugiere describir cómo se calcula la incertidumbre del valor asignado ($u(x\_{pt})$). El documento menciona las fuentes de incertidumbre (Caracterización, Estabilidad, Homogeneidad) 7, lo cual es técnicamente correcto y transparente.  
* **Criterios de Evaluación (7.4.2):**  
* *Evaluación:* **CUMPLE.**  
* *Evidencia:* Se definen claramente los estadísticos de desempeño: Puntuación Zeta ($\\zeta$-score) y Puntuación $E\_n$ ($E\_n$-score), alineados con la ISO 13528:2022 7\. Se establecen los criterios de aceptación ($|z| \\le 2.0$ y $|E\_n| \\le 1.0$) 6\.

### 3\. Comunicación del Esquema (Cláusula 7.1.2)

El proveedor debe facilitar información detallada sobre el esquema.

* **Objetivos y Criterios de Participación (7.1.2.1 a, b):**  
* *Evaluación:* **CUMPLE.**  
* *Evidencia:* El objetivo es evaluar el desempeño en SO₂, NO/NO₂, CO y O₃ 8\. Se definen los requisitos de equipamiento (analizadores, calibradores, aire cero) como mandatorios 9\.  
* **Cronograma y Plazos Críticos (7.1.2.1 e):**  
* *Evaluación:* **CUMPLE PARCIALMENTE (Depende de adjuntos).**  
* *Evidencia:* El documento refiere a documentos adjuntos (*F-PSEA-01* y *F-PSEA-02*) para las fechas clave 9\. Mientras los adjuntos existan, el requisito se cumple.  
* **Confidencialidad (7.1.2.1 d / 4.2):**  
* *Evaluación:* **CUMPLE.**  
* *Evidencia:* Se garantiza la confidencialidad mediante códigos únicos y se exige la firma de un compromiso de no confabulación 10\.

### 4\. Hallazgos y Oportunidades de Mejora

A pesar del alto nivel técnico, identifico los siguientes puntos para fortalecer el cumplimiento con la ISO/IEC 17043:2023:

* **Definición de la Desviación Estándar para la Evaluación ($\\sigma\_{pt}$):**El documento menciona el uso del *z-score*, cuya fórmula requiere una desviación estándar para la evaluación de la aptitud ($\\sigma\_{pt}$) 11\. El documento actual *no especifica* cómo se determinará este valor (e.g., ¿será un valor fijo por criterio regulatorio, desviacion estándar robusta de los participantes, o un modelo general como Horwitz?) 12, 13\.  
* *Recomendación:* Especificar el origen de $\\sigma\_{pt}$ en la Sección 7 para que los participantes sepan contra qué variabilidad se les evalúa.  
* **Manejo de Apelaciones y Quejas (7.6 y 7.7):**La ISO 17043 exige tener procesos documentados para quejas y apelaciones y que la descripción de estos procesos esté disponible para las partes interesadas 14, 15\.  
* *Recomendación:* Incluir un breve párrafo o un enlace/referencia sobre cómo un participante puede apelar una evaluación de desempeño no satisfactoria.  
* **Seguridad y Transporte (7.3.4):**Si bien se menciona el embalaje de equipos, no se hace mención explícita a la seguridad en el manejo de los cilindros de gas patrón que los participantes deben llevar (Cláusula 7.3.4.4 sobre etiquetado y seguridad) 16\.  
* *Recomendación:* Reforzar la sección de transporte recordando el cumplimiento de normativa de transporte de mercancías peligrosas para los cilindros de gas.

### Conclusión del Auditor

El documento **"Comunicación Detallada EA"** demuestra una planificación técnica robusta compatible con un proveedor de ensayos de aptitud competente bajo **ISO/IEC 17043**. Las instrucciones técnicas para la medición *in situ* son excelentes. Para asegurar la conformidad total, se recomienda clarificar el origen estadístico de la $\\sigma\_{pt}$ y referenciar el proceso de apelaciones.

