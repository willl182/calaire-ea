# I-PSEA-09 — Instrucciones a Participantes

**Código:** I-PSEA-09  
**Nivel:** 3b — Instructivo Técnico  
**Estado:** skeleton  
**Versión:** 0.1-draft  
**Cláusulas ISO/IEC 17043:2023:** 7.3.5, 7.1.2.1  
**ISO 13528:2022:** 5.3  
**Oleada:** 1  
**Prioridad:** 🟠 Alta — requerido antes del inicio de la ronda  
**Alimenta a:** F-PSEA-12 (Reporte del Participante), F-PSEA-05A (Registro del Participante)  
**Referencia base:** `docs/docs_sgc/comunicacion_2_participantes.md` (segunda comunicación, auditada ✅)

---

> **Instrucción general para el redactor:**  
> Este instructivo define (1) el **procedimiento** que sigue el Coordinador EA para preparar y distribuir las instrucciones a los participantes, y (2) el **contenido mínimo** que esas instrucciones deben contener según ISO/IEC 17043:2023 §7.3.5.  
> El contenido técnico detallado ya existe en `docs/docs_sgc/comunicacion_2_participantes.md`, que pasa como **Comunicación Oficial Pre-Ronda** y ha sido auditada contra la norma (`docs/instrucciones/compliance_comunicacion.md`). Este instructivo formaliza ese proceso dentro del SGC.

---

## 1. Objeto

> **Instrucción:** Describir en 1–2 oraciones qué define este instructivo y su propósito dentro del SGC.

Definir el contenido mínimo, el proceso de preparación y el mecanismo de distribución de las instrucciones formales que el Esquema CALAIRE-EA entrega a cada participante antes del inicio de una ronda de ensayo de aptitud, en cumplimiento de la cláusula 7.3.5 de ISO/IEC 17043:2023.

---

## 2. Alcance

> **Instrucción:** Delimitar rondas, participantes, analitos y fase del ciclo PT que cubre este instructivo.

Este instructivo aplica a todas las rondas del Esquema CALAIRE-EA. Para la **Prueba Piloto 2026**, aplica a:

| Ronda | Participantes | Analitos | Semana |
|---|---|---|---|
| Ronda Simple | P1 (SIATA) | CO, SO₂ | Sem. 1 (20–25 abr) |
| Ronda Compleja F1 | P1 + P2 (SIATA + UPB) | O₃, NO, NO₂ | Sem. 2 (27 abr–2 may) |
| Ronda Compleja F2 | P2 (UPB) | CO, SO₂ | Sem. 2 (cierre) |

Aplica desde el momento en que se confirma la lista de participantes (F-PSEA-07) hasta el inicio del primer día de medición de cada ronda.

No cubre: el análisis de resultados (→ I-PSEA-11), la evaluación de desempeño (→ I-PSEA-12) ni el informe de resultados (→ P-PSEA-07).

---

## 3. Referencias

| Norma / Documento | Cláusula / Sección | Aspecto |
|---|---|---|
| ISO/IEC 17043:2023 | 7.3.5 | Instrucciones a participantes — contenido mínimo |
| ISO/IEC 17043:2023 | 7.1.2.1 | Información del esquema a los participantes |
| ISO/IEC 17043:2023 | 7.3.4 | Manejo y distribución de ítems PT |
| ISO 13528:2022 | 5.3 | Instrucciones de medición y reporte |
| DG-PSEA-01 | § (protocolo general) | Protocolo general del esquema |
| P-PSEA-20 | completo | Procedimiento de comunicación con participantes |
| F-PSEA-05A | completo | Hoja de Registro del Participante |
| F-PSEA-12 | completo | Reporte del Participante |
| `comunicacion_2_participantes.md` | completo | Plantilla de comunicación oficial pre-ronda |

---

## 4. Definiciones

