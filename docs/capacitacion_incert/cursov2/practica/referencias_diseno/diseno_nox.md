# Diseño de experimentos metrológicos NO/NO₂/NOₓ por quimioluminiscencia

## 0. Alcance, convenciones y preparación común

Documento para jornada práctica con analizador de NOₓ por quimioluminiscencia, convertidor NO₂→NO, calibrador-diluidor con generador de O₃/GPT, cilindro certificado de NO, aire cero y patrones de flujo. Todas las fracciones molares gaseosas se expresan en **nmol/mol**. NO₂ es magnitud calculada, no lectura directa.

Modelo base, cuando firmware no corrige eficiencia:

\[
y=c_{NO_2}=\frac{X-N}{\eta},
\]

donde \(X=c_{NO_x}\), \(N=c_{NO}\) y \(\eta\) es eficiencia del convertidor. Antes de aplicar modelo debe verificarse arquitectura real, sincronización de canales y estado de corrección automática.

### 0.1 Lista común de instrumentos

- Analizador NO/NOₓ por quimioluminiscencia, con registro de NO, NOₓ, NO₂ mostrado, temperatura de convertidor, presión y caudal de muestra.
- Calibrador-diluidor con GPT y generador de O₃.
- Cilindro certificado de NO en N₂, regulador compatible, válvula antirretorno y sujeción física.
- Generador de aire cero verificado.
- Patrón de flujo trazable para verificar caudales de NO, dilución y salida.
- Líneas inertes: corta 2 m, DI 4 mm; larga 8 m, DI 6 mm; sistema calefactado para 35 °C.
- Termómetro y barómetro calibrados o verificados.
- Cronómetro y sistema de adquisición con resolución mínima de 1 s.
- Detector ambiental de NO/NO₂ cuando esté disponible.
- Conducto de extracción para bypass y destructor catalítico o térmico de O₃.

### 0.2 Comprobaciones previas obligatorias

1. Confirmar identificación, rango y vigencia del certificado del cilindro; registrar concentración de NO, impureza de NO₂, incertidumbre y fecha.
2. Sujetar cilindro verticalmente. Inspeccionar regulador y conexiones. No usar aceite ni grasa.
3. Realizar prueba de fugas con gas inerte o presión controlada antes de admitir NO. No buscar fugas con llama.
4. Conectar todos los venteos y bypass a extracción. Nunca descargar NO, NO₂ u O₃ al recinto.
5. Encender analizador y calibrador según manual. Esperar calentamiento mínimo recomendado por fabricante; si no existe dato documentado, usar 60 min y exigir estabilidad de cero y variables internas.
6. Verificar aire cero: NO, NOₓ y O₃ por debajo de límite definido por laboratorio; para esta práctica, lectura absoluta <1 nmol/mol y deriva <1 nmol/mol durante 5 min.
7. Verificar caudal total suficiente para demanda del analizador más bypass continuo de 0.3 a 1.0 L/min. Falta de bypass puede causar presión no representativa o entrada de aire ambiente.
8. Acondicionar líneas con gas de ensayo al menos tres volúmenes internos y hasta cumplir cambio <1 nmol/mol en 5 min.
9. Registrar datos crudos. Nunca sobrescribirlos con valores corregidos.
10. Abortar ante olor, alarma, pérdida de extracción, fuga, sobrepresión, inestabilidad térmica o caudal insuficiente.

---

# E3 — Covarianza medida entre canales NO y NOₓ

## Objetivo

Estimar covarianza y correlación entre indicaciones simultáneas de NO y NOₓ bajo concentración estable; cuantificar incertidumbre de diferencia \(D=X-N\) usando independencia, covarianza medida y desviación estándar directa de diferencias.

## Instrumentos

Instrumentos comunes; cilindro de NO; diluidor; aire cero; adquisición de datos de ambos canales con sello temporal común.

## Procedimiento paso a paso

1. **Preparación, 10 min.** Completar comprobaciones comunes. Desactivar corrección de eficiencia solo si manual permite hacerlo y registrar estado. Seleccionar promedio de 60 s para resultado principal; conservar datos de 1 s si están disponibles.
2. **Cero, 10 min.** Introducir aire cero durante 5 min de acondicionamiento y registrar 5 pares de 1 min. Confirmar estabilidad.
3. **Generación, 5 min.** Generar NO de \(200\pm10\) nmol/mol sin O₃. Usar caudales verificados. Mantener caudal y presión constantes.
4. **Estabilización, 10 min.** Acondicionar hasta que medias móviles de NO y NOₓ cambien <1 nmol/mol en 5 min.
5. **Serie principal, 60 min.** Registrar al menos 60 pares sincronizados \((N_i,X_i)\), uno por minuto. No eliminar puntos por apariencia. Marcar eventos operativos.
6. **Chequeo de estacionariedad, 10 min.** Graficar o revisar primera y segunda mitad; calcular pendientes temporales. Si deriva excede 1 nmol/mol/h o existe salto operativo, repetir después de corregir causa.
7. **Cierre, 5 min.** Volver a aire cero, purgar línea de NO y cerrar cilindro siguiendo secuencia del laboratorio.
8. **Análisis, 20 min.** Calcular medias, desviaciones, covarianza, correlación, diferencias y autocorrelación de primer orden. Si datos de 1 min tienen autocorrelación, no usar \(n\) nominal para incertidumbre de media.

Duración estimada: 130 min incluyendo análisis; adquisición útil: 60 min.

## Tabla de registro

