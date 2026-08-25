---
title: "Implementación de ensayos de aptitud en la matriz aire"
subtitle: "Caso gases contaminantes criterio — Proyecto 61134 · Convenio 005-2023 INM–UNAL"
author: "Laboratorio CALAIRE — Facultad de Minas, Universidad Nacional de Colombia, Sede Medellín"
date: "Intercambio Técnico INM–UNAL · 12 de agosto de 2026"
---

<!-- Compilar desde docs/informes con:
     pandoc presentacion_it_inm.md -o presentacion_it_inm.pptx --slide-level=2 --reference-doc=plantilla_presentacion_it_inm.pptx
-->

# Contexto

## Marco del encuentro

- Convenio 005-2023 INM–UNAL: fortalecimiento de capacidades metrológicas y de innovación de los laboratorios UNAL.
- Proyecto 61134 (Sede Medellín, Facultad de Minas): *Implementación de ensayos de aptitud en la matriz aire. Caso gases contaminantes criterio*.
- Intercambio técnico: espacio de cooperación entre expertos, no de control — orientado a identificar riesgos y oportunidades de articulación.
- **Cortes de información:** línea base del seguimiento 09 al **8-jul-2026** y actualización técnica al **12-ago-2026**.

::: notes
Encuadre según guía metodológica del INM (§3.1): carácter de intercambio de conocimiento. Presentación ~35 min, resto para preguntas técnicas y matriz de riesgos. Distinguir la línea base del seguimiento 09 de los avances posteriores, en particular la ronda con Corantioquia.
:::

## Agenda y criterio de seguimiento

1. Objetivos y resultados esperados del proyecto 61134.
2. Avances técnicos y medios de verificación.
3. Piloto, aplicativos e integración al sistema de gestión.
4. Pendientes, dificultades y fecha de finalización.
5. Riesgos y oportunidades de articulación con el INM.

::: notes
Cadena de trazabilidad usada: objetivo → medio de verificación → resultado/producto → actividad → estado → riesgo o acción de cierre.
:::

# Objetivos del proyecto

## Objetivo general y alcance

**Objetivo:** establecer un servicio de comparaciones interlaboratorios y/o ensayos de aptitud (EA) para la evaluación competente, imparcial e independiente del desempeño de laboratorios y redes de monitoreo de calidad del aire del país y la región.

- **Alcance:** CO, SO₂, O₃ y óxidos de nitrógeno, con mediciones específicas de NO y NO₂ según la ronda.
- **Base normativa:** ISO/IEC 17043:2023 (proveedores de ensayos de aptitud) e ISO 13528:2017 (métodos estadísticos).
- **Articulación:** sistema de gestión del Laboratorio CALAIRE bajo NTC ISO/IEC 17025.

## Objetivos específicos — base técnica

- **O1. Identificar procedimientos internacionales** mediante estudio bibliográfico.\
  *Verificación:* informe de estado del arte — **100 %**.
- **O2. Elaborar los protocolos** para los gases del alcance.\
  *Verificación:* protocolo general y cuatro procedimientos — **100 %**.
- **O3. Definir la metodología estadística y desarrollar el aplicativo libre.**\
  *Verificación:* aplicativo e informe de validación/análisis — **100 %**.

## Objetivos específicos — validación y sostenibilidad

- **O4. Desarrollar la prueba piloto** y ajustar protocolos y aplicativo.\
  *Línea base:* **86,7 %**; actualización: tres rondas ejecutadas y ronda multiparticipante pendiente.
- **O5. Integrar los protocolos al sistema de gestión de CALAIRE.**\
  *Línea base:* **50 %**; documentos finales en revisión y control de cambios.
- **O6. Desarrollar costeo, política de precios y condiciones del servicio.**\
  *Línea base:* **0 %**; insumos técnicos y viabilidad en elaboración.

# Resultados esperados del proyecto 61134

## Resultados esperados — desarrollo técnico

- **R1. Estado del arte:** informe terminado.
- **R2. Protocolo general y cuatro procedimientos:** versión final, en integración al SGC.
- **R3. Instructivo de embalaje y transporte:** terminado.
- **R4. Prueba piloto:** informe en consolidación; rondas adicionales pendientes.

## Resultados esperados — operación del servicio

- **R5. Aplicativo estadístico libre e informe de análisis:** pt_app y validación entregados; falta prueba final como usuario.
- **R6. Protocolos finales integrados al SGC:** documentos controlados e informe de actualización en curso.
- **R7. Costeo, política de precios, condiciones y portafolio:** modelo de costos y oferta actualizada en elaboración.

::: notes
Los porcentajes corresponden a la línea base presentada el 8-jul-2026. Los textos de estado posteriores describen la actualización técnica al 12-ago-2026 y no implican el cierre contractual de los resultados aún pendientes.
:::