| Término | Definición |
|---|---|
| **Participante** | Laboratorio o entidad que participa en el esquema PT bajo un código anónimo (P1, P2, …) |
| **Ítem PT** | Atmósfera gaseosa de concentración conocida generada dinámicamente por CALAIRE y distribuida simultáneamente a todos los analizadores conectados al manifold |
| **Manifold** | Sistema de distribución de vidrio que garantiza la entrega homogénea del ítem PT a todas las líneas de medición |
| **σ_pt** | Desviación estándar de aptitud: criterio de variabilidad aceptable para evaluar el desempeño del participante |
| **u(x_pt)** | Incertidumbre estándar del valor asignado: combinación de u_char, u_hom, u_stab |
| **z-score** | Puntuación de desempeño cuando u(x_pt) ≤ 0,3·σ_pt |
| **z'-score** | Puntuación de desempeño cuando u(x_pt) > 0,3·σ_pt (incorpora incertidumbre del valor asignado) |
| **ζ-score (zeta)** | Puntuación que evalúa desempeño e incertidumbre declarada del participante simultáneamente |
| **En-score** | Puntuación basada en incertidumbres expandidas (k=2); |En| ≤ 1.0 = satisfactorio |
| **Promedio horario** | Promedio de los datos minutales continuos registrados durante 1 hora de estabilización a cada nivel de concentración |

---

## 5. Responsabilidades

| Rol | Responsabilidades |
|---|---|
| **Coordinador EA** | Preparar, personalizar y distribuir las instrucciones; verificar recepción; atender consultas; gestionar acceso a instalaciones |
| **Técnico CALAIRE** | Proveer datos técnicos del sistema de generación (niveles, gases, conexiones) para completar las instrucciones |
| **Participante** | Leer las instrucciones antes de la ronda; declarar equipos y personal en F-PSEA-05A; cumplir el protocolo de medición; reportar resultados en el plazo indicado |
| **Responsable SGC** | Revisar y aprobar las instrucciones antes de la distribución; verificar trazabilidad normativa |

---

## 6. Procedimiento

### 6.1 Preparación del paquete de instrucciones

> **Instrucción:** Describir los pasos para armar el paquete de documentos que se envía al participante. Los tiempos T-N son relativos al primer día de medición de cada ronda.

**Plazo:** T-14 días (dos semanas antes de la ronda)

1. El Coordinador EA recupera la plantilla de comunicación oficial (`comunicacion_2_participantes.md`) y la personaliza con:
   - Nombre y código del participante (P1, P2)
   - Ronda específica (Simple / Compleja F1 / Compleja F2)
   - Analitos de la ronda
   - Fechas exactas (instalación, medición, recolección)
   - Fecha límite de respuesta de F-PSEA-05A
   - Datos de contacto del coordinador: `[Nombre] — [Teléfono] — [Email]`

2. Verificar que la comunicación incluye el **contenido mínimo** requerido por ISO 17043:2023 §7.3.5 (ver §6.3 de este instructivo).

3. Adjuntar al correo:
   - F-PSEA-01 (Calendario del EA) — versión de la ronda correspondiente
   - F-PSEA-02 (Cronograma Detallado) — versión de la ronda correspondiente
   - F-PSEA-05A (Hoja de Registro del Participante) — encabezado pre-llenado con código y ronda
   - I-PSEA-01 (Instructivo de Embalaje y Transporte) — si aplica

4. Registrar el envío en F-PSEA-07 (Lista Maestra de Participantes): fecha de envío, canal y nombre del destinatario.

---

### 6.2 Contenido mínimo de las instrucciones (§7.3.5)

> **Instrucción:** Esta sección documenta formalmente qué debe contener la comunicación. Cada ítem tiene su fuente en la plantilla y su referencia normativa.

