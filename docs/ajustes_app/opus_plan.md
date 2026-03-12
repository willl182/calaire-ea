# Plan de Implementacion - Ajustes Aplicativo Estadistico CALAIRE-APP

**Fuente:** Informe No. 2 de revision (Cesar, 2026-02-23)
**Fecha del plan:** 2026-03-06
**Status:** draft

---

## Resumen de Hallazgos del Informe

El revisor tecnico (Cesar) evaluo los calculos del aplicativo contra la formulacion del Anexo B de la ISO 13528:2022 e identifico:

| # | Componente | Veredicto | Detalle |
|---|-----------|-----------|---------|
| H1 | Formula B.10 (homogeneidad) | ERROR | Cuando el radicando de ss^2 es negativo, el app usa valor absoluto (`ABS()`). La norma indica que ss = 0. |
| H2 | MADe - origen de datos | ERROR | Calcula MADe con datos de homogeneidad en vez de datos de participantes. |
| H3 | MADe - serie de datos | ERROR | Usa columna DATOS 1 cuando el ejercicio correspondia a DATOS 2. |
| H4 | Selector MADe/nIQR vs Algoritmo A | PENDIENTE | Para n >= 12 se debe usar Algoritmo A. Revisor no pudo validar por falta de datos. |
| H5 | nIQR | OK | Calculo correcto. |
| H6 | Estabilidad | OK | Calculo correcto. |
| H7 | Exportacion CSV | DEFICIENTE | Formato confuso, dificil de interpretar para validacion externa. |
| H8 | Interfaz de carga | DEFICIENTE | No hay separacion clara entre zonas de carga (homogeneidad, estabilidad, participantes). |
| H9 | Tablas de calculos intermedios | DEFICIENTE | No se puede acceder facilmente a los datos con los que se hicieron las corridas. |

---

## Fases de Implementacion

### Fase 1: Correcciones Estadisticas Criticas

Errores que invalidan resultados. Prioridad maxima.

#### 1.1 Formula B.10 - Varianza entre muestras (ss^2)

**Hallazgo:** H1
**Norma:** ISO 13528:2022, Anexo B, Formula B.10

```
ss^2 = ss,w^2 - sw^2 = (1/(g-1)) * SUM((x_t - x_bar)^2) - (1/m) * sw^2
```

**Regla:** Si ss^2 < 0, entonces ss = 0 (ver NOTE debajo de B.10 en la norma).

**Estado actual:** El aplicativo calcula `SQRT(ABS(radicando))`, lo cual produce un valor positivo ficticio.

**Correccion requerida:**
- Localizar la funcion que calcula ss (desviacion estandar entre muestras).
- Reemplazar `sqrt(abs(...))` por logica condicional:
  ```
  si radicando < 0:
      ss = 0
  sino:
      ss = sqrt(radicando)
  ```
- No usar `abs()` en ningun caso.

**Criterio de aceptacion:** Con los datos del informe, ss debe ser 0 cuando el radicando resulta negativo.

#### 1.2 MADe - Origen de datos

**Hallazgo:** H2, H3
**Norma:** ISO 13528:2022, Seccion 9

**Estado actual:** El aplicativo calcula MADe usando los datos de homogeneidad (10 muestras del estudio de homogeneidad).

**Correccion requerida:**
- MADe debe calcularse exclusivamente con los datos de los participantes.
- Verificar que la funcion de calculo de MADe reciba como entrada el dataset de participantes, no el de homogeneidad.
- Verificar que se use la serie de datos correcta (DATOS 1 o DATOS 2) segun corresponda a la corrida.

**Valores de referencia (del informe):**
- App actual (incorrecto): MADe = 0.0389 (usa datos homogeneidad, columna equivocada)
- Con DATOS 1 de homogeneidad: MADe = 0.041 (sigue siendo fuente incorrecta)
- Con DATOS 2 de homogeneidad: MADe = 0.0473 (sigue siendo fuente incorrecta)
- Valor correcto: debe calcularse con datos de participantes (pendiente de validar).

**Criterio de aceptacion:** MADe calculado con datos de participantes coincide con calculo manual en Excel del revisor.

#### 1.3 Selector de metodo robusto por tamano muestral

**Hallazgo:** H4
**Norma:** ISO 13528:2022, Seccion 9

**Regla:**
- n < 12 participantes: usar MADe o nIQR
- n >= 12 participantes: usar Algoritmo A

