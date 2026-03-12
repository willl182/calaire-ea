# Plan de Implementación: Correcciones CALAIRE-APP
## Basado en Informe No. 2 de Revisión — 2026-02-23

**Elaborado por:** Claude Sonnet 4.6
**Fecha:** 2026-03-06
**Fuente:** `docs/ajustes_app/Revisión aplicativo estadístico.pdf`
**Nota:** Este plan es agnóstico a la codebase. No asume lenguaje ni arquitectura específica.

---

## Resumen de Hallazgos

| # | Componente | Estado | Tipo |
|---|-----------|--------|------|
| 1 | Fórmula B.10 — varianza entre muestras (homogeneidad) | Error | Bloqueante |
| 2 | MADe — fuente de datos | Error | Bloqueante |
| 3 | Selector MADe/nIQR vs Algoritmo A (n >= 12) | Sin validar | Bloqueante |
| 4 | nIQR | Correcto | — |
| 5 | Estabilidad | Correcto | — |
| 6 | Algoritmo A | Sin datos para validar | Pendiente |
| 7 | Exportación CSV | Ilegible | Usabilidad |
| 8 | Zonas de carga separadas | Ausente | Usabilidad |

---

## Fase 1: Correcciones Estadísticas Bloqueantes

### 1.1 — Fórmula B.10: Varianza entre muestras (ss)

**Problema:**
El aplicativo aplica valor absoluto bajo la raíz en la fórmula B.10 de ISO 13528:2022.
La captura del informe muestra en Excel: `=SQRT(ABS((B32^2)-((B33^2)/2)))`.

La norma define la fórmula como:

```
s²_s = s²_{s,w} - s²_w = [1/(g-1)] * sum(x̄_t - x̄)² - (1/m) * s²_w
```

Y su nota dice explícitamente:
> "In the case that s²_s < 0, then it is appropriate to use s_s = 0."

No existe valor absoluto en la norma. El ABS enmascara el caso negativo en vez de detectarlo.

**Corrección requerida:**
```
si (s²_{s,w} - s²_w) < 0:
    s_s = 0
sino:
    s_s = sqrt(s²_{s,w} - s²_w)
```

**Criterio de salida:** Con datos donde el radicando sea negativo, el aplicativo retorna `s_s = 0`, no un valor positivo artificial.

---

### 1.2 — MADe: Fuente de datos incorrecta

**Problema:**
El aplicativo calcula MADe usando datos del módulo de homogeneidad. Debe usar exclusivamente datos de participantes.

**Evidencia numérica del informe:**

| Dataset usado | MADe resultante |
|--------------|----------------|
| Datos de homogeneidad (DATOS 1) | 0.0412 |
| Datos de homogeneidad (Datos 2) | 0.0473 |
| App (fuente no confirmada) | 0.0389 |
| Esperado (datos de participantes) | pendiente validar |

El informe también detectó ambigüedad en la selección de serie: el aplicativo usaba "Datos 2" de homogeneidad cuando el ejercicio debía trabajar con "DATOS 1". Esta ambigüedad desaparece si la fuente es correcta (participantes), pero la serie usada debe ser explícita y trazable.

**Corrección requerida:**
- MADe debe leer exclusivamente del dataset de participantes.
- La serie de datos usada debe quedar registrada como metadato.
- Eliminar cualquier ruta donde MADe, nIQR o Algoritmo A puedan recibir datos de homogeneidad.

**Criterio de salida:** Dado un dataset de participantes conocido, el valor de MADe del aplicativo coincide con el cálculo manual en Excel del revisor dentro de tolerancia de redondeo.

---

### 1.3 — Selector de método robusto: umbral n >= 12

**Problema:**
Según ISO 13528:2022, la selección del estadístico de dispersión robusto depende del tamaño muestral:

```
n < 12  ->  usar MADe y/o nIQR
n >= 12 ->  usar Algoritmo A
```

El informe señala que este switch no está verificado. El Algoritmo A no pudo validarse porque el revisor no recibió los datos que usó el aplicativo.

**Acciones requeridas:**

1. Confirmar que el selector existe y aplica el umbral n = 12.
2. Compartir con el revisor los datos de entrada del Algoritmo A para cierre de validación.
3. Mostrar en la interfaz qué método fue seleccionado y con qué n.

**Criterio de salida:**
- Con n = 11: el aplicativo usa MADe/nIQR y no invoca Algoritmo A.
- Con n = 12: el aplicativo usa Algoritmo A y no usa MADe/nIQR.
- Datos del Algoritmo A entregados al revisor.

---

## Fase 2: Trazabilidad y Modelo de Datos

### 2.1 — Separación explícita de datasets por origen

**Problema:**
No existe distinción clara entre tres tipos de datos en el modelo interno:

- Datos de **homogeneidad** (muestras del proveedor, replicados en laboratorio)
- Datos de **estabilidad** (seguimiento temporal)
- Datos de **participantes** (resultados reportados por los laboratorios en la ronda)

La mezcla entre homogeneidad y participantes es la causa raíz de los errores 1.2 y 1.3.

**Corrección requerida:**
- El modelo de datos debe etiquetar explícitamente el `origen_dato` de cada conjunto.
- Ningún cálculo de MADe, nIQR o Algoritmo A debe aceptar datos con `origen_dato = homogeneidad`.
- Validación de entrada: rechazar o advertir si se intenta usar la fuente incorrecta.

