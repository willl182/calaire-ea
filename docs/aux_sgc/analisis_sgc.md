# Análisis de Conectividad del SGC PEA

**Fecha:** 2026-06-13  
**Estado:** consolidado  
**Propósito:** evaluar la conectividad documental del SGC PEA contra dos reglas de arquitectura: (1) cada instructivo/documento debe estar anclado a un procedimiento, y (2) cada procedimiento debe tener una salida (formato/registro).

**Fuentes analizadas:**
- `docs/documentacion_sgc/mapa_navegacion_sgc_pea.html` (mapa visual SVG)
- `docs/rev_conex_sgc.md` (revisión de conexiones)
- `docs/documentacion_sgc/sesion_grill_sgc_pea_v1.md` (decisiones de arquitectura)
- `docs/documentacion_sgc/mapa_tentativo_sgc_pea.md` (vista rápida del sistema)
- `docs/documentacion_sgc/mapa_decisiones_documentales_pea.md` (decisiones documentales)

---

## 1. Estado general del mapa de navegación

El mapa HTML contiene **22 procedimientos (P)**, **3 documentos generales (DG)**, **4 instructivos (I)** y **20 formatos/registros (F)** —más 3 procedimientos retirados (OUT)— con un total de **53 aristas (edges)** que representan las relaciones documentales actuales.

La estructura visual está organizada en tres columnas conceptuales: **Procedimientos → Documentos/Instructivos → Formatos/Registros**. Sin embargo, el análisis revela que las conexiones reales no respetan completamente esta lógica de flujo.

---

## 2. Análisis por familia documental

### 2.1 Instructivos I-PSEA: Anclaje a procedimientos

| Código | Instructivo | Anclaje actual en el mapa | Estado respecto a la regla |
|---|---|---|---|
| **I-PSEA-10** | Participante en calaire-app | Entrada desde **DG-PSEA-02** (aplicativo). No tiene arista directa desde ningún P-PSEA. | **FALLA**. El instructivo depende del aplicativo, pero no está gobernado por un procedimiento. |
| **I-PSEA-16** | Administración de rondas | Entrada desde **P-PSEA-09** (planificación de ronda). | **CUMPLE**. Está anclado a P-PSEA-09. |
| **I-PSEA-17** | Preprocesador pt_app | Entrada desde **DG-PSEA-03** (aplicativo) y **P-PSEA-23** (flujo técnico). | **PARCIAL**. Tiene anclaje a P-PSEA-23, pero P-PSEA-23 es un procedimiento técnico de flujo de datos. El instructivo opera bajo el aplicativo, no bajo un procedimiento operativo de análisis. |
| **I-PSEA-18** | Análisis PT en pt_app | Entrada desde **DG-PSEA-03**, **F-PSEA-14** y **F-PSEA-13**. No tiene arista directa desde ningún P-PSEA. | **FALLA**. El instructivo de análisis está conectado a formatos (salidas del preprocesador) y al aplicativo, pero no a un procedimiento rector directo. |

**Hallazgo clave:** `I-PSEA-10` y `I-PSEA-18` son los dos casos de anclaje ausente. Según `rev_conex_sgc.md`, se recomienda:
- **P-PSEA-20 → I-PSEA-10** (comunicaciones gobiernan el instructivo del participante) o **P-PSEA-23 → I-PSEA-10**.
- **P-PSEA-06 → I-PSEA-18** (diseño estadístico gobierna el análisis PT) y/o **P-PSEA-07 → I-PSEA-18** (informe de resultados gobierna el análisis).

**Riesgo de la conexión actual:** `I-PSEA-10` cuelga de `DG-PSEA-02`. Esto crea una dependencia indirecta donde el procedimiento de comunicaciones (`P-PSEA-20`) o el procedimiento de planificación (`P-PSEA-09`) deberían ser el punto de anclaje formal, no el aplicativo en sí.

---

### 2.2 Procedimientos P-PSEA: Salidas a formatos/registros

