# Mapa de viaje: 15 artefactos comerciales

**Propósito:** visualización de un extremo a otro de cómo se conectan los 15 artefactos de CS a lo largo del recorrido del cliente, desde el primer contacto hasta la renovación. Úselo para incorporar nuevos miembros al equipo, encontrar qué artefacto pertenece a un paso determinado e identificar brechas.


**Estado:** documento vivo. Se actualiza cada vez que se agrega, elimina un artefacto o cambia su alcance.

---

## Recorrido del cliente frente a cadena de artefactos

El recorrido del cliente (según la sección 1 del plan) es:

```text
Descubrir el servicio
      ↓
Comprender el alcance y las condiciones
      ↓
Seleccionar uno o más de los cuatro bloques de gases
      ↓
Recibir una cotización controlada
      ↓
Inscribirse y aceptar los términos
      ↓
Recibir la confirmación comercial
      ↓
Recibir las instrucciones técnicas existentes del SGC
      ↓
Participar en la ronda
      ↓
Recibir el informe y la declaración de participación
      ↓
Cerrar la facturación, los comentarios y la renovación
```

Los 15 artefactos CS se asignan a este viaje de la siguiente manera:

| Paso del viaje | Poseer artefacto(s) | Lo que ve el cliente | Cadena de artefactos internos |
|---|---|---|---|
| Descubra el servicio | Catálogo CS-02, aviso redondo CS-03 | Material de marketing, web/PDF | Referencias de catálogo CS-01 (decisiones) y CS-04 (lista de precios) |
| Comprender el alcance y las condiciones | Catálogo CS-02 (secciones 4, 5, 11) | Descripción del servicio | Lo mismo |
| Seleccionar uno o más de los cuatro bloques de gases | Formulario de expresión de interés CS-05 | Formulario de EoI (sin compromiso) | Etapa "Interés" del canal de oportunidades CS-10 |
| Reciba una cotización controlada | Plantilla de cotización CS-06 | Cotización PDF / correo electrónico | CS-09 (revisión de contrato) puertas CS-11 (confirmación) |
| Regístrate y acepta términos | Formulario de registro CS-07, términos CS-08 | Formulario de inscripción + términos firmados | CS-07 → CS-09 (revisión) |
| Recibir confirmación comercial | Mensaje de confirmación CS-11 (y mensajes de lista de espera/rechazo) | Correo electrónico de confirmación | CS-11 → Traspaso de SGC (P-PSEA-04, F-PSEA-04, F-PSEA-03, P-PSEA-05) |
| Recibir instrucciones técnicas del SGC | Paquete de incorporación CS-11 (enlaces a documentos de SGC) | DG-PSEA-01, I-PSEA-01, I-PSEA-02, calaire-app | CS-11 hace referencia al SGC, no comercial |
| Participa en la ronda | (Ejecución del SGC, no comercial) | n/a | n/a |
| Recibir informe y declaración de participación | Entrega de informe CS-13 | Borrador + informe final, declaración de participación | CS-13 → CS-12 si se necesitan cambios |
| Cerrar facturación, comentarios y renovación | Cambio/cancelación/reembolso de CS-12, comentarios de CS-14, renovación de CS-15 | Formulario de comentarios, correo electrónico de seguimiento | CS-12 (si hay cambios), CS-14 (comentarios), CS-15 (renovación) |

---

## Gráfico de dependencias de los artefactos (Mermaid)

```mermaid
flowchart TB
    CS01[CS-01 Decisiones comerciales] --> CS02[CS-02 Catálogo]
    CS01 --> CS03[CS-03 Aviso de ronda]
    CS01 --> CS04[CS-04 Modelo de costos]
    CS01 --> CS06[CS-06 Cotización]
    CS01 --> CS08[CS-08 Términos]
    CS04 --> CS06
    CS04 --> CS11[Lista de precios aprobada]

    CS02 --> CS05[CS-05 Expresión de interés]
    CS03 --> CS05
    CS05 --> CS10[(CS-10 Rastreador)]
    CS10 --> CS06

    CS06 --> CS07[CS-07 Inscripción]
    CS07 --> CS08
    CS07 --> CS09[CS-09 Revisión del contrato]
    CS09 --> CS10

    CS10 --> CS11[CS-11 Confirmación]
    CS11 --> SGC[(docs/qms/)]

    SGC --> CS13[CS-13 Entrega del informe]
    CS13 --> CS12[CS-12 Cambio/cancelación/reembolso]
    CS13 --> CS14[CS-14 Comentarios]
    CS14 --> CS15[CS-15 Renovación]
    CS12 --> CS10
    CS15 --> CS05
    CS15 --> CS10
```

---

## Gráfico de dependencias de los artefactos (alternativa ASCII)

