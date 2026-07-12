evaluación comparativa del documento **"Comunicación Detallada EA" de CALAIRE** Fuente 172 frente a los modelos internacionales de referencia (**JRC-ERLAP** de la Comisión Europea, **UBA** de Austria, **PTPP** de Brno y **UCLSB** de Bulgaria) y los requisitos normativos vigentes.

### Resumen Ejecutivo de la Auditoría

El documento de CALAIRE es técnicamente competente y se alinea estrechamente con el modelo del **JRC-ERLAP** (el referente europeo para gases), lo cual es una señal de robustez técnica. Sin embargo, carece de la profundidad administrativa y de gestión de riesgos (logística/seguridad) que caracteriza a los proveedores europeos maduros como UBA o JRC.

### 1\. Comparativa Técnica: Esquemas "In-Situ" (CALAIRE vs. JRC-ERLAP)

Dado que ambos proveedores (CALAIRE y JRC) ejecutan ensayos de aptitud mediante medición simultánea en sitio (gases), esta es la comparación más relevante.

Característica,JRC-ERLAP (Comisión Europea) Fuente 1,CALAIRE (Colombia) Fuente 172,Evaluación del Auditor

Generación de Muestra,"Manifold de vidrio, dilución dinámica \+ MRC.","Manifold de vidrio, dilución dinámica \+ MRC.",Equivalente. Ambos cumplen el estándar de oro técnico.

Cronograma,"Hora a hora (muy detallado). Define tiempos de estabilización y ""cero"".",Detallado por días. Refiere a un anexo F-PSEA-02 para detalles horarios.,Conforme. El uso de anexos es válido según ISO 17043 (7.1.2).

Logística y Seguridad,"Exhaustivo: Aduanas, voltaje, seguridad de cilindros, EPPs, acceso a instalaciones nucleares.",Básico: Menciona voltaje (110V) y embalaje. Omite detalles críticos de seguridad de cilindros.,"Oportunidad de Mejora. CALAIRE debe reforzar los requisitos de seguridad (presión, transporte de mercancías peligrosas)."

Infraestructura,"Detalla conectores, venteos y suminstro de gases auxiliares (H2, Aire).",Detalla conectores (1/4” teflón) y electricidad.,Conforme.

**Hallazgo:** El documento de JRC Fuente 48 incluye una sección específica de **"Seguridad"** (Safety) que prohíbe caminar sin escolta y exige EPP. CALAIRE menciona el transporte seguro Fuente 176 pero no establece normas de seguridad dentro del laboratorio (ej. manejo de gases a presión), lo cual es un riesgo en esquemas presenciales.

### 2\. Comparativa Estadística y de Evaluación (vs. ISO 13528\)

Evaluación de cómo CALAIRE define sus criterios frente a los otros proveedores.

* **Definición del Valor Asignado ($x\_{pt}$):**  
* **CALAIRE:** Determinado por el laboratorio mediante trazabilidad (Fotómetro Nivel 2 / MRC) Fuente 174\. Esto es **método 7.5 de ISO 13528** (Valor de Referencia).  
* **UBA/Brno:** Utilizan mayoritariamente **Consenso de participantes** (Algoritmo A / Grubbs) Fuente 82, 188\.  
* *Veredicto:* **CALAIRE es superior** en este aspecto para grupos pequeños. Al usar un valor de referencia propio, evita los problemas de estadística robusta con $n \< 12$ que sufren los esquemas por consenso.  
* **Criterio de Desempeño ($\\sigma\_{pt}$):**  
* **JRC/UBA:** Utilizan criterios fijos ("Fitness for purpose") basados en directivas europeas Fuente 31\. Esto hace que la evaluación sea constante en el tiempo.  
* **CALAIRE:** No explicita si la $\\sigma\_{pt}$ es fija o derivada de la desviación estándar del grupo. Solo menciona el uso de ISO 13528\.  
* *Riesgo:* Si CALAIRE usa la desviación del grupo (como sugiere su informe 2026), penaliza a los participantes cuando el grupo es muy preciso y premia cuando el grupo es malo.  
* *Recomendación:* Adoptar el enfoque de **JRC** y definir una $\\sigma\_{pt}$ fija (ej. 15% para NO2) en el protocolo.  
* **Manejo de la Incertidumbre ($u(x\_{pt})$):**  
* **CALAIRE:** Introduce el **Zeta-score ($\\zeta$)** y el **En-score** Fuente 181\.  
* **JRC:** Utiliza **z'-score** cuando la incertidumbre es alta Fuente 27\.  
* *Análisis:* El enfoque de CALAIRE es técnicamente más exigente. El uso de $\\zeta$ y $E\_n$ obliga a los participantes a reportar correctamente sus incertidumbres (ISO 17043 7.3.5.2 f), mientras que el $z'$-score de JRC "perdona" un poco más al expandir los límites de aceptación.

