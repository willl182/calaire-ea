# CS-01 — Hoja de Decisión Comercial

**Propietario:** Profesional de proyectos
**Próxima revisión:** al completar costos, validación técnica y revisión jurídica
**Última revisión:** 2026-07-14 (entrevista decisión institucional y aprobación de propuesta)
**Referencia de códigos del SGC:** ver `00_control/equivalencia_codigos_sgc.md` para el mapeo de códigos PSEA / F-PSEA / I-PSEA / DG-PSEA tras la renumeración del 2026-06-14.

## Objetivo

Fuente única de verdad para alcance, precio, condiciones y reclamos. Evita contradicciones entre folletos, cotizaciones, formularios de registro, términos y correos electrónicos de los clientes.

## 1. Identidad del servicio

| Campo | Valor aprobado | Pruebas/fuente de entrada |
|---|---|---|
| Nombre del servicio | Ensayos de Aptitud para Gases Contaminantes Criterio | decisión institucional del 2026-07-14 |
| Identidad legal del proveedor | Universidad Nacional de Colombia, NIT 899.999.063-3, Sede Medellín | confirmación institucional del 2026-07-14; documentos oficiales de contratación UNAL |
| Unidad ejecutora | Facultad de Minas, Laboratorio CALAIRE | confirmación institucional del 2026-07-14 |
| Contacto para quejas | Profesional de proyectos — `calaire_med@unal.edu.co` (recepción y registro); Profesional de calidad (clasificación y supervisión SGC) | decisión institucional del 2026-07-14; `P-PSEA-17` |
| Idioma de trabajo del servicio (interfaz comercial) | Español | decisión institucional del 2026-07-14 |
| Idiomas de publicación del servicio (catálogo, EoI, términos) | Español | decisión institucional del 2026-07-14; ver CS-02 sección 12 y CS-08 cláusula 18 |

### Roles del equipo

| Rol |
|---|
| Directora del grupo |
| Líder técnico |
| Profesional de proyectos |
| Profesional de infraestructura |
| Técnico instrumental especializado (respaldo técnico) |
| Profesional de calidad |

## 2. Alcance y paquetes seleccionables

| Gas | Unidades de reporte | Capacidad por gas individual |
|---|---|---|
| CO | µmol/mol | 4 analizadores participantes |
| SO₂ | nmol/mol | 4 analizadores participantes |
| NO | nmol/mol | 4 analizadores participantes |
| NO₂ | nmol/mol | 4 analizadores participantes |
| O₃ | nmol/mol | 4 analizadores participantes |

**Definiciones de los paquetes**

- Participación en un solo bloque: uno de CO, SO₂, O₃ o NO/NO₂.
- Participación multibloque: dos o tres bloques seleccionados.
- Participación completa: los cuatro bloques (CO, SO₂, O₃ y NO/NO₂).

**Unidad estándar de participación:** una organización registrada bajo un código de
participante, con derecho a inscribir hasta un analizador por cada bloque
contratado. La participación completa puede comprender hasta cuatro
analizadores: uno para CO, uno para SO₂, uno para O₃ y uno para el bloque
NO/NO₂. Cada analizador consume un cupo operativo en su bloque, pero el precio
no se calcula por analizador.

**Analizador adicional en el mismo bloque:** puede admitirse si queda capacidad
residual después de asignar un cupo primario a cada organización elegible. No
es excluyente, pero requiere revisión de capacidad en CS-09 y no puede desplazar
a otra organización de su primer cupo en ese bloque. Su tratamiento de precio
es provisionalmente sin recargo durante la etapa de propuesta; puede revisarse
cuando CS-04 disponga de costos y evidencia operativa.

## 3. Ancla de precio y objetivo

