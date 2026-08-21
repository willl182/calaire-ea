# Lanzar registro de cambios

**Ubicación:** `servicio_comercial/00_control/registro_cambios_versiones.md`
**Propietario:** Directora del grupo
**Última actualización:** 2026-07-14


## Reglas

- Aquí se registra cada lanzamiento controlado de un artefacto comercial. Una "lanzamiento" es un cambio que afecta **múltiples artefactos simultáneamente** o que es lo suficientemente significativo como para requerir conocimiento entre equipos (por ejemplo, un cambio de regla CS-01 que se propaga a CS-02, CS-06, CS-08).
- Las revisiones por artefacto también se registran aquí, en una fila propia.
- Las revisiones de una cotización (CS-06) se rastrean en `03_ventas_contratacion/CS-06_cotizaciones.md` por familia de cotizaciones; este registro registra solo versiones a nivel de plantilla.
- Los cambios en los documentos técnicos del SGC se registran en `docs/qms/`; este registro cubre solo la capa de artefactos comerciales.
- Cada fila de lanzamiento debe incluir: fecha de lanzamiento, ID de artefacto afectado, versión y resumen de cambios.

## Cómo se relaciona este registro con el registro de artefactos

- `00_control/registro_artefactos.md` enumera el **estado actual** de cada artefacto (estado, versión, propietario, ubicación).
- Este `registro_cambios_versiones.md` enumera el **historial de lanzamientos** (cambios de plantilla entre artefactos).
- Este archivo es la única fuente del historial de revisiones; los artefactos no llevan tabla de aprobación interna.

Los dos son complementarios, no redundantes: el registro responde "¿cuál es el estado actual?", el registro responde "¿qué cambió en esta versión?".

## Registro

| Fecha de lanzamiento | ID(es) de artefactos | Versión | Resumen de cambios |
| --- | --- | --- | --- |
| [POR DILIGENCIAR] | CS-01 | 0,1 | Borrador inicial creado a partir del plano de MVP |
| 2026-07-14 | CS-01, CS-04, CS-11, CS-13 | 0,2 | Conciliación de la renumeración de códigos del SGC; guía de evidencia de CS-01; factor de uso por ronda y pestaña 6.A de CS-04; corrección del código del SGC en el paquete de incorporación CS-11; recordatorio estándar de uso del informe en CS-13, enlace con CS-12 y manejo de falta de recepción |
| 2026-07-14 | CS-02, CS-03, CS-05, CS-06, CS-07, CS-08, CS-09, CS-10, CS-11, CS-12, CS-14, CS-15 | 0,2 | Mejoras menores por artefacto: idioma, versión, fechas de calibración, tablas de pago, ramas de consentimiento, lista de espera, autorización dual, anonimato, SLA, sincronización CS-05. |
| 2026-07-14 | 00_control (nuevo) | 1.0 | Se agregaron `equivalencia_codigos_sgc.md` y `mapa_viaje.md` para admitir lectores de artefactos |
| 2026-07-14 | 02_precios_restringidos, 04_inscripcion_restringida (nuevos) | 1.0 | Se agregó `PROPIETARIOS.md` a cada carpeta restringida |
| 2026-07-14 | README | 0.2 | Se agregaron la sección de convenciones, la referencia al mapeo de códigos del SGC y las referencias cruzadas |
| 2026-07-14 | ptservice_art_prop.md (modelo) | 0,2 | Artículo 19 actualizado con códigos post-renumeración; se añade una nueva subsección 19.1 |
| 2026-07-14 | CS-01, CS-08, CS-09, CS-13, README, registro_artefactos | correctivo | Unificación del bloque estándar "uso del informe" en CS-01 §9, CS-08 cláusula 16 y CS-13 (texto idéntico, incluye frase de uso íntegro y autorización de distribución); corrección de rutas de carpeta traducidas en README y registro_artefactos; corrección de terminología ("Profesional de proyectos", "cupo", "verificación"); estados PLANIFICADO actualizados a BORRADOR en artefactos con contenido redactado |
| 2026-07-14 | Todos los artefactos + soportes | correctivo | Nombres de archivos y carpetas traducidos al español (sin tildes), incluida la raíz `servicio_comercial/`; referencias actualizadas en artefactos, README, plan maestro (`ptservice_art_prop.md` §22) y `scripts/build_cs10_tracker.py` |

## Cambios pendientes

| Fecha prevista | ID de artefacto | Cambio propuesto | Responsable | Bloqueador |
|---|---|---|---|---|
| [POR DILIGENCIAR] | CS-01 | Aprobar reglas comerciales (cerrar todos los marcadores `[POR DILIGENCIAR]` con el visto bueno de la gerencia) | Directora del grupo | Aprobación de la dirección |
| [POR DILIGENCIAR] | CS-04 | Complete los supuestos de costos, provisiones del ciclo de vida, comparación de cilindros, derivación de referencia de la pestaña 6.A | Profesional de proyectos | aprobación CS-01; inventario de equipos + historial de mantenimiento |
| [POR DILIGENCIAR] | CS-02 | Borrador de contenido del catálogo (cerrar todos los marcadores narrativos `[POR DILIGENCIAR]`) | Profesional de proyectos | Aprobación CS-01 |
| [POR DILIGENCIAR] | CS-03 | Aviso de borrador de ronda para el próximo programa | Directora del grupo | Confirmación del calendario |
| [POR DILIGENCIAR] | CS-08 | Revisión jurídica de las cláusulas 18 (fuerza mayor, resolución de conflictos, responsabilidad) y 19 (protección de datos) | Gestión/jurídico | Contratación de asesoría jurídica |
| 2026-07-14 | CS-10 | Libro de trabajo operativo protegido implementado con indicadores de capacidad/pago/EoI obsoleto, valores controlados, vistas requeridas y simulación sintética | Directora del grupo | Almacenamiento institucional, cambio de contraseña y aprobación del propietario pendientes |
| 2026-07-14 | CS-02, CS-03, CS-04, CS-05, lista de precios aprobada | Artefactos reformulados como propuesta de viabilidad; copia completa del catálogo, eliminación de la etapa del informe preliminar, alineación de la EoI con la política de COP únicamente, registro de cantidades de mano de obra provisionales y eliminación del punto de referencia no aprobado de la lista publicable | Directora del grupo + Profesional de proyectos | Quedan pendientes la publicación y la aprobación del precio |
| [POR DILIGENCIAR] | Todo | Resolver los marcadores `[POR DILIGENCIAR]` restantes identificados en la revisión `logs/history/260714_0927_review-ptservice-art-impl.md` | Varios | Dependencias secuenciales de la aprobación CS-01 |
