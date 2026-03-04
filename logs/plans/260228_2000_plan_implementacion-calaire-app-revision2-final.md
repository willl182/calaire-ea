# Plan: Implementacion Final CALAIRE-APP Revision 2

**Created**: 2026-02-28 20:00
**Updated**: 2026-02-28 20:00
**Status**: approved
**Slug**: implementacion-calaire-app-revision2-final

---

## Objetivo

Definir un plan final, ejecutable por un agente tecnico en el repositorio del modelo, para disenar e implementar las correcciones estadisticas y de trazabilidad del aplicativo [[CALAIRE-APP]] conforme a los hallazgos del Informe de Revision No. 2 y los criterios de [[QMS]].

---

## Alcance y Prioridad

1. Corregir logica estadistica bloqueante (B.10, MADe, seleccion de metodo robusto).
2. Eliminar ambiguedad de origen de datos (homogeneidad, estabilidad, participantes).
3. Garantizar trazabilidad completa por corrida y reproducibilidad externa.
4. Mejorar flujo de carga y exportables para validacion con revisor externo (Excel).
5. Cerrar validacion tecnica con evidencia verificable.

---

## Reglas Tecnicas Obligatorias

1. **Homogeneidad B.10:** si el radicando es negativo, forzar `ss = 0`.
2. **MADe/nIQR/Algoritmo A:** calcular exclusivamente con datos de participantes.
3. **Switch por tamano muestral:** `n < 12` usa MADe/nIQR; `n >= 12` usa Algoritmo A.
4. **Trazabilidad minima por resultado:** dataset fuente, serie usada, timestamp y version de algoritmo.

---

## Fases

### Fase 0: Descubrimiento Tecnico del Repositorio Objetivo

**Objetivo:** mapear arquitectura real antes de proponer cambios de codigo.

| # | Entregable | Accion | Descripcion |
|---|------------|--------|-------------|
| 0.1 | Mapa de modulos | Identificar | Localizar calculos de homogeneidad, robustos, carga de datos y exportacion |
| 0.2 | Inventario de funciones | Documentar | Listar funciones candidatas a ajuste y sus dependencias |
| 0.3 | Flujo end-to-end | Trazar | Describir pipeline `carga -> calculo -> visualizacion -> exportacion` |

### Fase 1: Correcciones Estadisticas Bloqueantes

**Objetivo:** corregir errores que comprometen validez tecnica.

| # | Componente | Accion | Criterio de salida |
|---|-----------|--------|--------------------|
| 1.1 | Formula B.10 | Corregir | Caso de radicando negativo retorna `ss = 0` |
| 1.2 | MADe | Corregir | MADe usa solo dataset de participantes |
| 1.3 | Selector de metodo robusto | Implementar/Verificar | `n=11` aplica MADe/nIQR y `n=12` activa Algoritmo A |
| 1.4 | Validaciones defensivas | Endurecer | Manejo de NA, vacios y tipos invalidos sin romper corrida |

### Fase 2: Trazabilidad y Modelo de Datos

**Objetivo:** evitar mezcla de fuentes y garantizar auditabilidad.

| # | Componente | Accion | Criterio de salida |
|---|-----------|--------|--------------------|
| 2.1 | Esquema de entrada | Estandarizar | Campo `origen_dato` obligatorio y validado |
| 2.2 | Seleccion de serie | Formalizar | Regla explicita para DATOS 1/DATOS 2 con registro en metadatos |
| 2.3 | Metadatos de corrida | Persistir | Cada resultado conserva dataset, serie y version de calculo |

### Fase 3: Usabilidad Tecnica y Exportables

**Objetivo:** mejorar lectura operativa y capacidad de replica externa.

| # | Componente | Accion | Criterio de salida |
|---|-----------|--------|--------------------|
| 3.1 | Interfaz de carga | Separar | Tres zonas independientes: homogeneidad, estabilidad y participantes |
| 3.2 | Tablas intermedias | Exponer | Visualizacion clara de datos de entrada y resultados intermedios |
| 3.3 | Exportacion CSV | Redisenar | Archivo legible, consistente y reproducible en Excel |

### Fase 4: Validacion Cruzada y Cierre

**Objetivo:** confirmar equivalencia tecnica y cerrar hallazgos.

| # | Componente | Accion | Criterio de salida |
|---|-----------|--------|--------------------|
| 4.1 | Casos de prueba dorados | Construir | Cobertura minima: `n=11`, `n=12`, extremos, NA y series multiples |
| 4.2 | Comparacion App vs Excel | Ejecutar | Diferencias dentro de tolerancia definida |
| 4.3 | Acta de validacion | Consolidar | Resultado por caso con decision de aceptacion/rechazo |
| 4.4 | Checklist de cierre | Completar | B.10, MADe, selector, trazabilidad y exportables en estado cerrado |

---

## Instrucciones para el Agente Implementador (Repositorio del Modelo)

1. No iniciar por UI: cerrar primero exactitud matematica y origen de datos.
2. Entregar propuesta de cambios por archivo/funcion antes de modificar codigo.
3. Implementar pruebas unitarias por formula y una prueba de integracion del flujo completo.
4. Mantener evidencia de trazabilidad en cada salida calculada.
5. Adjuntar evidencia de validacion cruzada contra referencia externa.

---

## Criterios Globales de Aceptacion

- Los calculos corregidos coinciden con referencia externa en casos controlados.
- No existe ruta donde MADe/nIQR/Algoritmo A use datos de homogeneidad.
- El umbral `n >= 12` queda cubierto por pruebas y evidencia de ejecucion.
- Todas las corridas incluyen metadatos minimos de trazabilidad.
- Los exportables permiten auditoria externa sin ambiguedad.

---

## Riesgos y Mitigacion

- **Riesgo:** mezcla de datasets en capas intermedias.
  **Mitigacion:** validacion estricta de esquema y tipado de origen.
- **Riesgo:** ausencia de dataset patron para Algoritmo A.
  **Mitigacion:** congelar un set dorado para regresion.
- **Riesgo:** despliegue prematuro sin validacion cruzada.
  **Mitigacion:** gate de liberacion condicionado al acta de validacion.

---

## Log de Ejecucion

- [x] Plan final consolidado y aprobado
- [ ] Fase 0 iniciada en repositorio objetivo
- [ ] Fase 1 completada
- [ ] Fase 2 completada
- [ ] Fase 3 completada
- [ ] Fase 4 completada
