# Revisión de Implementación: `ptservice_art_prop.md` → `commercial_service/`

**Fecha:** 2026-07-14 09:27
**Alcance:** Estructura de carpetas, contenido de los 15 artefactos CS, coherencia con el QMS activo, huecos que la sesión actual no ha resuelto.
**Documentos revisados:** `ptservice_art_prop.md` (blueprint, 768 líneas), `commercial_service/README.md` (42 líneas), los 15 artefactos CS-01 → CS-15, `docs/sgc/matriz_equivalencias_codigos_sgc_pea.md` (renumeración QMS activa), `docs/qms/01_bloque_general/05_matrices_inventarios/Árbol Maestro PSEA.md`, `docs/sgc/checklist_sgc_pdts.md`.

---

## 1. Veredicto global

La implementación **cumple el blueprint a nivel estructural y de cobertura**. Los 15 artefactos existen, están en las carpetas que prescribe la sección 22, contienen los campos mínimos definidos en las secciones 5–18, reproducen las reglas duras de la sección 2 (sin a1–a7, sin claim de acreditación, distinción piloto/pagado, capacidad 4 individuales / 3+6 simultáneo CO/SO₂), y citan el QMS como fuente de verdad técnica en lugar de duplicar cláusulas.

**Pero la implementación arrastra tres problemas que sí deben atacarse antes de aprobar CS-01:**

1. **Referencias QMS obsoletas** por la renumeración aprobada el 2026-06-14. Los artefactos引用an `P-PSEA-17`, `P-PSEA-18`, `P-PSEA-19`, `F-PSEA-05A`, `F-PSEA-04` con el *significado* antiguo, cuando la matriz de equivalencias ya migró esos códigos a procedimientos distintos. La consecuencia es que un lector que abra el QMS siguiendo la cita cae en un procedimiento diferente del que la plantilla comercial espera.
2. **Plantillas deliberadamente vacías** (que es el diseño), pero con muy poca indicación de cómo se llena cada `[FILL]`. CS-01 en particular tiene 20 marcadores sin guía de evidencia esperada; CS-04 tiene 9 pestañas que son casi todo `[CALC]`. Sin una guía operativa, el siguiente agente que tome la tarea no sabrá qué preguntar a quién.
3. **Ausencia de la lógica de "Closed institutional round"** dentro de CS-04. El blueprint la menciona (sección 8.6) y CS-06 la recoge como variante, pero el modelo de precios no tiene pestaña ni método de cálculo para ella. Si llega una solicitud institucional antes de cerrar CS-04, no hay forma de cotizarla sin inventar la estructura fuera del modelo.

Hay además una decena de mejoras menores (sección 5) que no bloquean la fase actual pero conviene registrar.

---

## 2. Cobertura estructural vs. blueprint

Mapeo de la sección 22 del blueprint contra el filesystem real:

| Carpeta blueprint | Contenido blueprint | Filesystem | ¿Cumple? |
|---|---|---|---|
| `00_control/` | CS-01, register, change log | `CS-01_commercial_decisions.md`, `artifact_register.md`, `release_change_log.md` | Sí |
| `01_market/` | CS-02, CS-03, CS-05 | los tres | Sí |
| `02_pricing_restricted/` | CS-04, approved price lists | los dos + marca `RESTRICTED ACCESS` | Sí |
| `03_sales_contracting/` | CS-06, CS-07, CS-08, CS-09 | los cuatro | Sí |
| `04_enrollment_restricted/` | CS-10, CS-11 | los dos + marca `RESTRICTED ACCESS` | Sí |
| `05_changes_finance/` | CS-12 | el uno | Sí |
| `06_delivery_retention/` | CS-13, CS-14, CS-15 | los tres | Sí |

README presente, 42 líneas, resume estructura, reglas, fases, gates. Adecuado para que un tercero nuevo encuentre todo en cinco minutos.

**Detalle faltante en la estructura:** ninguna carpeta tiene un `.gitkeep` ni un `OWNERS.md` con la lista explícita de quién tiene permiso de lectura/escritura. README dice "access-controlled" para `02_pricing_restricted/` y `04_enrollment_restricted/`, pero el control de acceso se menciona solo a nivel carpeta, no a nivel archivo. Para una operación real eso importa: CS-04 (modelo de costos) y CS-10 (tracker de enrollment) tienen sensibilidad diferente y podrían necesitarse permisos diferenciados dentro de la misma carpeta.

