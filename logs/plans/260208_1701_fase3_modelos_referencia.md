# Fase 3: Extracción de Modelos de Referencia

**Plan Padre**: `260208_1635_plan_ajuste-comunicacion-detallada-ea.md`
**Created**: 2026-02-08 17:01
**Status**: completed
**Brechas Objetivo**: 4 (Seguridad Industrial, Definición σpt, Quejas y Apelaciones, Declaración Subcontratación)

---

## Resumen Ejecutivo

Se extrajo contenido modelo de los 4 proveedores de referencia identificados en la matriz de hallazgos (Fase 1) para servir como base técnica en la redacción de mejoras (Fase 4).

| # | PDF Referencia | Sección Extraída | Estado |
|---|----------------|-----------------|--------|
| 3.1 | JRC-ERLAP | Safety (11.5) | Extraído |
| 3.2 | UBA | Quejas/Apelaciones | Extraído |
| 3.3 | UBA | Criterio de desempeno (σpt) | Parcial |
| 3.4 | Brno (PTPP_ZK) | Horn procedure (n<5) | Extraído |
| 3.5 | UCLSB | Subcontratación | Extraído |

---

## 3.1 JRC-ERLAP - Safety Section

**Documento**: `docs/referencias/Ejemplo Protocolo ERLAP GAS_PHASE_11_8_March_2023_protocol.pdf`
**Ubicación**: Sección 11.5 (página 16)
**Contexto**: Protocolo para gases inorgánicos contaminantes (SO2, CO, NO, NO2, O3)

### Contenido Extraído

```
11.5 Safety

JRC Ispra Site has one emergency number: +39 0332 78 9999. We strongly
recommend you to memorize the number on your mobile at the very beginning of the
list, in order to have it when needed. It is for both medical and non-medical
emergencies.
We would invite you not to walk around if you are not accompanied by JRC-ERLAP
staff. It is forbidden.
At JRC Ispra premises, Italian legislation for Safety at Work (D.lgs. 81/2008) is
implemented. Be sure you wear adequate work safety equipment, like work gloves
and safety shoes.
Pay attention to signs:
       - any circular plate, with a red diameter, indicates a forbidden action
       - any plate with blue background indicates a recommendation.
A fire extinguisher is placed at the entrance of the PT area.
We would invite you to respect JRC colleague's indications regarding safety and
installation timing, to avoid too many people on place.
Below are shown the two meeting points (Figure 2: Emergency signs) in case of
emergency. For nuclear emergency a double siren tone will be heard and
everybody must go to the internal assembly point. In case of non-nuclear
emergency the alarm will be a single tone sound and everybody is requested to go
outside and stay close to the external assembly point.

  - Posto di Raduno                         - Punto di Raccolta
  - Internal assembly point                 - External assembly point
  - In case of nuclear emergency            - In case of non-nuclear emergency
  - (Double tone siren)                     - (Single tone siren)
```

### Elementos Clave para CALAIRE-EA

| Elemento | Aplicabilidad CALAIRE-EA |
|----------|------------------------|
| Número de emergencia | Adaptar: contacto de emergencia del laboratorio anfitrión |
| EPP obligatorio | Adaptar: gloves, safety shoes, goggles para gases |
| Regulación de referencia | D.lgs. 81/2008 (Italia) → Normativa colombiana vigente |
| Señalización estandarizada | Prohibición (rojo), Recomendación (azul) |
| Extintor en área de PT | Ubicación de equipos de seguridad |
| Puntos de encuentro | Protocolo de evacuación del laboratorio |
| Restricción de circulación | Solo personal autorizado del PT |

### Observaciones Técnicas

- El documento de JRC-ERLAP enfatiza la normativa local (Italia) como base regulatoria
- Para CALAIRE-EA, se debe referenciar la normativa colombiana de seguridad industrial aplicable (MinTrabajo)
- La sección incluye procedimientos de emergencia nuclear, no aplicables a CALAIRE-EA
- El modelo es conciso pero cubre: emergencias, EPP, señalización, restricciones de movimiento

