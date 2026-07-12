# P-PSEA-06 — Diseño Estadístico para Ensayos de Aptitud de Gases Contaminantes Criterio

**Código:** P-PSEA-06  
**Versión:** 3.0  
**Fecha de emisión:** 2026-03-22  
**Referencia normativa:** ISO/IEC 17043:2023, ISO 13528:2022  
**Procedimientos relacionados:** P-PSEA-09  

---

## 1. Información general del procedimiento

### 1.1 Objetivo

Establecer las reglas estadísticas para diseñar, calcular y validar la evaluación de desempeño en las rondas de ensayos de aptitud (EA) de gases contaminantes criterio —SO₂, NO/NO₂, CO y O₃— organizadas por el Laboratorio CALAIRE, conforme a ISO 13528:2022 e ISO/IEC 17043:2023. Este procedimiento define la determinación del valor asignado, la estimación de la desviación estándar para la evaluación de aptitud, la integración de los estudios de homogeneidad y estabilidad, y la interpretación de los puntajes de desempeño.

### 1.2 Alcance

Este procedimiento aplica al diseño estadístico de todas las rondas EA organizadas por el Laboratorio CALAIRE. Abarca la etapa de diseño estadístico (planificación), la verificación de suficiencia de datos, la estimación de parámetros robustos, el cálculo de la incertidumbre asociada al valor asignado, la evaluación del desempeño de los participantes, el tratamiento de escenarios con bajo número de participantes, y la detección de multimodalidad en los resultados.

### 1.3 Definiciones

| Término | Definición |
|---|---|
| x_pt | Valor asignado al mensurando del EA. |
| σ_pt | Desviación estándar para la evaluación de la aptitud; medida de dispersión preestablecida contra la cual se compara la desviación del participante. |
| u(x_pt) | Incertidumbre estándar del valor asignado por la vía de caracterización estadística (consenso o formulación). |
| u(x_pt,def) | Incertidumbre estándar definitiva del valor asignado, integrada con las contribuciones por homogeneidad y estabilidad. |
| u_hom | Contribución por heterogeneidad del lote de ítems de ensayo a la incertidumbre del valor asignado. |
| u_stab | Contribución por inestabilidad del ítem de ensayo durante la ronda a la incertidumbre del valor asignado. |
| p | Número de participantes válidos incluidos en el cálculo del valor asignado. |
| x* | Estimador robusto de ubicación (media robusta). |
| s* | Estimador robusto de dispersión (desviación estándar robusta). |
| Algoritmo A | Procedimiento iterativo de winsorización para estimar x* y s* simultáneamente, conforme a ISO 13528:2022 Anexo C.3. |
| MADe | Desviación absoluta mediana escalada: 1,483 × mediana(\|x_i − mediana(x)\|). |
| Q_n | Estimador robusto de escala basado en diferencias absolutas por pares, conforme a ISO 13528:2022 Anexo C. |
| nIQR | Rango intercuartílico normalizado: IQR / 1,349. |
| Q/Hampel | Método robusto en dos pasos: Q para dispersión, luego Hampel para ubicación. Punto de ruptura ~35%. |

### 1.4 Documentos de referencia

- ISO 13528:2022 — Métodos estadísticos para EA por comparación interlaboratorio.
- ISO/IEC 17043:2023 — Requisitos generales para proveedores de EA.
- ISO/IEC 17025:2017 — Requisitos generales para laboratorios de ensayo y calibración.
- ISO 6142-1:2015 — Preparación gravimétrica de mezclas gaseosas.
- Guía Eurachem — Selection, Use and Interpretation of Proficiency Testing Schemes (3ª ed., 2021).
- ILAC P9:01/2024 — Policy on the Use of Proficiency Testing.
- EA-4/18 — Guidance on level and frequency of participation.
- EA-4/21 INF:2018 — Guidelines for assessing the appropriateness of small interlaboratory comparisons.
- P-PSEA-09 — Planificación y preparación de rondas de EA.
- P-PSEA-07 — Elaboración de informe de resultados.

---

## 2. Roles y responsabilidades

