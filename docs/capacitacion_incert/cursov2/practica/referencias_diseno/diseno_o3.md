# Diseño experimental PISTA O₃ — laboratorio de incertidumbre

## 1. Alcance, mensurando y reglas comunes

**Mensurando común:** fracción de cantidad de sustancia de O₃ en aire seco entregada al puerto de muestra del analizador o indicada por este, según experimento, expresada en **nmol/mol**.

**Equipos mínimos:** analizador UV de O₃ bajo prueba (UUT), calibrador-diluidor con generador de O₃, fotómetro patrón o patrón de transferencia con certificado vigente, generador de aire cero, distribuidor de vidrio o PTFE, tubería PFA/PTFE, rotámetro o medidor de flujo, termómetro, barómetro, cronómetro y sistema de adquisición capaz de registrar a 1 s y 1 min.

### 1.1 Seguridad y venteo, obligatorio en todos los experimentos con O₃

1. Trabajar en zona ventilada. No descargar O₃ al recinto.
2. Conectar salida del distribuidor y bypass a destructor catalítico de O₃ o extracción exterior dedicada.
3. Mantener venteo a presión atmosférica. No estrangular bypass ni conectar extractor capaz de producir depresión en distribuidor.
4. Confirmar flujo total del generador mayor que suma de demandas de patrón y UUT, con excedente de 10–20 %. Si demanda total es 2.0 L/min, usar 2.3–2.4 L/min.
5. Comprobar que desconectar temporalmente una rama no cambia presión del distribuidor más de 0.2 kPa ni indicación estable más de 0.5 nmol/mol.
6. Realizar prueba de fugas con aire cero antes de producir O₃: presurización máxima según fabricante o prueba de caída de presión de baja presión; nunca bloquear salida de instrumento. Alternativa operativa: variar bypass ±0.2 L/min; cambio de indicación >0.5 nmol/mol o ingreso de aire ambiente indica montaje no válido.
7. Ante olor, alarma, tubo suelto, destructor caliente fuera de especificación o pérdida de extracción: apagar generación de O₃, mantener aire cero 10 min, evacuar según plan local y registrar incidente.
8. Usar gafas, guantes para conexiones y protección definida por evaluación local. O₃ es oxidante y tóxico; no usar elastómeros incompatibles ni líneas de PVC.

### 1.2 Preparación común

- Encender fotómetro, calibrador y UUT con **mínimo 2 h** de anticipación, o tiempo mayor indicado por fabricante.
- Mantener sala entre 20 y 30 °C; registrar temperatura y presión.
- Usar PFA/PTFE o vidrio limpio. Minimizar uniones y volumen muerto.
- Purgar líneas nuevas con aire cero durante 10 min y acondicionar con O₃ a 150–180 nmol/mol durante 20 min antes de E2, E6 o E11.
- Criterio común de estabilización: cambio absoluto de media móvil de 1 min **<1.0 nmol/mol durante 5 min**, sin tendencia monotónica visible; además, desviación estándar de las últimas cinco medias de 1 min ≤0.5 nmol/mol. Registrar solo después de cumplir ambos criterios.
- Conservar datos crudos. Correcciones por certificado crean columnas nuevas; nunca sobrescriben indicaciones.
- Redondear solo al final.

### 1.3 Decisiones que resuelven vacíos 1–8 del brief

1. **Repetibilidad y precisión intermedia:** repetibilidad se estima con series dentro de sesión. Precisión intermedia usa mínimo 3 días, 2 ciclos por día y 3 promedios por nivel; ideal 7 días y al menos 2 operadores. Se informa `s_pooled` cuando no hay efecto de día significativo y componente ANOVA cuando lo hay.
2. **Promediado y n:** adquisición a 1 s para diagnóstico; resultado operativo por punto = media de cinco registros de 1 min después de estabilización. E1 calcula tamaño efectivo por autocorrelación; no supone 300 lecturas independientes.
3. **Orden multipunto:** tres ciclos independientes: ascendente, descendente y orden fijo pseudoaleatorio. Esto separa nivel de tiempo y permite revelar histéresis o deriva.
4. **Purga, acondicionamiento y calentamiento:** 2 h de calentamiento; 10 min de aire cero; 20 min de acondicionamiento a O₃ alto; fin de purga definido por estabilidad, no solo cronómetro.
5. **Aire cero:** E9 compara tres fuentes contra referencia común; aceptación propuesta: media absoluta ≤0.5 nmol/mol, diferencia entre fuentes ≤0.5 nmol/mol y ausencia de respuesta transitoria >1.0 nmol/mol.
6. **Fugas y venteo:** prueba previa obligatoria, bypass con 10–20 % de excedente y venteo sin presión/depresión a destructor o exterior.
7. **Transmisión de línea:** E6 compara línea patrón corta contra línea real con filtro a 150 nmol/mol, alternando configuraciones y calculando factor de transmisión y su incertidumbre.
8. **Presión sensor–celda:** se registra presión indicada por sensor y presión medida en punto próximo a celda cuando exista puerto seguro. Diferencia no se absorbe en “presión” genérica; queda como corrección o componente Tipo B. Si no existe acceso aprobado, se documenta como vacío y no se abre el instrumento.

---

# E1 — Ruido y repetibilidad de cero

## Objetivo y componente ilustrado

Cuantificar ruido de lectura, repetibilidad de cero e incertidumbre del promedio operativo. Ilustra evaluación Tipo A, diferencia entre `s` y `s/√n`, autocorrelación y término absoluto `u₀`.

## Instrumentos y montaje

Generador de aire cero, UUT, distribuidor PFA/vidrio, línea PFA corta, medidor de flujo y adquisición a 1 s. Aire cero alimenta UUT con excedente 10–20 %; bypass ventea a destructor/exterior.

