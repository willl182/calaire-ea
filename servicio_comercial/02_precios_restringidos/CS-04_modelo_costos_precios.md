# CS-04 — Modelo de precios y lista de precios aprobada

**Estado:** PROPUESTA DE VIABILIDAD — ACCESO RESTRINGIDO; evidencia de costos pendiente
**Propietario:** Financiero/comercial
**Requerido antes:** Cotización
**Última revisión:** 2026-07-14 (supuestos laborales provisionales aprobados registrados e insumos de viabilidad faltantes consolidados)
**QMS code reference:** ver `00_control/equivalencia_codigos_sgc.md`. Los códigos PSEA / F-PSEA referenciados en este modelo apuntan a los significados vigentes post-renumeración 2026-06-14.

## Objetivo

Validar la tarifa plana provisional, calcular los costes reales y la viabilidad, y
respaldar una futura revisión de precios sin asumir una facturación basada en el gas o el analizador.

## Pricing architecture

```text
Precio del participante = tarifa fija por ronda y organización participante
                          para uno a cuatro bloques seleccionados
```

La propuesta utiliza **COP 5.928.000 sin impuestos por participante
organización**, ya sea que seleccione de uno a cuatro bloques: CO, SO₂, O₃ y NO/NO₂.
El importe es una conversión indicativa de 1.600 EUR, no un precio aprobado y
no es un sustituto del modelo de costos. Incluye hasta un analizador por bloque;
Se puede aceptar un analizador adicional sin recargo sólo cuando haya residuos
capacity exists.

## Workbook tabs

El modelo de costos real debe implementarse como una hoja de cálculo con las siguientes pestañas. Este documento define el contenido requerido para cada pestaña.

### Pestaña 1 — Supuestos

| Asunción | Valor | Fuente/responsable |
|---|---|---|
| Tasa de cambio de referencia | TRM USD/COP × referencia BCE USD/EUR, solo para convertir valores de referencia | CS-01 |
| Exchange-rate refresh frequency | En la fecha de revisión del benchmark | CS-01 |
| FX risk allocation | No aplica a clientes: cotización y facturación únicamente en COP | CS-01 |
| Capacity per gas (individual) | 4 analyzers | CS-01 |
| Capacity simultaneous CO/SO₂ | 3 participants, 6 analyzers | CS-01 |
| Inscripción prevista | [RELLENO] | Estimación de mercado |
| Impuestos (IVA, retenciones, etc.) | [RELLENO] | Asesor tributario |
| Diferencial tributario para clientes internacionales | [RELLENO — exención de IVA, retención, aplicación de tratados] | Asesor tributario |
| Target margin / objective | Lanzamiento y validación; sin margen ni subsidio comprometidos; no cotizar bajo costo directo | CS-01 |
| Factor de uso por ronda para la asignación del ciclo de vida | [RELLENO — fracción entre 0 y 1] | Responsable técnico (basado en historial de uso) |
| Momento de cobro del pago (predeterminado) | [RELLENO — por ejemplo, 100 % anticipado / 50 % con la orden + 50 % antes de la ronda / orden de compra a 30 días] | Política financiera |
| Calendario de cobro de pagos (institucional) | [RELLENO] | Política financiera |

### Supuestos laborales provisionales – tarifas no aprobadas

Estas cantidades se pueden utilizar únicamente para la planificación. El costeo monetario permanece
bloqueado hasta que Finanzas proporcione una tasa de apoyo y un tratamiento del empleo
cargos por cada rol. Reemplace una cantidad únicamente con evidencia operativa fechada.

| Rol/recurso | Cantidad provisional por ronda | Estado de costeo |
|---|---:|---|
| Operación técnica — Fabián | 72h | Horas aprobadas como supuesto de planificación; tasa pendiente |
| Coordinación | 68h | 36 h de operación + 12 h de planificación/cierre + 12 h de cálculos + 8 h de informe final; tasa pendiente |
| Infraestructura | Hasta 4 h por actividad efectiva/semana activa | No multiplique por el calendario completo; registro de actividad y tasa pendiente |
| Proyectos | Hasta 4 h por actividad efectiva/semana activa | No multiplique por el calendario completo; registro de actividad y tasa pendiente |
| Calidad del aire | Hasta 4 h por actividad efectiva/semana activa | No multiplique por el calendario completo; registro de actividad y tasa pendiente |
| Gestión de Calidad | Hasta 4 h por actividad efectiva/semana activa | No multiplique por el calendario completo; registro de actividad y tasa pendiente |
| Instalaciones | Aporte institucional, sin cuantificar | No inventar alquileres ni servicios públicos; Finanzas puede revisar el tratamiento |

### Pestaña 2 — Costo común