| campo | unidad/forma |
|---|---|
| fecha, operador, analizador, firmware | texto |
| corrección de eficiencia | activada/desactivada/no configurable |
| concentración certificada de NO | µmol/mol |
| caudales NO, dilución y total | mL/min o L/min |
| temperatura, presión | °C, kPa |
| índice y hora | entero, ISO 8601 |
| \(N_i\), \(X_i\) | nmol/mol |
| \(D_i=X_i-N_i\) | nmol/mol |
| temperatura convertidor, presión y caudal de muestra | unidades del equipo |
| bandera de estabilidad/evento | texto |

## Modelo de cálculo

Para \(n\) pares:

\[
\bar N=\frac1n\sum N_i,\quad \bar X=\frac1n\sum X_i,
\]

\[
s_N^2=\frac{\sum(N_i-\bar N)^2}{n-1},\quad
s_X^2=\frac{\sum(X_i-\bar X)^2}{n-1},
\]

\[
s_{XN}=\operatorname{cov}(X,N)=
\frac{\sum(X_i-\bar X)(N_i-\bar N)}{n-1},
\quad
r=\frac{s_{XN}}{s_Xs_N}.
\]

Varianza de una diferencia individual:

\[
s_D^2=s_X^2+s_N^2-2s_{XN}.
\]

Debe coincidir, salvo redondeo, con varianza calculada directamente sobre \(D_i=X_i-N_i\). Para media de diferencias independientes, \(u(\bar D)=s_D/\sqrt n\). Con autocorrelación de primer orden aproximada \(r_1\):

\[
n_{ef}\approx n\frac{1-r_1}{1+r_1},\qquad
u(\bar D)=\frac{s_D}{\sqrt{n_{ef}}}.
\]

Usar bloque, análisis espectral o método documentado si estructura temporal no es AR(1).

## Ejemplo numérico trabajado

Serie de 60 pares a NO estable produce:

- \(\bar X=200.42\) nmol/mol;
- \(\bar N=199.98\) nmol/mol;
- \(s_X=1.20\) nmol/mol;
- \(s_N=1.00\) nmol/mol;
- \(r=0.70\).

Covarianza:

\[
s_{XN}=0.70(1.20)(1.00)=0.840\ (\mathrm{nmol/mol})^2.
\]

Si se supone independencia:

\[
s_{D,ind}=\sqrt{1.20^2+1.00^2}=1.562\ \mathrm{nmol/mol}.
\]

Con covarianza medida:

\[
s_D=\sqrt{1.20^2+1.00^2-2(0.840)}
=\sqrt{0.760}=0.872\ \mathrm{nmol/mol}.
\]

Cálculo directo de 60 diferencias debe dar aproximadamente 0.872 nmol/mol. Si \(r_1=0.25\):

\[
n_{ef}=60\frac{0.75}{1.25}=36,
\qquad u(\bar D)=0.872/\sqrt{36}=0.145\ \mathrm{nmol/mol}.
\]

Usar \(60\) sin corregir daría 0.113 nmol/mol y subestimaría incertidumbre de media.

## Criterios de aceptación

- Al menos 60 pares válidos y sincronizados.
- Identidad \(s_D^2\approx s_X^2+s_N^2-2s_{XN}\) dentro de 1 % por cálculo sin redondear.
- Sin salto, alarma ni deriva >1 nmol/mol/h durante serie.
- Covarianza debe medirse, no imponerse. Resultado negativo, cero o positivo puede ser válido si está respaldado por datos.
- Si sincronización entre canales no puede demostrarse, ensayo no sirve para presupuesto diferencial dinámico.

## Seguridad

Cilindro de NO siempre sujeto, regulador compatible y prueba de fugas previa. Mantener bypass en extracción. Aunque E3 no genera O₃, confirmar generador O₃ desactivado. Al terminar, cerrar válvula del cilindro, consumir presión atrapada conforme procedimiento y purgar con aire cero.

---

# E4 — GPT y eficiencia del convertidor con escalera rediseñada

## Objetivo

Generar NO₂ por titulación en fase gaseosa, estimar eficiencia \(\eta\) del convertidor en cinco niveles, evaluar linealidad y repetibilidad entre dos días, y eliminar defecto de titulación profunda del diseño anterior.

## Fundamento del rediseño D4

Diseño anterior usaba NO inicial cercano a 160 nmol/mol y nivel N150 cercano a 150 nmol/mol, dejando aproximadamente 10 nmol/mol de NO residual: solo 6.25 % del NO inicial. Ese margen es demasiado pequeño; errores de O₃, mezcla, impureza y caudal dominan resultado.

Nueva condición propuesta:

- NO antes de GPT: \(N_0=450\) nmol/mol;
- NO₂ GPT nominal: 0, 40, 80, 120 y 160 nmol/mol;
- NO residual esperado: 450, 410, 370, 330 y 290 nmol/mol.

En nivel máximo:

\[
\frac{N_{res}}{N_0}=\frac{450-160}{450}=0.644=64.4\%,
\]

\[
\frac{N_{res}}{NO_{2,GPT}}=\frac{290}{160}=1.81.
\]

Queda exceso holgado de NO, y 160 nmol/mol cubre 80 % de rango didáctico 0–200 nmol/mol. Para cilindro de 50 µmol/mol y flujo total de 5.000 L/min:

\[
q_{NO}=\frac{450}{50\,000}(5000)=45.0\ \mathrm{mL/min},
\]

con \(q_{dil}=4955.0\) mL/min antes de ajustes GPT. Si concentración certificada difiere, recalcular caudal; no copiar 45.0 mL/min.

## Instrumentos

Instrumentos comunes; calibrador GPT con cámara de mezcla; analizador de O₃ o fotómetro de transferencia para asignar O₃ cuando arquitectura lo permita; patrón de flujo; cilindro NO certificado.

