# Artefactos de servicio comercial CALAIRE-EA

Estructura de carpetas para el sistema de artefactos comerciales MVP que convierte el esquema PT técnico existente de CALAIRE-EA en un servicio pago contratable.

## Structure

| Folder | Contents | Access |
|---|---|---|
| `00_control/` | CS-01 decisiones comerciales, registro de artefactos, registro de cambios de versiones, mapa de equivalencia de códigos QMS, mapa de viaje | Gerente de servicio |
| `01_mercado/` | Catálogo, aviso de programa, formulario de manifestación de interés | Líder comercial |
| `02_precios_restringidos/` | Modelo de costes y listas de precios aprobadas | Finanzas / comercial |
| `03_ventas_contratacion/` | Cotizaciones, inscripciones, condiciones, revisiones de contratos | Líder comercial |
| `04_inscripcion_restringida/` | Seguimiento y confirmación / lista de espera / rechazo / paquetes de incorporación | Coordinador de ronda |
| `05_cambios_finanzas/` | Registros de cambios, cancelaciones y reembolsos | Comercial / finanzas |
| `06_entrega_retencion/` | Entrega de informes, retroalimentación, renovación | Coordinador de ronda |

## Rules

- Todos los artefactos provienen del texto de `00_control/CS-01_decisiones_comerciales.md` o de documentos QMS existentes en `docs/qms/`.
- Ningún archivo fuera de `docs/qms/` se trata como el maestro QMS actual.
- Los registros de la ronda técnica permanecen en la estructura PEA/QMS en `docs/qms/`.
- `02_precios_restringidos/` y `04_inscripcion_restringida/` contienen datos de costo e identidad del participante: acceso controlado. El acceso por archivo puede ser más restrictivo que el nivel de carpeta; consulte `02_precios_restringidos/PROPIETARIOS.md` y `04_inscripcion_restringida/PROPIETARIOS.md`.

## QMS code mapping (renumbering 2026-06-14)

El SGC sufrió una renumeración de códigos aprobada el 14-06-2026 (`docs/sgc/matriz_equivalencias_codigos_sgc_pea.md`). Los artefactos comerciales citan códigos `P-PSEA-XX`, `F-PSEA-XX`, `I-PSEA-XX`, `DG-PSEA-XX` que pueden haber cambiado de significado o número. El mapeo canónico utilizado por los artefactos se encuentra en:

- `00_control/equivalencia_codigos_sgc.md` — tabla de equivalencia completa para los códigos que aparecen en CS-01 a CS-15.

**En caso de duda:** si un artefacto hace referencia a un código `*-PSEA-NN`, verifique `00_control/equivalencia_codigos_sgc.md` antes de abrir el archivo QMS. El SGC tiene autoridad; Esta tabla es una ayuda de traducción para lectores de artefactos.

## Phases

1. **Fase 1: congelar la oferta (semana 1):** Aprobar CS-01.
2. **Fase 2: precio de construcción y materiales de mercado (semanas 2 a 3):** Complete CS-02 a CS-05.
3. **Fase 3: crear un flujo de pedido a confirmación (semanas 3 a 4):** Complete CS-06 a CS-11.
4. **Fase 4: excepción de compilación y flujo de cierre (semana 5):** Complete CS-12 a CS-15.
5. **Fase 5: Lanzamiento y prueba piloto (Semana 6):** Capacite a los usuarios, publique CS-02/CS-03, ejecute el primer flujo de trabajo de pago.

## Conventions

- **Nombre de archivo:** `CS-NN_short-name.md` (por ejemplo, `CS-04_modelo_costos_precios.md`). Archivos aprobados solo dentro de la carpeta.
- **Control de versiones:** cada artefacto tiene una línea de "Última revisión" en el encabezado con la fecha y el resumen. Los cambios sustanciales incrementan la versión en el encabezado del artefacto Y `registro_cambios_versiones.md` (una entrada por versión).
- **Marcadores de estado:**
- "BORRADOR" — pendiente de aprobación; El contenido puede cambiar.
- `PLANIFICADO` — solo estructura; los marcadores `[FILL]` permanecen.
- `APROBADO`: el contenido está bloqueado; los cambios requieren una nueva revisión.
- **Guía de evidencia:** los marcadores `[FILL]` de nivel de decisión deben identificar la fuente de evidencia esperada (organigrama, política financiera, QMS, etc.) o señalar el artefacto de control. Consulte `CS-01_decisiones_comerciales.md` para ver el ejemplo canónico. Los campos de transacción en formularios reutilizables no requieren una nota de evidencia separada para cada marcador.
- **Referencias de códigos QMS:** al citar un código `*-PSEA-NN`, agregar un paréntesis con el código previo a la renumeración si el significado o el número cambió (e.g., "`F-PSEA-04` (post-renumeración; antiguo `F-PSEA-05A`)").
- **Registro de cambios en línea:** cada artefacto mantiene una tabla de 4 columnas en la parte inferior (Versión, Fecha, Aprobador, Notas) que registra todas las revisiones. `registro_cambios_versiones.md` es un **índice resumido** de versiones entre artefactos, no un reemplazo de los registros de cambios en línea.
- **Bloques de texto estándar:** algunos artefactos comparten texto exacto (por ejemplo, el "recordatorio de uso de informe" en la sección 9 de CS-01, la cláusula 16 de CS-08 y la plantilla de CS-13). Si es necesario cambiar un bloque estándar, actualice todas las instancias en la misma revisión y anote el cambio en el registro de cambios en línea de cada artefacto afectado.

## Approval Gates

| Gate | Required artifacts | Approval question |
|---|---|---|
| Lanzamiento al mercado | CS-01–CS-05 | ¿La oferta es precisa, tiene un precio, es comprensible y está honestamente posicionada? |
| Lanzamiento de cotización | CS-04, CS-06, CS-08 | ¿Se pueden defender y aceptar el precio y las condiciones? |
| Aceptación del pedido | CS-07–CS-10 | ¿Se alinean el alcance, la capacidad, los términos y el pago/PO? |
| Traspaso técnico | CS-11 + entradas del SGC | ¿Puede el proceso de planificación circular existente actuar sobre el pedido confirmado? |
| Cambio/reembolso | CS-12 | ¿Está documentado y autorizado el efecto financiero y de capacidad? |
| Entrega de informes | CS-13 + aprobación del informe SGC existente | ¿El informe controlado correcto va al destinatario correcto? |
| Cierre comercial | CS-14–CS-15 | ¿Se registran los comentarios, el estado de los ingresos y los intereses futuros? |

## Cross-references

- **Mapa del viaje:** consulta `00_control/mapa_viaje.md` para obtener una vista completa de cómo se conectan los 15 artefactos.
- **Registro de artefactos:** consulte `00_control/registro_artefactos.md` para obtener la lista canónica, propietarios y estados.
- **Registro de versiones:** consulte `00_control/registro_cambios_versiones.md` para conocer el historial de versiones entre artefactos (solo cambios a nivel de plantilla; las revisiones por artefacto se encuentran en el registro de cambios en línea de cada artefacto).
- **Fuente de la verdad de QMS:** `docs/qms/`. La capa comercial hace referencia, nunca se duplica.
- **Implementation blueprint:** `ptservice_art_prop.md` (parent document).
