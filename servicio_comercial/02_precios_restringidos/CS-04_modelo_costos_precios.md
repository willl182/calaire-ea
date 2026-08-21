# CS-04 — Modelo de precios y lista de precios aprobada

**Propietario:** Profesional de proyectos
**Última revisión:** 2026-07-14 (supuestos laborales provisionales aprobados registrados e insumos de viabilidad faltantes consolidados)
**Referencia de códigos del SGC:** ver `00_control/equivalencia_codigos_sgc.md`. Los códigos PSEA / F-PSEA referenciados en este modelo apuntan a los significados vigentes tras la renumeración del 2026-06-14.

## Objetivo

Validar la tarifa plana provisional, calcular los costos reales y la viabilidad, y
respaldar una futura revisión de precios sin asumir una facturación basada en el gas o el analizador.

## Arquitectura de precios

```text
Precio del participante = tarifa fija por ronda y organización participante
                          para uno a cuatro bloques seleccionados
```

La propuesta utiliza **COP 5.928.000 sin impuestos por organización participante**, ya sea que seleccione de uno a cuatro bloques: CO, SO₂, O₃ y NO/NO₂.
El importe es una conversión indicativa de 1.600 EUR, no un precio aprobado y
no sustituye el modelo de costos. Incluye hasta un analizador por bloque;
puede aceptarse un analizador adicional sin recargo solo cuando exista
capacidad residual.

## Pestañas del libro de cálculo

El modelo de costos se implementa en el libro `CS-04_modelo_costos_precios.xlsx` (esta misma carpeta), generado sobre la plantilla `F-PSEA-01 Plantilla Formato_Excel.xlsx` mediante `scripts/build_cs04_modelo.py`. Este documento define el contenido requerido para cada pestaña.

### Pestaña 1 — Supuestos

| Asunción | Valor | Fuente/responsable |
|---|---|---|
| Tasa de cambio de referencia | TRM USD/COP × referencia BCE USD/EUR, solo para convertir valores de referencia | CS-01 |
| Frecuencia de actualización del tipo de cambio | En la fecha de revisión de la referencia comparativa | CS-01 |
| Asignación del riesgo cambiario | No aplica a clientes: cotización y facturación únicamente en COP | CS-01 |
| Capacidad por gas (individual) | 4 analizadores | CS-01 |
| Capacidad simultánea de CO/SO₂ | 3 participantes, 6 analizadores | CS-01 |
| Inscripción prevista | [POR DILIGENCIAR] | Estimación de mercado |
| Impuestos (IVA, retenciones, etc.) | [POR DILIGENCIAR] | Asesor tributario |
| Diferencial tributario para clientes internacionales | [POR DILIGENCIAR — exención de IVA, retención, aplicación de tratados] | Asesor tributario |
| Margen / objetivo previsto | Lanzamiento y validación; sin margen ni subsidio comprometidos; no cotizar bajo el costo directo | CS-01 |
| Factor de uso por ronda para la asignación del ciclo de vida | [POR DILIGENCIAR — fracción entre 0 y 1] | Responsable técnico (basado en historial de uso) |
| Momento de cobro del pago (predeterminado) | [POR DILIGENCIAR — por ejemplo, 100 % anticipado / 50 % con la orden + 50 % antes de la ronda / orden de compra a 30 días] | Política financiera |
| Calendario de cobro de pagos (institucional) | [POR DILIGENCIAR] | Política financiera |

### Supuestos laborales provisionales – tarifas no aprobadas

Estas cantidades se pueden utilizar únicamente para la planificación. El costeo monetario permanece
bloqueado hasta que el Profesional de proyectos defina la tarifa horaria y el tratamiento de las
cargas laborales de cada rol. Una cantidad solo se reemplaza con evidencia operativa fechada.

| Rol/recurso | Cantidad provisional por ronda | Estado de costeo |
|---|---:|---|
| Operación técnica | 72h | Horas aprobadas como supuesto de planificación; tasa pendiente |
| Coordinación | 68h | 36 h de operación + 12 h de planificación/cierre + 12 h de cálculos + 8 h de informe final; tasa pendiente |
| Infraestructura | Hasta 4 h por actividad efectiva/semana activa | No multiplique por el calendario completo; registro de actividad y tasa pendiente |
| Proyectos | Hasta 4 h por actividad efectiva/semana activa | No multiplique por el calendario completo; registro de actividad y tasa pendiente |
| Calidad del aire | Hasta 4 h por actividad efectiva/semana activa | No multiplique por el calendario completo; registro de actividad y tasa pendiente |
| Gestión de Calidad | Hasta 4 h por actividad efectiva/semana activa | No multiplique por el calendario completo; registro de actividad y tasa pendiente |
| Instalaciones | Aporte institucional, sin cuantificar | No inventar alquileres ni servicios públicos; la Directora del grupo puede revisar el tratamiento |