## Procedimiento paso a paso

### Sesión 1, aproximadamente 100 min

1. **Montaje y seguridad, 15 min.** Completar comprobaciones comunes. Confirmar venteo, prueba de fugas y caudal total.
2. **Verificación de caudales, 10 min.** Medir caudal de NO y dilución en puntos de trabajo. Registrar correcciones de referencia.
3. **Cero, 10 min.** Aire cero: 5 min de acondicionamiento y 5 min de registro.
4. **NO base, 15 min.** Generar 450 nmol/mol de NO sin O₃; acondicionar 10 min o hasta <1 nmol/mol en 5 min; registrar cinco promedios de 1 min.
5. **Escalera ascendente, 40 min.** Aplicar niveles GPT 40, 80, 120 y 160 nmol/mol. En cada nivel: 5 min de acondicionamiento mínimo y 5 promedios de 1 min. Exigir NO residual >250 nmol/mol.
6. **Retorno, 10 min.** Repetir nivel 80 nmol/mol y luego cero para detectar memoria o deriva.
7. **Cierre, 5 min.** Desactivar O₃, mantener NO/aire cero hasta eliminar O₃, cerrar NO y purgar.

### Sesión 2 (día distinto), aproximadamente 100 min

1. Repetir preparación y cero.
2. Repetir NO base.
3. Aplicar orden descendente 160, 120, 80, 40 nmol/mol para separar deriva de efecto de orden.
4. Repetir nivel 80 y cero final.
5. Analizar pendientes por día y pendiente combinada con efecto de día.

## Tabla de registro

| campo | unidad/forma |
|---|---|
| día, ciclo, orden, hora | texto/entero |
| concentración NO del certificado y \(U,k\) | µmol/mol |
| impureza NO₂ del cilindro y \(U,k\) | nmol/mol en cilindro |
| \(q_{NO}\), \(q_{dil}\), caudal total | mL/min |
| NO generado antes de GPT | nmol/mol |
| O₃ asignado/NO₂ GPT | nmol/mol |
| NO residual | nmol/mol |
| NO, NOₓ, diferencia NOₓ−NO | nmol/mol |
| temperatura, presión, residencia GPT | °C, kPa, s |
| temperatura convertidor | °C |
| estabilidad, alarma, observación | texto |

## Modelo de cálculo

NO diluido:

\[
N_0=c_{cil,NO}\frac{q_{NO}}{q_{NO}+q_{dil}}.
\]

Corrección por impureza de NO₂ del cilindro:

\[
I_{mezcla}=I_{cil}\frac{q_{NO}}{q_T}.
\]

Bajo GPT estequiométrica y O₃ limitante:

\[
G_i=c_{NO_2,GPT,i}=c_{O_3,i},\qquad
N_{res,i}=N_0-G_i.
\]

Respuesta diferencial observada:

\[
R_i=X_i-N_i.
\]

Ajuste recomendado:

\[
R_i=b+\eta G_i+\varepsilon_i.
\]

Pendiente \(\eta\) estima eficiencia si asignación GPT, sincronización y selectividad son adecuadas. Incertidumbre debe incluir certificado de NO/O₃, caudales, impureza, repetibilidad, ajuste y condiciones GPT. No interpretar selectividad frente a NOy desde este ensayo.

Si se fuerza paso por origen, debe justificarse después de corregir cero e impureza. Preferir intercepto libre para diagnóstico.

## Ejemplo numérico trabajado completo

Cilindro: \(c_{cil}=50.000\) µmol/mol = 50 000 nmol/mol. Caudales: \(q_{NO}=45.00\) mL/min y \(q_T=5000.0\) mL/min.

\[
N_0=50\,000\frac{45}{5000}=450.0\ \mathrm{nmol/mol}.
\]

Para nivel GPT 160:

\[
N_{res}=450.0-160.0=290.0\ \mathrm{nmol/mol}.
\]

Datos medios corregidos de un día:

| \(G_i\) | \(N_i\) | \(X_i\) | \(R_i=X_i-N_i\) |
|---:|---:|---:|---:|
| 0 | 449.9 | 450.3 | 0.4 |
| 40 | 409.8 | 449.0 | 39.2 |
| 80 | 369.9 | 447.9 | 78.0 |
| 120 | 329.8 | 446.6 | 116.8 |
| 160 | 289.9 | 445.5 | 155.6 |

Estos valores siguen aproximadamente:

\[
R=0.40+0.970G.
\]

Por tanto \(\hat\eta=0.970\). Si error estándar de pendiente es 0.0030 y componente estándar por asignación GPT equivale a 0.0040 en eficiencia:

\[
u(\eta)=\sqrt{0.0030^2+0.0040^2}=0.0050.
\]

\[
U(\eta)=2u(\eta)=0.010,
\]

o \(\eta=0.970\pm0.010\), \(k=2\). Si la sesión 2 entrega 0.966, diferencia entre días es 0.004, menor que \(\sqrt{0.005^2+0.005^2}=0.0071\), por lo que no se detecta cambio significativo al nivel de una incertidumbre estándar combinada.

## Criterios de aceptación