### 2.2 — Metadatos mínimos por corrida

Cada resultado calculado debe conservar:

| Metadato | Descripción |
|---------|-------------|
| `dataset_fuente` | Identificador del archivo/tabla de entrada |
| `serie_usada` | DATOS 1 / Datos 2 / identificador de serie |
| `n` | Número de datos usados |
| `metodo_robusto` | MADe / nIQR / Algoritmo A |
| `timestamp` | Fecha y hora de la corrida |
| `version_algoritmo` | Versión de las fórmulas implementadas |

Estos metadatos deben ser visibles en la interfaz y exportables.

---

## Fase 3: Usabilidad y Exportables

### 3.1 — Zonas de carga separadas

**Problema actual:**
El revisor no puede distinguir con facilidad qué datos corresponden a cada módulo.

**Corrección requerida:**
Tres zonas de carga independientes y claramente etiquetadas:

1. **Carga de Homogeneidad** -> alimenta cálculos B.10
2. **Carga de Estabilidad** -> alimenta cálculos de estabilidad
3. **Carga de Participantes** -> alimenta MADe, nIQR, Algoritmo A, score z

Cada zona debe mostrar una vista previa de los datos cargados antes de ejecutar cálculos.

### 3.2 — Tabla intermedia de cálculo visible

**Problema actual:**
El revisor no puede ver los datos intermedios usados en cada cálculo dentro del aplicativo sin exportar el CSV.

**Corrección requerida:**
Para cada módulo, exponer tabla que muestre datos de entrada, valores intermedios clave y resultado final.

Ejemplo mínimo para MADe:

| x_i | x_i - mediana | |x_i - mediana| |
|-----|--------------|---------------|
| ... | ... | ... |
| Mediana | | |
| Mediana de diferencias | | |
| MADe (x 1.4826) | | |

### 3.3 — Rediseño del CSV de exportación

**Problema actual:**
El CSV exportado es ilegible sin conocer la estructura:
```
co,corrida_1,0-µmol/mol,1,1,0.00670212766
```

**Corrección requerida:**
- Fila de encabezados con nombres descriptivos
- Una fila por dato de participante
- Columnas separadas para: `id_laboratorio`, `corrida`, `unidad`, `replica`, `valor`, `origen_dato`
- Columnas adicionales para resultados: `score_z`, `metodo_sigma`, `valor_sigma`
- El archivo debe ser legible en Excel sin transformaciones previas

---

## Fase 4: Validación Cruzada y Cierre

### 4.1 — Casos de prueba dorados

| Caso | n | Método esperado | Condición especial |
|------|---|-----------------|-------------------|
| A | 10 | MADe / nIQR | radicando B.10 positivo |
| B | 10 | MADe / nIQR | radicando B.10 negativo -> ss = 0 |
| C | 12 | Algoritmo A | caso estándar |
| D | 15 | Algoritmo A | con outlier |
| E | 10 | MADe / nIQR | con valor NA o vacío |

### 4.2 — Comparación app vs Excel del revisor

Para cada caso dorado:
- Ejecutar en el aplicativo
- Ejecutar en Excel de referencia (César)
- Diferencia aceptable: acordar con revisor (sugerido: <= 6 cifras significativas)

### 4.3 — Entrega de datos Algoritmo A al revisor

Acción pendiente bloqueante: exportar y compartir con César los datos exactos que el aplicativo usó en la corrida del Algoritmo A para que pueda completar la validación.

### 4.4 — Acta de cierre

- Resultado por caso de prueba (aceptado / rechazado / diferencia)
- Estado final de cada hallazgo del informe
- Firma de conformidad del revisor

---

## Dependencias entre Fases

```
1.1 (B.10)         --+
1.2 (fuente MADe)  --+--> 2.1 (separación datasets) --> 4.2 (validación cruzada)
1.3 (selector n)   --+         |
                               v
                          2.2 (metadatos)
                               |
                    3.1 + 3.2 + 3.3 (usabilidad) [puede ir en paralelo con Fase 2]
```

---

## Criterios Globales de Aceptación

- [ ] Con radicando negativo en B.10, el aplicativo retorna `s_s = 0`
- [ ] MADe, nIQR y Algoritmo A usan exclusivamente datos de participantes
- [ ] El selector `n < 12` / `n >= 12` es verificable y está cubierto por prueba
- [ ] Los metadatos de corrida son visibles y exportables
- [ ] El CSV es reproducible en Excel sin conocimiento previo del formato
- [ ] El revisor puede validar cualquier cálculo desde la interfaz sin extraer código
- [ ] Acta de validación cruzada completada

---

## Pendientes Abiertos (Antes de Iniciar Implementación)

1. **Datos Algoritmo A:** compartir con César los datos de entrada de la corrida actual para completar validación del módulo antes de tocar ese componente.
2. **Definición de serie de participantes:** aclarar si para MADe se usa la primera réplica, la segunda, o un promedio — y documentarlo como regla fija en el modelo.
3. **Tolerancia numérica:** acordar con César el número de cifras significativas aceptable para diferencias de redondeo entre app y Excel.
