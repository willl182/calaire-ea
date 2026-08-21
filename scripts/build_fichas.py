#!/usr/bin/env python3
"""Genera fichas resumen (MD + HTML) para los 15 artefactos comerciales.

Salida: servicio_comercial/fichas/ficha_NN_slug.{md,html} + indice.{md,html}
Fuente de contenido: artefactos CS-01..CS-15 con corte al 2026-07-16.
"""

import html as html_mod
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "servicio_comercial" / "fichas"

FICHAS = [
    {
        "num": "01",
        "slug": "hoja_decision_comercial",
        "nombre": "Hoja de decisión comercial",
        "grupo": "Control central",
        "proposito": "Fuente única de verdad para el alcance, el precio, las condiciones y las afirmaciones que se hacen sobre el servicio. Evita contradicciones entre folletos, cotizaciones, formularios, términos y correos a clientes: si dos documentos difieren, esta hoja tiene la autoridad.",
        "responsable": "Profesional de proyectos",
        "estado": "Propuesta aprobada (2026-07-14); puertas de liberación pendientes",
        "estado_tipo": "aprob",
        "requerido": "Antes de cualquier otro artefacto: todos derivan de esta hoja",
        "contenido": [
            "Identidad del servicio: nombre, entidad legal (UNAL, NIT 899.999.063-3), unidad ejecutora (Facultad de Minas, Laboratorio CALAIRE), roles asignados e idioma de trabajo (español).",
            "Alcance: cuatro bloques de gases (CO, SO₂, O₃, NO/NO₂) con capacidad de 4 analizadores por gas individual; definición de paquetes y de la unidad estándar de participación.",
            "Ancla de precio: referencia de ≈ COP 5.928.000 por organización (tarifa plana provisional para 1 a 4 bloques), facturación solo en COP, validez de cotización de 30 días.",
            "Límites de capacidad (provisionales; validación en espera del T700U), asignación de costos de ciclo de vida, estrategia de cilindros de gas certificado, tarifas de cancelación y texto estándar de uso del informe.",
        ],
        "conexiones": [
            "Alimenta directamente el catálogo, la convocatoria, el modelo de costos, la cotización y los términos.",
            "El texto estándar de uso del informe debe coincidir exactamente con los términos y la plantilla de entrega de informe.",
        ],
        "reglas": [
            "Ningún material de cara al cliente puede afirmar algo que esta hoja no respalde.",
            "El precio de referencia no es un precio aprobado: la acumulación de costos debe completarse primero.",
        ],
        "archivo": "00_control/CS-01_decisiones_comerciales.md",
    },
    {
        "num": "02",
        "slug": "catalogo_servicios",
        "nombre": "Catálogo de servicios",
        "grupo": "Mercado",
        "proposito": "Dar a un cliente potencial la información suficiente para decidir si solicita una cotización, sin abrumarlo con detalle técnico de procedimientos. Explica qué es el servicio, a quién está dirigido, el valor de participar y las condiciones generales.",
        "responsable": "Profesional de proyectos",
        "estado": "Contenido de la propuesta completo; aprobación de publicación pendiente",
        "estado_tipo": "avance",
        "requerido": "Lanzamiento de marketing",
        "contenido": [
            "Formato: una página web concisa más un PDF de dos a cuatro páginas, ambos con el mismo texto aprobado.",
            "Qué es el servicio, a quién está dirigido (laboratorios, redes de monitoreo, autoridades, academia) y valor de participar.",
            "Bloques seleccionables (CO, SO₂, O₃, NO/NO₂ como bloque único con analizador NOx) y modelo de tarifa plana por organización.",
            "Modalidad en instalaciones de CALAIRE en Medellín: el participante transporta su analizador; alcance incluido y excluido.",
        ],
        "conexiones": [
            "Todo dato de alcance, capacidad y precio proviene de la hoja de decisión comercial y del modelo de costos.",
            "Remite al formulario de expresión de interés y a la convocatoria de ronda vigente.",
        ],
        "reglas": [
            "El resultado no constituye certificación, acreditación ni declaración general de competencia — así debe decirlo.",
            "El valor de referencia es solo benchmark de viabilidad: no puede publicarse como tarifa antes de aprobar el modelo de costos.",
            "Redacción pre-acreditación obligatoria en todo el texto.",
        ],
        "archivo": "01_mercado/CS-02_catalogo.md",
    },
    {
        "num": "03",
        "slug": "programa_convocatoria_ronda",
        "nombre": "Programa anual y convocatoria de ronda",
        "grupo": "Mercado",
        "proposito": "Convertir el servicio genérico en una ronda programada y adquirible: publica fechas, capacidad, gases ofrecidos y plazos de inscripción de cada ronda.",
        "responsable": "Líder técnico",
        "estado": "Plantilla completa; sección de publicación de ronda pendiente",
        "estado_tipo": "avance",
        "requerido": "Lanzamiento de marketing",
        "contenido": [
            "Campos mínimos: año del programa, identificación de la ronda, estado, ubicación, fechas de ejecución, bloques ofrecidos, capacidad, apertura y cierre de inscripciones, fecha objetivo del informe final.",
            "Control de versiones del aviso: cada cambio de fecha, capacidad, gases o tarifas tras la primera publicación exige nueva versión (v1, v2, …) con nota de cambio pública.",
            "Declaración pre-acreditación obligatoria y aviso de que las instrucciones técnicas detalladas solo se entregan a participantes confirmados.",
        ],
        "conexiones": [
            "Precios y capacidades deben coincidir con la hoja de decisión y el modelo de costos.",
            "Las fechas se alinean con los documentos de planificación técnica existentes del SGC.",
        ],
        "reglas": [
            "No duplica instrucciones técnicas del esquema de ensayos.",
            "Permanece como plantilla no publicada hasta cerrar las revisiones de costos, jurídica y cilindros.",
        ],
        "archivo": "01_mercado/CS-03_programa_convocatoria_ronda.md",
    },
    {
        "num": "04",
        "slug": "modelo_costos_precios",
        "nombre": "Modelo de costos y precios",
        "grupo": "Precio (acceso restringido)",
        "proposito": "Validar la tarifa plana provisional, calcular los costos reales de ejecutar una ronda y el umbral de viabilidad, y respaldar una futura revisión de precios sin asumir facturación por gas o por analizador.",
        "responsable": "Profesional de proyectos",
        "estado": "Propuesta de viabilidad; evidencia de costos pendiente",
        "estado_tipo": "borrador",
        "requerido": "Emisión de cotizaciones",
        "contenido": [
            "Libro `CS-04_modelo_costos_precios.xlsx` sobre la plantilla F-PSEA-01: supuestos, costo común, costo por gas, ciclo de vida de equipos, estrategia de cilindros, tarifa, validación de referencia, inscripción, escenarios y aprobación.",
            "Supuestos laborales provisionales: horas por rol y tarifas institucionales aún pendientes de validación.",
            "Política cambiaria: TRM USD/COP × referencia BCE solo para convertir referencias; facturación únicamente en COP.",
        ],
        "conexiones": [
            "Toma capacidad, arquitectura de precio y política monetaria de la hoja de decisión comercial.",
            "Alimenta la lista de precios aprobada y el valor de cada cotización.",
        ],
        "reglas": [
            "Ninguna oferta real puede emitirse por debajo del costo directo de ejecución que arroje este modelo.",
            "El costeo monetario permanece bloqueado hasta validar institucionalmente las tarifas por rol.",
            "Acceso restringido: contiene datos internos de costos (ver política de la carpeta).",
        ],
        "archivo": "02_precios_restringidos/CS-04_modelo_costos_precios.md",
    },
    {
        "num": "05",
        "slug": "expresion_de_interes",
        "nombre": "Formulario de expresión de interés",
        "grupo": "Mercado",
        "proposito": "Verificar la demanda antes de comprometer fechas y costos. El cliente manifiesta interés en uno o más bloques de gases sin adquirir compromiso ni reservar cupo.",
        "responsable": "Profesional de proyectos",
        "estado": "Borrador; aprobación pendiente",
        "estado_tipo": "borrador",
        "requerido": "Lanzamiento de marketing",
        "contenido": [
            "16 preguntas mínimas: organización, contacto, país, gases deseados, analizadores (fabricante, modelo, año), fechas de calibración, viabilidad de operación simultánea CO/SO₂, periodo preferido, proceso de compra y aceptación de facturación en COP.",
            "Texto de consentimiento explícito de protección de datos (Ley 1581/2012), visible y no premarcado, con revocatoria vía calaire_med@unal.edu.co.",
            "Caducidad de la respuesta: las expresiones obsoletas se marcan y se excluyen del canal activo.",
        ],
        "conexiones": [
            "Cada respuesta entra al rastreador de inscripciones como oportunidad en etapa de interés.",
            "Las fechas de calibración alimentan la verificación de compatibilidad de la revisión de contrato; el idioma preferido alimenta cotización y términos.",
        ],
        "reglas": [
            "El formulario debe decir explícitamente: enviar la expresión de interés no reserva un lugar en la ronda.",
            "No se publica ningún precio no aprobado: la pregunta de tarifa valida la arquitectura, no el valor.",
        ],
        "archivo": "01_mercado/CS-05_expresiones_de_interes.md",
    },
    {
        "num": "06",
        "slug": "plantilla_cotizacion",
        "nombre": "Plantilla de cotización",
        "grupo": "Venta y contratación",
        "proposito": "Realizar una oferta comercial controlada: nada se ofrece por fuera de esta plantilla. Fija alcance, valor, validez, método de aceptación y condiciones de pago de cada oferta.",
        "responsable": "Profesional de proyectos",
        "estado": "Borrador; aprobación pendiente",
        "estado_tipo": "borrador",
        "requerido": "Emisión de ofertas",
        "contenido": [
            "Encabezado controlado: número único, familia de cotización, revisión, fechas de emisión, caducidad y fecha límite de aceptación (distinta del vencimiento).",
            "Método de aceptación: cotización firmada por representante autorizado desde correo institucional, u orden de compra formal aceptada por la Universidad.",
            "Paquete de gases seleccionado, analizadores, configuración operativa, entregables incluidos, exclusiones (transporte, seguros, aduanas, impuestos de importación para internacionales), precio y cronograma de pagos.",
        ],
        "conexiones": [
            "El valor proviene del modelo de costos aprobado; la moneda y validez, de la hoja de decisión.",
            "El número de cotización se cita en la inscripción, la revisión de contrato y el rastreador; las revisiones abren registro de cambios.",
        ],
        "reglas": [
            "Facturación en COP salvo aprobación explícita en contrario.",
            "Una cotización vencida no se reactiva: se emite una nueva revisión de la misma familia.",
        ],
        "archivo": "03_ventas_contratacion/CS-06_cotizaciones.md",
    },
    {
        "num": "07",
        "slug": "formulario_inscripcion",
        "nombre": "Formulario de inscripción",
        "grupo": "Venta y contratación",
        "proposito": "Capturar al comprador: identidad legal, alcance seleccionado y datos administrativos y de facturación. Reutiliza los campos técnicos del SGC y de calaire-app en lugar de duplicarlos: solo agrega la sección comercial.",
        "responsable": "Profesional de proyectos",
        "estado": "Borrador; aprobación pendiente",
        "estado_tipo": "borrador",
        "requerido": "Aceptación del pedido",
        "contenido": [
            "Campos comerciales: nombre legal, identificación tributaria, facturación, número de cotización válido, paquete de gases, idioma del informe, contactos contractual y técnico.",
            "Evidencia de aceptación: marca de tiempo ISO 8601, canal (portal, correo, PDF firmado, papel) y origen IP si aplica — facilita resolver controversias.",
            "Consentimientos separados: aceptación de términos, selección de confidencialidad/divulgación y consentimiento de mercadeo (texto Ley 1581/2012 aparte del consentimiento del servicio).",
        ],
        "conexiones": [
            "El número de cotización debe ser válido, no vencido y no aceptado por otra parte.",
            "Cerrar la inscripción dispara la revisión de contrato; los datos técnicos van por los formularios vigentes del SGC.",
        ],
        "reglas": [
            "Solo los participantes confirmados pasan a la planificación formal de la ronda.",
            "Si la cotización aceptada requiere revisión, el registro pasa a «revisión de cotización en curso» y vuelve a «cotizado» con nueva revisión.",
        ],
        "archivo": "03_ventas_contratacion/CS-07_inscripciones.md",
    },
    {
        "num": "08",
        "slug": "terminos_condiciones",
        "nombre": "Términos y condiciones (acuerdo del participante)",
        "grupo": "Venta y contratación",
        "proposito": "Establecer las condiciones de servicio vinculantes entre la Universidad Nacional de Colombia y la organización participante. Define contenido; la redacción legal final la aprueba la asesoría jurídica institucional.",
        "responsable": "Profesional de proyectos",
        "estado": "Borrador; aprobación pendiente",
        "estado_tipo": "borrador",
        "requerido": "Aceptación del pedido",
        "contenido": [
            "Cláusulas mínimas: partes y descripción del servicio, alcance seleccionado con incorporación del SGC por referencia, responsabilidades de proveedor y participante.",
            "Transporte, custodia y riesgo de equipos; consecuencias de falla del instrumento. Las cláusulas de riesgo/seguro, pagos, cancelaciones, retiro y fuerza mayor están marcadas como pendientes de redacción jurídica.",
            "Precio, impuestos y pagos; inscripción mínima, aplazamiento y cancelación; retiro y sustitución; protección de datos (Ley 1581 de 2012); uso correcto del informe.",
        ],
        "conexiones": [
            "Los documentos técnicos vigentes del SGC rigen la ejecución: estas condiciones los complementan, no los sustituyen.",
            "La cláusula de uso del informe usa el texto estándar compartido con la hoja de decisión y la entrega de informe.",
            "La revisión de contrato compara cláusula por cláusula cualquier orden de compra contra este acuerdo.",
        ],
        "reglas": [
            "La cláusula de transporte no puede firmarse sin el instructivo vigente de embalaje y transporte de equipos.",
            "Sin calificación agregada a1–a7 ni afirmación de acreditación en ninguna cláusula.",
        ],
        "archivo": "03_ventas_contratacion/CS-08_terminos.md",
    },
    {
        "num": "09",
        "slug": "revision_contrato",
        "nombre": "Lista de verificación de revisión de contrato",
        "grupo": "Venta y contratación",
        "proposito": "Impedir que CALAIRE-EA acepte un pedido que no puede entregar o cuya orden de compra contradiga las condiciones del servicio. Es la compuerta previa a toda confirmación.",
        "responsable": "Líder técnico",
        "estado": "Borrador; aprobación pendiente",
        "estado_tipo": "borrador",
        "requerido": "Confirmación de cada pedido",
        "contenido": [
            "17 verificaciones firmadas (iniciales obligatorias): validez de la cotización, no doble reserva, gases ofrecidos en la ronda, capacidad disponible y residual ≥ 0, compatibilidad del equipo, coherencia de precio y pagos.",
            "Revisión de la orden de compra contra los términos: que no anule en silencio reglas de cancelación, confidencialidad, informes ni la ausencia de calificación agregada.",
            "Tres consentimientos de divulgación verificados por separado: regulatorio, de mercadeo y transfronterizo (Ley 1581/2012). Un «acepto la divulgación» genérico es insuficiente.",
        ],
        "conexiones": [
            "Lee capacidad del rastreador; su decisión (aceptado, lista de espera, rechazado) lo actualiza y dispara el paquete de confirmación.",
            "Si el pedido consume el último cupo se marca «último espacio» y requiere autorización del Líder técnico.",
        ],
        "reglas": [
            "Iniciales faltantes bloquean la decisión; los rechazos exigen motivo documentado y compartido con el cliente.",
            "Pedidos en lista de espera se rastrean con fecha y criterios de prioridad aplicados.",
        ],
        "archivo": "03_ventas_contratacion/CS-09_revisiones_contrato.md",
    },
    {
        "num": "10",
        "slug": "rastreador_inscripciones_ingresos",
        "nombre": "Rastreador de inscripciones e ingresos",
        "grupo": "Inscripción y confirmación (acceso restringido)",
        "proposito": "Controlar capacidad, pedidos, pagos y viabilidad de la ronda. Es el núcleo operativo del sistema: casi todos los demás artefactos leen o escriben aquí, y es la vista en tiempo real del estado de cada oportunidad.",
        "responsable": "Profesional de proyectos",
        "estado": "Implementado v0.3; aprobación institucional pendiente",
        "estado_tipo": "avance",
        "requerido": "Confirmación y ejecución",
        "contenido": [
            "Libro Excel institucional protegido, con plantilla limpia, copia de simulación sintética (nunca usar como registro vivo) y generador reproducible en scripts/build_cs10_tracker.py.",
            "Estados comerciales: interés → cotizado → registrado → en revisión → aceptado pendiente de pago → confirmado / lista de espera / rechazado / retirado.",
            "Columnas de control: fechas límite de aceptación y de pago, seguimiento de pagos parciales, capacidad consumida por bloque, indicador de último cupo, prioridad de lista de espera (grupo 1: laboratorio acreditado; grupo 2: demás elegibles).",
        ],
        "conexiones": [
            "Recibe expresiones de interés, cotizaciones, inscripciones, decisiones de revisión, cambios y renovaciones.",
            "Los cambios de capacidad se reflejan de inmediato, sin actualizaciones por lotes.",
        ],
        "reglas": [
            "No almacena resultados técnicos de participantes.",
            "La columna de comunicaciones solo apunta a calaire_med@unal.edu.co o carpetas institucionales controladas — nada de bandejas personales.",
            "Cambiar la contraseña de protección de hoja antes del uso real; acceso restringido por identidad de participantes.",
        ],
        "archivo": "04_inscripcion_restringida/CS-10_seguimiento.md",
    },
    {
        "num": "11",
        "slug": "paquete_confirmacion_incorporacion",
        "nombre": "Paquete de confirmación, lista de espera, rechazo e incorporación",
        "grupo": "Inscripción y confirmación (acceso restringido)",
        "proposito": "Comunicar al cliente el resultado de su pedido (confirmación, lista de espera o rechazo) y, cuando se confirma, entregar el paquete de incorporación con las instrucciones técnicas del SGC. Es el traspaso formal de la capa comercial a la técnica.",
        "responsable": "Líder técnico",
        "estado": "Borrador; aprobación pendiente",
        "estado_tipo": "borrador",
        "requerido": "Preparación técnica",
        "contenido": [
            "Mensaje de confirmación con código de participante asignado por el SGC, gases y analizadores confirmados, fechas, estado de pago, contactos técnico y administrativo, y próximos plazos.",
            "Plazo de acuse de recibo: 5 días hábiles; sin respuesta hay seguimiento registrado — un cupo pagado no se libera sin proceso formal de cancelación.",
            "Plantillas de lista de espera (con prioridad conservada) y de rechazo (con motivo).",
        ],
        "conexiones": [
            "Se dispara solo con la revisión de contrato aprobada y el rastreador actualizado.",
            "El paquete de incorporación enlaza los documentos del SGC; no los duplica.",
        ],
        "reglas": [
            "La confirmación tiene fecha de validez: sin acuse, el cupo pasa a lista de espera conservando prioridad.",
            "Acceso restringido: contiene identidad de participantes.",
        ],
        "archivo": "04_inscripcion_restringida/CS-11_confirmaciones.md",
    },
    {
        "num": "12",
        "slug": "registro_cambios_cancelaciones_reembolsos",
        "nombre": "Registro de cambios, cancelaciones y reembolsos",
        "grupo": "Cambios y reembolsos",
        "proposito": "Controlar toda modificación posterior a la confirmación —cambio de gases o analizadores, retiro, aplazamiento, cancelación, reembolso o nota crédito— dejando trazable su efecto económico y de capacidad.",
        "responsable": "Profesional de proyectos",
        "estado": "Borrador; aprobación pendiente",
        "estado_tipo": "borrador",
        "requerido": "Cuando se activa un evento de cambio",
        "contenido": [
            "Eventos disparadores: cambio de alcance, retiro del participante, aplazamiento o cancelación del proveedor, inscripción mínima no alcanzada, fuerza mayor, solicitud de reembolso, error sustancial del informe.",
            "Registro mínimo con referencia a la familia de cotización original y su revisión, tarifa aplicable del catálogo, cálculo línea por línea de reembolso o crédito, impacto en capacidad y en viabilidad de la ronda.",
            "Compromisos: reembolso típico en 30 días hábiles desde la aprobación; las notas crédito tienen validez limitada.",
        ],
        "conexiones": [
            "Los cambios de capacidad se reflejan de inmediato en el rastreador.",
            "Quejas técnicas o no conformidades detectadas durante un cambio van a los procedimientos del SGC, no se quedan aquí.",
        ],
        "reglas": [
            "Toda decisión con impacto económico exige autorización del Profesional de proyectos.",
            "Cada registro cita la cotización original: protege contra disputas sobre qué términos aplicaban.",
        ],
        "archivo": "05_cambios_finanzas/CS-12_cambios_cancelaciones_reembolsos.md",
    },
    {
        "num": "13",
        "slug": "entrega_informe",
        "nombre": "Entrega de informe y declaración de participación",
        "grupo": "Entrega y retención",
        "proposito": "Completar la entrega al cliente de manera consistente: el informe técnico ya lo controla el SGC; la capa comercial aporta el mensaje de entrega controlada y la declaración de participación.",
        "responsable": "Líder técnico",
        "estado": "Borrador; aprobación pendiente",
        "estado_tipo": "borrador",
        "requerido": "Emisión del informe",
        "contenido": [
            "Mensaje con código de participante, identificador y versión del informe, estado FINAL (ruta directa, sin informe preliminar), aviso de confidencialidad e instrucciones de acceso seguro.",
            "Plazo de apelación: 14 días calendario desde la emisión final, según el procedimiento de apelaciones del SGC.",
            "Recordatorio estándar de uso del informe: el participante puede declarar que participó, pero no que CALAIRE-EA o la ronda estén acreditadas ni que la participación pruebe competencia; distribución a terceros requiere autorización escrita.",
        ],
        "conexiones": [
            "Requiere la aprobación previa del informe dentro del SGC.",
            "Correcciones aceptadas se controlan como revisión del informe final; un error sustancial abre registro de cambios.",
        ],
        "reglas": [
            "El recordatorio de uso del informe es texto estándar compartido: no se modifica sin aprobar el cambio simultáneamente en la hoja de decisión y aquí.",
        ],
        "archivo": "06_entrega_retencion/CS-13_entrega_informes.md",
    },
    {
        "num": "14",
        "slug": "retroalimentacion_cliente",
        "nombre": "Formulario de retroalimentación del cliente",
        "grupo": "Entrega y retención",
        "proposito": "Medir la experiencia del participante y la demanda futura del servicio al cierre de cada ronda.",
        "responsable": "Profesional de proyectos",
        "estado": "Borrador; aprobación pendiente",
        "estado_tipo": "borrador",
        "requerido": "Cierre de ronda",
        "contenido": [
            "12 preguntas: claridad de oferta y cotización, facilidad de registro y pago, comunicaciones, logística, utilidad del informe, valor percibido por precio, interés para la próxima ronda, NPS y comentarios libres.",
            "Opción de envío anónimo (sin vínculo al código de participante; solo vistas agregadas).",
            "Ventana de envío definida desde la entrega del informe final.",
        ],
        "conexiones": [
            "Si el participante autoriza contacto de renovación, sus preferencias de gases y periodo generan una nueva expresión de interés vinculada a su registro en el rastreador.",
            "Comentarios que revelen queja, apelación o no conformidad se enrutan al procedimiento del SGC en 1 día hábil; los temas con impacto económico abren registro de cambios.",
        ],
        "reglas": [
            "El registro de retroalimentación no se cierra hasta que la queja quede registrada por separado en el SGC.",
        ],
        "archivo": "06_entrega_retencion/CS-14_retroalimentacion.md",
    },
    {
        "num": "15",
        "slug": "renovacion_clientes_potenciales",
        "nombre": "Mensaje de renovación y registro de clientes potenciales",
        "grupo": "Entrega y retención",
        "proposito": "Convertir la participación completada en demanda recurrente: agradece, invita a la siguiente ronda, recoge el interés futuro y lo registra en el canal de oportunidades.",
        "responsable": "Profesional de proyectos",
        "estado": "Borrador; aprobación pendiente",
        "estado_tipo": "borrador",
        "requerido": "Después de cada ronda",
        "contenido": [
            "SLA de plazos: seguimiento a las 2–4 semanas del informe final, recordatorio si no hay respuesta, marca de «obsoleto» tras el umbral definido y reintento en la siguiente ronda.",
            "Contenido del mensaje: agradecimiento, enlace al formulario de retroalimentación, próximo periodo del programa, registro de gases de interés futuro y enlace a la expresión de interés.",
        ],
        "conexiones": [
            "Los clientes potenciales y su estado (activo/obsoleto) viven en el rastreador.",
            "Requiere verificar el consentimiento de mercadeo registrado en la inscripción antes de enviar.",
        ],
        "reglas": [
            "No inventar descuentos: sin esquema de fidelidad aprobado en el modelo de costos, el mensaje omite el tema por completo.",
            "Prohibido divulgar o hacer mercadeo con base en el desempeño confidencial del participante.",
        ],
        "archivo": "06_entrega_retencion/CS-15_renovacion.md",
    },
]