- NO residual >250 nmol/mol y >20 % de NO inicial en todos los niveles; diseño propuesto deja 64.4 % en máximo.
- Caudal total mayor que demanda del analizador y bypass visible.
- Estabilidad <1 nmol/mol en 5 min antes de registrar.
- Pendiente dentro del criterio aprobado por método, fabricante y sistema de calidad aplicable. Para práctica, usar 0.95–1.05 como ventana didáctica, no como límite normativo universal.
- Intercepto absoluto ≤2 nmol/mol después de cero e impureza; mayor valor exige investigar blanco, impureza, sincronización o NOy.
- \(R^2\ge0.995\) y residuos sin curvatura visible para aceptación didáctica.
- Diferencia de pendientes entre días compatible con sus incertidumbres; si no, incluir precisión intermedia o declarar inestabilidad.
- Ensayo mide eficiencia, no selectividad del convertidor.

## Seguridad

NO es tóxico y se oxida a NO₂. Cilindro sujeto, regulador correcto, extracción activa y prueba de fugas obligatoria. O₃ es oxidante y tóxico: bypass debe ir a destructor y extracción. Desactivar O₃ antes de cerrar NO; purgar cámara y líneas con aire cero. No abrir sistema ni desconectar línea mientras exista O₃ o presión.

---

# E5 — Verificación de corrección de eficiencia en firmware

## Objetivo

Determinar si firmware aplica corrección automática por \(\eta\), verificar valor configurado y evitar doble corrección en cálculo externo.

## Instrumentos

Mismos de E4; acceso autorizado a configuración o menú de diagnóstico; copia del manual y registro de configuración.

## Procedimiento paso a paso

1. **Revisión documental, 5 min.** Identificar definición del canal NO₂ mostrado, parámetro de eficiencia y posibilidad de activar/desactivar corrección.
2. **Registrar estado encontrado, 5 min.** Fotografiar o transcribir firmware, valor \(\eta_f\), modo y unidades. No cambiar configuración sin autorización.
3. **Cero y NO base, 5 min.** Confirmar cero y NO base estables.
4. **Nivel GPT, 10 min.** Aplicar \(G=100\) nmol/mol. Estabilizar 5 min y registrar cinco medias de 1 min de NO, NOₓ y NO₂ mostrado.
5. **Prueba de identidad, 5 min.** Calcular \(D=X-N\), \(D/\eta_f\) y comparar ambos con NO₂ mostrado.
6. **Cambio controlado, 10 min.** Solo si autorizado, guardar configuración y cambiar temporalmente \(\eta_f\) de 0.970 a 0.950, sin cambiar gas. Esperar 3 min y registrar cinco medias. Restaurar valor original inmediatamente.
7. **Confirmación, 5 min.** Repetir lectura con valor restaurado y verificar retorno.
8. **Documentación, 5 min.** Declarar modelo correcto para exportación cruda y para pantalla.

Duración: 50 min.

## Tabla de registro

| estado | \(\eta_f\) | NO | NOₓ | \(D\) | \(D/\eta_f\) | NO₂ mostrado | diferencia vs modelo | observación |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| encontrado | | | | | | | | |
| cambio autorizado | | | | | | | | |
| restaurado | | | | | | | | |

Todas las concentraciones en nmol/mol.

## Modelo de cálculo

Hipótesis H0, firmware sin corrección:

\[
M\approx D=X-N.
\]

Hipótesis H1, firmware corrige eficiencia:

\[
M\approx \frac{D}{\eta_f}.
\]

Cambio esperado al modificar \(\eta\), manteniendo \(D\) constante:

\[
\Delta M=D\left(\frac1{\eta_2}-\frac1{\eta_1}\right).
\]

## Ejemplo numérico trabajado

Con gas estable se observa \(X=448.0\), \(N=351.0\), por tanto:

\[
D=448.0-351.0=97.0\ \mathrm{nmol/mol}.
\]

Con \(\eta_f=0.970\):

\[
D/\eta_f=97.0/0.970=100.0\ \mathrm{nmol/mol}.
\]

Pantalla muestra 100.1 nmol/mol: coincide con corrección. Si se cambia temporalmente a 0.950:

\[
M_2=97.0/0.950=102.105\ \mathrm{nmol/mol},
\]

\[
\Delta M=2.105\ \mathrm{nmol/mol}.
\]

Pantalla muestra 102.0 nmol/mol mientras NO y NOₓ crudos permanecen dentro de 0.3 nmol/mol. Resultado confirma corrección automática. Aplicar de nuevo \(D/\eta\) a NO₂ mostrado produciría \(100.1/0.970=103.2\) nmol/mol: doble corrección incorrecta.

## Criterios de aceptación

- Estado de firmware y valor de \(\eta_f\) quedan trazables.
- Modelo seleccionado reproduce pantalla dentro de máximo 0.5 nmol/mol o resolución del equipo.
- Cambio observado por modificación autorizada coincide con \(\Delta M\) dentro de incertidumbre y estabilidad del gas.
- Configuración original restaurada y verificada.
- Si campos NO y NOₓ exportados ya están procesados, documentar arquitectura; no asumir que son crudos.

## Seguridad

Aplican controles de cilindro NO y venteo O₃ de E4. Cambio de firmware solo con autorización, copia de estado inicial y responsable presente. No dejar instrumento operativo con valor de prueba.

---

# E7 — Formación de NO₂ en línea corta, larga y larga caliente

## Objetivo

Medir artefacto de formación de NO₂ por reacción NO+O₃ durante residencia externa e interna; comparar tres configuraciones y validar cálculo cinético.

## Instrumentos

Instrumentos comunes; líneas definidas; control térmico a 35 °C; mezclador capaz de entregar simultáneamente NO=180 y O₃=90 nmol/mol; analizador NOₓ; analizador O₃ cuando esté disponible.

## Procedimiento paso a paso

