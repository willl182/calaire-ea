# Plan: Implementación de Correcciones Estadísticas CALAIRE-APP

**Created**: 2026-03-06
**Updated**: 2026-03-06
**Status**: draft
**Slug**: glm47-plan-implementacion
**Source**: Revisión aplicativo estadístico.pdf (Informe No. 2, César Yate, 2026-02-23)

---

## Objetivo

Corregir errores en los cálculos estadísticos del aplicativo CALAIRE-APP identificados en el Informe No. 2 y mejorar la usabilidad para facilitar la validación técnica externa.

---

## Resumen de Hallazgos

### Errores Confirmados (Bloqueantes)

**1. Fórmula B.10 (Homogeneidad) - ISO 13528:2022 Anexo B**
- **Problema**: Error en el cálculo de la desviación estándar entre muestras
- **Causa**: La fórmula B.10 no incluye valor absoluto; cuando la raíz cuadrada es negativa, el resultado es incorrecto
- **Corrección**: Si radicando < 0 → `ss = 0`

**2. MADe - Fuente de datos incorrecta**
- **Problema**: El aplicativo calcula MADe usando datos de homogeneidad en lugar de datos de participantes
- **Evidencia**: App reportó MADe = 0.0389; cálculo correcto con participantes = 0.041 o 0.0473
- **Corrección**: Usar exclusivamente datos de los participantes para MADe

**3. Selector de método robusto - Regla faltante**
- **Problema**: Falta implementación de la regla de cambio de algoritmo
- **Corrección**: n < 12 → MADe/nIQR; n ≥ 12 → Algoritmo A (ISO 13528:2022 Sección 9)

### Cálculos Correctos
- ✅ nIQR: Correcto
- ✅ Estabilidad: Correcta

### Validación Pendiente
- **Algoritmo A**: Requiere datos de entrada y resultados intermedios para validación cruzada

---

## Fases de Implementación

### Fase 1: Correcciones de Cálculo (Bloqueantes)

**Objetivo**: Corregir errores que comprometen la validez técnica de los resultados

#### 1.1 Fórmula B.10 - Desviación estándar entre muestras

**Archivo/Componente**: Lógica de cálculo de homogeneidad

**Corrección**:
```pseudocode
# Versión actual (INCORRECTA)
ss = sqrt((sum((xi - x_bar)^2) / (m - 1)) - (ss_within / m))

# Corrección requerida
radicando = (sum((xi - x_bar)^2) / (m - 1)) - (ss_within / m)
if radicando < 0:
    ss = 0
else:
    ss = sqrt(radicando)
```

**Criterio de aceptación**:
- Caso de prueba con radicando negativo retorna `ss = 0`
- Caso de prueba con radicando positivo retorna valor correcto
- Cumple ISO 13528:2022 Anexo B, B.10

#### 1.2 MADe - Fuente de datos

**Archivo/Componente**: Lógica de cálculo de métodos robustos

**Corrección**:
- Identificar origen actual de datos (homogeneidad DATOS 1)
- Reemplazar con origen correcto (participantes DATOS 1/DATOS 2)
- Eliminar cualquier referencia a datos de homogeneidad en cálculo MADe

**Criterio de aceptación**:
- MADe calculado con datos de participantes coincide con cálculo manual
- Serie 1 de 10 datos: MADe ≈ 0.041
- Serie 2 de 10 datos: MADe ≈ 0.0473
- Cumple ISO 13528:2022 Sección 9

#### 1.3 Selector de método robusto por tamaño muestral

**Archivo/Componente**: Lógica de selección de algoritmo

**Corrección**:
```pseudocode
n = length(datos_participantes)

if n < 12:
    usar_metodo = "MADe/nIQR"
else:
    usar_metodo = "Algoritmo A"
```

**Criterio de aceptación**:
- Caso n=11: usa MADe/nIQR
- Caso n=12: usa Algoritmo A
- Caso n=10: usa MADe/nIQR
- Cumple ISO 13528:2022 Sección 9

#### 1.4 Validaciones defensivas

**Archivo/Componente**: Capa de validación de datos de entrada

**Añadir validaciones**:
- Verificar que datos de homogeneidad y participantes no se mezclan
- Manejo robusto de valores NA/vacíos sin interrumpir corrida
- Validación de tipos de datos (numéricos)
- Alertas cuando n < 10 (tamaño mínimo recomendado)

**Criterio de aceptación**:
- Corrida no se rompe con datos incompletos
- Alertas claras cuando se detectan anomalías en datos
- Logs detallados de origen de datos por cálculo

---

### Fase 2: Trazabilidad y Modelo de Datos

**Objetivo**: Eliminar ambigüedad en origen de datos y garantizar auditabilidad

#### 2.1 Esquema de entrada estandarizado

**Componente**: Interfaz de carga de datos