| # | Elemento requerido | Fuente en plantilla | Norma |
|---|---|---|---|
| 1 | Descripción del esquema (qué es, para qué sirve) | §2 "¿Qué es un EA?" | 17043 §7.1.2.1 |
| 2 | Analitos, niveles de concentración y unidades | §3 "¿Qué se mide?" | 17043 §7.3.5.2(b) |
| 3 | Naturaleza del ítem PT (generación dinámica, manifold) | §4 "¿Cómo se genera?" | 17043 §7.3.5.2(b) |
| 4 | Protocolo de medición día a día | §5 "¿Cómo se desarrolla?" | 17043 §7.3.5.2(c)(e) |
| 5 | Lista completa de equipos requeridos | §6 "¿Qué equipos traer?" | 17043 §7.3.5.2(a) |
| 6 | Formato de reporte: cifras decimales, datos crudos, incertidumbre | §7 "¿Cómo reportar?" | 17043 §7.3.5.2(f) |
| 7 | Criterios de evaluación (z, z', ζ, En) con umbrales | §8 "¿Cómo se evalúa?" | 17043 §7.4.2 |
| 8 | Procedimiento de confirmación (F-PSEA-05A) | §9 "Confirmación" | 17043 §7.2.1.3(j) |
| 9 | Política de confidencialidad y anonimato | §10 "Confidencialidad" | 17043 §4.2 |
| 10 | Contacto del coordinador | Pie de página | 17043 §7.1.2.1 |
| 11 | ⚠️ **Pendiente:** Origen de σ_pt por analito | No incluido en plantilla | 13528:2022 §5.3 |
| 12 | ⚠️ **Pendiente:** Proceso de apelaciones y quejas | No incluido en plantilla | 17043 §7.6–7.7 |
| 13 | ⚠️ **Pendiente:** Normativa transporte cilindros de gas | Mención parcial §6 | 17043 §7.3.4.4 |

> **Nota:** Los ítems marcados ⚠️ fueron identificados como brechas en la auditoría de cumplimiento (`compliance_comunicacion.md`). Deben incorporarse a la plantilla antes de la distribución final.

---

### 6.3 Brechas a resolver antes de distribuir

> **Instrucción:** Completar estos tres campos en la plantilla antes del envío. Consultar I-PSEA-07 para σ_pt y P-PSEA-09/DG-PSEA-01 para apelaciones.

**Brecha 1 — σ_pt por analito:**

Agregar en §8 de la comunicación una tabla con los valores de σ_pt prescrito para la prueba piloto:

| Analito | σ_pt (nmol/mol o µmol/mol) | Criterio origen |
|---|---|---|
| O₃ | [___] | [US-EPA / regulatorio / I-PSEA-07] |
| NO | [___] | |
| NO₂ | [___] | |
| SO₂ | [___] | |
| CO | [___] µmol/mol | |

**Brecha 2 — Apelaciones:**

Agregar párrafo en §10 o sección nueva §11:

> "Un participante que considere que su evaluación de desempeño es incorrecta puede presentar una apelación formal al Coordinador EA dentro de los 15 días posteriores a la recepción del informe individual. El proceso está documentado en [referencia a F-PSEA-17 o P-PSEA-22]."

**Brecha 3 — Transporte de cilindros:**

Agregar nota en §6 ("¿Qué equipos traer?"):

> "Los cilindros de gas patrón deben transportarse cumpliendo la normativa vigente de mercancías peligrosas (clase 2). Deben viajar en posición vertical, con tapa de seguridad, etiquetados según el fabricante, y sin exposición a fuentes de calor."

---

### 6.4 Distribución y seguimiento

> **Instrucción:** Completar con el canal oficial de envío y el procedimiento de confirmación de recepción.

**Plazo de distribución:** T-14 días

1. Enviar por correo electrónico a los contactos registrados en F-PSEA-07.
2. En el asunto del correo incluir: `[CALAIRE-EA] Instrucciones Pre-Ronda — [Código Ronda] — [Código Participante]`
3. En el cuerpo del correo incluir un resumen de los adjuntos y la fecha límite de respuesta de F-PSEA-05A.
4. Registrar envío en F-PSEA-07, columna "Instrucciones enviadas": fecha + canal + confirmación de lectura (Sí/Pendiente).

**Seguimiento:**

| T | Acción |
|---|---|
| T-14 días | Enviar paquete completo |
| T-7 días | Verificar recepción de F-PSEA-05A diligenciado; reenviar recordatorio si no hay respuesta |
| T-3 días | Confirmar asistencia, equipos y acceso a instalaciones |
| T-1 día | Enviar recordatorio de punto de encuentro, hora de llegada y contacto del día |

---

### 6.5 Gestión de consultas de participantes

1. Las consultas sobre el protocolo se responden en un plazo máximo de **48 horas hábiles**.
2. Si la consulta modifica alguna instrucción distribuida, el Coordinador emite una **fe de erratas** por el mismo canal y la registra en F-PSEA-07.
3. Las consultas sobre equipos o logística de la instalación se escalan al Técnico CALAIRE.

---

## 7. Criterios de aceptación

| Criterio | Condición | Resultado |
|---|---|---|
| Distribución en plazo | Instrucciones enviadas ≥ T-14 días antes de la ronda | ✅ Cumple / ❌ No cumple |
| Contenido mínimo completo | Los 13 elementos de §6.2 presentes (incluidas brechas resueltas) | ✅ Cumple / ❌ No cumple |
| Recepción confirmada | F-PSEA-05A recibido de todos los participantes antes de T-7 días | ✅ Cumple / ❌ No cumple |
| Sin brechas normativas abiertas | Ítems ⚠️ de §6.2 resueltos en la plantilla antes del envío | ✅ Cumple / ❌ No cumple |

---

## 8. Registros

| Formato | Descripción | Cuándo |
|---|---|---|
| F-PSEA-05A | Hoja de Registro del Participante (datos personales, equipos, logística) | Al enviar instrucciones; recibir antes de T-7 días |
| F-PSEA-07 | Lista Maestra de Participantes — columnas: instrucciones enviadas, recepción confirmada | Al enviar y al recibir confirmación |
| `comunicacion_2_participantes.md` | Plantilla de comunicación (versión personalizada por ronda/participante) | Archivar versión enviada como registro del SGC |
| Correo electrónico archivado | Evidencia de envío y recepción por participante | Archivar en carpeta del proyecto |

---

## 9. Secuencia de comunicación pre-ronda

```mermaid
gantt
    title Secuencia comunicación pre-ronda (días antes del Día 1)
    dateFormat  D
    axisFormat  T-%d

    section Coordinador EA
    Preparar paquete instrucciones     :done, p1, 14, 13
    Enviar paquete (T-14)              :milestone, m1, 14, 0d
    Seguimiento F-PSEA-05A             :active, p2, 13, 7
    Recordatorio T-7 si no hay respuesta :milestone, m2, 7, 0d
    Confirmar asistencia/equipos/acceso :p3, 6, 3
    Recordatorio T-1                   :milestone, m3, 1, 0d

    section Participante
    Leer instrucciones                 :p4, 13, 10
    Diligenciar y enviar F-PSEA-05A    :p5, 13, 7
    Preparar equipos                   :p6, 10, 1
    Llegada Día 1 (08:00 am)           :milestone, m4, 0, 0d
```

---

## Control de versiones

| Versión | Fecha | Descripción del cambio | Elaboró | Revisó | Aprobó |
|---|---|---|---|---|---|
| 0.1 | 2026-04-08 | Skeleton inicial — contenido basado en `comunicacion_2_participantes.md` (auditada ✅) | [Nombre] | — | — |
| 1.0 | [FECHA] | Versión para uso en prueba piloto — brechas §6.3 resueltas, aprobada | [Nombre] | [Nombre] | [Nombre] |