| Rol | Responsabilidad |
|---|---|
| Estadístico / Experto técnico | Define el diseño estadístico, selecciona los métodos aplicables, ejecuta los cálculos y valida la coherencia técnica de los resultados. |
| Coordinador EA | Aprueba el diseño estadístico, verifica la conformidad con ISO 13528:2022 e ISO/IEC 17043:2023 y autoriza la emisión de resultados. |
| Ingeniero operativo | Garantiza la calidad de los datos de entrada, las condiciones técnicas y la trazabilidad de los registros primarios. |
| Profesional de calidad | Verifica el control documental, la vigencia del procedimiento y la evidencia de cumplimiento. |

---

## 3. Desarrollo del diseño estadístico

### 3.1 Definición del objetivo estadístico

Antes de definir el modelo estadístico, se establece el objetivo técnico del EA y la finalidad de la evaluación de desempeño. Los objetivos del diseño pueden comprender:

1. Evaluar el desempeño de los laboratorios frente a un criterio preestablecido.
2. Comparar métodos o equipos de medición.
3. Detectar sesgos o tendencias sistemáticas.
4. Validar la trazabilidad de resultados.
5. Evaluar la consistencia con incertidumbres declaradas.

El diseño estadístico debe ser coherente con estos objetivos y documentarse explícitamente antes del inicio de la ronda.

### 3.2 Tipo de datos y suficiencia de participantes

Los resultados del EA deben ser cuantitativos, expresados en unidades de concentración (nmol/mol, μmol/mol, ppb o ppm) normalizadas y metrológicamente consistentes.

La distribución esperada de resultados debe ser aproximadamente normal; cuando exista asimetría significativa podrá considerarse transformación logarítmica o un tratamiento robusto equivalente, sujeto a justificación técnica.

Las reglas por tamaño de muestra son:

| Condición | Enfoque estadístico |
|---|---|
| p ≥ 20 | Puede emplearse consenso robusto con Algoritmo A o Q/Hampel. σ_pt puede derivarse de s* bajo control técnico. |
| 12 ≤ p < 20 | Consenso de participantes con Q/Hampel (preferido) o valor externo. σ_pt prescriptiva o de rondas anteriores. Estadístico z' recomendado. |
| 6 ≤ p < 12 | Se prioriza valor asignado externo y σ_pt prescriptiva; consenso no recomendado. Estadístico z' o ζ. |
| p < 6 | No se utiliza consenso como base principal de desempeño. Se aplica valor asignado externo obligatorio, σ_pt prescriptiva y estadístico ζ o En. |

Para esquemas por consenso, el criterio de insignificancia de la incertidumbre del valor asignado es:

`u(x_pt) ≤ 0,3 × σ_pt`

Cuando este criterio no se cumple, el puntaje z clásico no es la métrica principal y debe emplearse z', ζ o En conforme a la sección 7 de este procedimiento. Para poblaciones reducidas con valor asignado de consenso, es prácticamente imposible satisfacer este criterio cuando p < 17, por lo cual el uso de z' o ζ es obligatorio.

El número mínimo de participantes depende del método de valor asignado seleccionado:

- **Valor asignado independiente (MRC, laboratorio de referencia, valor formulado):** No existe un mínimo estadístico; el diseño es válido incluso con p < 5.
- **Valor asignado de consenso de laboratorios expertos:** Se recomienda p ≥ 8 para estimaciones robustas confiables.
- **Valor asignado de consenso de participantes:** Se requiere p ≥ 12 para que u(x_pt) ≤ 0,3σ_pt. Para 7 ≤ p < 12, el uso es cuestionable y requiere justificación técnica. Para p < 7, no se recomienda.

Cuando el número de participantes sea insuficiente para los objetivos del diseño, el proveedor debe documentar y comunicar a los participantes los enfoques alternativos utilizados (ISO/IEC 17043:2023, 7.2.2.3). Para escenarios con pocos participantes, se recomienda aumentar información solicitando múltiples ítems, replicados o pares Youden/split samples.

### 3.3 Preparación y depuración de datos

Antes del cálculo se ejecuta la depuración siguiente:

1. Normalizar unidades y códigos de participante.
2. Identificar y eliminar errores evidentes (blunders): errores de unidades, transposición de dígitos, resultados fuera de rango físicamente posible, valores con errores de formato manifiestos. Los blunders se tratan separadamente y no se incluyen en el análisis estadístico principal.
3. Excluir datos no válidos (NA, valores no finitos, errores de unidad residuales, envíos fuera de la ventana de reporte).
4. Documentar cada exclusión con la causa técnica, la fecha y la identificación del registro afectado.