### Pestaña 2 — Costo común

| Elemento de costo | Importe anual | Asignación por ronda | Notas |
|---|---|---|---|
| Coordinación | [POR DILIGENCIAR] | [POR DILIGENCIAR] | |
| Preparación de instalaciones | [POR DILIGENCIAR] | [POR DILIGENCIAR] | |
| Registro y administración de datos | [POR DILIGENCIAR] | [POR DILIGENCIAR] | |
| Entrega de informes | [POR DILIGENCIAR] | [POR DILIGENCIAR] | |
| Equipo compartido (calibrador, generador de aire cero) | [POR DILIGENCIAR] | [POR DILIGENCIAR] | Desde la pestaña 4 |

### Pestaña 3 — Costo por gas

| Bloque | Costo del cilindro / generación | Ciclo de vida específico del analizador | Asignación de costos | Notas |
|---|---|---|---|---|
| CO | [POR DILIGENCIAR] | [POR DILIGENCIAR] | [CÁLCULO] | |
| SO₂ | [POR DILIGENCIAR] | [POR DILIGENCIAR] | [CÁLCULO] | |
| NO/NO₂ | [POR DILIGENCIAR] | [POR DILIGENCIAR] | [CÁLCULO] | Un solo bloque NOx |
| O₃ | [POR DILIGENCIAR] | [POR DILIGENCIAR] | [CÁLCULO] | |

### Pestaña 4 — Ciclo de vida de los equipos

Provisión anual para todos los equipos CALAIRE identificados:

| Activo | Mantenimiento planificado | Consumibles | Calibración / servicio | Provisión de reparación correctiva basada en riesgos | Provisión anual total | **Factor de uso por ronda** | **Asignación por ronda** |
|---|---|---|---|---|---|---|---|
| Analizador / sistema de referencia de O₃ | [POR DILIGENCIAR] | [POR DILIGENCIAR] | [POR DILIGENCIAR] | [POR DILIGENCIAR] | [CÁLCULO] | [POR DILIGENCIAR — 0–1] | [CÁLCULO] |
| Analizador de SO₂ | [POR DILIGENCIAR] | [POR DILIGENCIAR] | [POR DILIGENCIAR] | [POR DILIGENCIAR] | [CÁLCULO] | [POR DILIGENCIAR — 0–1] | [CÁLCULO] |
| Analizador de CO | [POR DILIGENCIAR] | [POR DILIGENCIAR] | [POR DILIGENCIAR] | [POR DILIGENCIAR] | [CÁLCULO] | [POR DILIGENCIAR — 0–1] | [CÁLCULO] |
| Analizador de NOx | [POR DILIGENCIAR] | [POR DILIGENCIAR] | [POR DILIGENCIAR] | [POR DILIGENCIAR] | [CÁLCULO] | [POR DILIGENCIAR — 0–1] | [CÁLCULO] |
| Calibrador dinámico | [POR DILIGENCIAR] | [POR DILIGENCIAR] | [POR DILIGENCIAR] | [POR DILIGENCIAR] | [CÁLCULO] | [POR DILIGENCIAR — 0–1] | [CÁLCULO] |
| Generador de aire cero | [POR DILIGENCIAR] | [POR DILIGENCIAR] | [POR DILIGENCIAR] | [POR DILIGENCIAR] | [CÁLCULO] | [POR DILIGENCIAR — 0–1] | [CÁLCULO] |

**Factor de uso por ronda (FUR):** fracción del año de uso intensivo del equipo atribuible a una ronda típica. Se estima a partir del historial de campañas (horas de uso / horas totales disponibles) o, en su defecto, a partir del plan de mantenimiento del fabricante. Sin este factor, la asignación por ronda no se puede calcular.

**Fórmula:**

```text
Provisión anual del ciclo de vida
    = mantenimiento planificado + consumibles + calibración/servicio
    + provisión para reparaciones correctivas basada en riesgos

Asignación por ronda
    = provisión anual del ciclo de vida × factor de uso por ronda (FUR)
```

