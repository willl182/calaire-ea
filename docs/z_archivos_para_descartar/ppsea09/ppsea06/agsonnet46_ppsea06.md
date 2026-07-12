# P-PSEA-06 — Diseño Estadístico para Ensayos de Aptitud de Gases Contaminantes Criterio

**Código:** P-PSEA-06  
**Versión:** 3.0  
**Fecha de emisión:** 2026-03-22  
**Referencia normativa:** ISO/IEC 17043:2023, ISO 13528:2022  
**Procedimientos relacionados:** P-PSEA-09, P-PSEA-07, P-PSEA-08  

---

## 1. Información general del procedimiento

### 1.1 Objetivo

Establecer las reglas estadísticas para diseñar, calcular y validar la evaluación de desempeño en las rondas de ensayos de aptitud (EA) de gases contaminantes criterio —SO₂, NO/NO₂, CO y O₃— organizadas por el Laboratorio CALAIRE, conforme a ISO 13528:2022 e ISO/IEC 17043:2023. Este procedimiento define: la determinación del valor asignado, la estimación de la desviación estándar para la evaluación de aptitud, la integración de los resultados de los estudios de homogeneidad y estabilidad en el presupuesto de incertidumbre, el tratamiento de escenarios con bajo número de participantes, la detección de multimodalidad y el tratamiento de participantes excluidos.

### 1.2 Alcance

Este procedimiento aplica al diseño estadístico de todas las rondas EA organizadas por el Laboratorio CALAIRE. Abarca la etapa de diseño estadístico, la verificación de suficiencia de datos, la estimación de parámetros robustos, el cálculo de la incertidumbre asociada al valor asignado, la evaluación del desempeño de los participantes y el tratamiento de escenarios críticos reducidos (p < 12 y p < 6).

### 1.3 Definiciones

| Término | Definición |
|---|---|
| x_pt | Valor asignado al mensurando del EA. |
| σ_pt | Desviación estándar para la evaluación de la aptitud; medida de dispersión preestablecida contra la cual se compara la desviación de cada participante. |
| u(x_pt) | Incertidumbre estándar del valor asignado por la vía de caracterización estadística (consenso, formulación o referencia). |
| u(x_pt,def) | Incertidumbre estándar definitiva del valor asignado, integrada con las contribuciones por homogeneidad y estabilidad: √[u(x_pt)² + u_hom² + u_stab²]. |
| u_hom | Contribución a la incertidumbre del valor asignado debida a la heterogeneidad del lote de ítems de ensayo. |
| u_stab | Contribución a la incertidumbre del valor asignado debida a la inestabilidad del ítem durante la ronda. |
| p | Número de participantes válidos incluidos en el cálculo del valor asignado. |
| x* | Estimador robusto de ubicación (media robusta) obtenido mediante el Algoritmo A. |
| s* | Estimador robusto de dispersión (desviación estándar robusta) obtenido mediante el Algoritmo A. |
| Algoritmo A | Procedimiento iterativo de winsorización para estimar x* y s* simultáneamente, conforme a ISO 13528:2022, Anexo C.3. |
| MADe | Desviación absoluta mediana escalada: 1,483 × mediana(\|x_i − mediana(x)\|). Factor institucional: 1,483. |
| nIQR | Rango intercuartílico normalizado: 0,7413 × (Q₃ − Q₁), equivalente a IQR/1,349. |
| Q_n | Estimador robusto de escala basado en diferencias absolutas por pares, conforme a ISO 13528:2022, Anexo C. Mayor punto de ruptura que MADe. |

---

## 2. Roles y responsabilidades

