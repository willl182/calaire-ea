| INFORMACION GENERAL DEL PROCEDIMIENTO |
| --- |
| **CODIGO:** P-PSEA-06 |
| **VERSION:** 4.0-candidata |
| **FECHA DE EMISION:** 2026-03-22 |
| **OBJETIVO:** Establecer las reglas estadisticas aplicables al diseno, calculo, validacion y evaluacion de los ensayos de aptitud para gases contaminantes criterio desarrollados por CALAIRE, conforme a ISO 13528:2022 e ISO/IEC 17043:2023. El procedimiento define la determinacion del valor asignado, la seleccion de la desviacion estandar para evaluacion de aptitud, el presupuesto de incertidumbre, la evaluacion de homogeneidad y estabilidad, y las reglas para interpretar el desempeno de los participantes. |
| **ALCANCE:** Aplica a las rondas de ensayo de aptitud para SO2, NO, NO2, O3 y CO. Cubre la preparacion y depuracion de datos, la seleccion del modelo estadistico, el tratamiento de escenarios con pocos participantes, la deteccion de multimodalidad, la gestion de exclusiones y la emision de puntajes z, z', zeta y En, segun corresponda. |
| **DOCUMENTOS DE REFERENCIA:** ISO 13528:2022. ISO/IEC 17043:2023. ISO/IEC 17025:2017. ISO 6142-1:2015. P-PSEA-09. P-PSEA-07. P-PSEA-08. F-PSEA-01. DG-PSEA-01. I-PSEA-01. |
| **CONDICIONES GENERALES:** La seleccion del modelo estadistico debe ser coherente con el objetivo del esquema, el tipo de mensurando, la fuente del valor asignado, la disponibilidad de incertidumbres y el numero de participantes validos. Se deben privilegiar, siempre que sean tecnicamente viables, las fuentes de valor asignado y de sigma_pt independientes de los resultados de los participantes. |

## 1. Definiciones

| Termino | Definicion |
| --- | --- |
| x_pt | Valor asignado al mensurando del ensayo de aptitud. |
| sigma_pt | Desviacion estandar para la evaluacion de la aptitud. |
| u(x_pt) | Incertidumbre estandar del valor asignado segun su metodo de obtencion. |
| u(x_pt,def) | Incertidumbre estandar definitiva del valor asignado, integrada con homogeneidad y estabilidad. |
| u_hom | Contribucion por heterogeneidad del lote de items. |
| u_stab | Contribucion por inestabilidad del item durante la ronda. |
| p | Numero de participantes validos incluidos en el analisis. |
| x* | Estimador robusto de ubicacion obtenido mediante Algoritmo A. |
| s* | Estimador robusto de dispersion obtenido mediante Algoritmo A. |
| MADe | Desviacion absoluta mediana escalada: 1,483 x mediana(|x_i - mediana(x)|). |
| nIQR | Rango intercuartilico normalizado: 0,7413 x (Q3 - Q1), equivalente a IQR/1,349. |
| Q_n | Estimador robusto de dispersion basado en diferencias absolutas por pares, conforme al Anexo C de ISO 13528:2022. |
| Q/Hampel | Metodo robusto en dos pasos: Q para dispersion y Hampel para ubicacion. |

## 2. Roles y responsabilidades

| Rol | Responsabilidad |
| --- | --- |
| Estadistico o experto tecnico | Define y ejecuta el modelo estadistico, selecciona x_pt, sigma_pt y el puntaje de desempeno, verifica la convergencia del algoritmo y documenta las decisiones metodologicas. |
| Coordinador EA | Aprueba el diseno estadistico, valida la coherencia con P-PSEA-09 y autoriza la emision de resultados. |
| Ingeniero operativo | Asegura la integridad de los datos de entrada, la trazabilidad tecnica de los items y la disponibilidad de resultados de homogeneidad y estabilidad. |
| Profesional de calidad | Controla la vigencia documental, la trazabilidad de registros y la evidencia de revision y aprobacion. |

## 3. Desarrollo del diseno estadistico

### 3.1 Objetivo estadistico de la ronda

Antes de calcular cualquier parametro, se debe declarar el objetivo tecnico de la ronda. El diseno puede orientarse a:

1. Evaluar desempeno frente a un criterio preestablecido.
2. Comparar laboratorios, metodos o equipos de medicion.
3. Verificar compatibilidad metrologica con incertidumbres declaradas.
4. Detectar sesgos, tendencias sistematicas o diferencias entre subgrupos.

El objetivo condiciona la seleccion de x_pt, sigma_pt y del estadistico de desempeno.

### 3.2 Tipo de datos y suficiencia de participantes

Los resultados deben ser cuantitativos, expresados en unidades de concentracion normalizadas y metrologicamente consistentes. Antes del analisis se debe verificar coherencia de analito, nivel, unidades, fecha de reporte e incertidumbre declarada, cuando aplique.

La suficiencia de participantes se interpreta asi:

| Condicion | Regla institucional |
| --- | --- |
| p >= 20 | Puede aplicarse consenso robusto con Algoritmo A o Q/Hampel. La dispersion observada puede usarse con fines diagnosticos y, solo si no existe una opcion superior, apoyar la seleccion de sigma_pt. |
| 17 <= p < 20 | El consenso robusto es viable, pero el uso de z basado en consenso requiere verificar explicitamente u(x_pt) <= 0,3 x sigma_pt. |
| 12 <= p < 17 | El consenso robusto solo procede con justificacion tecnica expresa y sin desplazar fuentes independientes superiores. En este rango, z' suele ser el puntaje principal. |
| 6 <= p < 12 | No se usa consenso como base de x_pt o sigma_pt. Se utiliza valor asignado externo y sigma_pt prescriptiva o por aptitud para el uso. |
| p < 6 | Se aplica el mismo enfoque externo con maxima cautela. El estadistico principal es En cuando existan incertidumbres expandidas; en otro caso, z'. |

Para esquemas por consenso, el criterio de insignificancia de la incertidumbre del valor asignado es:

`u(x_pt) <= 0,3 x sigma_pt`

Si este criterio no se cumple, el puntaje z no debe usarse como metrica principal. Cuando s* es del mismo orden de sigma_pt, este criterio exige tipicamente al menos 17 participantes validos, por lo que en poblaciones reducidas debe preferirse z', zeta o En segun la informacion disponible.

Cuando el numero de participantes sea insuficiente para sostener el modelo inicialmente previsto, el cambio metodologico debe documentarse y comunicarse en el expediente de la ronda y en el informe final.

### 3.3 Preparacion y depuracion de datos

Antes del analisis se debe:

1. Normalizar unidades, codigos de participante, analitos y niveles.
2. Verificar cifras significativas, consistencia formal y ventana de reporte definida en F-PSEA-01 y DG-PSEA-01.
3. Excluir del analisis principal los valores faltantes, no finitos, tecnicamente invalidos o reportados fuera de plazo cuando asi lo exija el plan.
4. Registrar toda exclusion con causa tecnica, fecha y responsable de la decision.

Se consideran causales tipicas de exclusion: errores de unidad o transcripcion no subsanados, incumplimiento de instrucciones de I-PSEA-01, ausencia de informacion minima obligatoria e inconsistencia metrologica no resuelta. No se excluyen resultados solamente por mostrar mal desempeno estadistico.

### 3.4 Jerarquia de seleccion del valor asignado

La seleccion de x_pt se realiza en el siguiente orden de preferencia. Debe elegirse el primer metodo tecnicamente viable:

| Orden | Metodo | Criterio de uso |
| --- | --- | --- |
| 1 | Valor formulado | Mezcla gaseosa preparada con trazabilidad metrologica demostrada, por ejemplo gravimetria o dilucion dinamica adecuadamente controlada. |
| 2 | Material de referencia certificado | Uso de CRM o MRC vigente con incertidumbre adecuada para el proposito del esquema. |
| 3 | Laboratorio de referencia | Resultado de laboratorio competente con trazabilidad demostrada. |
| 4 | Consenso de expertos | Panel de laboratorios expertos no participantes, con soporte documental suficiente. |
| 5 | Consenso de participantes | Alternativa de ultima instancia, solo cuando no exista fuente mejor y la base de datos sea tecnicamente defendible. |