---

## 3. Cobertura de contenido: 15 artefactos uno por uno

### CS-01 — Commercial decision sheet (`00_control/CS-01_commercial_decisions.md`)

168 líneas. Es el artefacto más desarrollado y el único con `Status: DRAFT — pending management approval` (los demás están en `PLANNED`).

**Lo que está bien:**

- 12 secciones que siguen el orden del blueprint 5: identidad, alcance, precio, capacidad, lifecycle, cilindros, enrollment, cancelación, acreditación, valor asignado, incluidos/excluidos, aprobación.
- Reglas duras repetidas literalmente: "no a1–a7 grade and no overall pass/fail grade", "One, several or all five gases may be selected", fórmula de arquitectura de precios.
- Acceptance test al pie (línea 166–168), que es la frase exacta del blueprint.
- Tabla de lifecycle con la asignación de costos (gas-specific vs. common fee).
- Tabla comparativa de estrategias de cilindro con columna "Hybrid" añadida — una mejora sobre el blueprint, que solo tenía 2 columnas.

**Lo que falta / preocupa:**

- 20 marcadores `[FILL]` sin guía de evidencia. Ejemplos críticos:
  - `Service name`, `Provider legal identity`: el blueprint no dice cuál es; hace falta decisión de gerencia.
  - `Invoicing currency`, `Exchange-rate method`: el blueprint no las predefine, pero un agente que llene esto necesita saber si aplica TRM colombiana, tasa BCE, o un fix interno.
  - `Pricing objective` (margin / full cost recovery / strategic subsidy): la sección 8.6 del blueprint dice que management debe "explicitly record" cuál aplica; sin esa decisión, CS-04 no puede fijar margen objetivo.
  - `Approved cylinder strategy` + 2 approvers names: bloquea el lanzamiento hasta que se llene.
  - `Cancellation and postponement` (sección 8 del CS-01): no hay tabla de tarifas por plazo de retiro. CS-12 luego se referirá a estas tarifas pero no existirán.
- Falta referencia al **riesgo cambiario** cuando la moneda de facturación no es la moneda de costo. El blueprint menciona "exchange-rate method" pero CS-01 no obliga a documentar el método de cobertura o revaluación.
- Falta el **idioma de trabajo** del servicio (separado del idioma del informe). CS-03 lo pide para el round, pero CS-01 debería fijarlo como regla general.
- La "Approved strategy" en cilindros tiene tres columnas pero el contenido de la columna Hybrid está completamente en blanco. Si se aprueba hybrid, hay que documentarlo aquí, no solo en CS-04.

### CS-02 — Service catalogue (`01_market/CS-02_catalogue.md`)

86 líneas. Sigue la estructura de 12 secciones recomendada por el blueprint 6. Reproduce la regla de evaluación (z o z′, sin a1–a7) y el pre-accreditation statement. Incluye un **checklist de controles de redacción** (líneas 73–80) que es la única forma de auditoría rápida de que la pieza no viola las reglas duras de la sección 2 del blueprint.

**Lo que falta / preocupa:**

- Casi todo el contenido narrativo está en `[FILL]`. El catálogo es lo que va a leer un prospecto; sin contenido real es solo un armazón.
- No incluye el **idioma** del catálogo. ¿Se publica en español, inglés, ambos? CS-03 lo pide para el round pero CS-02 debería definirlo para la pieza de marketing.
- No hay campo de **fecha de revisión** del catálogo (los artefactos individuales sí lo tienen, pero la pieza pública también lo necesita para que el cliente sepa qué versión leyó).

### CS-03 — Annual programme and round notice (`01_market/CS-03_programme_round_notice.md`)

60 líneas. Es la plantilla de comunicación pública por round.

**Lo que está bien:**

- 15 campos mínimos que cubren el blueprint 7.
- Plantilla en bloque de texto lista para copiar y llenar.
- Controles explícitos: "no duplica instrucciones técnicas PSEA", "precios y capacidad coinciden con CS-01 y CS-04", "fechas alineadas con planificación PSEA".

