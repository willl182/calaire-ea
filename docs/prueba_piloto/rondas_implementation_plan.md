# Reorganización de documentación Prueba Piloto PSEA

## Contexto

El directorio `docs/prueba_piloto/` contiene 52 placeholders con trazabilidad normativa y 9 archivos preexistentes. Se necesita:
1. Separar documentos **operativos** (necesarios para ejecutar técnicamente la prueba) de los de **gestión** (gobernanza/SGC)
2. Crear carpetas por ronda con copias de los formatos requeridos
3. Planificar el contenido de cada formato por ronda

## Estructura de las rondas (según `calendario_ppiloto.md`)

> La Ronda Compleja inicia con la medición de O₃, NO-NO₂ y **finaliza con la medición simultánea de CO-SO₂ con un solo participante** (P2 = UPB).

| | **Ronda Simple** | **Ronda Compleja — Fase 1** | **Ronda Compleja — Fase 2** |
|---|---|---|---|
| **Analitos** | CO, SO₂ | O₃, NO, NO₂ | CO, SO₂ |
| **Participantes** | 1 (P1 = SIATA) | 2 (P1 = SIATA, P2 = UPB) | 1 (P2 = UPB) |
| **Semana** | Semana 1 (abril 20–25) | Semana 2 (abril 27–mayo 2) | Semana 2 (cierre) |
| **Duración medición** | 1 jornada | 2–3 jornadas | 1 jornada |
| **Tipo** | Simple | Multi-analito, multi-participante | Simple (dentro de ronda compleja) |

## Cambios propuestos

### 1. Crear subcarpeta `gestion/` y mover documentos de gestión

**Documentos a mover a `prueba_piloto/gestion/`** — procedimientos de gobernanza Nivel 2 que NO son necesarios para la ejecución técnica de la prueba piloto:

| Código | Título | Justificación de clasificación |
|---|---|---|
| P-PSEA-11 | Reporte de Resultados (17025) | Complementario, no bloquea la ronda |
| P-PSEA-12 | Control Documental del PEA | Gobernanza pura |
| P-PSEA-13 | Control de Registros del PEA | Gobernanza pura |
| P-PSEA-14 | Gestión de Riesgos | Gobernanza pura |
| P-PSEA-15 | Mejora Continua | Gobernanza pura |
| P-PSEA-16 | No Conformidades/CAPA | Gobernanza, aunque se usa para cierre |
| P-PSEA-17 | Auditorías Internas | Gobernanza pura |
| P-PSEA-18 | Revisión por Dirección | Gobernanza pura |
| P-PSEA-19 | Monitoreo de Imparcialidad | Gobernanza pura |
| P-PSEA-21 | Divulgación de Valores | Complementario |
| P-PSEA-23 | Gestión de Datos | Complementario, robustecimiento |
| P-PSEA-24 | Quejas del PEA | Gobernanza, cierre documental |
| P-PSEA-25 | Apelaciones del PEA | Gobernanza, cierre documental |
| P-PSEA-26 | Confidencialidad | Gobernanza, robustecimiento |
| P-PSEA-27 | Competencia y Autorización | Gobernanza, robustecimiento |
| P-PSEA-28 | Proveedores Externos | Gobernanza, robustecimiento |

> **16 documentos** de gestión → `prueba_piloto/gestion/`

### 2. Documentos operativos que permanecen en `prueba_piloto/`

**Procedimientos técnicos:**

| Código | Título | Rol operativo |
|---|---|---|
| P-PSEA-10 | Manejo de Items PT | Manejo de cilindros/atmósferas |
| P-PSEA-20 | Comunicación PT | Comunicación con participantes, acuerdos |
| P-PSEA-22 | Reportes PT | Informe de resultados del piloto |

**Instructivos técnicos (todos operativos):**

