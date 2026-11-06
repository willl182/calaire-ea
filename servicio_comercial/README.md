# Artefactos del servicio comercial CALAIRE-EA

Estructura de carpetas del sistema de artefactos comerciales MVP que convierte el esquema técnico de ensayos de aptitud de CALAIRE-EA en un servicio pago contratable.

## Estructura

| Carpeta | Contenido | Acceso |
|---|---|---|
<<<<<<< Updated upstream
| `00_control/` | CS-01 decisiones comerciales, registro de artefactos, registro de cambios de versiones, mapa de equivalencia de códigos SGC, mapa de viaje | Directora del grupo |
| `01_mercado/` | Catálogo, aviso de programa, formulario de manifestación de interés | Profesional de proyectos |
| `02_precios_restringidos/` | Modelo de costos y listas de precios aprobadas | Profesional de proyectos |
| `03_ventas_contratacion/` | Cotizaciones, inscripciones, condiciones, revisiones de contratos | Profesional de proyectos |
| `04_inscripcion_restringida/` | Seguimiento y confirmación / lista de espera / rechazo / paquetes de incorporación | Directora del grupo |
| `05_cambios_finanzas/` | Registros de cambios, cancelaciones y reembolsos | Directora del grupo + Profesional de proyectos |
| `06_entrega_retencion/` | Entrega de informes, retroalimentación, renovación | Directora del grupo |

## Reglas

- Todos los artefactos provienen del texto de `00_control/CS-01_decisiones_comerciales.md` o de documentos SGC existentes en `docs/qms/`.
- Ningún archivo fuera de `docs/qms/` se trata como el maestro SGC actual.
- Los registros de la ronda técnica permanecen en la estructura PEA/SGC en `docs/qms/`.
- `02_precios_restringidos/` y `04_inscripcion_restringida/` contienen datos de costo e identidad del participante: acceso controlado. El acceso por archivo puede ser más restrictivo que el nivel de carpeta; consulte `02_precios_restringidos/PROPIETARIOS.md` y `04_inscripcion_restringida/PROPIETARIOS.md`.

## Equivalencia de códigos del SGC (renumeración del 2026-06-14)
=======
| `00_control/` | CS-01 decisiones comerciales, registro de artefactos, registro de cambios de versiones, equivalencia de códigos SGC, mapa del recorrido | Gerente de servicio |
| `01_mercado/` | Catálogo, convocatoria de la ronda, formulario de expresión de interés | Líder comercial |
| `02_precios_restringidos/` | Modelo de costos y listas de precios aprobadas | Finanzas / comercial |
| `03_ventas_contratacion/` | Cotizaciones, inscripciones, términos y condiciones, revisiones de contrato | Líder comercial |
| `04_inscripcion_restringida/` | Seguimiento y confirmación / lista de espera / rechazo / paquetes de incorporación | Coordinador de ronda |
| `05_cambios_finanzas/` | Registros de cambios, cancelaciones y reembolsos | Comercial / finanzas |
| `06_entrega_retencion/` | Entrega de informes, retroalimentación, renovación | Coordinador de ronda |

## Reglas

- Todos los artefactos se derivan de `00_control/CS-01_decisiones_comerciales.md` o de documentos del SGC existentes en `docs/qms/`.
- Ningún archivo fuera de `docs/qms/` se considera la versión maestra vigente del SGC.
- Los registros técnicos de la ronda permanecen en la estructura PEA/SGC de `docs/qms/`.
- `02_precios_restringidos/` y `04_inscripcion_restringida/` contienen datos de costos e identidad de participantes: acceso controlado. El acceso por archivo puede ser más restrictivo que el de la carpeta; consulte `02_precios_restringidos/PROPIETARIOS.md` y `04_inscripcion_restringida/PROPIETARIOS.md`.

## Equivalencia de códigos SGC (renumeración del 2026-06-14)
>>>>>>> Stashed changes

El SGC tuvo una renumeración de códigos aprobada el 2026-06-14 (`docs/sgc/matriz_equivalencias_codigos_sgc_pea.md`). Los artefactos comerciales citan códigos `P-PSEA-XX`, `F-PSEA-XX`, `I-PSEA-XX` y `DG-PSEA-XX` que pueden haber cambiado de significado o número. La equivalencia usada por los artefactos está en:

- `00_control/equivalencia_codigos_sgc.md` — tabla completa para los códigos que aparecen en CS-01 a CS-15.

<<<<<<< Updated upstream
**En caso de duda:** si un artefacto hace referencia a un código `*-PSEA-NN`, verifique `00_control/equivalencia_codigos_sgc.md` antes de abrir el archivo SGC. El SGC tiene autoridad; esta tabla es una ayuda de traducción para lectores de artefactos.

## Fases

Los artefactos se completan y aprueban según las dependencias y puertas de control documentadas, sin asignar semanas artificiales.

## Convenciones

- **Nombre de archivo:** `CS-NN_nombre_corto.md` (por ejemplo, `CS-04_modelo_costos_precios.md`). Archivos aprobados solo dentro de la carpeta.
- **Control de versiones:** cada artefacto tiene una línea de "Última revisión" en el encabezado con la fecha y el resumen. Los cambios sustanciales incrementan la versión en el encabezado del artefacto Y `registro_cambios_versiones.md` (una entrada por versión).
- **Marcadores de estado:**
- "BORRADOR" — pendiente de aprobación; el contenido puede cambiar.
- `PLANIFICADO` — solo estructura; los marcadores `[POR DILIGENCIAR]` permanecen.
- `APROBADO`: el contenido está bloqueado; los cambios requieren una nueva revisión.
- **Guía de evidencia:** los marcadores `[POR DILIGENCIAR]` de nivel de decisión deben identificar la fuente de evidencia esperada (organigrama, política financiera, SGC, etc.) o señalar el artefacto de control. Consulte `CS-01_decisiones_comerciales.md` para ver el ejemplo canónico. Los campos de transacción en formularios reutilizables no requieren una nota de evidencia separada para cada marcador.
- **Referencias de códigos SGC:** al citar un código `*-PSEA-NN`, agregar un paréntesis con el código previo a la renumeración si el significado o el número cambió (e.g., "`F-PSEA-04` (post-renumeración; antiguo `F-PSEA-05A`)").
- **Registro de cambios:** el historial de versiones se lleva únicamente en `00_control/registro_cambios_versiones.md`; los artefactos no llevan tabla de aprobación interna.
- **Bloques de texto estándar:** algunos artefactos comparten texto exacto (por ejemplo, el "recordatorio de uso de informe" en la sección 9 de CS-01, la cláusula 16 de CS-08 y la plantilla de CS-13). Si es necesario cambiar un bloque estándar, actualice todas las instancias en la misma revisión y anote el cambio en `00_control/registro_cambios_versiones.md`.
=======
**En caso de duda:** si un artefacto cita un código `*-PSEA-NN`, verifique `00_control/equivalencia_codigos_sgc.md` antes de abrir el archivo del SGC. El SGC tiene la autoridad; esta tabla es una ayuda de lectura.

## Fases

1. **Fase 1 — congelar la oferta (semana 1):** aprobar CS-01.
2. **Fase 2 — precios y materiales de mercado (semanas 2 a 3):** completar CS-02 a CS-05.
3. **Fase 3 — flujo de pedido a confirmación (semanas 3 a 4):** completar CS-06 a CS-11.
4. **Fase 4 — flujo de excepciones y cierre (semana 5):** completar CS-12 a CS-15.
5. **Fase 5 — lanzamiento y piloto (semana 6):** capacitar a los usuarios, publicar CS-02/CS-03 y ejecutar el primer flujo pago.

## Convenciones

- **Nombre de archivo:** `CS-NN_nombre_corto.md` (por ejemplo, `CS-04_modelo_costos_precios.md`). Los archivos aprobados se guardan solo dentro de su carpeta.
- **Control de versiones:** cada artefacto tiene una línea de "Última revisión" en el encabezado con fecha y resumen. Los cambios sustanciales incrementan la versión en el encabezado del artefacto y en `registro_cambios_versiones.md` (una entrada por versión).
- **Estados:**
    - `BORRADOR` — pendiente de aprobación; el contenido puede cambiar.
    - `PLANIFICADO` — solo estructura; falta contenido.
    - `APROBADO` — contenido bloqueado; los cambios requieren una nueva revisión.