### 3\. Comparativa de Gestión y Comunicación al Cliente (vs. ISO 17043\)

Aspectos administrativos y de derechos del cliente.

* **Quejas y Apelaciones (ISO 17043 Cláusula 7.6 y 7.7):**  
* **UBA:** Define explícitamente un plazo de **14 días** para objeciones y describe el proceso Fuente 87\.  
* **JRC:** Incluye un formulario de apelación en el anexo del protocolo Fuente 54\.  
* **CALAIRE:** El documento analizado **no menciona** el procedimiento de apelación.  
* *No Conformidad Potencial:* La norma exige que la descripción del proceso de manejo de apelaciones esté disponible para las partes interesadas. Debe incluirse una referencia o enlace en la comunicación detallada.  
* **Confidencialidad (ISO 17043 Cláusula 4.2):**  
* **UBA:** Detalla excepciones legales donde debe informar al Ministerio Fuente 85\.  
* **CALAIRE:** Menciona que la información puede remitirse al IDEAM o acreditadores Fuente 183\.  
* *Veredicto:* **Conforme.** Ambos proveedores gestionan correctamente las excepciones a la confidencialidad requeridas por la autoridad reguladora.  
* **Subcontratación:**  
* **UCLSB:** Identifica claramente al subcontratista para la preparación de muestras Fuente 221\.  
* **CALAIRE:** No menciona subcontratistas, lo cual es correcto si realiza todo internamente. Sin embargo, debe declarar explícitamente si alguna fase (ej. calibración de patrones primarios) es externa.

### Conclusión y Hoja de Ruta para CALAIRE

La **"Comunicación Detallada" de CALAIRE** es un documento técnicamente sólido para la ejecución operativa, pero presenta brechas en la gestión normativa frente a sus pares europeos.

**Acciones Recomendadas:**

1. **Seguridad (Crítico):** Añadir una sección de seguridad similar a la del **JRC**, especificando la normativa de transporte de cilindros y las normas de seguridad industrial dentro de las instalaciones de CALAIRE (uso de EPP, rutas de evacuación).  
2. **Transparencia Estadística:** Definir en el documento el origen de la Desviación Estándar para la Aptitud ($\\sigma\_{pt}$). ¿Es un valor fijo regulatorio (como JRC) o estadístico del grupo? Esto es vital para que el participante entienda las reglas del juego antes de jugar.  
3. **Derechos del Cliente:** Incluir un apartado sobre **"Quejas y Apelaciones"** con plazos definidos, imitando el modelo de **UBA**.  
4. **Gestión de Grupos Pequeños:** Dado que CALAIRE usa valores de referencia (metrológicos), debe explicitar en la comunicación que el esquema es robusto incluso con pocos participantes ($n \< 5$), diferenciándose positivamente de esquemas como el de **Brno** que dependen de métodos estadísticos complejos (Horn) para grupos pequeños.