La regla establece que cada procedimiento debe producir o gobernar al menos un formato/registro (`F-PSEA`). Se analizan los 22 procedimientos del mapa:

#### Procedimientos TÉCNICOS POR ANALITO (P-PSEA-02 a 05)

| Código | Salidas actuales en el mapa | ¿Tiene salida directa a F-PSEA? |
|---|---|---|
| P-PSEA-02 (NO/NO₂) | P-PSEA-10, P-PSEA-06, P-PSEA-07 | **NO**. Solo remite a otros procedimientos. |
| P-PSEA-03 (CO) | P-PSEA-10, P-PSEA-06, P-PSEA-07 | **NO**. Solo remite a otros procedimientos. |
| P-PSEA-04 (O₃) | P-PSEA-10, P-PSEA-06, P-PSEA-07 | **NO**. Solo remite a otros procedimientos. |
| P-PSEA-05 (SO₂) | P-PSEA-10, P-PSEA-06, P-PSEA-07 | **NO**. Solo remite a otros procedimientos. |

**Interpretación:** Los procedimientos por analito no tienen salidas directas a formatos. Esto es **conceptualmente aceptable** bajo el diseño decidido en la sesión de grill: los procedimientos por gas deben "aligerarse" y citar transversales (`P-PSEA-06`, `P-PSEA-07`, `P-PSEA-10`, `P-PSEA-23`). Sin embargo, **no producen un formato propio que registre las condiciones específicas del analito** (por ejemplo, un registro de condiciones de ensayo por gas). Si el diseño intencional es que no tengan formato propio, esto debe quedar explícito en `P-PSEA-12` (matriz documental).

#### Procedimientos MARCO Y TRANSVERSALES

| Código | Salidas actuales | ¿Tiene salida directa a F-PSEA? |
|---|---|---|
| **P-PSEA-01** | DG-PSEA-01, P-PSEA-12, P-PSEA-09, P-PSEA-06, P-PSEA-07 | **NO**. Es marco; no genera registro propio. |
| **P-PSEA-06** | F-PSEA-13, F-PSEA-13A-D, F-PSEA-14, F-PSEA-04, P-PSEA-07 | **SÍ**. Produce formatos de H/E y dataset consolidado. |
| **P-PSEA-07** | F-PSEA-04 | **SÍ**. Gobierna el informe final. |
| **P-PSEA-08** | P-PSEA-16, P-PSEA-20-28 | **NO**. No genera registro directo de colusión/falsificación. |
| **P-PSEA-09** | DG-PSEA-02, I-PSEA-16, F-PSEA-07, F-PSEA-01, F-PSEA-02, F-PSEA-06, P-PSEA-10 | **SÍ**. Gobierna formatos de planificación. |
| **P-PSEA-10** | F-PSEA-08, F-PSEA-13, P-PSEA-06 | **SÍ**. Produce dossier del item y conecta con H/E. |
| **P-PSEA-12** | P-PSEA-13 | **NO**. Debería producir matriz documental (lista de documentos). |
| **P-PSEA-13** | P-PSEA-23 | **NO**. Debería producir matriz de registros/evidencias. |
| **P-PSEA-16** | *(ninguna en el mapa)* | **NO**. Es el hallazgo más claro: debería apuntar a `F-PSEA-16` (registro de quejas/NC). |
| **P-PSEA-20** | F-PSEA-04 | **SÍ**. Gobierna comunicaciones y remite al informe. |
| **P-PSEA-21** | F-PSEA-04 | **SÍ**. Gobierna valores sensibles y remite al informe. |
| **P-PSEA-23** | DG-PSEA-02, DG-PSEA-03, I-PSEA-17, F-PSEA-09, F-PSEA-05A, F-PSEA-12, F-PSEA-10, F-PSEA-14 | **SÍ**. Gobierna múltiples formatos del flujo digital. |
| **P-PSEA-24** | *(ninguna en el mapa)* | **NO**. Debería apuntar a `F-PSEA-16` (casos SGC de quejas). |
| **P-PSEA-25** | *(ninguna en el mapa)* | **NO**. Debería apuntar a `F-PSEA-17` (registro de apelaciones). |
| **P-PSEA-26** | F-PSEA-04 | **SÍ**. Remite al informe. |
| **P-PSEA-27** | *(ninguna en el mapa)* | **NO**. Debería apuntar a `F-PSEA-21` (matriz de competencia). |
| **P-PSEA-28** | *(ninguna en el mapa)* | **NO**. Debería apuntar a `F-PSEA-23` (evaluación de proveedores). |

