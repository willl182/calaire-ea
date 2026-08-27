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

## 3. Guion de exposición con tiempos

El libreto de exposición está organizado en páginas/diapositivas Markdown independientes. Cada página conserva el texto dictable, el minutaje y sus apoyos; este apartado funciona como índice.

1. [M6 — Página 01 — 3.1 Qué mide analizador NOx — 0:00 a 0:12; acumulado 0:12 (12 min)](../paginas/M6_01_3_1_que_mide_analizador_nox_0_00_a_0_12_acumulado_0_12_12_min.md)
2. [M6 — Página 02 — 3.2 Modelo, convertidor y covarianza — 0:12 a 0:27; acumulado 0:27 (15 min)](../paginas/M6_02_3_2_modelo_convertidor_y_covarianza_0_12_a_0_27_acumulado_0_27_15_min.md)
3. [M6 — Página 03 — 3.3 Fuentes específicas — 0:27 a 0:47; acumulado 0:47 (20 min)](../paginas/M6_03_3_3_fuentes_especificas_0_27_a_0_47_acumulado_0_47_20_min.md)
4. [M6 — Página 04 — 3.4 Presupuesto informativo EN 14211 — 0:47 a 1:02; acumulado 1:02 (15 min)](../paginas/M6_04_3_4_presupuesto_informativo_en_14211_0_47_a_1_02_acumulado_1_02_15_min.md)

## 4 Ejercicio/actividad — 1:02 a 1:22; acumulado 1:22 (20 min)

**Nombre:** Diagnóstico GPT, convertidor y línea de muestra.

**Organización:** parejas. Una persona calcula; otra audita unidades, fuentes, correcciones y decisiones. Cambiar roles después de 10 min.

> **Advertencia sobre el dataset de GPT (defecto D4):** el diseño original de titulación dejaba NO residual ≈10 nmol/mol en el nivel más alto (≈6 % del NO inicial), margen demasiado estrecho. La escalera rediseñada y validada en `practica/E04_gpt_eficiencia_convertidor.md` usa NO base 450 nmol/mol y niveles GPT 0–160 nmol/mol, dejando NO residual mínimo de 290 nmol/mol (64.4 % del NO inicial). Use los valores recalculados de ese protocolo, no los del dataset original, al interpretar eficiencia.

> **Advertencia sobre el dataset de línea NOx (defecto D6):** los valores de NO₂ formado en línea del dataset original (0.18–0.62 nmol/mol) subestiman la cinética NO+O₃ en 70–100×; el cálculo corregido con `k=1.8×10⁻¹⁴ cm³ molécula⁻¹ s⁻¹` da 18.45–45.13 nmol/mol para las mismas configuraciones. Ver protocolo real `practica/E07_formacion_no2_linea.md` y la sección "Cálculos correctivos" de su diseño. La Parte B del ejercicio siguiente conserva su dataset y su propósito didáctico (practicar la decisión operativa); úsese esta advertencia para explicar en clase que el nivel absoluto es ilustrativo y no predice el resultado de laboratorio, que se obtiene por separado en E07.

**Enlace con la práctica:** el Día 2 de laboratorio trata con instrumento real los mismos temas de este módulo, como bloque independiente y sin reemplazar los ejercicios de esta sección: `practica/E03_covarianza_no_nox.md` mide la covarianza NO/NOx que la Parte C usa como dato; `practica/E04_gpt_eficiencia_convertidor.md` y `practica/E05_correccion_firmware.md` corresponden a la Parte A; `practica/E07_formacion_no2_linea.md` corresponde a la Parte B.

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