La exclusión de resultados se limita a: errores de unidad o transcripción evidentes, incumplimiento de instrucciones del esquema, o datos no finitos. No se excluyen datos por desempeño estadístico sin justificación técnica independiente.

### 3.4 Jerarquía de selección del valor asignado (x_pt)

El valor asignado se determina siguiendo la jerarquía de preferencia descendente (ISO 13528:2022, cláusula 7). Se selecciona el primer método viable conforme a la disponibilidad de recursos y la naturaleza del esquema.

| Orden | Método | Descripción | Cuándo es viable |
|---|---|---|---|
| 1 | **Valor formulado** | Mezcla gaseosa preparada gravimétricamente (ISO 6142-1) o por dilución dinámica con concentración conocida y trazable al SI. | Siempre que se disponga de patrón de masa calibrado y capacidad de preparación. Es el enfoque preferido para gases contaminantes donde existe trazabilidad a SI. |
| 2 | **Material de referencia certificado (MRC)** | Valor certificado de un CRM con trazabilidad a un NMI o laboratorio acreditado. Incertidumbres típicas: 0,1–0,2% relativo (k = 2) para patrones de gas certificados (ISO 6142). | Cuando se dispone de un CRM vigente con incertidumbre adecuada para el propósito. |
| 3 | **Laboratorio de referencia** | Resultado de un laboratorio competente con trazabilidad metrológica demostrada (NMI, laboratorio de referencia acreditado o experto designado). | Explícitamente adecuado cuando los enfoques de consenso no funcionan por número insuficiente de participantes. |
| 4 | **Consenso de expertos** | Valor derivado de un panel de laboratorios expertos designado, no participantes en la evaluación. u(x_pt) = s*/√p del grupo experto. | Cuando los métodos anteriores no son viables y se dispone de al menos 3 laboratorios expertos. |
| 5 | **Consenso de participantes** | Estimación robusta a partir de los resultados de los participantes. u(x_pt) = 1,25 × s*/√p. | Solo cuando p ≥ 12 y no existen alternativas de mayor independencia. |

Cuando se selecciona el método de consenso de participantes (orden 5), se aplica la sección 4 de este procedimiento.

La selección final del método de valor asignado debe justificarse en el expediente técnico del esquema, indicando el método empleado, la base de datos utilizada y el control de coherencia realizado.

### 3.5 Jerarquía de selección de σ_pt (ISO 13528:2022, cláusula 8)

La desviación estándar para la evaluación de la aptitud se determina siguiendo la jerarquía de preferencia. Se selecciona el primer método viable.

| Orden | Método | Descripción | Fundamento normativo |
|---|---|---|---|
| 1 | **Prescriptivo / regulatorio** | σ_pt fijada por requisito regulatorio, especificación técnica o panel de expertos del sector. Para gases contaminantes criterio, se toma como referencia la incertidumbre expandida máxima del 15% establecida por la Directiva 2008/50/CE para mediciones fijas de SO₂, NO₂, CO y O₃, lo que se traduce en σ_pt ≈ 5–7,5% relativo. | ISO 13528:2022, cláusula 8.1. |
| 2 | **Aptitud para el propósito** | σ_pt definida por un comité técnico del esquema en función del uso previsto de los resultados (fitness-for-purpose). | ISO 13528:2022, cláusula 8.2. |
| 3 | **Datos históricos robustos** | σ_pt derivada de la desviación estándar de reproducibilidad de rondas equivalentes anteriores, utilizando estimadores robustos. | ISO 13528:2022, cláusula 8.3. |
| 4 | **Modelo predictivo** | σ_pt calculada a partir de un modelo empírico del desempeño esperado del sistema de medición (por ejemplo, la ecuación de Horwitz-Thompson modificada donde aplique, aunque presenta limitaciones para mediciones instrumentales de gases). | ISO 13528:2022, cláusula 8.4. |
| 5 | **Modelo metrológico** | σ_pt derivada de un modelo metrológico del sistema de medición, considerando la incertidumbre objetivo. | ISO 13528:2022, cláusula 8.5. |
| 6 | **Estimación robusta desde participantes** | σ_pt estimada como s*, MADe o nIQR a partir de los resultados de los participantes. Solo procede cuando p ≥ 20 y el valor asignado es independiente de los participantes. Para p < 20 este método es inapropiado. | ISO 13528:2022, cláusula 8.6. |