CSS = """
  :root { --ink:#111827; --soft:#6B7280; --accent:#FDB913; --accent-dark:#E5A610;
    --accent-soft:#F5F5F0; --amber:#A96200; --amber-soft:#FFF4DB; --line:#D1D5DB;
    --line-soft:#E5E7EB; --bg:#E8EAED; --surface:#F5F6F7; --card:#FBFBFA;
    --ok:#008760; --ok-soft:#E5F8EF; --danger:#C0103A; --danger-soft:#FFF0F3;
    --focus-ring:rgba(253,185,19,.4); }
  * { box-sizing:border-box; margin:0; }
  body { font-family:"Droid Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif; background:var(--bg); color:var(--ink); line-height:1.6; }
  ::selection { background:var(--accent); color:var(--ink); }
  :focus-visible { outline:2px solid var(--accent); outline-offset:2px; box-shadow:0 0 0 4px var(--focus-ring); }
  .wrap { max-width:860px; margin:0 auto; padding:2rem 1.5rem 3rem; }
  .head { background:var(--card); color:var(--ink); border-bottom:4px solid var(--accent);
    border-radius:12px; padding:1.6rem 1.8rem; box-shadow:0 6px 18px rgba(17,24,39,.10); }
  .head .grupo { font-size:.78rem; text-transform:uppercase; letter-spacing:.08em; opacity:.8; }
  .head h1 { font-size:1.45rem; margin-top:.3rem; letter-spacing:-.01em; }
  .meta { display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:.8rem; margin:1.2rem 0; }
  .meta .box { background:var(--card); border:1px solid var(--line); border-radius:10px; padding:.8rem 1rem; box-shadow:0 2px 6px rgba(17,24,39,.08); }
  .meta b.k { display:block; font-size:.72rem; text-transform:uppercase; letter-spacing:.06em; color:var(--soft); margin-bottom:.25rem; }
  .meta .v { font-size:.92rem; font-weight:600; }
  .tag { display:inline-block; font-size:.74rem; font-weight:700; padding:.18rem .6rem; border-radius:999px; }
  .tag.aprob { background:var(--ok-soft); color:var(--ok); }
  .tag.avance { background:var(--accent-soft); color:var(--accent); }
  .tag.borrador { background:var(--amber-soft); color:var(--amber); }
  h2 { font-size:1.02rem; color:var(--ink); margin:1.5rem 0 .6rem; border-left:4px solid var(--accent); padding-left:.6rem; }
  p.prop { background:var(--card); border:1px solid var(--line); border-radius:10px; padding:.9rem 1.1rem; font-size:.95rem; }
  ul { padding-left:1.2rem; display:grid; gap:.45rem; font-size:.93rem; }
  .foot { margin-top:1.8rem; font-size:.78rem; color:var(--soft); border-top:1px solid var(--line); padding-top:.8rem; }
  code { background:var(--accent-soft); padding:.08rem .3rem; border-radius:4px; font-size:.85em; }
  a { color:var(--ink); text-decoration-color:var(--accent-dark); text-decoration-thickness:2px; }
  @media print { body{background:#fff} .wrap{padding:0} }
"""