**Lo que falta / preocupa:**

- No hay campo para el **número de versión** del round notice que se publica, crítico si se emiten dos notices para el mismo año (cambios de fecha, etc.).
- No hay mención al **idioma de trabajo del round** como dato independiente de los idiomas de los informes por participante.
- "Approximate report date" se pide pero no se distingue entre draft y final (CS-13 sí lo hace, pero CS-03 debería comprometerse a un SLA hacia draft y otro hacia final).

### CS-04 — Price model (`02_pricing_restricted/CS-04_cost_price_model.md`)

164 líneas. Reproduce la arquitectura del blueprint 8.1, las 9 pestañas de la sección 8.2, y la fórmula de lifecycle de 8.3.

**Lo que está bien:**

- Marca `RESTRICTED ACCESS` y define que el contenido de costo/margen **no sale al exterior** (sección 8.7 del blueprint).
- Cada pestaña tiene la estructura esperada; los `[CALC]` están donde corresponde.
- Controles de lógica comercial al pie (líneas 150–158) cubren los cinco riesgos identificados en el blueprint 8.6.
- Reproduce el control clave: "The €1,600 benchmark is not tested using an assumed 8–15 participants when current physical capacity is four."

**Lo que falta / preocupa (importante):**

- **No hay pestaña ni método para "closed institutional round"**. El blueprint 8.6 dice "Closed institutional rounds require a separate full-cost quotation" pero CS-04 no da una fórmula para derivar ese precio. La variante existe en CS-06 pero el modelo de costos no la soporta.
- **No hay pestaña de riesgos de flujo de caja**: cuándo se cobra (anticipo, contra entrega, después del round), cómo impacta la viabilidad. Esto es input para la decisión de "pricing objective".
- **No hay pestaña de sensibilidad cambiaria** cuando se factura en moneda distinta a la de costo.
- La sección 4 (Equipment lifecycle) tiene 6 activos listados según blueprint 8.3, pero **falta el `round-use factor`** en la fórmula. La fórmula dice "× documented round-use factor" pero la columna no existe. Sin este factor, no se puede calcular la asignación por round.
- **No se documenta de dónde sale la cifra de aproximadamente €1,600**. CS-01 la cita como benchmark; CS-04 debería mostrar la derivación (cost buildup) que la respalda para que gerencia pueda defenderla.
- La pestaña 6 (Packages) solo tiene 3 filas (single, multi, complete). El blueprint 8.1 dice "single-, multi- y five-gas prices" pero la realidad comercial probablemente tendrá paquetes de 2 gases, 3 gases, 4 gases — todos deberían estar calculados, o documentarse por qué solo se ofrecen tres niveles.

### CS-05 — Expression-of-interest form (`01_market/CS-05_expressions_of_interest.md`)

44 líneas. 14 preguntas en tabla, todas con su propósito explícito. Incluye aviso explícito de que "no reserva plaza" (línea 36). Pregunta por separado sobre CO/SO₂ simultáneo (líneas 24–25), que es exactamente el detalle que determina la capacidad de 3+6.

**Lo que está bien:** compacto, sin ambigüedad, alimenta CS-10 como pipeline stage "Interest".

**Lo que falta:**

- Falta pregunta sobre **certificado de calibración del analizador** (fecha de última calibración, próximo vencimiento). CS-09 lo pide, pero si se pregunta de entrada se filtran candidatos incompatibles.
- Falta campo de **fecha límite de respuesta** o, alternativamente, mecanismo de expiración del EoI.
- Falta mención al **idioma** en que el prospecto prefiere recibir la cotización.

### CS-06 — Quotation template (`03_sales_contracting/CS-06_quotes.md`)

116 líneas. 14 secciones, todas marcadas con `[FILL]` o `[CALC]`. Cuatro variantes de plantilla (standard, complete, international, institutional/closed).

**Lo que está bien:**

- Tabla de precio con desglose (common fee + gas fees + additional analyzer + taxes).
- Mecanismo de revisión de cotización (líneas 100–101): "Every revision retains the same quote family with a revision number."
- Variantes separadas para `International` (currency/export notes) y `Institutional/closed` (separate full-cost quotation).