---

## 3.2 UBA - Quejas y Apelaciones

**Documento**: `docs/referencias/ejemplo UBA_proficiency_testing_scheme_2025.pdf`
**Ubicación**: Sección "Dealing with complaints/objections"
**Contexto**: Proficiency Testing Scheme for Water Analysis (Austria)

### Contenido Extraído

```
Dealing with complaints/objections:
  ⚫   All participants have the opportunity to report any complaints or objections by e-mail to
      ringversuche@umweltbundesamt.at within 14 days after receiving the confirmation of
      participation (containing information on assessment, on assigned values and criteria) and
      after receiving the report. Furthermore, questions, requests or suggestions by participants
      can be sent to ringversuche@umweltbundesamt.at.
  ⚫   All complaints and objections received by the proficiency testing provider will be handled ac-
      cording to our complaints management. In the event of a complaint or objection, the staff
      of the proficiency testing team will contact the participant. The facts of the case are then ex-
      amined internally and the participant is informed of the investigations carried out and the
      measures required. Complaints or objections are processed by experts form the proficiency
      testing team who were not involved in the matter in question. It is ensured that the complaint
      or objection does not result in any disadvantage to the complainant. The participant will be
      informed of the end of the processing of the complaint or objection.
  ⚫   In case of justified complaints or objections, the participants will be contacted by e-mail
      and informed about possible editorial or technical changes including reference to a new
      edition (e.g. report edition 2).
```

### Elementos Clave para CALAIRE-EA

| Elemento | Aplicabilidad CALAIRE-EA |
|----------|------------------------|
| Plazo para presentar quejas | 14 días → Adaptar: tiempo razonable según contexto |
| Canal de comunicación | Correo electrónico → Adaptar: canal definido en CALAIRE-EA |
| Momentos de aplicación | Confirmación de participación + Recepción del reporte |
| Proceso de manejo | Contacto inicial → Investigación interna → Información de medidas |
| Imparcialidad | Expertos no involucrados en el caso original |
| Protección del reclamante | "No result in any disadvantage to the complainant" |
| Resolución | Cambios editoriales o técnicos, nueva edición del reporte |

### Observaciones Técnicas

- El modelo de UBA sigue claramente los requisitos de ISO/IEC 17043:2023 clausula 8.5 (Appeals/Complaints)
- Define dos momentos de aplicación: (1) confirmación de participación, (2) recepción del reporte
- Establece explícitamente que el procesamiento es por expertos no involucrados (independencia)
- El plazo de 14 días es un estándar internacional adoptado por múltiples PT providers
- Incluye protección contra represalias para el reclamante (garantía de imparcialidad)

---

## 3.3 UBA - Criterio de Desempeno (σpt)

**Documento**: `docs/referencias/ejemplo UBA_proficiency_testing_scheme_2025.pdf`
**Ubicación**: Sección "Minimum concentrations and performance criterion"
**Contexto**: Definición del criterio de evaluación para PT de agua real

### Contenido Extraído

```
The criterion used to evaluate the participants' performance is the reproducibility standard devia-
tion calculated from previous rounds of proficiency testing with real water samples (more than 6
rounds, since 2013, see tables below). As an alternative criterion, the reproducibility standard devi-
ation vR is calculated from the participants' results after removal of outliers in the current round.
```

### Elementos Clave para CALAIRE-EA

| Elemento | Aplicabilidad CALAIRE-EA |
|----------|------------------------|
| Definición σpt | Reproducibility standard deviation |
| Fuente primaria | Rondas históricas del PT (>6 rondas) |
| Fuente alternativa | Resultados de la ronda actual (sin outliers) |
| Documentación | Tablas con valores por parámetro |

### Observaciones Técnicas