**Procedimientos OUT (fuera de alcance):** P-PSEA-17, P-PSEA-18, P-PSEA-19. Estos no requieren salida al no estar en el alcance PEA.

**Resumen de procedimientos SIN salida directa a F-PSEA:**
- P-PSEA-01 (marco, aceptable)
- P-PSEA-02, 03, 04, 05 (por analito, aceptable si se documenta así)
- P-PSEA-08 (colusión, **riesgo**: no deja registro de evaluación)
- P-PSEA-12 (matriz documental, **debería** producir matriz)
- P-PSEA-13 (matriz de registros, **debería** producir matriz)
- P-PSEA-16 (TNC/NC/CAPA, **CRÍTICO**: falta `F-PSEA-16`)
- P-PSEA-24 (quejas, **CRÍTICO**: falta conexión a `F-PSEA-16`)
- P-PSEA-25 (apelaciones, **CRÍTICO**: falta `F-PSEA-17`)
- P-PSEA-27 (competencia, **CRÍTICO**: falta `F-PSEA-21`)
- P-PSEA-28 (proveedores, **CRÍTICO**: falta `F-PSEA-23`)

---

### 2.3 Formatos F-PSEA: Presencia en el mapa y anclaje

| Código | ¿Presente en el mapa HTML? | Anclaje a procedimiento | Estado |
|---|---|---|---|
| F-PSEA-01 | SÍ | P-PSEA-09 | ✓ |
| F-PSEA-02 | SÍ | P-PSEA-09 | ✓ |
| F-PSEA-03 | NO | Retirado | N/A |
| F-PSEA-04 | SÍ | P-PSEA-06, P-PSEA-07, P-PSEA-20-28 | ✓ |
| F-PSEA-05 | **NO** | `rev_conex_sgc.md` sugiere P-PSEA-09 o P-PSEA-20 | **FALTA EN MAPA** |
| F-PSEA-05A | SÍ | P-PSEA-23 | ✓ |
| F-PSEA-06 | SÍ | P-PSEA-09 | ✓ |
| F-PSEA-07 | SÍ | P-PSEA-09 | ✓ |
| F-PSEA-08 | SÍ | P-PSEA-10 | ✓ |
| F-PSEA-09 | SÍ | P-PSEA-23 | ✓ |
| F-PSEA-10 | SÍ | P-PSEA-23, I-PSEA-17 | ✓ |
| F-PSEA-11 | NO | Reservado | N/A |
| F-PSEA-12 | SÍ | P-PSEA-23 | ✓ |
| F-PSEA-13 | SÍ | P-PSEA-06, P-PSEA-10 | ✓ |
| F-PSEA-13A-D | SÍ | P-PSEA-06, I-PSEA-17 | ✓ |
| F-PSEA-14 | SÍ | P-PSEA-06, I-PSEA-17 | ✓ |
| F-PSEA-16 | **NO** | Debería anclarse a P-PSEA-16, P-PSEA-24 | **FALTA EN MAPA** |
| F-PSEA-17 | **NO** | Debería anclarse a P-PSEA-25, P-PSEA-20 | **FALTA EN MAPA** |
| F-PSEA-21 | **NO** | Debería anclarse a P-PSEA-27 | **FALTA EN MAPA** |
| F-PSEA-23 | **NO** | Debería anclarse a P-PSEA-28 | **FALTA EN MAPA** |