| Artículo | Valor aprobado | Pruebas/fuente de entrada |
|---|---|---|
| Referencia por ronda (sin impuestos) | Aproximadamente COP 5.928.000 por organización participante, tanto para uno como para los cuatro bloques de gases; incluye hasta un analizador por bloque y no es un precio aprobado | conversión indicativa de la referencia comparativa de EUR 1.600 al 2026-07-14: TRM COP 3.248,87/USD × referencia BCE 1,1404 USD/EUR; acumulación de costos en CS-04 antes de aprobar |
| Objetivo de precios | Propuesta para lanzamiento y validación comercial; sin meta de margen ni subsidio comprometido. Antes de emitir una oferta real, el precio no debe quedar por debajo del costo directo de ejecución calculado en CS-04. | decisión institucional del 2026-07-14; referencia al apartado 8.6 del plan |
| Moneda de facturación | COP | decisión institucional del 2026-07-14 |
| Método de tipo de cambio | Para convertir referencias en EUR: tasa cruzada formada con la TRM USD/COP certificada por la Superintendencia Financiera y la referencia EUR/USD del BCE vigentes o más recientes disponibles en la fecha del cálculo. | decisión institucional del 2026-07-14 |
| Política monetaria (facturación ≠ cálculo de costos) | Cotización y facturación únicamente en COP. El valor queda fijo en COP durante la vigencia de la cotización; referencias en moneda extranjera no constituyen precio ofrecido. | decisión institucional del 2026-07-14 |
| Impuestos | Precio expresado antes de impuestos. Los impuestos y retenciones aplicables serán determinados por la Universidad Nacional de Colombia al emitir cada cotización. No se presume una tarifa hasta validación financiera institucional. | decisión institucional del 2026-07-14; validación financiera requerida antes de cotizar |
| Validez de la cotización | 30 días calendario desde su emisión, sin exceder la fecha límite de inscripción ni permanecer vigente dentro de los 15 días anteriores al inicio de la ronda | decisión institucional del 2026-07-14; ver CS-06 sección 1 |
| Plazo de aceptación (después del cual se retira la oferta) | La primera fecha entre: vencimiento de los 30 días, fecha límite de inscripción, 15 días antes del inicio de la ronda o agotamiento de la capacidad aplicable | decisión institucional del 2026-07-14 |
| Regla de precio del paquete | Tarifa plana provisional por organización participante: el mismo valor para seleccionar entre uno y cuatro bloques. Los bloques son CO, SO₂, O₃ y NO/NO₂. | decisión institucional del 2026-07-14; modelo de referencia UBA |

**Política monetaria** (subsección que se debe documentar antes de aprobar):

- Si la moneda de facturación es distinta a la moneda de costo, documentar: tipo de cambio de referencia, frecuencia de actualización, quién autoriza revaluaciones, y si el riesgo cambiario lo asume CALAIRE-EA o el cliente.
- La pestaña 1 de CS-04 (Supuestos) debe referenciar la misma política.

**Arquitectura**

```text
Precio del participante = tarifa fija por ronda y organización participante
                          para uno a cuatro bloques de gases seleccionados
```

- La tarifa provisional no cambia entre uno y cuatro bloques seleccionados.
- El bloque NO/NO₂ se contrata y opera como una sola unidad con un analizador NOx.
- La tarifa incluye hasta un analizador por bloque contratado.

## 4. Límites de capacidad

| Configuración | Límite de planificación comercial actual |
|---|---|
| Gas operado individualmente | 4 participantes / analizadores |
| CO y SO₂ funcionan simultáneamente | 3 participantes, hasta 2 analizadores cada uno; 6 analizadores participantes en total |

La capacidad se reserva por analizador y configuración, no solo por organización.
Estos valores son límites provisionales de planificación; su validación queda
en espera del T700U.

**Puerta de verificación de capacidad:** antes de aceptar un pedido, la verificación CS-09 #4 debe confirmar que el pedido se mantiene dentro de estos límites y que la capacidad residual después del pedido es al menos 0. Si un pedido consume el último cupo, el siguiente debe ir a una lista de espera (CS-10) con la regla de prioridad documentada.

## 5. Asignación de costos del ciclo de vida

Provisión anual aprobada a recuperar mediante cuotas por ronda:

| Activo | Categorías de costos incluidas | Método de asignación |
|---|---|---|
| Analizador de O₃ / sistema de referencia | Mantenimiento preventivo, lámparas, depuradores, filtros, reparaciones, repuestos | Específico del gas |
| Analizador de SO₂ | Mantenimiento preventivo, lámparas, filtros, bombas, reparaciones, repuestos | Específico del gas |
| Analizador de CO | Mantenimiento preventivo, filtros, bombas, reparaciones, repuestos | Específico del gas |
| Analizador de NOx | Mantenimiento preventivo, convertidor, ozonizador, bombas, filtros, reparaciones, repuestos | Específico del gas |
| Calibrador dinámico | Calibración, servicio MFC, sellos, válvulas, mantenimiento, reparación | Tarifa común u horas de uso |
| Generador de aire cero | Reemplazo de catalizador/depurador/filtro, servicio y reparación de compresores/bombas | Tarifa común u horas de uso |

**Fórmula de asignación por ronda**

```text
Provisión anual del ciclo de vida
    = mantenimiento planificado + consumibles + calibración/servicio
    + provisión para reparaciones correctivas basada en riesgos

Asignación por ronda
    = provisión anual del ciclo de vida × factor documentado de uso por ronda
```

El **factor de uso por ronda** (fracción del año de uso intensivo del equipo atribuible a una ronda típica) debe documentarse en la pestaña 4 de CS-04, columna "Factor de uso por ronda", con su evidencia (historial de uso, campañas anteriores, plan de mantenimiento). Sin este factor la asignación por ronda no se puede calcular.

Las piezas y los intervalos exactos deben provenir de los modelos de equipos instalados, programas del fabricante, cotizaciones de servicio o historial de mantenimiento.

**Responsables de la evidencia:** Profesional de infraestructura levanta inventario, modelo, serie y estado;
Técnico instrumental especializado (respaldo técnico) identifica repuestos, consumibles, mantenimiento e intervalos;
Profesional de proyectos obtiene cotizaciones y costos; Líder técnico valida la pertinencia
técnica; Directora del grupo aprueba su incorporación al modelo CS-04.

## 6. Estrategia de cilindros de gas certificado

| Criterio | Mezcla multicomponente | Cilindros individuales | Híbrida |
|---|---|---|---|
| Adquisiciones | Menos pedidos/cilindros | Varios pedidos/cilindros | Utilice la mezcla existente para lanzar; compare opciones de reemplazo antes de comprar |
| Concentraciones | Una especificación para todas las diluciones | Optimizado por gas | Las especificaciones de CO/SO₂/NOx existentes deben compararse con los niveles previstos.
| Estabilidad / compatibilidad | Debe ser certificablemente estable | Gestionado por separado | Mezcla aceptada únicamente con evidencia válida de estabilidad específica del componente |
| Trazabilidad | Un certificado, valores de los componentes | Certificados separados | El certificado existente debe indicar valores e incertidumbres para CO, SO₂ y NOx |
| Costo del paquete | Más difícil de asignar a las ventas de un solo gas | Mapas directamente al paquete de gas | La tarifa fija hace que la asignación compartida sea aceptable para la propuesta |
| Fallo / Caducidad | Un problema puede afectar a varios gases | Aislado a un gas | La comparación de reemplazo debe valorar el riesgo correlacionado de falla/caducidad |
| Equipos / almacenamiento | Menos reguladores/conexiones | Más reguladores, almacenamiento, manipulación | La configuración existente favorece la mezcla si es técnicamente adecuada |
| Plazo de entrega | Disponibilidad de mezclas personalizadas | Varía según el gas | Obtenga plazos de entrega de proveedores comparables antes de la aprobación del reemplazo |
| Costo estimado por ronda (COP / EUR) | [POR DILIGENCIAR — de CS-04 Pestaña 5] | [POR DILIGENCIAR] | [POR DILIGENCIAR] |