def esc(s: str) -> str:
    return html_mod.escape(s, quote=False)


def li(items):
    return "\n".join(f"    <li>{esc(i)}</li>" for i in items)


def build_md(f) -> str:
    lines = [
        f"# {f['nombre']}",
        "",
        f"**Archivo fuente:** `servicio_comercial/{f['archivo']}`",
        "",
        "## Propósito",
        "",
        f['proposito'],
        "",
        "## Contenido clave",
        "",
    ]
    lines += [f"- {c}" for c in f["contenido"]]
    lines += ["", "## Se conecta con", ""]
    lines += [f"- {c}" for c in f["conexiones"]]
    lines += ["", "## Reglas críticas", ""]
    lines += [f"- {r}" for r in f["reglas"]]
    lines += [
        "",
        "---",
        "",
        "*Documento de consulta · corte al 2026-07-16 ·"
        " índice: [indice.md](indice.md)*",
        "",
    ]
    return "\n".join(lines)


def build_html(f) -> str:
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(f['nombre'])} — CALAIRE-EA</title>
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
  <div class="head">
    <h1>{esc(f['nombre'])}</h1>
  </div>
  <div class="meta">
    <div class="box"><b class="k">Archivo fuente</b><div class="v"><code>servicio_comercial/{esc(f['archivo'])}</code></div></div>
  </div>
  <h2>Propósito</h2>
  <p class="prop">{esc(f['proposito'])}</p>
  <h2>Contenido clave</h2>
  <ul>
{li(f['contenido'])}
  </ul>
  <h2>Se conecta con</h2>
  <ul>
{li(f['conexiones'])}
  </ul>
  <h2>Reglas críticas</h2>
  <ul>
{li(f['reglas'])}
  </ul>
  <div class="foot">Documento de consulta · corte al 2026-07-16 · <a href="indice.html">índice de documentos</a></div>