| Rol | Responsabilidad |
|---|---|
| Estadístico / Experto técnico | Define el diseño estadístico, selecciona los métodos aplicables, ejecuta los cálculos, supervisa la convergencia del Algoritmo A y valida la coherencia técnica de los resultados. |
| Coordinador EA | Aprueba el diseño estadístico, verifica la conformidad con ISO 13528:2022 e ISO/IEC 17043:2023 y autoriza la emisión de resultados. |
| Ingeniero operativo | Garantiza la calidad de los datos de entrada, las condiciones técnicas de preparación del ítem y la trazabilidad de los registros primarios. |
| Profesional de calidad | Verifica el control documental, la vigencia del procedimiento y la evidencia de cumplimiento. |

---

## 3. Diseño estadístico

### 3.1 Definición del objetivo estadístico

Antes de definir el modelo estadístico de la ronda, se establece el objetivo técnico del EA y la finalidad de la evaluación de desempeño. Los objetivos pueden comprender:

1. Evaluar el desempeño de los laboratorios frente a un criterio preestablecido.
2. Comparar métodos o equipos de medición.
3. Detectar sesgos o tendencias sistemáticas.
4. Validar la trazabilidad y reproducibilidad de resultados.

### 3.2 Tipo de datos y suficiencia de participantes

Los resultados del EA deben ser cuantitativos, expresados en unidades de concentración normalizadas (nmol/mol, μmol/mol, ppb o ppm) y metrológicamente consistentes.

**Reglas por tamaño de muestra (p = número de participantes válidos):**

| Condición | Regla estadística aplicable |
|---|---|
| p ≥ 17 | Consenso robusto (Algoritmo A); u(x_pt) ≤ 0,3 σ_pt verificable cuando s* ≈ σ_pt. |
| 12 ≤ p < 17 | Consenso robusto viable; verificar que u(x_pt) ≤ 0,3 σ_pt antes de aplicar puntaje z. |
| 6 ≤ p < 12 | Contingencia: valor asignado externo u órdenes 1–3 de §3.4; σ_pt prescriptiva; puntaje z', ζ o En. |
| p < 6 | No se aplica consenso como base de desempeño. Valor asignado externo obligatorio; σ_pt prescriptiva; puntaje En o z'. Ver §8. |

**Criterio de insignificancia de u(x_pt):**

Para que el puntaje z clásico sea la métrica principal, debe verificarse:

`u(x_pt) ≤ 0,3 × σ_pt`

Si este criterio no se cumple, el estadístico principal pasa a z', y se complementa con ζ o En cuando los participantes declaran incertidumbre.

### 3.3 Preparación y depuración de datos

Antes del cálculo se ejecuta la siguiente depuración:

1. Normalizar unidades y códigos de participante.
2. Excluir datos no válidos: NA, valores no finitos (Inf, −Inf), errores de unidad, envíos fuera de la ventana de reporte definida en F-PSEA-01 y DG-PSEA-01.
3. Documentar cada exclusión con la causa técnica, la fecha y la identificación del registro afectado.

La exclusión de resultados se limita a: errores de unidad o transcripción evidentes, incumplimiento de instrucciones del esquema o datos no finitos. **No se excluyen datos por desempeño estadístico adverso sin justificación técnica objetiva y aprobación del estadístico.**

### 3.4 Jerarquía de selección del valor asignado (x_pt)

El valor asignado se determina siguiendo la jerarquía de preferencia descendente. Se selecciona el primer método viable conforme a la disponibilidad de recursos y la naturaleza del esquema.

| Orden | Método | Descripción | Condición de viabilidad |
|---|---|---|---|
| 1 | **Valor formulado** | Mezcla gaseosa preparada gravimétricamente (ISO 6142-1) con concentración conocida y trazable al SI. | Siempre que se disponga de patrón de masa calibrado y capacidad de preparación acreditada. |
| 2 | **Material de referencia certificado (MRC)** | Valor del certificado de un CRM con trazabilidad a un NMI o laboratorio acreditado (ISO 17034). | Cuando se dispone de un MRC vigente con incertidumbre certificada adecuada para el propósito. |
| 3 | **Laboratorio de referencia** | Resultado de un laboratorio competente con trazabilidad metrológica demostrada y reconocida. | Cuando se cuenta con un NMI, laboratorio de referencia acreditado o experto designado. |
| 4 | **Consenso de expertos** | Valor derivado de un panel de laboratorios expertos designados, no participantes en la evaluación. | Cuando los órdenes 1–3 no son viables y se dispone de al menos 3 laboratorios expertos independientes. |
| 5 | **Consenso de participantes** | Estimación robusta (x*) a partir de los resultados de los participantes del EA. | **Solo cuando p ≥ 12** y se cumple u(x_pt) ≤ 0,3 σ_pt. |

