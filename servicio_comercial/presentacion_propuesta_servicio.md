# Propuesta de Servicio Comercial — Ensayos de Aptitud para Gases Contaminantes Criterio

**Documento técnico para el equipo de trabajo — Laboratorio CALAIRE, Facultad de Minas, Universidad Nacional de Colombia, Sede Medellín**

Estado de la información: 14 de julio de 2026. Fuentes: hoja de decisión comercial (v0.3), registro de artefactos, mapa de viaje del cliente y lineamientos de la carpeta `servicio_comercial/`.

---

## 1. Propósito de este documento

Este documento presenta los elementos que componen la propuesta de servicio comercial para los Ensayos de Aptitud de Gases Contaminantes Criterio (CALAIRE-EA): el conjunto de artefactos que convierten el esquema técnico de ensayos de aptitud existente en un servicio pago contratable. La ejecución técnica de las rondas permanece bajo el sistema de gestión (SG); la capa comercial que aquí se describe la rodea, la referencia y nunca la duplica.

El documento sigue este orden: primero los artefactos que conforman el sistema, luego el recorrido del cliente que los conecta, y finalmente las decisiones de oferta y precio, los controles de aprobación y los roles del equipo.

---

## 2. Los artefactos del sistema comercial

El sistema se compone de quince artefactos operativos, organizados según la etapa del ciclo comercial que atienden. Cada uno tiene un propietario, un estado de aprobación y una función única; ninguno repite información que ya viva en otro.

### 2.1 Artefacto de control central

**[Hoja de decisión comercial](fichas/ficha_01_hoja_decision_comercial.md).** Es la fuente única de verdad para el alcance, el precio, las condiciones y las afirmaciones que se hacen sobre el servicio. Todo folleto, cotización, formulario o correo al cliente debe ser coherente con lo que aquí se decide; si dos documentos se contradicen, esta hoja tiene la autoridad. Su responsable es el Profesional de proyectos y es el único artefacto con propuesta ya aprobada (14 de julio de 2026), con las puertas de liberación aún pendientes.

### 2.2 Artefactos de mercado

Estos tres artefactos ponen el servicio frente a los clientes potenciales antes de cualquier compromiso de compra.

- **[Catálogo de servicios](fichas/ficha_02_catalogo_servicios.md).** Explica y posiciona la oferta: qué es el ensayo de aptitud, qué bloques de gases cubre, qué recibe el participante y bajo qué condiciones. Es el material que un cliente lee primero. Su contenido de propuesta está completo; falta la aprobación de publicación.
- **[Programa anual y convocatoria de ronda](fichas/ficha_03_programa_convocatoria_ronda.md).** Publica las fechas, la capacidad disponible y el alcance seleccionado de cada ronda. La plantilla está completa; los campos específicos de cada ronda se llenan al convocarla.
- **[Formulario de expresión de interés](fichas/ficha_05_expresion_de_interes.md).** Permite validar la demanda antes de abrir ventas: el cliente manifiesta interés en uno o más bloques de gases sin adquirir compromiso. Cada expresión recibida alimenta el rastreador de inscripciones como una oportunidad en etapa de interés.

### 2.3 Artefactos de precio (acceso restringido)

- **[Modelo de costos y precios](fichas/ficha_04_modelo_costos_precios.md).** Es la herramienta donde se acumulan los costos reales de ejecutar una ronda (mantenimiento, consumibles, gases certificados, personal) y donde se calcula el umbral de viabilidad. Ninguna oferta real puede emitirse con un precio por debajo del costo directo que este modelo arroje. Ya está implementado como libro de cálculo sobre la plantilla F-PSEA-01 (`CS-04_modelo_costos_precios.xlsx`); la evidencia de costos sigue pendiente.
- **[Lista de precios aprobada](fichas/ficha_04_modelo_costos_precios.md).** Versión de cara al cliente derivada del modelo de costos. Permanece bloqueada: no existe aún ningún precio aprobado.

Ambos viven en una carpeta de acceso controlado porque contienen datos de costos internos.

### 2.4 Artefactos de venta y contratación

Cuatro artefactos llevan al cliente desde la cotización hasta el pedido aceptado.

