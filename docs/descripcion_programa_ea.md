# Ensayos de Aptitud para Calidad de Aire — Descripción del Programa

**Proyecto:** CALAIRE-EA (Proyecto 61134 — INM + UNAL)  
**Fecha de corte:** 2026-04-27  
**Estado:** Prueba piloto en ejecución (Contrato 2)

---

## 1. ¿Qué es un ensayo de aptitud para calidad de aire?

Un **Ensayo de Aptitud (EA)** —también llamado *Proficiency Testing* (PT)— es un mecanismo de evaluación en el que varios laboratorios participantes miden simultáneamente un mismo ítem bajo condiciones controladas, y sus resultados individuales son comparados estadísticamente con un **valor asignado de referencia**. El proveedor del EA organiza la logística, calcula los estadísticos de desempeño y emite un informe con la calificación de cada laboratorio.

En el contexto de **calidad de aire**, el ítem PT es una concentración de gas contaminante criterio suministrada por el laboratorio de referencia (UNAL). Los participantes conectan sus analizadores ambientales a la fuente, realizan mediciones y reportan sus resultados. El proveedor calcula **puntajes z, z', ζ y En** según ISO 13528:2022 para indicar si el desempeño del laboratorio es satisfactorio (|z| < 2), cuestionable (2 ≤ |z| < 3) o insatisfactorio (|z| ≥ 3).

### Gases contaminantes criterio

| Gas | Símbolo | Principio de medición típico |
|-----|---------|------------------------------|
| Monóxido de carbono | CO | Absorción infrarroja no dispersiva (NDIR) |
| Dióxido de azufre | SO₂ | Fluorescencia ultravioleta pulsada |
| Ozono | O₃ | Absorción ultravioleta |
| Óxidos de nitrógeno | NO / NO₂ (NOₓ) | Quimioluminiscencia |

---

## 2. Marco normativo

El programa se diseña y opera bajo tres estándares internacionales complementarios:

