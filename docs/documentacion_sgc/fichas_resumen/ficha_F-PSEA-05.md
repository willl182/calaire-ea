# Ficha Resumen: F-PSEA-05

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `F-PSEA-05` |
| **Nombre decidido** | Registro de participacion |
| **Tipo documental** | Registro |
| **Estado** | Mantener / Actualizar |
| **Prioridad** | Media |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Registro principal de participacion de laboratorios en una ronda de ensayo de aptitud. Documenta la inscripcion, confirmacion, datos de contacto, estado de participacion y resultado final de cada laboratorio. Se genera desde `calaire-app`.

### Rol en el flujo

- [x] Registro oficial
- [x] Evidencia
- [ ] Entrada
- [ ] Salida
- [ ] Criterio tecnico
- [ ] Instructivo
- [ ] Matriz
- [ ] Soporte documental

---

## Aplicativos y tecnologia

#### Aplicativo asociado

- [x] `calaire-app`
- [ ] `pt_app`
- [ ] Ambos
- [ ] Ninguno

Registro generado y mantenido en `calaire-app`.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `calaire-app` | Inscripcion y confirmacion de laboratorios | Origen |
| `P-PSEA-09` | Planificacion de ronda | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-06` | Plan de ronda EA | Referencia |
| `F-PSEA-12` | Datos exportados para analisis | Referencia |
| `P-PSEA-20` | Comunicaciones a participantes | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-09` | Planificacion que define participantes | Obligatorio |
| `F-PSEA-05A` | Anexo tecnico de equipos por participante | Obligatorio |
| `F-PSEA-12` | Datos exportados derivados de la participacion | Obligatorio |
| `DG-PSEA-02` | Aplicativo que gestiona la participacion | Obligatorio |
| `I-PSEA-10` | Instructivo para participante | Referencia |

---

## Limites y riesgos

#### Limites de alcance

- No es el anexo tecnico de equipos (eso es `F-PSEA-05A`).
- No contiene datos reportados (eso es `F-PSEA-09`).
- No es el informe final (eso es `F-PSEA-04`).
- No es un instructivo de uso.

#### Riesgos de interpretacion

- **Confundir con F-PSEA-05A:** `F-PSEA-05` es el registro de participacion; `F-PSEA-05A` es el anexo tecnico de equipos.
- **Omitir trazabilidad:** Debe vincularse con los datos exportados (`F-PSEA-12`) y el plan de ronda (`F-PSEA-06`).
- **Incluir resultados de aptitud:** Los resultados de aptitud se reportan en el informe (`F-PSEA-04`), no en el registro de participacion.

---

## Criterio minimo de elaboracion

El registro de participacion contiene inscripcion, confirmacion, datos de contacto, estado y resultado final de cada laboratorio, generado desde `calaire-app`, vinculado con `F-PSEA-05A` y `F-PSEA-12`.