Las piezas y los intervalos exactos deben provenir de los modelos de equipos instalados, programas del fabricante, cotizaciones de servicio o historial de mantenimiento.

### Pestaña 5 — Estrategia de cilindros

Compare mezclas multicomponentes, cilindros individuales y opciones híbridas:

| Criterio | Mezcla multicomponente | Cilindros individuales | Híbrida (si aplica) |
|---|---|---|---|
| Adquisición | Menos pedidos / cilindros | Varios pedidos / cilindros | [POR DILIGENCIAR] |
| Concentraciones | Una especificación debe adaptarse a todas las diluciones | Optimizado por gas | [POR DILIGENCIAR] |
| Estabilidad / compatibilidad | Debe ser certificablemente estable | Gestionado por separado | [POR DILIGENCIAR] |
| Trazabilidad | Un certificado, valores por componente | Certificados separados | [POR DILIGENCIAR] |
| Cálculo de costos del paquete | Más difícil de asignar a ventas de un solo gas | Se asigna directamente al paquete de gases | [POR DILIGENCIAR] |
| Falla / vencimiento | Un problema puede afectar varios gases | Aislado a un solo gas | [POR DILIGENCIAR] |
| Equipos / almacenamiento | Menos reguladores / conexiones | Más reguladores, almacenamiento y manipulación | [POR DILIGENCIAR] |
| Plazo de entrega | Disponibilidad de mezclas personalizadas | Varía según el gas | [POR DILIGENCIAR] |
| Costo estimado por ronda (COP / EUR) | [POR DILIGENCIAR] | [POR DILIGENCIAR] | [POR DILIGENCIAR] |
| **Recomendación** | [POR DILIGENCIAR] | [POR DILIGENCIAR] | [POR DILIGENCIAR] |

**Estrategia aprobada:** [POR DILIGENCIAR]
**Aprobador técnico:** [POR DILIGENCIAR]
**Aprobador comercial/financiero:** [POR DILIGENCIAR]

### Pestaña 6 — Tarifa fija de participación

| Bloques seleccionados | Analizadores incluidos | Tarifa provisional sin impuestos | Analizador adicional con capacidad residual | Notas |
|---|---:|---:|---:|---|
| Cualquier 1 bloque | Hasta 1 | COP 5.928.000 | COP 0 | Solo propuesta |
| Cualquier 2 bloques | Hasta 2, uno por bloque | COP 5.928.000 | COP 0 | Solo propuesta |
| 3 bloques cualesquiera | Hasta 3, uno por bloque | COP 5.928.000 | COP 0 | Solo propuesta |
| Los 4 bloques | Hasta 4, uno por bloque | COP 5.928.000 | COP 0 | CO, SO₂, O₃ y NO/NO₂ |

Un analizador adicional nunca desplaza el primer cupo de otra organización
y requiere revisión de capacidad CS-09.

### Pestaña 6.A — Validación del valor de referencia

Esta pestaña compara el costo real (directo y total) por organización participante
contra COP 5.928.000. Debe mostrar el costo por separado para cada escenario de
bloques seleccionados, aunque el precio propuesto al cliente sea fijo.

| Medida | Valor (COP) | Fuente / calculo |
|---|---:|---|
| Costo directo, 1 bloque | [CÁLCULO] | Pestañas 2–4 |
| Costo directo, 2 bloques | [CÁLCULO] | Pestañas 2–4 |
| Costo directo, 3 bloques | [CÁLCULO] | Pestañas 2–4 |
| Costo directo, 4 bloques | [CÁLCULO] | Pestañas 2–4 |
| Costo total asignado, 4 bloques | [CÁLCULO] | Pestañas 2–4 |
| Tarifa plana provisional | 5.928.000 | CS-01 |
| Contribución / déficit por escenario | [CÁLCULO] | tarifa − costo |
| **Interpretación/decisión** | [POR DILIGENCIAR] | aprobación de la dirección antes de la cotización |

### Pestaña 7 — Inscripción