Para esquemas con pocos participantes (p < 12), se recomienda usar σ_pt prescriptivo (basado en requisitos regulatorios) o de aptitud para el propósito, evitando derivar σ_pt de la dispersión observada en la ronda actual.

La comparación de la σ_pt seleccionada con la dispersión robusta observada en la ronda debe documentarse, independientemente del método elegido.

---

## 4. Estimadores robustos y Algoritmo A

### 4.1 Métodos robustos disponibles

ISO 13528:2022 (cláusula 6.5) prefiere explícitamente los métodos robustos sobre las pruebas formales de atípicos para derivar valores de consenso, ya que eliminan la subjetividad en la decisión de excluir datos.

| Método | Descripción | Punto de ruptura | Eficiencia | Aplicabilidad |
|---|---|---|---|---|
| **Algoritmo A** (M-estimador de Huber) | Estimación iterativa con winsorización a ±1,5s* | ~25% | ~96% | p ≥ 18, distribución aproximadamente normal |
| **Q/Hampel** | Dos pasos: Q para dispersión, luego Hampel para ubicación | ~35% | ~96% | p ≥ 8, muy estable, preferido para pocos datos |
| **Mediana + MADe** | Mediana para ubicación, MAD escalada (1,483 × MAD) para dispersión | 50% | ~78% | Muestras pequeñas, pero baja eficiencia |
| **Mediana + nIQR** | Mediana para ubicación, IQR/1,349 para dispersión | 50% | ~74% | Muestras pequeñas, simple |

Para poblaciones reducidas (p < 20), el método Q/Hampel es preferible por su estabilidad y mayor punto de ruptura. El Algoritmo A puede tener problemas de convergencia con muestras pequeñas.

### 4.2 Algoritmo A (ISO 13528:2022, Anexo C.3)

Cuando el valor asignado se determina por consenso de participantes, se utiliza el Algoritmo A como método robusto principal.

**Inicialización:**

- x*₀ = mediana(x_i)
- s*₀ = 1,483 × mediana(|x_i − x*₀|)

Si la dispersión inicial no es finita o es prácticamente nula, se utilizará la desviación estándar clásica como mecanismo de respaldo. Si la dispersión resultante continúa siendo nula o no finita, se concluirá que el conjunto de datos no presenta variabilidad suficiente para una aplicación informativa del algoritmo.

**Iteración:**

Para cada ciclo k = 1, 2, ... :

1. Cálculo del límite de winsorización: δ_k = 1,5 × s*_{k-1}.
2. Winsorización: para cada x_i, si |x_i − x*_{k-1}| > δ_k, se reemplaza x_i por x*_{k-1} + δ_k × signo(x_i − x*_{k-1}).
3. Se recalcula x*_k como la media aritmética de los valores winsorizados.
4. Se recalcula s*_k = 1,134 × √[ (1/(p-1)) × Σ(x_i,k* − x*_k)² ]. El factor 1,134 es obligatorio y corrige el sesgo introducido por la winsorización.
5. Se verifica convergencia.

**Tolerancia institucional:** se define como el menor valor entre 0,001 × x*_{k-1} y 10⁻⁴ en las unidades del mensurando. El número máximo de iteraciones es 50. Si dicho límite se alcanza sin convergencia, el resultado deberá reportarse como no convergente y quedará sujeto a revisión técnica.

**Nota:** La función base `run_algorithm_a()` admite una tolerancia por defecto de 1×10⁻⁶; para efectos del presente procedimiento operativo se adopta una tolerancia institucional de 1×10⁻⁴.

**Salidas del algoritmo:**

Una vez alcanzada la convergencia, el valor asignado se establece como x_pt = x* y la desviación estándar para evaluación de aptitud se establece como σ_pt = s*, salvo que el diseño del esquema defina una σ_pt objetivo por otra vía técnica o normativa. Se conserva el registro del número de iteraciones ejecutadas, del número final de observaciones winsorizadas y de los límites de winsorización aplicados.

