# P-PSEA-06 — Diseño Estadístico para Ensayos de Aptitud de Gases Contaminantes Criterio

**Código:** P-PSEA-06  
**Versión:** 2.0  
**Fecha de emisión:** 2026-03-22  
**Referencia normativa:** ISO/IEC 17043:2023, ISO 13528:2022  
**Procedimientos relacionados:** P-PSEA-09  

---

## 1. Información general del procedimiento

### 1.1 Objetivo

Establecer las reglas estadísticas para diseñar, calcular y validar la evaluación de desempeño en las rondas de ensayos de aptitud (EA) de gases contaminantes criterio —SO₂, NO/NO₂, CO y O₃— organizadas por el Laboratorio CALAIRE, conforme a ISO 13528:2022 e ISO/IEC 17043:2023. Este procedimiento define la determinación del valor asignado, la estimación de la desviación estándar para la evaluación de aptitud, la integración de los estudios de homogeneidad y estabilidad, y la interpretación de los puntajes de desempeño.

### 1.2 Alcance

Este procedimiento aplica al diseño estadístico de todas las rondas EA organizadas por el Laboratorio CALAIRE. Abarca la etapa de diseño estadístico (planificación), la verificación de suficiencia de datos, la estimación de parámetros robustos, el cálculo de la incertidumbre asociada al valor asignado, la evaluación del desempeño de los participantes y el tratamiento de escenarios con bajo número de participantes.

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

### 3.2 Tipo de datos y suficiencia de participantes

Los resultados del EA deben ser cuantitativos, expresados en unidades de concentración (nmol/mol, μmol/mol, ppb o ppm) normalizadas y metrológicamente consistentes.

Las reglas por tamaño de muestra son:

| Condición | Enfoque estadístico |
|---|---|
| p ≥ 12 | Puede emplearse consenso robusto bajo control técnico. |
| 6 ≤ p < 12 | Se prioriza valor asignado externo y σ_pt prescriptiva; se utilizan métodos robustos con cautela. |
| p < 6 | No se utiliza consenso como base principal de desempeño. Se aplica valor asignado externo, σ_pt prescriptiva y estadístico En o ζ. |

Para esquemas por consenso, el criterio de insignificancia de la incertidumbre del valor asignado es:

`u(x_pt) ≤ 0,3 × σ_pt`

Cuando este criterio no se cumple, el puntaje z clásico no es la métrica principal y debe emplearse z', ζ o En conforme a la sección 7 de este procedimiento.

### 3.3 Preparación y depuración de datos

Antes del cálculo se ejecuta la depuración siguiente:

1. Normalizar unidades y códigos de participante.
2. Excluir datos no válidos (NA, valores no finitos, errores de unidad, envíos fuera de la ventana de reporte).
3. Documentar cada exclusión con la causa técnica, la fecha y la identificación del registro afectado.

La exclusión de resultados se limita a: errores de unidad o transcripción evidentes, incumplimiento de instrucciones del esquema, o datos no finitos. No se excluyen datos por desempeño estadístico sin justificación técnica.

### 3.4 Jerarquía de selección del valor asignado (x_pt)

El valor asignado se determina siguiendo la jerarquía de preferencia descendente. Se selecciona el primer método viable conforme a la disponibilidad de recursos y la naturaleza del esquema.

| Orden | Método | Descripción | Cuándo es viable |
|---|---|---|---|
| 1 | **Valor formulado** | Mezcla gaseosa preparada gravimétricamente (ISO 6142-1) con concentración conocida y trazable al SI. | Siempre que se disponga de patrón de masa calibrado y capacidad de preparación. |
| 2 | **Material de referencia certificado (MRC)** | Valor certificado de un CRM con trazabilidad a un NMI o laboratorio acreditado. | Cuando se dispone de un CRM vigente con incertidumbre adecuada para el propósito. |
| 3 | **Laboratorio de referencia** | Resultado de un laboratorio competente con trazabilidad metrológica demostrada. | Cuando se cuenta con un NMI, laboratorio de referencia acreditado o experto designado. |
| 4 | **Consenso de expertos** | Valor derivado de un panel de laboratorios expertos designado, no participantes en la evaluación. | Cuando los métodos anteriores no son viables y se dispone de al menos 3 laboratorios expertos. |
| 5 | **Consenso de participantes** | Estimación robusta a partir de los resultados de los participantes. | Solo cuando p ≥ 12 y se cumplen los criterios de insignificancia. |

