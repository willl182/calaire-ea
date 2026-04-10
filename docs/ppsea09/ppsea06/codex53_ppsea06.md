# P-PSEA-06 - Diseño Estadístico para Ensayos de Aptitud

## 1. Información general del procedimiento

**Objetivo**  
Establecer las reglas estadísticas para diseñar, calcular y validar la evaluación de desempeño en rondas de ensayos de aptitud (EA) de gases contaminantes criterio, conforme a ISO 13528:2022 e ISO/IEC 17043:2023.

**Alcance**  
Aplica a la determinación de valor asignado, desviación estándar para evaluación de aptitud (`sigma_pt`), incertidumbre, análisis de homogeneidad y estabilidad, y cálculo de estadísticos de desempeño (`z`, `z'`, `zeta`, `En`) para SO2, NO/NO2, CO y O3.

## 2. Roles y responsabilidades

- **Estadístico/experto técnico:** define diseño estadístico, selecciona métodos y valida coherencia técnica.
- **Coordinador EA:** aprueba el diseño y autoriza su uso en la ronda.
- **Ingeniero operativo:** asegura calidad de datos de entrada, condiciones técnicas y trazabilidad de registros primarios.
- **Profesional de calidad:** verifica control documental, cambios, versiones y evidencia de cumplimiento.

## 3. Desarrollo del diseño estadístico

### 3.1 Definición de objetivo estadístico
Cada ronda debe declarar explícitamente si el objetivo principal es:
- evaluación de aptitud frente a un criterio (`sigma_pt`),
- comparación metrológica basada en incertidumbre,
- o ambas, en análisis complementarios.

### 3.2 Tipo de datos y suficiencia de participantes
Los resultados deben ser cuantitativos, en unidades normalizadas y metrológicamente consistentes.  
Reglas base:
- `p >= 12`: puede emplearse consenso robusto bajo control técnico.
- `p < 12`: se prioriza valor asignado externo y `sigma_pt` prescriptiva.
- `p < 5`: no se usa consenso como base principal de desempeño; se aplica enfoque de contingencia con referencias externas y evaluación reforzada.

Para esquemas por consenso, el criterio de insignificancia de incertidumbre del valor asignado es:

`u(x_pt) <= 0.3 * sigma_pt`

Cuando no se cumple, no procede puntaje `z` clásico como métrica principal.

### 3.3 Preparación y depuración de datos
Previo al cálculo:
- normalizar unidades y códigos de participante,
- excluir datos no válidos (NA, no finitos, errores de unidad, envío fuera de ventana),
- documentar exclusiones con causa técnica y fecha.

### 3.4 Jerarquía de selección del valor asignado (`x_pt`)
Orden de preferencia:
1. Valor por formulación/metrología de referencia del esquema.
2. Valor certificado de MRC o material caracterizado.
3. Resultado de laboratorio de referencia con trazabilidad demostrada.
4. Consenso de expertos con sustento documental.
5. Consenso de participantes (solo cuando la base de datos es suficiente y defendible).

### 3.5 Jerarquía de selección de `sigma_pt` (ISO 13528, enfoque de diseño)
Orden de preferencia:
1. `sigma_pt` prescriptiva por requisito regulatorio/especificación técnica.
2. Criterio de aptitud para propósito definido por comité técnico.
3. Históricos robustos de rondas equivalentes.
4. Modelo predictivo justificado (p. ej., Horwitz/Thompson donde aplique).
5. Modelo metrológico derivado de desempeño esperado del sistema de medición.
6. Estimación robusta desde participantes (`s*`, MADe, nIQR), solo cuando el tamaño muestral y la calidad del conjunto lo soportan.

### 3.6 Estimadores robustos y Algoritmo A
El Algoritmo A se utiliza como método robusto principal cuando aplica consenso de participantes.

Inicialización:
- `x*_0 = mediana(x_i)`
- `s*_0 = 1.483 * mediana(|x_i - x*_0|)`