### 4.3 Manejo de no convergencia del Algoritmo A

Si el Algoritmo A no converge o produce una escala inestable (s* < 0 o variaciones anómalas), se aplican los mecanismos de contingencia en el siguiente orden:

1. **Fallback 1:** Ajustar criterios de convergencia (aumentar número máximo de iteraciones, modificar tolerancia).
2. **Fallback 2:** Mediana + MADe (estimadores no paramétricos directos).
3. **Fallback 3:** Evaluación del estimador Q_n o Q/Hampel como alternativa robusta con mayor punto de ruptura.
4. **Fallback 4:** Análisis de sensibilidad "con y sin" resultados extremos.
5. **Fallback 5:** Escalamiento a revisión técnica por el estadístico, con decisión documentada sobre la validez del valor asignado antes de liberar la evaluación.

Cualquier contingencia debe documentarse en el informe de resultados con la justificación de la decisión adoptada.

---

## 5. Determinación de la incertidumbre del valor asignado

### 5.1 Componente por caracterización (consenso)

Cuando el valor asignado se deriva de consenso de participantes:

`u(x_pt) = 1,25 × s* / √p`

donde s* es el estimador robusto de dispersión y p es el número de participantes válidos. En los casos en que se utilice otro estimador de dispersión aprobado para el esquema, la expresión anterior se aplicará sustituyendo s* por el estimador correspondiente.

### 5.2 Componente por heterogeneidad

La contribución por heterogeneidad se estima como:

`u_hom = s_s`

donde s_s es la desviación estándar entre unidades de ensayo, determinada en el estudio de homogeneidad posterior al envasado final.

### 5.3 Componente por estabilidad

Sean δ = (x_fin − x_ini) el cambio del valor asignado entre el inicio y el final de la ventana de la ronda, y σ_pt el criterio establecido:

- Si |δ| ≤ 0,3 × σ_pt, entonces u_stab = 0.
- Si |δ| > 0,3 × σ_pt, entonces u_stab = |δ| / √3.

### 5.4 Incertidumbre definitiva

`u(x_pt,def) = √[ u(x_pt)² + u_hom² + u_stab² ]`

Donde:

- u(x_pt): incertidumbre del valor asignado por el método de determinación.
- u_hom: contribución por heterogeneidad, estimada como s_s.
- u_stab: contribución por inestabilidad, estimada conforme a 5.3.

El valor asignado debe reportarse con su incertidumbre definitiva en todos los casos.

---

## 6. Evaluación de homogeneidad y estabilidad

### 6.1 Evaluación de homogeneidad

Se selecciona una muestra representativa del lote de ítems de ensayo (mínimo 10 unidades) extraídas en diferentes posiciones de la línea de envasado y a diferentes tiempos. Las unidades se ensayan con r = 2 réplicas bajo condiciones de repetibilidad dentro de un mismo laboratorio. Se utiliza un método de ensayo con repetibilidad adecuada (σ_an / σ_pt < 0,5).

**Media por ítem:** Para cada ítem i con m réplicas:

`x̄_i = (1/m) × Σ x_ij`

**Varianza entre medias de ítem:**

`s²_x̄ = (1/(g-1)) × Σ(x̄_i − x̄̄)²`

donde g es el número de ítems y x̄̄ es la media global de las medias por ítem.

**Desviación dentro de ítem (para m = 2):**

`s_w = √[ (1/(2g)) × Σ(x_i1 − x_i2)² ]`

**Componente de variación entre ítems:**

`s²_s = s²_x̄ − s²_w / m`

Si s²_s < 0, se adopta s_s = 0. En caso contrario, s_s = √(s²_s).

**Criterio de aceptación:** s_s ≤ 0,3 × σ_pt. Si no se cumple, u_hom = s_s y se incorpora a u(x_pt,def).

**Criterio expandido** (ISO 13528:2022, Tabla 4): cuando se requiera, se aplica:

`MS_b ≤ F₁ × (0,3σ_pt)² + F₂ × MS_w`

donde F₁ y F₂ son factores tabulados dependientes del número de ítems y MS_b y MS_w representan los cuadrados medios entre y dentro de ítems, respectivamente.

### 6.2 Evaluación de estabilidad

