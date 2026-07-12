evaluación detallada del documento **"P-PSEA-01 Protocolo General EA"** frente a las normas **ISO/IEC 17043:2023** e **ISO 13528:2022**.

Adicionalmente, realizo el **Análisis de Brechas (Gap Analysis)** identificando los elementos críticos que el aplicativo (**Manual v0.4.0**) ejecuta y resuelve técnicamente, pero que el protocolo omite o no define con la suficiente precisión normativa.

### PARTE I: Auditoría del Protocolo P-PSEA-01 vs. Normativa

#### 1\. Gestión y Recursos (ISO/IEC 17043 Cláusulas 4, 5 y 6\)

* **Imparcialidad y Confidencialidad (4.1, 4.2):**  
* **Evaluación:** **CONFORME.**  
* **Evidencia:** El protocolo define una "Política de conflicto de intereses" robusta, prohibiendo explícitamente que el personal involucrado en la preparación o caracterización participe como evaluado 1\. Se garantiza el uso de códigos para el anonimato y se establecen restricciones claras para la comunicación grupal.  
* **Personal y Roles (6.2):**  
* **Evaluación:** **CONFORME.**  
* **Evidencia:** Se definen claramente las responsabilidades del Coordinador, Estadístico, Ingeniero Operativo y Experto en Calidad del Aire. Es destacable que se asigna explícitamente al **Estadístico** la autoridad para identificar valores atípicos y evaluar homogeneidad 1, cumpliendo con el requisito de competencia estadística.  
* **Subcontratación (6.4):**  
* **Evaluación:** **CONFORME.**  
* **Evidencia:** El protocolo declara explícitamente que CALAIRE es el "único organizador" y prohíbe subcontratar la planificación, evaluación del rendimiento y autorización de informes, alineándose estrictamente con ISO/IEC 17043:2023 (6.4.1) 1\.

#### 2\. Diseño y Planificación (ISO/IEC 17043 Cláusula 7.2)

