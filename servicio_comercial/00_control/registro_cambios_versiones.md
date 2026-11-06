# Registro de cambios de versiones

<<<<<<< Updated upstream
**Ubicación:** `servicio_comercial/00_control/registro_cambios_versiones.md`
**Propietario:** Directora del grupo
**Última actualización:** 2026-07-14


## Reglas

- Aquí se registra cada lanzamiento controlado de un artefacto comercial. Una "lanzamiento" es un cambio que afecta **múltiples artefactos simultáneamente** o que es lo suficientemente significativo como para requerir conocimiento entre equipos (por ejemplo, un cambio de regla CS-01 que se propaga a CS-02, CS-06, CS-08).
- Las revisiones por artefacto también se registran aquí, en una fila propia.
- Las revisiones de una cotización (CS-06) se rastrean en `03_ventas_contratacion/CS-06_cotizaciones.md` por familia de cotizaciones; este registro registra solo versiones a nivel de plantilla.
- Los cambios en los documentos técnicos del SGC se registran en `docs/qms/`; este registro cubre solo la capa de artefactos comerciales.
- Cada fila de lanzamiento debe incluir: fecha de lanzamiento, ID de artefacto afectado, versión y resumen de cambios.
=======
**Ubicación:** `servicio_comercial/00_control/registro_cambios_versiones.md`\
**Propietario:** Gerente de servicio\
**Última actualización:** 2026-07-14

## Reglas

- Aquí se registra cada versión controlada de un artefacto comercial. Una "versión" es un cambio que afecta **múltiples artefactos simultáneamente** o que es lo suficientemente significativo como para requerir conocimiento entre equipos (por ejemplo, un cambio de regla CS-01 que se propaga a CS-02, CS-06, CS-08).
- Las revisiones por artefacto (por ejemplo, corregir un error tipográfico solo en CS-11) se rastrean **solo en el registro de cambios en línea en la parte inferior del artefacto afectado**, no aquí. Esto evita la duplicación y mantiene local el historial de cada artefacto.
- Las revisiones de una cotización (CS-06) se rastrean en `03_ventas_contratacion/CS-06_cotizaciones.md` por familia de cotizaciones; este registro registra solo versiones a nivel de plantilla.
- Los cambios en los documentos técnicos del SGC se registran en `docs/qms/`; este registro cubre sólo la capa de artefactos comerciales.
- Cada fila debe incluir: fecha, ID de artefacto afectado, versión, resumen de cambios, autor, aprobador y fecha de vigencia.
>>>>>>> Stashed changes

## Cómo se relaciona este registro con el registro de artefactos

- `00_control/registro_artefactos.md` enumera el **estado actual** de cada artefacto (estado, versión, propietario, ubicación).
<<<<<<< Updated upstream
- Este `registro_cambios_versiones.md` enumera el **historial de lanzamientos** (cambios de plantilla entre artefactos).
- Este archivo es la única fuente del historial de revisiones; los artefactos no llevan tabla de aprobación interna.
=======
- Este `registro_cambios_versiones.md` enumera el **historial de versiones** (cambios de plantilla entre artefactos).
- Para conocer el historial de revisiones por artefacto, consulte el registro de cambios en línea en la parte inferior de cada artefacto (última tabla del archivo).
>>>>>>> Stashed changes

Los dos son complementarios, no redundantes: el registro de artefactos responde "¿cuál es el estado actual?" y este registro responde "¿qué cambió en esta versión?".

## Registro

<<<<<<< Updated upstream
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
=======
| Fecha | ID(s) de artefactos | Versión | Resumen de cambios | Autor | Aprobador | Efectividad |
|---|---|---|---|---|---|---|
| 2026-07-12 | CS-01 | 0,1 | Borrador inicial creado a partir del documento base MVP | — | — | Tras la aprobación |
| 2026-07-14 | CS-01, CS-04, CS-11, CS-13 | 0,2 | Conciliación de la renumeración de códigos SGC; guía de evidencia CS-01; CS-04 factor de uso por ronda + pestaña 6.A + pestaña 10; corrección del código SGC del paquete de incorporación CS-11; recordatorio estándar de uso del informe en CS-13 + enlace a CS-12 + manejo de no recepción | — | — | Tras la aprobación |
| 2026-07-14 | CS-02, CS-03, CS-05, CS-06, CS-07, CS-08, CS-09, CS-10, CS-11, CS-12, CS-14, CS-15 | 0,2 | Mejoras menores por artefacto: idioma, versión, fechas de calibración, tablas de pago, ramas de consentimiento, lista de espera, autorización dual, anonimato, plazos, sincronización CS-05. Ver el historial de cambios de cada artefacto. | — | — | Tras la aprobación |
| 2026-07-14 | 00_control (nuevo) | 1.0 | Se agregaron `equivalencia_codigos_sgc.md` y `mapa_viaje.md` para admitir lectores de artefactos | — | — | Inmediato |
| 2026-07-14 | 02_precios_restringidos, 04_inscripcion_restringida (nuevo) | 1.0 | Se agregó `PROPIETARIOS.md` en cada carpeta restringida | — | — | Inmediato |
| 2026-07-14 | README | 0.2 | Se agregaron convenciones, referencia de equivalencia de códigos SGC y referencias cruzadas | — | — | Inmediato |
| 2026-07-14 | ptservice_art_prop.md (documento base) | 0,2 | Artículo 19 actualizado con códigos post-renumeración; se añade una nueva subsección 19.1 | — | — | Inmediato |
| 2026-07-14 | CS-01, CS-08, CS-09, CS-13, README, registro_artefactos | correctivo | Unificación del bloque estándar "uso del informe" en CS-01 §9, CS-08 cláusula 16 y CS-13 (texto idéntico, incluye frase de uso íntegro y autorización de distribución); corrección de rutas de carpeta traducidas en README y registro_artefactos; corrección de terminología ("Líder comercial", "cupo", "verificación"); estados PLANIFICADO actualizados a BORRADOR en artefactos con contenido redactado | — | — | Inmediato |
| 2026-07-14 | Todos los artefactos + soportes | correctivo | Nombres de archivos y carpetas traducidos al español (sin tildes), incluida la raíz `servicio_comercial/`; referencias actualizadas en artefactos, README, documento base (`ptservice_art_prop.md` §22) y `scripts/build_cs10_tracker.py` | — | — | Inmediato |
>>>>>>> Stashed changes