**Formatos faltantes en el mapa visual:** `F-PSEA-05`, `F-PSEA-16`, `F-PSEA-17`, `F-PSEA-21`, `F-PSEA-23`. Esto representa **5 registros ausentes** que sí existen en el diseño tentativo y en los documentos operativos (`mapa_tentativo_sgc_pea.md`, `sesion_grill_sgc_pea_v1.md`).

**Nota importante sobre F-PSEA-05:** En el mapa tentativo y en los documentos de calaire-app (`calaire-app_reg_docs_sgc.md`, `calaire-app_func_docs_sgc.md`), `F-PSEA-05` se ha unificado con `F-PSEA-05A` como `F-PSEA-05/05A`. Sin embargo, en el mapa HTML solo aparece `F-PSEA-05A`. Esto genera inconsistencia semántica: el mapa visual pierde el registro de participación (confirmación) mientras que el diseño tentativo y el aplicativo operativo lo mantienen.

---

### 2.4 Documentos generales DG-PSEA: Anclaje a procedimientos

| Código | Anclaje actual | Estado |
|---|---|---|
| DG-PSEA-01 | P-PSEA-01 | ✓ |
| DG-PSEA-02 | P-PSEA-09, P-PSEA-23 | ✓ |
| DG-PSEA-03 | P-PSEA-23 | ✓ |

Los documentos generales cumplen con la regla de anclaje a procedimiento.

---

## 3. Flujos de datos: Análisis de rutas críticas

El mapa define 4 rutas críticas. Se analiza su coherencia:

### Ruta 1: Flujo oficial de datos (`data`)
`P-PSEA-23 > calaire-app > pt_app > informe`

Secuencia en el mapa: P-PSEA-23 → DG-PSEA-02 → I-PSEA-10 → F-PSEA-09 → F-PSEA-12 → DG-PSEA-03 → I-PSEA-17 → F-PSEA-10 → F-PSEA-14 → I-PSEA-18 → F-PSEA-04

**Problema:** `I-PSEA-18` está en la ruta, pero no está anclado directamente a un procedimiento. La ruta depende de que `F-PSEA-14` y `F-PSEA-13` actúen como "puentes" hacia el instructivo. Esto rompe la regla de anclaje.

### Ruta 2: Homogeneidad y estabilidad (`he`)
`P-PSEA-10 + P-PSEA-06 > H/E > análisis`

Secuencia: P-PSEA-10 → F-PSEA-08 → P-PSEA-06 → F-PSEA-13 → F-PSEA-13A-D → I-PSEA-18 → F-PSEA-04

**Problema:** Similar al anterior. `I-PSEA-18` aparece como nodo intermedio sin anclaje procedimental directo.

### Ruta 3: Planificación (`planning`)
`P-PSEA-09 > ficha, calendario, plan`

Secuencia: P-PSEA-09 → DG-PSEA-02 → I-PSEA-16 → F-PSEA-07 → F-PSEA-01 → F-PSEA-02 → F-PSEA-06 → P-PSEA-10

**Coherencia:** Esta ruta es consistente. `I-PSEA-16` está correctamente anclado a `P-PSEA-09`. Los formatos fluyen desde la planificación.

### Ruta 4: Orden de elaboración (`update`)
Secuencia: P-PSEA-01 → P-PSEA-12 → P-PSEA-13 → P-PSEA-23 → P-PSEA-09 → P-PSEA-10 → P-PSEA-06 → P-PSEA-07 → P-PSEA-02-05 → formatos → instructivos → DG cierre.

**Coherencia:** Es una ruta lógica de priorización, no de flujo operativo. No presenta problemas de conectividad.

---

## 4. Análisis de conectividad de procedimientos transversales específicos

### P-PSEA-08 (Colusión y falsificación)
**Salidas actuales:** P-PSEA-16, P-PSEA-20, P-PSEA-21, P-PSEA-24, P-PSEA-25, P-PSEA-26, P-PSEA-27, P-PSEA-28.