1. **Caracterización geométrica, 10 min.** Medir longitud y DI; calcular volumen. Verificar caudal con patrón.
2. **Blancos, 10 min.** Aire cero y luego NO=180 sin O₃, 5 min cada uno. Confirmar que diferencia NOₓ−NO no cambia por línea.
3. **Referencia de mezcla, 10 min.** Preparar NO=180 y O₃=90 nmol/mol en punto de entrada. Confirmar caudales y ausencia de condensación.
4. **Línea corta A, 20 min.** Instalar 2 m, DI 4 mm, 1.0 L/min, 22 °C. Acondicionar 10 min o hasta estabilidad; registrar cinco medias de 1 min y variables internas.
5. **Purga, 5 min.** Desactivar O₃ y purgar con aire cero.
6. **Línea larga B, 25 min.** Instalar 8 m, DI 6 mm, 1.8 L/min, 28 °C. Acondicionar 15 min; registrar cinco medias.
7. **Purga, 5 min.** Igual paso anterior.
8. **Línea larga caliente C, 30 min.** Misma geometría, 1.55 L/min, 35 °C. Esperar equilibrio térmico 10 min, acondicionar gas 10 min y registrar cinco medias.
9. **Secuencia inversa, 20 min.** Repetir A al final para comprobar deriva. Si A final difiere >1 nmol/mol de A inicial, invalidar comparación o modelar deriva.
10. **Análisis, 20 min.** Corregir blancos, calcular residencia total, predicción cinética y diferencia medida.

Duración: 155 min.

## Tabla de registro

| configuración | L (m) | DI (mm) | V (mL) | Q (L/min) | \(t_{ext}\) (s) | \(t_{int}\) (s) | T (°C) | P (kPa) | NO entrada | O₃ entrada | NO₂ entrada | NO₂ salida | NO₂ formado |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A corta | 2 | 4 | | 1.00 | | 1.5 | 22 | | 180 | 90 | | | |
| B larga | 8 | 6 | | 1.80 | | 1.8 | 28 | | 180 | 90 | | | |
| C larga caliente | 8 | 6 | | 1.55 | | 1.8 | 35 | | 180 | 90 | | | |

## Modelo de cálculo

Volumen cilíndrico:

\[
V=\pi\left(\frac d2\right)^2L.
\]

Residencia externa, con unidades coherentes:

\[
t_{ext}=\frac{V}{Q},\qquad t=t_{ext}+t_{int}.
\]

Densidad molecular para gas ideal:

\[
n=\frac{P}{k_BT}\frac1{10^6}\quad[\mathrm{moléculas/cm^3}],
\]

donde división por \(10^6\) convierte m³ a cm³. Concentraciones moleculares iniciales:

\[
A_0=x_{NO}n,\qquad B_0=x_{O_3}n.
\]

Para \(-dA/dt=kAB\), \(k=1.8\times10^{-14}\) cm³ molécula⁻¹ s⁻¹ y \(A_0\ne B_0\), extensión \(z\) en moléculas/cm³:

\[
R=\frac{A_0}{B_0}\exp[(A_0-B_0)kt],
\qquad
z=\frac{RB_0-A_0}{R-1}.
\]

NO₂ formado:

\[
x_{NO_2,form}=10^9\frac{z}{n}\quad\mathrm{nmol/mol}.
\]

Modelo debe considerarse predicción de diseño: flujo no ideal, mezcla, perfil térmico, presión y reacción dentro del analizador requieren evaluación experimental.

## Ejemplo numérico trabajado

Para A, \(L=2\) m y \(d=4\) mm:

\[
V=\pi(0.002)^2(2)=2.513\times10^{-5}\ \mathrm{m^3}=25.13\ \mathrm{mL}.
\]

Con \(Q=1.0\) L/min = 16.667 mL/s:

\[
t_{ext}=25.13/16.667=1.508\ \mathrm{s},
\quad t=1.508+1.500=3.008\ \mathrm{s}.
\]

A 22 °C y 101.325 kPa:

\[
n=\frac{101325}{(1.380649\times10^{-23})(295.15)}10^{-6}
=2.4865\times10^{19}\ \mathrm{cm^{-3}}.
\]

\[
A_0=180\times10^{-9}n=4.4757\times10^{12},
\quad B_0=90\times10^{-9}n=2.2379\times10^{12}.
\]

Aplicando ecuación integrada resulta:

\[
x_{NO_2,form}=18.45\ \mathrm{nmol/mol}.
\]

Mismo cálculo para tres configuraciones, incluyendo residencia interna:

| configuración | \(V\) mL | \(t_{ext}\) s | \(t_{int}\) s | \(t\) s | T °C | NO₂ formado corregido nmol/mol | consumo de NO inicial % |
|---|---:|---:|---:|---:|---:|---:|---:|
| A corta | 25.13 | 1.51 | 1.50 | 3.01 | 22 | 18.45 | 10.25 |
| B larga | 226.19 | 7.54 | 1.80 | 9.34 | 28 | 42.43 | 23.57 |
| C larga caliente | 226.19 | 8.76 | 1.80 | 10.56 | 35 | 45.13 | 25.07 |

Si NO₂ de entrada es 20 nmol/mol, salidas cinéticas ideales serían 38.45, 62.43 y 65.13 nmol/mol antes de efectos de convertidor. Cambio relativo respecto a NO₂ inicial sería 92.2 %, 212.1 % y 225.7 %, no 0.9 %, 2.15 % y 3.1 % del dataset original.

## Criterios de aceptación