## Procedimiento

1. Calentar UUT y generador 2 h.
2. Ejecutar prueba de fugas y confirmar bypass.
3. Purgar con aire cero 15 min.
4. Esperar estabilidad común durante 5 min.
5. Registrar 30 min a 1 s, sin cambiar configuración: 1800 observaciones nominales.
6. Continuar 20 min y registrar simultáneamente medias de 1 min o calcularlas desde datos de 1 s.
7. Repetir serie completa tres veces en mismo día, separando series con 5 min de aire cero estable. Para precisión intermedia, repetir en 3 días, dos series por día.
8. No ejecutar ajuste de cero entre series. Si ajuste es obligatorio, cerrar serie, guardar estado encontrado y marcar intervención.

**Tiempo activo:** 55–70 min.

## Tabla de registro

| fecha_hora | dia | operador | serie | segundo_desde_inicio | lectura_cruda_nmol_mol | media_1min_nmol_mol | T_amb_C | P_amb_kPa | flujo_L_min | estado_estable | ajuste_previo | incidencia |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|

## Modelo de cálculo

Para serie `x_t`, calcular media y desviación estándar:

\[
\bar x=\frac{1}{n}\sum x_t,\qquad s=\sqrt{\frac{\sum(x_t-\bar x)^2}{n-1}}.
\]

Autocorrelación muestral a retardo `k`:

\[
\rho_k=\frac{\sum_{t=1}^{n-k}(x_t-\bar x)(x_{t+k}-\bar x)}{\sum_{t=1}^{n}(x_t-\bar x)^2}.
\]

Usar suma hasta primer retardo donde autocorrelaciones dejan de ser positivas, o máximo razonable antes de ruido numérico:

\[
n_{ef}=\frac{n}{1+2\sum_{k=1}^{K}\left(1-\frac{k}{n}\right)\rho_k},\qquad
u_A\approx n_{ef}-1.
\]

Para aproximación AR(1), útil como comprobación:

\[
n_{ef}\approx n\frac{1-\rho_1}{1+\rho_1}.
\]

Incertidumbre de media:

\[
u(\bar x)=\frac{s}{\sqrt{n_{ef}}}.
\]

Término absoluto recomendado para una **lectura operativa de 1 min**:

\[
u_0=\sqrt{s_{1min}^2+u^2(\bar z)+u^2_{residual,aire\ cero}},
\]

sin agregar resolución si ya está visible dentro de dispersión observada.

## Ejemplo numérico trabajado

Serie resumida de 30 medias de 1 min: `n=30`, media `0.18 nmol/mol`, `s=0.31 nmol/mol`. Autocorrelaciones positivas: `ρ1=0.55`, `ρ2=0.30`, `ρ3=0.12`; siguiente valor negativo, por tanto `K=3`.

\[
D=1+2[(29/30)0.55+(28/30)0.30+(27/30)0.12]
=1+2(0.532+0.280+0.108)=2.840.
\]

\[
n_{ef}=30/2.840=10.56.
\]

Si resultado es media de 30 min:

\[
u(\bar x)=0.31/\sqrt{10.56}=0.095\ \mathrm{nmol/mol}.
\]

Usar `30` como n habría dado `0.057 nmol/mol`, subestimación de 40 %. Para resultado operativo de una media de 1 min, ruido relevante es `s₁min=0.31 nmol/mol`, no 0.095. Si E9 estima residual de aire cero `u=0.20 nmol/mol` y sesgo medio se corrige, entonces:

\[
u_0=\sqrt{0.31^2+0.20^2}=0.369\approx0.37\ \mathrm{nmol/mol}.
\]

## Criterios de aceptación

- Media de cero, estado encontrado: `|x̄| ≤1.0 nmol/mol`; objetivo interno recomendado `≤0.5 nmol/mol`.
- `s₁min ≤0.50 nmol/mol`; comparar además con especificación del fabricante para 60 s.
- Sin tendencia lineal absoluta >0.5 nmol/mol por 30 min.
- Si `n_ef/n <0.25`, revisar filtro digital y aumentar duración; no “arreglar” dividiendo por √n nominal.

## Riesgos

Ingreso de aire ambiente por bypass, condensación, ajuste automático durante serie y falsa independencia por filtro digital. No se genera O₃, pero venteo sigue conectado porque sistema puede conservar O₃ residual.

---

# E2 — Verificación multipunto O₃, tres ciclos

## Objetivo y componente ilustrado

Verificar relación entre patrón y UUT, cuantificar pendiente, intercepto, falta de ajuste, incertidumbre de predicción y estabilidad entre ciclos. Produce evidencia para término relativo `u_r`, residual local y precisión intermedia.

## Instrumentos y montaje

Patrón certificado y UUT en paralelo desde mismo distribuidor; calibrador con O₃; aire cero; líneas PFA de longitud semejante; flujo excedente 10–20 %; venteo seguro.

## Procedimiento

1. Calentar 2 h. Verificar vigencia y ecuación del certificado.
2. Probar fugas con aire cero. Registrar presiones de distribuidor, sensor y celda si existe medición aprobada.
3. Purgar 10 min con aire cero.
4. Acondicionar 20 min a 180 nmol/mol.
5. Volver a cero y esperar estabilidad.
6. Ejecutar tres ciclos independientes, cada uno con cero previo, seis niveles y cero posterior:
   - Ciclo 1 ascendente: `0, 20, 40, 70, 100, 140, 180, 0`.
   - Ciclo 2 descendente: `0, 180, 140, 100, 70, 40, 20, 0`.
   - Ciclo 3 pseudoaleatorio fijo: `0, 70, 180, 20, 140, 40, 100, 0`.
