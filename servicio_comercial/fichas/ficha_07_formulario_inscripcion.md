# Formulario de inscripción

**Archivo fuente:** `servicio_comercial/03_ventas_contratacion/CS-07_inscripciones.md`

## Propósito

Capturar al comprador: identidad legal, alcance seleccionado y datos administrativos y de facturación. Reutiliza los campos técnicos del SGC y de calaire-app en lugar de duplicarlos: solo agrega la sección comercial.

## Contenido clave

- Campos comerciales: nombre legal, identificación tributaria, facturación, número de cotización válido, paquete de gases, idioma del informe, contactos contractual y técnico.
- Evidencia de aceptación: marca de tiempo ISO 8601, canal (portal, correo, PDF firmado, papel) y origen IP si aplica — facilita resolver controversias.
- Consentimientos separados: aceptación de términos, selección de confidencialidad/divulgación y consentimiento de mercadeo (texto Ley 1581/2012 aparte del consentimiento del servicio).

## Se conecta con

- El número de cotización debe ser válido, no vencido y no aceptado por otra parte.
- Cerrar la inscripción dispara la revisión de contrato; los datos técnicos van por los formularios vigentes del SGC.

## Reglas críticas

- Solo los participantes confirmados pasan a la planificación formal de la ronda.
- Si la cotización aceptada requiere revisión, el registro pasa a «revisión de cotización en curso» y vuelve a «cotizado» con nueva revisión.

---

*Documento de consulta · corte al 2026-07-16 · índice: [indice.md](indice.md)*