**Lo que falta:**

- **No hay campo de "vigencia de la oferta" distinto de la fecha de expiración**. CS-01 lo cubre, pero CS-06 no lo refleja como campo de relleno.
- **No hay tabla de condiciones de pago aceptables** (anticipo 100%, 50/50, PO a 30/60/90 días, etc.). La sección 9 lo pide en texto libre pero un cliente espera ver el calendario de pagos tabulado.
- **Falta cláusula de "aceptación por silencio"** o mecanismo claro de aceptación (la sección 14 dice "[FILL]"). Para evitar cotizaciones zombies, hace falta regla dura: la oferta se considera aceptada solo con X.
- La variante `International` no incluye **consideraciones de impuestos de importación / IVA diferencial / withholding** que aplican para clientes fuera de Colombia. Es un hueco que puede generar conflictos en facturación.
- No hay link al **cálculo de viability** (CS-04 Tab 8) que justifique la cifra cotizada cuando es un cliente nuevo en moneda local.

### CS-07 — Registration / order form (`03_sales_contracting/CS-07_registrations.md`)

57 líneas. Tabla de 14 campos comerciales/legal con su `Required` y notas. Status logic en 7 estados encadenados (líneas 36–40). Checklist de aceptación al pie.

**Lo que está bien:** reuso explícito de `calaire-app`, `F-PSEA-05A`, `F-PSEA-04` para datos técnicos (línea 13), que es exactamente lo que pide el blueprint 11. Separación entre "Participant marketing consent" y el consentimiento del servicio (línea 29).

**Lo que falta:**

- **No hay campo de fecha/hora de aceptación** más granular que `Signature / acceptance date`. Para auditoría hace falta timestamp.
- **No hay campo de IP o canal de aceptación** (portal, email, firma física). Importante si hay disputa sobre si la orden fue recibida.
- **No hay campo de orden de prioridad** en caso de overbooking. La wait-list se maneja en CS-10, pero el orden de la lista debe establecerse en el momento de la inscripción.
- El status logic menciona `Wait-listed / Rejected / Withdrawn` como posibles desenlaces, pero **no hay rama para "Accepted pending revised quote"** (cuando la oferta inicial no aplica exactamente al cliente y se requiere una nueva cotización). CS-06 cubre la revisión de la cotización, pero CS-07 no refleja esa transición.

### CS-08 — Terms and conditions (`03_sales_contracting/CS-08_terms.md`)

95 líneas. 18 cláusulas, con contenido real (no solo `[FILL]`) en las 3 que importan (assigned-value rule 12, evaluation indicators 13, pre-accreditation 17) — son las que el blueprint 12 exige como literales.

**Lo que está bien:** declaración explícita "This document defines content, not legal wording. Legal counsel or the University's authorized contracting function should approve the binding clauses" (líneas 12–13). Las tres cláusulas literales están blindadas contra copy-paste que rompa la regla.

**Lo que falta:**

- Casi todo el contenido contractual es `[FILL]`. Para que esto sea un contrato real, hace falta trabajo de legal.
- **No hay cláusula de resolución de disputas / jurisdicción / arbitraje**. La cláusula 18 dice "[FILL — legal counsel to draft]", pero en CS-06 sección 11 dice "Cancellation terms" sin referencia al foro.
- **No hay cláusula de protección de datos personales** (Habeas Data en Colombia). El CS-05 pide consentimiento comercial, pero los términos deben cubrir el tratamiento de datos personales según regulación colombiana (Ley 1581 de 2012).
- **No hay referencia al "tiempo máximo de respuesta"** en caso de queja o appeal (los procedimientos PSEA los tienen, pero el contrato debe comprometerlos).
- La cláusula 9 (deadlines, corrections, late submissions) debería tener tiempos concretos referenciados a PSEA, no solo "[FILL]".

### CS-09 — Contract/PO review checklist (`03_sales_contracting/CS-09_contract_reviews.md`)

52 líneas. 12 checks con `Evidence required` y `Pass / Fail / N/A`. Revisión con campos para reviewer, decisión y autorización.