- Geometría, caudal, T, P y residencia interna documentados.
- Repetición A final compatible con A inicial dentro de 1 nmol/mol.
- Para uso rutinario, formación permitida debe definirse por objetivo de datos. Criterio didáctico de 2 % no es límite universal.
- Con condiciones dadas, predicción excede ampliamente 2 % respecto a NO₂ inicial; configuraciones no son aceptables sin corrección/rediseño.
- Preferir reducción de volumen, aumento de caudal compatible, separación de O₃ antes de línea o modelación validada. Línea caliente no garantiza menor artefacto.
- Si medición difiere del modelo más que incertidumbre combinada, investigar mezcla, presión, temperatura real, pérdidas de O₃, residencia interna y respuesta temporal.

## Seguridad

Mezcla NO+O₃ forma NO₂ tóxico. Extracción y destructor de O₃ obligatorios. No calentar línea sin control de temperatura y material compatible. Desactivar O₃ primero, purgar completamente y después cerrar NO. No desconectar línea caliente o presurizada.

---

# E16 — Monte Carlo para modelo diferencial con covarianza medida

## Objetivo

Propagar distribución de \(NO_2=(X-N)/\eta\) mediante Monte Carlo (MCM), preservando covarianza medida en E3 y distribución de \(\eta\) obtenida en E4; comparar con aproximación GUM lineal.

## Instrumentos y software

Resultados E3 y E4; computador con R; plantilla de presupuesto; semilla registrada; mínimo \(10^6\) simulaciones para resultado final.

## Procedimiento paso a paso

1. **Reunir entradas, 5 min.** Medias \(X,N\), \(u_X,u_N\), covarianza o \(\rho\), \(\eta,u_\eta\), grados de libertad y evidencia de distribuciones.
2. **Validar matriz, 5 min.** Construir matriz de covarianza y comprobar semidefinida positiva.
3. **Definir distribuciones, 5 min.** Usar normal bivariada para canales si datos lo respaldaldan. Usar normal truncada \(0<\eta\le1\), beta ajustada o distribución empírica para eficiencia.
4. **Simulación piloto, 5 min.** Ejecutar \(10^5\) sorteos y revisar valores imposibles, histogramas y estabilidad.
5. **Simulación final, 10 min.** Ejecutar \(10^6\) sorteos, calcular \(y_j=(X_j-N_j)/\eta_j\), media, desviación, mediana e intervalo de cobertura 95 % por cuantiles.
6. **Comparación GUM, 5 min.** Calcular modelo lineal con término de covarianza.
7. **Sensibilidad, 5 min.** Repetir con \(\rho=0\) para mostrar efecto de ignorar covarianza.

Duración: 40 min.

## Tabla de registro

| entrada | estimación | u estándar | distribución | correlación/fuente | unidad |
|---|---:|---:|---|---|---|
| \(X\) | | | normal conjunta | E3 | nmol/mol |
| \(N\) | | | normal conjunta | E3 | nmol/mol |
| \(\eta\) | | | normal truncada/beta/empírica | E4 | 1 |
| número de sorteos | 1 000 000 | — | — | — | — |
| semilla | | — | — | — | — |

## Modelo de cálculo

Matriz de canales:

\[
\Sigma=\begin{pmatrix}
u_X^2&\rho u_Xu_N\\
\rho u_Xu_N&u_N^2
\end{pmatrix}.
\]

Para cada sorteo:

\[
(X_j,N_j)\sim N_2[(\bar X,\bar N),\Sigma],
\quad \eta_j\sim f_\eta,
\quad y_j=\frac{X_j-N_j}{\eta_j}.
\]

Resultado MCM: media o mediana, desviación estándar y cuantiles 0.025 y 0.975. No imponer \(U=2u\) si distribución de salida es asimétrica.

Aproximación GUM:

\[
u_c^2(y)=\frac{u_X^2+u_N^2-2\rho u_Xu_N}{\eta^2}
+\left(\frac{X-N}{\eta^2}\right)^2u_\eta^2.
\]

## Ejemplo numérico trabajado completo

Entradas:

\[
X=205.0,\ u_X=1.2;\quad N=200.0,\ u_N=1.0;
\]

\[
\rho=0.70;\quad \eta=0.970,\ u_\eta=0.010.
\]

Covarianza:

\[
\operatorname{cov}(X,N)=0.70(1.2)(1.0)=0.84.
\]

Resultado:

\[
y=\frac{5.0}{0.970}=5.1546\ \mathrm{nmol/mol}.
\]

Coeficientes:

\[
c_X=1/0.970=1.03093,
\quad c_N=-1.03093,
\]

\[
c_\eta=-5/0.970^2=-5.31406\ \mathrm{nmol/mol}.
\]

Varianza de canales:

\[
u^2_{can}=1.03093^2(1.2^2+1.0^2)-2(1.03093^2)(0.84)
=0.8077.
\]

Varianza por eficiencia:

\[
u^2_\eta=(5.31406)^2(0.010)^2=0.00282.
\]

\[
u_c=\sqrt{0.8077+0.00282}=0.9003\ \mathrm{nmol/mol},
\quad U_{k=2}=1.801\ \mathrm{nmol/mol}.
\]

Sin covarianza:

\[
u_c=\sqrt{\frac{1.2^2+1.0^2}{0.970^2}+0.00282}
=1.611\ \mathrm{nmol/mol}.
\]

MCM con normal bivariada y \(\eta\) normal truncada debe producir aproximadamente media 5.155 nmol/mol, u 0.90 nmol/mol e intervalo 95 % cercano a [3.39, 6.92] nmol/mol; valores exactos dependen de semilla y distribución de \(\eta\). Diferencia frente a GUM debe ser pequeña porque incertidumbre relativa de \(\eta\) es baja.

Código R mínimo:

```r
set.seed(20260826)
B <- 1e6
mu <- c(X = 205, N = 200)
Sigma <- matrix(c(1.2^2, 0.84, 0.84, 1.0^2), 2, 2)
L <- chol(Sigma)
z <- matrix(rnorm(2 * B), ncol = 2)
canales <- sweep(z %*% L, 2, mu, `+`)
eta <- rnorm(B, 0.970, 0.010)
while (any(eta <= 0 | eta > 1)) {
  i <- which(eta <= 0 | eta > 1)
  eta[i] <- rnorm(length(i), 0.970, 0.010)
}
y <- (canales[, 1] - canales[, 2]) / eta
c(media = mean(y), u = sd(y), quantile(y, c(0.025, 0.5, 0.975)))
```

## Criterios de aceptación

- Matriz de covarianza válida y fuente de \(\rho\) trazable a E3.
- Distribución de \(\eta\) respeta dominio físico y evidencia E4.
- Resultado estable: duplicar sorteos cambia media, u y límites <0.5 %.
- MCM y GUM compatibles dentro de 2 % para caso casi lineal; diferencia mayor exige revisar no linealidad, truncamiento o código.
- Comparación con \(\rho=0\) se usa como diagnóstico, no como resultado si covarianza fue medida.

## Seguridad

E16 es análisis de datos y no requiere gases. Si se ejecuta mientras sistema permanece montado, cilindro debe quedar cerrado y líneas purgadas; generador de O₃ apagado y venteo conectado.

---

# Cálculos correctivos

## A. Corrección D6: cinética de formación de NO₂ en línea

Se aplica modelo de segundo orden completo, \(k=1.8\times10^{-14}\) cm³ molécula⁻¹ s⁻¹, presión asumida 101.325 kPa, NO=180 nmol/mol y O₃=90 nmol/mol. Residencia total incluye línea y analizador.

### A.1 Configuración A: 2 m, DI 4 mm, 1 L/min, 22 °C

\[
V=25.13\ \mathrm{mL},\quad t_{ext}=25.13/(1000/60)=1.508\ \mathrm{s},
\]

\[
t=1.508+1.500=3.008\approx3.01\ \mathrm{s}.
\]

Con \(n=2.4865\times10^{19}\) moléculas/cm³ y ecuación integrada:

\[
NO_{2,form}=18.45\ \mathrm{nmol/mol}.
\]

### A.2 Configuración B: 8 m, DI 6 mm, 1.8 L/min, 28 °C

\[
V=226.19\ \mathrm{mL},\quad Q=30.0\ \mathrm{mL/s},
\]

\[
t_{ext}=7.540\ \mathrm{s},\quad t=7.540+1.800=9.340\ \mathrm{s}.
\]

Con \(n=2.4370\times10^{19}\) moléculas/cm³:

\[
NO_{2,form}=42.43\ \mathrm{nmol/mol}.
\]

### A.3 Configuración C: 8 m, DI 6 mm, 1.55 L/min, 35 °C

\[
Q=1550/60=25.833\ \mathrm{mL/s},
\]

\[
t_{ext}=226.19/25.833=8.756\ \mathrm{s},
\quad t=8.756+1.800=10.556\ \mathrm{s}.
\]

Con \(n=2.3816\times10^{19}\) moléculas/cm³:

\[
NO_{2,form}=45.13\ \mathrm{nmol/mol}.
\]

### A.4 Valores que deben sustituir dataset

| configuración | valor original | valor cinético corregido | factor original/corregido | cambio relativo respecto a NO₂ inicial=20 |
|---|---:|---:|---:|---:|
| A corta | 0.18 | 18.45 | 0.0098 | 92.2 % |
| B larga | 0.43 | 42.43 | 0.0101 | 212.1 % |
| C larga caliente | 0.62 | 45.13 | 0.0137 | 225.7 % |

Unidades: nmol/mol. Valores originales subestiman formación aproximadamente 73 a 102 veces. Resultado corregido es predicción ideal y debe validarse mediante E7.

## B. Corrección D1: suma del presupuesto EN 14211

Vector del script R:

\[
(0,0,0.09,0.90,0.06,0.26,0.44,0.02,0.249,0.35,
2.70,3.22,0.58,1.44,1.04,2.08,2.08,0.60).
\]

Suma directa de cuadrados:

\[
\sum u_i^2=31.430601\ (\mathrm{nmol/mol})^2,
\]

\[
u_{c,reconstruido}=\sqrt{31.430601}=5.60630\ \mathrm{nmol/mol}.
\]

Redondeado a dos decimales: 5.61 nmol/mol. No coincide con suma publicada 30.4 ni con \(u_c=5.5\) nmol/mol:

\[
\sqrt{30.4}=5.51362\ \mathrm{nmol/mol}\approx5.5.
\]

Diferencia de varianza:

\[
31.430601-30.4=1.030601\ (\mathrm{nmol/mol})^2,
\]

Diferencia relativa de \(u_c\) respecto a 5.5:

\[
100(5.60630-5.5)/5.5=1.93\%.
\]

Diferencia relativa de varianza respecto a 30.4 es 3.39 %. Corrección documental correcta:

1. reportar **5.606 nmol/mol** como reconstrucción obtenida al sumar valores estándar redondeados de 18 filas;
2. reportar por separado **30.4 (nmol/mol)² y 5.5 nmol/mol** como valores publicados del ejemplo;
3. explicar que cifras de componentes, al estar redondeadas y/o reconstruidas, no reproducen exactamente total publicado;
4. no presentar 5.61 como reproducción exacta ni reemplazar silenciosamente total normativo;
5. mantener \(W=100(2\times5.5)/104=10.5769\%\approx10.6\%\) cuando se cita resultado publicado.

