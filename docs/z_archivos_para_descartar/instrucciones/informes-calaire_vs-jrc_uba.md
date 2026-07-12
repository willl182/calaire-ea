**Evaluación de Conformidad y Benchmarking** de los informes **EA\_2025** y **EA\_2026** generados por CALAIRE.

La evaluación contrasta estos informes frente a los requisitos normativos y las mejores prácticas internacionales observadas en los informes de referencia de **JRC (Barbiere)** y **Umweltbundesamt (UBA)**.

### 1\. Resumen Ejecutivo de la Auditoría

Los informes generados por CALAIRE demuestran una estructura técnica sólida y un cumplimiento general de la **ISO/IEC 17043:2023**, especialmente en la presentación de datos y el uso de algoritmos robustos modernos. Sin embargo, se han detectado **Hallazgos Críticos** en la gestión estadística de grupos pequeños y en la validación de la estabilidad de las muestras, los cuales difieren significativamente de la robustez observada en los informes de JRC y UBA.

Criterio,JRC (Barbiere) / UBA (Austria),Informe EA 2025 (CALAIRE),Informe EA 2026 (CALAIRE),Estado CALAIRE

Valor Asignado ($x\_{pt}$),"Valor de Referencia (Metrológico) 1, 2","Consenso (Algoritmo A / MADe) 3, 4",Consenso (nIQR) 5,Riesgo en $n\<12$

Desviación Estándar ($\\sigma\_{pt}$),"Criterio Fijo (Directivas UE/Fitness for purpose) 6, 7",Desviación robusta de los participantes ($s^\*$) 3,Desviación robusta (nIQR) 5,No Conforme (vs. objetivo)

Criterio de Evaluación,"z, z', En, Árbol de decisión a1-a7 8, 9","z-score (2025-13), Zeta (2025-7)",En-score,Conforme (Adaptativo)

Estabilidad/Homogeneidad,"Criterios estrictos ISO 13528 Anexo B 10, 11",Fallos reportados en criterios de estabilidad 12,No detallado en extracto,HALLAZGO CRÍTICO

### 2\. Evaluación Detallada vs. Normas ISO

#### A. Determinación del Valor Asignado (ISO 13528:2022 Cláusula 5\)

* **Normativa:** Para grupos pequeños ($n \< 12$), ISO 13528 desaconseja el uso de valores de consenso debido a la alta incertidumbre.  
* **Hallazgo (EA\_2026):** El informe del 2026 utiliza consenso (nIQR) con solo **4 participantes** 5, 13\. Esto es estadísticamente débil. Si un laboratorio tiene un sesgo fuerte, arrastrará el valor asignado.  
* **Benchmarking:** JRC y UBA utilizan **Valores de Referencia** trazables a sus propios patrones nacionales (acreditados ISO 17025\) independientemente del número de participantes 2, 6, 14\.  
* **Recomendación:** Para rondas con $n=4$ o $n=7$ (EA\_2025-7), CALAIRE debe actuar como laboratorio de referencia y asignar el valor $x\_{pt}$ mediante su propia medición calibrada, no por consenso.

#### B. Criterio de Desempeño $\\sigma\_{pt}$ (ISO 17043 Cláusula 7.4)

* **Normativa:** El proveedor debe establecer criterios de evaluación adecuados para el propósito.  
* **Comparativa:**  
* **UBA/JRC:** Utilizan una desviación estándar fija basada en directivas europeas (ej. $\\sigma\_{pt}$ calculado como función lineal de la concentración) 7, 9\. Esto asegura que la evaluación sea constante en el tiempo.  
* **CALAIRE:** Calcula $\\sigma\_{pt}$ basado en la variabilidad del grupo ($s^\*$, nIQR) 3, 5\.  
* **Riesgo:** En el informe 2026, al usar nIQR con 4 datos, la $\\sigma\_{pt}$ depende puramente de cuán cerca estén esos 4 laboratorios. Si todos miden mal pero igual, todos aprueban. Si miden bien pero con ligeras diferencias, la $\\sigma\_{pt}$ puede ser irrealmente pequeña.  
* **Recomendación:** Adoptar el modelo de UBA/JRC de definir una $\\sigma\_{pt}$ "Fitness for Purpose" (Aptitud para el uso) basada en la normativa colombiana o internacional, en lugar de derivarla de grupos pequeños.

#### C. Control de Estabilidad (ISO 17043 7.3.4 / ISO 13528 Anexo B)

