# Plan: Cierre de gates para liberación comercial CALAIRE-EA

**Created**: 2026-07-14 15:58 -05
**Updated**: 2026-07-14 15:58 -05
**Status**: approved
**Slug**: commercial-release-gates

## Objetivo

Reunir la evidencia económica, técnica, financiera y jurídica necesaria para
aprobar la primera ronda comercial con la capacidad física actual, desplegar
CS-10 y ejecutar una simulación administrativa integral antes de publicar fecha
o precio.

## Decisiones confirmadas

- La primera ronda comercial usará la capacidad actual: máximo 4 analizadores
  por bloque individual y, para CO/SO₂ simultáneo, máximo 3 organizaciones y 6
  analizadores totales.
- La capacidad de 10–12 participantes es un objetivo futuro y no se ofrecerá
  hasta validar la ampliación física.
- Se emitirá directamente el informe final; no habrá informe preliminar ni
  periodo formal previo de comentarios.
- El uso de las instalaciones es un aporte institucional no cuantificado. No se
  inventará alquiler ni consumo de servicios sin evidencia.
- Si los ingresos confirmados no cubren el costo directo, la regla provisional
  es aplazar la ronda, salvo autorización escrita de subsidio institucional.
- La ronda no tendrá fecha publicada hasta cerrar costos, Finanzas, Jurídica y
  aptitud del cilindro.
- La demanda se estimará con las redes oficiales y expresiones de interés. No se
  afirmará obligación legal de participar sin validación jurídica y acreditación.
- La simulación integral se ejecutará después de cerrar Finanzas y Jurídica.

## Supuestos de esfuerzo para CS-04

| Rol / recurso | Supuesto provisional por ronda | Validación requerida |
|---|---:|---|
| Fabián — operación técnica | 72 horas | Contrastar con primera ronda comercial |
| Coordinación | 68 horas | 36 operación + 12 planificación/cierre + 12 cálculos + 8 informe final |
| Infraestructura | Hasta 4 h por actividad/semana activa | Asignar solo trabajo efectivo |
| Proyectos | Hasta 4 h por actividad/semana activa | Asignar solo trabajo efectivo |
| Calidad del Aire | Hasta 4 h por actividad/semana activa | Asignar solo trabajo efectivo |
| Gestión de Calidad | Hasta 4 h por actividad/semana activa | Asignar solo trabajo efectivo |
| Instalaciones | Aporte institucional no cuantificado | Finanzas puede revisar tratamiento |

El calendario rector es `docs/qms/01_bloque_general/04_formatos_maestros/F-PSEA-01 Calendario Tipo_v0.xlsx`; el detalle de la operación es `F-PSEA-02`. Las horas no se calculan multiplicando toda la duración calendario por 4 h/semana: se cargan por actividad efectiva.

## Fases

### Fase 1: Recuperar evidencia económica

| # | Responsable | Evidencia / acción | Criterio de cierre |
|---|---|---|---|
| 1.1 | Responsable del servicio | Solicitar a David tarifas institucionales por perfil o valores contractuales equivalentes | Valores por rol, fuente, fecha y tratamiento de cargas documentados |
| 1.2 | Responsable del servicio + Infraestructura + Proyectos | Recuperar compras, mantenimientos, repuestos y consumibles de 4 analizadores, calibrador dinámico y aire cero | Valor, fecha y soporte suficiente para provisión general por activo |
| 1.3 | Responsable del servicio | Recuperar factura/registro del cilindro multicomponente | Costo antes de impuestos, moneda, fecha y conceptos incluidos identificados |
| 1.4 | Proyectos | Obtener cotizaciones faltantes cuando las compras históricas no sean representativas | Cotización vigente o supuesto marcado como pendiente de aprobación |
| 1.5 | Responsable del servicio + David | Obtener cotización, factura y condiciones de pago anonimizadas de otro servicio CALAIRE | Precedente institucional incorporable a CS-04/CS-06/CS-12 |
| 1.6 | Responsable del servicio | Diligenciar CS-04 con la evidencia anterior | Costo directo por ronda, costo por participante y umbral de equilibrio calculados |

### Fase 2: Cerrar evidencia técnica