```text
                       CS-01 (decisiones)
                       /    |    |    \
                      /     |    |     \
                 CS-02  CS-03 CS-04  CS-06, CS-08
                  |       |    |       |
                  v       v    v       v
                 CS-05 ---> CS-10 <--- (vista de capacidad)
                  |              ^
                  v              |
                 CS-06 ----------+
                  |
                  v
                 CS-07
                  |
                  v
                 CS-08  (términos)
                  |
                  v
                 CS-09  (revisión del contrato)
                  |
                  v
                 CS-10  (rastreador) ---> Confirmado
                  |
                  v
                 CS-11  (confirmación / lista de espera / rechazo)
                  |
                  v
                 [Traspaso al SGC: P-PSEA-04, F-PSEA-04, F-PSEA-03, P-PSEA-05]
                  |
                  v
              (ejecución de la ronda en el SGC)
                  |
                  v
                 CS-13  (entrega del informe)
                  |       \
                  |        --> CS-12 (si se requieren cambios durante la revisión del borrador)
                  v
                 CS-14  (retroalimentación)
                  |
                  v
                 CS-15  (renovación)
                  |       \
                  |        --> CS-10 (nueva entrada en el canal de oportunidades para la siguiente ronda)
                  |        --> CS-05 (para clientes potenciales nuevos, no para renovaciones)
                  v
              (regreso al inicio del recorrido para la siguiente ronda)
```

---

## Flujo de estado dentro de CS-10 (el sistema nervioso central)

El rastreador CS-10 es el núcleo operativo; casi todos los artefactos escriben o leen en él.

```text
[CS-05 Expresión de interés] ──> estado = Interés
                       │
                       v
[CS-06 Cotización] ──> estado = Cotizado
                       │
                       v
[CS-07 Inscripción] ──> estado = Inscrito
                       │
                       v
[CS-09 Revisión del contrato] ──> estado = En revisión
                       │
        ┌──────────────┼──────────────┐
        v              v              v
  Revisión de      Aceptado       Rechazado
  cotización       pendiente      (terminal)
  en curso         de pago/OC          │
        v              │               v
   (regreso a       estado =           (mensaje de
    Cotizado,       Confirmado          rechazo CS-11)
    nueva rev.)     (terminal)
        │              │               │
        v              v               v
   (CS-12)         [CS-11            (CS-10
                    confirmación]     cierre)

        Al agotarse la capacidad (verificación 4 o 6 de CS-09):
        estado = En lista de espera
            │
            ├──> Confirmado (si se libera un cupo) ──> [confirmación CS-11]
            │
            └──> Retirado (el cliente desiste)

        Al retirarse el cliente (en cualquier momento después de Inscrito):
        estado = Retirado
            │
            └──> CS-12 (reembolso / crédito)
```

---

## Mapa de puertas de aprobación (según la sección 21 del plan)

| Puerta | Artefactos requeridos antes de la puerta | Propietario de la aprobación |
|---|---|---|
| Lanzamiento al mercado | CS-01, CS-02, CS-03, CS-04, CS-05 | Responsable de servicios + profesional de proyectos |
| Lanzamiento de cotización | CS-04 (aprobado), CS-06, CS-08 | Profesional de proyectos |
| Aceptación del pedido | CS-07, CS-08 (firmado), CS-09 (aprobado), CS-10 (actualizado) | Profesional de proyectos |
| Traspaso técnico | CS-11 (enviado) + admisión de planificación de la ronda SGC | Directora del grupo |
| Cambio/reembolso | CS-12 (abierto, con doble autorización) | Directora del grupo + Profesional de proyectos |
| Entrega de informes | CS-13 + Aprobación del informe SGC | Directora del grupo |
| Cierre comercial | CS-14 (recibido), CS-15 (enviado), CS-10 (final) | Directora del grupo |

---

## Aspectos transversales (artefactos afectados)

| Aspecto | Artefactos afectados |
|---|---|
| Renumeración de códigos del SGC (2026-06-14) | CS-09, CS-11, CS-13, CS-14 (los que citan códigos PSEA) |
| Protección de datos (Ley 1581/2012) | CS-05 (consentimiento), CS-06 (transferencia internacional), CS-08 (cláusula 19), CS-15 (consentimiento comercial) |
| Capacidad (4 individuales / 3+6 simultáneos) | CS-01, CS-04, CS-09, CS-10, CS-11 |
| Redacción previa a la acreditación | CS-01, CS-02, CS-03, CS-06, CS-08, CS-13, CS-15 (en cualquier lugar de cara al cliente) |
| Moneda / cambio de divisas | CS-01, CS-04, CS-06, CS-10, CS-12 |
| Pago/evidencia de orden de compra | CS-07, CS-09, CS-10, CS-12 |
| Recordatorio estándar de uso de informes | CS-01, CS-08, CS-13 (debe coincidir exactamente) |

---

## Cómo usar este documento

- **Incorporación de un nuevo miembro del equipo:** recorra la tabla de recorrido del cliente y luego el gráfico Mermaid. Deberían poder localizar cualquier artefacto por paso del viaje.
- **Auditoría de una ronda:** comience en CS-13 (entrega), siga las flechas de regreso a CS-05 (interés). Verifique que la cadena esté intacta: cada participante confirmado tiene CS-09 (revisión) y CS-11 (confirmación) en su archivo.
- **Identificación de espacios:** el gráfico Mermaid resalta qué artefactos no tienen bordes entrantes o salientes. Si un artefacto está desconectado, es candidato a retirarse o una señal de falta de lógica.
- **Actualización del mapa:** cuando se agrega, elimina un artefacto o cambia su rol, actualizar la tabla de recorrido del cliente, el gráfico de dependencia y la tabla transversal.