Iteración por winsorización con límite `1.5 * s*`, actualización de `x*` y `s*`, y verificación de convergencia por tolerancia institucional.

Si el algoritmo no converge o produce escala inestable:
1. aplicar `mediana + MADe`,
2. evaluar `Q_n` como estimador alternativo robusto,
3. escalar a revisión técnica antes de liberar evaluación.

### 3.7 Determinación de incertidumbre del valor asignado

Componente estadística (cuando hay caracterización por consenso):

`u(x_pt) = 1.25 * s* / sqrt(p)`

Componente por homogeneidad:

`u_hom = s_s`

Componente por estabilidad:
- si `|delta| <= 0.3 * sigma_pt`, `u_stab = 0`,
- si `|delta| > 0.3 * sigma_pt`, `u_stab = |delta| / sqrt(3)`.

Incertidumbre definitiva:

`u(x_pt,def) = sqrt( u(x_pt)^2 + u_hom^2 + u_stab^2 )`

### 3.8 Evaluación de homogeneidad y estabilidad
Se realiza antes de la evaluación final de desempeño y con trazabilidad de:
- plan de muestreo de ítems,
- resultados brutos,
- modelo aplicado,
- decisión técnica de aceptación/rechazo.

### 3.9 Selección del estadístico de desempeño

Regla de decisión:
1. Si `u(x_pt) <= 0.3 * sigma_pt` y no se requiere incertidumbre del participante, usar `z`.
2. Si `u(x_pt) > 0.3 * sigma_pt`, usar `z'`.
3. Si se evalúa compatibilidad con incertidumbres estándar (`u(x_i)`, `u(x_pt)`), usar `zeta`.
4. Si se evalúa compatibilidad con incertidumbres expandidas (`U_i`, `U_pt`), usar `En`.

Fórmulas:
- `z = (x_i - x_pt) / sigma_pt`
- `z' = (x_i - x_pt) / sqrt(sigma_pt^2 + u(x_pt)^2)`
- `zeta = (x_i - x_pt) / sqrt(u(x_i)^2 + u(x_pt)^2)`
- `En = (x_i - x_pt) / sqrt(U_i^2 + U_pt^2)`

Interpretación:
- `|z|, |z'|, |zeta| <= 2`: satisfactorio.
- `2 < |score| < 3`: cuestionable.
- `|score| >= 3`: no satisfactorio.
- `|En| <= 1`: satisfactorio.
- `|En| > 1`: no satisfactorio.

### 3.10 Detección de multimodalidad y sesgos de subgrupos
Cuando la distribución sugiera múltiples poblaciones:
- evaluar densidad (KDE) y boxplots por subgrupo,
- aplicar gráficos de Youden en pares de niveles o replicados,
- revisar variables explicativas (método, equipo, calibración, laboratorio),
- documentar si corresponde segmentar evaluación o reportar advertencia técnica.

### 3.11 Gestión de participantes excluidos
Se excluyen del conjunto evaluable resultados con:
- entrega fuera de plazo definido en F-PSEA-01/DG-PSEA-01,
- errores de unidad o dato no trazable,
- inconsistencia metrológica no subsanada,
- ausencia de información mínima obligatoria.

El informe debe reportar:
- número total de inscritos,
- número evaluado,
- número y causas de exclusión,
- evaluación del mínimo viable para sostener la validez del esquema.

## 4. Registros mínimos obligatorios

- Base de datos cruda y base depurada (con control de cambios).
- Registro de exclusiones.
- Selección y justificación de `x_pt` y `sigma_pt`.
- Cálculos de `u(x_pt)`, `u_hom`, `u_stab`, `u(x_pt,def)`.
- Evidencias de convergencia o fallback del algoritmo.
- Tabla de puntajes y clasificación por participante.

## 5. Referencia cruzada con P-PSEA-09

P-PSEA-06 establece la metodología estadística detallada que P-PSEA-09 exige declarar en la planificación de cada ronda.