Se seleccionan al menos dos tiempos representativos del ciclo de la ronda (inicio y final de la ventana de reporte). Se miden al menos dos unidades en cada tiempo, en las mismas condiciones.

**Diferencia media:**

`δ = ȳ₁ − ȳ₂`

donde ȳ₁ representa la media de referencia y ȳ₂ la media bajo la condición de estabilidad.

**Criterio de estabilidad:** |δ| ≤ 0,3 × σ_pt.

Si no se cumple, u_stab = |δ| / √3 y se incorpora a u(x_pt,def).

**Consideraciones específicas por analito:**

- **CO, NO, SO₂ en N₂:** Se confía en datos históricos de estabilidad (varios años). Si se requiere confirmación, se analizan muestras de retención al inicio y final de la ronda.
- **NO₂ en aire, O₃:** Se realizan estudios específicos en cada ronda o se establecen condiciones estrictas de control (tiempo de uso, temperatura, presión de almacenamiento).

Cuando no se puede demostrar estabilidad plena, se cuantifica la inestabilidad y se incorpora al presupuesto de incertidumbre.

### 6.3 Verificación de modalidad de distribución

Antes de consolidar el análisis se ejecuta una revisión visual (ISO 13528:2022, cláusula 6.4):

1. Histograma y gráfico de densidad kernel de los resultados (preferible para detectar multimodalidad).
2. Boxplot para identificar valores extremos.
3. Gráfico cuantil-cuantil (Q-Q plot) para evaluar normalidad.
4. Diagrama de Youden para pares de muestras (si aplica).

**Evaluación de multimodalidad:** si la distribución sugiere múltiples poblaciones (clusters):

- Investigar las variables explicativas (método, equipo, calibración, laboratorio).
- Si la segmentación es técnicamente justificada, evaluar con x_pt, σ_pt e interpretación independientes por subgrupo.
- Documentar la decisión y la justificación en el expediente de la ronda.
- Si la segmentación no es viable, reportar advertencia técnica en el informe.

---

## 7. Selección del estadístico de desempeño

### 7.1 Árbol de decisión

La selección del estadístico sigue la regla de decisión siguiente:

```
¿Tiene valor asignado independiente (MRC, referencia externa, formulado)?
├── SÍ:
│   └── ¿Participantes reportan incertidumbre?
│       ├── SÍ: Usar ζ-score o En (preferido para comparaciones metrológicas)
│       └── NO: 
│           └── ¿u(x_pt) ≤ 0,3 × σ_pt?
│               ├── SÍ: Usar z-score
│               └── NO: Usar z'-score
└── NO (valor de consenso):
    └── ¿p ≥ 12 y u(x_pt) ≤ 0,3 × σ_pt?
        ├── SÍ: Usar z-score
        │       → ζ (complementario si participantes reportan incertidumbre)
        └── NO: 
            ├── Usar z'-score obligatoriamente
            └── En caso de incertidumbres expandidas: En
```

### 7.2 Fórmulas de los estadísticos

| Estadístico | Fórmula | Condición de uso | Umbral satisfactorio |
|---|---|---|---|
| z | z = (x_i − x_pt) / σ_pt | u(x_pt) ≤ 0,3 × σ_pt; sin incertidumbre de participante | \|z\| ≤ 2 |
| z' | z' = (x_i − x_pt) / √(σ_pt² + u(x_pt)²) | u(x_pt) > 0,3 × σ_pt; valor asignado con incertidumbre significativa | \|z'\| ≤ 2 |
| ζ (zeta) | ζ = (x_i − x_pt) / √(u(x_i)² + u(x_pt)²) | Se requiere incertidumbre estándar de participante; se evalúa compatibilidad | \|ζ\| ≤ 2 |
| En | En = (x_i − x_pt) / √(U_i² + U_pt²) | Incertidumbres expandidas (k = 2); comparaciones de calibración/metrológicas | \|En\| ≤ 1 |

### 7.3 Interpretación institucional

**Para z, z' y ζ:**

| Rango | Clasificación | Acción |
|---|---|---|
| \|score\| ≤ 2 | Satisfactorio | Ninguna intervención requerida. |
| 2 < \|score\| < 3 | Cuestionable | Se recomienda investigación preliminar de posibles causas. |
| \|score\| ≥ 3 | No satisfactorio | Se requiere investigación, acciones correctivas documentadas y seguimiento. |

