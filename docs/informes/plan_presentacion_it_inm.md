# Plan — Presentación Intercambio Técnico INM–UNAL (12 ago 2026, 9:00)

Proyecto 61134: Implementación de ensayos de aptitud en la matriz aire. Caso gases contaminantes criterio (CO, NOx, SO₂, O₃).

## Objetivo del documento

Producir `presentacion_it_inm.md` convertible con:

```bash
pandoc presentacion_it_inm.md -o presentacion_it_inm.pptx \
  --reference-doc=plantilla_calaire.pptx   # opcional; sin plantilla usa la default
```

Convenciones pandoc:
- `#` = título de sección (slide separadora), `##` = slide.
- `---` fuerza salto de slide.
- Notas del orador en bloque `::: notes ... :::`.
- Imágenes: rutas relativas a `docs/informes/` (gantt_piloto.png, timeline_piloto.png ya existen).
- Dos columnas con `:::: columns` / `::: column` si se necesita.

## Estructura de slides (responde agenda de `agenta_it_vf.md` y guía `guia_it_vf.pdf` §3.2.3.a)

### Bloque 0 — Portada y contexto (2 slides)
1. **Portada**: proyecto 61134, Convenio 005-2023, sede Medellín – Minas, Laboratorio CALAIRE, fecha.
2. **Contexto**: objetivo del intercambio técnico (no control, cooperación entre expertos), equipo del proyecto.

### Bloque 1 — Objetivo del proyecto (1–2 slides)
3. **Objetivo y alcance**: servicio de comparaciones interlaboratorios / ensayos de aptitud para CO, NOx, SO₂, O₃ bajo ISO 17043:2023 e ISO 13528:2017 (fuente: contrato_1/funciones.md).
4. **Productos comprometidos**: estado del arte, protocolos por analito, instructivo embalaje/transporte, informe prueba piloto interna, integración al SGC, aplicativo estadístico, costeo del servicio.

### Bloque 2 — Avances técnicos (4–5 slides)
5. **Estado del arte y protocolos**: informe de estado del arte terminado; cinco protocolos y procedimientos de medición en versión final, en revisión para integración al SGC (control de cambios).
6. **Marco estadístico definido**: métricas Z y Z' adoptadas como métricas iniciales (ISO 17043 permite avanzar sin incertidumbre del participante); Algoritmo A, NIQR, MADe implementados en el aplicativo; estrategia para desviación estándar del ensayo: réplicas internas + más rondas.
7. **Prueba piloto — rondas ejecutadas**:
   - EA-PP2026-R1: ronda simple CO/SO₂, abril 2026, participante SIATA.
   - EA-PP2026-R2: ronda simple O₃/NO/NO₂, abril 2026, participante único.
   - Ronda C: planificada con participante adicional (UPB); rondas adicionales con 4–5 participantes proyectadas para habilitar MADe.
   - Insertar `timeline_piloto.png`.
8. **Balance del piloto (highlights, sin atribución de personas)**:
   - Validación operativa de generación de ítems de ensayo y logística en sitio.
   - Lecciones incorporadas al SGC (F-PSEA-15): verificación pre-ronda de repuestos y GPT, criterio de temperatura para O₃, aire cero exclusivo, requisitos de llegada y disponibilidad del participante.
   - Necesidad identificada: >12 datos o réplicas internas para desviación estándar robusta; infraestructura limita participantes simultáneos.
9. **Integración al SGC**: estructura documental PSEA (formatos F-PSEA, instructivos I-PSEA), módulo de gestión centralizado con mapeo de requisitos ISO 17043.

### Bloque 3 — Aplicativos (2 slides)
10. **calaire-app** (contrato OSE 282/2025 — DG-PSEA-02): aplicativo estadístico en R/Shiny para evaluación de resultados EA: carga y validación de datos, homogeneidad/estabilidad (ANOVA, t-test), estadísticos robustos (Algoritmo A, NIQR, MADe), puntajes de desempeño, informes R Markdown, dashboards interactivos. Estado: versión beta entregada, informe de validación elaborado, pruebas como usuario final en curso con registro de hallazgos.
11. **pt_app** (DG-PSEA-03): aplicativo de gestión del esquema PT (desplegado en shinyapps.io): gestión de rondas, participantes, requisitos documentales de ISO 17043. Mejoras derivadas del piloto: IDs aleatorios de participantes, flujo de descarga/almacenamiento de datos crudos.

### Bloque 4 — Resultados a la fecha, cronograma, fecha de finalización (2–3 slides)
12. **Resultados a la fecha** (tabla): entregables vs estado (terminado / en revisión / en curso).
13. **Cronograma actividades pendientes**: rondas adicionales (réplicas internas + ronda multiparticipante), consolidación de reproducibilidad intermedia, integración final de protocolos al SGC, validación final del aplicativo, costeo y viabilidad comercial postpiloto. Insertar `gantt_piloto.png` o gantt actualizado.
14. **Fecha de finalización proyectada** + hitos restantes.

### Bloque 5 — Dificultades (1–2 slides) — insumo directo para riesgos INM
15. **Dificultades técnicas**:
    - **Daño del calibrador dinámico Teledyne API T700U** — dificultad principal. En garantía con el proveedor; actualmente en pruebas de verificación. Impacto: disponibilidad para rondas siguientes; mitigación: solicitud de prórroga presentada ante instancia de seguimiento, reprogramación de rondas.
    - Incertidumbre de participantes no disponible; mitigado con Z/Z' y consulta a experto en metrología.
    - Infraestructura (aire cero, espacio) limita número de participantes simultáneos.
16. **Dificultades administrativas / sostenibilidad**: coordinación de participación externa (inasistencias reprogramadas), continuidad contractual del equipo, transición piloto → servicio comercializable.

### Bloque 6 — Cierre (1 slide)
17. **Preparados para preguntas del INM / insumos para matriz de riesgos**: mapa de riesgos preliminar en 4 categorías del formato guía (objetivos/alcance, entregables, técnicas, administrativas) + oportunidades de articulación con INM (trazabilidad, MRC de gases, asesoría en incertidumbre).

Total: ~17 slides. Presentación 2 h con preguntas; apuntar a 30–40 min de exposición.

## Reglas de contenido

- Notas de reuniones: solo balance y highlights, sin atribuir intervenciones a personas.
- Contratos (contrato_1, contrato_app) solo como referencia de objetivos técnicos y entregables; no exponer valores económicos.
- Riesgos del bloque 5 alineados con las 4 categorías del formato INM para facilitar diligenciamiento del "Formato – Guía para la Reunión técnica".
- Equipo T700U: presentar como dificultad gestionada (garantía activa, en pruebas), no como riesgo sin control.

## Pasos de ejecución

1. Verificar fechas/estados con `docs/informes/260208_ie_01_rev_consolidado.md` y calendario piloto.
2. Redactar `docs/informes/presentacion_it_inm.md` según estructura anterior.
3. Compilar con pandoc; revisar overflow de texto por slide (máx ~6 bullets).
4. Ajustar imágenes (gantt/timeline) y regenerarlas si desactualizadas.
5. Revisión final contra agenda del correo INM punto por punto.