| # | Responsable | Evidencia / acción | Criterio de cierre |
|---|---|---|---|
| 2.1 | Responsable del servicio | Recuperar certificado completo del cilindro CO/SO₂/NOx | Certificado legible y vigente disponible |
| 2.2 | Wilson Salas | Revisar concentraciones, incertidumbres, vigencia, estabilidad y compatibilidad con niveles | Concepto técnico registrado |
| 2.3 | Carmen Elena Zapata | Aprobar o rechazar el uso del cilindro | Aprobación fechada o acción de reposición definida |
| 2.4 | Responsable del servicio + Fabián | Verificar espacio, conexiones, flujo, energía, adquisición de datos y supervisión para capacidad actual | Checklist y evidencia del montaje respaldan 4 por bloque y 3 organizaciones/6 analizadores CO/SO₂ |
| 2.5 | Responsable del servicio | Registrar ampliación a 10–12 como proyecto futuro | No aparece como capacidad disponible en oferta ni CS-10 |

### Fase 3: Cerrar Finanzas y Jurídica

| # | Responsable | Evidencia / acción | Criterio de cierre |
|---|---|---|---|
| 3.1 | Responsable del servicio + David | Identificar la dependencia financiera usando precedentes de servicios CALAIRE | Ruta y responsable institucional identificados |
| 3.2 | Finanzas UNAL | Validar impuestos, facturación, anticipos, órdenes de compra, devoluciones y notas crédito | Concepto aplicable a CS-06, CS-08, CS-10 y CS-12 |
| 3.3 | Responsable del servicio | Solicitar a David el contrato/modelo institucional vigente | Modelo controlado disponible |
| 3.4 | David | Canalizar revisión jurídica de CS-08 | Dependencia jurídica y revisor identificados |
| 3.5 | Jurídica UNAL | Revisar responsabilidad, controversias, cancelación, fuerza mayor y uso de informes | CS-08 aprobado o lista cerrada de correcciones |
| 3.6 | Jurídica UNAL | Confirmar antes de cualquier comunicación la base de una eventual obligación de participación | Norma, sujetos, periodicidad y condiciones documentados; sin afirmaciones previas |

### Fase 4: Desplegar CS-10

| # | Responsable | Evidencia / acción | Criterio de cierre |
|---|---|---|---|
| 4.1 | Coordinación | Cargar `CS-10_enrollment_revenue_tracker.xlsx` al servidor institucional | Ruta controlada registrada |
| 4.2 | Coordinación | Cambiar la contraseña inicial y probar permisos existentes | Contraseña rotada; acceso restringido confirmado sin documentar la clave |
| 4.3 | Coordinación | Ejecutar prueba de aceptación del libro | Fórmulas, capacidad, pagos, respaldo y ausencia de resultados técnicos verificados |
| 4.4 | Carmen Elena Zapata | Aprobar CS-10 v0.3 para uso institucional | Aprobación fechada registrada en artefacto/control documental |

### Fase 5: Decidir liberación y simular

| # | Responsable | Evidencia / acción | Criterio de cierre |
|---|---|---|---|
| 5.1 | Responsable del servicio + Finanzas | Comparar costo directo con ingresos para 1–4 participantes | Mínimo comercial o decisión de subsidio documentados en CS-01/CS-04 |
| 5.2 | Responsable del servicio | Actualizar fecha, umbral y condiciones solo después de aprobaciones | CS-03, CS-06, CS-08 y CS-10 alineados |
| 5.3 | Equipo comercial/operativo | Ejecutar simulación sintética CS-05 → CS-15 | Cotización, registro, capacidad, pago/PO, confirmación, cancelación y reasignación trazables |
| 5.4 | Carmen + Finanzas + Jurídica | Revisar gates de liberación | Precio y fecha se publican únicamente con todos los gates cerrados |

## Solicitudes inmediatas del responsable del servicio

1. Pedir a David tarifas por perfil o equivalentes contractuales.
2. Pedir a David cotización, factura y condiciones de pago de otro servicio CALAIRE.
3. Pedir a David el modelo contractual institucional y la canalización jurídica.
4. Recuperar con Infraestructura/Proyectos compras y mantenimiento de equipos.
5. Recuperar factura y certificado del cilindro.
6. Coordinar con Fabián la verificación de capacidad actual.

## Log de ejecución

- [x] Plan aprobado a partir del grill de decisiones del 2026-07-14.
- [ ] Fase 1 iniciada.
- [ ] Fase 1 completada.
- [ ] Fase 2 completada.
- [ ] Fase 3 completada.
- [ ] Fase 4 completada.
- [ ] Fase 5 completada.