* **Instrucciones a Participantes (7.3.5):**  
* **Evaluación:** **EXCELENTE.**  
* **Evidencia:** Las instrucciones técnicas para la instalación, suministro eléctrico, verificación de fugas y seguridad (uso de reguladores, venteo de manifold) son exhaustivas y mitigan riesgos operativos que podrían invalidar el ensayo 1\.  
* **Diseño Estadístico (7.2.2):**  
* **Evaluación:** **CONFORME PARCIALMENTE.**  
* **Evidencia:** Se definen los puntajes ($z, z', E\_n$) y se mencionan las estadísticas robustas 2\.  
* **Observación:** El protocolo indica que la desviación estándar para la evaluación ($\\sigma\_{pt}$) se calcula mediante "interpolación lineal... acordados por Laboratorios de Referencia" 2\. Esto es un criterio externo (fitness for purpose). Sin embargo, no detalla qué sucede si el desempeño del grupo es mejor o peor de lo esperado (ver discrepancia con el aplicativo más adelante).

### PARTE II: Análisis de Brechas (Omisiones del Protocolo vs. Capacidades del Aplicativo)

El aplicativo (Manual v0.4.0) implementa controles matemáticos rigurosos según ISO 13528 que el Protocolo P-PSEA-01 menciona de forma genérica u omite.

#### 1\. Definición Específica de Algoritmos Robustos (ISO 13528 Anexo C)

* **Lo que dice el Protocolo:** Menciona el uso de "estadísticas robustas" para minimizar la influencia de valores atípicos y menciona el "valor de consenso" 2\.  
* **Lo que hace el Aplicativo:** Implementa específicamente el **Algoritmo A** con escala iterativa, **MADe** (Median Absolute Deviation) y **nIQR** (Normalized IQR) 3-6.  
* **La Omisión:** El protocolo **debe especificar** cuál de estos métodos es el primario para la determinación del valor asignado cuando se usa consenso. No basta con decir "estadísticas robustas"; la norma exige transparencia en el método exacto (p.ej., "Se utilizará el Algoritmo A según ISO 13528 Anexo C").

#### 2\. Criterios Cuantitativos de Homogeneidad y Estabilidad (ISO 13528 Cláusula 9 y Anexo B)

* **Lo que dice el Protocolo:** Indica que las pruebas "están descritos en los Procedimientos para cada contaminante" 1\.  
* **Lo que hace el Aplicativo:** Realiza un ANOVA de un factor y aplica criterios estrictos:  
* **Homogeneidad:** Compara la varianza entre muestras ($s\_s$) contra el criterio $0.3 \\times \\sigma\_{pt}$ o el criterio expandido considerando $s\_w$ 7, 8\.  
* **Estabilidad:** Calcula la diferencia absoluta $D \= |\\bar{\\bar{x}}*{hom} \- \\bar{\\bar{x}}*{stab}|$ y verifica si $D \\le 0.3 \\sigma\_{pt} \+ 2u$ 9\.  
* **La Omisión:** El protocolo general debería establecer el **criterio de aceptación política**. Por ejemplo: *"Se aceptará el lote solo si la varianza entre muestras no excede el 30% de la desviación estándar de la aptitud ($0.3\\sigma\_{pt}$), verificado mediante el aplicativo validado"*. Dejar esto solo en los procedimientos específicos fragmenta la política de calidad del proveedor.

#### 3\. Manejo de Incertidumbre en la Evaluación (ISO 13528 Cláusula 9.5)

* **Lo que dice el Protocolo:** Menciona el uso de **z'-score** cuando la incertidumbre es significativa y el **En-score** 1, 2\.  
* **Lo que hace el Aplicativo:** Automatiza la decisión de usar $z$ o $z'$ basándose en si $u(x\_{pt}) \> 0.3 \\sigma\_{pt}$ 10\. También permite el cálculo de **Zeta-score ($\\zeta$)** 10\.  
* **La Omisión:** El protocolo debe declarar el **criterio de decisión**. ¿Cuándo se activará el $z'$? El aplicativo usa el criterio estándar de ISO 13528 ($u \> 0.3\\sigma$), pero el protocolo debe formalizar esa regla de decisión para que los participantes sepan de antemano bajo qué condiciones su evaluación incluirá la incertidumbre del valor asignado.

#### 4\. Tratamiento de Grupos Pequeños ($n \< 12$ o $n \< 5$)

* **Lo que dice el Protocolo:** No menciona procedimientos específicos para bajo número de participantes.  
* **Lo que hace el Aplicativo:** El aplicativo tiene validaciones como "Insufficient data" para el Algoritmo A si $p \< 3$ y ajusta cálculos 5, 11\. También permite métodos alternativos como usar un valor de referencia externo o métodos de consenso simplificados (Mediana/MADe) 12\.  
* **La Omisión (CRÍTICA):** Dado que los EA de gases a menudo tienen pocos participantes, el protocolo **debe** describir la estrategia para $n$ pequeño (ISO 17043 7.2.2.3). Debe indicar: *"En caso de $n \< X$, el Coordinador no usará el consenso de participantes sino un Valor de Referencia o el Procedimiento de Horn/Mediana, procesado a través del aplicativo"*.

#### 5\. Compatibilidad Metrológica

* **Lo que dice el Protocolo:** Menciona trazabilidad y MCR, y el uso de $E\_n$ 2\.  
* **Lo que hace el Aplicativo:** Tiene una función específica de "Compatibilidad Metrológica" que calcula un índice $D$ para comparar el valor de referencia ($x\_{ref}$) contra el consenso ($x\_{consenso}$) validando si existe sesgo en el grupo 12, 13\.  
* **La Omisión:** El protocolo no menciona cómo se valida el valor asignado cuando este proviene de consenso frente a un valor de referencia (validación cruzada). Esta es una herramienta potente de calidad que el aplicativo ofrece y el protocolo ignora.

### Recomendaciones para la Actualización del P-PSEA-01

1. **Vincular el Aplicativo al SGC:** Mencionar explícitamente en la sección "Procesamiento de datos" que los cálculos estadísticos se realizan mediante el software validado "PT App v0.4.0" (o la versión vigente), el cual cumple los algoritmos de ISO 13528\.  
2. **Formalizar Criterios Estadísticos:** Trasladar los criterios de decisión críticos del Manual del Aplicativo al Protocolo (Umbral de incertidumbre para usar z', criterio $0.3\\sigma\_{pt}$ para homogeneidad).  
3. **Plan de Contingencia Estadística:** Añadir un párrafo sobre el manejo de grupos pequeños ($n \< 5$), aprovechando las opciones que ya permite el software (cambio de método de Valor Asignado).

