# M6 — Incertidumbre en analizadores de NO, NO₂ y NOₓ por quimioluminiscencia

## 1 Ficha

**Duración:** 1 h 30 min (90 min).

**Carácter:** obligatorio. Sexto módulo, después de M5 — Patrones de transferencia y antes de M7 — Taller integrador.

**Propósito:** transferir conceptos GUM y disciplina documental del caso O₃ a una segunda familia instrumental: medición de NO, NO₂ y NOₓ por quimioluminiscencia, con énfasis en medición indirecta de NO₂, convertidor, GPT, línea de muestra y covarianza.

**Prerrequisitos:** M1, M3, M4 y M5; M2 sirve como contraste entre modelo físico Beer–Lambert y modelo diferencial del NO₂.

**Materiales:**

1. `datasets/dataset_nox_gpt_convertidor.csv` y `dataset_nox_linea_muestreo.csv`;
2. `datasets/dataset_nox_metadata.md` y `datasets/generar_dataset_nox.R`;
3. `plantillas/plantilla_presupuesto_nox.csv` y `.R`;
4. `handout/handout_no_nox.md`;
5. BS EN 14211:2012, especialmente Anexo F informativo;
6. calculadora o R.

**Fuentes principales:** BS EN 14211:2012, principio de quimioluminiscencia y Anexo F informativo, pp. impresas 81–88; JCGM 100:2008 para propagación con covarianzas; Doval Miñarro et al. (2011) para el mecanismo y dependencias de formación de NO₂ en líneas, sin usar sus magnitudes como base del dataset; Gluck et al. (2003) para convertidor y matriz en contexto de emisiones; Pernigotti et al. (2013) para incertidumbre, correlación e interferencias.

**Distribución del tiempo:** principio y arquitectura, 12 min; modelo y convertidor, 15 min; fuentes, 20 min; presupuesto EN 14211, 15 min; caso práctico, 20 min; cierre, 8 min. Total: 90 min.

> **Control documental:** APOA-370 es analizador de O₃ por absorción UV. No usar su manual como fuente instrumental NOx. El manual local `APNA-370_Operaton_Manual_GZ9100497232L.pdf` corresponde a un HORIBA Ambient NOx Monitor (2021) y está disponible. Verificar si APNA-370 es el equipo realmente instalado queda a cargo del operador antes de atribuir especificaciones comerciales.

## 2 Objetivos específicos

Al finalizar, participante podrá:

1. explicar reacción quimioluminiscente y ruta de señal;
2. distinguir canal NO, canal NOₓ y NO₂ calculado;
3. formular modelo diferencial y corrección por eficiencia sin duplicarla;
4. separar eficiencia, selectividad y estabilidad del convertidor;
5. identificar fuentes en detector, GPT, matriz, muestreo y operación;
6. convertir evidencia en contribuciones estándar sin confundir tolerancia con incertidumbre;
7. reconstruir presupuesto informativo EN 14211 a 104 nmol/mol;
8. propagar covarianza entre canales NO y NOₓ;
9. diagnosticar eficiencia GPT y formación NO₂ en línea;
10. proponer controles operativos defendibles.

## 3 Guion de exposición con tiempos

### 3.1 Qué mide analizador NOx — 0:00 a 0:12; acumulado 0:12 (12 min)

**Idea fuerza:** detector responde a NO; NO₂ depende de conversión y diferencia.

Reacciones:

\[
\mathrm{NO+O_3\rightarrow NO_2^*+O_2},\qquad
\mathrm{NO_2^*\rightarrow NO_2+h\nu}.
\]

Emisión ocupa región amplia del infrarrojo cercano, con máximo aproximado cercano a 1200 nm. Ruta incluye cámara con exceso de O₃, filtro óptico, detector, bomba, orificios y control de presión/flujo.

Canal NO mide muestra sin convertir. Canal NOₓ conduce muestra por convertidor NO₂→NO y mide NO original más fracción convertida. Equipos pueden conmutar rutas o usar canales paralelos. No describir NO₂ como lectura directa.