Cuando se utilice consenso de participantes, la decision debe justificar por que no fue posible aplicar un metodo de mayor independencia. Para p < 12, el consenso de participantes queda excluido como opcion para el valor asignado.

### 3.5 Jerarquia de seleccion de sigma_pt

La desviacion estandar para evaluacion de aptitud se selecciona en el siguiente orden:

| Orden | Metodo | Criterio de uso |
| --- | --- | --- |
| 1 | Prescriptiva o regulatoria | Requisito regulatorio, especificacion tecnica o criterio formal adoptado por el esquema. |
| 2 | Aptitud para el uso | Criterio definido por el comite tecnico en funcion del uso previsto de los resultados. |
| 3 | Datos historicos robustos | Evidencia de reproducibilidad de rondas equivalentes o desempeno historico comparable. |
| 4 | Modelo predictivo | Modelo empirico del desempeno esperado del sistema de medicion, cuando resulte aplicable. |
| 5 | Modelo metrologico | Derivacion de sigma_pt a partir de incertidumbre objetivo o desempeno esperado del sistema. |
| 6 | Estimacion robusta desde participantes | Uso de s*, MADe o nIQR solo cuando exista soporte tecnico suficiente y no haya una opcion superior. |

Para p < 12, no se deriva sigma_pt de la dispersion observada de los participantes. En ese escenario debe usarse obligatoriamente un criterio de los ordenes 1 o 2.

La comparacion entre la sigma_pt adoptada y la dispersion robusta observada puede documentarse como verificacion diagnostica, pero no reemplaza una fuente superior sin justificacion tecnica expresa.

### 3.6 Estimadores robustos y Algoritmo A

Cuando la ronda se sustente en consenso de participantes, el Algoritmo A de ISO 13528:2022 es el metodo robusto institucional principal. Para muestras moderadas o pequenas, Q/Hampel puede usarse como contraste diagnostico y, si el contexto lo justifica, como alternativa robusta preferible a Algoritmo A por estabilidad.

#### 3.6.1 Inicializacion

- x*_0 = mediana(x_i)
- s*_0 = 1,483 x mediana(|x_i - x*_0|)

Si s*_0 es nula o no finita, se usa la desviacion estandar clasica como respaldo inicial. Si la dispersion resultante sigue siendo nula o no finita, el conjunto se declara no apto para aplicacion informativa del algoritmo y se remite a revision tecnica.

#### 3.6.2 Iteracion

Para cada iteracion k:

1. Calcular el umbral de winsorizacion delta_k = 1,5 x s*_(k-1).
2. Reemplazar cada valor fuera de los limites x*_(k-1) +/- delta_k por el limite correspondiente.
3. Calcular x*_k como la media de los valores winsorizados.
4. Calcular s*_k = 1,134 x desviacion estandar de los valores winsorizados respecto a x*_k.
5. Verificar convergencia comparando x*_k y s*_k con la iteracion anterior.

#### 3.6.3 Tolerancia y maximo de iteraciones

La tolerancia institucional es:

`toler = min(0,001 x |x*_(k-1)|, 1 x 10^-4)`

El numero maximo de iteraciones es 50. Si no hay convergencia dentro de ese limite, el resultado se clasifica como no convergente.

#### 3.6.4 Contingencia por no convergencia

Si el Algoritmo A no converge o produce una escala inestable, se aplica el siguiente orden:

1. Mediana + MADe.
2. Estimador Q_n.
3. Revision tecnica formal para decidir si se mantiene un enfoque de consenso o se migra a un valor asignado externo.

El fallback debe quedar registrado con su justificacion tecnica. En escenarios p < 12, estos estimadores solo se admiten como diagnostico complementario y no como base de decision sobre x_pt o sigma_pt.

## 4. Incertidumbre del valor asignado

### 4.1 Componente por caracterizacion

Cuando x_pt se determine por consenso de participantes, puede emplearse:

`u(x_pt) = 1,25 x s* / sqrt(p)`

Si x_pt proviene de valor formulado, material de referencia certificado o laboratorio de referencia, se usa la incertidumbre documentada por ese metodo de asignacion.

### 4.2 Componente por homogeneidad

La contribucion por homogeneidad se expresa como:

`u_hom = s_s`

donde s_s es la desviacion estandar entre unidades estimada en el estudio de homogeneidad.