**Acciones**:
1. Definir campos obligatorios en dataset de entrada:
   - `origen_dato`: "homogeneidad" | "estabilidad" | "participantes"
   - `serie_dato`: "DATOS 1" | "DATOS 2" | "DATOS 3"
   - `fecha_carga`: timestamp
   - `metadatos`: contexto adicional (ej: número de corrida)

2. Validación en carga:
   - Rechazar archivos sin `origen_dato`
   - Alertar si `origen_dato` no coincide con zona de carga

**Criterio de aceptación**:
- Todos los datasets incluyen `origen_dato`
- Validación impide mezcla involuntaria de fuentes

#### 2.2 Selección de serie formalizada

**Componente**: Configuración de cálculo

**Acciones**:
1. Crear mecanismo explícito de selección de serie (DATOS 1/DATOS 2/DATOS 3)
2. Registrar en metadatos de corrida:
   - Serie seleccionada
   - Timestamp de selección
   - Usuario que realizó selección

**Criterio de aceptación**:
- Selección de serie es explícita y auditable
- Historial de cambios por corrida está disponible

#### 2.3 Metadatos de corrida persistentes

**Componente**: Sistema de almacenamiento de resultados

**Acciones**:
1. Cada resultado calculado debe incluir:
   - `dataset_fuente`: identificador de archivo/serie
   - `serie_usada`: DATOS 1/DATOS 2/DATOS 3
   - `origen_dato`: homogeneidad/estabilidad/participantes
   - `timestamp_calculo`: fecha/hora
   - `version_algoritmo`: versión del código de cálculo
   - `parametros_usados`: n, método seleccionado, etc.

**Criterio de aceptación**:
- Todos los resultados son trazables a origen exacto
- Auditoría externa puede reproducir cualquier cálculo

---

### Fase 3: Usabilidad Técnica y Exportables

**Objetivo**: Mejorar comprensión de datos y facilitar validación externa

#### 3.1 Interfaz de carga separada

**Componente**: UI de carga de datos

**Acciones**:
1. Separar en 3 zonas independientes:
   - Zona 1: Carga de datos de homogeneidad
   - Zona 2: Carga de datos de estabilidad
   - Zona 3: Carga de datos de participantes

2. Cada zona:
   - Indicador visual de origen de dato
   - Validación específica por tipo
   - Previsualización de datos cargados
   - Etiquetas claras (ej: "Cargar datos de homogeneidad (Anexo B)")

**Criterio de aceptación**:
- Usuario entiende claramente qué datos carga en cada zona
- No existe confusión entre datos de homogeneidad y participantes

#### 3.2 Tablas intermedias visibles

**Componente**: Visualización de resultados

**Acciones**:
1. Crear sección de "Tabla de Cálculos Intermedios"
2. Para cada cálculo (homogeneidad, estabilidad, métodos robustos):
   - Mostrar datos de entrada
   - Mostrar resultados intermedios (ej: desviaciones absolutas)
   - Mostrar resultado final
   - Indicar origen de datos (homogeneidad/participantes)
   - Incluir valores de referencia cuando aplique

**Criterio de aceptación**:
- Revisor técnico puede validar cada paso del cálculo
- Origen de datos es explícito por cálculo

#### 3.3 Exportación CSV rediseñada

**Componente**: Generación de exportables

**Problema actual**:
```
co,corrida_1,0-µmol/mol,1,1,0.00670212766
```

**Acciones**:
1. Nuevo formato estructurado:
   - Archivo separado por tipo de dato (homogeneidad, estabilidad, participantes)
   - Headers descriptivos
   - Valores separados por coma estándar
   - Incluir metadatos de corrida

2. Ejemplo de nuevo formato:
```csv
# Corrida 1 - Datos de Participantes - DATOS 1
# Timestamp: 2026-02-23 14:30:00
# Método robusto: MADe/nIQR (n=11)
columna,valor
DATOS_1,0.006702128
DATOS_2,0.004787234
...

# Resultados Calculados
parametro,valor,origen_dato,metodo
mediana,-0.047,participantes,MADe
MADe,0.041,participantes,MADe
nIQR,<valor>,participantes,nIQR
```

**Criterio de aceptación**:
- CSV es legible en Excel sin confusión
- Estructura clara permite validar cálculo manual
- Incluye metadatos necesarios para auditoría

---

### Fase 4: Validación Cruzada y Cierre

**Objetivo**: Confirmar equivalencia técnica y cerrar hallazgos

#### 4.1 Casos de prueba dorados

**Acciones**:
1. Construir dataset de referencia con casos:
   - n=10, método MADe/nIQR
   - n=11, método MADe/nIQR
   - n=12, método Algoritmo A
   - Caso extremo (radicando negativo en B.10)
   - Caso con NA/vacíos
   - Series múltiples (DATOS 1, DATOS 2, DATOS 3)

2. Validar cada caso con cálculo manual (Excel) de referencia

