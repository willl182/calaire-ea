# M4 — Presupuesto de incertidumbre del analizador

## 1 Ficha

**Duración:** 1 h 10 min (70 min).

**Posición en la jornada:** cuarto módulo, después de M3 — Conceptos GUM: Tipo A/B, PDFs y sensibilidad. Precede a M5 — Patrones de transferencia: calibración multipunto, deriva y verificación.

**Propósito:** construir y auditar un presupuesto Tipo B para un analizador de ozono a 120 nmol/mol, a partir de especificaciones de fabricante y otras fuentes documentales, y reconocer cuáles componentes deben sustituirse posteriormente por evaluaciones experimentales.

**Prerrequisitos:**

- distinguir evaluación Tipo A y Tipo B;
- convertir límites e incertidumbres expandidas a incertidumbres estándar;
- reconocer distribuciones normal y rectangular;
- aplicar combinación en cuadratura para componentes independientes;
- interpretar coeficientes de sensibilidad y participación en la varianza.

**Materiales:**

1. `contenido/plantillas/plantilla_presupuesto.R`, caso 1;
2. Thermo Fisher Scientific, *Model 49i Instruction Manual*, Table 1-1 y cap. 4;
3. HORIBA, *APOA-370 Operation Manual*, §10.2;
4. `contenido/handout/handout_teorico_gum_o3.md`, §§3.1–3.3 y 4.2–4.4;
5. `evaluation and uncertainty budget of ozone.md`, utilizada únicamente como **fuente secundaria** para la estructura de presupuestos tipo EN 14625;
6. calculadora o entorno R y una hoja para registrar fuente, interpretación, PDF, divisor y contribución.

**Distribución del tiempo:** exposición, 31 min; ejercicio central, 31 min; errores frecuentes y preguntas, 4 min; cierre y transición, 4 min. Total: 70 min.

## 2 Objetivos específicos

Al finalizar el módulo, el participante podrá:

1. **identificar** en una ficha técnica al menos cuatro especificaciones relevantes para un presupuesto de incertidumbre;
2. **convertir** ruido RMS, límites bilaterales e incertidumbre expandida en incertidumbres estándar con una PDF justificada;
3. **calcular** la incertidumbre estándar combinada de un presupuesto Tipo B con componentes independientes;
4. **ordenar** las fuentes según su contribución a la varianza e indicar cuáles requieren evidencia experimental propia;
5. **comparar** especificaciones del Thermo 49i y del APOA-370 sin equiparar magnitudes, periodos o condiciones diferentes.

## 3 Guion de exposición con tiempos

### 3.1 Del dato documental a la fila del presupuesto — 0:00 a 0:08; acumulado 0:08 (8 min)

**Idea fuerza:** una especificación no es automáticamente una incertidumbre estándar; primero hay que establecer qué representa.

**Guion dictable:**

“En este módulo evaluaremos la indicación de un analizador de ozono en 120 nmol/mol. Para el cálculo didáctico trataremos numéricamente 120 nmol/mol como 120 ppb. El presupuesto será Tipo B porque parte de manuales, un certificado supuesto y límites documentales, no de una serie experimental obtenida durante la clase.”

“Cada fila debe contestar seis preguntas: ¿qué efecto físico representa?, ¿qué cifra informa la fuente?, ¿en qué unidad?, ¿es RMS, límite, incertidumbre estándar o incertidumbre expandida?, ¿qué distribución representa el conocimiento disponible?, ¿está ya incluida en otra fila? Si falta una respuesta, la fila todavía no es defendible.”

Presente las conversiones que se usarán:

\[
u(x)=a/\sqrt3
\]

para un efecto limitado entre \(-a\) y \(+a\), con PDF rectangular;

\[
u(x)=U/k
\]

cuando un certificado declara incertidumbre expandida \(U\) y factor de cobertura \(k\); y conservación directa de una cifra RMS como incertidumbre estándar cuando el significado, el tiempo de promedio y las condiciones son compatibles.