7. En cada cambio, purgar al menos tres constantes de tiempo del sistema, nunca menos de 3 min. Luego aplicar criterio de estabilidad común.
8. Después de estabilidad, registrar cinco medias consecutivas de 1 min de patrón y UUT. Resultado del punto = media de cinco valores; conservar los cinco.
9. Entre ciclos, mantener aire cero 10 min y confirmar cero estable. No ajustar UUT.
10. Si punto falla estabilidad después de 15 min, registrarlo como no estable; revisar montaje antes de repetir. No eliminarlo silenciosamente.

**Tiempo:** 55–70 min por ciclo; total 3–3.5 h.

## Tabla de registro

| fecha_hora | ciclo | orden | punto | nivel_nominal_nmol_mol | replica_1min | indicacion_ref_cruda_nmol_mol | valor_ref_corregido_X_nmol_mol | lectura_UUT_nmol_mol | diferencia_d_nmol_mol | T_celda_K | P_sensor_kPa | P_celda_kPa | flujo_ref_L_min | flujo_UUT_L_min | tiempo_estabilizacion_min | estable | incidencia |
|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

## Modelo de cálculo

Corrección de certificado:

\[
X_i=(I_{ref,i}-b_{ref})/m_{ref}.
\]

Por ciclo, OLS:

\[
y_i=b_0+m_0X_i+e_i,
\quad e_i=y_i-(b_0+m_0X_i).
\]

Desviación residual:

\[
s_{y/x}=\sqrt{\frac{\sum e_i^2}{N-2}}.
\]

Incertidumbre estándar de predicción de una **media de `r` lecturas** en nivel `x₀`:

\[
u_{pred}(x_0)=s_{y/x}\sqrt{\frac{1}{r}+\frac{1}{N}+\frac{(x_0-\bar X)^2}{\sum(X_i-\bar X)^2}}.
\]

Para una lectura individual, sustituir `1/r` por `1`. Añadir incertidumbre del patrón por separado si no está incluida en residual:

\[
u_{ver}(x_0)=\sqrt{u_{pred}^2(x_0)+m_0^2u_X^2(x_0)}.
\]

Componente relativo de pendiente, si pendiente se corrige o se modela alrededor de 1:

\[
u_r=\sqrt{s_m^2+u^2(m_{ref})+u^2_{m,PI}},
\]

depurando solapamientos. Con tres ciclos, `s_m` describe estabilidad corta, no precisión anual.

### Precisión intermedia: `s_pooled` y ANOVA

Con `D` días y `r` réplicas por día a nivel fijo:

\[
s_{pooled}=\sqrt{\frac{\sum_{d=1}^{D}(r_d-1)s_d^2}{\sum_{d=1}^{D}(r_d-1)}}.
\]

ANOVA de un factor:

\[
MS_{dentro}=\frac{SS_{dentro}}{N-D},\quad
MS_{dia}=\frac{SS_{dia}}{D-1},
\]

\[
s_{dia}=\sqrt{\max\left(0,\frac{MS_{dia}-MS_{dentro}}{r}\right)},\qquad
s_{PI}=\sqrt{MS_{dentro}+s_{dia}^2}.
\]

Si operadores están cruzados con días, usar ANOVA de dos factores o modelo de efectos aleatorios; no sumar una fila “operador” además de `s_PI` si ya está cubierto.

## Ejemplo numérico trabajado

Certificado: `m_ref=1.003`, `b_ref=-0.4 nmol/mol`. En ciclo 1, indicaciones de referencia crudas `[−0.40, 19.66, 39.72, 69.81, 99.90, 140.02, 180.14]` producen valores corregidos aproximados `X=[0,20,40,70,100,140,180]`.

Medias UUT: `[0.30,20.50,40.60,70.75,100.85,141.05,181.45]` nmol/mol. Ajuste calculado:

\[
y=0.25+1.0060X,
\]

con residuos aproximados `[0.05,0.13,0.11,0.08,0.00,-0.04,0.12]` nmol/mol y `s_y/x=0.10 nmol/mol`.

Para `x₀=180`, `N=7`, `r=5`, `X̄=78.57`, `Σ(X-X̄)²≈23885.7`:

\[
u_{pred}=0.10\sqrt{0.2+1/7+(101.43^2/23885.7)}
=0.10\sqrt{0.774}=0.088\ \mathrm{nmol/mol}.
\]

Si certificado da `U_X=0.5+0.01X=2.3 nmol/mol`, `k=2`, entonces `u_X=1.15 nmol/mol`:

\[
u_{ver}=\sqrt{0.088^2+(1.006\times1.15)^2}=1.16\ \mathrm{nmol/mol}.
\]

Tres pendientes: `1.0060, 1.0110, 1.0200`; media `1.0123`, `s_m=0.00709`, cumple límite `s_m<0.0075`. Interceptos `0.25, 0.55, 1.10`; `s_b=0.431 nmol/mol`, cumple `<1.00`.

Ejemplo de precisión intermedia a 100 nmol/mol, tres días, tres réplicas: medias diarias `100.4, 101.0, 99.9`; desviaciones dentro de día `0.20, 0.30, 0.25`. `MS_dentro=(0.04+0.09+0.0625)/3=0.0642`. Varianza de medias diarias `s²=0.303`; `MS_dia=r s²=0.909`. Entonces:

\[
s_{dia}=\sqrt{(0.909-0.0642)/3}=0.531,
\quad s_{PI}=\sqrt{0.0642+0.531^2}=0.588\ \mathrm{nmol/mol}.
\]

## Criterios de aceptación

- Para `X≤50`: `|d|≤1.5 nmol/mol`.
- Para `X>50`: `|100d/X|≤3.1 %`.
- Pendiente por ciclo: `0.97–1.03`.
- Intercepto: `−3 a +3 nmol/mol`.
- `s` de pendientes `<0.0075`; `s` de interceptos `<1.00 nmol/mol`.
- Residuos sin curvatura ni tendencia temporal. Punto no estable invalida decisión hasta investigar.
- La aceptación no incorpora automáticamente incertidumbre del patrón; regla de decisión real debe estar definida por sistema de calidad.