**Criterio de aceptación**:
- Cobertura ≥ 6 casos representativos
- Valores de referencia documentados

#### 4.2 Comparación App vs Excel

**Acciones**:
1. Ejecutar corrida con casos dorados en CALAIRE-APP
2. Comparar cada resultado con cálculo manual de César
3. Documentar diferencias y tolerancias aceptables (ej: ±0.0001 para valores pequeños)

**Criterio de aceptación**:
- Todas las diferencias dentro de tolerancia definida
- César valida resultados como equivalentes

#### 4.3 Acta de validación consolidada

**Acciones**:
1. Crear documento "Acta de Validación de Correcciones - CALAIRE-APP"
2. Incluir:
   - Resumen de correcciones aplicadas
   - Resultados por caso de prueba
   - Comparación App vs Excel
   - Decisión: Aceptado/Rechazado
   - Firma de validador (César Yate)
   - Fecha de validación

**Criterio de aceptación**:
- Acta firmada y documentada
- Todos los hallazgos del Informe No. 2 cerrados

#### 4.4 Checklist de cierre

**Acciones**:
1. Verificar cierre de cada hallazgo del Informe No. 2

| Hallazgo | Estado | Evidencia |
|---------|--------|-----------|
| B.10 radicando negativo | Cerrado | Caso de prueba validado |
| MADe fuente incorrecta | Cerrado | Comparación con datos participantes |
| Selector n ≥ 12 | Cerrado | Casos n=11 y n=12 validados |
| Algoritmo A | Pendiente | Datos compartidos con César |

**Criterio de aceptación**:
- Checklist completo
- Evidencias documentadas

---

## Referencias Normativas

- **ISO 13528:2022** - Statistical methods for use in proficiency testing by interlaboratory comparison
  - Anexo B: Homogeneity testing
  - Sección B.10: Standard deviation between samples
  - Sección 9: Robust statistics
- **ISO 17043:2023** - Conformity assessment — Proficiency testing
- **NTC ISO/IEC 17025:2017** - General requirements for the competence of testing and calibration laboratories

---

## Criterios Globales de Aceptación

1. **Exactitud matemática**: Todos los cálculos corregidos coinciden con referencia externa en casos controlados
2. **No mezcla de fuentes**: No existe ruta donde MADe/nIQR/Algoritmo A use datos de homogeneidad
3. **Umbral n ≥ 12**: Regla de cambio de algoritmo cubierta por pruebas y evidencia
4. **Trazabilidad completa**: Todas las corridas incluyen metadatos mínimos de origen y contexto
5. **Auditoría externa**: Exportables permiten validar cálculos sin ambigüedad
6. **Validación cruzada**: César Yate confirma equivalencia técnica de resultados

---

## Riesgos y Mitigación

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| Mezcla de datasets en capas intermedias | Media | Alto | Validación estricta de esquema y tipado de origen |
| Ausencia de dataset patrón para Algoritmo A | Media | Medio | Congelar set dorado para regresión |
| Despliegue prematuro sin validación cruzada | Baja | Crítico | Gate de liberación condicionado a acta de validación |
| Degradación de usabilidad con correcciones técnicas | Baja | Bajo | Pruebas de usabilidad con revisores técnicos |

---

## Dependencias Externas

1. **Validación cruzada con César Yate**: Requiere coordinación para compartir datos de Algoritmo A
2. **Acceso a datos de homogeneidad/participantes**: Confirmar estructura actual de datasets
3. **Validación de casos dorados**: César debe validar cálculos manuales de referencia

---

## Log de Ejecución

- [ ] Fase 1 iniciada
- [ ] Fase 1 completada
- [ ] Fase 2 iniciada
- [ ] Fase 2 completada
- [ ] Fase 3 iniciada
- [ ] Fase 3 completada
- [ ] Fase 4 iniciada
- [ ] Fase 4 completada

---

## Anexo: Evidencias del Informe No. 2

### Evidencia 1: MADe Incorrecto con Datos de Homogeneidad

```
App reportó: MADe = 0.0389

Cálculo correcto con participantes (Serie 1):
- Mediana: -0,022837013
- Desviaciones absolutas: [0,029539, 0,027624, 0,026446, 0,027092, 0,028858, 0,029427, 0,02605, 0,027918, 0,029125, 0,02605]
- Mediana de diferencias: 0,027771
- MADe = 0,041184

Diferencia: 0.041 - 0.0389 ≈ 0.002 (5% error)
```

### Evidencia 2: Ambigüedad de Serie de Datos

```
App usó: Primeros 10 datos de homogeneidad DATOS 1
Debió usar: DATOS 2 (según contexto del ejercicio)
```

### Evidencia 3: Problema de Usabilidad en CSV

```
Formato actual (confuso):
co,corrida_1,0-µmol/mol,1,1,0.00670212766

Problema: No es posible identificar estructura de datos ni origen
```