**Lo que está bien:** check 7 ("PO does not silently override cancellation, confidentiality or report rules") es exactamente la protección que pide el blueprint 13. Check 9 (imparciality / conflict of interest) correctamente **escala al QMS** en vez de resolver localmente.

**Lo que falta:**

- No hay check de **disclosure consent** que distinga entre disclosure a terceros (autoridades regulatorias) y disclosure para fines comerciales (marketing). CS-07 los separa, CS-09 debería verificarlo.
- No hay check de **continuidad operativa**: si la ronda se cancela, ¿el PO queda automáticamente cancelado o requiere acción? CS-12 cubre el cambio, pero CS-09 debería haberlo detectado antes de aceptar.
- No hay check de **capacidad residual después de aceptar este PO** (i.e., ¿quedan plazas? ¿se está llenando el último cupo?). CS-10 lo monitorea, pero el check previo a la aceptación debe confirmar.
- La columna `Pass / Fail / N/A` está vacía en el template; sin embargo, en una operación real debe ser obligatorio (no opcional) firmar cada check. El template debería indicarlo.

### CS-10 — Enrollment and revenue tracker (`04_enrollment_restricted/CS-10_tracker.md`)

96 líneas. 20 columnas, 5 vistas, 2 flags automáticos de capacidad, controles de acceso.

**Lo que está bien:**

- Marca `RESTRICTED ACCESS`.
- Las 5 vistas (Pipeline, Enrollment, Viability, Receivables, Exceptions) son exactamente las que pide el blueprint 14.
- Flags de capacidad (líneas 81–84): "more than 4 confirmed positions" / "more than 3 participants or 6 analyzers".
- Control explícito: "Handoff to QMS round planning is a controlled export or approved participant list, not manual retyping" (línea 90).

**Lo que falta:**

- **No hay prioridad documentada en la wait-list**. CS-09 autoriza la wait-list, CS-12 cubre cambios, pero ¿cuál es el criterio de desempate: orden de inscripción, orden de pago, orden de EoI? Sin regla, la espera puede ser conflictiva.
- **No hay campo de "fecha límite de pago"** (cuándo expira la inscripción si no se ha recibido payment/PO). CS-07 dice "Pending payment/PO", pero la duración de ese estado debe estar acotada.
- **No hay manejo de pagos parciales o分期付款 (pagos en cuotas)**. Si CS-06 permite 50/50, el tracker debe distinguir "abonado" vs "saldo pendiente".
- La columna `Communication link/location` (línea 39) está abierta a cualquier sistema; sin regla sobre qué sistema de email/CRM se usa, el dato termina disperso.

### CS-11 — Confirmation and onboarding pack (`04_enrollment_restricted/CS-11_confirmations.md`)

86 líneas. Mensaje de confirmación con 12 campos, plantilla en bloque de texto, paquete de onboarding con 7 documentos y referencia QMS por cada uno.

**Lo que está bien:**

- El **mensaje de confirmación reproduce el status "Confirmed"** como hito explícito — solo los confirmados pasan a planificación de ronda.
- Onboarding pack con tabla referenciando QMS (DG-PSEA-01, I-PSEA-01, I-PSEA-02, F-PSEA-05A, F-PSEA-04, calaire-app) — esto es lo que pide el blueprint 15.
- Handoff a QMS con tres destinatarios explícitos: P-PSEA-04, F-PSEA-05A/F-PSEA-04/calaire-app, P-PSEA-05 (líneas 75–80).

**Lo que falta:**

- **No hay template de "rechazo" o "wait-list"** del lado del onboarding. Si CS-09 rechaza, el mensaje debe existir.
- **No hay fecha de expiración de la confirmación** ni manejo de "lo confirmé pero no respondiste en X días, plaza se libera".
- No hay campo para **participante adicional** (organizaciones que vienen con varias personas); CS-07 no lo pide, CS-11 debería definir quién es el "primary contact" y cómo se manejan los demás.

### CS-12 — Change, cancellation and refund record (`05_changes_finance/CS-12_change_cancellation_refund.md`)

56 líneas. 8 trigger events en checklist, 16 campos de registro, controles al pie.

**Lo que está bien:**