**Análisis:** Este procedimiento actúa como un **hub de gobernanza** que distribuye a otros procedimientos operativos, pero no genera un registro propio de "evaluación de colusión" o "detección de indicios". En la sesión de grill se decidió que conecta con medidas preventivas en `F-PSEA-06` (plan de ronda), pero en el mapa HTML no existe esa arista.

**Recomendación:** Añadir `P-PSEA-08 → F-PSEA-06` (medidas preventivas en plan de ronda) y considerar un formato específico de registro de indicios si la operación lo requiere.

### P-PSEA-16 (TNC/NC/CAPA)
**Salidas actuales:** Ninguna en el mapa.

**Análisis:** Según el mapa tentativo, `P-PSEA-16` debe conectar con `F-PSEA-16` (registro/caso de queja o NC). En el mapa actual, `F-PSEA-16` no existe como nodo. Esto es un **punto ciego** del sistema documental: el procedimiento de no conformidades no tiene dónde registrar las no conformidades.

**Recomendación:** Agregar nodo `F-PSEA-16` y arista `P-PSEA-16 → F-PSEA-16`.

### P-PSEA-20 a P-PSEA-28 (Gestión operativa)
**Patrón observado:** Todos remiten a `F-PSEA-04` (informe final) como salida, pero solo `P-PSEA-20`, `P-PSEA-21`, `P-PSEA-26` tienen esa arista en el mapa. Los demás (`P-PSEA-24`, `P-PSEA-25`, `P-PSEA-27`, `P-PSEA-28`) no tienen salida alguna.

**Análisis:** El diseño tentativo les asigna formatos específicos (`F-PSEA-16`, `F-PSEA-17`, `F-PSEA-21`, `F-PSEA-23`), pero el mapa HTML no los incluye. Esto crea una **desconexión entre la gestión operativa y sus evidencias**.

---

## 5. Matriz de inconsistencias y riesgos

| # | Inconsistencia | Severidad | Impacto | Corrección |
|---|---|---|---|---|
| 1 | `I-PSEA-10` no anclado a procedimiento | **Alta** | El instructivo del participante carece de gobierno procedimental. | Añadir `P-PSEA-20 → I-PSEA-10` o `P-PSEA-09 → I-PSEA-10`. |
| 2 | `I-PSEA-18` no anclado a procedimiento | **Alta** | El instructivo de análisis PT carece de gobierno procedimental. | Añadir `P-PSEA-06 → I-PSEA-18` y/o `P-PSEA-07 → I-PSEA-18`. |
| 3 | `P-PSEA-16` sin salida a `F-PSEA-16` | **Crítica** | No hay registro de NC/CAPA. | Agregar nodo `F-PSEA-16` y arista `P-PSEA-16 → F-PSEA-16`. |
| 4 | `P-PSEA-24` sin salida a `F-PSEA-16` | **Crítica** | No hay registro de quejas. | Agregar arista `P-PSEA-24 → F-PSEA-16`. |
| 5 | `P-PSEA-25` sin salida a `F-PSEA-17` | **Crítica** | No hay registro de apelaciones. | Agregar nodo `F-PSEA-17` y arista `P-PSEA-25 → F-PSEA-17`. |
| 6 | `P-PSEA-27` sin salida a `F-PSEA-21` | **Alta** | No hay registro de competencia. | Agregar nodo `F-PSEA-21` y arista `P-PSEA-27 → F-PSEA-21`. |
| 7 | `P-PSEA-28` sin salida a `F-PSEA-23` | **Alta** | No hay registro de proveedores. | Agregar nodo `F-PSEA-23` y arista `P-PSEA-28 → F-PSEA-23`. |
| 8 | `F-PSEA-05` ausente del mapa | **Media** | El registro de participación no se visualiza. | Decidir si se unifica con `F-PSEA-05A` (como en calaire-app) o se mantiene separado. |
| 9 | `P-PSEA-08` sin salida a registro de colusión | **Media** | No hay evidencia documental de detección. | Añadir `P-PSEA-08 → F-PSEA-06` (medidas en plan) o crear formato específico. |
| 10 | `P-PSEA-12` y `P-PSEA-13` sin salida a matriz | **Media** | Las matrices no generan registros visibles. | Establecer si la matriz misma es el registro (autoevidencia) o requiere formato. |
| 11 | `P-PSEA-02` a `P-PSEA-05` sin salida directa | **Baja** | Los procedimientos por gas no dejan registro propio. | Aceptable si se documenta en `P-PSEA-12` que citan transversales. |

