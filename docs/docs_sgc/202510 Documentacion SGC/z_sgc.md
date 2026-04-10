Esta es una propuesta inicial para el diseño de un Sistema de Gestión de Calidad (SGC) integrado para un Proveedor de Ensayos de Aptitud (PEA) bajo los requisitos de la norma ISO/IEC 17043:2023 y el soporte estadístico de la ISO 13528:2022.

Dado que la ISO 17043 es la norma de requisitos de competencia y gestión, y la ISO 13528 es la guía técnica estadística, el sistema se estructurará con la 17043 como el "esqueleto" administrativo y la 13528 como el "cerebro" técnico-estadístico.

---

# PROPUESTA DE DISEÑO DEL SISTEMA DE GESTIÓN DE CALIDAD (ISO 17043 \+ ISO 13528\)

## **1\. Estructura Documental del Sistema**

El SGC debe ser dinámico y basado en riesgos. Se propone una pirámide documental:

1. **Nivel 1 \- Política y Objetivos de Calidad:** Manual de Calidad (Declaración de política, estructura, compromiso de imparcialidad).  
2. **Nivel 2 \- Procedimientos e Instructivos (REQUISITOS ISO 17043):**  
   * *Procedimiento de Imparcialidad y Confidencialidad.*  
   * *Procedimiento de Revisión de Solicitudes, Contratos y Tenders.*  
   * *Procedimiento de Compras y Servicios Externos* (Crítico para la producción de ítems).  
   * *Procedimiento de Gestión de Quejas, Apelaciones y Retroalimentación.*  
   * *Procedimiento de Control de Registros y Datos.*  
3. **Nivel 3 \- Planes Técnicos y Protocolos (NEXO CON ISO 13528):**  
   * *Plan de Diseño Estadístico del Esquema* (Definición de objetivos, tipos de datos).  
   * *Protocolo de Determinación de Valores Asignados e Incertidumbre.*  
   * *Protocolo de Evaluación del Desempeño (Cálculo de z-scores, etc.).*  
   * *Protocolo de Homogeneidad y Estabilidad.*  
4. **Nivel 4 \- Registros y Formatos:** Matrices de trazabilidad, resultados de participantes, reportes finales.

---

## **2\. Bloques Funcionales del Sistema**

### BLOQUE 1: Gestión de los Recursos y Requisitos Generales (ISO 17043 Cláusulas 4, 5 y 6\)

Este bloque asegura que el laboratorio tiene "con qué" operar.

* **Imparcialidad y Confidencialidad (Cl. 4):**  
  * Implementar un análisis de riesgos continuo para identificar amenazas a la imparcialidad (ej. presión financiera para que todos aprueben).  
  * Firmas de acuerdos de confidencialidad con el personal y proveedores externos.  
* **Estructura (Cl. 5):**  
  * Definir un organigrama donde se separen funciones comerciales de las técnicas (para evitar conflictos de interés).  
  * Designar un **Comité Técnico Asesor** (requisito clave para la validez técnica y estadística).  
* **Personnel (Cl. 6.2):**  
  * *Punto Crítico:* Definir la competencia del "Experto Estadístico". La ISO 17043 exige acceso a esta pericia.  
  * Matrices de competencia para el personal que valida la homogeneidad y estabilidad.  
* **Instalaciones y Equipos (Cl. 6.3):**  
  * Control de condiciones ambientales para el almacenamiento de muestras (estabilidad física).  
  * Trazabilidad metrológica de los equipos usados para la caracterización de los ítems (si se hace internamente).  
* **Servicios Externos (Cl. 6.4):**  
  * **Restricción:** No se puede subcontratar el diseño del esquema ni la evaluación del desempeño.  
  * Establecer criterios estrictos para proveedores de materiales de referencia o servicios de transporte.

### BLOQUE 2: Gestión de Procesos Técnicos (Núcleo del Sistema \- Integración ISO 17043 Cl. 7 \+ ISO 13528\)

Aquí es donde ocurre la magia del ensayo de aptitud.

#### A. Diseño y Planificación (ISO 17043 Cl. 7.2 | ISO 13528 Cl. 5\)

El sistema debe forzar la definición *antes* de iniciar.

* **Plan del Esquema:** Definir si es cuantitativo o cualitativo.  
* **Diseño Estadístico (ISO 13528):**  
  * Definir la distribución esperada de resultados (Normal, Poisson, etc.).  
  * Establecer el número mínimo de participantes (si es bajo \< 10-15, aplicar métodos alternativos según ISO 13528).  
  * Elegir el modelo de error (Modelo básico: $x\_i \= \\mu \+ \\epsilon\_i$).

