# Plan de Implementación de Ajustes del Aplicativo Estadístico

**Fecha:** 2026-03-07  
**Estado:** propuesto  
**Archivo fuente único:** `docs/ajustes_app/Revisión aplicativo estadístico.pdf`  
**Restricción de alcance:** este plan no revisa la codebase del aplicativo ni se apoya en otros planes previos.

---

## 1. Propósito

Definir una ruta de implementación funcional y documental para atender los hallazgos consignados en la revisión del aplicativo estadístico, dejando preparado un paquete de especificación suficiente para una etapa posterior de desarrollo técnico.

---

## 2. Hallazgos de partida

Del informe se desprenden seis frentes de intervención:

1. **Homogeneidad, fórmula B.10:** cuando el radicando resulte negativo, el valor operativo debe cerrarse en cero y no continuar con una raíz inválida.
2. **Cálculo de MADe:** el estimador se está alimentando con datos de homogeneidad, aunque debe construirse con datos de participantes.
3. **Regla metodológica por tamaño muestral:** si existen doce datos o más, debe utilizarse el Algoritmo A; en caso contrario, procede el estimador robusto aplicable.
4. **Trazabilidad de series utilizadas:** el informe identifica ambigüedad entre `DATOS 1` y `DATOS 2`, lo cual impide verificar qué serie fue realmente usada.
5. **Validación del Algoritmo A:** no se cuenta con la evidencia de datos de entrada ni con el detalle suficiente para contrastar externamente este cálculo.
6. **Comprensión y exportación de datos:** la estructura actual de carga o descarga no facilita la revisión técnica en Excel ni la lectura directa de los insumos.

---

## 3. Objetivo de implementación

Establecer, antes de cualquier intervención sobre el aplicativo, las reglas funcionales, los conjuntos de datos, los casos de validación y los requerimientos de auditabilidad necesarios para corregir los hallazgos con trazabilidad y respaldo técnico.

---

## 4. Alcance

### Incluye

- especificación de reglas de cálculo;
- definición del origen válido de cada dato;
- diseño de validaciones técnicas cruzadas;
- criterios de presentación y exportación de resultados;
- condiciones de cierre para cada hallazgo.

### No incluye

- revisión del repositorio o de archivos de código;
- implementación en R, Shiny u otra tecnología;
- pruebas automatizadas;
- despliegue o ajustes de infraestructura.

---

## 5. Principios de ejecución

1. La consistencia estadística prevalece sobre cualquier mejora de interfaz.
2. Cada resultado debe declarar de forma explícita el dataset del cual proviene.
3. Ningún hallazgo se considerará resuelto sin evidencia reproducible.
4. La validación externa debe poder ejecutarse sin interpretar supuestos ocultos.
5. La separación entre homogeneidad, estabilidad y participantes debe quedar formalmente establecida.

---

## 6. Fases del plan

### Fase 1. Formalización de reglas estadísticas

**Objetivo:** convertir los hallazgos del informe en reglas funcionales inequívocas.

**Actividades**
- Documentar la regla operativa de la fórmula B.10 para radicando negativo.
- Definir que MADe, nIQR y Algoritmo A se calculan con datos de participantes, no con datos de homogeneidad.
- Establecer la regla de decisión por tamaño muestral, dejando explícito el umbral `n >= 12`.
- Precisar qué debe entenderse por dato válido para el conteo de `n`.

**Entregable**
- Especificación funcional de reglas estadísticas.

**Criterio de cierre**
- Cada regla queda redactada sin ambigüedad y vinculada a un hallazgo concreto del informe.

### Fase 2. Definición de fuentes de datos y trazabilidad

**Objetivo:** eliminar mezclas de origen y asegurar reconstrucción completa de los cálculos.

**Actividades**
- Definir tres fuentes separadas: homogeneidad, estabilidad y participantes.
- Establecer un diccionario mínimo de campos para cada registro.
- Crear la regla documental para identificar la serie usada en cada corrida, incluyendo distinción inequívoca entre `DATOS 1` y `DATOS 2`.
- Definir cómo debe registrarse la relación entre analito, corrida, serie, unidad y resultado.

**Entregables**
- Diccionario de datos.
- Matriz de trazabilidad de cálculos.

**Criterio de cierre**
- Todo resultado puede rastrearse hasta su serie, dataset y contexto de cálculo.

