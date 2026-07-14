# Lanzar registro de cambios

**Location:** `servicio_comercial/00_control/registro_cambios_versiones.md`
**Propietario:** Gerente de servicio
**Last updated:** 2026-07-14

## Rules

- Aquí se registra cada lanzamiento controlado de un artefacto comercial. Una "lanzamiento" es un cambio que afecta **múltiples artefactos simultáneamente** o que es lo suficientemente significativo como para requerir conocimiento entre equipos (por ejemplo, un cambio de regla CS-01 que se propaga a CS-02, CS-06, CS-08).
- Las revisiones por artefacto (por ejemplo, corregir un error tipográfico solo en CS-11) se rastrean **solo en el registro de cambios en línea en la parte inferior del artefacto afectado**, no aquí. Esto evita la duplicación y mantiene local el historial de cada artefacto.
- Las revisiones de una cotización (CS-06) se rastrean en `03_ventas_contratacion/CS-06_cotizaciones.md` por familia de cotizaciones; este registro registra solo versiones a nivel de plantilla.
- Los cambios en los documentos técnicos del SGC se registran en `docs/qms/`; este registro cubre sólo la capa de artefactos comerciales.
- Cada fila de lanzamiento debe incluir: fecha de lanzamiento, ID de artefacto afectado, versión, resumen de cambios, autor, aprobador y fecha de vigencia.

## Cómo se relaciona este registro con el registro de artefactos

- `00_control/registro_artefactos.md` enumera el **estado actual** de cada artefacto (estado, versión, propietario, ubicación).
- Este `registro_cambios_versiones.md` enumera el **historial de lanzamientos** (cambios de plantilla entre artefactos).
- Para conocer el historial de revisiones por artefacto, consulte el registro de cambios en línea en la parte inferior de cada artefacto (última tabla del archivo).

Los dos son complementarios, no redundantes: el registro responde "¿cuál es el estado actual?", el registro responde "¿qué cambió en esta versión?".

## Log

| Fecha de lanzamiento | ID(es) de artefactos | Versión | Resumen de cambios | Autor | Aprobador | Efectividad |
|---|---|---|---|---|---|---|
| [RELLENO] | CS-01 | 0,1 | Borrador inicial creado a partir del plano de MVP | [RELLENO] | [RELLENO] | Tras la aprobación |
| 2026-07-14 | CS-01, CS-04, CS-11, CS-13 | 0,2 | Código QMS que renumera la conciliación; Guía de evidencia CS-01; CS-04 factor de uso redondo + Tab 6.A + Tab 10; Corrección del código QMS del paquete de incorporación CS-11; Recordatorio de uso de informe estándar CS-13 + enlace CS-12 + manejo sin recepción | [RELLENO] | [RELLENO] | Tras la aprobación |
| 2026-07-14 | CS-02, CS-03, CS-05, CS-06, CS-07, CS-08, CS-09, CS-10, CS-11, CS-12, CS-14, CS-15 | 0,2 | Mejoras menores por artefacto: idioma, versión, fechas de calibración, tablas de pago, ramas de consentimiento, lista de espera, autorización dual, anonimato, SLA, sincronización CS-05. Vea el registro de cambios en línea de cada artefacto. | [RELLENO] | [RELLENO] | Tras la aprobación |
| 2026-07-14 | 00_control (nuevo) | 1.0 | Se agregaron `equivalencia_codigos_sgc.md` y `mapa_viaje.md` para admitir lectores de artefactos | [RELLENO] | [RELLENO] | Inmediato |
| 2026-07-14 | 02_precios_restringidos, 04_inscripcion_restringida (new) | 1.0 | Added `PROPIETARIOS.md` per restricted folder | [FILL] | [FILL] | Immediate |
| 2026-07-14 | README | 0.2 | Added conventions section, QMS code mapping reference, cross-references | [FILL] | [FILL] | Immediate |
| 2026-07-14 | ptservice_art_prop.md (modelo) | 0,2 | Artículo 19 actualizado con códigos post-renumeración; se añade una nueva subsección 19.1 | [RELLENO] | [RELLENO] | Inmediato |
| 2026-07-14 | CS-01, CS-08, CS-09, CS-13, README, registro_artefactos | correctivo | Unificación del bloque estándar "uso del informe" en CS-01 §9, CS-08 cláusula 16 y CS-13 (texto idéntico, incluye frase de uso íntegro y autorización de distribución); corrección de rutas de carpeta traducidas en README y registro_artefactos; corrección de terminología ("Líder comercial", "cupo", "verificación"); estados PLANIFICADO actualizados a BORRADOR en artefactos con contenido redactado | [RELLENO] | [RELLENO] | Inmediato |
| 2026-07-14 | Todos los artefactos + soportes | correctivo | Nombres de archivos y carpetas traducidos al español (sin tildes), incluida la raíz `servicio_comercial/`; referencias actualizadas en artefactos, README, blueprint (`ptservice_art_prop.md` §22) y `scripts/build_cs10_tracker.py` | [RELLENO] | [RELLENO] | Inmediato |

## Pending changes

| Fecha prevista | ID de artefacto | Cambio propuesto | Responsable | Bloqueador |
|---|---|---|---|---|
| [RELLENO] | CS-01 | Aprobar reglas comerciales (cerrar todos los marcadores `[FILL]` con el visto bueno de la gerencia) | Gerente de servicio | Aprobación de la dirección |
| [RELLENO] | CS-04 | Complete los supuestos de costos, provisiones del ciclo de vida, comparación de cilindros, derivación de referencia de la pestaña 6.A, fijación de precios institucionales de la pestaña 10 | Finanzas / comercial | aprobación CS-01; inventario de equipos + historial de mantenimiento |
| [RELLENO] | CS-02 | Borrador de contenido del catálogo (cerrar todos los marcadores narrativos `[FILL]`) | Líder comercial | Aprobación CS-01 |
| [RELLENO] | CS-03 | Aviso de borrador de ronda para el próximo programa | Coordinador de ronda | Confirmación del calendario |
| [RELLENO] | CS-08 | Revisión jurídica de las cláusulas 18 (fuerza mayor, resolución de conflictos, responsabilidad) y 19 (protección de datos) | Gestión/jurídico | Contratación de asesoría jurídica |
| 2026-07-14 | CS-10 | Libro de trabajo operativo protegido implementado con indicadores de capacidad/pago/EoI obsoleto, valores controlados, vistas requeridas y simulación sintética | Coordinador de ronda | Almacenamiento institucional, cambio de contraseña y aprobación del propietario pendientes |
| 2026-07-14 | CS-02, CS-03, CS-04, CS-05, lista de precios aprobada | Artefactos reformulados como propuesta de viabilidad; copia completa del catálogo, eliminación de la etapa del informe preliminar, alineación de la EoI con la política de COP únicamente, registro de cantidades de mano de obra provisionales y eliminación del punto de referencia no aprobado de la lista publicable | Responsable de servicios / comercial / Finanzas | Quedan pendientes la publicación y la aprobación del precio |
| [RELLENO] | Todo | Resolver los marcadores `[FILL]` restantes identificados en la revisión `logs/history/260714_0927_review-ptservice-art-impl.md` | Varios | Dependencias secuenciales de la aprobación CS-01 |