Cuando se selecciona el método de consenso de participantes (orden 5), se aplica la sección 4 de este procedimiento.

### 3.5 Jerarquía de selección de σ_pt

La desviación estándar para la evaluación de la aptitud se determina siguiendo la jerarquía de preferencia. Se selecciona el primer método viable.

| Orden | Método | Descripción | Fundamento normativo |
|---|---|---|---|
| 1 | **Prescriptivo / regulatorio** | σ_pt fijada por requisito regulatorio, especificación técnica o panel de expertos del sector. Para gases contaminantes criterio, se toma como referencia la incertidumbre expandida máxima del 15% establecida por la Directiva 2008/50/CE para mediciones fijas de SO₂, NO₂, CO y O₃. | ISO 13528:2022, cláusula 8.1. |
| 2 | **Aptitud para el propósito** | σ_pt definida por un comité técnico del esquema en función del uso previsto de los resultados. | ISO 13528:2022, cláusula 8.2. |
| 3 | **Datos históricos robustos** | σ_pt derivada de la desviación estándar de reproducibilidad de rondas equivalentes anteriores, utilizando estimadores robustos. | ISO 13528:2022, cláusula 8.3. |
| 4 | **Modelo predictivo** | σ_pt calculada a partir de un modelo empírico del desempeño esperado del sistema de medición (por ejemplo, la ecuación de Horwitz-Thompson modificada donde aplique). | ISO 13528:2022, cláusula 8.4. |
| 5 | **Modelo metrológico** | σ_pt derivada de un modelo metrológico del sistema de medición, considerando la incertidumbre objetivo. | ISO 13528:2022, cláusula 8.5. |
| 6 | **Estimación robusta desde participantes** | σ_pt estimada como s*, MADe o nIQR a partir de los resultados de los participantes. Solo procede cuando p ≥ 12 y el valor asignado es independiente de los participantes. | ISO 13528:2022, cláusula 8.6. |

### 3.6 Estimadores robustos y Algoritmo A

Cuando el valor asignado se determina por consenso de participantes, se utiliza el Algoritmo A de ISO 13528:2022 (Anexo C.3) como método robusto principal.

**Inicialización:**
- x*₀ = mediana(x_i)
- s*₀ = 1,483 × mediana(|x_i − x*₀|)

**Iteración:**
Para cada ciclo k = 1, 2, ... :

1. Winsorización: para cada x_i, si |x_i − x*_{k-1}| > 1,5 × s*_{k-1}, se reemplaza x_i por x*_{k-1} + 1,5 × s*_{k-1} × signo(x_i − x*_{k-1}).
2. Se recalcula x*_k como la media aritmética de los valores winsorizados.
3. Se recalcula s*_k como la desviación estándar de los valores winsorizados.
4. Se verifica convergencia: si |x*_k − x*_{k-1}| < tolerancia y |s*_k − s*_{k-1}| < tolerancia, el algoritmo converge.

**Tolerancia institucional:** se define como el menor valor entre 0,001 × x*_{k-1} y 10⁻⁶ en las unidades del mensurando. El número máximo de iteraciones es 100.

**Manejo de no convergencia:**

Si el Algoritmo A no converge o produce una escala inestable (s* < 0 o变异系数的异常变化), se aplican los mecanismos de contingencia en el siguiente orden:

1. **Fallback 1:** Médiana + MADe (estimadores no paramétricos directos).
2. **Fallback 2:** Evaluación del estimador Q_n como alternativa robusta con mayor punto de ruptura.
3. **Fallback 3:** Escalamiento a revisión técnica por el estadístico, con decisión documentada sobre la validez del valor asignado antes de liberar la evaluación.

### 3.7 Determinación de la incertidumbre del valor asignado

#### 3.7.1 Componente por caracterización (consenso)

Cuando el valor asignado se deriva de consenso de participantes:

`u(x_pt) = 1,25 × s* / √p`

donde s* es el estimador robusto de dispersión y p es el número de participantes válidos.

#### 3.7.2 Componente por heterogeneidad

La contribución por heterogeneidad se estima como:

`u_hom = s_s`

donde s_s es la desviación estándar entre unidades de ensayo, determinada en el estudio de homogeneidad posterior al envasado final.

#### 3.7.3 Componente por estabilidad

Sean δ = (x_fin − x_ini) el cambio del valor asignado entre el inicio y el final de la ventana de la ronda, y σ_pt el criterio establecido:

- Si |δ| ≤ 0,3 × σ_pt, entonces u_stab = 0.
- Si |δ| > 0,3 × σ_pt, entonces u_stab = |δ| / √3.