| Escenario | Participantes | Analizadores | Ingresos | Costos | Contribución | Momento de entrada del efectivo | ¿Viable? |
|---|---|---|---|---|---|---|---|
| Baja (1 participante, 1 gas) | 1 | 1 | [CÁLCULO] | [CÁLCULO] | [CÁLCULO] | [POR DILIGENCIAR] | [POR DILIGENCIAR] |
| Previsto | [POR DILIGENCIAR] | [POR DILIGENCIAR] | [CÁLCULO] | [CÁLCULO] | [CÁLCULO] | [POR DILIGENCIAR] | [POR DILIGENCIAR] |
| Capacidad total para un gas individual | 4 | 4 | [CÁLCULO] | [CÁLCULO] | [CÁLCULO] | [POR DILIGENCIAR] | [POR DILIGENCIAR] |
| Capacidad total simultánea de CO/SO₂ | 3 | 6 | [CÁLCULO] | [CÁLCULO] | [CÁLCULO] | [POR DILIGENCIAR] | [POR DILIGENCIAR] |
| Selección mixta | [POR DILIGENCIAR] | [POR DILIGENCIAR] | [CÁLCULO] | [CÁLCULO] | [CÁLCULO] | [POR DILIGENCIAR] | [POR DILIGENCIAR] |

**Momento de la entrada de efectivo:** columna crítica para entender la viabilidad real. Si el ingreso se cobra 100% anticipado y los costos se pagan durante la ronda, la viabilidad operativa es muy distinta a un escenario de pago a 30 días. CS-06 sección 9 y CS-10 columna "PO/pago/estado de factura" usan esta misma escala temporal.

### Pestaña 8 — Escenarios

| Escenario | Descripción | Resultado |
|---|---|---|
| Punto de equilibrio para gas individual | Cupos pagados mínimos para cubrir el costo | [CÁLCULO] |
| Punto de equilibrio para CO/SO₂ simultáneos | Cupos pagados mínimos para cubrir el costo | [CÁLCULO] |
| Punto de equilibrio para el paquete completo | Cupos pagados mínimos para cubrir el costo | [CÁLCULO] |
| Capacidad baja | 1–2 participantes | [CÁLCULO] |
| Capacidad prevista | [POR DILIGENCIAR] | [CÁLCULO] |
| Capacidad total | Según los límites de CS-01 | [CÁLCULO] |
| Flujo de caja en el peor de los casos (matriculación baja + pagos atrasados) | Tensión de caja | [CÁLCULO] |

### Pestaña 9 — Aprobación

| Campo | Valor |
|---|---|
| Cuota fija de participación aprobada | [POR DILIGENCIAR] |
| Ajuste de bloque seleccionado aprobado | COP 0 a menos que se revise CS-01 |
| Tarifa de analizador adicional aprobada | COP 0 durante la etapa de propuesta, sujeto a capacidad residual |
| Estrategia de cilindro aprobada (de la pestaña 5) | [POR DILIGENCIAR] |
| Paquetes aprobados (de la pestaña 6) | [POR DILIGENCIAR] |
| Política cambiaria aprobada (de la pestaña 1) | [POR DILIGENCIAR] |
| Calendario de cobro de efectivo aprobado (de la pestaña 1) | [POR DILIGENCIAR] |
| Precios aprobados válidos desde | [POR DILIGENCIAR] |
| Precios aprobados válidos hasta | [POR DILIGENCIAR] |
| Aprobador (comercial/financiero) | [POR DILIGENCIAR — nombre, fecha y firma] |
| Aprobador (técnico) | [POR DILIGENCIAR — nombre, fecha y firma] |
| Aprobador (dirección) | [POR DILIGENCIAR — NOMBRE, FECHA, FIRMA] |

## Lista de precios orientada al cliente

La lista externa (consulte `listas_precios_aprobadas.md`) muestra solo los precios aprobados, la moneda, los impuestos, las inclusiones, la tarifa del analizador adicional, la validez y los requisitos de cotización. Los detalles de costos internos y márgenes siguen siendo restringidos.

## Comprobaciones de lógica comercial

- [ ] La tarifa fija se muestra consistentemente para uno a cuatro bloques seleccionados.
- [ ] Se acepta un analizador adicional solo con capacidad residual y no desplaza una primera posición.
- [ ] Se documentan el objetivo de la propuesta y el costo mínimo directo del CS-01.
- [ ] El punto de referencia de COP 5.928.000 se compara con la capacidad verificada, no con una ronda supuesta de 8 a 15 participantes.
- [ ] El factor de uso por ronda se completa para cada activo en la pestaña 4.
- [ ] La pestaña 6.A muestra la contribución o el déficit directo y de costo total para cada escenario de bloque seleccionado.
- [ ] El tiempo de entrada de efectivo en la pestaña 7 refleja la política de pago de CS-01/CS-06.