“Tipo B no significa sistemático. Es el método de evaluación basado en información distinta del análisis estadístico de observaciones actuales. Tampoco debemos asignar rectangular por costumbre: la PDF debe corresponder al contenido real de la fuente.”

**Referencias verificadas:** handout, §§3.1–3.3: asignación de PDFs, distribución rectangular y normal; líneas 223–262 del archivo. JCGM 100:2008, §§4.3 y 5.1, según la síntesis del handout.

### 3.2 Combinación, ranking y doble conteo — 0:08 a 0:16; acumulado 0:16 (8 min)

**Idea fuerza:** el ranking orienta prioridades, pero solo después de verificar el modelo y el origen de los datos.

**Guion dictable:**

“En el caso didáctico todas las entradas se expresan directamente en ppb equivalentes. Por eso el coeficiente de sensibilidad es uno. Supondremos independencia para practicar la combinación, aunque en una evaluación real esta hipótesis debe revisarse.”

Escriba:

\[
u_c(y)=\sqrt{\sum_i[c_i u(x_i)]^2},
\qquad
p_i=100\frac{[c_i u(x_i)]^2}{u_c^2(y)}.
\]

“La primera expresión combina las contribuciones estándar independientes. La segunda calcula la participación de cada componente en la varianza. Un porcentaje alto sugiere dónde conviene mejorar evidencia o desempeño. Sin embargo, una fuente omitida nunca aparecerá en el ranking y una fila duplicada parecerá más importante de lo que realmente es.”

“Debemos vigilar especialmente el doble conteo. Si el certificado de calibración ya incorpora repetibilidad, presión o temperatura internas, no se agregan otra vez sin una desagregación coherente. Tampoco se suman como independientes ruido, detección y repetibilidad solo porque las tres cifras aparecen en un manual: pueden describir aspectos solapados.”

“Para cada componente anotaremos su linaje: manual, certificado, ensayo propio o supuesto didáctico. La trazabilidad documental no es una columna decorativa; permite descubrir interpretaciones incorrectas antes de aceptar el total.”

**Referencias verificadas:** handout, §4.2, ley de propagación; §4.3, doble conteo; §4.4, presupuesto y contribuciones. Líneas 380–439. JCGM 100:2008, §§5.1–5.2 y advertencia de §4.3.10, según el handout.

### 3.3 Lectura crítica del Thermo 49i — 0:16 a 0:24; acumulado 0:24 (8 min)

**Idea fuerza:** deben conservarse literalmente la base temporal, la escala y las condiciones de cada especificación.

**Guion dictable:**

“La Table 1-1 del Model 49i informa ruido de cero de 0.25 ppb RMS con promedio de 60 s; límite inferior detectable de 0.5 ppb; deriva de cero menor que 1 ppb en 24 horas y menor que 2 ppb en 7 días; deriva de span menor que 1 % por mes, incluyendo deriva de transductores; y linealidad de más o menos 1 % de escala completa. Las especificaciones de desempeño se basan en operación entre 20 °C y 30 °C.”

“Si seleccionamos una escala completa de 200 ppb, la linealidad de 1 % equivale a un límite de 2 ppb. Si solo conocemos ese límite y admitimos valores igualmente posibles dentro de él, usamos rectangular. La deriva de cero de 24 horas puede tratarse de manera análoga. El ruido RMS se conserva como incertidumbre estándar solo para el promedio de 60 segundos declarado.”

“Ahora auditemos la plantilla. El caso 1 rotula una deriva de span de 1 % en 24 horas. La Table 1-1 no respalda ese periodo: dice menos de 1 % por mes. Además, la tabla no aclara en esa fila si el porcentaje se aplica a lectura o a escala completa. Ejecutaremos la plantilla sin modificarla porque el objetivo incluye auditar un caso precargado, pero esa fila debe quedar marcada como supuesto no verificado.”