- UBA define σpt como "reproducibility standard deviation" (desviación estándar de reproducibilidad)
- El criterio se basa en datos históricos del propio esquema de PT (mínimo 6 rondas desde 2013)
- Existe un criterio alternativo para cuando no hay datos históricos suficientes: calcular vR de la ronda actual
- Para gases contaminantes, σpt se deriva típicamente de ISO 13528:2015 (métodos estadísticos para PT)
- Para CALAIRE-EA, se debe considerar que la Prueba Piloto es la primera ronda, por lo que σpt inicialmente se basará en valor asignado (ensayo de exactitud) y se documentará para futuras rondas

---

## 3.4 Brno (PTPP_ZK) - Horn Procedure

**Documento**: `docs/referencias/ejemplo PTPP_ZK 2023-1_EN.pdf`
**Ubicación**: Sección 2.1 (Specifications and Characteristics)
**Contexto**: Proficiency Testing Plan ZK 2023/1 – Aggregate Testing

### Contenido Extraído

```
2.1    Specifications and Characteristics
Testing laboratories and other institutions interested can register for the PTP. The minimum number
of participants is 5. If the number of participants is close to the minimum, the coordinator will consider
the evaluation of PTP results using Horn's procedure to determine the assigned value and measurement
uncertainty. The maximum number of participants is 30. If the minimum number of participants is not
reached, the PT Provider reserves the right to cancel the PTP.
```

### Elementos Clave para CALAIRE-EA

| Elemento | Aplicabilidad CALAIRE-EA |
|----------|------------------------|
| Número mínimo de participantes | 5 → Alineado con CALAIRE-EA |
| Condición de uso | "Close to the minimum" → Definir umbral (ej: n < 8) |
| Propósito | Determinar valor asignado e incertidumbre de medición |
| Responsable | Coordinador del PT |
| Cancelación si mínimo no alcanzado | Reserva del PT provider |

### Observaciones Técnicas

- Horn's procedure (Horn, 1983) es un método robusto para estimar valor asignado en muestras pequeñas (n < 10-15)
- Es un método no-paramétrico basado en mediana, por lo que es menos sensible a outliers
- Para CALAIRE-EA, Horn's procedure es relevante en:
  * Rondas piloto iniciales con pocos participantes
  * Muestras de gases donde n < 10 es posible
  * Casos donde la distribución de resultados no es normal
- Debe documentarse en el procedimiento estadístico de CALAIRE-EA el criterio de activación (ej: n < 8)
- La referencia original: Horn, J. (1983). Some easy T-statistics. J. Am. Stat. Assoc. 78, 930-936

---

## 3.5 UCLSB - Declaración de Subcontratación

**Documento**: `docs/referencias/ejemplo QF-4.4-1-MC-03-2022-ENG.pdf`
**Ubicación**: Sección 2.3 (The procedure for conducting...)
**Contexto**: Interlaboratory Technical Project MC 03/2022 (Building materials)

### Contenido Extraído

```
Accredited PT provider (organizer) SSLSB for this technical project will use the services of
Construction and testing center at TRA EOOD – a subcontractor of the PT provider under its
procedure and in the presence of members of its team. After evaluation of the results by the
technical expert and verification of homogeneity, the samples will be sent to the participants.
Otherwise, a new homogenization is performed according to the current procedures of the PT provider.
The stability of the samples will be determined by the subcontractor (Construction and testing
center at TRA EOOD) at the request of the PT provider through the same tests that were performed
to determine the level of homogeneity.
```

### Elementos Clave para CALAIRE-EA

| Elemento | Aplicabilidad CALAIRE-EA |
|----------|------------------------|
| Declaración explícita | "use the services of ... a subcontractor" |
| Responsabilidad | PT provider remains responsible |
| Procedimiento | "under its procedure" → Documentación formal |
| Supervisión | "in the presence of members of its team" |
| Actividades subcontratadas | Homogeneidad, estabilidad de muestras |
| Calificación | Subcontrator competente y bajo procedimiento formal |