- **Campos de formulario:** los campos en blanco de los formularios reutilizables (cotización, inscripción, confirmación, etc.) se diligencian en cada transacción.
- **Referencias a códigos SGC:** al citar un código `*-PSEA-NN`, se agrega entre paréntesis el código anterior a la renumeración si cambió el significado o el número (p. ej., "`F-PSEA-04` (tras la renumeración; antes `F-PSEA-05A`)").
- **Historial de cambios en línea:** cada artefacto mantiene al final una tabla de 4 columnas (Versión, Fecha, Aprobador, Notas) con todas sus revisiones. `registro_cambios_versiones.md` es un **índice resumido** entre artefactos y no reemplaza esos historiales.
- **Bloques de texto estándar:** algunos artefactos comparten texto idéntico (por ejemplo, el "recordatorio de uso del informe" en la sección 9 de CS-01, la cláusula 16 de CS-08 y la plantilla de CS-13). Si se modifica un bloque estándar, se actualizan todas sus instancias en la misma revisión y se anota en el historial de cada artefacto afectado.
>>>>>>> Stashed changes

## Puertas de aprobación

| Puerta | Artefactos requeridos | Pregunta de aprobación |
|---|---|---|
<<<<<<< Updated upstream
| Lanzamiento al mercado | CS-01–CS-05 | ¿La oferta es precisa, tiene un precio, es comprensible y está honestamente posicionada? |
| Lanzamiento de cotización | CS-04, CS-06, CS-08 | ¿Se pueden defender y aceptar el precio y las condiciones? |
| Aceptación del pedido | CS-07–CS-10 | ¿Se alinean el alcance, la capacidad, los términos y el pago/PO? |
| Traspaso técnico | CS-11 + entradas del SGC | ¿Puede el proceso de planificación de rondas existente actuar sobre el pedido confirmado? |
| Cambio/reembolso | CS-12 | ¿Está documentado y autorizado el efecto financiero y de capacidad? |
| Entrega de informes | CS-13 + aprobación del informe SGC existente | ¿El informe controlado correcto va al destinatario correcto? |
| Cierre comercial | CS-14–CS-15 | ¿Se registran los comentarios, el estado de los ingresos y los intereses futuros? |

## Referencias cruzadas

- **Mapa del viaje:** consulta `00_control/mapa_viaje.md` para obtener una vista completa de cómo se conectan los 15 artefactos.
- **Registro de artefactos:** consulte `00_control/registro_artefactos.md` para obtener la lista canónica, propietarios y estados.
- **Registro de versiones:** consulte `00_control/registro_cambios_versiones.md` para conocer el historial de versiones entre artefactos (historial de versiones de los artefactos).
- **Fuente de la verdad de SGC:** `docs/qms/`. La capa comercial hace referencia, nunca se duplica.
- **Plan maestro de implementación:** `ptservice_art_prop.md` (documento principal).
=======
| Lanzamiento al mercado | CS-01–CS-05 | ¿La oferta es precisa, tiene precio, es comprensible y está posicionada con honestidad? |
| Emisión de cotizaciones | CS-04, CS-06, CS-08 | ¿El precio y las condiciones se pueden defender y aceptar? |
| Aceptación del pedido | CS-07–CS-10 | ¿Coinciden alcance, capacidad, términos y pago u orden de compra? |
| Traspaso técnico | CS-11 + entradas del SGC | ¿El proceso existente de planificación de la ronda puede actuar sobre el pedido confirmado? |
| Cambio / reembolso | CS-12 | ¿El efecto financiero y de capacidad está documentado y autorizado? |
| Entrega de informes | CS-13 + aprobación del informe en el SGC | ¿El informe controlado correcto llega al destinatario correcto? |
| Cierre comercial | CS-14–CS-15 | ¿Quedan registrados los comentarios, el estado de los ingresos y el interés futuro? |

## Referencias cruzadas

- **Mapa del recorrido:** `00_control/mapa_viaje.md` muestra cómo se conectan los 15 artefactos.
- **Registro de artefactos:** `00_control/registro_artefactos.md` contiene la lista canónica, propietarios y estados.
- **Registro de versiones:** `00_control/registro_cambios_versiones.md` contiene el historial de versiones entre artefactos.
- **Fuente de verdad del SGC:** `docs/qms/`. La capa comercial lo referencia y nunca lo duplica.
- **Documento base de implementación:** `ptservice_art_prop.md`.
>>>>>>> Stashed changes