“La cifra de presión equivalente de 0.36 ppb, la resolución de 0.1 ppb y el certificado con 1.8 ppb y factor dos tampoco aparecen en Table 1-1. Pueden ser entradas válidas si existe otra fuente, pero no deben atribuirse a esa tabla.”

“El capítulo 4 aporta el contexto para reemplazar especificaciones por evidencia. Solicita la misma fuente de aire cero para el fotómetro y el ozonizador, describe una calibración multipunto, propone span cercano al 80 % del límite superior, recomienda al menos otros cinco niveles y establece verificaciones periódicas de cero y span. Por ello, falta de ajuste y deriva deben terminar respaldadas por datos del sistema real.”

**Referencias exactas verificadas:** Thermo Fisher Scientific, *Model 49i Instruction Manual*, Table 1-1, página impresa 1-3, página 25 del PDF. Cap. 4: equipo y aire cero, pp. impresas 4-1–4-2, PDF 137–138; linealidad, pp. 4-5–4-6, PDF 141–142; calibración multipunto, pp. 4-8–4-11, PDF 144–147; verificaciones periódicas, pp. 4-11–4-12, PDF 147–148.

### 3.4 Comparación con APOA-370 y presupuestos de laboratorio/campo — 0:24 a 0:31; acumulado 0:31 (7 min)

**Idea fuerza:** la comparación solo es válida entre componentes homólogos bajo igual escala, periodo y condición de operación.

**Guion dictable:**

“El APOA-370 declara sensibilidad mínima de 0.5 ppb expresada como dos sigma para intervalos de 0.2 ppm o menores; reproducibilidad de más o menos 1 % de escala completa; linealidad de más o menos 1 % de escala completa; deriva de cero de más o menos 1 % de escala completa por día y 2 % por semana; y los mismos límites para deriva de span.”

“A escala completa de 200 ppb, cada especificación de 1 % representa un límite de 2 ppb. La cifra de detección expresada como dos sigma puede convertirse a una sigma si aceptamos la interpretación normal indicada por esa notación. No obstante, no formaremos un total oficial del APOA: faltan decisiones sobre solapamiento, condiciones, componentes y correlaciones.”

“El manual también declara efectos de interferencia: humedad al 2.5 %, más o menos 2.5 ppb; tolueno a 1 ppm, más o menos 2.5 ppb; y dióxido de azufre a 0.2 ppm, más o menos 4 % de escala completa. Esos valores no se agregan indiscriminadamente. Primero se define si las condiciones y sustancias son pertinentes para el mensurando.”

“Como orientación secundaria, el resumen local de EN 14625 diferencia un presupuesto de laboratorio —repetibilidad, falta de ajuste, influencias, interferentes, promediado, diferencia entre puertos e incertidumbre del gas de calibración— de uno de campo, que añade deriva de largo plazo, reproducibilidad en sitio y pureza del aire cero. EN 14625 queda marcada aquí como fuente secundaria porque no se verificó el texto normativo original ni se atribuyen páginas o cláusulas.”

**Referencias exactas verificadas:** HORIBA, *APOA-370 Operation Manual*, §10.2 “Specification”, página impresa 92, página 104 del PDF. Fuente secundaria `evaluation and uncertainty budget of ozone.md`, apartado 2, líneas 35–71; los totales allí resumidos son \(u_c=4.3\) nmol/mol y \(W=7.1\%\) para laboratorio, y \(u_{c,act}=4.7\) nmol/mol y \(W=7.8\%\) para campo; no constituyen el resultado del ejercicio.

## 4 Ejercicio/actividad

### Presupuesto Tipo B del Thermo 49i y comparación con APOA-370 — 0:31 a 1:02; acumulado 1:02 (31 min)

**Organización:** parejas; una persona opera la plantilla y la otra verifica manual y trazabilidad. Intercambian funciones a mitad del ejercicio.

