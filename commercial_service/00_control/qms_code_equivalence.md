# Equivalencia de Códigos QMS (Blueprint → Vigente)

**Propósito:** los artefactos `CS-01` a `CS-15` citan códigos `P-PSEA-XX`, `F-PSEA-XX`, `I-PSEA-XX` del QMS. La matriz `docs/sgc/matriz_equivalencias_codigos_sgc_pea.md` (aprobada 2026-06-14) renumeró estos códigos. Esta tabla traduce referencias heredadas al código vigente del QMS para que la búsqueda directa funcione.

**Regla de uso:** cuando un artefacto diga `X-PSEA-NN` con significado antiguo, este mapa indica el código vigente. Si el significado antiguo y el nuevo son el mismo (no renumerado), se deja sin cambio.

## Procedimientos P-PSEA

| Referencia en blueprint / artefacto | Significado que el blueprint le daba | Código vigente en QMS (post-renumeración 2026-06-14) | Notas |
|---|---|---|---|
| `P-PSEA-01` | Protocolo general EA | `P-PSEA-01` | Sin cambio. |
| `P-PSEA-04` | Round planning | `P-PSEA-04` | Sin cambio. |
| `P-PSEA-05` | Comunicaciones del PEA | `P-PSEA-05` | Sin cambio en número ni significado (P-PSEA-20 → P-PSEA-05, mismo nombre). |
| `P-PSEA-06` | Statistical design and evaluation | `P-PSEA-07` | Renumerado (antiguo P-PSEA-06 → nuevo P-PSEA-07). Actualizar referencias. |
| `P-PSEA-07` | Statistical work | `P-PSEA-07` | Mismo código vigente, mismo significado funcional (se renumeró P-PSEA-06 → P-PSEA-07). |
| `P-PSEA-08` | Digital data management | `P-PSEA-08` | Sin cambio. |
| `P-PSEA-09` | Report generation and emission | `P-PSEA-09` | Sin cambio en número (antiguo P-PSEA-07 → nuevo P-PSEA-09, mismo nombre funcional). |
| `P-PSEA-15` | Mejora continua (antiguo) | `P-PSEA-15` | Cambio de significado: ahora = Trabajo no conforme / NC / CAPA. |
| `P-PSEA-16` | Confidencialidad operativa (antiguo) | `P-PSEA-16` | Cambio de significado: ahora = Divulgación y control de valores sensibles. |
| `P-PSEA-17` | Auditorías (antiguo, retirado) | `P-PSEA-17` | Cambio de significado: ahora = Quejas del PEA. |
| `P-PSEA-18` | Revisión por la dirección (antiguo, retirado) | `P-PSEA-18` | Cambio de significado: ahora = Apelaciones del PEA. |
| `P-PSEA-19` | Imparcialidad institucional (antiguo, retirado) | `P-PSEA-19` | Cambio de significado: ahora = Confidencialidad operativa interna. |
| `P-PSEA-20` | Competencia del personal (antiguo) | `P-PSEA-20` | Sin cambio. |

## Formatos y registros F-PSEA

| Referencia en blueprint / artefacto | Significado que el blueprint le daba | Código vigente en QMS | Notas |
|---|---|---|---|
| `F-PSEA-01` | Round calendar | `F-PSEA-01` | Sin cambio. |
| `F-PSEA-02` | Round schedule | `F-PSEA-02` | Sin cambio. |
| `F-PSEA-04` | Informe final de resultados (código antiguo) | `F-PSEA-13` | Renumerado. En el QMS vigente, `F-PSEA-04` identifica el anexo técnico de equipos. **Para el informe final usar `F-PSEA-13`.** |
| `F-PSEA-05` | Round plan EA | `F-PSEA-03` | Renumerado. |
| `F-PSEA-05A` | Anexo técnico de equipos (antiguo) | `F-PSEA-04` | Renumerado. El anexo técnico está en `F-PSEA-04`. **No usar `F-PSEA-05A`.** |
| `F-PSEA-06` | Plan de ronda (antiguo) | `F-PSEA-05` | Renumerado. |
| `F-PSEA-07` | Ficha digital de ronda (antiguo) | `F-PSEA-06` | Renumerado. |
| `F-PSEA-08` a `F-PSEA-12` | Datos y preprocesamiento | `F-PSEA-07` a `F-PSEA-12` | Mapeo según matriz. |
| `F-PSEA-13` | Paquete de homogeneidad / estabilidad (antiguo) | `F-PSEA-11` | Renumerado. **Y el "F-PSEA-13" del blueprint (informe final) ahora está en `F-PSEA-13`.** Colisión importante: la matriz renumeró el antiguo F-PSEA-13 a F-PSEA-11, y al mismo tiempo promovió el antiguo F-PSEA-04 (informe final) a F-PSEA-13. |
| `F-PSEA-14` | Datos consolidados (antiguo) | `F-PSEA-12` | Renumerado. |
| `F-PSEA-15` | Queja / NC / CAPA (antiguo) | `F-PSEA-14` | Renumerado. |
| `F-PSEA-16` | Registro de queja / NC / CAPA (antiguo) | `F-PSEA-14` | Renumerado. Este es el antecedente correcto del registro vigente de quejas / NC / CAPA. |
| `F-PSEA-17` | Registro de apelaciones (antiguo) | `F-PSEA-15` | Renumerado. |

## Instructivos I-PSEA

| Referencia | Significado | Código vigente | Notas |
|---|---|---|---|
| `I-PSEA-01` | Embalaje y transporte | `I-PSEA-01` | Sin cambio. |
| `I-PSEA-02` | Uso de `calaire-app` | `I-PSEA-02` | Sin cambio. |

## Documentos generales DG-PSEA

| Referencia | Significado | Código vigente | Notas |
|---|---|---|---|
| `DG-PSEA-01` | Protocolo general de participación | `DG-PSEA-01` | Sin cambio. |

## Implicación operativa para los artefactos

Cualquier referencia en `CS-01` … `CS-15` debe leerse a través de esta tabla. Tres puntos críticos:

1. **Para informe final de resultados** usar `F-PSEA-13` (no el antiguo `F-PSEA-04`). CS-13 ya está correcto.
2. **Para datos técnicos de equipos e instrumentos** usar `F-PSEA-04` (no el antiguo `F-PSEA-05A`). CS-11 ya usa el código vigente.
3. **Para quejas** usar `P-PSEA-17`. **Para apelaciones** usar `P-PSEA-18`. **Para confidencialidad** usar `P-PSEA-19`. **Para NC/CAPA** usar `P-PSEA-15`.

Si un artefacto cita un código que la tabla marca como "Cambio de significado", el lector debe confirmar que el significado **nuevo** es el que aplica al uso comercial (casi siempre sí, pero conviene verificarlo en la primera lectura).

## Fuente normativa

- `docs/sgc/matriz_equivalencias_codigos_sgc_pea.md` (aprobada 2026-06-14).
- `docs/qms/01_bloque_general/05_matrices_inventarios/Árbol Maestro PSEA.md` (mapa activo).
- `docs/sgc/checklist_sgc_pdts.md` (checklist de procedimientos activos).
