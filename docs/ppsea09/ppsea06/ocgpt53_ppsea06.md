# P-PSEA-06 - Diseno Estadistico para Ensayos de Aptitud

## 1. Informacion general del procedimiento

**Objetivo**  
Establecer las reglas estadisticas para disenar, calcular y validar la evaluacion de desempeno en rondas de ensayos de aptitud (EA) de gases contaminantes criterio, conforme a ISO 13528:2022 e ISO/IEC 17043:2023.

**Alcance**  
Aplica a la determinacion de valor asignado, desviacion estandar para evaluacion de aptitud (`sigma_pt`), incertidumbre, analisis de homogeneidad y estabilidad, y calculo de estadisticos de desempeno (`z`, `z'`, `zeta`, `En`) para SO2, NO/NO2, CO y O3.

## 2. Roles y responsabilidades

- **Estadistico/experto tecnico:** define diseno estadistico, selecciona metodos y valida coherencia tecnica.
- **Coordinador EA:** aprueba el diseno y autoriza su uso en la ronda.
- **Ingeniero operativo:** asegura calidad de datos de entrada, condiciones tecnicas y trazabilidad de registros primarios.
- **Profesional de calidad:** verifica control documental, cambios, versiones y evidencia de cumplimiento.

## 3. Desarrollo del diseno estadistico

### 3.1 Definicion de objetivo estadistico
Cada ronda debe declarar explicitamente si el objetivo principal es:
- evaluacion de aptitud frente a un criterio (`sigma_pt`),
- comparacion metrologica basada en incertidumbre,
- o ambas, en analisis complementarios.

### 3.2 Tipo de datos y suficiencia de participantes
Los resultados deben ser cuantitativos, en unidades normalizadas y metrologicamente consistentes.  
Reglas base:
- `p >= 12`: puede emplearse consenso robusto bajo control tecnico.
- `p < 12`: se prioriza valor asignado externo y `sigma_pt` prescriptiva.
- `p < 5`: no se usa consenso como base principal de desempeno; se aplica enfoque de contingencia con referencias externas y evaluacion reforzada.

Para esquemas por consenso, el criterio de insignificancia de incertidumbre del valor asignado es:

`u(x_pt) <= 0.3 * sigma_pt`

Cuando no se cumple, no procede puntaje `z` clasico como metrica principal.

### 3.3 Preparacion y depuracion de datos
Previo al calculo:
- normalizar unidades y codigos de participante,
- excluir datos no validos (NA, no finitos, errores de unidad, envio fuera de ventana),
- documentar exclusiones con causa tecnica y fecha.

### 3.4 Jerarquia de seleccion del valor asignado (`x_pt`)
Orden de preferencia:
1. Valor por formulacion/metrologia de referencia del esquema.
2. Valor certificado de MRC o material caracterizado.
3. Resultado de laboratorio de referencia con trazabilidad demostrada.
4. Consenso de expertos con sustento documental.
5. Consenso de participantes (solo cuando la base de datos es suficiente y defendible).

### 3.5 Jerarquia de seleccion de `sigma_pt` (ISO 13528, enfoque de diseno)
Orden de preferencia:
1. `sigma_pt` prescriptiva por requisito regulatorio/especificacion tecnica.
2. Criterio de aptitud para proposito definido por comite tecnico.
3. Historicos robustos de rondas equivalentes.
4. Modelo predictivo justificado (por ejemplo, Horwitz/Thompson donde aplique).
5. Modelo metrologico derivado de desempeno esperado del sistema de medicion.
6. Estimacion robusta desde participantes (`s*`, MADe, nIQR), solo cuando el tamano muestral y la calidad del conjunto lo soportan.

### 3.6 Estimadores robustos y Algoritmo A
El Algoritmo A se utiliza como metodo robusto principal cuando aplica consenso de participantes.

Inicializacion:
- `x*_0 = mediana(x_i)`
- `s*_0 = 1.483 * mediana(|x_i - x*_0|)`