**Estrategia aprobada:** mezcla multicomponente CO/SO₂/NOx como referencia
provisional para el lanzamiento, usando el cilindro existente solo si su
certificado, vigencia, concentraciones, incertidumbres y estabilidad son
adecuados. O₃ se genera fotométricamente. Antes de reponer inventario, CS-04
debe comparar una nueva mezcla equivalente contra cilindros individuales.  
**Aprobador técnico:** Directora del grupo, con concepto técnico de Líder técnico
**Aprobador comercial/financiero:** pendiente de aprobación institucional sobre la comparación de costos

**Nota sobre el alcance híbrido:** la columna "Híbrida" de esta tabla y de la pestaña 5 de CS-04 es la única que admite combinaciones documentadas (p. ej., mezcla certificada compatible + cilindro individual para un gas que requiere concentración o estabilidad distinta). Sin documentación explícita no se aprueba una estrategia "híbrida" en CS-01.

## 7. Normas de inscripción y confirmación

| Regla | Valor aprobado | Pruebas/fuente de entrada |
|---|---|---|
| Inscripción mínima (participantes) | 1 organización confirmada como mínimo operativo provisional | decisión institucional del 2026-07-14; técnicamente compatible con la regla de valor asignado para menos de 12 resultados |
| Inscripción mínima (umbral de ingresos) | Pendiente de CS-04 | análisis de viabilidad CS-04 |
| Inscripción máxima | Limitada por los límites de capacidad anteriores | sección 4 |
| Condición de confirmación | Revisión de alcance/capacidad Y pago u orden de compra aceptados | CS-09, CS-10 |
| Fecha límite de pago/PO después del registro | 15 días calendario por defecto, sin exceder el cierre de inscripción. Prevalecen las políticas financieras y contractuales vigentes de la Universidad Nacional de Colombia; cualquier plazo distinto debe constar en la cotización. Al vencer sin pago ni orden aceptable, el cupo se libera y la solicitud requiere nueva revisión. | decisión institucional del 2026-07-14; CS-10 columna "Plazo de pago" |
| Criterios de prioridad de la lista de espera | Primero, solicitudes completas y elegibles de laboratorios acreditados, en estricto orden de fecha y hora de completitud. Después, las demás organizaciones elegibles, también por orden de completitud. La expresión de interés no reserva prioridad. | decisión institucional del 2026-07-14; sección "Lista de espera" de CS-10 |
| Política de pago parcial | Se rige exclusivamente por las políticas financieras y contractuales vigentes de la Universidad Nacional de Colombia. La cotización debe indicar la modalidad autorizada y CS-09 debe verificar su cumplimiento antes de confirmar el cupo. | decisión institucional del 2026-07-14; CS-06 y CS-09 |

<!-- Por discutir en equipo: si se ejecuta una ronda pagada cuando el ingreso confirmado no cubre el costo directo (depende de CS-04). -->

## 8. Cancelación y aplazamiento