### 4.3 Componente por estabilidad

Sea:

`delta = |x_fin - x_ini|`

Entonces:

- si delta <= 0,3 x sigma_pt, u_stab = 0
- si delta > 0,3 x sigma_pt, u_stab = delta / sqrt(3)

### 4.4 Incertidumbre definitiva

La incertidumbre estandar definitiva del valor asignado se obtiene como:

`u(x_pt,def) = sqrt(u(x_pt)^2 + u_hom^2 + u_stab^2)`

El presupuesto de incertidumbre completo debe formar parte del expediente de la ronda.

## 5. Evaluacion de homogeneidad y estabilidad

### 5.1 Homogeneidad

La homogeneidad debe evaluarse antes del uso operativo del lote, con una muestra representativa de items y bajo condiciones de repetibilidad en un mismo laboratorio.

Se aplican las siguientes expresiones:

- media por item: `xbar_i = (1/m) x sum(x_ij)`
- varianza entre medias de item: `s2_xbar = [1/(g-1)] x sum((xbar_i - xbarbar)^2)`
- desviacion dentro de item para m = 2: `s_w = sqrt([1/(2g)] x sum((x_i1 - x_i2)^2))`
- componente entre items: `s2_s = s2_xbar - s2_w / m`

Si s2_s < 0, se adopta s_s = 0. En otro caso, `s_s = sqrt(s2_s)`.

El criterio basico de aceptacion es:

`s_s <= 0,3 x sigma_pt`

Cuando se requiera el criterio expandido de ISO 13528:2022, Tabla 4, se aplica:

`MS_b <= F1 x (0,3 x sigma_pt)^2 + F2 x MS_w`

Si la homogeneidad no es satisfactoria, u_hom debe incorporarse a u(x_pt,def) y la viabilidad del lote debe revisarse antes de continuar.

### 5.2 Estabilidad

La estabilidad debe verificarse comparando al menos dos tiempos representativos del ciclo de la ronda. La diferencia media entre la condicion de referencia y la condicion de estabilidad se calcula como:

`delta = |ybar_1 - ybar_2|`

Si `delta > 0,3 x sigma_pt`, la contribucion u_stab debe incorporarse al presupuesto y evaluarse si la ronda sigue siendo tecnicamente viable.

Como criterio operativo por analito:

- para CO, NO y SO2 en N2 pueden apoyarse decisiones en evidencia historica de estabilidad, siempre que siga siendo pertinente al esquema actual
- para NO2 en aire y O3 deben realizarse verificaciones especificas o aplicarse controles mas estrictos de tiempo y condiciones de uso

### 5.3 Revision diagnostica de la distribucion

Antes de emitir resultados se debe revisar la estructura de los datos mediante:

1. Histograma.
2. Grafico de densidad kernel.
3. Boxplot.
4. Grafico Q-Q.
5. Diagrama de Youden, cuando aplique.

Si la evidencia sugiere multimodalidad o subpoblaciones tecnicamente diferenciadas, debe investigarse la relacion con metodo, equipo, calibracion o laboratorio. Solo si la segmentacion tiene sustento tecnico se permite una evaluacion separada por subgrupo.

## 6. Seleccion del estadistico de desempeno

### 6.1 Regla de decision

La seleccion del estadistico se realiza asi:

1. Si `u(x_pt) <= 0,3 x sigma_pt` y no se requiere evaluar incertidumbre del participante, usar z.
2. Si `u(x_pt) > 0,3 x sigma_pt`, usar z'.
3. Si se requiere evaluar compatibilidad con incertidumbres estandar declaradas, usar zeta.
4. Si se dispone de incertidumbres expandidas y la evaluacion es de compatibilidad metrologica, usar En.

Para p < 12, el puntaje principal es En cuando existan incertidumbres expandidas; en otro caso, z'. En ese escenario, z y los estimadores robustos solo pueden usarse como diagnostico complementario.

### 6.2 Formulas