| Elemento de costo | Importe anual | Asignación redonda | Notas |
|---|---|---|---|
| Coordinación | [RELLENO] | [RELLENO] | |
| Preparación de instalaciones | [RELLENO] | [RELLENO] | |
| Registro y administración de datos | [RELLENO] | [RELLENO] | |
| Entrega de informes | [RELLENO] | [RELLENO] | |
| Equipo compartido (calibrador, generador de aire cero) | [RELLENO] | [RELLENO] | Desde la pestaña 4 |

### Pestaña 3 — Costo por gas

| Bloque | Costo del cilindro / generación | Ciclo de vida específico del analizador | Asignación de costos | Notas |
|---|---|---|---|---|
| CO | [RELLENO] | [RELLENO] | [CÁLCULO] | |
| SO₂ | [RELLENO] | [RELLENO] | [CÁLCULO] | |
| NO/NO₂ | [RELLENO] | [RELLENO] | [CÁLCULO] | Un solo bloque NOx |
| O₃ | [RELLENO] | [RELLENO] | [CÁLCULO] | |

### Pestaña 4 — Ciclo de vida de los equipos

Provisión anual para todos los equipos CALAIRE identificados:

| Activo | Mantenimiento planificado | Consumibles | Calibración / servicio | Provisión de reparación correctiva basada en riesgos | Provisión anual total | **Factor de uso redondo** | **Asignación redonda** |
|---|---|---|---|---|---|---|---|
| Analizador / sistema de referencia de O₃ | [RELLENO] | [RELLENO] | [RELLENO] | [RELLENO] | [CÁLCULO] | [RELLENO — 0–1] | [CÁLCULO] |
| Analizador de SO₂ | [RELLENO] | [RELLENO] | [RELLENO] | [RELLENO] | [CÁLCULO] | [RELLENO — 0–1] | [CÁLCULO] |
| Analizador de CO | [RELLENO] | [RELLENO] | [RELLENO] | [RELLENO] | [CÁLCULO] | [RELLENO — 0–1] | [CÁLCULO] |
| Analizador de NOx | [RELLENO] | [RELLENO] | [RELLENO] | [RELLENO] | [CÁLCULO] | [RELLENO — 0–1] | [CÁLCULO] |
| Calibrador dinámico | [RELLENO] | [RELLENO] | [RELLENO] | [RELLENO] | [CÁLCULO] | [RELLENO — 0–1] | [CÁLCULO] |
| Generador de aire cero | [RELLENO] | [RELLENO] | [RELLENO] | [RELLENO] | [CÁLCULO] | [RELLENO — 0–1] | [CÁLCULO] |

**Factor de uso redondo (RUF):** fracción del año de uso intensivo del equipo atribuible a un redondo típico. Se estima a partir del historial de campañas (horas de uso / horas totales disponibles) o, en su defecto, a partir del plan de mantenimiento del fabricante. Sin este factor, la asignación por ronda no se puede calcular.

**Fórmula:**

```text
Provisión anual del ciclo de vida
    = planned maintenance + consumables + calibration/service
    + risk-based corrective repair provision

Asignación por ronda
    = provisión anual del ciclo de vida × factor de uso por ronda (RUF)
```

Las piezas y los intervalos exactos deben provenir de los modelos de equipos instalados, programas del fabricante, cotizaciones de servicio o historial de mantenimiento.

### Pestaña 5 — Estrategia de cilindros

Compare mezclas multicomponentes, cilindros individuales y opciones híbridas:

| Criterion | Multi-component mixture | Individual cylinders | Hybrid (if applicable) |
|---|---|---|---|
| Adquisición | Menos pedidos / cilindros | Varios pedidos / cilindros | [RELLENO] |
| Concentraciones | Una especificación debe adaptarse a todas las diluciones | Optimizado por gas | [RELLENO] |
| Estabilidad / compatibilidad | Debe ser certificablemente estable | Gestionado por separado | [RELLENO] |
| Trazabilidad | Un certificado, valores por componente | Certificados separados | [RELLENO] |
| Cálculo de costos del paquete | Más difícil de asignar a ventas de un solo gas | Se asigna directamente al paquete de gases | [RELLENO] |
| Falla / vencimiento | Un problema puede afectar varios gases | Aislado a un solo gas | [RELLENO] |
| Equipos / almacenamiento | Menos reguladores / conexiones | Más reguladores, almacenamiento y manipulación | [RELLENO] |
| Plazo de entrega | Disponibilidad de mezclas personalizadas | Varía según el gas | [RELLENO] |
| Costo estimado por ronda (COP / EUR) | [RELLENO] | [RELLENO] | [RELLENO] |
| **Recomendación** | [RELLENO] | [RELLENO] | [RELLENO] |