#### 3.7.4 Incertidumbre definitiva

`u(x_pt,def) = √[ u(x_pt)² + u_hom² + u_stab² ]`

---

## 4. Evaluación de homogeneidad y estabilidad

### 4.1 Evaluación de homogeneidad

Se selecciona una muestra representativa del lote de ítems de ensayo (mínimo 10 unidades) extraídas en diferentes posiciones de la línea de envasado y a diferentes tiempos. Las unidades se ensayan en condiciones de repetibilidad dentro de un mismo laboratorio.

Se aplica un ANOVA de una vía con las unidades como factor. La varianza entre unidades (s_s²) se compara con el objetivo (0,3 × σ_pt)².

**Criterio de aceptación:** s_s ≤ 0,3 × σ_pt. Si no se cumple, u_hom = s_s y se incorpora a u(x_pt,def).

### 4.2 Evaluación de estabilidad

Se seleccionan al menos dos tiempos representativos del ciclo de la ronda (por ejemplo, inicio y final de la ventana de reporte). Se miden al menos dos unidades en cada tiempo, en las mismas condiciones.

Se evalúa la diferencia entre tiempos (δ) y se aplica el criterio de la sección 3.7.3. Si |δ| > 0,3 × σ_pt, la inestabilidad se cuantifica como u_stab y se incorpora a u(x_pt,def).

### 4.3 Verificación de modalidad de distribución

Antes de consolidar el análisis se ejecuta una revisión visual (ISO 13528:2022, cláusula 6.4):

1. Histograma y gráfico de densidad kernel de los resultados.
2. Boxplot para identificar valores extremos.
3. Evaluación de multimodalidad: si la distribución sugiere múltiples poblaciones (clusters), se aplica lo siguiente:
   - Investigar las variables explicativas (método, equipo, calibración, laboratorio).
   - Si la segmentación es técnicamente justificada, evaluar con x_pt, σ_pt e interpretación independientes por subgrupo.
   - Documentar la decisión y la justificación en el expediente de la ronda.
   - Si la segmentación no es viable, reportar advertencia técnica en el informe.

---

## 5. Selección del estadístico de desempeño

### 5.1 Árbol de decisión

La selección del estadístico sigue la regla de decisión siguiente:

```
¿u(x_pt) ≤ 0,3 × σ_pt?
  ├── Sí, y los participantes NO reportan incertidumbre:
  │       → z = (x_i − x_pt) / σ_pt
  ├── Sí, y los participantes SÍ reportan incertidumbre:
  │       → z = (x_i − x_pt) / σ_pt
  │       → ζ = (x_i − x_pt) / √[u(x_i)² + u(x_pt)²]  (complementario)
  └── No (u(x_pt) > 0,3 × σ_pt):
          → z' = (x_i − x_pt) / √[σ_pt² + u(x_pt)²]
          → En caso de incertidumbres expandidas: En = (x_i − x_pt) / √[U_i² + U_pt²]
```

### 5.2 Fórmulas de los estadísticos

| Estadístico | Fórmula | Condición de uso | Umbral satisfactorio |
|---|---|---|---|
| z | z = (x_i − x_pt) / σ_pt | u(x_pt) ≤ 0,3 × σ_pt; sin incertidumbre de participante | \|z\| ≤ 2 |
| z' | z' = (x_i − x_pt) / √(σ_pt² + u(x_pt)²) | u(x_pt) > 0,3 × σ_pt; valor asignado con incertidumbre significativa | \|z'\| ≤ 2 |
| ζ (zeta) | ζ = (x_i − x_pt) / √(u(x_i)² + u(x_pt)²) | Se requiere incertidumbre de participante; se evalúa compatibilidad | \|ζ\| ≤ 2 |
| En | En = (x_i − x_pt) / √(U_i² + U_pt²) | Incertidumbres expandidas (k = 2); comparaciones de calibración | \|En\| ≤ 1 |

### 5.3 Interpretación institucional

| |z|, |z'|, |ζ| | Clasificación | Acción |
|---|---|---|---|
| ≤ 2 | Satisfactorio | Ninguna intervención requerida. |
| > 2 y < 3 | Cuestionable | Se recomienda investigación preliminar de posibles causas. |
| ≥ 3 | No satisfactorio | Se requiere investigación, acciones correctivas documentadas y seguimiento. |