### Fase 3. Diseño del protocolo de validación

**Objetivo:** preparar la verificación técnica independiente de los cálculos corregidos.

**Actividades**
- Diseñar casos de prueba para B.10 con radicando positivo y negativo.
- Diseñar casos para MADe calculado con datos correctos de participantes.
- Incluir escenarios de borde con `n = 11` y `n = 12`.
- Definir el caso de validación específico para Algoritmo A con evidencia de entradas, iteraciones y resultado final.
- Incluir condiciones de datos faltantes, series erróneas y selección equivocada de fuente.

**Entregables**
- Matriz de casos de validación.
- Formato de registro de resultados observados vs. esperados.

**Criterio de cierre**
- Cada hallazgo crítico dispone de al menos un caso de validación independiente.

### Fase 4. Requerimientos de auditabilidad y revisión externa

**Objetivo:** asegurar que la futura solución permita revisión técnica comprensible.

**Actividades**
- Definir que la carga de datos de homogeneidad, estabilidad y participantes permanezca separada.
- Especificar tablas mínimas para visualizar entradas, resultados intermedios y resultados finales.
- Definir un formato de exportación legible para revisión en Excel.
- Establecer encabezados, nombres de columnas y metadatos mínimos para eliminar ambigüedad.

**Entregables**
- Especificación de tablas de revisión.
- Especificación de exportables de auditoría.

**Criterio de cierre**
- Un revisor externo puede reconstruir los cálculos sin depender de interpretación adicional.

### Fase 5. Consolidación y preparación para implementación futura

**Objetivo:** dejar un paquete de implementación listo para trasladarse posteriormente a desarrollo.

**Actividades**
- Consolidar hallazgos, reglas, datos, validaciones y requisitos de salida en un solo paquete documental.
- Clasificar cada hallazgo como cerrado, pendiente o condicionado.
- Identificar riesgos residuales antes de abrir una etapa de desarrollo.
- Definir prerrequisitos mínimos para iniciar implementación sobre la aplicación.

**Entregables**
- Checklist de cierre técnico.
- Documento de prerrequisitos de implementación.

**Criterio de cierre**
- Existe un paquete documental completo, revisable y utilizable por un equipo técnico sin vacíos funcionales críticos.

---

## 7. Priorización

| Prioridad | Frente | Motivo |
|---|---|---|
| Alta | Corrección de B.10 | Compromete la validez del cálculo de homogeneidad |
| Alta | Reasignación de fuente para MADe | Introduce error metodológico en la desviación robusta |
| Alta | Regla `n >= 12` para Algoritmo A | Puede producir selección estadística incorrecta |
| Media | Trazabilidad `DATOS 1` / `DATOS 2` | Afecta verificabilidad y reproducibilidad |
| Media | Evidencia de Algoritmo A | Impide validación externa completa |
| Media | Exportación y visualización de datos | Dificulta auditoría y revisión técnica |

---

## 8. Riesgos del proceso

| Riesgo | Impacto | Control propuesto |
|---|---|---|
| Mantener mezcla entre datos de homogeneidad y participantes | Persistencia del error metodológico | Diccionario de datos y regla obligatoria de origen por estadístico |
| Corregir fórmulas sin evidencia de validación | Cierre falso de hallazgos | Matriz de casos con resultados esperados y observados |
| Implementar sin resolver ambigüedad de series | Baja trazabilidad de resultados | Registro obligatorio de serie y corrida en cada cálculo |
| Entregar salidas poco legibles | Revisión externa ineficiente | Especificación mínima de tablas y exportables |

---

## 9. Secuencia recomendada

1. Formalizar reglas estadísticas.
2. Definir fuentes de datos y trazabilidad.
3. Diseñar protocolo de validación.
4. Establecer requisitos de auditabilidad y exportación.
5. Consolidar el paquete final para futura implementación.

---

## 10. Condición de salida

El plan se considerará cumplido cuando exista una especificación funcional completa que permita a un equipo de desarrollo intervenir posteriormente el aplicativo con estos elementos ya cerrados:

- reglas estadísticas corregidas;
- datasets y series definidos sin ambigüedad;
- validaciones cruzadas diseñadas;
- requisitos de revisión externa documentados;
- criterios formales de cierre por hallazgo.

---

## 11. Referencia base

- `docs/ajustes_app/Revisión aplicativo estadístico.pdf`