| Escenario | Regla | Tarifa / reembolso | Referencia |
|---|---|---|---|
| Baja de participantes ≥ 30 días calendario antes del inicio de la ronda | El participante puede solicitar una única reprogramación (sujeta a capacidad) o cancelar. | Si cancela, la devolución de lo pagado menos únicamente costos directos no recuperables, ya incurridos, documentados y permitidos por las políticas de la Universidad. Sin penalidad porcentual genérica. | CS-12 |
| Baja de participantes < 30 días calendario antes del inicio de la ronda | El participante puede solicitar una única reprogramación, sujeta a capacidad y al pago de costos incrementales documentados. | No hay devolución automática. Si no se reprograma, solo se reconoce el saldo recuperable que determina los costos efectivamente comprometidos y las políticas financieras de la Universidad. | CS-12 |
| Participante no presentado | La inasistencia sin aviso no genera reprogramación automática. Solo puede evaluarse una excepción por fuerza mayor demostrada y registrada. | Sin devolución, salvo decisión excepcional permitida por las políticas de la Universidad y documentada en CS-12. | CS-12 |
| Sustitución de participantes (analizador u organización) | Cambio de analizador dentro de la misma organización: permitido hasta 15 días antes del inicio, sujeto a nueva revisión técnica y sin cambiar gases ni capacidad. Cambio de organización: requiere nuevo registro, aceptación de términos y revisión CS-09; el cupo solo se conserva si la nueva organización completa la aceptación dentro del plazo. | Sin tarifa administrativa genérica; se cobrarán únicamente costos adicionales documentados y permitidos por la Universidad. | CS-08 cláusula 8 |
| Aplazamiento por el proveedor (fuerza mayor o logística) | Notificación con al menos 15 días calendario cuando la causa sea previsible; ante una emergencia, tan pronto como sea razonablemente posible. El participante elige conservar el cupo en la nueva fecha, trasladarlo a otra ronda disponible o cancelar. | Devolución del 100 % si el participante elige cancelar, conforme al trámite financiero de la Universidad; sin penalidad. | Disparador 4 de CS-12 |
| Cancelación de proveedor (incumplimiento de inscripción mínima o imposibilidad técnica/logística) | CALAIRE-EA notifica formalmente y ofrece conservar el cupo para una fecha reprogramada o cancelar la participación, a elección del participante. | Devolución del 100 % de lo pagado si el participante elige cancelar, tramitada conforme a las políticas financieras de la Universidad; sin penalidad. | Gatillo CS-12 5 |
| Fuerza mayor que afecta la participación | Acontecimiento externo, imprevisible e irresistible que impide el cumplimiento, evaluado caso por caso conforme al derecho colombiano. Puede incluir desastre natural, incendio no atribuible, emergencia sanitaria, orden de autoridad, alteración grave del orden público o interrupción crítica externa. No incluye fallas evitables, falta de mantenimiento, falta de fondos ni problemas ordinarios de personal. La parte afectada debe mitigar, documentar y notificar oportunamente. | Reprogramación o reconocimiento del saldo recuperable según el impacto, los costos comprometidos y las políticas de la Universidad; requiere registro y decisión en CS-12. | Disparador 7 de CS-12; revisión jurídica requerida |
| Plazo de procesamiento del reembolso | El establecido por las políticas y procedimientos vigentes de la Universidad Nacional de Colombia, contado desde que la solicitud queda completa y aprobada. La cotización debe informar el plazo institucional aplicable antes del pago. | política financiera institucional | CS-12 |
| Vigencia de la nota crédito | La emisión, aplicación, vigencia y tratamiento de saldos mediante nota crédito se rigen exclusivamente por las políticas contables y financieras de la Universidad Nacional de Colombia y deben documentarse en cada caso. | política financiera institucional | CS-12 |

**Definición de fuerza mayor:** la cláusula de fuerza mayor requiere un perímetro explícito. Sin lista taxativa o referencia a una ley marco, la cláusula se vuelve litigable. Referenciar aquí el catálogo de eventos cubiertos o la ley aplicable.

## 9. Acreditación y reclamaciones

| Regla | Texto aprobado |
|---|---|
| Estado de acreditación | El servicio de preacreditación podrá describir sus bases de diseño pero no podrá afirmar que CALAIRE-EA o la ronda están acreditadas. |
| Informe de uso | El participante podrá declarar que participó en la Ronda CALAIRE-EA [ID] para los gases [LISTA]. No podrá declarar ni dar a entender que CALAIRE-EA está acreditada, que la ronda está acreditada o que el participante es técnicamente competente únicamente en virtud de su participación. El informe debe utilizarse íntegramente y sin representaciones engañosas de sus resultados o alcance. La evaluación detallada del desempeño se proporciona en el informe técnico separado. La distribución de este informe o su contenido a terceros requiere autorización escrita de CALAIRE-EA. |

**Texto estándar del recordatorio de uso de informes** está en CS-13; mantener consistencia. Cualquier variación debe aprobarse en ambos lugares.

## 10. Valor asignado y evaluación