**Para En:**

| Rango | Clasificación | Acción |
|---|---|---|
| \|En\| ≤ 1 | Satisfactorio | Compatibilidad metrológica demostrada. |
| \|En\| > 1 | No satisfactorio | Incompatibilidad; requiere investigación. |

La categoría cuestionable no aplica a En debido a que este puntaje se fundamenta en incertidumbres expandidas y expresa una condición de compatibilidad metrológica con criterio binario de aceptación.

---

## 8. Gestión de participantes excluidos y criterios de viabilidad

### 8.1 Causas de exclusión

Se excluyen del conjunto evaluable los resultados con alguna de las siguientes causas:

1. Entrega fuera de la ventana de reporte definida en F-PSEA-01 / DG-PSEA-01.
2. Errores de unidad o dato no trazable.
3. Inconsistencia metrológica no subsanada tras solicitud de aclaración.
4. Ausencia de información mínima obligatoria (resultado, método, fecha).
5. Incumplimiento de las instrucciones de I-PSEA-01 que comprometa la validez del dato.

### 8.2 Tratamiento de datos censurados

Cuando los participantes reportan valores como "menor que" (< LOD) o "mayor que" (> rango):

- Se registran como resultados censurados en la base de datos.
- Si la proporción de datos censurados es baja (< 10%), se puede excluir del análisis de consenso pero incluir en evaluación individual.
- Si la proporción es alta, se requieren métodos especiales (estimación por máxima verosimilitud, bootstrap con censura).
- Se documenta en el informe la decisión sobre el tratamiento de datos censurados.

### 8.3 Mínimo viable para esquemas por consenso

Para que un esquema por consenso sea estadísticamente viable:

- Se requiere un mínimo de **p ≥ 6** participantes válidos para iniciar el cálculo del valor asignado.
- Si después de la depuración p < 6, se activa la regla de continuidad: se declara el valor asignado externo como método de respaldo y se recalcula la σ_pt prescriptiva correspondiente.

### 8.4 Registro de exclusiones

El informe EA reporta:

1. Número total de laboratorios inscritos.
2. Número de participantes que reportaron resultados.
3. Número y causas de exclusiones, con referencia a la sección de este procedimiento que las justifica.
4. Número de participantes evaluados finalmente.
5. Evaluación del mínimo viable y la decisión tomada.

---

## 9. Escenarios específicos por tamaño de muestra

### 9.1 Escenario A: p ≥ 20 (población grande)

- **Valor asignado:** consenso de participantes con Algoritmo A o Q/Hampel.
- **σ_pt:** desviación estándar robusta de la ronda (s*) o prescriptivo según objetivos.
- **Estadístico:** z-score (si u(x_pt) ≤ 0,3σ_pt) o z'-score.

### 9.2 Escenario B: 12 ≤ p < 20 (población moderada)

- **Valor asignado:** consenso de participantes con Q/Hampel (preferido) o valor externo.
- **σ_pt:** prescriptivo (aptitud para el propósito) o de rondas anteriores.
- **Estadístico:** z'-score (recomendado) o ζ-score si hay incertidumbres.
- **Nota:** los métodos robustos se emplean con cautela; se debe verificar que u(x_pt) ≤ 0,3σ_pt.

### 9.3 Escenario C: 6 ≤ p < 12 (población pequeña)

- **Valor asignado:** valor externo (MRC, laboratorio de referencia, valor formulado) — consenso no recomendado.
- **σ_pt:** prescriptivo obligatorio (basado en requisitos regulatorios o aptitud para el uso).
- **Estadístico:** z'-score o ζ-score (cuando se reportan incertidumbres).
- **Métodos robustos:** solo como diagnóstico complementario, no como base para el valor asignado o σ_pt.

### 9.4 Escenario D: p < 6 (población muy pequeña)

- **Valor asignado:** valor externo obligatorio (MRC, laboratorio de referencia, valor formulado).
- **σ_pt:** prescriptivo obligatorio.
- **Estadístico:** ζ-score o En (preferible para comparaciones metrológicas).
- **Consideración:** usar En cuando el objetivo sea compatibilidad de incertidumbres.

