# Control de acceso — `02_precios_restringidos/`

<<<<<<< Updated upstream
**Carpeta:** `servicio_comercial/02_precios_restringidos/`
**Clasificación:** RESTRINGIDO
**Propietario:** Profesional de proyectos
**Última actualización:** 2026-07-14


## Archivos de esta carpeta

| Archivo | Clasificación | Acceso de lectura | Acceso de escritura |
|---|---|---|---|
| `CS-04_modelo_costos_precios.md` | RESTRINGIDO: costo y margen internos | Profesional de proyectos y Directora del grupo | Profesional de proyectos, con aprobación de la Directora del grupo |
| `listas_precio_aprobadas.md` | Orientación al cliente: publicado | Público (después de la aprobación) | Profesional de proyectos, con aprobación de la Directora del grupo |
=======
**Carpeta:** `servicio_comercial/02_precios_restringidos/`\
**Clasificación:** RESTRINGIDA\
**Propietario:** Finanzas / comercial\
**Última actualización:** 2026-07-14

## Archivos de esta carpeta

| Archivo | Clasificación | Acceso de lectura | Acceso de escritura |
|---|---|---|---|
| `CS-04_modelo_costos_precios.md` | RESTRINGIDO: costos y márgenes internos | Finanzas, líder comercial, gerente de servicio, dirección | Finanzas + líder comercial (doble autorización para cualquier cambio) |
| `listas_precios_aprobadas.md` | De cara al cliente: se publica | Público (después de la aprobación) | Finanzas + líder comercial (doble autorización) |
>>>>>>> Stashed changes

## Por qué esta carpeta es restringida

- `CS-04_modelo_costos_precios.md` contiene la **estructura de costos internos**, los **objetivos de precio**, la **provisión de ciclo de vida por activo**, la **comparación de costos de la estrategia de cilindros** y los **escenarios de punto de equilibrio**. Su divulgación a participantes o competidores expondría la posición comercial de CALAIRE-EA y podría comprometer precios futuros.
- `listas_precios_aprobadas.md` se publica solo después de que la dirección apruebe los valores en `CS-04`; los datos de costos y márgenes nunca se publican.

## Procedimientos de acceso

<<<<<<< Updated upstream
- **El acceso de lectura** se otorga al Profesional de proyectos y a la Directora del grupo. El personal técnico puede solicitar acceso de lectura cuando sea necesario, registrado en el registro de auditoría.
- **El acceso de escritura** requiere doble autorización: un cambio propuesto es redactado por un rol y aprobado por el otro (líder financiero o comercial). El cambio se registra en `00_control/registro_cambios_versiones.md`.
- **No se permite la exportación** del contenido `CS-04_modelo_costos_precios.md` a sistemas externos (correo electrónico, documentos orientados al cliente, SaaS de terceros) sin la aprobación explícita de la administración documentada en `00_control/registro_cambios_versiones.md`.
- El **control de versiones** de ambos archivos se registra en `00_control/registro_cambios_versiones.md`.
=======
- **Acceso de lectura:** equipo de finanzas, líder comercial, gerente de servicio y dirección. Otros roles (coordinador de ronda, personal técnico) pueden solicitarlo cuando sea necesario; la solicitud queda en el registro de auditoría.
- **Acceso de escritura:** requiere doble autorización; un rol redacta el cambio y el otro lo aprueba (finanzas o líder comercial). Ambas firmas quedan en el historial de cambios del archivo afectado.
- **No se permite exportar** el contenido de `CS-04_modelo_costos_precios.md` a sistemas externos (correo electrónico, documentos para clientes, servicios de terceros) sin aprobación explícita de la dirección registrada en el historial del archivo.
- **Versiones:** ambos archivos se registran en `00_control/registro_cambios_versiones.md` y en su propio historial de cambios.
>>>>>>> Stashed changes

## Auditoría

- Toda lectura o escritura de `CS-04_modelo_costos_precios.md` debe registrarse en el sistema institucional de registro de accesos.
- Revisión trimestral: finanzas y el líder comercial verifican que las listas de acceso estén actualizadas.

## Artefactos relacionados

- `00_control/CS-01_decisiones_comerciales.md` — objetivo y reglas de fijación de precios.
- `00_control/registro_cambios_versiones.md` — historial de versiones.
<<<<<<< Updated upstream
- `docs/qms/` — no contiene datos de costos equivalentes; los costos comerciales no están duplicados en el SGC.
=======
- `docs/qms/` — no contiene datos de costos equivalentes; los costos comerciales no se duplican en el SGC.
>>>>>>> Stashed changes