# Avances técnicos

## Estado del arte y protocolos

- Informe de estado del arte **terminado**: procedimientos internacionales de EA, requisitos de trazabilidad metrológica y criterios de aceptación de las mediciones.
- **Cinco documentos técnicos en versión final** —un protocolo general y cuatro procedimientos de medición— remitidos para revisión e integración al sistema de gestión (control de cambios en curso).
- Estructura documental del servicio bajo el proceso PSEA: formatos (F-PSEA), instructivos (I-PSEA) y documentos guía (DG-PSEA).

## Marco estadístico definido

- Metodología de comparación conforme a ISO 13528: estimadores robustos — **Algoritmo A, NIQR, MADe** — implementados y verificados en el aplicativo estadístico.
- **Puntajes Z y Z' adoptados como métricas iniciales de desempeño**: ISO 17043 permite avanzar sin exigir la incertidumbre reportada por el participante.
- Homogeneidad y estabilidad de los ítems de ensayo evaluadas con ANOVA y pruebas t.
- Estrategia para consolidar la desviación estándar del ensayo: **réplicas internas del proceso de medición + rondas adicionales** (meta: >12 datos por analito); revisión comparativa de normas europeas y handbook EPA para métricas complementarias.

## Prueba piloto — rondas ejecutadas

| Ronda | Analitos | Modalidad | Fecha |
|---|---|---|---|
| EA-PP2026-R1 | CO / SO₂ | Ronda simple, 1 participante | Semana 20-abr-2026 |
| EA-PP2026-R2 | O₃ / NO / NO₂ | Ejecutada con participante único | Semana 27-abr-2026 |
| EA-PP2026-R3 | O₃ / NO / NO₂ | Ronda simple, participante Corantioquia | 15 al 17-jul-2026 |

- Secuencia operativa validada: instalación, calibración multipunto, medición por niveles (cero + 4 niveles descendentes), devolución y cierre logístico.
- R3 replicó el flujo con un **segundo laboratorio participante** y parque instrumental distinto: corridas de O₃, NO y NO₂ (esta última por titulación en fase gaseosa, GPT), con operación nocturna continua de 13–15 h por contaminante.
- **Próximas rondas:** ronda con participantes con conjunto completo de analizadores; réplica de CO/SO₂ con participante que disponga de esos analizadores; réplicas internas; ronda con 4–5 participantes para habilitar estimación robusta (MADe).

---

![Cronología de la prueba piloto](timeline_piloto.png)

## Balance del piloto — validación operativa

- Generación de ítems, logística en sitio y secuencias de medición **validadas en tres rondas**, con dos laboratorios participantes.
- R3 demostró la repetibilidad del flujo: instalación, calibración, operación continua, desmontaje y cierre de registros.
- Generación de NO₂ por titulación en fase gaseosa (GPT) ejecutada durante R3.
- Instructivo de cálculo y reporte entregado desde R3: ventanas horarias, promedios e incertidumbre expandida.
- Evaluación de desempeño viable con puntajes Z/Z' aun sin incertidumbres reportadas por los participantes.

## Balance del piloto — lecciones y restricciones

- Lecciones registradas en F-PSEA-15:
  - Verificar repuestos y sistema GPT antes de la ronda (F-PSEA-08).
  - Controlar la temperatura para O₃ y reservar aire cero para calibración e ítems.
  - Exigir llegada previa de equipos y disponibilidad del participante durante el ensayo.
- **Restricciones:** manifold de una salida y ausencia de control térmico para mediciones prolongadas.
- **Consecuencia:** la ronda multiparticipante requiere mejoras de infraestructura y disponibilidad del T700U.

## Integración al sistema de gestión

- Mapeo de requisitos de ISO/IEC 17043:2023 sobre la estructura documental del laboratorio.
- Módulo de gestión centralizado del esquema: rondas, participantes, requisitos documentales y registros.
- Documentos del servicio en flujo de revisión y control de cambios para su incorporación formal al SGC (NTC ISO/IEC 17025).

# Aplicativos desarrollados

## pt_app — evaluación estadística

Aplicativo estadístico en **software libre (R/Shiny)** para la evaluación de resultados y elaboración de informes de los EA (DG-PSEA-03), desplegado en shinyapps.io:

- Carga y validación de datos de participantes.
- Homogeneidad y estabilidad de ítems (ANOVA, t-test).
- Núcleo robusto: Algoritmo A, NIQR, MADe.
- Puntajes de desempeño e informe automatizado (R Markdown).
- Dashboards interactivos: boxplots, histogramas, gráficos de puntajes.

