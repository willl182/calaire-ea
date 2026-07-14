# Access Control — `02_precios_restringidos/`

**Folder:** `servicio_comercial/02_precios_restringidos/`
**Classification:** RESTRICTED
**Propietario:** Financiero/comercial
**Last updated:** 2026-07-14

## Files in this folder

| File | Classification | Read access | Write access |
|---|---|---|---|
| `CS-04_modelo_costos_precios.md` | RESTRINGIDO: coste y margen internos | Finanzas, líder comercial, gerente de servicios, gestión | Finanzas + liderazgo comercial (doble autorización para cualquier cambio) |
| `listas_precio_aprobadas.md` | Orientación al cliente: publicado | Público (después de la aprobación) | Finanzas + liderazgo comercial (doble autorización) |

## Why this folder is restricted

- `CS-04_modelo_costos_precios.md` contiene **acumulación de costos internos**, **objetivos de margen**, **provisión del ciclo de vida por activo**, **comparación de costos de estrategia de cilindro** y **escenarios de equilibrio**. La divulgación a los participantes o competidores expondría la posición comercial de CALAIRE-EA y podría comprometer los precios futuros.
- El `listas_precios_aprobadas.md` orientado al cliente se publica solo después de que la gerencia apruebe los valores en `CS-04`; los datos de costos y márgenes nunca se publican.

## Access procedures

- **El acceso de lectura** se otorga a: equipo financiero, líder comercial, gerente de servicios, gerencia. Otros roles (coordinador de ronda, personal técnico) pueden solicitar acceso de lectura cuando sea necesario, registrado en el registro de auditoría.
- **El acceso de escritura** requiere doble autorización: un cambio propuesto es redactado por un rol y aprobado por el otro (líder financiero o comercial). Ambas firmas aparecen en el registro de cambios en línea del archivo afectado.
- **No se permite la exportación** del contenido `CS-04_modelo_costos_precios.md` a sistemas externos (correo electrónico, documentos orientados al cliente, SaaS de terceros) sin la aprobación explícita de la administración documentada en el registro de cambios en línea del archivo.
- **Versioning** of both files is tracked in `00_control/registro_cambios_versiones.md` plus each file's inline changelog.

## Audit

- Cualquier lectura o escritura de `CS-04_modelo_costos_precios.md` debe registrarse en el sistema de registro de acceso institucional.
- Revisión trimestral: el líder financiero y comercial verifica que las listas de acceso estén actualizadas.

## Related artifacts

- `00_control/CS-01_decisiones_comerciales.md` — objetivo y reglas de fijación de precios.
- `00_control/registro_cambios_versiones.md` — release history.
- `docs/qms/` — no contiene datos de costos equivalentes; Los costos comerciales no están duplicados en el SGC.
