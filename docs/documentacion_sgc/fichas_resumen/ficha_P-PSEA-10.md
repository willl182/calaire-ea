# Ficha Resumen: P-PSEA-10

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `P-PSEA-10` |
| **Nombre decidido** | Procedimiento tecnico NO/NO2 |
| **Tipo documental** | Procedimiento |
| **Estado** | Implementado |
| **Prioridad** | Media |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Procedimiento tecnico especifico para la evaluacion de aptitud en oxidos de nitrogeno (NO/NO2) dentro del PEA. El documento activo es el `.docx` original suministrado como `0P-PSEA-02 Procedimiento NO-NO2.docx`, copiado y renombrado como `P-PSEA-10 Procedimiento tecnico NO-NO2.docx`. No debe sustituirse por una transcripcion generada ni por una ficha resumen.

### Rol en el flujo

- [x] Criterio tecnico
- [x] Procedimiento
- [ ] Entrada
- [ ] Salida
- [ ] Registro oficial
- [ ] Evidencia
- [ ] Instructivo
- [ ] Matriz
- [ ] Soporte documental

---

## Aplicativos y tecnologia

#### Aplicativo asociado

- [ ] `calaire-app`
- [x] `pt_app`
- [ ] Ambos
- [ ] Ninguno

El analisis estadistico se ejecuta en `pt_app`, pero este procedimiento define criterios especificos del analito.

#### Fuente controlada

| Fuente original | Archivo activo |
|---|---|
| `0P-PSEA-02 Procedimiento NO-NO2.docx` | `01_bloque_general/02_procedimientos/P-PSEA-10 Procedimiento tecnico NO-NO2.docx` |

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `P-PSEA-07` | Diseno estadistico | Referencia obligatoria |
| `F-PSEA-11` | Registro de H/E | Referencia obligatoria |
| `P-PSEA-06` | Preparacion del item | Referencia |
| `F-PSEA-12` | Dataset oficial | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `P-PSEA-09` | Informe de resultados | Referencia |
| `F-PSEA-13` | Informe final | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-07` | Cita para diseno estadistico | Obligatorio |
| `F-PSEA-11` | Cita para H/E | Obligatorio |
| `P-PSEA-09` | Cita para informe | Obligatorio |
| `P-PSEA-08` | Cita para flujo de datos | Obligatorio |
| `DG-PSEA-03` | Aplicativo de analisis | Referencia |
| `I-PSEA-04` | Instructivo de preprocesador | Referencia |
| `I-PSEA-05` | Instructivo de analisis | Referencia |

---

## Limites y riesgos

#### Limites de alcance

- No duplica el diseno estadistico (eso es `P-PSEA-07`).
- No duplica la evaluacion de H/E (eso es `F-PSEA-11` y `P-PSEA-07`).
- No duplica la generacion del informe (eso es `P-PSEA-09`).
- No duplica el flujo de datos (eso es `P-PSEA-08`).
- No es un instructivo de uso de aplicativos.
- No se reconstruye desde fichas, transcripciones `.md` ni texto generado.

#### Riesgos de interpretacion

- **Duplicar P-PSEA-07:** El procedimiento debe citar `P-PSEA-07` para estadistica, no replicar definiciones.
- **Reemplazar el original:** El riesgo principal es sustituir el `.docx` original por una version generada. La accion correcta es conservar el original renombrado.
- **Omitir particularidades de NO/NO2:** El archivo original conserva las condiciones especificas de este gas (reactividad, conversion NO-NO2, etc.).
- **Incluir H/E como procedimiento separado:** La evaluacion de H/E se documenta en `F-PSEA-11` y `P-PSEA-07`; aqui solo se cita.
- **Confundir con F-PSEA-13:** Este procedimiento no define el formato del informe; cita `P-PSEA-09` y `F-PSEA-13`.

---

## Criterio minimo de elaboracion

El procedimiento tecnico para NO/NO2 queda controlado como DOCX original activo: `0P-PSEA-02 Procedimiento NO-NO2.docx` copiado byte-a-byte y renombrado como `P-PSEA-10 Procedimiento tecnico NO-NO2.docx`.