| Estadistico | Formula | Uso principal |
| --- | --- | --- |
| z | `z = (x_i - x_pt) / sigma_pt` | u(x_pt) insignificante frente a sigma_pt |
| z' | `z' = (x_i - x_pt) / sqrt(sigma_pt^2 + u(x_pt)^2)` | u(x_pt) significativa |
| zeta | `zeta = (x_i - x_pt) / sqrt(u(x_i)^2 + u(x_pt)^2)` | compatibilidad con incertidumbres estandar |
| En | `En = (x_i - x_pt) / sqrt(U_i^2 + U_pt^2)` | compatibilidad con incertidumbres expandidas |

### 6.3 Interpretacion

| Estadistico | Criterio | Clasificacion |
| --- | --- | --- |
| z, z', zeta | |score| <= 2 | satisfactorio |
| z, z', zeta | 2 < |score| < 3 | cuestionable |
| z, z', zeta | |score| >= 3 | no satisfactorio |
| En | |En| <= 1 | satisfactorio |
| En | |En| > 1 | no satisfactorio |

La categoria cuestionable no aplica a En.

## 7. Gestion de participantes excluidos y viabilidad del esquema

### 7.1 Causas de exclusion

Se excluyen del analisis principal los resultados que presenten:

1. entrega fuera de la ventana de reporte aplicable
2. error de unidad o conversion no subsanado
3. inconsistencia metrologica no resuelta
4. ausencia de informacion minima obligatoria
5. incumplimiento del protocolo que comprometa la validez del dato

Los resultados excluidos deben conservarse en el expediente tecnico.

### 7.2 Datos censurados

Cuando existan reportes del tipo "< LOD" o "> rango", se debe registrar la condicion de censura y documentar la decision metodologica. Si la proporcion de datos censurados compromete el analisis, se requiere revision tecnica antes de emitir evaluacion.

### 7.3 Minimo viable y reglas de contingencia

| Condicion tras depuracion | Decision |
| --- | --- |
| p >= 12 | Puede mantenerse un esquema por consenso si no existe una fuente mejor de x_pt y se justifica tecnicamente. |
| 6 <= p < 12 | Activar contingencia: valor asignado externo y sigma_pt de los ordenes 1 o 2 de la jerarquia. |
| p < 6 | Mantener solo enfoque externo, con revision tecnica previa a la emision del informe. |

En todos los casos debe reportarse el numero de inscritos, el numero de resultados recibidos, las exclusiones aplicadas, la tasa de exclusion y el impacto sobre la representatividad del esquema.

## 8. Registros minimos obligatorios

| Registro | Contenido minimo |
| --- | --- |
| Base de datos cruda | Resultados originales, con fecha de recepcion y sin modificacion. |
| Base de datos depurada | Datos usados en el analisis, con trazabilidad de cambios. |
| Registro de exclusiones | Causa tecnica, fecha, responsable y soporte. |
| Decision sobre x_pt y sigma_pt | Metodo seleccionado, jerarquia aplicada y justificacion. |
| Presupuesto de incertidumbre | u(x_pt), u_hom, u_stab y u(x_pt,def). |
| Evidencia de Algoritmo A o fallback | Iteraciones, convergencia y contingencia aplicada. |
| Evaluacion de homogeneidad y estabilidad | Valores calculados, criterios y conclusion. |
| Diagnostico grafico | Histograma, densidad, boxplot, Q-Q y Youden cuando aplique. |
| Tabla de puntajes | Estadisticos calculados, clasificacion e interpretacion por participante. |
| Revision y aprobacion | Evidencia de revision tecnica y autorizacion. |

## 9. Referencias cruzadas

| Documento | Relacion |
| --- | --- |
| P-PSEA-09 | Define que debe planificarse en la ronda; P-PSEA-06 define el sustento estadistico. |
| P-PSEA-07 | Usa los registros estadisticos para la emision del informe de resultados. |
| P-PSEA-08 | Se consulta cuando los patrones estadisticos sugieren colusion o falsificacion. |
| F-PSEA-01 | Define la ventana de reporte aplicable a exclusiones por plazo. |
| DG-PSEA-01 | Define requisitos de reporte, unidades y formato. |
| I-PSEA-01 | Establece instrucciones operativas cuyo incumplimiento puede invalidar resultados. |

| REVISO |  | APROBO |  |
| --- | :--- | :--- | :--- |
| **ROL** |  | **ROL** |  |
| **FECHA** |  | **FECHA** |  |