**Pregunta de control:** si canal NOₓ marca 205 y canal NO marca 200 nmol/mol, ¿qué señal pequeña determina NO₂? Diferencia de 5 nmol/mol; incertidumbres absolutas de ambos canales importan.

### 3.2 Modelo, convertidor y covarianza — 0:12 a 0:27; acumulado 0:27 (15 min)

Modelo mínimo:

\[
c_{NO_2}=c_{NO_x}-c_{NO}.
\]

Modelo didáctico corregido:

\[
c_{NO_2}=\frac{c_{NO_x}-c_{NO}}{\eta_c}.
\]

Antes de aplicarlo, verificar arquitectura y software: si instrumento ya corrige eficiencia, dividir otra vez genera doble corrección.

Coeficientes de sensibilidad:

\[
c_{NO_x}=1/\eta_c,\quad c_{NO}=-1/\eta_c,\quad
c_{\eta}=-\frac{c_{NO_x}-c_{NO}}{\eta_c^2}.
\]

Propagación:

\[
u^2(c_{NO_2})=\frac{u^2(c_{NO_x})+u^2(c_{NO})-2\operatorname{cov}(c_{NO_x},c_{NO})}{\eta_c^2}
+\left(\frac{c_{NO_x}-c_{NO}}{\eta_c^2}\right)^2u^2(\eta_c).
\]

Covarianza positiva reduce varianza de diferencia porque coeficientes de canales tienen signos opuestos. No asumir independencia ni correlación sin evidencia.

- **Eficiencia:** fracción de NO₂ convertida.
- **Selectividad:** capacidad de evitar respuesta por HNO₃, HONO, PAN, NH₃ y otros NOy.
- **Estabilidad:** cambio con temperatura, edad, contaminación y matriz.

EN 14211:2012 distingue capacidad mínima de convertidor, criterio de aprobación y corrección en intervalo intermedio; verificar cláusula y edición aplicables antes de convertir esos valores en regla local. Método EPA de 2002 usa criterio histórico distinto; no mezclar contextos.

### 3.3 Fuentes específicas — 0:27 a 0:47; acumulado 0:47 (20 min)

Construya diagrama causa–efecto con seis ramas:

1. **Detector y canales:** repetibilidad, resolución, sincronización, respuesta, falta de ajuste, rutas, reproducibilidad.
2. **Convertidor:** eficiencia, incertidumbre, concentración, temperatura, selectividad, envejecimiento, corrección automática.
3. **Calibración y GPT:** certificado y estabilidad de NO, impureza NO₂, caudales, presión/temperatura, O₃, aire cero, residencia, regresión.
4. **Interferencias y matriz:** NOy convertibles, quenching por H₂O/CO₂, condensación, memoria y ensayos de tipo.
5. **Muestreo:** pérdidas en línea/filtro, reacción NO–O₃ previa, material, volumen, caudal, residencia, suciedad y caída de presión.
6. **Ambiente y operación:** presión, temperatura, tensión, caudales, vacío, bomba, deriva y disponibilidad.

EN 14211 reconoce pérdidas y formación NO₂ en muestreo, pero ejemplo informativo no cuantifica toda fuente física. “Reconocida” no significa “incluida”. Doval Miñarro et al. (2011) muestra dependencia del artefacto con NO, O₃, temperatura y residencia; usar mecanismo para diseñar controles, no copiar umbral como criterio universal.

### 3.4 Presupuesto informativo EN 14211 — 0:47 a 1:02; acumulado 1:02 (15 min)

Anexo F de BS EN 14211:2012 es informativo. Ejemplo a límite horario de NO₂:

\[
l_h=104\ \mathrm{nmol/mol}.
\]

Verificación directa contra PDF, Anexo F, ejemplo F.4:

- suma de varianzas publicada: 30.4 (nmol/mol)²;
- incertidumbre combinada publicada: 5.5 nmol/mol;
- con factor de cobertura 2, incertidumbre expandida absoluta reconstruida: 11.0 nmol/mol;
- incertidumbre expandida relativa publicada: 10.6 %.

\[
W=100\frac{2(5.5)}{104}=10.6\%\text{, redondeado}.
\]