---

## 6. Recomendaciones de corrección para el mapa

### A. Correcciones mínimas (obligatorias)

Agregar las siguientes aristas al `edges` del mapa HTML:

1. `P-PSEA-20 → I-PSEA-10` (anclar instructivo del participante)
2. `P-PSEA-06 → I-PSEA-18` (anclar instructivo de análisis PT)
3. `P-PSEA-07 → I-PSEA-18` (alternativa/refuerzo de anclaje)
4. `P-PSEA-16 → F-PSEA-16` (salida de NC/CAPA)
5. `P-PSEA-24 → F-PSEA-16` (salida de quejas)
6. `P-PSEA-25 → F-PSEA-17` (salida de apelaciones)
7. `P-PSEA-27 → F-PSEA-21` (salida de competencia)
8. `P-PSEA-28 → F-PSEA-23` (salida de proveedores)

### B. Nodos faltantes por agregar

Agregar nodos de formato al `nodes` del mapa HTML:

- `F-PSEA-05`: Registro de participación (posiblemente unificado como `F-PSEA-05/05A`)
- `F-PSEA-16`: Registro/caso de queja o NC
- `F-PSEA-17`: Registro de apelaciones
- `F-PSEA-21`: Matriz de competencia/autorización
- `F-PSEA-23`: Evaluación de proveedores críticos

### C. Ajustes de flujo

- `P-PSEA-08 → F-PSEA-06`: Conectar colusión con el plan de ronda donde se documentan medidas preventivas.
- Revisar si `P-PSEA-12` y `P-PSEA-13` deben apuntarse a sí mismos como salida (autoevidencia) o si generan un formato PDF/Excel.

### D. Consistencia con calaire-app

El aplicativo calaire-app (`calaire-app_reg_docs_sgc.md`) ya opera con `F-PSEA-05/05A` como registro calculado unificado. El mapa HTML debe reflejar esta realidad operativa: o bien eliminar `F-PSEA-05A` y mantener solo `F-PSEA-05/05A`, o bien mantener ambos separados y conectar `F-PSEA-05` a `P-PSEA-09` (planificación) y `P-PSEA-20` (comunicaciones).

---

## 7. Resumen ejecutivo

El mapa de navegación actual tiene **53 conexiones** entre 52 documentos, pero presenta **gaps estructurales** que deben cerrarse:

- **2 instructivos sin anclaje procedimental** (`I-PSEA-10`, `I-PSEA-18`)
- **4 procedimientos operativos sin salida a formato** (`P-PSEA-16`, `P-PSEA-24`, `P-PSEA-25`, `P-PSEA-27`, `P-PSEA-28`)
- **5 formatos ausentes del mapa visual** (`F-PSEA-05`, `F-PSEA-16`, `F-PSEA-17`, `F-PSEA-21`, `F-PSEA-23`)
- **1 procedimiento de gobernanza sin registro** (`P-PSEA-08`)

La arquitectura documental decidida en la sesión de grill (`sesion_grill_sgc_pea_v1.md`) y consignada en el mapa tentativo (`mapa_tentativo_sgc_pea.md`) ya identifica estos documentos y sus roles. La corrección del mapa HTML consiste principalmente en **materializar en el SVG lo que ya está diseñado en los documentos de texto**: agregar los nodos faltantes y las aristas que cierran las reglas de conectividad.

La conectividad del SGC PEA está **diseñada correctamente pero no representada completamente**. El mapa visual es un subconjunto del sistema real.