* **Hallazgo Crítico (EA 2025):** En el informe del 10/12/2025, la tabla de estabilidad muestra explícitamente **"NO CUMPLE CRITERIO ESTABILIDAD"** para múltiples niveles de CO, NO, NO2 y O3 (Diferencia \> 0.3$\\sigma$) 12\.  
* **Impacto:** A pesar de fallar la prueba, el informe emite z-scores y declara resultados satisfactorios. Esto viola el principio de que el ítem debe ser estable durante el ensayo.  
* **Diferencia con JRC/UBA:** JRC documenta explícitamente "Yes" en la prueba de \<0.5% o criterios de estabilidad 10\. UBA declara "Los criterios... fueron cumplidos" 11\.  
* **Acción Correctiva Requerida:** Si la estabilidad falla, ISO 13528 exige expandir la incertidumbre del valor asignado ($u(x\_{pt})$) sumando el componente de inestabilidad antes de evaluar a los participantes. El informe no aclara si esto se hizo.

### 3\. Comparación de Estructura y Presentación de Informes

#### Similitudes

1. **Gráficas de Desempeño:** Tanto CALAIRE como JRC/UBA utilizan gráficas claras de z-scores y errores normalizados (En). CALAIRE incluye una "Matriz de desempeño" visualmente útil 15\.  
2. **Transparencia Metrológica:** CALAIRE ha implementado una sección de **"Compatibilidad Metrológica"** 16, 17 que compara el valor de referencia (medido por CALAIRE) contra el consenso. Esto es excelente y se alinea con las mejores prácticas de JRC, permitiendo validar el sesgo del grupo.

#### Diferencias Notables (A favor de JRC/UBA)

1. **Sistema de Evaluación Escalonado (UBA):** El informe de UBA utiliza un sistema sofisticado de clasificación (a1, a2, a3... a7) que integra z-score, En-score e incertidumbre en una sola decisión 9\. CALAIRE evalúa los índices por separado (Tabla 5\) 18\.  
2. **Análisis Gráfico Youden:** JRC utiliza gráficos de Youden para NO/NO2 para distinguir errores sistemáticos de aleatorios 19\. Los informes actuales de CALAIRE no muestran este tipo de análisis bivariado.  
3. **Manejo de la Incertidumbre:** JRC utiliza el **z'-score** (z-prime) cuando la incertidumbre del valor asignado es alta 6\. CALAIRE cambia a **Zeta-score** en grupos pequeños (EA 2025-7) 20, lo cual es técnicamente válido pero requiere que los participantes reporten incertidumbres muy fiables.

### 4\. Veredicto del Auditor

**Informe EA 2025 (n=13) Source 204:**

* **Estado:** **CONFORME PARCIALMENTE.**  
* **Fortaleza:** Buen uso de estadísticas robustas (Algoritmo A).  
* **Debilidad Crítica:** Fallo en criterios de estabilidad 12 sin evidencia clara de mitigación en el cálculo de puntajes.

**Informe EA 2025 (n=7) Source 225:**

* **Estado:** **OBSERVACIÓN.**  
* **Punto:** El uso de MADe para consenso con 7 laboratorios es arriesgado. El cambio a Zeta-score es una buena estrategia para mitigar la falta de datos, siempre que la incertidumbre de CALAIRE (Referencia) esté bien controlada.

**Informe EA 2026 (n=4) Source 238:**

* **Estado:** **NO CONFORME TÉCNICAMENTE (Riesgo Alto).**  
* **Causa:** Uso de consenso (nIQR) con 4 datos.  
* **Justificación:** ISO 13528 establece que la estadística robusta pierde validez con $n$ tan bajos. El valor asignado y la $\\sigma\_{pt}$ son inestables.  
* **Solución:** Debe usarse el **Valor de Referencia** medido por CALAIRE (el cual ya miden para la tabla de compatibilidad 13\) como el Valor Asignado oficial para la evaluación.

### Recomendaciones Finales para el Sistema CALAIRE

1. **Implementar "Fitness for Purpose":** Dejar de calcular $\\sigma\_{pt}$ basado en el grupo. Adoptar los valores fijos de JRC/UBA (ej. CO 10-20%, NO2 15%) para asegurar comparabilidad histórica.  
2. **Política de Grupos Pequeños:** Establecer en el protocolo (P-PSEA-01) que para $n \< 10$, el Valor Asignado **será** el Valor de Referencia de CALAIRE, no el consenso.  
3. **Gestión de Inestabilidad:** Automatizar en el aplicativo que, si falla el criterio de estabilidad (Anexo B), se incremente automáticamente la incertidumbre del valor asignado ($u\_{xpt}$) en el cálculo de z/z'.