| Norma | Título | Función en CALAIRE-EA |
|-------|--------|----------------------|
| **ISO/IEC 17043:2023** | Requisitos generales para ensayos de aptitud | Marco principal del proveedor EA: planificación, operación, ítems PT, informes, imparcialidad, confidencialidad |
| **ISO 13528:2022** | Métodos estadísticos para ensayos de aptitud | Diseño estadístico, valor asignado (Algoritmo A robusto), evaluación de desempeño (puntajes z/z'/ζ/En), homogeneidad y estabilidad |
| **ISO/IEC 17025:2017** | Requisitos generales para la competencia de laboratorios de ensayo | Base del SGC del laboratorio de referencia UNAL; aplica a control documental, registros, gestión de equipos y personal |

### Correspondencia normativa con el SGC

Los documentos del SGC de CALAIRE-EA mapean cláusulas específicas de estas normas:

- **Planificación de rondas** → ISO 17043:2023 §7.2.1
- **Diseño estadístico** → ISO 13528:2022 caps. 4–5 + ISO 17043:2023 §7.2.2
- **Valor asignado** → ISO 13528:2022 cap. 7 + ISO 17043:2023 §7.2.3
- **Homogeneidad y estabilidad** → ISO 17043:2023 §7.3.2 + ISO 13528:2022 cap. 6
- **Manejo de ítems PT** → ISO 17043:2023 §7.3.3–7.3.4 + ISO 17025:2017 §7.7
- **Instrucciones a participantes** → ISO 17043:2023 §7.3.1.3 + ISO 13528:2022 §5.5
- **Análisis de datos** → ISO 17043:2023 §7.4.1 + ISO 13528:2022 §6.2–6.6
- **Evaluación de desempeño** → ISO 13528:2022 caps. 8–9 + ISO 17043:2023 §7.4.2
- **Informes PT** → ISO 17043:2023 §7.4.3
- **Confidencialidad** → ISO 17043:2023 §4.2 + ISO 17025:2017 §4.2

---

## 3. Estructura del programa CALAIRE-EA

### 3.1 Objetivo y alcance

CALAIRE-EA establece un servicio de Ensayos de Aptitud para gases contaminantes criterio (CO, NOₓ, SO₂, O₃) orientado a laboratorios de calidad de aire en Colombia. El proyecto Proyecto 61134 cubre el **diseño y validación técnica del servicio** (sin lanzamiento operativo posterior al piloto). La inversión total es de $437 M COP.

### 3.2 Roles

| Rol | Entidad | Función |
|-----|---------|---------|
| Proveedor EA | INM / UNAL | Diseña y opera el esquema, suministra el valor asignado, emite el informe |
| Laboratorio de referencia | UNAL (instalaciones) | Genera la concentración patrón, alberga los equipos participantes |
| Participantes (P1, P2…) | Laboratorios externos (p. ej. SIATA, UPB) | Conectan sus analizadores, reportan mediciones |

### 3.3 Tipos de ronda

| Tipo | Analitos | Participantes | Descripción |
|------|----------|---------------|-------------|
| Ronda simple | CO, SO₂ | P1 (un laboratorio) | Diseño de validación con un solo participante; ronda de arranque o verificación |
| Ronda compleja F1 | O₃, NO, NO₂ | P1 + P2 | Dos participantes simultáneos, gases de alto requerimiento analítico |
| Ronda compleja F2 | CO, SO₂ | P2 | Segundo participante con gases criterio básicos |

---

## 4. Sistema de Gestión de Calidad (SGC)

El SGC sigue una **arquitectura documental de cuatro niveles** alineada a ISO/IEC 17043:2023, con segregación entre documentación operativa (ejecución de rondas) y de gestión (gobernanza del sistema).

### 4.1 Jerarquía documental

```
Nivel 1 — Manual / Documento General
    └── DG-PSEA-01  Protocolo General de Participación EA (gases criterio)

Nivel 2 — Procedimientos (P-PSEA)
    ├── Operativos:  P-01, P-04, P-09, P-10, P-20, P-22
    └── Gestión:     P-11 a P-19, P-21, P-23 a P-28

Nivel 3 — Instructivos (I-PSEA)
    └── I-02 a I-15  (14 instructivos técnicos)

Nivel 4 — Formatos y registros (F-PSEA)
    └── F-01 a F-23  (23 formatos)
```

### 4.2 Procedimientos operativos clave

| Código | Título | Norma principal | Estado |
|--------|--------|-----------------|--------|
| P-PSEA-01 | Protocolo General EA | ISO 17043:2023 §5.3–5.4 | in_review |
| P-PSEA-04 | Procedimiento EA para O₃ | ISO 17043:2023 | draft |
| P-PSEA-09 | Planificación de Ronda EA | ISO 17043:2023 §7.2.1 | draft |
| P-PSEA-10 | Manejo de Ítems PT | ISO 17043:2023 §7.3.3–7.3.4, ISO 17025:2017 §7.7 | skeleton |
| P-PSEA-20 | Comunicación PT | ISO 17043:2023 §7.1.2, §7.3.5 | skeleton |
| P-PSEA-22 | Reportes PT | ISO 17043:2023 §7.4.3 | skeleton |

### 4.3 Instructivos técnicos

| Código | Título | Norma principal |
|--------|--------|-----------------|
| I-PSEA-02 | Producción de Ítems PT | ISO 17043:2023 §7.3.1, ISO 17025:2017 §6.1.3 |
| I-PSEA-07 | Diseño Estadístico | ISO 13528:2022 caps. 4–5, ISO 17043:2023 §7.2.2 |
| I-PSEA-08 | Valor Asignado | ISO 13528:2022 cap. 7, ISO 17043:2023 §7.2.3 |
| I-PSEA-09 | Instrucciones a Participantes | ISO 17043:2023 §7.3.1.3, ISO 13528:2022 §5.5 |
| I-PSEA-10 | Homogeneidad y Estabilidad | ISO 17043:2023 §7.3.2, ISO 13528:2022 cap. 6 |
| I-PSEA-11 | Análisis de Datos | ISO 17043:2023 §7.4.1, ISO 13528:2022 §6.2–6.6 |
| I-PSEA-12 | Evaluación de Desempeño | ISO 13528:2022 caps. 8–9, ISO 17043:2023 §7.4.2 |
| I-PSEA-13 | Validación de Software y Sistemas | ISO 17043:2023 §7.5.2, ISO 13528:2022 §4.1.4 |

### 4.4 Formatos de ejecución por ronda (F-PSEA-05 a F-PSEA-14)

Estos diez formatos constituyen el **paquete documental de cada ronda** y se copian en la subcarpeta correspondiente antes de la ejecución:

| Código | Título | Momento de uso |
|--------|--------|----------------|
| F-PSEA-05 | Confirmación de Participación | Pre-ronda (T−2 semanas) |
| F-PSEA-05A | Hoja de Registro del Participante | Pre-ronda: datos personales, equipos, permisos de ingreso |
| F-PSEA-06 | Plan de Ronda EA | Pre-ronda: cronograma, roles, parámetros estadísticos |
| F-PSEA-07 | Lista Maestra de Participantes | Pre-ronda / apertura de ronda |
| F-PSEA-08 | Registro de Preparación del Ítem | Día de recepción y acondicionamiento (miércoles) |
| F-PSEA-09 | Registro de Homogeneidad | Durante los días de prueba |
| F-PSEA-10 | Registro de Estabilidad | Durante los días de prueba |
| F-PSEA-11 | Registro de Envío y Recepción | Logística de transporte de equipos |
| F-PSEA-12 | Formato de Reporte del Participante | Cierre de prueba: entrega de resultados |
| F-PSEA-13 | Hoja de Revisión de Datos | Post-ronda: control de calidad de datos recibidos |
| F-PSEA-14 | Hoja de Cálculo y Aprobación Estadística | Post-ronda: cálculo de puntajes y aprobación |

> **Nota sobre F-PSEA-06:** El Plan de Ronda EA ha sido sometido a cuatro auditorías cruzadas (completitud estructural, placeholders, coherencia interdocumental y línea base pre-corrección). Dictamen actual: operativamente utilizable, pendiente de aprobación formal por inconsistencia del parámetro σ_pt interdocumental (backlog C4-01 a C4-04).

### 4.5 Decisión estadística clave: σ_pt post-ronda

Se adoptó el enfoque **fitness-for-purpose** con la fórmula JRC-ERLAP:

```
σ_pt = a · x_pt + b
```

donde `a` y `b` son coeficientes del analito y `x_pt` es el valor asignado. Los parámetros se determinan **después de la ronda** a partir de los datos reales, en lugar de fijarlos a priori. Esta decisión queda registrada en el SGC (2026-04-10).

---

## 5. Ciclo operativo de una ronda

Cada ronda sigue un ciclo de cinco días hábiles distribuidos en una semana:

```
Miércoles   → Recepción y acondicionamiento de equipos participantes
Jueves      → Prueba GAS1 / GAS2  (primera jornada de medición)
Viernes     → Prueba GAS2 / GAS3  (segunda jornada)
Sábado      → Prueba GAS3 / GAS4  (tercera jornada, cierre de pruebas)
Lunes (+1)  → Devolución / recolección de equipos
```

Las mediciones se realizan en las instalaciones del laboratorio de referencia (UNAL). El acceso requiere **Inducción SST** (Seguridad y Salud en el Trabajo) completada por los técnicos participantes, conforme al protocolo documentado en el SGC.

---

## 6. El aplicativo CALAIRE-APP

El ecosistema de software del programa consta de dos aplicaciones complementarias integradas mediante un contrato de datos CSV (`summary_n13.csv`).

### 6.1 Motor estadístico: pt_app + ptcalc

| Atributo | Detalle |
|----------|---------|
| Tecnología | R / Shiny + paquete interno ptcalc v0.1.1 |
| Norma implementada | ISO 13528:2022 |
| Despliegue | https://w421.shinyapps.io/pt_app/ |
| Estado | Operativo |

**Cadena de cálculo validada:**

```
Datos participantes (CSV)
  → Revisión inicial (ISO 13528:2022 cap. 6)
     ├── Homogeneidad  (I-PSEA-10, F-PSEA-09)
     └── Estabilidad   (I-PSEA-10, F-PSEA-10)
  → Valor asignado — Algoritmo A robusto (ISO 13528:2022 §9.4, n ≥ 12)
  → Incertidumbres combinadas (u_hom, u_stab, u_xpt_def, U_xpt)
  → Puntajes de desempeño
     ├── z  = (x_i − x_pt) / σ_pt
     ├── z' = (x_i − x_pt) / √(σ_pt² + u_i²)
     ├── ζ  = (x_i − x_pt) / √(u_xpt² + u_i²)
     └── En = (x_i − x_ref) / √(U_i² + U_ref²)
  → F-PSEA-14 (Hoja de Cálculo y Aprobación Estadística)
```

**Correcciones técnicas aplicadas (H1–H9):**
- H1: Fórmula B.10 de ISO 13528 corregida (`max(0, ...)` en lugar de `abs()`)
- H2: MADe separado para homogeneidad (`MADe_hom`) y para σ_pt de puntajes
- H4: Umbral del Algoritmo A elevado a n ≥ 12 (ISO 13528:2022 §9.4)
- Deprecación de `sample_group`: contrato de datos simplificado a 7 columnas

**Validación:** pipeline tripartita (APP / R independiente / Python sin dependencias) sobre 15 combinaciones analito-nivel-réplica y 5 workbooks de auditoría.

### 6.2 Portal web: calaire-app

| Atributo | Detalle |
|----------|---------|
| Tecnología | Next.js 16 (App Router) + WorkOS (auth) + Supabase (PostgreSQL) |
| Autenticación | Email OTP / Magic Link (compatible con laboratorios con Azure AD bloqueado) |
| Despliegue | Vercel (pendiente) |
| Estado | Operativo en local |

**Funcionalidades:**

| Módulo | Descripción |
|--------|-------------|
| Dashboard coordinador | Creación y gestión de rondas (CRUD), transiciones de estado, contaminantes |
| Gestión de participantes | Invitación por token manual, creación de usuarios WorkOS, perfiles |
| Formulario participante | Auto-guardado (debounce 1500ms), cierre formal con `submitted_at`, modo solo lectura post-envío |
| Panel laboratorio de referencia | Interfaz diferenciada con badge violeta para el laboratorio UNAL |
| Resultados + exportación CSV | Visualización admin y exportación en formato `summary_n13.csv` para pt_app |

### 6.3 Flujo de datos integrado

```
Participante ingresa resultados
  → calaire-app (formulario web)
  → Base de datos Supabase (tabla: envios)
  → Exportación CSV por el coordinador
  → summary_n13.csv (7 columnas: lab_code, pollutant, level, run, rep, result, unit)
  → pt_app (motor estadístico ISO 13528)
  → Puntajes z / z' / ζ / En
  → F-PSEA-14 (Hoja de Cálculo y Aprobación Estadística)
  → Informe de resultados al participante
```

---

## 7. Prueba piloto 2026

### 7.1 Cronograma de rondas

| Ronda | Semana | Fechas de prueba | Estado | Observaciones |
|-------|--------|-----------------|--------|---------------|
| Ronda 1 | S1 Feb | 19–21 feb 2026 | Cancelada | Contingencias ambientales (temporada crítica SIATA/Corantioquia) |
| Ronda 2 | S2 Feb | 26–28 feb 2026 | Cancelada | Misma causa que Ronda 1 |
| Ronda 3 | S5 Mar | 19–21 mar 2026 | Planificada | — |
| Ronda 4 | S6 Mar | 26–28 mar 2026 | Planificada | — |
| Ronda 5 | S8 Abr | 9–11 abr 2026 | Planificada | UPB confirmada |
| Ronda 6 | S9 Abr | 16–18 abr 2026 | Planificada | — |
| Ronda 7 | S10 Abr | 23–25 abr 2026 | Planificada | En ejecución (semana actual) |
| Ronda 8 | S11 Abr | 30 abr–2 may 2026 | Planificada | Cierre del piloto |

> **Lección aprendida:** Los meses de febrero y marzo son temporada crítica para redes de monitoreo (SIATA, Corantioquia) por contingencias ambientales. Las futuras programaciones del servicio deben evitar este período.

### 7.2 Laboratorios participantes

| Código | Laboratorio | Gases | Estado |
|--------|-------------|-------|--------|
| P1 | SIATA | CO, SO₂ | Participación confirmada |
| P2 | Universidad Pontificia Bolivariana (UPB) | O₃, NO, NO₂ (y CO, SO₂ en F2) | Confirmada desde Ronda 5 |

### 7.3 Documentos por ronda

Cada ronda se ejecuta con el conjunto de formatos F-PSEA-05 a F-PSEA-14, almacenados en su subcarpeta:

```
docs/prueba_piloto/
  ├── ronda_simple/           ← CO/SO₂, P1
  ├── ronda_compleja_fase1/   ← O₃/NO/NO₂, P1+P2
  └── ronda_compleja_fase2/   ← CO/SO₂, P2
```

---

## 8. Estado actual y pendientes críticos

### Completado

- SGC: 23 formatos + 14 instructivos + 4 procedimientos operativos creados
- Motor estadístico pt_app: cadena completa validada (Algoritmo A → puntajes)
- Portal web calaire-app: 6 módulos operativos en local
- F-PSEA-06 (Plan de ronda simple): auditado × 4, operativamente utilizable
- Comunicaciones pre-ronda: cartas institucionales y formularios de participantes listos
- Inducción SST: flujo de acceso a instalaciones UNAL documentado

### Pendientes prioritarios

| Ítem | Descripción | Impacto |
|------|-------------|---------|
| Aprobación F-PSEA-06 | Resolver backlog C4-01 a C4-04 (σ_pt interdocumental, hito T-3) | Bloquea aprobación formal del plan de ronda |
| Deploy Vercel | calaire-app funcional en local, sin despliegue en producción | Bloquea uso remoto del portal |
| Migración SQL | `migrate_envios_pt_nuevos_campos.sql` no ejecutada | Bloquea funcionalidad de nuevos campos |
| Exportación CSV calaire-app → pt_app | Integración diseñada, implementación pendiente | Bloquea flujo automatizado de datos |
| Cifras significativas pt_app | Fases 5–6 (tests + validación cruzada) | Afecta presentación de resultados en informe |
| I-PSEA-07 skeleton | Parámetros por analito (a, b para σ_pt) por completar | Necesario para la fórmula σ_pt por gas |

---

## 9. Referencias documentales

| Documento | Ubicación |
|-----------|-----------|
| Hub documental y SGC (Logseq) | `pages/CALAIRE-EA.md`, `pages/QMS.md` |
| Ecosistema de software | `pages/CALAIRE-APP.md` |
| Árbol Maestro PSEA (SGC completo) | `docs/docs_sgc/202510 Documentacion SGC/Árbol Maestro PSEA.md` |
| Índice de formatos prueba piloto | `docs/prueba_piloto/indice_documentos.md` |
| Cronograma Gantt | `docs/auxiliares/gantt.md` |
| Línea de tiempo rondas | `docs/auxiliares/timeline.md` |
| Evolución general del proyecto | `260423_evolucion_general_proyecto.md` |
| Repositorio motor estadístico | `/home/w182/w421/pt_app` (deploy: shinyapps.io/pt_app) |
| Repositorio portal web | `/home/w182/w421/calaire-app` (deploy: Vercel, pendiente) |

---

*Documento de referencia para el programa CALAIRE-EA. Actualizar al cierre de cada ronda o hito significativo.*
