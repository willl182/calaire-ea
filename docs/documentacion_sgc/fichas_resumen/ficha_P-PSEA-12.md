# Ficha Resumen: P-PSEA-12

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `P-PSEA-12` |
| **Nombre decidido** | Matriz documental basica del PEA |
| **Tipo documental** | Matriz |
| **Estado** | Elaborar |
| **Prioridad** | Alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Controla y lista el universo documental numerado del PEA, incluyendo documentos generales (`DG-PSEA`), procedimientos (`P-PSEA`), instructivos (`I-PSEA`) y formatos/registros (`F-PSEA`) con sus subformatos. Sirve como mapa de referencia para que otros documentos citen el codigo correcto sin duplicar listados.

### Rol en el flujo

- [x] Matriz
- [ ] Entrada
- [ ] Salida
- [ ] Registro oficial
- [ ] Evidencia
- [ ] Criterio tecnico
- [ ] Instructivo
- [ ] Soporte documental

Es la matriz maestra de todo lo numerado; se consulta, no se ejecuta.

---

## Aplicativos y tecnologia

#### Aplicativo asociado

- [ ] `calaire-app`
- [ ] `pt_app`
- [ ] Ambos
- [x] Ninguno

Es un documento matriz; no depende de aplicativo.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `mapa_tentativo_sgc_pea.md` | Inventario operativo tentativo | Insumo |
| `mapa_decisiones_documentales_pea.md` | Decisiones firmes por codigo | Insumo |
| `sesion_grill_sgc_pea_v1.md` | Decisiones de arquitectura | Insumo |
| `00_inventario_maestro_fichas.md` | Matriz maestra de fichas | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| Procedimientos `P-PSEA` | Referencia documental para citar codigos | Referencia |
| Formatos `F-PSEA` | Referencia documental para citar codigos | Referencia |
| Instructivos `I-PSEA` | Referencia documental para citar codigos | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-13` | Cita / Diferencia de alcance | Obligatorio |
| `P-PSEA-23` | Cita / Flujo de datos | Obligatorio |
| `DG-PSEA-01` | Referencia al cierre | Referencia |
| `P-PSEA-01` | Referencia al cierre | Referencia |

---

## Limites y riesgos

#### Limites de alcance

- No trata aprobacion, retencion, obsolescencia ni control documental macro.
- No lista archivos tecnicos internos del preprocesador (van en `P-PSEA-23`).
- No define contenido de cada documento; solo lista codigo, nombre, estado y familia.
- No es la matriz de evidencias por ronda (eso es `P-PSEA-13`).

#### Riesgos de interpretacion

- **Confundir con P-PSEA-13:** `P-PSEA-12` lista documentos del sistema; `P-PSEA-13` lista registros/evidencias generadas por ronda o evento.
- **Incluir archivos tecnicos internos:** Los archivos tecnicos del preprocesador deben mapearse en `P-PSEA-23`, no en `P-PSEA-12`.
- **Tratar como procedimiento de control documental macro:** No es un procedimiento de gestion documental institucional; es una matriz especifica del PEA.

---

## Criterio minimo de elaboracion

La matriz documental basica lista todo lo numerado (`DG`, `P`, `I`, `F` y subformatos) con codigo, nombre operativo, familia y estado consolidado, sin ambiguedades respecto a documentos retirados, reservados o absorbidos.