## Riesgos

O₃ alto, sobrepresión/depresión por bypass, adsorción en líneas, diferencias de tiempo entre ramas, cambio de escala automática y ajuste inadvertido. Ventear siempre a destructor/exterior.

---

# E14 — Recorrido documental de cadena metrológica

## Objetivo y componente ilustrado

Reconstruir trazabilidad desde patrón primario/SRP hasta valor corregido usado por UUT. Ilustra incertidumbre Tipo B, correcciones, cobertura, vigencia, dependencia y prevención de doble conteo.

## Instrumentos y montaje

No requiere generación de O₃. Usar certificado del patrón de transferencia, certificado superior citado, historial de verificaciones, manual UUT, procedimiento vigente, identificación de software y hoja de campo E2.

## Procedimiento

1. Reunir documentos sin editar: certificado actual, certificado anterior, alcance del laboratorio, procedimiento, registro de recepción, mantenimiento y verificación.
2. Identificar patrón por fabricante, modelo, serie y firmware.
3. Localizar mensurando, intervalo, matriz/base seca, ecuación de corrección, unidad, incertidumbre, `k`, cobertura, condiciones y fecha de vencimiento.
4. Seguir cada referencia citada hasta nivel superior disponible. Marcar eslabón no disponible como vacío, no como “trazable”.
5. Verificar que ecuación implementada en hoja o software coincide con certificado, incluido signo de intercepto.
6. Tomar una indicación real y recalcular valor corregido manualmente.
7. Construir matriz “componente–fuente–cobertura–duplicado”.
8. Comparar presión del sensor usada por software con presión de celda declarada por certificado/procedimiento. Si no son misma magnitud, abrir acción técnica.
9. Revisar vigencia al momento de medición, no solo al momento del curso.
10. Cerrar con estado: completo, condicionado o no demostrable.

**Tiempo:** 30–45 min.

## Tabla de registro

| eslabon | documento | emisor | codigo_version | patron_serie | mensurando | intervalo_nmol_mol | ecuacion_correccion | U_declarada | k | u_estandar | condiciones | fecha_emision | fecha_vigencia | referencia_superior | evidencia_disponible | cubre | no_cubre | posible_duplicado | estado | accion |
|---|---|---|---|---|---|---|---|---:|---:|---:|---|---|---|---|---|---|---|---|---|---|---|

## Modelo de cálculo

Para cada certificado:

\[
u=U/k.
\]

Para ecuación `X=(I-b)/m`, sensibilidades:

\[
\frac{\partial X}{\partial I}=1/m,\quad
\frac{\partial X}{\partial b}=-1/m,\quad
\frac{\partial X}{\partial m}=-(I-b)/m^2=-X/m.
\]

\[
u^2(X)=\left(\frac{u(I)}{m}\right)^2+\left(\frac{u(b)}{m}\right)^2+
\left(\frac{X u(m)}{m}\right)^2+\text{covarianzas}.
\]

No combinar `U` global del certificado con filas internas que ya la componen.

## Ejemplo numérico trabajado

Certificado declara `m=1.0030`, `b=−0.40 nmol/mol`, `U(X)=0.50+0.010X`, `k=2`, intervalo 0–200 nmol/mol. Indicación `I=99.90`:

\[
X=(99.90-(-0.40))/1.0030=100.00\ \mathrm{nmol/mol}.
\]

\[
U=0.50+0.010(100)=1.50,
\quad u=1.50/2=0.75\ \mathrm{nmol/mol}.
\]

Hoja existente usaba `X=(I+b)/m`, dando `(99.90−0.40)/1.003=99.20 nmol/mol`: error documental de `−0.80 nmol/mol`. Resultado E14: cadena **condicionada/no conforme documentalmente** hasta corregir fórmula, preservar datos y recalcular verificaciones afectadas. Si certificado global ya cubre regresión y repetibilidad, no se añaden `u(m)` y `u(b)` otra vez.

## Criterios de aceptación

- Identificación única y coincidencia física de serie.
- Certificado vigente para fecha de uso.
- Mensurando, unidad, intervalo y condiciones compatibles.
- Ecuación reproducida con error numérico <0.01 nmol/mol en caso de prueba.
- `U`, `k` y cobertura explícitos; referencias superiores localizables.
- Sin doble conteo en presupuesto.
- Diferencia sensor–celda resuelta o declarada como limitación.

## Riesgos

Riesgo principal: aplicar corrección incorrecta, certificado vencido o atribuir trazabilidad sin cadena demostrada. No hay exposición a O₃; no abrir instrumentos para localizar sensor de presión.

---

# E15 — Presupuesto híbrido del equipo propio

## Objetivo y componente ilustrado

Construir presupuesto evaluado con evidencia propia y documental:

\[
u(c)=\sqrt{u_0^2+(u_r c)^2}.
\]

Integra E1/E9 como término absoluto, E2 como término relativo y residual, E6 como transporte, E8 como deriva y certificado como patrón. Entrena depuración anti-doble-conteo.

## Instrumentos y montaje

Hojas E1, E2, E6, E8, E9, E11, certificados, manuales, calculadora/R y matriz de cobertura. Sin O₃ activo salvo verificación opcional.

## Procedimiento