## Cambios pendientes

| Fecha prevista | ID de artefacto | Cambio propuesto | Responsable | Bloqueador |
|---|---|---|---|---|
<<<<<<< Updated upstream
| [POR DILIGENCIAR] | CS-01 | Aprobar reglas comerciales (cerrar todos los marcadores `[POR DILIGENCIAR]` con el visto bueno de la gerencia) | Directora del grupo | Aprobación de la dirección |
| [POR DILIGENCIAR] | CS-04 | Complete los supuestos de costos, provisiones del ciclo de vida, comparación de cilindros, derivación de referencia de la pestaña 6.A | Profesional de proyectos | aprobación CS-01; inventario de equipos + historial de mantenimiento |
| [POR DILIGENCIAR] | CS-02 | Borrador de contenido del catálogo (cerrar todos los marcadores narrativos `[POR DILIGENCIAR]`) | Profesional de proyectos | Aprobación CS-01 |
| [POR DILIGENCIAR] | CS-03 | Aviso de borrador de ronda para el próximo programa | Directora del grupo | Confirmación del calendario |
| [POR DILIGENCIAR] | CS-08 | Revisión jurídica de las cláusulas 18 (fuerza mayor, resolución de conflictos, responsabilidad) y 19 (protección de datos) | Gestión/jurídico | Contratación de asesoría jurídica |
| 2026-07-14 | CS-10 | Libro de trabajo operativo protegido implementado con indicadores de capacidad/pago/EoI obsoleto, valores controlados, vistas requeridas y simulación sintética | Directora del grupo | Almacenamiento institucional, cambio de contraseña y aprobación del propietario pendientes |
| 2026-07-14 | CS-02, CS-03, CS-04, CS-05, lista de precios aprobada | Artefactos reformulados como propuesta de viabilidad; copia completa del catálogo, eliminación de la etapa del informe preliminar, alineación de la EoI con la política de COP únicamente, registro de cantidades de mano de obra provisionales y eliminación del punto de referencia no aprobado de la lista publicable | Directora del grupo + Profesional de proyectos | Quedan pendientes la publicación y la aprobación del precio |
| [POR DILIGENCIAR] | Todo | Resolver los marcadores `[POR DILIGENCIAR]` restantes identificados en la revisión `logs/history/260714_0927_review-ptservice-art-impl.md` | Varios | Dependencias secuenciales de la aprobación CS-01 |
=======
| Por programar | CS-01 | Aprobar las puertas de liberación financiera, jurídica y técnica | Gerente de servicio | Aprobación de la dirección |
| Por programar | CS-04 | Completar los supuestos de costos, provisiones del ciclo de vida, comparación de cilindros, derivación de referencia de la pestaña 6.A, fijación de precios institucionales de la pestaña 10 | Finanzas / comercial | aprobación CS-01; inventario de equipos + historial de mantenimiento |
| Por programar | CS-02 | Aprobar la publicación del catálogo | Líder comercial | Aprobación CS-01 |
| Por programar | CS-03 | Convocatoria de la próxima ronda | Coordinador de ronda | Confirmación del calendario |
| Por programar | CS-08 | Revisión jurídica de las cláusulas 18 (fuerza mayor, resolución de conflictos, responsabilidad) y 19 (protección de datos) | Gestión/jurídico | Contratación de asesoría jurídica |
| 2026-07-14 | CS-10 | Libro de trabajo operativo protegido implementado con indicadores de capacidad, pago y expresiones de interés vencidas, valores controlados, vistas requeridas y simulación sintética | Coordinador de ronda | Almacenamiento institucional, cambio de contraseña y aprobación del propietario pendientes |
| 2026-07-14 | CS-02, CS-03, CS-04, CS-05, lista de precios aprobada | Artefactos reformulados como propuesta de viabilidad; copia completa del catálogo, eliminación de la etapa del informe preliminar, alineación de la expresión de interés con la política de COP únicamente, registro de cantidades de mano de obra provisionales y eliminación del punto de referencia no aprobado de la lista publicable | Responsable de servicios / comercial / Finanzas | Quedan pendientes la publicación y la aprobación del precio |
>>>>>>> Stashed changes