Cuando se aplica el orden 5, el valor asignado se determina mediante el Algoritmo A conforme al §3.6 de este procedimiento.

### 3.5 Jerarquía de selección de σ_pt

La desviación estándar para la evaluación de la aptitud se determina siguiendo la jerarquía de preferencia. Se selecciona el primer método viable.

| Orden | Método | Descripción | Fundamento normativo |
|---|---|---|---|
| 1 | **Prescriptivo / regulatorio** | σ_pt fijada por requisito regulatorio, especificación técnica o panel de expertos del sector. Para gases contaminantes criterio se toma como referencia la incertidumbre expandida máxima del 15% establecida por la Directiva 2008/50/CE para mediciones fijas de SO₂, NO₂, CO y O₃. σ_pt ≈ 7,5% de la concentración objetivo (U = 2σ_pt). | ISO 13528:2022, §8.1. |
| 2 | **Aptitud para el propósito** | σ_pt definida por un comité técnico del esquema en función del uso previsto de los resultados de la ronda. | ISO 13528:2022, §8.2. |
| 3 | **Datos históricos robustos** | σ_pt derivada de la desviación estándar de reproducibilidad de rondas previas equivalentes, usando estimadores robustos. Requiere mínimo 3 rondas con datos fiables. | ISO 13528:2022, §8.3. |
| 4 | **Modelo predictivo** | σ_pt calculada a partir de un modelo empírico del desempeño esperado del sistema de medición; por ejemplo, la ecuación de Horwitz-Thompson modificada donde aplique. | ISO 13528:2022, §8.4. |
| 5 | **Modelo metrológico** | σ_pt derivada de un modelo metrológico del sistema de medición, considerando la incertidumbre objetivo declarada. | ISO 13528:2022, §8.5. |
| 6 | **Estimación robusta desde participantes** | σ_pt estimada como s*, MADe o nIQR a partir de los resultados de los participantes. **Solo procede cuando p ≥ 12** y el valor asignado es de fuente independiente (órdenes 1–4 de §3.4). | ISO 13528:2022, §8.6. |

**Cuando p < 12:** no se utiliza el orden 6. Se aplica obligatoriamente el orden 1 (prescriptivo).

### 3.6 Estimadores robustos y Algoritmo A

Cuando el valor asignado se determina por consenso de participantes (orden 5 de §3.4), se aplica el Algoritmo A de ISO 13528:2022, Anexo C.3, como método principal.

#### 3.6.1 Inicialización

- x*₀ = mediana(x_i)
- s*₀ = 1,483 × mediana(|x_i − x*₀|)

Si s*₀ = 0 o no es finito, se utiliza la desviación estándar clásica como mecanismo de respaldo inicial. Si la dispersión resultante sigue siendo nula o no finita, el conjunto de datos no presenta variabilidad suficiente para la aplicación informativa del algoritmo y se declara como caso de revisión técnica.

#### 3.6.2 Iteración

Para cada ciclo k = 1, 2, ...:

1. **Winsorización:** calcular el umbral δ_k = 1,5 × s*_{k−1}. Para cada x_i:
   - Si x_i < x*_{k−1} − δ_k, reemplazar por x*_{k−1} − δ_k.
   - Si x_i > x*_{k−1} + δ_k, reemplazar por x*_{k−1} + δ_k.
   - En otro caso, mantener x_i.