1. Definir resultado: media de cinco lecturas de 1 min del UUT, aire seco, puerto de muestra, intervalo 0–180 nmol/mol.
2. Dibujar ramas: patrón/generación, aire cero, transporte, respuesta UUT, deriva, T/P, datos.
3. Para cada candidato, registrar mecanismo, evidencia, periodo, condiciones y cobertura.
4. Elegir `u₀`: ruido/repetibilidad de media operativa, residual de aire cero y deriva aditiva no cubierta.
5. Elegir `u_r`: pendiente/escala, incertidumbre relativa del patrón, transmisión proporcional y deriva de span no cubierta.
6. Separar términos locales no representables por forma de dos parámetros; si son pequeños y conservadores, asignarlos justificadamente a `u₀` o `u_r`; si no, usar modelo extendido.
7. Eliminar duplicados. Si `s_PI` ya cubre día, operador, ruido y ambiente, no conservar esas filas por separado.
8. Calcular a 0, 20, 100 y 180 nmol/mol.
9. Calcular contribución porcentual a varianza.
10. Validar orden de magnitud contra residuos E2, QC histórico o comparación independiente.
11. Informar `u_c`; si se requiere `U`, declarar `k` y fundamento. Para curso, `k=2` didáctico.

**Tiempo:** 90 min.

## Tabla de registro

| componente | mecanismo | evidencia | tipo_A_B | valor_original | PDF | divisor | u_estandar | forma_absoluta_relativa | coef_sensibilidad | contribucion_a_u0 | contribucion_a_ur | periodo_cubierto | condiciones_cubiertas | cubierto_por | duplicado_eliminado | fuente | calidad_evidencia | observacion |
|---|---|---|---|---:|---|---:|---:|---|---:|---:|---:|---|---|---|---|---|---|---|

## Modelo de cálculo

\[
u_0=\sqrt{\sum_j u_{0,j}^2},\qquad
u_r=\sqrt{\sum_k u_{r,k}^2},
\]

\[
u(c)=\sqrt{u_0^2+(u_rc)^2}.
\]

Si existe covarianza relevante, añadir términos cruzados; forma simple supone independencia entre grupo absoluto y relativo.

## Ejemplo numérico trabajado

Filas depuradas:

- Repetibilidad de media operativa y cero, E1/E9: `0.37 nmol/mol`, absoluta.
- Deriva de cero residual entre correcciones, E8: límite `0.60 nmol/mol`, rectangular: `0.60/√3=0.346 nmol/mol`, absoluta.
- Falta de ajuste residual E2: `0.25 nmol/mol`, absoluta.
- Patrón: `0.60 %` estándar: `u_r=0.0060`.
- Pendiente/precisión intermedia E2: `0.45 %`: `0.0045`.
- Transmisión de línea E6: `0.30 %`: `0.0030`.
- Deriva de span residual E8: límite `0.50 %`, rectangular: `0.005/√3=0.00289`.

Ruido separado y resolución se eliminan porque E1 los contiene. Día/operador se eliminan porque `s_PI` de pendiente los cubre.

\[
u_0=\sqrt{0.37^2+0.346^2+0.25^2}=0.565\ \mathrm{nmol/mol}.
\]

\[
u_r=\sqrt{0.0060^2+0.0045^2+0.0030^2+0.00289^2}=0.00860.
\]

A 20:

\[
u(20)=\sqrt{0.565^2+(0.00860\times20)^2}=0.591\ \mathrm{nmol/mol}.
\]

A 100:

\[
u(100)=\sqrt{0.565^2+0.860^2}=1.029\ \mathrm{nmol/mol}.
\]

A 180:

\[
u(180)=\sqrt{0.565^2+1.548^2}=1.648\ \mathrm{nmol/mol}.
\]

Con `k=2`, `U(100)=2.06 nmol/mol` y `U(180)=3.30 nmol/mol`. A 100, fracción de varianza proporcional = `0.860²/1.029²=69.9 %`; prioridad: patrón/pendiente.

## Criterios de aceptación

- Cada fila tiene mecanismo, fuente, PDF, unidad y cobertura.
- Ninguna cifra global se combina con componentes que ya contiene.
- Predicción del presupuesto es compatible con verificaciones independientes: al menos 95 % de diferencias históricas dentro de aproximadamente `±2u(c)` cuando condiciones son comparables, sin usar mismos datos como única validación.
- Presupuesto se usa solo dentro de intervalo y condiciones evaluados.
- Cerca de cero se informa incertidumbre absoluta; no porcentaje infinito.

## Riesgos

Riesgo metrológico de falsa precisión, doble conteo y usar tres ciclos como evidencia anual. Si se hace verificación adicional, aplicar venteo O₃ común.

---

# E6 — Transmisión de línea O₃

## Objetivo y componente ilustrado

Cuantificar pérdida o ganancia aparente causada por línea real, uniones y filtro. Ilustra corrección de transporte, incertidumbre de razón y efecto proporcional externo al analizador.

## Instrumentos y montaje

Patrón o UUT estable, calibrador O₃, válvula selectora inerte o reconexión controlada, línea A corta PFA `≤1 m` sin filtro y línea B real con longitud, codos y filtro usados en estación. Misma entrada/salida y flujo.

## Procedimiento

1. Calentar 2 h; fugas con aire cero.
2. Purgar ambas líneas 10 min con aire cero.
3. Acondicionar ambas 20 min a 150 nmol/mol.
4. Fijar `150 nmol/mol`; flujo igual al uso real, tolerancia ±5 %.
5. Alternar secuencia `A-B-A-B-A-B` para separar deriva.
6. Tras cada cambio, purgar al menos `3V/q` y mínimo 3 min; esperar criterio de estabilidad.
7. Registrar cinco medias de 1 min por configuración.
8. Repetir a cero para detectar contaminación/desorción.
9. Opcional: repetir a 50 nmol/mol para evaluar si factor es proporcional.

**Tiempo:** 60–75 min.

## Tabla de registro

