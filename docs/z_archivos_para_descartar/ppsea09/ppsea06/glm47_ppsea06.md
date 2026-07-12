
| INFORMACIÓN GENERAL DEL PROCEDIMIENTO |
| ----- |
| **OBJETIVO:** Establecer el procedimiento estadístico aplicable al diseño, cálculo, validación y evaluación de esquemas de ensayos de aptitud desarrollados en CALAIRE, de conformidad con los criterios de la norma ISO 13528:2022 y con los requisitos generales de ISO/IEC 17043:2023. Este procedimiento define la determinación del valor asignado, la estimación de la desviación estándar para evaluación de aptitud, el tratamiento de resultados atípicos mediante métodos robustos, la integración de los estudios de homogeneidad y estabilidad, y la interpretación de los puntajes de desempeño. |
| **ALCANCE:** Este procedimiento aplica al diseño estadístico de todas las rondas de EA para gases contaminantes criterio (SO₂, NO/NO₂, CO y O₃) organizadas por el Laboratorio CALAIRE. |
| **DEFINICIONES:** x_pt: valor asignado al mensurando objeto del ensayo de aptitud. σ_pt: desviación estándar para evaluación de aptitud. u(x_pt): incertidumbre estándar asociada al valor asignado por la vía estadística. u(x_pt,def): incertidumbre estándar definitiva del valor asignado, una vez integradas las contribuciones por homogeneidad y estabilidad. u_hom: contribución por homogeneidad. u_stab: contribución por estabilidad. p: número de participantes válidos. x* y s*: estimadores robustos de ubicación y dispersión obtenidos mediante Algoritmo A. z: puntaje estandarizado de desempeño. z': puntaje ajustado que incorpora incertidumbre del valor asignado. ζ: puntaje que incorpora incertidumbres del participante y del valor asignado. E_n: número de error normalizado para comparaciones metrológicas. |
| **DOCUMENTOS DE REFERENCIA:** ISO 13528:2022 Statistical methods for use in proficiency testing by interlaboratory comparisons. ISO/IEC 17043:2023 Conformity assessment — General requirements for proficiency testing providers. P-PSEA-09 Procedimiento de planificación de ensayos de aptitud. Guía Eurachem Selection, Use and Interpretation of Proficiency Testing Schemes (3ª ed., 2021). ILAC P9:01/2024 Policy on the Use of Proficiency Testing as Part of Conformity Assessment. EA-4/18 Guidance on level and frequency of participation. EA-4/21 INF:2018 Guidelines for assessing the appropriateness of small interlaboratory comparisons. |
| **CONDICIONES GENERALES:** Este procedimiento aplica a los ejercicios de ensayos de aptitud en los que el valor asignado se establece a partir de resultados de participantes, de laboratorios de referencia o de modelos combinados de caracterización. Su aplicación comprende la etapa de diseño estadístico, la verificación de suficiencia de datos, la estimación de parámetros robustos, el cálculo de incertidumbre asociada al valor asignado y la evaluación del desempeño de los laboratorios participantes. |

| INFORMACIÓN ESPECÍFICA DEL PROCEDIMIENTO |
| ----- |

**2.1 Roles y responsabilidades**

| Cargo | Responsabilidad |
|-------|---------------|
| Estadístico / Experto técnico | Diseñar el modelo estadístico del esquema, seleccionar los estimadores aplicables, calcular el valor asignado, la desviación estándar para evaluación y revisar la coherencia técnica de los resultados. |
| Coordinador EA | Aprobar el diseño estadístico, verificar la conformidad con ISO 13528:2022 e ISO/IEC 17043:2023, y autorizar la emisión de resultados a participantes. |
| Ingeniero Operativo | Garantizar las condiciones técnicas de preparación, manejo y seguimiento de los ítems del ensayo de aptitud, así como la disponibilidad y consistencia de los datos de entrada. |
| Profesional de Calidad | Controlar la documentación aplicable, asegurar la trazabilidad de registros, verificar la vigencia del procedimiento y conservar evidencia de revisión y aprobación. |

**2.2 Desarrollo del diseño estadístico**

**2.2.1 Definición de los objetivos**

Antes de definir el modelo estadístico del esquema, se debe establecer el objetivo técnico del ensayo de aptitud y la finalidad de la evaluación de desempeño. Los objetivos del diseño pueden comprender los siguientes propósitos:

- Evaluar el desempeño de los laboratorios.
- Comparar métodos o equipos de medición.
- Validar la precisión y trazabilidad de resultados.
- Determinar sesgos o tendencias sistemáticas.
- Evaluar la consistencia con incertidumbres declaradas.

El diseño estadístico debe ser coherente con estos objetivos y documentarse explícitamente antes del inicio de la ronda.

**2.2.2 Selección del tipo de datos y número de participantes**

La definición del tipo de datos y del número de participantes debe realizarse antes de seleccionar el estimador del valor asignado. Para el presente procedimiento se adoptan las siguientes condiciones:

- Los datos del esquema deben ser cuantitativos y expresarse en unidades de concentración, tales como nmol/mol, μmol/mol, ppb o ppm, según corresponda al mensurando.
- La distribución esperada de resultados debe ser aproximadamente normal; cuando exista asimetría significativa podrá considerarse transformación logarítmica o un tratamiento robusto equivalente, sujeto a justificación técnica.
- El número mínimo de participantes depende del método de valor asignado seleccionado:
  - **Valor asignado independiente (MRC, laboratorio de referencia, valor formulado):** No existe un mínimo estadístico; el diseño es válido incluso con p < 5.
  - **Valor asignado de consenso de laboratorios expertos:** Se recomienda p ≥ 8 para estimaciones robustas confiables.
  - **Valor asignado de consenso de participantes:** Se requiere p ≥ 12 para que u(x_pt) ≤ 0.3σ_pt. Para 7 ≤ p < 12, el uso es cuestionable y requiere justificación técnica. Para p < 7, no se recomienda usar consenso de participantes.

Cuando el número de participantes sea insuficiente para cumplir con los objetivos del diseño estadístico, el proveedor debe documentar y comunicar a los participantes los enfoques alternativos utilizados (ISO/IEC 17043:2023, 7.2.2.3).

**2.2.3 Determinación del valor asignado (x_pt) y su incertidumbre u(x_pt)**

ISO 13528:2022 (cláusula 7) establece cinco métodos en orden descendente de independencia respecto a los datos de participantes. La jerarquía de métodos es:

1. **Valor formulado:** El ítem de PT se prepara por procedimientos conocidos (preparación gravimétrica o dilución dinámica). La incertidumbre se calcula a partir del proceso de preparación. Es el enfoque preferido para gases contaminantes donde existe trazabilidad a SI.

2. **Material de Referencia Certificado (MRC):** Se emplea un MRC con valor de propiedad trazable al SI. Para gases: patrones de gas certificados preparados según ISO 6142. Las incertidumbres típicas son 0.1–0.2% relativo (k = 2).

3. **Laboratorio de referencia:** Un único laboratorio competente (NMI, laboratorio nacional de referencia acreditado) proporciona el valor asignado. Es explícitamente adecuado cuando los enfoques de consenso no funcionan por número insuficiente de participantes.

4. **Consenso de laboratorios expertos:** Un grupo designado de laboratorios expertos, separado de los participantes, proporciona mediciones para derivar el valor asignado. La incertidumbre se estima como u(x_pt) = s*/√p, donde s* es la desviación estándar robusta de los expertos.

5. **Consenso de participantes:** Valor derivado de los resultados de todos los participantes, utilizando métodos robustos (mediana, Algoritmo A, Q/Hampel). La incertidumbre se estima como u(x_pt) = 1.25 × s*/√p. Solo se recomienda cuando p ≥ 12 y no existen alternativas de mayor independencia.

**Criterio de incertidumbre del valor asignado:**

ISO 13528 (cláusula 9.2) establece el criterio fundamental para la validez del z-score:

u(x_pt) ≤ 0.3 × σ_pt

Cuando este criterio no se cumple, debe emplearse el z'-score, ζ-score o E_n en lugar del z-score convencional. Para poblaciones reducidas con valor asignado de consenso, es prácticamente imposible satisfacer este criterio cuando p < 17, por lo cual el uso de z' o ζ es obligatorio.

**Presupuesto de incertidumbre definitiva:**

El valor asignado debe reportarse con su incertidumbre definitiva, que integra todas las contribuciones relevantes:

u(x_pt,def) = √[u(x_pt)² + u_hom² + u_stab²]

Donde:
- u(x_pt): incertidumbre del valor asignado por el método de determinación
- u_hom: contribución por heterogeneidad, estimada como s_s/√n_hom (donde s_s es la desviación estándar entre unidades y n_hom el número de muestras evaluadas)
- u_stab: contribución por inestabilidad, estimada a partir de estudios de estabilidad

**2.2.4 Estimación de la desviación estándar para evaluación de aptitud (σ_pt)**

ISO 13528 (cláusula 8) establece seis enfoques para determinar σ_pt, en orden de preferencia:

1. **σ_pt prescriptivo/regulatorio:** Se fija por especificación técnica, regulación o panel de expertos. Para calidad de aire, la Directiva 2008/50/CE establece una incertidumbre máxima del 15% para mediciones fijas, lo que se traduce en σ_pt ≈ 5–7.5% relativo.

2. **Percepción de expertos / aptitud para el propósito:** Un comité técnico establece σ_pt con base en lo que se considera una precisión óptima para el uso previsto de los resultados.

3. **Ecuación de Horwitz:** σ_H = 0.02 × C^0.8495, donde C es la fracción másica. Aplicable a análisis químicos pero presenta limitaciones para mediciones instrumentales de gases.

4. **Datos de reproducibilidad históricos:** Si existen datos de estudios colaborativos previos (ISO 5725) para el método y la matriz, σ_pt puede igualarse a la desviación estándar de reproducibilidad s_R publicada.

5. **σ_pt derivado de datos de rondas anteriores:** Se utiliza la desviación estándar robusta de rondas previas como referencia, siempre que las condiciones sean comparables.

6. **Desviación estándar robusta de la ronda actual (s*):** Solo se recomienda cuando p ≥ 20 y no existen alternativas externas. Para poblaciones reducidas, este método es inapropiado.

Para esquemas con pocos participantes (p < 12), se recomienda usar σ_pt prescriptivo (basado en requisitos regulatorios) o de aptitud para el propósito, evitando derivar σ_pt de la dispersión observada en la ronda actual.

**2.2.5 Métodos robustos para tratamiento de datos atípicos**

ISO 13528:2022 (cláusula 6.5) prefiere explícitamente los métodos robustos sobre las pruebas formales de atípicos para derivar valores de consenso, ya que eliminan la subjetividad en la decisión de excluir datos.

**Métodos robustos disponibles:**

| Método | Descripción | Punto de ruptura | Eficiencia | Aplicabilidad |
|--------|-------------|-------------------|------------|---------------|
| **Algoritmo A** (M-estimador de Huber) | Estimación iterativa con winsorización a ±1.5s* | ~25% | ~96% | p ≥ 18, distribución aproximadamente normal |
| **Q/Hampel** | Dos pasos: Q para dispersión, luego Hampel para ubicación | ~35% | ~96% | p ≥ 8, muy estable, preferido para pocos datos |
| **Mediana + MADe** | Mediana para ubicación, MAD escalada (1.483 × MAD) para dispersión | 50% | ~78% | Muestras pequeñas, pero baja eficiencia |
| **Mediana + NIQR** | Mediana para ubicación, IQR/1.349 para dispersión | 50% | ~74% | Muestras pequeñas, simple |

Para poblaciones reducidas (p < 20), el método Q/Hampel es preferible por su estabilidad y mayor punto de ruptura. El Algoritmo A puede tener problemas de convergencia con muestras pequeñas.

**Procedimiento de identificación de "blunders":**

Antes de aplicar métodos robustos, se identifican y eliminan resultados que constituyan errores evidentes (blunders):
- Errores de unidades (ej: reportar ppm cuando se solicita ppb)
- Transposición incorrecta de dígitos
- Resultados fuera de rango físicamente posible
- Valores reportados con errores de formato manifiestos

Los blunders se tratan separadamente y no se incluyen en el análisis estadístico principal.

**2.2.6 Manejo de fallos de convergencia del Algoritmo A**

Cuando el Algoritmo A no converge o presenta inestabilidad, se aplican los siguientes procedimientos de contingencia en orden de preferencia:

1. Ajustar criterios de convergencia (aumentar número máximo de iteraciones, modificar tolerancia)
2. Usar mediana + MADe o mediana + NIQR como estimadores alternativos
3. Utilizar el método Q/Hampel como alternativa más estable
4. Realizar análisis de sensibilidad "con y sin" resultados extremos

Cualquier contingencia debe documentarse en el informe de resultados.

**2.2.7 Integración de estudios de homogeneidad y estabilidad**

**Homogeneidad:**

El estudio de homogeneidad se realiza de acuerdo con ISO 13528:2022 (cláusula 6.1). El procedimiento incluye:

- Selección aleatoria de n = 10 unidades del lote final
- Análisis de cada unidad con r = 2 réplicas bajo condiciones de repetibilidad
- Análisis de varianza (ANOVA de una vía) para estimar s_s² (varianza entre unidades)
- Criterio de aceptación: s_s ≤ 0.3 × σ_pt

La contribución a la incertidumbre del valor asignado es:

u_hom = s_s / √n_hom

**Estabilidad:**

El estudio de estabilidad evalúa si los ítems mantienen sus propiedades durante la ronda. Para gases:

- **CO, NO, SO₂ en N₂:** Se confía en datos históricos de estabilidad (varios años). Si se requiere confirmación, se analizan muestras de retención al inicio y final de la ronda.
- **NO₂ en aire, O₃:** Se realizan estudios específicos en cada ronda o se establecen condiciones estrictas de control (tiempo de uso, temperatura, presión de almacenamiento).

Cuando no se puede demostrar estabilidad plena, se cuantifica la inestabilidad (δ_stab) y se incorpora al presupuesto de incertidumbre.

**2.2.8 Detección de multimodalidad**

Antes de proceder con el análisis estadístico, se realiza una revisión visual de la distribución de resultados para identificar:

- Bimodalidad o multimodalidad (puede indicar presencia de subpoblaciones o diferentes métodos)
- Asimetría significativa (puede requerir transformación de datos)
- Valores extremos sospechosos

Herramientas gráficas recomendadas:
- Histograma
- Gráfico de densidad kernel (preferible para detectar multimodalidad)
- Boxplot
- Gráfico cuantil-cuantil (Q-Q plot)

Si se detecta multimodalidad significativa:
- Se investiga la causa (diferentes métodos, tipos de equipos, matrices)
- Se considera la estratificación por subpoblaciones
- Se documenta el hallazgo en el informe de resultados

**2.2.9 Lógica de selección del estadístico de desempeño**

La selección del estadístico de desempeño sigue el siguiente algoritmo de decisión:

```
¿Tiene valor asignado independiente (MRC, referencia externa)?
├── SÍ: 
│   └── ¿Participantes reportan incertidumbre?
│       ├── SÍ: Usar ζ-score o E_n (preferido para calibración)
│       └── NO: Usar z-score (si u(x_pt) ≤ 0.3σ_pt) o z'-score
└── NO (valor de consenso):
    └── ¿p ≥ 12 y u(x_pt) ≤ 0.3σ_pt?
        ├── SÍ: Usar z-score
        └── NO: Usar z'-score obligatoriamente
```

**Criterios de interpretación:**

| Estadístico | Fórmula | |z| ≤ 2.0 | 2.0 < |z| < 3.0 | |z| ≥ 3.0 |
|-------------|----------|-----------|----------------|-----------|
| z | (x - x_pt) / σ_pt | Satisfactorio | Cuestionable | Insatisfactorio |
| z' | (x - x_pt) / √(σ_pt² + u(x_pt)²) | Satisfactorio | Cuestionable | Insatisfactorio |
| ζ | (x - x_pt) / √(u(x)² + u(x_pt)²) | Satisfactorio | Cuestionable | Insatisfactorio |
| E_n | (x - x_pt) / √(U(x)² + U(x_pt)²) | |E_n| ≤ 1: Satisfactorio | |E_n| > 1: Insatisfactorio |

**2.2.10 Tratamiento de datos censurados**

Cuando los participantes reportan valores como "menor que" (< LOD) o "mayor que" (> rango):

- Se registran como resultados censurados en la base de datos
- Se evalúa el impacto en el análisis estadístico:
  - Si la proporción de datos censurados es baja (< 10%), se puede excluir del análisis de consenso pero incluir en evaluación individual
  - Si la proporción es alta, se requieren métodos especiales (estimación por máxima verosimilitud, bootstrap con censura)