**Datos del caso 1 a 120 nmol/mol:** ruido RMS 0.25 ppb, normal con divisor 1; deriva de cero 24 h con límite 1.0 ppb, rectangular; deriva de span precargada como 1 % de 120 ppb, rectangular, pero marcada para auditoría frente al periodo mensual del manual; linealidad 1 % de escala completa de 200 ppb, rectangular; efecto de presión equivalente 0.36 ppb, rectangular y con fuente pendiente; resolución 0.1 ppb tratada como semiancho 0.05 ppb, rectangular y con fuente pendiente; certificado de calibración con \(U=1.8\) ppb y \(k=2\), con fuente pendiente. Use \(c_i=1\), independencia y grados de libertad infinitos para este ejercicio Tipo B.

**Secuencia de trabajo:**

1. **0:31–0:37:** registre cada componente, valor, unidad, PDF, divisor y fuente declarada.
2. **0:37–0:45:** convierta las entradas a incertidumbres estándar y ejecute el caso 1 de `plantilla_presupuesto.R`.
3. **0:45–0:51:** compruebe combinación en cuadratura y ordene componentes por contribución, sin confundir ranking matemático con validez metrológica.
4. **0:51–0:57:** audite las filas contra Thermo Table 1-1: clasifique como verificada, interpretación no respaldada o fuente adicional requerida.
5. **0:57–1:02:** compare semicuantitativamente con APOA-370 a escala completa de 200 ppb. Incluya linealidad, reproducibilidad, deriva diaria de cero y span y detección a dos sigma; no calcule un total del APOA ni sume posibles componentes solapados.

**Producto:** tabla completa del caso 1, total combinado, incertidumbre expandida, ranking elaborado por el participante, auditoría de procedencia y un párrafo de comparación prudente con APOA-370.

**Resultado esperado, en una línea:** el caso 1 ejecutado sin modificar debe dar aproximadamente \(u_c=1.75\) ppb, \(U=3.50\) ppb con \(k\approx2\) y \(W=2.9\%\), acompañado de la advertencia de que la deriva de span está mal periodizada frente al manual y tres entradas requieren fuente adicional.

## 5 Errores frecuentes y preguntas típicas

### 1:02 a 1:06; acumulado 1:06 (4 min)

**Errores frecuentes:**

- tratar todo límite como incertidumbre estándar sin aplicar divisor;
- leer “1 %” sin indicar si corresponde a lectura o escala completa;
- cambiar “por mes” a “por día” para acomodar la plantilla;
- sumar detección, ruido y reproducibilidad como componentes independientes sin revisar solapamiento;
- atribuir al manual cifras que proceden de un certificado, supuesto o cálculo auxiliar;
- interpretar el primer lugar del ranking como prueba de que la fuente está correctamente modelada.

**Preguntas típicas y respuestas cortas:**

1. **¿RMS siempre equivale a incertidumbre estándar?** Solo cuando la definición, el promedio y las condiciones son compatibles con el mensurando.
2. **¿Una especificación “±a” siempre usa rectangular?** No; rectangular es defendible cuando solo se conocen límites y no hay información que favorezca valores internos.
3. **¿Puede usarse la deriva mensual para un resultado diario?** Solo mediante un modelo temporal explícito y evidencia; no cambiando la etiqueta.
4. **¿El componente mayor es siempre el primero que debe reducirse?** No; primero se verifica que sea válido, independiente y pertinente.
5. **¿Por qué no calculamos una incertidumbre total del APOA-370?** Porque la ficha no define por sí sola un presupuesto completo ni resuelve solapamientos y condiciones de uso.

## 6 Cierre y transición

### 1:06 a 1:10; acumulado 1:10 (4 min)

Un presupuesto defendible comienza con lectura crítica, definición del efecto y trazabilidad de cada entrada; el cálculo y el ranking vienen después. El caso mostró qué puede obtenerse de especificaciones y, sobre todo, qué debe reemplazarse con calibraciones y verificaciones propias. En M5 se desarrollará esa evidencia mediante calibración multipunto, análisis de falta de ajuste, deriva y verificación de patrones de transferencia.