- **[Plantilla de cotización](fichas/ficha_06_plantilla_cotizacion.md).** Formaliza la oferta comercial de manera controlada: alcance seleccionado, valor en pesos colombianos, validez y condiciones de aceptación. Nada se ofrece por fuera de esta plantilla.
- **[Formulario de inscripción](fichas/ficha_07_formulario_inscripcion.md).** Captura al comprador: identidad de la organización, alcance seleccionado, datos administrativos y de facturación.
- **[Términos y condiciones](fichas/ficha_08_terminos_condiciones.md).** Acuerdo del participante que establece las condiciones de servicio vinculantes, incluida la cláusula de uso correcto del informe y el tratamiento de datos personales.
- **[Lista de verificación de revisión de contrato](fichas/ficha_09_revision_contrato.md).** Antes de aceptar cualquier pedido, esta lista confirma que CALAIRE-EA realmente puede cumplirlo: que el alcance es el ofrecido, que hay capacidad disponible, que los términos fueron aceptados y que el pago u orden de compra está en regla.

### 2.5 Artefactos de inscripción y confirmación (acceso restringido)

- **[Rastreador de inscripciones e ingresos](fichas/ficha_10_rastreador_inscripciones_ingresos.md).** Es el núcleo operativo del sistema: una hoja de cálculo donde casi todos los demás artefactos leen o escriben. Controla la capacidad, el estado de cada oportunidad (interés → cotizado → registrado → en revisión → confirmado, en lista de espera, rechazado o retirado), los pagos y la viabilidad de la ronda. Ya está implementado, con aprobación pendiente.
- **[Paquete de confirmación, lista de espera, rechazo e incorporación](fichas/ficha_11_paquete_confirmacion_incorporacion.md).** Comunica al cliente el resultado de su pedido y, cuando es confirmado, entrega el paquete de incorporación con los enlaces a los documentos técnicos del SGC. Es el punto de traspaso formal de la capa comercial a la capa técnica.

Esta carpeta también es de acceso controlado porque contiene identidad de participantes.

### 2.6 Artefacto de cambios y reembolsos

**[Registro de cambios, cancelaciones y reembolsos](fichas/ficha_12_registro_cambios_cancelaciones_reembolsos.md).** Toda modificación posterior a la confirmación —cambio de alcance, cancelación, reembolso o crédito— se documenta con autorización del Profesional de proyectos, dejando trazable su efecto económico y de capacidad.

### 2.7 Artefactos de entrega y retención

Tres artefactos cierran el ciclo y siembran el siguiente.

- **[Entrega de informe y declaración de participación](fichas/ficha_13_entrega_informe.md).** Asegura que el informe controlado correcto llegue al destinatario correcto, junto con la declaración de participación, de manera consistente en cada ronda.
- **[Formulario de retroalimentación del cliente](fichas/ficha_14_retroalimentacion_cliente.md).** Mide la experiencia del participante y la demanda futura del servicio.
- **[Mensaje de renovación y registro de clientes potenciales](fichas/ficha_15_renovacion_clientes_potenciales.md).** Convierte cada participación completada en demanda repetida: invita a la siguiente ronda y registra el interés futuro en el rastreador.

### 2.8 Documentos de soporte

Acompañan a los quince artefactos sin ser parte del flujo transaccional: el mapa de viaje del cliente (visualización de cómo se conectan todos los artefactos), el registro de artefactos (lista canónica con propietarios y estados), el registro de cambios de versiones, la tabla de equivalencia de códigos del SGC (necesaria tras la renumeración del 14 de junio de 2026) y las políticas de acceso de las dos carpetas restringidas.

### 2.9 Resumen de estado