2. **Actualización de ubicación:** x*_k = media aritmética de los valores winsorizados.
3. **Actualización de dispersión:** s*_k = 1,134 × desviación estándar de los valores winsorizados respecto a x*_k. El factor 1,134 es obligatorio y corrige el sesgo introducido por la winsorización.
4. **Verificación de convergencia:** si max(|x*_k − x*_{k−1}|, |s*_k − s*_{k−1}|) < tolerancia, el algoritmo converge.

#### 3.6.3 Tolerancia y número máximo de iteraciones

La tolerancia institucional se define como: **toler = min(0,001 × x*_{k−1}, 10⁻⁴)** en las unidades del mensurando. El número máximo de iteraciones es **50**. Si este límite se alcanza sin convergencia, el resultado se clasifica como no convergente y se activa el mecanismo de contingencia.

#### 3.6.4 Mecanismo de contingencia ante no convergencia

Si el Algoritmo A no converge o produce una escala inestable (s* ≤ 0 o cambios erráticos de escala), se aplican los mecanismos siguientes en orden estricto:

1. **Fallback 1:** Mediana + MADe (estimadores no paramétricos directos). x_pt = mediana(x_i); s* = MADe = 1,483 × mediana(|x_i − mediana(x_i)|).
2. **Fallback 2:** Estimador Q_n conforme a ISO 13528:2022, Anexo C, como alternativa con mayor punto de ruptura que MADe.
3. **Fallback 3:** Escalamiento a revisión técnica por el estadístico, con decisión documentada sobre la validez del valor asignado antes de liberar la evaluación.

El uso de cualquier fallback se registra en el expediente de la ronda con la justificación técnica detallada.

#### 3.6.5 Estimadores auxiliares de dispersión

- **MADe:** s* = 1,483 × mediana(|x_i − mediana(x)|). El factor institucional es **1,483** (no 1,4826). Se aplica cuando se requiere un estimador robusto simple de dispersión.
- **nIQR:** nIQR = 0,7413 × (Q₃ − Q₁). Se aplica como alternativa robusta cuando conviene contrastar MADe frente a distribuciones no estrictamente normales.
- **Q_n:** estimador robusto basado en diferencias absolutas por pares, conforme a ISO 13528:2022, Anexo C. Posee mayor punto de ruptura (50%) y se aplica como fallback 2 del Algoritmo A.

---

## 4. Incertidumbre del valor asignado

### 4.1 Componente por caracterización estadística (consenso de participantes)

Cuando el valor asignado se determina por consenso de participantes:

`u(x_pt) = 1,25 × s* / √p`

donde s* es el estimador robusto de dispersión y p es el número de participantes válidos.

### 4.2 Componente por heterogeneidad

La contribución por heterogeneidad del lote a la incertidumbre del valor asignado se estima como:

`u_hom = s_s`

donde s_s es la desviación estándar entre unidades de ensayo, determinada en el estudio de homogeneidad conforme a §5.1.

Si el criterio de homogeneidad se cumple (s_s < 0,3 σ_pt), se documenta pero puede adoptarse u_hom = s_s de todas formas para incorporar la contribución real. La decisión se registra en el expediente.

### 4.3 Componente por inestabilidad

Sea δ = |x_fin − x_ini| la diferencia absoluta entre el valor asignado al inicio y al final de la ventana de la ronda:

- Si δ ≤ 0,3 × σ_pt → u_stab = 0.
- Si δ > 0,3 × σ_pt → u_stab = δ / √3.

### 4.4 Incertidumbre definitiva

La incertidumbre estándar definitiva del valor asignado integra todas las contribuciones:

`u(x_pt,def) = √[ u(x_pt)² + u_hom² + u_stab² ]`

El presupuesto completo de incertidumbre, con los valores numéricos de cada componente, se documenta en el expediente de la ronda.

