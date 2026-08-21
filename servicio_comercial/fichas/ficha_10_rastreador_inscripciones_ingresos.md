# Rastreador de inscripciones e ingresos

**Archivo fuente:** `servicio_comercial/04_inscripcion_restringida/CS-10_seguimiento.md`

## Propósito

Controlar capacidad, pedidos, pagos y viabilidad de la ronda. Es el núcleo operativo del sistema: casi todos los demás artefactos leen o escriben aquí, y es la vista en tiempo real del estado de cada oportunidad.

## Contenido clave

- Libro Excel institucional protegido, con plantilla limpia, copia de simulación sintética (nunca usar como registro vivo) y generador reproducible en scripts/build_cs10_tracker.py.
- Estados comerciales: interés → cotizado → registrado → en revisión → aceptado pendiente de pago → confirmado / lista de espera / rechazado / retirado.
- Columnas de control: fechas límite de aceptación y de pago, seguimiento de pagos parciales, capacidad consumida por bloque, indicador de último cupo, prioridad de lista de espera (grupo 1: laboratorio acreditado; grupo 2: demás elegibles).

## Se conecta con

- Recibe expresiones de interés, cotizaciones, inscripciones, decisiones de revisión, cambios y renovaciones.
- Los cambios de capacidad se reflejan de inmediato, sin actualizaciones por lotes.

## Reglas críticas

- No almacena resultados técnicos de participantes.
- La columna de comunicaciones solo apunta a calaire_med@unal.edu.co o carpetas institucionales controladas — nada de bandejas personales.
- Cambiar la contraseña de protección de hoja antes del uso real; acceso restringido por identidad de participantes.

---

*Documento de consulta · corte al 2026-07-16 · índice: [indice.md](indice.md)*