**Estado:** entregado en su totalidad con documentación e informe de validación de cálculos y procesos; pendiente únicamente la prueba como usuario final en la última ronda del piloto.

## calaire-app — gestión de rondas

Aplicativo de gestión de rondas del esquema de ensayos de aptitud (DG-PSEA-02), versión actual en desarrollo (calaire-app2):

- Administración de rondas, participantes e inscripciones.
- Trazabilidad de requisitos documentales de ISO/IEC 17043.
- Soporte a la operación del piloto y a la formalización del servicio.

**Mejoras derivadas del piloto:** asignación de identificadores aleatorios a participantes (confidencialidad) y ajuste del flujo de descarga y almacenamiento de datos crudos.

**Estado:** entregado; pendiente únicamente la prueba operativa en la última ronda del piloto.

# Resultados, cronograma y finalización

## Resultados a la fecha

| Producto | Estado |
|---|---|
| Informe de estado del arte | Terminado |
| Protocolo general + cuatro procedimientos de medición | Versión final, en integración al SGC |
| Instructivo embalaje y transporte | Terminado |
| Prueba piloto interna (R1, R2, R3) | Ejecutada; informes operativos emitidos (v3-1 para R1/R2; R3 Corantioquia v1) |
| Marco estadístico (Z/Z', robustos) | Definido y formalizado |
| pt_app | Entregado; pendiente prueba en última ronda |
| calaire-app | Entregado; pendiente prueba en última ronda |
| Costeo del servicio | Insumos técnicos en elaboración |

## Cronograma de actividades pendientes

- Rondas adicionales: réplicas internas sin participantes externos, réplica de CO/SO₂ con participante habilitado y ronda multiparticipante (4–5) para muestra intercomparativa.
- Mejoras de infraestructura: manifold multi-salida y control térmico del área de prueba, previas al escalamiento multi-participante.
- Consolidación de la desviación estándar del ensayo y de la reproducibilidad intermedia.
- Cierre del ciclo de validación del aplicativo estadístico como usuario final.
- Integración final de protocolos y procedimientos al SGC con control de cambios.
- Costeo y análisis de viabilidad del servicio postpiloto.

---

![Cronograma de la prueba piloto](gantt_piloto.png)

## Fecha de finalización proyectada

- Ejecución contractual del rol técnico líder proyectada a **diciembre de 2026**.
- La reprogramación de rondas por la indisponibilidad temporal del calibrador dinámico motivó la **solicitud de prórroga por 60 días ante la instancia de seguimiento institucional**, para asegurar el cierre completo de rondas pendientes y la validación estadística; no se presenta como aprobada mientras no exista confirmación formal.
- Hitos de cierre: rondas restantes → consolidación estadística → informe final del piloto → protocolos integrados al SGC → servicio listo para etapa comercial.

# Dificultades

## Dificultades técnicas

- **Calibrador dinámico T700U:** en garantía con el proveedor y actualmente en pruebas de verificación.
- **Impacto:** disponibilidad para la ronda multiparticipante; la R3 operativa con Corantioquia sí fue ejecutada.
- **Mitigación:** reprogramación, solicitud de prórroga por 60 días y seguimiento formal de la garantía.
- **Incertidumbre no reportada por participantes:** evaluación inicial con puntajes Z/Z' y apoyo experto para el modelo de incertidumbre.
- **Infraestructura:** manifold de una salida, generación de aire cero y falta de control térmico; en R3 se observaron 18–23 °C, relevantes para O₃.

## Dificultades administrativas y sostenibilidad

- Coordinación de la participación externa: inasistencias institucionales obligaron a reprogramar la ronda multiparticipante.
- Continuidad de la capacidad técnica del equipo del proyecto entre etapas contractuales.
- Sostenibilidad: transición del piloto a un servicio comercializable exige finalizar protocolos, consolidar el modelo de costos y asegurar la infraestructura de generación de ítems.

# Cierre

## Insumos para la matriz de riesgos y articulación

| Categoría (formato INM) | Riesgo preliminar identificado |
|---|---|
| Objetivos y alcance | Retraso en rondas por disponibilidad del calibrador T700U |
| Entregables | Desviación estándar del ensayo con muestra aún insuficiente |
| Técnicas | Incertidumbre de participantes no reportada; límite de infraestructura |
| Administrativas | Tiempos de garantía del proveedor; continuidad contractual |

**Oportunidades de articulación con el INM:** trazabilidad metrológica de las mezclas de gases, materiales de referencia, asesoría en modelos de incertidumbre del valor asignado y experiencia como proveedor acreditado de EA.

::: notes
Cierre alineado con las 4 categorías del Formato – Guía para la Reunión técnica, para diligenciamiento directo durante la sesión.
:::