---

## 5. Evaluación de homogeneidad y estabilidad

### 5.1 Evaluación de homogeneidad

Se selecciona una muestra representativa del lote de ítems de ensayo (mínimo 10 unidades) extraídas en diferentes posiciones de la línea de envasado y a diferentes tiempos. Las unidades se ensayan en condiciones de repetibilidad dentro de un mismo laboratorio.

#### 5.1.1 Media por ítem

Para cada ítem i con m réplicas:

`x̄_i = (1/m) × Σ x_ij`

#### 5.1.2 Varianza entre medias de ítem

`s²_x̄ = [1/(g−1)] × Σ (x̄_i − x̄̄)²`

donde g es el número de ítems y x̄̄ es la media global de las medias por ítem.

#### 5.1.3 Varianza dentro de ítem (para m = 2 réplicas)

`s_w = √{ [1/(2g)] × Σ (x_i1 − x_i2)² }`

#### 5.1.4 Componente de varianza entre ítems

`s²_s = s²_x̄ − s²_w / m`

Si s²_s < 0, se adopta s_s = 0. En caso contrario, s_s = √(s²_s).

#### 5.1.5 Criterio de aceptación de homogeneidad

- **Criterio básico:** s_s < 0,3 σ_pt. Si se cumple, el lote se declara suficientemente homogéneo.
- **Criterio expandido:** conforme a ISO 13528:2022, Tabla 4: MS_b ≤ F₁ × (0,3 σ_pt)² + F₂ × MS_w.

Si el criterio no se cumple, u_hom = s_s y se incorpora a u(x_pt,def).

### 5.2 Evaluación de estabilidad

Se seleccionan al menos dos tiempos representativos del ciclo de la ronda (inicio y final de la ventana de reporte). Se miden al menos dos unidades en cada tiempo, en las mismas condiciones.

La diferencia media entre la condición de referencia y la condición de estabilidad:

`δ = |ȳ₁ − ȳ₂|`

donde ȳ₁ es la media de la condición de referencia y ȳ₂ es la media bajo la condición de estabilidad.

Se aplica el criterio de §4.3. Si |δ| > 0,3 σ_pt, se calcula u_stab = δ / √3 y se incorpora a u(x_pt,def).

### 5.3 Verificación de modalidad de distribución

Antes de consolidar el análisis estadístico se realiza la revisión diagnóstica de la distribución de resultados (ISO 13528:2022, §6.4):

1. Elaborar histograma y gráfico de densidad kernel de los resultados válidos.
2. Construir boxplot para identificar valores extremos.
3. Evaluar multimodalidad: si la distribución sugiere múltiples poblaciones (clusters), se procede así:
   - Investigar las variables explicativas: método de medición, equipo, laboratorio, calibración.
   - Si la segmentación es técnicamente justificada, definir x_pt, σ_pt y evaluación independiente por subgrupo metodológico.
   - Si la segmentación no es viable o no tiene sustento técnico, reportar advertencia técnica en el informe de la ronda, sin modificar el conjunto global de evaluación.
   - Documentar la decisión y su justificación en el expediente de la ronda.

---

## 6. Selección del estadístico de desempeño

### 6.1 Árbol de decisión

La selección del estadístico de desempeño sigue la siguiente lógica:

```
¿Se conoce u(x_pt)?
  ├── Sí:
  │     ¿u(x_pt) ≤ 0,3 × σ_pt?
  │       ├── Sí (u(x_pt) insignificante):
  │       │     ¿Los participantes reportan incertidumbre?
  │       │       ├── No  → z = (x_i − x_pt) / σ_pt
  │       │       └── Sí  → z (principal); ζ (complementario para compatibilidad)
  │       └── No (u(x_pt) significativa):
  │             ¿Los participantes reportan incertidumbre expandida?
  │               ├── No  → z' = (x_i − x_pt) / √(σ_pt² + u(x_pt)²)
  │               └── Sí  → En = (x_i − x_pt) / √(U_i² + U_pt²)
  └── No (valor asignado externo sin u conocida):
        Véase caso p < 12 en §8.
```

