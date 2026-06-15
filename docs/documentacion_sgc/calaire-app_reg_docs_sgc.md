# Registros y Documentos del SGC — Guía Completa

**Proyecto:** calaire-app · SGC Fase 3  
**Fecha:** 2026-06-12  
**Archivos fuente:** `_workspace/sgc/checklist_sgc.md`, `_workspace/sgc/workflow_cobertura_rondas.md`, `_workspace/sgc/registros-sgc.html`

---

## Índice

1. [Introducción al SGC](#1-introducción-al-sgc)
2. [Los 9 Formatos del SGC](#2-los-9-formatos-del-sgc)
3. [Clasificación por Modo de Cumplimiento](#3-clasificación-por-modo-de-cumplimiento)
4. [El Checklist y su Funcionamiento](#4-el-checklist-y-su-funcionamiento)
5. [Vistas del Aplicativo](#5-vistas-del-aplicativo)
6. [Flujo de Trabajo por Fase](#6-flujo-de-trabajo-por-fase)
7. [Estados de los Ítems del Checklist](#7-estados-de-los-ítems-del-checklist)
8. [Justificaciones y Excepciones](#8-justificaciones-y-excepciones)
9. [Matriz Documental Maestra](#9-matriz-documental-maestra)
10. [Tablas de Referencia Rápida](#10-tablas-de-referencia-rápida)
11. [Historial de Transición de Formatos SGC](#11-historial-de-transición-de-formatos-sgc)

---

## 1. Introducción al SGC

El **Sistema de Gestión de Calidad (SGC)** de calaire-app es el módulo responsable de garantizar que todas las rondas de Ensayos de Aptitud (EA) cumplan con los requisitos documentales establecidos por la norma ISO 17043 y las políticas internas del laboratorio CALAIRE.

El SGC opera sobre un concepto central: **cada ronda debe dejar un conjunto de 9 registros/documentos obligatorios** que evidencian la correcta planificación, ejecución, evaluación y cierre del programa de EA. Estos documentos se organizan en **5 fases del ciclo de vida** de una ronda.

### 1.1 Las 5 Fases del Ciclo SGC

| Fase | Descripción |
|---|---|
| **Planeación** | Calendarios, cronogramas, planificación estructurada y planes operativos logísticos |
| **Convocatoria** | Confirmación y aceptación de participación mediante fichas electrónicas |
| **Ejecución** | Carga de niveles y calibrador dinámico, y recepción de resultados del participante |
| **Evaluación** | Procesamiento y análisis estadístico en pt_app |
| **Cierre** | Generación y publicación del informe final de resultados en pt_app |

### 1.2 Objetivo de Este Documento

Este documento explica:
- **Qué es** cada uno de los 9 formatos/documentos del SGC
- **Para qué sirve** dentro del sistema de gestión de calidad
- **Cómo se genera/completa** en el aplicativo (UI, cálculo automático, carga de archivos o procesamiento en pt_app)
- **Dónde se visualiza** en el aplicativo
- **Cuál es el flujo de trabajo** asociado a cada uno

---

## 2. Los 9 Formatos del SGC

Cada formato tiene un código único, una fase asignada, y un "modo" que determina cómo se genera o verifica su cumplimiento. Todos son **críticos** para el cierre de la ronda.

| Código | Nombre | Fase | Modo |
|---|---|---|---|
| `F-PSEA-01` | Calendario de rondas | Planeación | Nativo (UI) |
| `F-PSEA-02` | Cronograma detallado de la ronda | Planeación | Nativo (UI) |
| `F-PSEA-05/05A` | Ficha del participante | Convocatoria | Nativo Calculado |
| `F-PSEA-06` | Planificación de la ronda | Planeación | Nativo (UI) |
| `F-PSEA-08` | Asignación de niveles / Calibrador dinámico | Ejecución | Archivo (Carga) |
| `F-PSEA-09` | Recepción de datos/resultados del participante | Ejecución | Nativo Calculado |
| `F-PSEA-10/13` | pt_app — Procesamiento estadístico | Evaluación | Externo (pt_app) |
| `F-PSEA-11` | Plan operativo de ronda | Planeación | Nativo (UI) |
| `F-PSEA-14` | Informe de resultados | Cierre | Externo (pt_app) |

---

## 3. Clasificación por Modo de Cumplimiento

Los formatos se clasifican en **4 modos** según la mecánica por la cual el sistema determina su completitud. Esta distinción es fundamental porque determina qué acción debe tomar el coordinador.

### 3.1 Nativo (UI) — Generados Directamente en el Aplicativo

Estos formatos se crean y guardan a través de **formularios dentro de la aplicación**. El sistema verifica que la información esté configurada y que se haya guardado el estado correspondiente.

| Código | Formato | Qué genera el coordinador |
|---|---|---|
| `F-PSEA-01` | Calendario de rondas | Configura la programación de las rondas en la vista Gantt/Calendario |
| `F-PSEA-02` | Cronograma detallado de la ronda | Define los hitos principales con fechas en la tabla de cronograma |
| `F-PSEA-06` | Planificación de la ronda | Completa el plan de bloques (a–u) y lo marca como finalizado |
| `F-PSEA-11` | Plan operativo de ronda | Registra la operativa logística y los detalles de ejecución |

**Comportamiento del sistema:**
- Se marca como **completo** cuando el registro correspondiente está configurado y guardado en la base de datos (con snapshot para F-PSEA-06 y F-PSEA-11).
- Se marca como **pendiente** si falta configurar o finalizar el flujo.

### 3.2 Nativo Calculado — Calculados Automáticamente por el Sistema

El sistema **calcula en tiempo real** la completitud basándose en datos operativos de la ronda. No requieren acción directa del coordinador más allá de gestionar los datos operativos subyacentes, y admiten justificación.

| Código | Formato | Qué verifica el sistema |
|---|---|---|
| `F-PSEA-05/05A` | Ficha del participante | Que todos los participantes esperados hayan diligenciado su ficha (aceptación + instrumentos/personas) |
| `F-PSEA-09` | Recepción de datos/resultados | Que se hayan recibido el 100% de los resultados/datos esperados de los participantes |

### 3.3 Archivo (Carga) — Cargas al Servidor de Almacenamiento

El coordinador debe **subir archivos** al storage del aplicativo como evidencia documental. El sistema verifica que existan las versiones vigentes.

| Código | Formato | Evidencia requerida |
|---|---|---|
| `F-PSEA-08` | Asignación de niveles / Calibrador dinámico | Archivo de información del calibrador dinámico (cargar) y archivo de datos asociados (cargar) |

**Comportamiento del sistema:**
- Se marca como **completo** cuando existen los archivos cargados vigentes en el storage (`_storage`).
- Se marca como **pendiente** si falta cargar alguno de los archivos.

### 3.4 Externo (pt_app) — Procesamiento en pt_app

Los registros provienen de **pt_app**, el aplicativo externo especializado de análisis y procesamiento estadístico. calaire-app referencia o consume los resultados generados por este.

| Código | Formato | Qué verifica el sistema |
|---|---|---|
| `F-PSEA-10/13` | pt_app — Procesamiento estadístico | Que el procesamiento y la revisión de datos estén completados en pt_app |
| `F-PSEA-14` | Informe de resultados | Que el informe final de resultados haya sido generado y publicado por pt_app |

---

## 4. El Checklist y su Funcionamiento

### 4.1 Qué es el Checklist

El **checklist** es la estructura de datos central del SGC. Por cada ronda, el sistema genera un array de 9 `SgcChecklistItem` — uno por cada formato — con toda la información de estado, responsable, observaciones y vínculos.

### 4.2 Estructura de un SgcChecklistItem

```typescript
{
  codigo: SgcFormatoCodigo,       // "F-PSEA-01", "F-PSEA-05/05A", etc.
  nombre: string,                 // Nombre legible del formato
  fase: SgcFase,                  // planeacion | convocatoria | ejecucion | evaluacion | cierre
  modo: string,                   // nativo | nativo_calculado | archivo | no_aplica_inicial
  critico: boolean,              // Siempre true para los 9 formatos
  estado: SgcItemEstado,          // completo | pendiente | no_aplica | advertencia
  responsable: string,            // Nombre de quien actualizó o "Coordinacion SGC"
  ultimaActualizacion: string | null,  // ISO timestamp
  vinculo: string | null,        // Texto contextual (ej. "3/5 participantes")
  observaciones: string,          // Mensaje explicativo del estado actual
  bloqueante: boolean,            // true si critico=true AND estado=pendiente
}
```

### 4.3 Lógica de Cálculo del Checklist (`calcularChecklistSgc`)

La función `calcularChecklistSgc` en `lib/sgc/checklist.ts` (líneas 60–163) recibe un `SgcCoverageInput` con todos los datos operativos de la ronda y devuelve el array de 9 ítems con su estado calculado.

**Ejemplos de lógica por formato:**

| Código | Condición de completo |
|---|---|
| `F-PSEA-01` | Programado con fechas en calendario/Gantt |
| `F-PSEA-02` | Hitos definidos con fechas en cronograma |
| `F-PSEA-05/05A` | `fichasEnviadas >= participantesEsperados` (o `justificacionVigente`) |
| `F-PSEA-06` | `planFinalizado == true` Y `snapshotsPlan > 0` |
| `F-PSEA-08` | `evidenciasVigentes['F-PSEA-08'] == true` (info calibrador + datos) |
| `F-PSEA-09` | `enviosRecibidos >= enviosEsperados` (o `justificacionVigente`) |
| `F-PSEA-10/13` | `ptAppProcesado && resultadosDisponibles` (en pt_app) |
| `F-PSEA-11` | `planOperativoFinalizado == true` Y `snapshots > 0` |
| `F-PSEA-14` | `informeGenerado && publicado` (en pt_app) |

### 4.4 Bloqueantes

Un ítem se considera **bloqueante** cuando es crítico (`critico: true`) Y su estado es `pendiente`. Los bloqueantes se derivan del checklist mediante la función `derivarBloqueantes()`:

```typescript
// lib/sgc/checklist.ts:L44-48
export function derivarBloqueantes(items: SgcChecklistItem[]) {
  return items
    .filter((item) => item.bloqueante)
    .map((item) => `${item.codigo}: ${item.observaciones}`)
}
```

Estos bloqueantes aparecen:
1. En las **tarjetas de resumen de ronda** en `/dashboard/sgc` (sección inferior de cada card)
2. En el **Tablero de Cobertura por Ronda** como celdas rojas (🔴)
3. En el conteo del dashboard (`bloqueantesTotal`)

### 4.5 Progreso de la Ronda

El **progreso** de una ronda se calcula como el porcentaje de los 9 formatos que están en estado `completo` o `no_aplica`:

```
progreso = (count(estado == 'completo' | estado == 'no_aplica') / 9) * 100
```

Este valor aparece:
- En la barra de progreso de cada tarjeta de ronda en `/dashboard/sgc`
- Como **"Avance SGC"** (promedio de todas las rondas) en el resumen del dashboard
- En el **Tablero de Cobertura por Ronda** (columna derecha "%")

---

## 5. Vistas del Aplicativo

El aplicativo presenta el SGC en **dos vistas principales** accesibles desde `/dashboard/sgc`:

### 5.1 Vista: "Cobertura por Ronda" (Tablero Cruzado)

Esta es la **vista por defecto** al entrar a `/dashboard/sgc`. Muestra una tabla cruzada donde:

- **Filas** = Rondas registradas
- **Columnas** = Los 9 formatos, agrupados por las 5 fases
- **Celdas** = Dots semáforo indicando el estado de cada formato por ronda

```
┌──────────────┬────── Planeación ──────┬─ Convoc. ─┬── Ejecución ──┬─ Evaluación ─┬─ Cierre ─┬──────────┐
│ Ronda        │ F-01 │ F-02 │ F-06 │ F-11 │  F-5/A  │ F-08 │  F-09  │   F-10/13   │   F-14   │ Cobertura│
├──────────────┼──────┼──────┼──────┼──────┼─────────┼──────┼────────┼─────────────┼──────────┼──────────┤
│ R-2024-01    │  🟢  │  🟢  │  🟢  │  🟢  │   🟢    │  🟢  │   🟢   │     🟢      │    🟢    │ 100% ███ │
```

**Funcionalidades del tablero:**
- **Búsqueda** por código o nombre de ronda
- **Toggle** "Ocultar rondas cerradas"
- **Tooltip** al pasar el mouse sobre un dot (muestra nombre + observaciones)
- **Navegación** al hacer clic en un dot: lleva al panel SGC de esa ronda (`/dashboard/rondas/[id]/sgc`)
- **Columnas sticky** (izquierda: ronda; derecha: % de cobertura) durante scroll horizontal

### 5.2 Vista: "Documentos" (Matriz Documental Maestra)

La segunda pestaña muestra la **Matriz Documental Maestra**, que es un registro maestro de **todos los documentos** del SGC (no solo los 9 de la ronda). Aquí se gestionan:

- Documentos por proceso (Planeación, Convocatoria, Ejecución, etc.)
- Tipos: formato, procedimiento, instructivo, plantilla, registro, otro
- Estados: borrador, vigente, obsoleto, en_revision
- Versiones vigentes e historial de cambios
- Carga de archivos fuente

### 5.3 Panel SGC por Ronda

Además de la vista global, cada ronda tiene su propio panel en `/dashboard/rondas/[id]/sgc` donde el coordinador puede:

- Configurar el **Calendario de rondas** (`F-PSEA-01`)
- Configurar el **Cronograma detallado** (`F-PSEA-02`)
- Ver y editar la **Planificación de la ronda** (`F-PSEA-06`)
- Ver y editar el **Plan operativo** (`F-PSEA-11`)
- Cargar **evidencias** de calibrador dinámico y datos (`F-PSEA-08`)
- Gestionar **hitos** de la ronda
- Registrar **justificaciones** para formatos calculados
- Gestionar **comunicaciones, publicaciones, comentarios y notificaciones**
- Ver **resultados estadísticos** (homogeneidad, estabilidad)
- Gestionar **casos** (consultas, desviaciones, quejas, apelaciones)

---

## 6. Flujo de Trabajo por Fase

### 6.1 Fase: Planeación

**Formatos:** `F-PSEA-01` (Calendario de rondas), `F-PSEA-02` (Cronograma detallado), `F-PSEA-06` (Planificación de la ronda), `F-PSEA-11` (Plan operativo)

**Flujo:**
1. **Calendario de rondas (`F-PSEA-01`):** El coordinador registra la programación anual de las rondas en la vista calendario/Gantt de calaire-app.
2. **Cronograma detallado (`F-PSEA-02`):** Se definen las fechas de los hitos clave para la ronda en la tabla de cronograma.
3. **Planificación de la ronda (`F-PSEA-06`):** El coordinador redacta el plan interactivo de bloques (a–u) y lo finaliza. Se guarda un snapshot histórico.
4. **Plan operativo de ronda (`F-PSEA-11`):** Se configura la operativa logística de distribución y códigos de participante, guardando el snapshot correspondiente.

**Resultado en checklist:**
- `F-PSEA-01`: 🟢 completo si está programado con fechas en calendario.
- `F-PSEA-02`: 🟢 completo si los hitos tienen fechas asignadas.
- `F-PSEA-06`: 🟢 completo cuando planFinalizado === true + snapshotsPlan > 0.
- `F-PSEA-11`: 🟢 completo cuando planOperativoFinalizado === true + snapshotsPlanOperativo > 0.

### 6.2 Fase: Convocatoria

**Formatos:** `F-PSEA-05/05A` (Ficha del participante)

**Flujo:**
1. Los participantes se inscriben y completan su **ficha del participante**.
2. El diligenciamiento y envío de la ficha es la confirmación formal y prueba de aceptación de las condiciones.
3. Registra de forma automatizada las **personas** responsables y los **instrumentos/métodos** a emplear.

**Resultado en checklist:**
- `F-PSEA-05/05A`: 🟢 si el 100% de los participantes esperados enviaron sus fichas, o si existe una justificación escrita vigente.

### 6.3 Fase: Ejecución

**Formatos:** `F-PSEA-08` (Asignación de niveles / Calibrador dinámico), `F-PSEA-09` (Recepción de datos/resultados del participante)

**Flujo:**
1. **Asignación de niveles (`F-PSEA-08`):** Se configuran los niveles de la ronda y se suben al storage la información del calibrador dinámico y los datos en los campos de carga física de calaire-app.
2. **Recepción de resultados (`F-PSEA-09`):** Los participantes envían sus resultados metrológicos. El aplicativo calcula automáticamente la cobertura de recepción en tiempo real.

**Resultado en checklist:**
- `F-PSEA-08`: 🟢 completo si los archivos vigentes de información del calibrador dinámico y datos asociados están cargados.
- `F-PSEA-09`: 🟢 completo si el 100% de los resultados esperados han sido recibidos en calaire-app, o si existe una justificación vigente.

### 6.4 Fase: Evaluación

**Formatos:** `F-PSEA-10/13` (pt_app — Procesamiento estadístico de aptitud)

**Flujo:**
1. **pt_app** realiza el procesamiento y análisis estadístico especializado (cálculo de z-scores, incertidumbres y desempeño) y la revisión de datos.
2. calaire-app verifica de forma integrada que los resultados estén procesados y disponibles para consulta.

**Resultado en checklist:**
- `F-PSEA-10/13`: 🟢 completo si el procesamiento y revisión de datos en pt_app se reporta como finalizado.

### 6.5 Fase: Cierre

**Formatos:** `F-PSEA-14` (Informe de resultados)

**Flujo:**
1. pt_app genera el Informe de Resultados metrológico consolidado y las evaluaciones individuales.
2. El informe final de resultados es publicado en pt_app y se comunica formalmente el cierre documental a los participantes.

**Resultado en checklist:**
- `F-PSEA-14`: 🟢 completo si el informe de resultados ha sido generado y publicado por pt_app.

---

## 8. Justificaciones y Excepciones

Algunos formatos calculados (`F-PSEA-05/05A`, `F-PSEA-09`) permiten una **justificación** cuando una condición no se cumple pero existe una razón válida documentada.

### 8.1 Cuándo se puede justificar

| Formato | Condición que se justificaría |
|---|---|
| `F-PSEA-05/05A` | Participantes esperados no completaron sus fichas (ej. retiro de última hora) |
| `F-PSEA-09` | Recepción de datos/resultados incompleta por causas de fuerza mayor |

### 8.2 Cómo funciona

1. El coordinador va al panel SGC de la ronda
2. Encuentra el formato en estado 🔴 (pendiente)
3. Acciona "Agregar justificación"
4. Ingresa el **alcance** (a qué aplica) y la **razón** (por qué no se cumplió)
5. El sistema marca el formato como **completo** con la observación de la justificación
6. La justificación queda registrada en el **audit log** del SGC

### 8.3 Justificaciones vs. No Aplica

En el nuevo esquema de 9 formatos, no hay un formato configurado como "No Aplica Inicial" por defecto. El estado `no_aplica` (⚪) queda reservado para justificaciones de casos de fuerza mayor u omisiones documentadas genéricamente por la coordinación.

---

## 9. Matriz Documental Maestra

La **Matriz Documental Maestra** es el registro maestro de todos los documentos del SGC, no limitado a los 9 formatos de la ronda. Es accesible desde la pestaña "Documentos" en `/dashboard/sgc`.

### 9.1 Estructura de la Matriz

```typescript
type MatrizDocumentalSgc = {
  documentos: DocumentoSgc[]      // Todos los documentos registrados
  versiones: Array<{
    documentoId: string
    vigente: DocumentoSgcVersion | null   // Versión actualmente vigente
    historial: DocumentoSgcVersion[]      // Historial de versiones
  }>
  procesos: string[]               // Lista de procesos únicos
  resumen: {
    total: number
    vigentes: number
    enRevision: number
    obsoletos: number
  }
}
```

### 9.2 Tipos de Documento

| Tipo | Descripción |
|---|---|
| `formato` | Formato de registro normalizado (ej. los 9 del checklist) |
| `procedimiento` | Procedimiento operativo estándar |
| `instructivo` | Instructivo de uso o carga |
| `plantilla` | Plantilla vacía para llenado |
| `registro` | Registro de evidencia |
| `otro` | Otros documentos |

### 9.3 Estados de un Documento

| Estado | Significado |
|---|---|
| `borrador` | Documento en preparación, no usable aún |
| `vigente` | Documento aprobado y en uso |
| `en_revision` | Documento siendo actualizado |
| `obsoleto` | Documento reemplazado o fuera de uso |

### 9.4 Componentes de la Matriz Interactiva

El componente `MatrizInteractiva` (`app/(protected)/dashboard/sgc/MatrizInteractiva.tsx`) permite:

- **Filtrar** por proceso, tipo, estado
- **Buscar** por código o nombre
- **Ver versiones** vigentes e historial
- **Subir nuevas versiones** de documentos
- **Gestionar metadatos** (propietario, criticidad, retención)

---

## 10. Tablas de Referencia Rápida

### 10.1 Mapeo Fase → Formatos

| Fase | Formatos |
|---|---|
| Planeación | `F-PSEA-01`, `F-PSEA-02`, `F-PSEA-06`, `F-PSEA-11` |
| Convocatoria | `F-PSEA-05/05A` |
| Ejecución | `F-PSEA-08`, `F-PSEA-09` |
| Evaluación | `F-PSEA-10/13` |
| Cierre | `F-PSEA-14` |

### 10.2 Mapeo Formato → Modo → Backend

| Formato | Modo | Backend (Convex) |
|---|---|---|
| `F-PSEA-01` | nativo | `calcularChecklistSgc` (fechas programadas) |
| `F-PSEA-02` | nativo | `calcularChecklistSgc` (hitos definidos) |
| `F-PSEA-05/05A` | nativo_calculado | `calcularChecklistSgc` (fichasEnviadas) |
| `F-PSEA-06` | nativo | `calcularChecklistSgc` (snapshotsPlan > 0) |
| `F-PSEA-08` | archivo | `calcularChecklistSgc` (evidenciasVigentes) |
| `F-PSEA-09` | nativo_calculado | `calcularChecklistSgc` (enviosRecibidos) |
| `F-PSEA-10/13` | externo_ptapp | `calcularChecklistSgc` (ptAppProcesado) |
| `F-PSEA-11` | nativo | `calcularChecklistSgc` (snapshotsPlanOperativo > 0) |
| `F-PSEA-14` | externo_ptapp | `calcularChecklistSgc` (informeGenerado + publicado) |

### 10.3 Archivos Clave del SGC

| Archivo | Propósito |
|---|---|
| `lib/sgc/catalog.ts` | Definición de los 9 formatos, fases, modos y bloques del plan |
| `lib/sgc/checklist.ts` | Lógica de cálculo del checklist y derivación de bloqueantes |
| `lib/sgc/index.ts` | API pública del SGC (funciones para frontend) |
| `convex/sgc/*.ts` | Backend Convex (queries, mutations, tablas) |
| `app/(protected)/dashboard/sgc/page.tsx` | Página principal del dashboard SGC |
| `app/(protected)/dashboard/sgc/SgcResumenClient.tsx` | Componente client con tarjetas + tabs |
| `app/(protected)/dashboard/sgc/TableroCoberturaRondas.tsx` | Tabla cruzada de cobertura |
| `app/(protected)/dashboard/sgc/MatrizInteractiva.tsx` | Matriz documental maestra |

---

## 11. Historial de Transición de Formatos SGC (De 12 a 9 Formatos)

La siguiente tabla resume cómo se migraron y adaptaron los formatos de calidad desde el antiguo esquema de 12 documentos al nuevo flujo operativo unificado de 9 formatos en calaire-app:

| Formato Original | Nuevo Código / Estado | Modo de Cumplimiento | Resumen del Cambio y Funcionamiento |
|---|---|---|---|
| **F-PSEA-01** | `F-PSEA-01` | Nativo (UI) | Calendario global de rondas (tipo calendario/Gantt en la UI). |
| **F-PSEA-02** | `F-PSEA-02` | Nativo (UI) | Cronograma detallado de la ronda (tipo tabla de hitos en la UI). |
| **F-PSEA-03** | `F-PSEA-06` | Nativo (UI) | La Planificación de la ronda (interfaz nativa por bloques) pasa de su antiguo código F-PSEA-03 (o F-PPSEA-03) al nuevo **F-PSEA-06**. |
| **F-PSEA-05** y **F-PSEA-05A** | `F-PSEA-05/05A` | Nativo Calculado | Se integran en un único registro calculado. Su diligenciamiento es la prueba de aceptación y confirmación de participación, registrando de forma unificada personas e instrumentos/métodos. |
| **F-PSEA-06** (old) | `F-PSEA-11` | Nativo (UI) | El Plan operativo de la ronda (antes F-PSEA-06) pasa a usar el código **F-PSEA-11**, que anteriormente estaba sin uso. |
| **F-PSEA-07** | **Eliminado** | Integración | Se elimina como formato independiente y sus requisitos (asignación de códigos únicos anonimizados y control de provisionales) se integran dentro del Plan operativo (**F-PSEA-11**). |
| **F-PSEA-08** | `F-PSEA-08` | Archivo (Carga) | Asignación de niveles. Requiere cargar dos evidencias físicas en los campos específicos de la UI: la información del calibrador dinámico y los archivos de datos asociados. |
| **F-PSEA-09** | `F-PSEA-09` | Nativo Calculado | Se completa automáticamente en el momento en que el aplicativo recibe formalmente los datos y resultados ingresados por el participante. |
| **F-PSEA-10** y **F-PSEA-13** | `F-PSEA-10/13` | Externo (pt_app) | El procesamiento estadístico (antes F-PSEA-10) y la revisión sistemática de datos (antes F-PSEA-13) se unifican bajo el procesamiento del aplicativo externo **pt_app**. |
| **F-PSEA-11** (old) | **Eliminado** | Reasignado | Se elimina el "Registro no aplicable inicial" que ocupaba esta posición para liberar el código F-PSEA-11 para el Plan operativo de la ronda. |
| **F-PSEA-12** | **Eliminado** | No se necesita | Se elimina por completo del ciclo operativo al no ser necesario para el flujo documental. |
| **F-PSEA-14** | `F-PSEA-14` | Externo (pt_app) | Informe final de resultados consolidado generado por el aplicativo externo **pt_app**. |

---

*Documento generado con base en `checklist_sgc.md` y `workflow_cobertura_rondas.md` — calaire-app SGC Fase 3*