| |En| | Clasificación | Acción |
|---|---|---|
| ≤ 1 | Satisfactorio | Compatibilidad metrológica demostrada. |
| > 1 | No satisfactorio | Incompatibilidad; requiere investigación. |

---

## 6. Gestión de participantes excluidos y criterios de viabilidad

### 6.1 Causas de exclusión

Se excluyen del conjunto evaluable los resultados con alguna de las siguientes causas:

1. Entrega fuera de la ventana de reporte definida en F-PSEA-01 / DG-PSEA-01.
2. Errores de unidad o dato no trazable.
3. Inconsistencia metrológica no subsanada tras solicitud de aclaración.
4. Ausencia de información mínima obligatoria (resultado, método, fecha).
5. Incumplimiento de las instrucciones de I-PSEA-01 que comprometa la validez del dato.

### 6.2 Mínimo viable para esquemas por consenso

Para que un esquema por consenso sea estadísticamente viable:

- Se requiere un mínimo de **p ≥ 6** participantes válidos para iniciar el cálculo del valor asignado.
- Si después de la depuración p < 6, se activa la regla de continuidad: se declara el valor asignado externo como método de respaldo y se recalcula la σ_pt prescriptiva correspondiente.

### 6.3 Registro de exclusiones

El informe EA reporta:

1. Número total de laboratorios inscritos.
2. Número de participantes que reportaron resultados.
3. Número y causas de exclusiones, con referencia a la sección de este procedimiento que las justifica.
4. Número de participantes evaluados finalmente.
5. Evaluación del mínimo viable y la decisión tomada.

---

## 7. Registros mínimos obligatorios

Cada ronda EA genera los siguientes registros:

| Registro | Descripción |
|---|---|
| Base de datos cruda | Datos originales recibidos de cada participante, sin modificar. |
| Base de datos depurada | Datos después de la depuración, con control de cambios trazable. |
| Registro de exclusiones | Lista de datos excluidos con causa técnica, fecha y justificación. |
| Selección de x_pt y σ_pt | Documento de decisión con la justificación del método seleccionado en la jerarquía. |
| Cálculo de u(x_pt), u_hom, u_stab, u(x_pt,def) | Detalle de cada componente, valores numéricos y fórmulas aplicadas. |
| Evidencia de convergencia o fallback del Algoritmo A | Log de iteraciones, valores de x* y s* por ciclo, verificación de convergencia o activación de fallback. |
| Tabla de puntajes | x_i, x_pt, σ_pt, u(x_pt), z, z', ζ, En (según aplique) y clasificación por participante. |
| Verificación de homogeneidad y estabilidad | Resultados del ANOVA, valores de s_s, δ, u_hom, u_stab y criterio de aceptación. |

---

## 8. Limitaciones para escenarios con menos de 12 participantes

Cuando p < 12, se aplican las siguientes reglas adicionales:

1. **No se deriva σ_pt de la dispersión observada de los participantes.**
2. **Se aplica σ_pt prescriptiva** conforme al orden 1 de la sección 3.5 de este procedimiento.
3. **Se utiliza valor asignado externo** conforme a los órdenes 1 a 3 de la sección 3.4.
4. **El puntaje principal es En** cuando los participantes declaren incertidumbres expandidas; en caso contrario, se utiliza z'.
5. **Los métodos robustos** (Algoritmo A, Q_n) **no se emplean como base para el valor asignado o σ_pt**, sino solo como diagnóstico complementario.
6. **Se documenta expresamente** en el informe de la ronda que el esquema opera con un número reducido de participantes y se explican las implicaciones estadísticas.

---

## 9. Referencias cruzadas

| Documento | Relación |
|---|---|
| P-PSEA-09 | P-PSEA-09 establece qué se planifica en la ronda; P-PSEA-06 establece cómo se sustenta estadísticamente. |
| P-PSEA-07 | Utiliza los registros generados por P-PSEA-06 para la emisión del informe de resultados. |
| P-PSEA-08 | Se consulta cuando los patrones de datos sugieren colusión o falsificación. |
| ISO 13528:2022 | Base normativa para todos los métodos estadísticos: estimadores robustos, incertidumbre del valor asignado, homogeneidad, estabilidad, puntajes z, z', ζ, En. |
| ISO/IEC 17043:2023 | Base normativa para autorización del personal, diseño estadístico, control de datos y confidencialidad. |

---

| REVISÓ |  | APROBÓ |  |
| --- | :--- | :--- | :--- |
| **ROL** |  | **ROL** |  |
| **FECHA** |  | **FECHA** |  |