#### B. Producción y Manejo de Ítems (ISO 17043 Cl. 7.3 | ISO 13528 Cl. 6\)

El SGC debe asegurar que la muestra es válida antes de enviarla.

* **Homogeneidad y Estabilidad (ISO 13528 Anexo B / Cl. 6.1):**  
  * *Procedimiento:* Ensayar un número suficiente de muestras al azar ($n \\geq 10$) de la misma partida.  
  * *Criterio de aceptación:* La incertidumbre por inhomogeneidad debe ser pequeña comparada con la desviación estándar para la evaluación de la aptitud ($\\sigma\_{pt}$).  
  * Monitoreo continuo de condiciones de almacenamiento y transporte.  
* **Instrucciones a Participantes:** Protocolos claros para evitar errores de "blunder" (ej. unidades incorrectas), que son la causa principal de "valores atípicos" según ISO 13528\.

#### C. Determinación de Valores Asignados (ISO 17043 Cl. 7.2.3 | ISO 13528 Cl. 7-9)

Este es el paso más crítico para la validez. El sistema debe documentar cómo se elige el valor "verdadero".

* **Opciones (ISO 13528):**  
  1. *Valor de Referencia Certificado:* Trazable a un CRM (ideal, pero costoso).  
  2. *Valor de Referencia (medida):* Asignado por un laboratorio de referencia (NMI).  
  3. *Valor de Consenso (Expertos):* Promedio de laboratorios expertos.  
  4. *Valor de Consenso (Participantes):* Promedio robusto de los resultados de la ronda.  
* **Requisito del Sistema:** El software o planilla de cálculo debe aplicar métodos robustos (ej. Algoritmo A, Mediana, MADe) para evitar que los valores atípicos distorsionen el valor asignado.

#### D. Análisis de Datos y Evaluación del Desempeño (ISO 17043 Cl. 7.4 | ISO 13528 Cl. 7, 10\)

* **Tratamiento de Datos (ISO 13528 Cl. 6.3 \- 6.6):**  
  * *Detección de Errores Groseros (Blunders):* Revisión visual (histogramas, diagramas de densidad kernel) y lógica antes de calcular estadísticas.  
  * *Valores Atípicos (Outliers):* Decidir entre pruebas estadísticas (Grubbs, Dixon) o métodos robustos. La tendencia actual es usar **métodos robustos** (Mediana, IQR normalizado) para no eliminar datos arbitrariamente.  
* **Cálculo de Puntajes (Scores):**  
  * Definir $\\sigma\_{pt}$ (Desviación estándar para la evaluación de la aptitud).  
  * Calcular z-score ($z \= (x \- X) / \\sigma\_{pt}$) o $z'$ (z-prima si la incertidumbre del valor asignado es significativa).  
  * Evaluar desempeño: $|z| \\leq 2.0$ (Satisfactorio), $2.0 \< |z| \< 3.0$ (Cuestionable), $|z| \\geq 3.0$ (Insatisfactorio).

#### E. Informes y Comunicación (ISO 17043 Cl. 7.4.3)

* El informe debe incluir no solo los puntajes, sino la interpretación estadística y comentarios técnicos.  
* Proteger la confidencialidad: códigos de identificación, no nombres públicos.

---

## **3\. Mejora y Soporte (ISO 17043 Cl. 7.5 y Cl. 8 implícita)**

* **Registros Técnicos:** Retener datos crudos y hojas de cálculo con fórmulas verificadas.  
* **Acciones Correctivas:** Si un lote falla la homogeneidad, o si un error sistemático afecta a la mayoría de participantes, el sistema debe detener la evaluación o emitir advertencias.  
* **Revisión por la Dirección:** Evaluar la idoneidad de los métodos estadísticos elegidos anualmente.

---

# PREGUNTAS PARA PULIR LA INVESTIGACIÓN

Para que este diseño pase de una estructura general a un plan de implementación concreto, necesito que aclares los siguientes puntos:

1. **Ámbito de Acreditación y Matrices:**

   * ¿En qué área de ensayo operará el sistema? (Ej. Química ambiental, Microbiología clínica, Calibración metrológica, Ensayos mecánicos). Esto define si los datos son cuantitativos continuos, discretos (cuentas) o cualitativos (identificación), cambiando radicalmente el tratamiento estadístico (ISO 13528 hace distinciones importantes en la cláusula 5 y 11).  
2. **Tamaño y Tipo de Participantes:**

   * ¿Cuál es el número esperado de participantes por ronda? (Si es un número bajo, ej. \< 10, las estadísticas de consenso son inútiles y se requiere usar Valores de Referencia externos, según ISO 13528 cláusula 5.4).  
   * ¿Los participantes usan un método estandarizado único o métodos diversos? (Si son métodos diversos, se puede requerir agrupación por método o normalización).  