### 6.2 Fórmulas de los estadísticos

| Estadístico | Fórmula | Condición de uso |
|---|---|---|
| z | z = (x_i − x_pt) / σ_pt | u(x_pt) ≤ 0,3 σ_pt; participantes no declaran incertidumbre. |
| z' | z' = (x_i − x_pt) / √(σ_pt² + u(x_pt)²) | u(x_pt) > 0,3 σ_pt; valor asignado con incertidumbre significativa. |
| ζ (zeta) | ζ = (x_i − x_pt) / √(u(x_i)² + u(x_pt)²) | Se requiere incertidumbre estándar de participante u(x_i); evalúa compatibilidad metrológica. |
| En | En = (x_i − x_pt) / √(U_i² + U_pt²) | Incertidumbres expandidas (U = k·u, k = 2); comparaciones de calibración y escenarios p < 12. |

### 6.3 Interpretación institucional

| Estadístico | Valor | Clasificación | Acción requerida |
|---|---|---|---|
| z, z', ζ | \|score\| ≤ 2 | Satisfactorio | Sin intervención. |
| z, z', ζ | 2 < \|score\| < 3 | Cuestionable | Investigación preliminar documentada. |
| z, z', ζ | \|score\| ≥ 3 | No satisfactorio | Investigación obligatoria; acciones correctivas documentadas; seguimiento. |
| En | \|En\| ≤ 1 | Satisfactorio | Compatibilidad metrológica demostrada. Sin intervención. |
| En | \|En\| > 1 | No satisfactorio | Incompatibilidad; investigación y acciones correctivas. |

La categoría "cuestionable" no aplica a En porque este puntaje expresa compatibilidad metrológica con criterio binario.

---

## 7. Gestión de participantes excluidos y criterios de viabilidad

### 7.1 Causas de exclusión

Se excluyen del conjunto evaluable los resultados que presenten alguna de las siguientes causas:

1. Entrega fuera de la ventana de reporte definida en F-PSEA-01 / DG-PSEA-01.
2. Error de unidad, transcripción o conversión no subsanado.
3. Inconsistencia metrológica no resuelta tras solicitud de aclaración al participante.
4. Ausencia de información mínima obligatoria (resultado, método, fecha, código de participante).
5. Incumplimiento de instrucciones de I-PSEA-01 que comprometa la validez del dato.

### 7.2 Mínimo viable para esquemas por consenso

| Condición | Acción |
|---|---|
| p ≥ 12 tras depuración | El esquema por consenso es estadísticamente viable. |
| 6 ≤ p < 12 tras depuración | Activar contingencia: valor asignado externo (órdenes 1–3 de §3.4) y σ_pt prescriptiva. Evaluar con z' o En. |
| p < 6 tras depuración | Activar las reglas del §8. Declarar el valor asignado externo como método único. El esquema no puede basar la evaluación en consenso. |

### 7.3 Registro de exclusiones

El informe de la ronda reporta los siguientes datos de gestión:

1. Número total de laboratorios inscritos.
2. Número de participantes que enviaron resultados.
3. Número y causas de exclusiones, con referencia a §7.1 del presente procedimiento.
4. Número de participantes evaluados finalmente.
5. Evaluación del mínimo viable y la decisión tomada.
6. Tasa de exclusión (exclusiones / inscritos) y análisis de impacto sobre la representatividad del esquema.

---

## 8. Reglas específicas para escenarios con número reducido de participantes (p < 12)

Cuando p < 12, se aplican las siguientes reglas adicionales sin excepción:

1. **No se deriva σ_pt de la dispersión observada de los participantes.** La σ_pt procede obligatoriamente del orden 1 (prescriptivo/regulatorio) de §3.5.
2. **Se utiliza valor asignado externo** conforme a los órdenes 1–3 de §3.4. El consenso de participantes queda excluido como opción.
3. **El estadístico principal es En** cuando los participantes declaran incertidumbre expandida (U = k·u), o z' cuando no la declaran.
4. **Los métodos robustos** (Algoritmo A, MADe, Q_n, nIQR) **no se emplean como base para x_pt o σ_pt.** Solo pueden utilizarse con carácter diagnóstico complementario, no para tomar decisiones de desempeño.
5. **Se documenta expresamente** en el informe de la ronda que el esquema opera con un número reducido de participantes, se explican las implicaciones estadísticas y se indica que la evaluación se basa en un valor asignado externo con σ_pt prescriptiva.
6. **Para p < 6,** se aplican las mismas reglas anteriores con el nivel máximo de cautela. El estadístico principal es En. La validez estadística del esquema queda sujeta a revisión técnica por el estadístico antes de la emisión del informe.

---

## 9. Registros mínimos obligatorios

Cada ronda EA genera los siguientes registros en el expediente:

| Registro | Descripción |
|---|---|
| Base de datos cruda | Datos originales recibidos de cada participante, sin modificar, con marca de tiempo de recepción. |
| Base de datos depurada | Datos después de la depuración, con control de cambios trazable y causas de exclusión. |
| Registro de exclusiones | Lista detallada de datos excluidos: causa técnica (§7.1), fecha y justificación. |
| Selección de x_pt y σ_pt | Documento de decisión: método seleccionado (jerarquía), valores numéricos, justificación técnica. |
| Presupuesto de incertidumbre | u(x_pt), u_hom, u_stab y u(x_pt,def): fórmulas aplicadas, valores numéricos, criterios de decisión. |
| Evidencia de Algoritmo A | Log de iteraciones: x* y s* por ciclo, verificación de convergencia o activación de fallback con justificación. |
| Diagnóstico de distribución | Histograma, density plot, boxplot; evaluación de multimodalidad con conclusión documentada. |
| Verificación de H&E | Resultados del estudio: s_s, δ, u_hom, u_stab y criterio de aceptación (§5.1 y §5.2). |
| Tabla de puntajes | Por participante: x_i, x_pt, σ_pt, u(x_pt), estadístico(s) calculados, clasificación de desempeño. |
| Decisión sobre número de participantes | Evaluación del mínimo viable, reglas de contingencia aplicadas (§7.2 y §8) y justificación. |

---

## 10. Referencias cruzadas

| Documento | Relación |
|---|---|
| P-PSEA-09 | P-PSEA-09 establece qué se planifica en la ronda EA; P-PSEA-06 establece cómo se sustenta estadísticamente. |
| P-PSEA-07 | Utiliza los registros generados por P-PSEA-06 (tabla de puntajes, incertidumbre, clasificación) para la emisión del informe. |
| P-PSEA-08 | Se consulta cuando los patrones estadísticos detectados en P-PSEA-06 sugieren colusión o falsificación. |
| ISO 13528:2022 | Base normativa para todos los métodos estadísticos: Algoritmo A (Anexo C.3), MADe, nIQR, Q_n, incertidumbre del valor asignado, homogeneidad (§6.1), estabilidad (§6.2), puntajes z, z', ζ, En (§9). |
| ISO/IEC 17043:2023 | Base normativa para autorización de personal, diseño estadístico, control de datos, confidencialidad y evaluación de desempeño. |
| F-PSEA-01 | Define la ventana de reporte que determina la exclusión de datos tardíos. |
| DG-PSEA-01 | Define los requisitos de reporte, unidades y formato que determinan la validez de los datos recibidos. |

---

| REVISÓ |   | APROBÓ |   |
| --- | :--- | :--- | :--- |
| **ROL** |   | **ROL** |   |
| **FECHA** |   | **FECHA** |   |
