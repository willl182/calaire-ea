# Plan: Ajustes CALAIRE-APP — Informe de Revisión No. 2 (César Yate)

**Created**: 2026-02-26 14:57
**Updated**: 2026-02-26 14:57
**Status**: draft
**Slug**: ajustes-app-revision-2

---

## Objetivo

Corregir los errores de cálculo y mejorar la usabilidad del aplicativo CALAIRE-APP según los hallazgos del Informe No. 2 de revisión (César Yate, 2026-02-23), e incorporar los hallazgos pendientes de la revisión anterior sobre el informe de resultados.

**Fuentes:**
- `docs/ajustes_app/Revisión aplicativo estadístico.pdf` — Informe No. 2 (2026-02-23)
- `logs/fase2_hallazgos_informe_especificos.md` — Hallazgos previos del informe EA

---

## Resumen de Observaciones de César (Informe No. 2)

### Errores confirmados
1. **Fórmula B.10 (Homogeneidad):** Error en la desviación estándar entre muestras. Cuando el radicando es negativo, el resultado debe ser cero. El aplicativo no lo maneja.
2. **Fuente de datos MADe:** Se calcula con datos de homogeneidad en vez de datos de participantes. César verificó que los valores no coinciden.
3. **Selección MADe vs Algoritmo A:** Si hay ≥12 datos de participantes, debe usarse Algoritmo A. No es claro que el aplicativo implemente esta lógica.

### Cálculos correctos
- nIQR ✅
- Estabilidad ✅

### Recomendaciones de usabilidad
- Separar zonas de carga para homogeneidad, estabilidad y participantes.
- Mejorar formato de exportación/descarga (CSV actual confuso).
- Mostrar tablas claras con datos usados en cada cálculo.

### Pendiente de validación
- César solicita datos del Algoritmo A para validación cruzada.

---

## Fases

### Fase 1: Correcciones de Cálculo (Bloqueantes)

**Objetivo:** Corregir errores en la lógica estadística del aplicativo.

| # | Componente | Acción | Descripción | Ref. Normativa |
|---|-----------|--------|-------------|----------------|
| 1.1 | Homogeneidad — Fórmula B.10 | Corregir | Si radicando < 0 → `ss = 0` | ISO 13528:2022 Anexo B, B.10 |
| 1.2 | MADe — Fuente de datos | Corregir | Usar datos de participantes, no de homogeneidad | ISO 13528:2022 §9 |
| 1.3 | Selección MADe/nIQR vs Algoritmo A | Corregir/Verificar | Implementar: n < 12 → MADe/nIQR; n ≥ 12 → Algoritmo A | ISO 13528:2022 §9 |

### Fase 2: Mejoras de Usabilidad

**Objetivo:** Mejorar la claridad de la interfaz para los revisores técnicos.

| # | Componente | Acción | Descripción |
|---|-----------|--------|-------------|
| 2.1 | Carga de datos | Rediseñar | Separar en 3 zonas: homogeneidad, estabilidad, participantes |
| 2.2 | Visualización de cálculos | Crear | Tablas resumen que muestren datos de entrada y resultados intermedios por cálculo |
| 2.3 | Exportación CSV | Mejorar | Formato legible con encabezados claros y estructura tabular |

### Fase 3: Validación y Documentación

**Objetivo:** Completar la validación con César y resolver hallazgos pendientes del informe.

| # | Componente | Acción | Descripción |
|---|-----------|--------|-------------|
| 3.1 | Algoritmo A | Exportar datos | Compartir datos de entrada y resultados intermedios del Algoritmo A con César |
| 3.2 | Estado de validación | Actualizar | Actualizar `pages/CALAIRE-APP.md` con nuevo estado: Homogeneidad ⚠️, MADe ⚠️ |
| 3.3 | Validación cruzada | Coordinar | César valida correcciones de Fase 1 contra su Excel |

### Fase 4: Hallazgos Pendientes del Informe de Resultados

**Objetivo:** Resolver hallazgos de `logs/fase2_hallazgos_informe_especificos.md` sobre el template del informe.

| # | Hallazgo | Severidad | Acción | Ref. Normativa |
|---|---------|-----------|--------|----------------|
| 4.1 | Fallos estabilidad sin acción mitigatoria documentada | Alta | Añadir subsección 2.2.3 en template | ISO 13528 Anexo B |
| 4.2 | Falta política σ_pt fitness for purpose | Alta | Añadir subsección 2.3.3 en template | ISO 13528 8.1.2 |
| 4.3 | Falta justificación documentada de σ_pt | Alta | Documentar en template | ISO 17043 7.2.2.3 |
| 4.4 | Falta documentación acciones ante fallos de estabilidad | Alta | Añadir en conclusiones del template | ISO 13528 Anexo B |
| 4.5 | Falta definición de z'-score y ζ-score | Media | Añadir en tabla de criterios | ISO 13528 9.5.1, 9.6.1 |
| 4.6 | Falta política para grupos pequeños (n<10) | Media | Añadir subsección 2.3.1 | ISO 13528 5.4 |
| 4.7 | Falta criterio de decisión z vs z' | Media | Añadir subsección 2.3.2 | ISO 13528 9.2.1, 9.5.1 |

---

## Verificación

| Fase | Método | Criterio de Aceptación |
|------|--------|----------------------|
| Fase 1 | Comparación con cálculos manuales de César | Valores coinciden con validación en Excel |
| Fase 1.1 | Caso con radicando negativo → ss = 0 | Resultado correcto |
| Fase 1.2 | MADe con datos de participantes conocidos | Valor coincide con cálculo manual |
| Fase 1.3 | Probar con n=11 y n=12 | Selección correcta de método |
| Fase 2 | Revisión de César | Interfaz clara y datos entendibles |
| Fase 3 | Validación cruzada con César | Algoritmo A verificado |

---

## Decisiones Pendientes (requieren input del usuario)

1. **¿Acceso al repositorio de la app?** Para Fase 1 y 2 se necesita el código R/Shiny.
2. **¿Prioridad de Fase 4?** ¿Se abordan los hallazgos del informe ahora o en una fase posterior?
3. **¿Hay observaciones adicionales de César** fuera de este PDF?

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