3. **Capacidad de Producción de Ítems:**

   * ¿El proveedor fabricará los ítems de ensayo de aptitud internamente o los comprará a un tercero (ej. Productor de Materiales de Referencia ISO 17034)?  
   * ¿Cuentan con laboratorio propio para hacer las pruebas de homogeneidad y estabilidad, o las subcontratarán?  
4. **Infraestructura Estadística:**

   * ¿Qué software o herramientas planean utilizar para el análisis de datos? (Excel, R, Python, software comercial especializado). Esto es crucial para el requisito de validación de software de la ISO 13528 cláusula 5.5.  
   * ¿Tienen acceso actual a un experto estadístico competente en comparaciones interlaboratoriales?  
5. **Estrategia de Valores Asignados:**

   * ¿Cuál es la preferencia inicial para determinar el "Valor Asignado"? ¿Valor de Consenso (más barato, requiere muchos participantes) o Valor de Referencia Certificado (más costoso y complejo, pero independiente del desempeño del grupo)?  
6. **Estado Actual:**

   * ¿Es una organización nueva o ya tienen un sistema ISO 9001 / ISO 17025 implementado sobre el cual construir? Esto facilita la parte documental.

Una vez respondas estas preguntas, podré detallar los protocolos estadísticos específicos y los procedimientos documentados necesarios.

Excelente. Esta información cambia el enfoque de "crear desde cero" a "adaptar y expandir". Tener una base ISO 17025 y equipo propio de referencia es una ventaja competitiva enorme, pero introduce riesgos de imparcialidad que el sistema debe controlar.

Aquí tienes el diseño ajustado a tu realidad:

---

# DISEÑO DEL SISTEMA DE GESTIÓN DE CALIDAD (SGC)

**Contexto:** Ensayos de Aptitud en Calidad del Aire (Gases Criterio) | Base existente: ISO 17025 | Nº Participantes: Bajo (\~12)

## **1\. Estrategia de Transición: De ISO 17025 a ISO 17043**

Dado que ya tienen ISO 17025, no necesitan reinventar la rueda. El SGC debe ser un **Anexo o Extensión** del sistema actual, pero con identidad propia para evitar confusiones entre las actividades del "Laboratorio de Ensayos" y el "Proveedor de Ensayos de Aptitud (PEA)".

### Cambios Clave en la Estructura:

1. **Definición de Roles:** En el manual de calidad, se debe distinguir claramente cuándo el personal actúa como "Laboratorio de Referencia" (para asignar valores) y cuándo como "PEA" (para evaluar a otros).  
2. **Imparcialidad (Riesgo Crítico):** Al usar su propio equipo como referencia, existe un riesgo de conflicto de interés (juez y parte).  
   * *Solución:* El sistema debe exigir que los Valores Asignados por Referencia sean validados por un tercero o por un Comité Técnico Externo antes de liberar el reporte, o declarar explícitamente la trazabilidad independiente.

---

## **2\. Bloque Técnico-Estadístico (Adaptado a Bajo Nº de Participantes)**

El desafío principal es el **número bajo de participantes (n ≈ 12\)**. La estadística de consenso pura (promedio de todos) es inestable con tan pocos datos.

### A. Definición del Valor Asignado ($X$) \- *ISO 13528 Cláusula 7 & 8*

Dado que tienen equipo de referencia, el diseño estadístico debe priorizar el **Enfoque de Valor de Referencia**.

* **Procedimiento:**  
  1. El laboratorio interno (bajo ISO 17025\) caracteriza los gases mediante comparación directa con patrones primarios/certificados.  
  2. Se asigna el valor ($X$) y su incertidumbre ($u\_x$).  
  3. *Ventaja:* Este valor es independiente de los participantes, lo que lo hace válido incluso si $n \< 12$.  
* **Uso del Consenso (Alternativa):**  
  * El consenso de los participantes se usará solo como "verificación cruzada".  
  * *Regla del Sistema:* Si el Valor de Referencia y el Valor de Consenso difieren significativamente (ej. Envery test), se debe investigar la causa antes de emitir el reporte.

### B. Desviación Estándar para la Evaluación de la Aptitud ($\\sigma\_{pt}$) \- *ISO 13528 Cláusula 9*

Con pocos participantes, la desviación estándar de la muestra no es un buen criterio de evaluación.