</div>
</body>
</html>
"""


def build_index():
    md = [
        "# Índice de fichas resumen — artefactos comerciales",
        "",
        "Una ficha por artefacto, en MD y HTML. Corte al 2026-07-16.",
        "",
        "| Artefacto | Ficha MD | Ficha HTML |",
        "|---|---|---|",
    ]
    rows = []
    for f in FICHAS:
        base = f"ficha_{f['num']}_{f['slug']}"
        md.append(f"| {f['nombre']} | [{base}.md]({base}.md) | [{base}.html]({base}.html) |")
        rows.append(
            f'<tr><td><a href="{base}.html">{esc(f["nombre"])}</a></td>'
            f'<td><a href="{base}.md">Versión editable</a></td></tr>'
        )
    md.append("")
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Índice de fichas — artefactos comerciales CALAIRE-EA</title>
<style>{CSS}
  table {{ width:100%; border-collapse:collapse; background:var(--card); border:1px solid var(--line); border-radius:10px; overflow:hidden; font-size:.9rem; margin-top:1.2rem; }}
  th {{ background:var(--accent-soft); text-align:left; padding:.6rem .8rem; font-size:.78rem; text-transform:uppercase; letter-spacing:.04em; color:var(--accent-dark); }}
  td {{ padding:.55rem .8rem; border-top:1px solid var(--line); }}
</style>
</head>
<body>
<div class="wrap">
  <div class="head">
    <div class="grupo">Servicio comercial CALAIRE-EA</div>
    <h1>Índice de fichas resumen de artefactos</h1>
  </div>
  <table>
    <tr><th>Artefacto</th><th>Documento</th></tr>
    {chr(10).join(rows)}
  </table>
  <div class="foot">Corte al 2026-07-16 · documento de contexto: <code>presentacion_propuesta_servicio.md</code></div>
</div>
</body>
</html>
"""
    return "\n".join(md), html


def main():
    OUT.mkdir(exist_ok=True)
    for f in FICHAS:
        base = OUT / f"ficha_{f['num']}_{f['slug']}"
        base.with_suffix(".md").write_text(build_md(f), encoding="utf-8")
        base.with_suffix(".html").write_text(build_html(f), encoding="utf-8")
    idx_md, idx_html = build_index()
    (OUT / "indice.md").write_text(idx_md, encoding="utf-8")
    (OUT / "indice.html").write_text(idx_html, encoding="utf-8")
    print(f"Generadas {len(FICHAS)} fichas (MD+HTML) + índice en {OUT}")


if __name__ == "__main__":
    main()