| fecha_hora | bloque | configuracion_A_B | longitud_m | diametro_interno_mm | material | filtro_id | nivel_nominal_nmol_mol | replica_1min | lectura_nmol_mol | flujo_L_min | T_C | P_kPa | tiempo_purga_min | tiempo_estabilizacion_min | incidencia |
|---|---:|---|---:|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|

## Modelo de cálculo

Emparejar cada B con media de A anterior y posterior interpolada:

\[
A_j^*=(A_{antes}+A_{despues})/2,
\quad T_j=B_j/A_j^*.
\]

\[
\bar T=\frac{1}{p}\sum T_j,
\quad L=1-\bar T,
\quad C_{linea}=1/\bar T.
\]

\[
u(\bar T)=s(T)/\sqrt p
\]

si pares son independientes; añadir repetibilidad de lecturas y patrón común solo si no se cancela. Con corrección `c_corr=c_obs/T`:

\[
u_r^2(c_{corr})\supset [u(T)/T]^2.
\]

## Ejemplo numérico trabajado

Medias A: `150.2, 150.0, 149.9, 149.7` nmol/mol. Medias B intermedias: `148.8, 148.5, 148.2`.

- B1: `A*=150.1`, `T1=148.8/150.1=0.99134`.
- B2: `A*=149.95`, `T2=148.5/149.95=0.99033`.
- B3: `A*=149.80`, `T3=148.2/149.80=0.98932`.

\[
\bar T=0.99033,
\quad L=0.00967=0.967\%,
\quad C_{linea}=1.00977.
\]

`s(T)=0.00101`; `u(T̄)=0.00101/√3=0.00058`. Para lectura observada `120.0`:

\[
c_{corr}=120/0.99033=121.17\ \mathrm{nmol/mol}.
\]

Contribución por transmisión:

\[
u=121.17(0.00058/0.99033)=0.071\ \mathrm{nmol/mol}.
\]

## Criterios de aceptación

- Objetivo operativo: `T≥0.99` y pérdida ≤1.0 %; si procedimiento local exige otro límite, usarlo predefinido.
- Diferencia entre `T` de 50 y 150 nmol/mol ≤0.5 % relativo.
- Sin aumento de cero >0.5 nmol/mol tras exposición.
- Si pérdida es estable pero significativa, corregir y presupuestar; si variable o dependiente de tiempo, reemplazar línea/filtro.

## Riesgos

Exposición al desconectar líneas, contaminación de filtro, bypass bloqueado y memoria de O₃. Antes de reconectar, bajar a aire cero; mantener venteo al destructor.

---

# E9 — Calidad de aire cero

## Objetivo y componente ilustrado

Comparar tres fuentes de aire cero y estimar residual, contaminación o efecto de matriz. Ilustra sesgo de cero, selectividad y componente absoluto.

## Instrumentos y montaje

Tres fuentes: A generador usado en calibración, B cilindro o generador independiente, C aire cero alternativo certificado/depurado. Válvula selectora inerte, UUT y, si disponible, fotómetro patrón. Mismos flujo y línea posterior a selector.

## Procedimiento

1. Calentar 2 h; comprobar fugas.
2. Purgar colector común 10 min con fuente A.
3. Ejecutar diseño balanceado `A-B-C-C-B-A`, reduciendo deriva temporal.
4. En cada cambio, purgar 5 min o tres volúmenes; esperar estabilidad 5 min.
5. Registrar diez medias de 1 min por bloque.
6. Después de C, exponer 10 min a 150 nmol/mol y volver a cada fuente para detectar memoria; registrar máximo transitorio y tiempo de recuperación.
7. Si patrón posee sensibilidad insuficiente cerca de cero, usar diferencias pareadas en UUT y declarar limitación.

**Tiempo:** 60–90 min; versión mínima A-B-C con 5 medias: 45 min.

## Tabla de registro

| fecha_hora | bloque | fuente_cero | lote_serie | tratamiento | replica_1min | lectura_UUT_nmol_mol | lectura_patron_nmol_mol | diferencia_vs_A_nmol_mol | flujo_L_min | T_C | P_kPa | tiempo_purga_min | estable | max_transitorio_nmol_mol | tiempo_recuperacion_min | incidencia |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|

## Modelo de cálculo

Para fuente `j`:

\[
\bar z_j,\quad s_j,\quad d_j=\bar z_j-\bar z_A.
\]

Con bloques pareados:

\[
u(d_j)=s(d_{j,b})/\sqrt B.
\]

Si fuente elegida tiene corrección `z_corr=−z̄_j`, residual estándar:

\[
u_{aire0}=\sqrt{u^2(\bar z_j)+u^2_{estabilidad}+u^2_{referencia,cero}}.
\]

No sumar nuevamente ruido UUT si `u( z̄_j )` ya proviene de misma serie y presupuesto usa resultado de ese promedio.

## Ejemplo numérico trabajado

Medias de bloques:

- A: `0.12` y `0.18`; media `0.15 nmol/mol`.
- B: `0.48` y `0.54`; media `0.51`; diferencias pareadas `0.36, 0.36`.
- C: `−0.05` y `0.01`; media `−0.02`; diferencias `−0.17, −0.17`.

Suponga `s` dentro de bloque `0.20 nmol/mol`, diez medias por bloque: `u(media)=0.20/√10=0.063`. Estabilidad entre dos bloques A: semidiferencia `0.03`, tratada estándar conservadora. Referencia cerca de cero `u=0.10`.

\[
u_{aire0,A}=\sqrt{0.063^2+0.03^2+0.10^2}=0.122\ \mathrm{nmol/mol}.
\]

B presenta sesgo frente a A de `+0.36 nmol/mol`; sigue dentro de límite 0.5, pero requiere investigar depurador. Si máximo transitorio después de O₃ es `1.4 nmol/mol` y tarda 7 min, criterio de memoria falla.

## Criterios de aceptación