### Observaciones Técnicas

- UCLSB declara explícitamente el uso de subcontratador para actividades específicas
- El PT provider mantiene responsabilidad total (requisito ISO/IEC 17043:2023 clausula 6.4)
- La subcontratación está bajo procedimiento formal y supervisión directa
- Para CALAIRE-EA, la subcontratación puede ser relevante en:
  * Elaboración de mezclas de gases (si se subcontrata)
  * Análisis de homogeneidad/estabilidad
  * Transporte especializado de cilindros
- La declaración debe incluir: nombre del subcontratador, actividades subcontratadas, criterios de selección

---

## Hallazgos de la Extracción

### Hallazgo #1: Seguridad Industrial
- **Fuente**: JRC-ERLAP (11.5 Safety)
- **Aplicabilidad**: Alta
- **Adaptación requerida**: Normativa colombiana, contexto de laboratorio de gases
- **Estado**: Listo para redacción en Fase 4

### Hallazgo #2: Quejas y Apelaciones
- **Fuente**: UBA (Dealing with complaints/objections)
- **Aplicabilidad**: Muy alta
- **Adaptación requerida**: Canal de comunicación específico de CALAIRE-EA
- **Estado**: Listo para redacción en Fase 4

### Hallazgo #3: Criterio de Desempeño (σpt)
- **Fuente**: UBA (Performance criterion)
- **Aplicabilidad**: Alta (para definición conceptual)
- **Adaptación requerida**: Definir σpt para gases según ISO 13528:2015
- **Estado**: Parcial - requiere complemento con estándares estadísticos para gases
- **Nota**: Para Prueba Piloto, σpt se basará en valor asignado (ensayo de exactitud)

### Hallazgo #4: Horn Procedure
- **Fuente**: Brno (PTPP_ZK 2023/1)
- **Aplicabilidad**: Alta (para escenarios con n < 8)
- **Adaptación requerida**: Definir umbral de activación en procedimiento CALAIRE-APP
- **Estado**: Listo para redacción en Fase 4

### Hallazgo #5: Declaración de Subcontratación
- **Fuente**: UCLSB (MC 03/2022)
- **Aplicabilidad**: Media (solo si aplica subcontratación en CALAIRE-EA)
- **Adaptación requerida**: Adaptar a contexto de gases contaminantes
- **Estado**: Listo para redacción en Fase 4

---

## Pendientes Especificos para σpt (Hallazgo #3)

Para completar la definición de σpt en Fase 4, se requiere:

| # | Pendiente | Accion | Prioridad |
|---|-----------|--------|-----------|
| 1 | Definicion formal σpt | Consultar `docs/iso 13528_2022.md` para definicion matematica de sigma para PT | Alta |
| 2 | Criterio para primera ronda | Definir metodo para determinar σpt en Prueba Piloto (sin datos historicos) | Alta |
| 3 | Fitness for purpose | Documentar criterio de "aptitud para el proposito" segun ISO/IEC 17043:2023 | Media |
| 4 | Aplicacion a gases | Validar metodo σpt para contaminantes gaseosos (SO2, CO, NO, NO2, O3) | Alta |

---

## Referencias Adicionales

Para complementar la información extraída, se recomienda consultar:

| Referencia | Propósito |
|------------|-----------|
| `docs/iso 13528_2022.md` | Métodos estadísticos para PT (σpt, Horn) |
| `docs/iso 17043_2023.md` | Requisitos de quejas/apelaciones (cláusula 8.5) |
| `docs/comparacion_comunicacion_vs_otras.md` | Análisis comparativo previo |

---

## Siguiente Fase

**Fase 4**: Redacción de Mejoras
- Utilizar los modelos extraídos como referencia técnica
- Redactar borradores lineados para cada mejora
- Considerar contexto específico de CALAIRE-EA (gases contaminantes, normativa colombiana)
- Documentar fuentes de referencia para cada sección

---

**Fin de Fase 3**