Para interferentes distintos de H₂O, EN 14211/EN ISO 14956 agrupa por signo: se suman por separado las respuestas positivas y negativas y se toma el grupo de mayor magnitud; H₂O se trata aparte. En el ejemplo, el valor 0.35 nmol/mol queda dominado por NH₃.

Valores estándar principales, parafraseados del ejemplo: falta de ajuste 0.90; temperatura de muestra 0.26; entorno 0.44; H₂O 0.249; otros interferentes 0.35; promediación 2.70; reproducibilidad de campo 3.22; deriva cero 0.58; deriva span 1.44; diferencia muestra/calibración 1.04; convertidor 2.08; gas de calibración 2.08; gas cero 0.60 nmol/mol.

Dominan reproducibilidad, promediación, convertidor y gas de calibración. Reducir contribuciones diminutas no mejora total de forma material. Comparación con 15 % solo corresponde al contexto europeo indicado; no presentarla como criterio colombiano universal.

## 4 Ejercicio/actividad — 1:02 a 1:22; acumulado 1:22 (20 min)

**Nombre:** Diagnóstico GPT, convertidor y línea de muestra.

**Organización:** parejas. Una persona calcula; otra audita unidades, fuentes, correcciones y decisiones. Cambiar roles después de 10 min.

**Parte A — GPT y eficiencia, 10 min**

1. filtrar niveles distintos de cero;
2. comprobar coherencia de unidades de caudal;
3. calcular `NO2_indicado = NOx - NO`;
4. ajustar `NO2_indicado = b + eta * NO2_GPT` por ciclo;
5. interpretar pendiente como eficiencia bajo modelo sintético;
6. separar criterio de aceptación de incertidumbre de pendiente.

**Parte B — línea, 5 min**

Comparar configuraciones por residencia total, temperatura y `cambio_relativo_pct`. Elegir aceptar/vigilar, reducir residencia y repetir, o invalidar hasta corregir. Criterio 2 % es didáctico.

**Parte C — diferencia y covarianza, 5 min**

Usar NOₓ=205, NO=200, η=0.97, u(NOₓ)=1.2, u(NO)=1.0, u(η)=0.01. Calcular con correlación 0 y 0.70 mediante plantilla. Explicar por qué incertidumbre relativa del NO₂ es grande.

**Producto:** tabla GPT, diagnóstico de línea, filas dominantes del presupuesto y conclusión máxima de 150 palabras.

## 5 Errores frecuentes y preguntas típicas

### 1:22 a 1:26; acumulado 1:26 (4 min)

- llamar “medición directa” a NO₂;
- aplicar corrección por η dos veces;
- tratar eficiencia y selectividad como sinónimos;
- asumir independencia de canales compartidos;
- usar límite de aceptación como incertidumbre estándar;
- ignorar residencia interna o externa;
- sumar fuentes ya incluidas en certificado o reproducibilidad;
- atribuir especificaciones NOx al APOA-370.

**Preguntas cortas:**

1. **¿Toda respuesta NOₓ adicional es NO₂?** No; convertidor puede responder a otras especies NOy.
2. **¿η=0.97 implica u(η)=0.03?** No; eficiencia y su incertidumbre son magnitudes distintas.
3. **¿Correlación positiva siempre reduce incertidumbre?** Reduce varianza de esta diferencia; efecto depende de signos del modelo.
4. **¿Anexo F fija presupuesto completo universal?** No; es ejemplo informativo y fuentes del sitio deben evaluarse.

## 6 Cierre y transición

### 1:26 a 1:30; acumulado 1:30 (4 min)

Lista oral:

1. ¿NO₂ fue medido o calculado?
2. ¿Eficiencia y selectividad se evaluaron por separado?
3. ¿Software ya corrige convertidor?
4. ¿Canales comparten fuentes y covarianza?
5. ¿Residencia incluye línea e instrumento?
6. ¿Criterios se separaron de incertidumbres estándar?

M7 integrará decisiones documentales, cálculo y validación. Transferencia clave: modelo debe representar arquitectura real antes de llenar presupuesto.