- `|z̄_j|≤0.5 nmol/mol` respecto de referencia disponible.
- Diferencia entre fuentes `≤0.5 nmol/mol`.
- `s₁min≤0.5 nmol/mol`.
- Tras O₃, transitorio ≤1.0 nmol/mol y recuperación a ±0.5 nmol/mol en ≤5 min.
- Fuente con olor, humedad, partículas o resultado inestable se rechaza aunque media cumpla.

## Riesgos

Presión de cilindro si se usa fuente envasada, contaminación cruzada y desorción de O₃. Regulador compatible y asegurado. Ventear O₃ residual a destructor.

---

# E11 — Tiempo de respuesta y criterio de estabilización

## Objetivo y componente ilustrado

Medir `t10`, `t90`, tiempo de subida/bajada y validar regla de espera antes de registrar. Ilustra efecto dinámico y sesgo por estabilización insuficiente.

## Instrumentos y montaje

Calibrador capaz de cambio rápido cero/span, distribuidor de bajo volumen, UUT, adquisición a 1 s y patrón opcional en paralelo. Línea representativa de uso.

## Procedimiento

1. Calentar 2 h; fugas y acondicionamiento 20 min a 150 nmol/mol.
2. Mantener cero hasta estabilidad 10 min.
3. Registrar 2 min de línea base a 1 s.
4. Cambiar rápidamente de 0 a 150 nmol/mol sin variar flujo total; marcar tiempo de válvula.
5. Registrar hasta estabilidad y mínimo 15 min.
6. Mantener 5 min estable.
7. Cambiar de 150 a 0; registrar mínimo 15 min.
8. Repetir tres ciclos.
9. Calcular `t10`, `t90` por interpolación y primer instante en que criterio `<1 nmol/mol en 5 min` permanece cumplido.
10. Comparar con espera usada en E2.

**Tiempo:** 45–60 min; versión mínima un ciclo: 30 min.

## Tabla de registro

| fecha_hora | ciclo | direccion_subida_bajada | segundo | estado_valvula | lectura_nmol_mol | base_inicial_nmol_mol | meseta_final_nmol_mol | fraccion_respuesta | T_C | P_kPa | flujo_L_min | t10_s | t90_s | estabilidad_5min_cumple | incidencia |
|---|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|

## Modelo de cálculo

Para subida:

\[
f(t)=\frac{y(t)-y_0}{y_\infty-y_0}.
\]

`t10` y `t90` son primeros cruces interpolados de `f=0.10` y `0.90`; tiempo de respuesta:

\[
t_r=t_{90}-t_{10}.
\]

Para bajada usar fracción restante `(y(t)-y∞)/(y0-y∞)`. Sesgo por registrar en tiempo `t`:

\[
b_{din}(t)=y(t)-y_\infty.
\]

Si respuesta de primer orden:

\[
y(t)=y_\infty-(y_\infty-y_0)e^{-t/\tau},\qquad t_{90}\approx2.303\tau.
\]

## Ejemplo numérico trabajado

Base `y0=0.2`, meseta `y∞=149.8 nmol/mol`. Umbrales:

\[
y_{10}=0.2+0.1(149.6)=15.16,
\quad y_{90}=0.2+0.9(149.6)=134.84.
\]

Cruces interpolados: `t10=22 s`, `t90=178 s`; `tr=156 s`. Entonces `τ≈178/2.303=77.3 s` si origen dinámico se aproxima a cero después del retardo.

A 180 s lectura era `135.2`; sesgo frente a meseta `−14.6 nmol/mol`: registrar a 3 min sería inválido. Criterio de estabilidad se alcanza a 410 s = 6.8 min. Tres tiempos de estabilización: `6.8, 7.2, 6.6 min`; usar espera mínima 8 min antes de evaluar estabilidad, no promedio fijo de 3 min.

## Criterios de aceptación

- `t90` según especificación del fabricante o procedimiento; si no existe, objetivo didáctico `≤180 s`.
- Diferencia subida/bajada de `t90` ≤20 %.
- Criterio de estabilidad cumplido en ≤10 min.
- Sobreimpulso ≤2 % de nivel.
- E2 debe usar espera no menor que máximo observado más verificación de estabilidad.

## Riesgos

Cambio de válvula puede alterar flujo/presión y simular respuesta. O₃ a 150 nmol/mol: venteo continuo a destructor/exterior; purgar con aire cero 10 min al terminar.

---

# E8 — Deriva de cero y span 24 h / 7 d, pasivo precurso

## Objetivo y componente ilustrado

Cuantificar cambio de cero y sensibilidad a 24 h y 7 d sin ajustes intermedios. Ilustra deriva temporal, precisión intermedia y diferencia entre límite documental y evidencia propia.

## Diseño y preparación

Iniciar al menos 7 días antes. Usar mismo patrón, fuente de aire cero, línea, flujo, escala y procedimiento. Programar verificaciones en `t=0`, `24 h` y `7 d`; ideal diario. En cada fecha realizar cero y span de `150 nmol/mol`, dos ciclos, cinco medias de 1 min por punto. Alternar operador A/B si objetivo incluye operador; conservar operador único si se quiere aislar equipo.

## Procedimiento

1. Día 0: calentamiento 2 h, fugas, 10 min aire cero, 20 min acondicionamiento O₃.
2. Registrar estado encontrado del cero y span. No ajustar.
3. Mantener UUT en operación normal entre fechas. Registrar apagados, mantenimiento, ambiente y cambios de consumibles.
4. A 24 h, repetir misma secuencia y horario ±1 h.
5. Días 2–6, si posible, repetir una vez al día.
6. Día 7, repetir dos ciclos completos.
7. Si instrumento falla criterio operativo y procedimiento exige ajuste, guardar datos previos, marcar ruptura de serie y continuar como nueva fase.
8. Purgar con aire cero 10 min al terminar cada exposición.