- **Doble autorización** para decisiones financieras (línea 47).
- Las quejas técnicas detectadas durante un cambio se enrutan a PSEA-15/16 (no se cierran comercialmente).
- Lista completa de trigger events alineada con blueprint 16.

**Lo que falta:**

- **No hay catálogo de fees por tipo de cambio**. La sección 7 del CS-01 (cancellation) está vacía, así que CS-12 referencia una tabla que no existe. El catálogo de "con X días de anticipación, retención Y%" debe estar poblado antes de aprobar CS-01.
- **No hay campo de impacto sobre la viabilidad del round**. Si un participante se retira y no se reemplaza, ¿la ronda sigue siendo viable? CS-04 (Tab 7) lo calcula, CS-12 debería referenciarlo.
- **No hay referencia al "tiempo de procesamiento de reembolso"** (cuánto tarda CALAIRE-EA en devolver el dinero). Crítico para el cliente.
- El control "Revisions to quotes follow CS-06 quote-control rules" es correcto, pero no se conecta con la trazabilidad de la cotización original (¿qué número de revisión tenía cuando se firmó?).

### CS-13 — Report delivery and participation message (`06_delivery_retention/CS-13_report_delivery.md`)

107 líneas. Dos plantillas (draft y final), participación statement con contenido permitido/prohibido, lista de chequeo de prohibido.

**Lo que está bien:**

- **Lista de prohibido** muy explícita (líneas 81–86): no claim de acreditación, no statement de competencia, no reemplazo del informe, no publicación de scores, no a1–a7. Esto blinda al comercial contra el error de sobre-claim.
- Diferencia explícita entre **draft (con appeal deadline)** y **final**.
- "The QMS already controls the technical report through P-PSEA-09 and F-PSEA-13" — referencia correcta al QMS.

**Lo que falta:**

- **No hay link a CS-12** para procesar correcciones derivadas del draft review. Si el participante apela, hay un cambio comercial + técnico que CS-12 debería registrar.
- **No hay manejo de "no recepción"** del draft por parte del participante (rebote de correo, buzón lleno). Procedimiento debería existir.
- El `Report-use reminder` está en `[FILL]` — debería tener un texto estándar, no personalizado por round, para no crear 15 versiones distintas.
- **No hay campo de "tiempo de retención del informe"** en nuestros sistemas después de la entrega final.

### CS-14 — Customer feedback form (`06_delivery_retention/CS-14_feedback.md`)

44 líneas. 10 preguntas con escala y tipo. Reglas de enrutamiento en 3 ramas (queja → PSEA, comercial → commercial lead, mejora → improvement register).

**Lo que está bien:** la regla de enrutamiento es lo mejor del documento — protege contra que una queja se cierre como comentario y no entre al procedimiento formal.

**Lo que falta:**

- **No hay campo de "fecha" en la respuesta**. Sin fecha, no se puede medir tiempo de respuesta ni segmentar por cohorte de ronda.
- **No hay canal formal de submission** definido (¿URL del formulario, email, app?). CS-05 sí lo define, CS-14 debería también.
- **No hay protección de anonimato** en las preguntas 7, 8, 9. Si el feedback es vinculado al participante, sus respuestas de mejora pueden ser comprometedoras; debe ofrecerse opción anónima.
- La pregunta 7 (gas/package interest for next round) duplica información que CS-05 ya captura al inicio. Habría que ligar las dos fuentes para no pedir dos veces lo mismo al mismo participante.

### CS-15 — Renewal / follow-up message and lead record (`06_delivery_retention/CS-15_renewal.md`)

70 líneas. Plantilla de email, lead record con 4 campos, controles (no marketing basado en performance, no claim de acreditación, check de consentimiento).

**Lo que está bien:** el control "Do not disclose or market based on confidential performance" (línea 24) es la barrera que evita que el comercial use los resultados como gancho de venta.

**Lo que falta:**