* **Diseño Recomendado:** Usar el **Enfoque de Reproducibilidad del Método Estandarizado**.  
  * Si los participantes usan métodos normalizados (ej. EPA, ISO, NOM), tomen el valor de precisión ($R$ o $\\sigma\_R$) declarado en la norma del método.  
  * Fórmula: $\\sigma\_{pt} \\approx \\sigma\_R$.  
* **Criterio de Desempeño:** Evaluar usando **z-score**. $$z \= \\frac{x \- X}{\\sigma\_{pt}}$$  
  * Donde $x$ es el resultado del participante, $X$ es el Valor de Referencia (del equipo interno).

### C. Tratamiento de Datos Atípicos (Outliers) \- *ISO 13528 Cláusula 6*

Con $n=12$, un solo outlier distorsiona mucho el promedio.

* El sistema debe implementar **Estadísticas Robustas** (Mediana y MADe \- Desviación Absoluta Mediana) para los gráficos y resúmenes, aunque la evaluación oficial se haga contra el Valor de Referencia.

---

## **3\. Validación del Software en R (Checklist para ISO 13528\)**

Como consultor, este es el entregable crítico para cumplir con ISO 17043 (Cl. 7.5.2) e ISO 13528 (Cl. 5.5). El aplicativo R debe ser validado.

**Checklist de Validación del Algoritmo R:**

1. **Verificación de Cálculos Básicos:**  
   - [ ] Crear un dataset sintético con valor conocido (ej. 10 datos con media 100 y SD 5).  
   - [ ] Correr el script y verificar que calcula correctamente: Media, Mediana, SD poblacional, SD robusta (nIQR o MADe).  
2. **Verificación de Algoritmos Robustos (ISO 13528 Anexo C):**  
   - [ ] Introducir un outlier severo en el dataset sintético (ej. valor 500 en lugar de 100).  
   - [ ] Verificar que la media robusta (Algoritmo A o similar) no se desplace significativamente (debe mantenerse cerca de 100).  
   - [ ] Verificar que la SD robusta ignore el outlier.  
3. **Verificación de Z-scores:**  
   - [ ] Calcular manualmente z-scores en Excel para el dataset de prueba.  
   - [ ] Comparar con los resultados del script R. Deben ser idénticos.  
4. **Manejo de Incertidumbre ($u\_x$):**  
   - [ ] Validar si el script calcula el $z'$ (z-prima) correctamente cuando la incertidumbre del valor asignado es significativa ($u\_x \> 0.3 \\sigma\_{pt}$).  
   - [ ] Fórmula a verificar en código: $z' \= (x \- X) / \\sqrt{\\sigma\_{pt}^2 \- u\_x^2}$.  
5. **Gráficos (ISO 13528 Cl. 10):**  
   - [ ] Verificar que los gráficos (ej. secuencial o de kernel) etiqueten correctamente a los participantes fuera de rango.  
6. **Gestión de Datos Faltantes:**  
   - [ ] Probar cómo reacciona el script si un participante no reporta (celdas vacías). No debe colapsar.

---

## **4\. Producción y Logística de Gases (Adaptado a ISO 17043 Cl. 7.3)**

La mayor dificultad en gases no es la estadística, es la **estabilidad**.

* **Protocolo de Homogeneidad (ISO 13528 Anexo B):**  
  * Para gases en cilindros, verificar la homogeneidad entre cilindros de la misma tanda. Seleccionar 3 a 5 cilindros al azar y analizarlos con el método de referencia (intra-laboratorio).  
  * Criterio: La variabilidad entre cilindros debe ser menor al 30% de la desviación estándar de aptitud ($\\sigma\_{pt}$).  
* **Protocolo de Estabilidad:**  
  * Dado que los gases pueden reaccionar o adsorberse en las paredes, se debe medir una muestra al inicio de la ronda y otra al final (después de recibir las respuestas) para asegurar que el valor asignado no "derivó" durante el transporte.  
* **Transporte:**  
  * Control de presiones y temperaturas durante el envío (registro en el formulario de recepción del participante).

---

## **5\. Próximos Pasos Recomendados**

Para pulir la investigación y pasar a la implementación, te sugiero priorizar:

1. **Redacción del "Plan de Esquema":** Un documento maestro que diga explícitamente: *"Como n \< 15, usaremos Valor de Referencia (Trazable) y $\\sigma\_{pt}$ basado en la reproducibilidad de la Norma \[X\]".*  
2. **Validación del Script R:** Ejecutar el checklist arriba descrito y archivar los resultados como evidencia ante una auditoría.  
3. **Política de Conflicto de Interés:** Redactar una cláusula donde el laboratorio declara que su equipo de referencia se calibra externamente con una trazabilidad independiente, garantizando que no "ajusta" los valores para favorecer su propia caracterización.

