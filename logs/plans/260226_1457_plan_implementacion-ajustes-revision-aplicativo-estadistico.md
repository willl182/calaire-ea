# Plan: Implementación de Ajustes de Revisión del Aplicativo Estadístico

**Created**: 2026-02-26 14:57
**Updated**: 2026-02-26 14:57
**Status**: draft
**Slug**: implementacion-ajustes-revision-aplicativo-estadistico

---

## Objetivo

Definir una ruta de implementación funcional y verificable para resolver los hallazgos del documento `docs/ajustes_app/Revisión aplicativo estadístico.pdf`, asegurando alineación con ISO 13528:2022, trazabilidad de datos y capacidad de validación externa en [[CALAIRE-APP]].

---

## Hallazgos de Entrada (Resumen Técnico)

1. Posible error en el cálculo de homogeneidad (referencia a Anexo B, fórmula B.10 ISO 13528:2022).
2. Uso de datos no correctos para estimadores robustos de dispersión (MADe/NIQR/Algoritmo A): se están tomando datos de homogeneidad cuando deben provenir de participantes.
3. Inconsistencia entre series de datos usadas en corridas (DATOS 1 vs DATOS 2).
4. Falta de insumos y trazabilidad para validar Algoritmo A.
5. Baja legibilidad del flujo de carga/descarga de datos para validación externa (CSV poco interpretable).

---

## Fases

### Fase 1: Especificación de Reglas Estadísticas

**Objetivo:** Congelar una especificación matemática única antes de tocar implementación.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 1.1 | docs/ajustes_app/especificacion_calculos_revision2.md | Crear | Definir fórmulas oficiales por módulo: homogeneidad, estabilidad, MADe, nIQR y Algoritmo A (con citas de cláusula/ecuación ISO 13528:2022). |
| 1.2 | docs/ajustes_app/matriz_origen_datos.md | Crear | Matriz de trazabilidad: cada estadístico debe declarar explícitamente su fuente de datos (`homogeneidad` o `participantes`). |
| 1.3 | docs/ajustes_app/criterios_validacion_revision2.md | Crear | Definir tolerancias numéricas (ej. error absoluto/relativo), redondeo, manejo de NA/outliers y reglas de desempate. |

### Fase 2: Diseño Funcional de Datos y Flujo de Carga

**Objetivo:** Evitar ambigüedad entre series y mejorar auditabilidad de entrada/salida.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 2.1 | docs/ajustes_app/diccionario_datos_entrada.md | Crear | Estandarizar campos mínimos: analito, corrida, serie, unidad, valor, tipo_muestra, origen_dato, timestamp. |
| 2.2 | docs/ajustes_app/plantillas_csv_validacion.md | Crear | Definir plantillas CSV separadas para homogeneidad, estabilidad y participantes; agregar ejemplo con encabezados legibles. |
| 2.3 | docs/ajustes_app/diseno_tablas_validacion.md | Crear | Especificar tabla de visualización interna para revisar datos cargados antes del cálculo. |
| 2.4 | docs/ajustes_app/reglas_seleccion_serie.md | Crear | Definir cómo selecciona el sistema DATOS 1, DATOS 2 u otra serie y cómo queda registrado en bitácora. |

### Fase 3: Implementación Lógica (Sin Código Disponible)

**Objetivo:** Dejar instrucciones de desarrollo ejecutables cuando se disponga del repositorio de la app.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 3.1 | docs/ajustes_app/instrucciones_implementacion_modulo_homogeneidad.md | Crear | Instrucciones para ajustar cálculo de desviación entre muestras conforme a la especificación de Fase 1. |
| 3.2 | docs/ajustes_app/instrucciones_implementacion_modulo_robusto.md | Crear | Instrucciones para forzar que MADe/nIQR/Algoritmo A usen exclusivamente datos de participantes. |
| 3.3 | docs/ajustes_app/instrucciones_implementacion_trazabilidad.md | Crear | Instrucciones para registrar versión de dataset, serie usada y parámetros de corrida en cada resultado. |
| 3.4 | docs/ajustes_app/instrucciones_implementacion_exportables.md | Crear | Instrucciones para generar exportables legibles (CSV y tabla) que permitan réplica en Excel. |

### Fase 4: Validación Técnica y Reconciliación con Revisor

**Objetivo:** Confirmar equivalencia numérica y cerrar hallazgos del informe.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 4.1 | docs/ajustes_app/casos_prueba_revision2.md | Crear | Diseñar batería de casos: <12 datos, >=12 datos (activa Algoritmo A), series múltiples, datos extremos y valores faltantes. |
| 4.2 | docs/ajustes_app/acta_validacion_cruzada_revision2.md | Crear | Registrar comparación app vs Excel por caso, con diferencias y decisión de aceptación/rechazo. |
| 4.3 | docs/ajustes_app/lista_cierre_hallazgos_revision2.md | Crear | Checklist de cierre por hallazgo: homogeneidad, MADe, nIQR, Algoritmo A, trazabilidad de datos. |

### Fase 5: Puesta en Operación Controlada

**Objetivo:** Liberar cambios con control de riesgo y soporte a usuarios técnicos.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 5.1 | docs/ajustes_app/guia_usuario_validacion_datos.md | Crear | Guía de uso para carga de datos, lectura de resultados y exportación para verificación externa. |
| 5.2 | docs/ajustes_app/notas_version_ajustes_revision2.md | Crear | Documentar qué se corrige, impacto esperado y limitaciones conocidas. |
| 5.3 | journals/2026_02_26.md | Modificar | Registrar avance del plan, estado de hallazgos y próximos controles en el journal diario. |

---

## Criterios de Aceptación Globales

- Toda fórmula implementada debe estar trazada a `especificacion_calculos_revision2.md`.
- MADe, nIQR y Algoritmo A deben calcularse únicamente con datos de participantes.
- Debe existir evidencia de trazabilidad de dataset y serie por cada corrida.
- Los resultados de validación cruzada App vs Excel deben cumplir tolerancias definidas en Fase 1.
- Debe existir set de prueba que cubra explícitamente el caso `n >= 12` para Algoritmo A.
- El usuario técnico debe poder identificar de forma legible qué datos de entrada generaron cada estadístico.

---

## Instrucciones Claras para el Equipo de Desarrollo (Cuando haya código)

1. Implementar primero reglas matemáticas y fuentes de datos; no iniciar por UI.
2. Asegurar pruebas unitarias por función estadística con datasets controlados.
3. Añadir prueba de integración que valide flujo completo: carga -> cálculo -> exportación.
4. Registrar metadatos de corrida (dataset, serie, fecha, versión de algoritmo).
5. Liberar en ambiente de pruebas con validación conjunta del revisor técnico del informe.

---

## Dependencias y Riesgos

- **Dependencia crítica:** acceso al repositorio y arquitectura actual de [[CALAIRE-APP]].
- **Riesgo técnico:** ambigüedad entre datos de homogeneidad y de participantes si no se tipifica el origen en el modelo de datos.
- **Riesgo de validación:** ausencia de dataset de referencia para Algoritmo A puede bloquear cierre estadístico.
- **Mitigación:** construir dataset patrón y acta de validación cruzada antes de despliegue.

---

## Log de Ejecución

- [x] Fase 1 iniciada (planificación documental)
- [ ] Fase 1 completada
- [ ] Fase 2 iniciada
- [ ] Fase 2 completada
- [ ] Fase 3 iniciada
- [ ] Fase 3 completada
- [ ] Fase 4 iniciada
- [ ] Fase 4 completada
- [ ] Fase 5 iniciada
- [ ] Fase 5 completada