**Estrategia aprobada:** [RELLENO]
**Aprobador técnico:** [RELLENO]
**Aprobador comercial/financiero:** [RELLENO]

### Pestaña 6 — Tarifa fija de participación

| Bloques seleccionados | Analizadores incluidos | Tasa provisional excl. impuestos | Analizador adicional con capacidad residual | Notas |
|---|---:|---:|---:|---|
| Cualquier 1 bloque | Hasta 1 | COP 5.928.000 | COP 0 | Sólo propuesta |
| Cualquier 2 bloques | Hasta 2, uno por bloque | COP 5.928.000 | COP 0 | Sólo propuesta |
| 3 bloques cualesquiera | Hasta 3, uno por bloque | COP 5.928.000 | COP 0 | Sólo propuesta |
| Los 4 bloques | Hasta 4, uno por bloque | COP 5.928.000 | COP 0 | CO, SO₂, O₃ y NO/NO₂ |

An additional analyzer never displaces another organization's first position
y requiere revisión de capacidad CS-09.

### Pestaña 6.A — Validación del valor de referencia

Esta pestaña compara el costo real directo y total por organización participante.
contra $5.928.000. Debe mostrar el costo por separado para cada bloque seleccionado.
escenario a pesar de que el precio propuesto al cliente es fijo.

| Medida | Valor (COP) | Fuente / calculo |
|---|---:|---|
| Costo directo, 1 bloque | [CÁLCULO] | Pestañas 2–4 |
| Costo directo, 2 bloques | [CÁLCULO] | Pestañas 2–4 |
| Costo directo, 3 bloques | [CÁLCULO] | Pestañas 2–4 |
| Costo directo, 4 bloques | [CÁLCULO] | Pestañas 2–4 |
| Costo total asignado, 4 bloques | [CÁLCULO] | Pestañas 2–4 |
| Provisional flat fee | 5.928.000 | CS-01 |
| Contribución / déficit por escenario | [CÁLCULO] | tarifa − costo |
| **Interpretación/decisión** | [RELLENO] | aprobación de la dirección antes de la cotización |

### Pestaña 7 — Inscripción

| Escenario | Participantes | Analizadores | Ingresos | Costos | Contribución | Momento de entrada del efectivo | ¿Viable? |
|---|---|---|---|---|---|---|---|
| Baja (1 participante, 1 gas) | 1 | 1 | [CALC] | [CALC] | [CALC] | [RELLENO] | [RELLENO] |
| Previsto | [RELLENO] | [RELLENO] | [CÁLCULO] | [CÁLCULO] | [CÁLCULO] | [RELLENO] | [RELLENO] |
| Capacidad total para un gas individual | 4 | 4 | [CÁLCULO] | [CÁLCULO] | [CÁLCULO] | [RELLENO] | [RELLENO] |
| Capacidad total simultánea de CO/SO₂ | 3 | 6 | [CÁLCULO] | [CÁLCULO] | [CÁLCULO] | [RELLENO] | [RELLENO] |
| Selección mixta | [RELLENO] | [RELLENO] | [CÁLCULO] | [CÁLCULO] | [CÁLCULO] | [RELLENO] | [RELLENO] |

**Momento de la entrada de efectivo:** columna crítica para entender la viabilidad real. Si el ingreso se cobra 100% anticipado y los costos se pagan durante la ronda, la viabilidad operativa es muy distinta a un escenario de pago a 30 días. CS-06 sección 9 y CS-10 columna "PO/pago/estado de factura" usan esta misma escala temporal.

### Pestaña 8 — Escenarios

| Escenario | Descripción | Resultado |
|---|---|---|
| Punto de equilibrio para gas individual | Cupos pagados mínimos para cubrir el costo | [CÁLCULO] |
| Punto de equilibrio para CO/SO₂ simultáneos | Cupos pagados mínimos para cubrir el costo | [CÁLCULO] |
| Punto de equilibrio para el paquete completo | Cupos pagados mínimos para cubrir el costo | [CÁLCULO] |
| Capacidad baja | 1–2 participantes | [CÁLCULO] |
| Capacidad prevista | [RELLENO] | [CÁLCULO] |
| Capacidad total | Según los límites de CS-01 | [CÁLCULO] |
| Flujo de caja en el peor de los casos (matriculación baja + pagos atrasados) | Tensión de caja | [CALC] |

### Pestaña 9 — Aprobación