**Correccion requerida:**
- Implementar o verificar la logica de seleccion automatica basada en el conteo de participantes.
- Asegurar que el Algoritmo A este correctamente implementado (el revisor no pudo validarlo por falta de datos de entrada).
- Exponer en la interfaz que metodo se selecciono y por que.

**Criterio de aceptacion:** Con n=11 se usa MADe/nIQR; con n=12 se activa Algoritmo A. El usuario puede ver cual metodo se aplico.

---

### Fase 2: Separacion de Fuentes de Datos

Eliminar ambiguedad sobre que datos alimentan cada calculo.

#### 2.1 Aislamiento de datasets

**Hallazgos:** H2, H3

**Estado actual:** Los datos de homogeneidad, estabilidad y participantes no estan claramente separados en el flujo interno del aplicativo, lo que causa que calculos de dispersion (MADe/nIQR/Algoritmo A) tomen datos de la fuente equivocada.

**Correccion requerida:**
- Definir internamente tres conjuntos de datos independientes:
  - `datos_homogeneidad` (para calculos de Anexo B: ss, sw, criterio de homogeneidad)
  - `datos_estabilidad` (para calculos de estabilidad temporal)
  - `datos_participantes` (para MADe, nIQR, Algoritmo A y z-scores)
- Cada funcion de calculo debe declarar explicitamente de cual dataset se alimenta.
- Ninguna funcion de dispersion robusta debe poder acceder a `datos_homogeneidad`.

#### 2.2 Seleccion de serie (DATOS 1 / DATOS 2)

**Hallazgo:** H3

**Correccion requerida:**
- Si el dataset contiene multiples series (DATOS 1, DATOS 2), el usuario debe poder seleccionar cual serie usar por corrida.
- Registrar en metadatos de la corrida cual serie se selecciono.

---

### Fase 3: Usabilidad y Exportacion

Mejoras para facilitar la validacion externa.

#### 3.1 Separar zonas de carga en la interfaz

**Hallazgo:** H8

**Correccion requerida:**
- Tres areas de carga independientes y etiquetadas:
  1. Datos de homogeneidad
  2. Datos de estabilidad
  3. Datos de participantes
- Cada zona debe indicar que datos espera y en que formato.

#### 3.2 Tablas de calculos intermedios

**Hallazgo:** H9

**Correccion requerida:**
- Mostrar en pantalla (o en pestana accesible) los datos de entrada usados para cada calculo.
- Mostrar resultados intermedios: mediana, desviaciones absolutas, mediana de diferencias, etc.
- El revisor debe poder ver exactamente que valores entraron a cada formula.

#### 3.3 Exportacion CSV mejorada

**Hallazgo:** H7

**Estado actual:** El CSV exportado tiene formato confuso:
```
co,corrida_1,0-mol/mol,1,1,0.00670212766
```

**Correccion requerida:**
- Encabezados descriptivos en la primera fila.
- Columnas claramente identificadas (analito, corrida, unidad, replica, valor).
- Separador consistente.
- El archivo debe ser legible directamente al abrirlo en Excel sin manipulacion adicional.

---

### Fase 4: Validacion y Cierre

#### 4.1 Casos de prueba

Construir un set de validacion con:
- Caso con radicando negativo en B.10 (verificar ss = 0)
- Caso con n = 11 (verificar que usa MADe/nIQR)
- Caso con n = 12 (verificar que usa Algoritmo A)
- Caso con datos del informe de Cesar para comparacion directa
- Caso con valores NA o vacios

#### 4.2 Validacion cruzada con el revisor

- Compartir datos de entrada del Algoritmo A (solicitud pendiente de Cesar).
- Ejecutar app y Excel con los mismos datos.
- Documentar diferencias y tolerancias.

#### 4.3 Cierre formal

- Acta con resultado por hallazgo (H1-H9).
- Evidencia de que cada calculo coincide con referencia externa.

---

## Dependencias

| Dependencia | Estado | Bloquea |
|-------------|--------|---------|
| Acceso al repositorio de la app (R/Shiny) | Pendiente | Todas las fases |
| Datos del Algoritmo A para validacion | Pendiente (solicitud de Cesar) | Fase 1.3, Fase 4.2 |

## Normativa de Referencia

- ISO 13528:2022 - Metodos estadisticos para ensayos de aptitud (Anexo B, Seccion 9)
- ISO 17043:2023 - Evaluacion de la conformidad - Requisitos para ensayos de aptitud