- **No hay SLA de envío** ("2–4 semanas" sugerido pero no comprometido). Sin SLA, el seguimiento se vuelve oportunista.
- **No hay contenido de renewal pricing** (¿hay descuento por renovación, paquete multi-round, prepago con descuento?). CS-04 no tiene lógica de fidelización; CS-15 debería conectar con un posible CS-04b "loyalty pricing" o documentar que no existe.
- **No hay manejo de "no respuesta"** al follow-up (¿cuántos reintentos?, ¿se cierra el lead?).
- No hay sincronización con CS-05 (EoI): si el participante responde al follow-up con intención de renovar, ¿se crea un nuevo EoI o se actualiza el lead record?

---

## 4. El problema crítico: la renumeración del QMS

**Hecho:** el documento `docs/sgc/matriz_equivalencias_codigos_sgc_pea.md` (estado: aprobada y aplicada para renumeración operativa, fecha 2026-06-14) renumeró toda la familia PSEA. Por ejemplo:

- Antiguo `P-PSEA-05` era "Procedimiento técnico SO2" → ahora `P-PSEA-13`.
- Antiguo `P-PSEA-17` era "Auditorías internas/externas" (retirado) → ahora `P-PSEA-17` es "Quejas del PEA".
- Antiguo `P-PSEA-18` era "Revisión por la dirección" (retirado) → ahora `P-PSEA-18` es "Apelaciones del PEA".
- Antiguo `P-PSEA-19` era "Imparcialidad institucional" (retirado) → ahora `P-PSEA-19` es "Confidencialidad operativa interna".
- Antiguo `P-PSEA-15` era "Mejora continua" → ahora `P-PSEA-15` es "Trabajo no conforme / NC / CAPA".
- Antiguo `F-PSEA-05A` era "Anexo técnico de equipos e instrumentos" → ahora `F-PSEA-04`.
- Antiguo `F-PSEA-04` era "Equipos e instrumentos" → ahora `F-PSEA-13` es "Informe final de resultados".

**Problema:** los artefactos comerciales引用an los códigos **con el significado antiguo**:

- `CS-05` y `CS-07`引用an `P-PSEA-19` para confidencialidad → correcto bajo la nueva numeración (P-PSEA-19 ahora es confidencialidad), pero un lector que venga del blueprint original (donde P-PSEA-19 era imparcialidad retirada) se confunde.
- `CS-09` y `CS-13`引用an `P-PSEA-17` y `P-PSEA-18` para quejas y apelaciones → **correcto bajo la nueva numeración**, pero el blueprint original usaba esos códigos con significados diferentes.
- `CS-09`, `CS-12`引用an `P-PSEA-15` y `P-PSEA-16` para NC/CAPA y divulgación de valores sensibles → **correcto bajo la nueva numeración**.
- `CS-11`引用an `F-PSEA-05A / F-PSEA-04` para datos de equipos → **incorrecto bajo la nueva numeración**: `F-PSEA-05A` ya no existe (ahora es `F-PSEA-04`); la referencia a `F-PSEA-04` colisiona con el nuevo `F-PSEA-04` que ES el anexo técnico. La lectura del template es ambigua.
- `CS-13`引用an `F-PSEA-13` para el informe final → **correcto bajo la nueva numeración**.

**Implicación:** el blueprint mismo arrastra las referencias antiguas, así que los artefactos son consistentes con su blueprint, pero **el blueprint no fue actualizado** después de la renumeración del 14 de junio. La consecuencia operativa:

- Si un auditor abre CS-11 buscando el "Anexo técnico de equipos" y va al QMS buscando `F-PSEA-05A`, no lo encuentra (porque ahora se llama `F-PSEA-04`).
- Si un implementador busca la "Confidencialidad" en el QMS usando `P-PSEA-19`, sí la encuentra, pero solo si conoce la nueva tabla; un recién llegado no.

**Acción sugerida:** crear una tabla de equivalencias en el README de `commercial_service/` o en la sección 0 de CS-01 que mapee cada referencia comercial a su código QMS vigente, y abrir un pendiente para actualizar el blueprint (sección 19 del `ptservice_art_prop.md`) en una próxima iteración. Esto es independiente de aprobar CS-01, pero el hueco debe quedar registrado.

---

## 5. Mejoras menores (no bloquean, conviene registrar)

1. **README no incluye convención de naming** (cómo se versionan, cómo se referencian, qué prefijo usar para borradores internos). Sugerencia: añadir una sección "Convenciones" de 5–8 líneas.