| Artefacto | Responsable | Estado |
|---|---|---|
| Hoja de decisión comercial | Profesional de proyectos | Propuesta aprobada; puertas de liberación pendientes |
| Catálogo de servicios | Profesional de proyectos | Contenido completo; aprobación de publicación pendiente |
| Programa anual y convocatoria de ronda | Líder técnico | Plantilla completa; campos de ronda pendientes |
| Modelo de costos y precios | Profesional de proyectos | Libro implementado; evidencia de costos pendiente |
| Formulario de expresión de interés | Profesional de proyectos | Borrador; aprobación pendiente |
| Plantilla de cotización | Profesional de proyectos | Borrador; aprobación pendiente |
| Formulario de inscripción | Profesional de proyectos | Borrador; aprobación pendiente |
| Términos y condiciones | Profesional de proyectos | Borrador; aprobación pendiente |
| Lista de verificación de revisión de contrato | Líder técnico | Borrador; aprobación pendiente |
| Rastreador de inscripciones e ingresos | Profesional de proyectos | Implementado; aprobación pendiente |
| Paquete de confirmación e incorporación | Líder técnico | Borrador; aprobación pendiente |
| Registro de cambios, cancelaciones y reembolsos | Profesional de proyectos | Borrador; aprobación pendiente |
| Entrega de informe y declaración de participación | Líder técnico | Borrador; aprobación pendiente |
| Formulario de retroalimentación del cliente | Profesional de proyectos | Borrador; aprobación pendiente |
| Mensaje de renovación y registro de clientes potenciales | Profesional de proyectos | Borrador; aprobación pendiente |
| Lista de precios aprobada (soporte) | Profesional de proyectos | Bloqueada; ningún precio aprobado |

---

## 3. El recorrido del cliente

Los artefactos no operan aislados: forman una cadena que acompaña al cliente desde el primer contacto hasta la renovación. El recorrido es el siguiente.

1. **Descubrir el servicio.** El cliente conoce la oferta a través del catálogo de servicios y la convocatoria de ronda vigente.
2. **Comprender el alcance y las condiciones.** El catálogo describe qué incluye el servicio, cómo funciona la ronda y bajo qué condiciones se participa.
3. **Expresar interés.** El cliente diligencia el formulario de expresión de interés seleccionando uno o más bloques de gases, sin compromiso. La oportunidad entra al rastreador.
4. **Recibir una cotización controlada.** El Profesional de proyectos emite la cotización con la plantilla oficial; el estado en el rastreador pasa a "cotizado".
5. **Inscribirse y aceptar los términos.** El cliente diligencia el formulario de inscripción y firma los términos y condiciones.
6. **Pasar la revisión de contrato.** La lista de verificación confirma alcance, capacidad, términos y pago antes de aceptar el pedido. Si la capacidad se agota, el pedido pasa a lista de espera con regla de prioridad documentada.
7. **Recibir la confirmación comercial.** El paquete de confirmación comunica la aceptación (o la lista de espera o el rechazo, según el caso).
8. **Recibir las instrucciones técnicas.** El paquete de incorporación entrega los enlaces a los documentos del SGC; desde aquí la ronda es asunto técnico, no comercial.
9. **Participar en la ronda.** Ejecución bajo el SGC.
10. **Recibir el informe.** La entrega del informe y la declaración de participación cierra el compromiso técnico. Si durante la revisión del borrador surgen cambios, interviene el registro de cambios.
11. **Cerrar el ciclo.** Se recoge la retroalimentación, se cierra la facturación y se envía el mensaje de renovación, que alimenta la demanda de la siguiente ronda.

El rastreador de inscripciones e ingresos actúa como sistema nervioso central de todo el recorrido: cada transición de estado del cliente queda registrada allí, y es la vista con la que se controla capacidad y viabilidad en tiempo real.

---

## 4. La oferta: alcance y paquetes

El servicio ofrece ensayos de aptitud para los gases contaminantes criterio, organizados en cuatro bloques contratables:

| Bloque de gas | Unidades de reporte | Capacidad (operación individual) |
|---|---|---|
| Monóxido de carbono (CO) | µmol/mol | 4 analizadores participantes |
| Dióxido de azufre (SO₂) | nmol/mol | 4 analizadores participantes |
| Óxidos de nitrógeno (NO/NO₂) | nmol/mol | 4 analizadores participantes |
| Ozono (O₃) | nmol/mol | 4 analizadores participantes |

Las modalidades de participación son tres: bloque único (uno de los cuatro), multibloque (dos o tres) y participación completa (los cuatro).

La unidad estándar de participación es una organización registrada bajo un código de participante, con derecho a inscribir hasta un analizador por cada bloque contratado; la participación completa puede llegar a cuatro analizadores. La capacidad se reserva por analizador y configuración, no solo por organización. Cuando CO y SO₂ operan simultáneamente, el límite es de tres participantes con hasta dos analizadores cada uno (seis analizadores en total). Todos estos límites son provisionales de planificación y deben validarse con evidencia operativa antes de abrir inscripciones.

---

## 5. Ancla de precio y política monetaria