Comentario recomendado para script:

```r
# La suma de componentes redondeados/reconstruidos es 31.430601 y uc=5.6063.
# EN 14211 publica por separado suma=30.4 y uc=5.5; diferencia procede de
# reconstrucción y redondeo, por lo que ambos resultados se etiquetan sin mezclarlos.
```

## C. Corrección D3: sensibilidades y covarianza del CSV

Para fila diferencial con \(X=205\), \(N=200\), \(\eta=0.97\):

\[
c_X=+1/\eta=+1.030927835,
\]

\[
c_N=-1/\eta=-1.030927835,
\]

\[
c_\eta=-(X-N)/\eta^2=-5/0.9409=-5.314061005.
\]

Con \(u_X=1.2\), \(u_N=1.0\), \(\rho=0.70\):

\[
\operatorname{cov}(X,N)=\rho u_Xu_N=0.840000.
\]

Contribuciones individuales:

\[
c_Xu_X=1.2371134,
\quad (c_Xu_X)^2=1.5304496,
\]

\[
c_Nu_N=-1.0309278,
\quad (c_Nu_N)^2=1.0628122.
\]

Fila explícita de covarianza:

\[
2c_Xc_N\operatorname{cov}(X,N)
=2(1.0309278)(-1.0309278)(0.84)
=-1.7855245\ (\mathrm{nmol/mol})^2.
\]

Varianza de canales:

\[
1.5304496+1.0628122-1.7855245=0.8077373.
\]

Filas corregidas sugeridas para CSV:

```csv
Canal NOx,indicación NOx,205,nmol/mol,caso diferencial,A,normal,1,1.030927835,1.2,1.237113402,1.530449580,,canal_compartido,NO,didactica,Coeficiente +1/eta
Canal NO,indicación NO,200,nmol/mol,caso diferencial,A,normal,1,-1.030927835,1.0,-1.030927835,1.062812201,,canal_compartido,NO,didactica,Coeficiente -1/eta
Eficiencia eta,eficiencia convertidor,0.97,fracción,caso diferencial,B,normal,1,-5.314061005,0.01,-0.053140610,0.002823921,,convertidor,NO,didactica,Coeficiente -(NOx-NO)/eta^2
Covarianza NOx-NO,covarianza medida,0.84,(nmol/mol)^2,E3,A,empirica,1,-2.125850781,0.84,, -1.785524489,,canal_compartido,NO,didactica,Termino 2*c_NOx*c_NO*cov; varianza puede ser negativa
```

En fila de covarianza, `coeficiente_sensibilidad=-2.125850781` representa \(2c_Xc_N\), `u_estandar_entrada=0.84` contiene covarianza, `contribucion_nmol_mol` debe quedar vacía porque término tiene unidades de varianza, y `varianza=-1.785524489`. Alternativa más limpia: añadir columnas específicas `covarianza_entrada` y `termino_covarianza`; no forzar covarianza dentro de esquema para entradas escalares.

Fila normativa «Eficiencia del convertidor» con coeficiente 104 pertenece a reconstrucción EN 14211 y no debe mezclarse con modelo diferencial. Debe etiquetarse como tratamiento normativo reconstruido o recalcularse desde modelo y definición exacta del ejemplo. Para caso diferencial, coeficiente correcto es −5.31406, no 104.

## D. Corrección D5: impureza realista de NO₂ en cilindro

Valor `impureza_no2_nmol_mol=0.40` atribuido al cilindro está mal dimensionado. Para cilindro de NO cercano a 40 µmol/mol, estimación de planificación realista de NO₂ como 1 % molar respecto a NO es:

\[
I_{cil}=0.01(40\ \mathrm{\mu mol/mol})
=0.40\ \mathrm{\mu mol/mol}
=400\ \mathrm{nmol/mol}.
\]

Con dilución 1:250:

\[
I_{mezcla}=400/250=1.60\ \mathrm{nmol/mol}.
\]

Por tanto:

- `0.40 nmol/mol` en cilindro es 1000 veces menor que `0.40 µmol/mol`;
- valor corregido de planificación es `400 nmol/mol` en cilindro;
- valor después de dilución 1:250 es `1.6 nmol/mol`;
- valor operativo debe tomarse del certificado real, con incertidumbre, fecha y estabilidad, no de supuesto genérico.

Para rediseño E4 con cilindro de 50 µmol/mol, mismo supuesto de 1 % sería 500 nmol/mol en cilindro. A fracción de dilución \(45/5000=0.009\):

\[
I_{mezcla}=500(0.009)=4.50\ \mathrm{nmol/mol}.
\]

Este valor no es despreciable frente a intercepto GPT y debe corregirse o incluirse como entrada de incertidumbre. Preferir cilindro con impureza certificada mucho menor; 1 % sirve para diseño conservador, no como sustituto de certificado.

---

# Cierre metrológico

1. E3 proporciona covarianza real para diferencia NOₓ−NO.
2. E4 estima eficiencia sin titulación profunda: NO residual mínimo 290 nmol/mol.
3. E5 establece si firmware ya aplica \(1/\eta\).
4. E7 demuestra que residencia interna no puede omitirse y corrige dataset por cinética.
5. E16 propaga modelo con covarianza y dominio físico de eficiencia.
6. Presupuesto debe separar reconstrucción con componentes redondeados de total publicado EN 14211.
7. Impureza de NO₂ debe expresarse en base y ubicación correctas: cilindro o mezcla diluida.
8. Ningún criterio didáctico sustituye método aplicable, certificado, manual del equipo ni sistema de calidad del laboratorio.