2. **Ningún artefacto tiene un "índice de cambios" inline**. El `release_change_log.md` existe pero los artefactos individuales solo tienen la última fila de aprobación. Para auditoría hace falta history local.

3. **CS-01, CS-04, CS-08 no tienen campo explícito de "idiomas aceptados"** del servicio (no del informe). El servicio puede ser en español, pero la documentación comercial puede ofrecerse bilingüe.

4. **CS-06 no tiene deadline de aceptación** explícito. La sección 1 (Quote header) tiene "Expiry date" pero no "Acceptance deadline" (que puede ser distinto de expiry).

5. **CS-08 cláusula 4 (Equipment transport, custody, installation, risk)** no hace referencia al `I-PSEA-01` (Embalaje y transporte), que es el documento que cubre esto en el QMS. Es un [FILL] que debería ser una referencia literal.

6. **CS-11 onboarding pack** tiene una fila "Facility and safety information" con [FILL]. Esto debería ser un documento fijo (no por round) que se referencia por link.

7. **CS-12 trigger event "Force majeure"** no tiene definición. ¿Qué eventos califican? Sin definición, "fuerza mayor" se vuelve litigable. Una cláusula de "fuerza mayor" sin perímetro es una puerta abierta a disputas.

8. **CS-15 timing** dice "approved post-round interval (e.g., 2–4 weeks after final report)" pero el "approved" no se ancla a CS-01. SinOwner documentado, la regla se vuelve informal.

9. **`artifact_register.md` columna "Version"** está vacía para los 14 PLANNED, pero CS-01 (DRAFT) tiene "0.1". Inconsistencia menor: el DRAFT tiene versión, los PLANNED no. Sugerencia: marcar todos como "0.0 PLANNED" o "—" uniformemente.

10. **`release_change_log.md`** tiene una sección "Pending changes" (líneas 18–23) que duplica el contenido del `artifact_register.md` columna "Status". Podría consolidarse para no mantener dos listas en paralelo.

11. **CS-05 pregunta 14** pide "Authorization for commercial follow-up" como checkbox. Para cumplimiento de protección de datos (Colombia: Ley 1581/2012, Decreto 1377/2013), el texto del consentimiento debe ser específico, no genérico.

12. **No hay artefacto "CS-00" o preámbulo** que explique el flujo completo de los 15 artefactos como journey. Un diagrama de flujo (mermaid o ASCII) que muestre cómo se conectan los 15 ayudaría a visualizar la cadena de valor. Podría vivir en el README o en un archivo nuevo `00_control/journey.md`.

---

## 6. Resumen de prioridades

**Antes de aprobar CS-01 (bloqueante):**

1. Diligenciar la sección 1 (Service identity) de CS-01 con el nombre legal del prestador y los roles.
2. Diligenciar la sección 3 (Pricing objective) — sin esto CS-04 no puede fijar margen.
3. Aprobar la estrategia de cilindros (sección 6) y registrar los dos approvers.
4. Definir las reglas de cancelación (sección 8) con tabla de tarifas por plazo. CS-12 las referenciará.
5. Crear la pestaña / método para "closed institutional round" en CS-04.
6. Documentar el round-use factor en la fórmula de lifecycle de CS-04.

**Antes del market release (no bloqueante para CS-01, sí para lanzamiento):**

7. Resolver las referencias QMS obsoletas por la renumeración (CS-11, blueprint sección 19).
8. Añadir evidencia esperada a cada [FILL] de CS-01 (al menos para los 5 campos más críticos).
9. Definir SLA de draft report, final report, y follow-up (CS-13, CS-15).
10. Definir idioma de trabajo del servicio y de la pieza comercial (CS-01, CS-02, CS-03).
11. Crear la journey map (diagrama) de los 15 artefactos.
12. Añadir cláusula de protección de datos personales en CS-08 (Habeas Data Colombia).
13. Definir criterio de desempate en wait-list (CS-10).

**Documentación complementaria:**

14. Crear `.gitkeep` y/o `OWNERS.md` por cada carpeta restringida.
15. Consolidar `release_change_log.md` y `artifact_register.md` para evitar duplicación.
16. Indexar los changelog in-place en cada artefacto.