- **Referencia por ronda:** aproximadamente COP 5.928.000 por organización participante, antes de impuestos, igual para uno o para los cuatro bloques. Es una conversión indicativa del benchmark europeo de EUR 1.600 (tasa cruzada TRM y referencia BCE del 14 de julio de 2026). **No es un precio aprobado:** la acumulación de costos en el modelo de costos debe completarse primero.
- **Regla de paquete:** tarifa plana provisional por organización; el valor no cambia entre uno y cuatro bloques seleccionados, e incluye hasta un analizador por bloque.
- **Moneda:** cotización y facturación únicamente en pesos colombianos; el valor queda fijo en COP durante la vigencia de la cotización. Las referencias en moneda extranjera no constituyen precio ofrecido.
- **Impuestos:** el precio se expresa antes de impuestos; los aplicables los determina la Universidad Nacional de Colombia al emitir cada cotización.
- **Validez de la cotización:** 30 días calendario, sin exceder la fecha límite de inscripción ni quedar vigente dentro de los 15 días previos al inicio de la ronda.
- **Condición de viabilidad:** ninguna oferta real puede emitirse por debajo del costo directo de ejecución calculado en el modelo de costos.

---

## 6. Puertas de aprobación

El sistema no avanza por inercia: siete puertas de control exigen que los artefactos correctos estén aprobados antes de cada paso irreversible.

| Puerta | Qué debe estar listo | Pregunta que responde | Quién aprueba |
|---|---|---|---|
| Lanzamiento al mercado | Hoja de decisión, catálogo, convocatoria, modelo de costos, expresión de interés | ¿La oferta es precisa, tiene precio, es comprensible y está honestamente posicionada? | Profesional de proyectos |
| Lanzamiento de cotización | Modelo de costos aprobado, plantilla de cotización, términos | ¿Se pueden defender y aceptar el precio y las condiciones? | Profesional de proyectos |
| Aceptación del pedido | Inscripción, términos firmados, revisión de contrato aprobada, rastreador actualizado | ¿Se alinean alcance, capacidad, términos y pago? | Profesional de proyectos |
| Traspaso técnico | Confirmación enviada + admisión de planificación de la ronda en el SGC | ¿Puede el proceso técnico actuar sobre el pedido confirmado? | Líder técnico |
| Cambio o reembolso | Registro de cambios abierto con autorización | ¿Está documentado y autorizado el efecto económico y de capacidad? | Profesional de proyectos |
| Entrega de informes | Entrega preparada + aprobación del informe en el SGC | ¿El informe controlado correcto va al destinatario correcto? | Líder técnico |
| Cierre comercial | Retroalimentación recibida, renovación enviada, rastreador cerrado | ¿Se registran los comentarios, el estado de ingresos y el interés futuro? | Profesional de proyectos |

---

## 7. Roles del equipo

| Rol |
|---|
| Directora del grupo |
| Profesional de proyectos |
| Líder técnico |
| Profesional de infraestructura |
| Técnico instrumental especializado (backup técnico) |
| Profesional de calidad |

---

## 8. Reglas transversales que todo el equipo debe conocer

- **El SGC manda.** La fuente de verdad técnica es `docs/qms/`; la capa comercial referencia, nunca duplica. Tras la renumeración de códigos del 14 de junio de 2026, toda cita a un código del SGC debe verificarse en la tabla de equivalencia antes de usarse.
- **Protección de datos.** La Ley 1581 de 2012 aplica al formulario de expresión de interés (consentimiento), a los términos y al consentimiento de mercadeo en la renovación.
- **Redacción pre-acreditación.** Todo material de cara al cliente debe reflejar con honestidad el estado de acreditación actual del servicio.
- **Sin calificación a1–a7.** Ni el catálogo, ni los términos, ni la declaración de participación usan ese esquema de calificación.
- **Texto estándar compartido.** El recordatorio de uso correcto del informe aparece con texto idéntico en la hoja de decisión, los términos y la plantilla de entrega; si cambia en uno, cambia en todos en la misma revisión.
- **Acceso restringido.** Las carpetas de precios y de inscripciones contienen datos de costos e identidad de participantes; el acceso por archivo puede ser más restrictivo que el de la carpeta.

---

*Documento interno de trabajo. Preparado a partir de los artefactos de `servicio_comercial/` con corte al 16 de julio de 2026.*