| Código | Título | Rol operativo |
|---|---|---|
| I-PSEA-02 | Producción PT Items | Producción de atmósferas |
| I-PSEA-03 | Control Ambiental | Condiciones de generación |
| I-PSEA-04 | Validación de Métodos | Validación de métodos de ensayo |
| I-PSEA-05 | Estimación de Incertidumbre | Incertidumbre de mediciones |
| I-PSEA-06 | Control de Calidad de Datos | QC de datos |
| I-PSEA-07 | Diseño Estadístico | Diseño ISO 13528 |
| I-PSEA-08 | Valor Asignado | Cálculo de x_pt y u(x_pt) |
| I-PSEA-09 | Instrucciones a Participantes | Instrucciones pre-ronda |
| I-PSEA-10 | Homogeneidad y Estabilidad | Verificación del ítem PT |
| I-PSEA-11 | Análisis de Datos | Revisión y outliers |
| I-PSEA-12 | Evaluación de Desempeño | Scoring (z, z', ζ) |
| I-PSEA-13 | Validación de Software | Validación R/Shiny |
| I-PSEA-14 | Visualización de Datos | Gráficos del informe |
| I-PSEA-15 | Caracterización | Caracterización de ítems PT |

**Formatos operativos (todos operativos):**

| Código | Título | Rol operativo |
|---|---|---|
| F-PSEA-05 | Confirmación Participación | Acuerdo del participante |
| F-PSEA-06 | Plan de Ronda EA | Plan aprobado de la ronda |
| F-PSEA-07 | Lista Participantes | Registro maestro codificado |
| F-PSEA-08 | Registro Preparación | Trazabilidad preparación ítem |
| F-PSEA-09 | Registro Homogeneidad | Evidencia homogeneidad |
| F-PSEA-10 | Registro Estabilidad | Evidencia estabilidad |
| F-PSEA-11 | Registro Envío y Recepción | Trazabilidad logística |
| F-PSEA-12 | Reporte del Participante | Captura resultados |
| F-PSEA-13 | Hoja Revisión de Datos | Revisión pre-análisis |
| F-PSEA-14 | Hoja Cálculo Estadística | Cálculos y aprobación |
| F-PSEA-15 | Registro NC/CAPA | Desviaciones en la ronda |
| F-PSEA-16 | Registro Quejas | Por si se producen |
| F-PSEA-17 | Registro Apelaciones | Por si se producen |
| F-PSEA-18 | Acta Revisión Dirección | Cierre formal del piloto |
| F-PSEA-19 | Lista Verificación Auditoría | Auditoría del piloto |
| F-PSEA-20 | Protocolo Validación Software | Validación R/Shiny |
| F-PSEA-21 | Matriz Competencia | Registro de personal |
| F-PSEA-22 | Matriz Riesgos Imparcialidad | Riesgos del piloto |
| F-PSEA-23 | Evaluación Proveedores | Si intervienen CRM externos |

> **36 documentos** operativos permanecen en `prueba_piloto/`

### 3. Crear carpetas por ronda con formatos requeridos

Se crearán tres subcarpetas:
- `prueba_piloto/ronda_simple/` — CO, SO₂ con P1 (SIATA)
- `prueba_piloto/ronda_compleja_fase1/` — O₃, NO, NO₂ con P1 (SIATA) + P2 (UPB)
- `prueba_piloto/ronda_compleja_fase2/` — CO, SO₂ con P2 (UPB)

Cada una contendrá **copias de trabajo** de los 10 formatos de ejecución (F-PSEA-05 a F-PSEA-14), adaptados con la planificación de contenido para sus analitos y participantes.

#### Formatos requeridos por ronda/fase

| Formato | Ronda Simple (P1, CO/SO₂) | R. Compleja F1 (P1+P2, O₃/NO/NO₂) | R. Compleja F2 (P2, CO/SO₂) |
|---|---|---|---|
| **F-PSEA-05** Confirmación Participación | P1 (SIATA). Analitos: CO, SO₂. 2 equipos | P1 (SIATA) + P2 (UPB). Analitos: O₃, NO, NO₂. 6 equipos | P2 (UPB). Analitos: CO, SO₂. 2 equipos |
| **F-PSEA-06** Plan de Ronda | 1 participante, 2 analitos, semana 1. Niveles CO/SO₂ según P-PSEA-03/05. CRM. Responsables | 2 participantes, 3 analitos, semana 2. Niveles O₃/NO/NO₂ según P-PSEA-02/04. Medición en paralelo | 1 participante, 2 analitos (cierre semana 2). Reutiliza CRM de ronda simple. Responsables |
| **F-PSEA-07** Lista Participantes | P1: SIATA — código, contacto, confirmación | P1: SIATA + P2: UPB — códigos, contactos, estados | P2: UPB — código, contacto, confirmación |
| **F-PSEA-08** Registro Preparación | Sistema generador CO/SO₂: setpoints, mezclas, condiciones | Sistema generador O₃/NO/NO₂: setpoints, mezclas. 3 analitos = más registros | Sistema generador CO/SO₂: setpoints (pueden diferir de ronda simple). Condiciones |
| **F-PSEA-09** Registro Homogeneidad | Homogeneidad CO/SO₂. ≥10 atmósferas, ≥2 réplicas. s_hom ≤ 0,3×σ_pt | Homogeneidad O₃/NO/NO₂. 3 analitos. Mismos criterios | Homogeneidad CO/SO₂ para P2. Mismos criterios |
| **F-PSEA-10** Registro Estabilidad | Estabilidad intrajornada CO/SO₂ (1 jornada) | Estabilidad O₃/NO/NO₂ durante 2–3 jornadas. O₃ reactivo requiere monitoreo especial | Estabilidad intrajornada CO/SO₂ (1 jornada, cierre) |
| **F-PSEA-11** Registro Envío/Recepción | Instalación in situ 2 equipos P1. Sin transporte externo | Instalación 6 equipos P1+P2. Coordinación tiempos ambos participantes | Instalación 2 equipos P2. Post-devolución de equipos O₃/NO/NO₂ |
| **F-PSEA-12** Reporte Participante | P1 reporta CO/SO₂: concentraciones, incertidumbres, cifras significativas | P1 y P2 reportan O₃/NO/NO₂: concentraciones, incertidumbres. Doble reporte | P2 reporta CO/SO₂: concentraciones, incertidumbres |
| **F-PSEA-13** Hoja Revisión Datos | Revisión datos P1 para CO/SO₂: unidades, plausibilidad | Revisión datos P1+P2 para O₃/NO/NO₂: más datos, mayor complejidad | Revisión datos P2 para CO/SO₂: unidades, plausibilidad |
| **F-PSEA-14** Hoja Cálculo Estadística | x_pt (CRM+dilución), σ_pt (δ_E/3), z-score P1 para CO/SO₂. Aprobación | x_pt, σ_pt, z-score P1+P2 para O₃/NO/NO₂. Algoritmo B si n<15. Aprobación | x_pt (CRM+dilución), σ_pt, z-score P2 para CO/SO₂. Aprobación |

> [!IMPORTANT]
> Los formatos F-PSEA-15 a F-PSEA-23 son de soporte/cierre y no requieren copia por ronda. Permanecen en el directorio operativo principal como plantillas de uso bajo demanda.

> [!NOTE]
> La Ronda Compleja Fase 2 (CO/SO₂ para P2) permite comparar los resultados de P2 con los de P1 de la Ronda Simple, validando la reproducibilidad del esquema con diferentes participantes para los mismos analitos.

### 4. Archivos preexistentes (sin cambios)

Los siguientes archivos permanecen intactos en `prueba_piloto/`:
- `calendario_ppiloto.md`
- `plan_doc_ppiloto.md`
- `F-PSEA-02 Cronograma Detallado_PPILOTO.xlsx`
- `gantt_a.md`, `gantt_b.md`
- `timeline_calendario_a.md`, `timeline_calendario_b.md`
- `timeline_rondas_a.md`, `timeline_rondas_b.md`

## Verificación

### Verificación manual
1. Verificar que `prueba_piloto/gestion/` contiene exactamente 16 archivos P-PSEA de gobernanza
2. Verificar que `prueba_piloto/` conserva 36 documentos operativos (3 P-PSEA + 14 I-PSEA + 19 F-PSEA) + 9 archivos preexistentes
3. Verificar que `prueba_piloto/ronda_simple/` contiene 10 formatos (F-PSEA-05 a F-PSEA-14) adaptados a CO/SO₂ y P1
4. Verificar que `prueba_piloto/ronda_compleja_fase1/` contiene 10 formatos adaptados a O₃/NO/NO₂ y P1+P2
5. Verificar que `prueba_piloto/ronda_compleja_fase2/` contiene 10 formatos adaptados a CO/SO₂ y P2 (UPB)
6. Los archivos preexistentes deben permanecer sin modificación