| Condición | Regla |
|---|---|
| Menos de 12 resultados técnicamente válidos | Valor de referencia de CALAIRE-EA |
| Doce o más resultados técnicamente válidos | Sólido consenso de los participantes |
| Indicadores de evaluación | z o z′, con ζ y En donde se puede utilizar información sobre la incertidumbre |
| Calificación agregada | Sin calificación general de aprobado/suspendido |

## 11. Servicios incluidos y excluidos

**Incluye:** inscripción y revisión del pedido; un cupo para un analizador en
cada bloque contratado; preparación y coordinación de la ronda; uso de las
instalaciones y del sistema de generación de CALAIRE; ejecución para los gases
contratados; administración y evaluación de datos; informe técnico digital;
constancia de participación; y atención de aclaraciones, quejas y apelaciones
por los canales del SGC.

**Excluido/a cargo del participante:** transporte del analizador hacia y desde
Medellín; seguro y riesgo del equipo; calibración, mantenimiento o reparación
del analizador del participante; aduanas, visas e impuestos de importación o
exportación; alojamiento, alimentación y demás gastos del personal del
participante.

**Plantilla recomendada para excluidos:**

- Transporte de equipo desde/hacia Medellín (incluye seguro de transporte).
- Riesgo de daño o pérdida del equipo del participante durante la ronda.
- Visas, permisos de ingreso y estadía del personal del participante.
- Aduanas e impuestos de importación / exportación para clientes internacionales.
- Calibración pre-ronda del analizador del participante (debe traer calibración vigente).
- Alojamiento y alimentación del personal del participante.

## Prueba de aceptación

El propietario debe poder responder todos los campos del CS-02 al CS-15 utilizando el CS-01 o una referencia del SGC existente. Si todavía se está inventando una decisión comercial en un correo electrónico, el CS-01 está incompleto.

## Anexo — Guía de evidencias para cada marcador [POR DILIGENCIAR]

Para que un implementador (o un agente de IA) que tome esta tarea pueda completar cada `[POR DILIGENCIAR]` sin ambigüedad, esta tabla indica qué documento o decisión hace falta para cada sección:

| Sección | Marcador [POR DILIGENCIAR] | Documento o decisión de origen |
|---|---|---|
| 1 | Nombre del servicio | propuesta aprobada, nombramiento del SGC |
| 1 | Identidad legal del proveedor | registro mercantil, NIT |
| 1 | Integrantes y cargos del equipo | directorio `pages/Equipo.md`, organigrama y acto institucional aplicable |
| 1 | Idioma de trabajo del servicio | decisión de gerencia comercial |
| 1 | Idiomas de publicación del servicio | decisión de gerencia comercial |
| 2 | Unidades de reporte por gas | P-PSEA-08 (gestión de datos digitales); informe operativo piloto |
| 3 | Objetivo de precios (margen / recuperación de costos / subsidio) | sección 8.6 del plan maestro + decisión de la gerencia |
| 3 | Moneda de facturación | política financiera |
| 3 | Método de tipo de cambio | política financiera |
| 3 | Impuestos | asesor tributario |
| 3 | Validez de la cotización | CS-06 |
| 3 | Plazo de aceptación | CS-06 |
| 3 | Precio fijo y tratamiento de analizador adicional | decisión institucional; validación de costos en CS-04 Tab 6 |
| 6 | Columna híbrida | pestaña 5 de CS-04; aprobación técnica + comercial |
| 6 | Estrategia aprobada + aprobadores | CS-04 Pestaña 5; ambos firmantes |
| 7 | Inscripción mínima (cantidad + ingresos) | pestañas 7/8 de CS-04 |
| 7 | Fecha límite de pago/orden de compra | CS-10 |
| 7 | Criterios de prioridad de la lista de espera | CS-10 |
| 7 | Política de pago parcial | CS-06, CS-10 |
| 8 | Toda la tabla | CS-12 (tarifas de cancelación) + política financiera |
| 9 | Informe de uso | CS-13 (estándar de recordatorio de uso de informes) |
| 11 | Incluido / Excluido | CS-06 secciones 6/7, CS-08 cláusula 4 |