Iteracion por winsorizacion con limite `1.5 * s*`, actualizacion de `x*` y `s*`, y verificacion de convergencia por tolerancia institucional.

Si el algoritmo no converge o produce escala inestable:
1. aplicar `mediana + MADe`,
2. evaluar `Q_n` como estimador alternativo robusto,
3. escalar a revision tecnica antes de liberar evaluacion.

### 3.7 Determinacion de incertidumbre del valor asignado

Componente estadistica (cuando hay caracterizacion por consenso):

`u(x_pt) = 1.25 * s* / sqrt(p)`

Componente por homogeneidad:

`u_hom = s_s`

Componente por estabilidad:
- si `|delta| <= 0.3 * sigma_pt`, `u_stab = 0`,
- si `|delta| > 0.3 * sigma_pt`, `u_stab = |delta| / sqrt(3)`.

Incertidumbre definitiva:

`u(x_pt,def) = sqrt( u(x_pt)^2 + u_hom^2 + u_stab^2 )`

### 3.8 Evaluacion de homogeneidad y estabilidad
Se realiza antes de la evaluacion final de desempeno y con trazabilidad de:
- plan de muestreo de items,
- resultados brutos,
- modelo aplicado,
- decision tecnica de aceptacion/rechazo.

### 3.9 Seleccion del estadistico de desempeno

Regla de decision:
1. Si `u(x_pt) <= 0.3 * sigma_pt` y no se requiere incertidumbre del participante, usar `z`.
2. Si `u(x_pt) > 0.3 * sigma_pt`, usar `z'`.
3. Si se evalua compatibilidad con incertidumbres estandar (`u(x_i)`, `u(x_pt)`), usar `zeta`.
4. Si se evalua compatibilidad con incertidumbres expandidas (`U_i`, `U_pt`), usar `En`.

Formulas:
- `z = (x_i - x_pt) / sigma_pt`
- `z' = (x_i - x_pt) / sqrt(sigma_pt^2 + u(x_pt)^2)`
- `zeta = (x_i - x_pt) / sqrt(u(x_i)^2 + u(x_pt)^2)`
- `En = (x_i - x_pt) / sqrt(U_i^2 + U_pt^2)`

Interpretacion:
- `|z|, |z'|, |zeta| <= 2`: satisfactorio.
- `2 < |score| < 3`: cuestionable.
- `|score| >= 3`: no satisfactorio.
- `|En| <= 1`: satisfactorio.
- `|En| > 1`: no satisfactorio.

### 3.10 Deteccion de multimodalidad y sesgos de subgrupos
Cuando la distribucion sugiera multiples poblaciones:
- evaluar densidad (KDE) y boxplots por subgrupo,
- aplicar graficos de Youden en pares de niveles o replicados,
- revisar variables explicativas (metodo, equipo, calibracion, laboratorio),
- documentar si corresponde segmentar evaluacion o reportar advertencia tecnica.

### 3.11 Gestion de participantes excluidos
Se excluyen del conjunto evaluable resultados con:
- entrega fuera de plazo definido en F-PSEA-01/DG-PSEA-01,
- errores de unidad o dato no trazable,
- inconsistencia metrologica no subsanada,
- ausencia de informacion minima obligatoria.

El informe debe reportar:
- numero total de inscritos,
- numero evaluado,
- numero y causas de exclusion,
- evaluacion del minimo viable para sostener la validez del esquema.

## 4. Registros minimos obligatorios

- Base de datos cruda y base depurada (con control de cambios).
- Registro de exclusiones.
- Seleccion y justificacion de `x_pt` y `sigma_pt`.
- Calculos de `u(x_pt)`, `u_hom`, `u_stab`, `u(x_pt,def)`.
- Evidencias de convergencia o fallback del algoritmo.
- Tabla de puntajes y clasificacion por participante.

## 5. Referencia cruzada con P-PSEA-09

P-PSEA-06 establece la metodologia estadistica detallada que P-PSEA-09 exige declarar en la planificacion de cada ronda.