## Tabla de registro

| fecha_hora | tiempo_desde_t0_h | dia | operador | ciclo | punto_cero_span | valor_ref_corregido_nmol_mol | lectura_UUT_nmol_mol | diferencia_nmol_mol | pendiente_span_relativa | T_C | P_kPa | flujo_L_min | horas_operacion | ajuste_desde_t0 | mantenimiento | estable | incidencia |
|---|---:|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|---|

## Modelo de cálculo

Deriva de cero:

\[
D_0(t)=z(t)-z(0).
\]

Deriva de span absoluta y relativa, corrigiendo cero:

\[
S(t)=y_{span}(t)-z(t),
\quad D_S(t)=S(t)-S(0),
\quad D_{S,r}(t)=\frac{S(t)}{S(0)}-1.
\]

Si deriva solo se conoce entre observaciones y se corrige en intervalos, modelo rectangular con semiancho igual al máximo cambio no corregido:

\[
u_{deriva}=a/\sqrt3.
\]

Para datos diarios, regresión temporal:

\[
d_t=\beta_0+\beta_1t+e_t.
\]

Incertidumbre de predicción al tiempo de uso combina incertidumbre de pendiente temporal y residual. Precisión intermedia se estima mediante `s_pooled`/ANOVA como en E2, usando días como factor. No sumar deriva como fila aparte si `s_PI` ya cubre mismo periodo y política de corrección.

## Ejemplo numérico trabajado

Medias de cero: día 0 `0.20`, 24 h `0.75`, 7 d `1.65 nmol/mol`.

\[
D_0(24h)=0.55,
\quad D_0(7d)=1.45\ \mathrm{nmol/mol}.
\]

Span bruto a 150: `150.40`, `150.60`, `150.55`. Span corregido por cero:

- Día 0: `150.40−0.20=150.20`.
- 24 h: `150.60−0.75=149.85`.
- 7 d: `150.55−1.65=148.90`.

\[
D_{S,r}(24h)=149.85/150.20-1=-0.00233=-0.233\%,
\]

\[
D_{S,r}(7d)=148.90/150.20-1=-0.00866=-0.866\%.
\]

Si corrección de cero se hace diaria y máximo cambio entre correcciones es `a=0.55`:

\[
u_{deriva,0}=0.55/\sqrt3=0.318\ \mathrm{nmol/mol}.
\]

Si span se verifica semanalmente y no se corrige entre medias, `a_r=0.00866`:

\[
u_{deriva,span,r}=0.00866/\sqrt3=0.00500.
\]

A 150 nmol/mol contribuye `0.750 nmol/mol`. No usar a la vez estas filas y `s_PI` semanal si mismos datos y efectos ya están contenidos.

## Criterios de aceptación

Basados en Thermo 49i como referencia didáctica, salvo especificación propia más aplicable:

- Deriva cero `<1 nmol/mol/24 h`.
- Deriva cero `<2 nmol/mol/7 d`.
- Deriva span: comparar con especificación real en su periodo; no convertir `<1 %/mes` en límite diario. Objetivo interno propuesto para 7 d: `|D_S,r|≤1 %`.
- Serie sin intervención no documentada.
- Si hay cambio brusco, investigar antes de modelar como deriva aleatoria.

## Riesgos

Operación desatendida: verificar alarmas, flujo, extracción, destructor y políticas locales. No dejar generación continua de O₃ si equipo no está aprobado para operación desatendida. Preferir verificaciones programadas con O₃ solo durante cada punto. Purga final con aire cero y venteo seguro.

---

# 2. Secuencia recomendada de jornada y productos

## Precurso, desde día −7

- Iniciar E8.
- Reunir certificados para E14.
- Confirmar compatibilidad de líneas, destructor y extracción.

## Día de laboratorio

1. Checklist, seguridad y calentamiento: 120 min pasivos.
2. E14 recorrido documental: 30–45 min.
3. E1 cero: 55–70 min.
4. E9 aire cero: 45–90 min.
5. Acondicionamiento O₃: 20 min.
6. E11 respuesta: 30–60 min.
7. E2 multipunto: 180–210 min.
8. E6 transmisión: 60–75 min.
9. E15 presupuesto híbrido: 90 min, con resultados disponibles y E8 precurso.

## Entregable mínimo por equipo

1. Hojas crudas completas y sin sobrescritura.
2. Gráficos diagnósticos opcionales: serie temporal, ACF, residuos contra nivel/orden y deriva contra tiempo.
3. Cálculos de `n_ef`, regresión, `u_pred`, transmisión, aire cero, `t10/t90`, deriva y presupuesto híbrido.
4. Matriz de cobertura y doble conteo.
5. Declaración final:

> Para el mensurando y condiciones definidos, el equipo presenta una incertidumbre estándar modelada como `u(c)=√(u₀²+(uᵣc)²)` nmol/mol, con `u₀=[valor] nmol/mol` y `uᵣ=[valor]`. Resultado válido entre `[mínimo, máximo] nmol/mol`, con promedio de cinco lecturas de 1 min, líneas y aire cero evaluados, y política de corrección indicada. Incertidumbre expandida `U=ku(c)` solo cuando se declare `k`, cobertura y regla de decisión.

# 3. Cierre técnico

Estos protocolos convierten especificaciones documentales en evidencia propia sin confundir verificación con ajuste. E1 y E9 sustentan término absoluto; E2 sustenta relación, residual y estabilidad; E6 cuantifica transporte; E11 fija espera válida; E8 caracteriza escala temporal; E14 demuestra trazabilidad; E15 integra todo sin doble conteo. Toda conclusión queda limitada por intervalo, días, operadores, montaje, referencia y condiciones realmente observadas.
