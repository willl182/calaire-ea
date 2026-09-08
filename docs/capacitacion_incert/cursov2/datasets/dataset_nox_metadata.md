# Metadatos — datasets sintéticos M6 NOx

## Identificación

- Archivos: `dataset_nox_gpt_convertidor.csv` y `dataset_nox_linea_muestreo.csv`.
- Naturaleza: datos enteramente sintéticos para enseñanza. No describen desempeño, calibración ni aceptación de equipo comercial.
- Generador: `generar_dataset_nox.R`.
- Semilla reproducible: `20260819`.
- Fecha base simulada: 2026-08-19, UTC.
- Unidades (defecto D7): todas las fracciones molares se expresan en **nmol/mol**; no usar ppb en hojas de campo ni plantillas derivadas de este dataset (BIPM.QM-K1 §4 desaconseja ppb/ppbv).
- El dataset original de GPT (niveles NO₂ 0–150 nmol/mol sobre NO base ≈160 nmol/mol) tiene el defecto de titulación profunda D4: NO residual en el nivel más alto queda en solo ≈6 % del NO inicial. La escalera corregida y validada está en `practica/E04_gpt_eficiencia_convertidor.md` (NO base 450 nmol/mol, niveles GPT 0–160 nmol/mol, NO residual mínimo 290 nmol/mol). Use ese protocolo, no el dataset original, para cualquier ejercicio cuantitativo sobre eficiencia del convertidor.

## Dataset GPT y convertidor

Contiene tres ciclos, cada uno con cero y cuatro niveles de NO₂ generado, para 15 filas. Concentraciones se expresan en nmol/mol salvo concentración del cilindro de NO, expresada en µmol/mol. Flujos conservan unidades indicadas en nombres de columnas.

Ecuaciones didácticas principales:

\[
c_{NO,gen}=c_{cil}\frac{q_{NO}}{q_{dil}+q_{NO}}
\]

con unidades de flujo convertidas antes de operar, y

\[
c_{NO_2,ind}=c_{NO_x}-c_{NO}=b+\eta c_{NO_2,GPT}+\varepsilon.
\]

Eficiencia sintética nominal inicia cerca de 0.972 y disminuye 0.0015 por ciclo. El término fijo de +0.35 nmol/mol en el canal NOx representa un sesgo residual del canal y explica que la pendiente ajustada no coincida exactamente con η. Ruido común agregado a canales NO y NOₓ introduce correlación positiva deliberada; ruido específico de cada canal se suma después. Esta construcción permite comparar propagación independiente frente a propagación con covarianza.

Temperatura, presión y flujos tienen incertidumbres estándar didácticas precargadas. Deliberadamente, `u_flujo_no_ml_min=0.08`, `u_temperatura_K=0.20` y `u_presion_kPa=0.10` no coinciden con las desviaciones estándar usadas para simular variación fila a fila (0.10 mL/min, 0.18 K y 0.08 kPa): las primeras son entradas declaradas del ejercicio y las segundas controlan la dispersión sintética. En filas de nivel cero, `flujo_no_ml_min=0`, coherente con la ecuación de generación. `no2_gpt_nmol_mol` representa valor generado ya calculado para ejercicio corto; flujo de O₃ sirve como variable de diagnóstico, no como modelo cinético completo.

> **Corrección de dimensionamiento (defecto D5):** la columna `impureza_no2_nmol_mol=0.40` está mal dimensionada como valor de cilindro. Para un cilindro de NO cercano a 40 µmol/mol, una estimación de planificación realista de 1 % molar de NO₂ respecto al NO es `0.01×40 µmol/mol=400 nmol/mol` en el cilindro, que tras una dilución típica 1:250 da `400/250=1.6 nmol/mol` en la mezcla final. El valor `0.40` es 1000 veces menor que el valor de planificación correcto en cilindro (`0.40 µmol/mol`). Para el rediseño de GPT con cilindro de 50 µmol/mol (`practica/E04_gpt_eficiencia_convertidor.md`), el mismo supuesto de 1 % da 500 nmol/mol en cilindro y, a la fracción de dilución `45/5000=0.009`, `I_mezcla=4.50 nmol/mol` — no despreciable frente al intercepto GPT. El valor operativo debe tomarse siempre del certificado real del cilindro, con incertidumbre y fecha; el 1 % es solo un supuesto conservador de diseño, no un sustituto de certificado.

## Dataset de línea de muestreo

Tres configuraciones comparan línea corta, línea larga y línea larga caliente. Tiempo externo se obtiene de volumen/caudal y se suma a tiempo interno declarado. Formación estimada de NO₂ aumenta relativamente con tiempo de residencia y temperatura. Sus magnitudes son puramente ilustrativas y no representan una simulación cinética ni datos experimentales de Doval Miñarro et al. (2011); solo preservan una dependencia relativa coherente entre configuraciones.

> **Advertencia (defecto D6):** los valores de NO₂ formado del dataset original (A=0.18, B=0.43, C=0.62 nmol/mol) subestiman en 70–100× la predicción de cinética de segundo orden NO+O₃ (`k=1.8×10⁻¹⁴ cm³ molécula⁻¹ s⁻¹`) para las mismas geometrías, caudales y temperaturas: el cálculo corregido da A=18.45, B=42.43, C=45.13 nmol/mol. No se regeneró este dataset: sigue sirviendo al ejercicio documental de M6 Parte B, cuyo objeto es practicar la decisión operativa, no predecir magnitudes. Para cualquier afirmación cuantitativa sobre formación real de NO₂ en línea, use los valores recalculados de `practica/E07_formacion_no2_linea.md`, que es un experimento independiente de la práctica de laboratorio.

Criterio didáctico de 2 % separa decisiones del ejercicio. No es límite normativo universal. Participante debe distinguir aceptar, corregir, repetir o invalidar según objetivo y procedimiento aplicable.

## Condiciones de referencia y correlaciones

- Base de cantidad: fracción molar.
- Temperatura y presión se registran para exigir base coherente de caudales; generador no aplica corrección adicional porque datos simulados ya comparten base.
- Correlación positiva entre canales procede de término de ruido común. No inferir mismo coeficiente en equipo real.
- Ceros, patrones y niveles no sustituyen certificado ni ensayo GPT trazable.

## Fuentes y límites

- BS EN 14211:2012: principio de medición, converter, GPT y ejemplo informativo de incertidumbre.
- Doval Miñarro et al. (2011): mecanismo de formación NO₂ en línea y papel de residencia.
- GUM/JCGM 100: propagación y covarianza.

Anexo F de EN 14211 fue consultado para estructura y números del presupuesto; texto se parafrasea. Dataset no copia tabla normativa. Validar edición aplicable y requisitos colombianos antes de uso operativo.

## Control documental

HORIBA APOA-370 es analizador de O₃ por absorción UV, no analizador NOx. El manual local `APNA-370_Operaton_Manual_GZ9100497232L.pdf` corresponde a un HORIBA Ambient NOx Monitor (2021) y está disponible como fuente. Verificar si APNA-370 es el equipo realmente instalado queda a cargo del operador. Ninguna especificación del APOA-370 se usa aquí como especificación NOx.