Para escenarios C y D, se recomienda aumentar información solicitando múltiples ítems, replicados o pares Youden/split samples.

**Se documenta expresamente** en el informe de la ronda que el esquema opera con un número reducido de participantes y se explican las implicaciones estadísticas.

---

## 10. Representaciones gráficas

Se deben incluir en el informe las siguientes representaciones gráficas:

1. Histograma de resultados de participantes.
2. Gráfico de densidad kernel (superior para detectar multimodalidad).
3. Gráfico de barras de z-scores (para cada laboratorio).
4. Boxplot de resultados.
5. Diagrama de Youden (para pares de muestras, si aplica).
6. Gráfico de desviación estándar de repetibilidad (si se reportan réplicas).
7. Gráfico multi-ronda (para seguimiento longitudinal, si hay datos históricos).

Los gráficos deben estar claramente etiquetados con información sobre:

- Valor asignado (x_pt).
- σ_pt.
- Umbrales de interpretación (satisfactorio, cuestionable, no satisfactorio).
- Identificación de laboratorio por código.

---

## 11. Registros mínimos obligatorios

Cada ronda EA genera los siguientes registros:

| Registro | Descripción |
|---|---|
| Plan estadístico del esquema | Firmado por estadístico y coordinador EA. |
| Base de datos cruda | Datos originales recibidos de cada participante, sin modificar. |
| Base de datos depurada | Datos después de la depuración, con control de cambios trazable. |
| Registros de caracterización del ítem | Valores de referencia, certificados MRC. |
| Registro de exclusiones | Lista de datos excluidos con causa técnica, fecha y justificación. |
| Selección de x_pt y σ_pt | Documento de decisión con la justificación del método seleccionado en la jerarquía. |
| Cálculo de u(x_pt), u_hom, u_stab, u(x_pt,def) | Detalle de cada componente, valores numéricos y fórmulas aplicadas. |
| Evidencia de convergencia o fallback del Algoritmo A | Log de iteraciones, valores de x* y s* por ciclo, verificación de convergencia o activación de fallback. |
| Verificación de homogeneidad y estabilidad | Resultados del ANOVA, valores de s_s, δ, u_hom, u_stab y criterio de aceptación. |
| Tabla de puntajes | x_i, x_pt, σ_pt, u(x_pt), z, z', ζ, En (según aplique) y clasificación por participante. |
| Informe técnico de análisis | Gráficos diagnósticos, evaluación de multimodalidad, conclusiones. |
| Registro de revisiones y aprobaciones | Firmas de revisión técnica y aprobación. |

**Criterios de revisión técnica:**

El diseño estadístico y los resultados deben ser revisados técnicamente antes de la emisión del informe. La revisión debe verificar:

- Coherencia con el plan estadístico aprobado.
- Adecuación de los métodos seleccionados al número de participantes.
- Validez de los supuestos estadísticos (normalidad, suficiencia de datos).
- Ausencia de errores en cálculos o fórmulas.
- Coherencia entre gráficos y resultados numéricos.
- Adecuación de la interpretación y conclusiones.
- Cumplimiento de requisitos de ISO 13528:2022 e ISO/IEC 17043:2023.

La revisión técnica debe ser realizada por personal distinto del que realizó el análisis, cuando sea posible, para asegurar imparcialidad.

---

## 12. Referencias cruzadas

| Documento | Relación |
|---|---|
| P-PSEA-09 | P-PSEA-09 establece **qué** se planifica en la ronda; P-PSEA-06 establece **cómo** se sustenta estadísticamente. |
| P-PSEA-07 | Utiliza los registros generados por P-PSEA-06 para la emisión del informe de resultados. |
| P-PSEA-08 | Se consulta cuando los patrones de datos sugieren colusión o falsificación. |
| ISO 13528:2022 | Base normativa para todos los métodos estadísticos: estimadores robustos, incertidumbre del valor asignado, homogeneidad, estabilidad, puntajes z, z', ζ, En. |
| ISO/IEC 17043:2023 | Base normativa para autorización del personal, diseño estadístico, control de datos y confidencialidad. |

---

| REVISÓ |  | APROBÓ |  |
| --- | :--- | :--- | :--- |
| **ROL** | Estadístico | **ROL** | Coordinador EA |
| **FECHA** |  | **FECHA** |  |