- Se documenta en el informe la decisión sobre el tratamiento de datos censurados

**2.2.11 Registros requeridos y criterios de revisión técnica**

**Registros obligatorios:**

1. Plan estadístico del esquema (firmado por estadístico y coordinador)
2. Registros de caracterización del ítem (valores de referencia, certificados MRC)
3. Registros de homogeneidad (datos brutos, análisis ANOVA, conclusión)
4. Registros de estabilidad (datos de estudios, conclusiones)
5. Base de datos de resultados de participantes (incluyendo metadatos: código, resultado, incertidumbre, método, fecha)
6. Cálculos de valor asignado (x_pt) con incertidumbre completa
7. Cálculos de σ_pt con justificación del método seleccionado
8. Cálculos de estadísticos de desempeño (z, z', ζ, E_n)
9. Informe técnico de análisis con gráficos y diagnóstico
10. Registro de revisiones y aprobaciones

**Criterios de revisión técnica:**

El diseño estadístico y los resultados deben ser revisados técnica antes de la emisión del informe. La revisión debe verificar:

- Coherencia con el plan estadístico aprobado
- Adecuación de los métodos seleccionados al número de participantes
- Validez de los supuestos estadísticos (normalidad, suficiencia de datos)
- Ausencia de errores en cálculos o fórmulas
- Coherencia entre gráficos y resultados numéricos
- Adecuación de la interpretación y conclusiones
- Cumplimiento de requisitos de ISO 13528:2022 e ISO/IEC 17043:2023

La revisión técnica debe ser realizada por personal distinto del que realizó el análisis, cuando sea posible, para asegurar imparcialidad.

**2.2.12 Escenarios específicos por tamaño de muestra**

**Escenario A: p ≥ 20 (población grande)**

- Valor asignado: consenso de participantes con Algoritmo A o Q/Hampel
- σ_pt: desviación estándar robusta de la ronda (s*) o prescriptivo según objetivos
- Estadístico: z-score (si u(x_pt) ≤ 0.3σ_pt) o z'-score

**Escenario B: 12 ≤ p < 20 (población moderada)**

- Valor asignado: consenso de participantes con Q/Hampel (preferido) o valor externo
- σ_pt: prescriptivo (aptitud para el propósito) o de rondas anteriores
- Estadístico: z'-score (recomendado) o ζ-score si hay incertidumbres

**Escenario C: 7 ≤ p < 12 (población pequeña)**

- Valor asignado: valor externo (MRC, laboratorio de referencia, valor formulado) — consenso no recomendado
- σ_pt: prescriptivo obligatorio (basado en requisitos regulatorios o aptitud para el uso)
- Estadístico: z'-score o ζ-score (cuando se reportan incertidumbres)

**Escenario D: p < 7 (población muy pequeña)**

- Valor asignado: valor externo obligatorio (MRC, laboratorio de referencia, valor formulado)
- σ_pt: prescriptivo obligatorio
- Estadístico: ζ-score o E_n (preferible para comparaciones metrológicas)
- Consideración: usar E_n cuando el objetivo sea compatibilidad de incertidumbres

Para escenarios C y D, se recomienda aumentar información solicitando múltiples ítems, replicados o pares Youden/split samples.

**2.2.13 Representaciones gráficas**

Se deben incluir en el informe las siguientes representaciones gráficas:

- Histograma de resultados de participantes
- Gráfico de densidad kernel (superior para detectar multimodalidad)
- Gráfico de barras de z-scores (para cada laboratorio)
- Diagrama de Youden (para pares de muestras, si aplica)
- Gráfico de desviación estándar de repetibilidad (si se reportan réplicas)
- Gráfico multi-ronda (para seguimiento longitudinal, si hay datos históricos)

Los gráficos deben estar claramente etiquetados con información sobre:
- Valor asignado (x_pt)
- σ_pt
- Umbrales de interpretación (satisfactorio, cuestionable, insatisfactorio)
- Identificación de laboratorio por código

| REVISÓ |  | APROBÓ |  |
| ----- | :---- | :---- | :---- |
| **ROL** | Estadístico | **ROL** | Coordinador EA |
| **FECHA** |  | **FECHA** |  |