| Campo | Valor |
|---|---|
| Cuota fija de participación aprobada | [RELLENO] |
| Ajuste de bloque seleccionado aprobado | COP 0 a menos que se revise CS-01 |
| Tarifa de analizador adicional aprobada | COP 0 durante la etapa de propuesta, sujeto a capacidad residual |
| Estrategia de cilindro aprobada (de la pestaña 5) | [RELLENO] |
| Paquetes aprobados (de la pestaña 6) | [RELLENO] |
| Política cambiaria aprobada (de la pestaña 1) | [RELLENO] |
| Calendario de cobro de efectivo aprobado (de la pestaña 1) | [RELLENO] |
| Precios aprobados válidos desde | [RELLENO] |
| Precios aprobados válidos hasta | [RELLENO] |
| Aprobador (comercial/financiero) | [LLENAR NOMBRE, FECHA, FIRMA] |
| Aprobador (técnico) | [LLENAR NOMBRE, FECHA, FIRMA] |
| Aprobador (dirección) | [RELLENO: NOMBRE, FECHA, FIRMA] |

### Pestaña 10 — Ronda institucional cerrada (cotización de costo total)

Esta pestaña cubre rondas dedicadas a un solo patrocinador o un grupo cerrado de participantes que requieren una cotización de costo total (apartado 8.6 del plan). Se estructura de manera distinta a la lista pública: no hay paquetes estándar; todo se calcula desde los componentes individuales.

| Item | Cálculo |
|---|---|
| Identificación del patrocinador | [RELLENO] |
| Alcance de la ronda (gases, configuración, capacidad reservada) | [RELLENO] |
| Costo común (pestaña 2 asignación de ronda × 1 ronda) | [CALC] |
| Costo específico del gas (pestaña 3 × cantidad de analizadores reservados) | [CÁLCULO] |
| Ciclo de vida del equipo (Pestaña 4 asignación de rondas × horas reservadas) | [CALC] |
| Prima de uso exclusivo (capacidad no compartida con ronda pública) | [RELLENO] |
| Requisitos personalizados (informes adicionales, idioma personalizado, días exclusivos de instalaciones) | [RELLENO] |
| Apoyo en viajes/in situ (si el patrocinador requiere personal de CALAIRE) | [RELLENO] |
| Subtotal de costos | [CÁLCULO] |
| Margen (según el objetivo de precios) | [RELLENO] |
| Precio institucional indicativo (sin impuestos) | [CALC] |
| Condiciones de pago (normalmente 50 % del pedido + 50 % de pre-ronda para instituciones) | [RELLENO] |
| Firma de aprobación del patrocinador | [RELLENO] |
| Aprobación interna (comercial/financiera + gestión) | [RELLENO] |

**Reglas de Tab 10:**

- No usar precios de lista pública; todo se calcula como costo más margen.
- La "prima de uso exclusivo" es obligatoria: el patrocinador paga por la capacidad que no se ofrece a otros clientes.
- Requiere doble aprobación (comercial/financiera + gestión) por el tamaño relativo.
- El patrocinador normalmente paga ≥ 50 % al confirmar la orden; la variante "Institucional/cerrada" de CS-06 lo refleja.

## Lista de precios orientada al cliente

La lista externa (consulte `listas_precios_aprobadas.md`) muestra solo los precios aprobados, la moneda, los impuestos, las inclusiones, la tarifa del analizador adicional, la validez y los requisitos de cotización. Los detalles de costos internos y márgenes siguen siendo restringidos.

## Comprobaciones de lógica comercial

- [ ] La tarifa fija se muestra consistentemente para uno a cuatro bloques seleccionados.
- [ ] Se acepta un analizador adicional sólo con capacidad residual y no desplaza una primera posición.
- [ ] Las rondas institucionales cerradas requieren una cotización del costo total por separado (Pestaña 10).
- [ ] Se documentan el objetivo de la propuesta y el costo mínimo directo del CS-01.
- [ ] El punto de referencia de COP 5.928.000 se compara con la capacidad verificada, no con una ronda supuesta de 8 a 15 participantes.
- [] El factor de uso redondo se completa para cada activo en la pestaña 4.
- [ ] La pestaña 6.A muestra la contribución o el déficit directo y de costo total para cada escenario de bloque seleccionado.
- [ ] El tiempo de entrada de efectivo en la pestaña 7 refleja la política de pago de CS-01/CS-06.

## Aprobación

| Versión | Fecha | Aprobador | Notas |
|---|---|---|---|
| 0.1 BORRADOR | [RELLENO] | [RELLENO] | Estructura inicial del CS-01 |
| 0.2 BORRADOR | 2026-07-14 | [RELLENO] | Se agregó el factor de uso redondo, Pestaña 6.A, derivación de referencia, Pestaña 10 institucional cerrada, política de tipo de cambio, columna de flujo de efectivo, filas de paquetes de gas de 2/3/4. |
| 0.3 PROPUESTA | 2026-07-14 | Pendiente de revisión financiera/comercial | Se agregaron cantidades de mano de obra provisionales aprobadas y se consolidaron los insumos de viabilidad faltantes; No hay precio aprobado. |
