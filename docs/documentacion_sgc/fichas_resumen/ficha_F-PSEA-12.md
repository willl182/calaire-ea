# Ficha Resumen: F-PSEA-12

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `F-PSEA-12` |
| **Nombre decidido** | Datos de participantes exportados para analisis PT |
| **Tipo documental** | Exportacion |
| **Estado** | Mantener / Actualizar |
| **Prioridad** | Alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Exportacion oficial de datos de participantes desde `calaire-app` hacia `pt_app` para analisis de ensayo de aptitud. Incluye datos reportados, informacion de participantes y equipos, pero no es el dataset consolidado final (eso es `F-PSEA-14`). Es la interfaz formal entre los dos aplicativos.

### Rol en el flujo

- [x] Salida
- [x] Entrada
- [ ] Registro oficial
- [ ] Evidencia
- [ ] Criterio tecnico
- [ ] Instructivo
- [ ] Matriz
- [ ] Soporte documental

Es salida de `calaire-app` y entrada oficial de `pt_app`.

---

## Aplicativos y tecnologia

#### Aplicativo asociado

- [x] `calaire-app`
- [x] `pt_app`
- [ ] Ambos
- [ ] Ninguno

Ambos aplicativos intervienen: `calaire-app` genera, `pt_app` consume.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-09` | Datos reportados por participante | Insumo |
| `F-PSEA-05` | Registro de participacion | Insumo |
| `F-PSEA-05A` | Anexo tecnico de equipos | Insumo |
| `calaire-app` | Interfaz de exportacion | Origen |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `pt_app` | Entrada para preprocesamiento y analisis | Entrada oficial |
| `P-PSEA-23` | Flujo tecnico que documenta este paso | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `F-PSEA-09` | Datos reportados que se exportan | Obligatorio |
| `F-PSEA-05` | Participacion que se exporta | Obligatorio |
| `F-PSEA-05A` | Equipos que se exportan | Obligatorio |
| `F-PSEA-14` | Dataset consolidado que resulta despues | Obligatorio |
| `P-PSEA-23` | Flujo tecnico que gobierna este paso | Obligatorio |
| `DG-PSEA-02` | Aplicativo de origen | Obligatorio |
| `DG-PSEA-03` | Aplicativo de destino | Obligatorio |

---

## Limites y riesgos

#### Limites de alcance

- No es el dataset consolidado final (eso es `F-PSEA-14`); es la exportacion desde `calaire-app`.
- No es el registro de preprocesamiento (eso es `F-PSEA-10`).
- No contiene resultados de H/E (eso es `F-PSEA-13C` y `F-PSEA-13D`).
- No es un instructivo de uso.

#### Riesgos de interpretacion

- **Confundir con F-PSEA-14:** `F-PSEA-12` es la exportacion desde `calaire-app`; `F-PSEA-14` es el dataset consolidado desde `pt_app`.
- **Confundir con F-PSEA-09:** `F-PSEA-09` es la captura individual; `F-PSEA-12` es la exportacion consolidada.
- **Omitir trazabilidad:** La exportacion debe tener fecha, version y responsable.
- **Usar como dataset final:** Solo `F-PSEA-14` es el dataset oficial para analisis; `F-PSEA-12` es la exportacion previa.

---

## Criterio minimo de elaboracion

La exportacion oficial contiene datos de participantes, equipos y registros, generada desde `calaire-app`, con fecha, version y responsable, como entrada oficial de `pt_app`, diferenciada claramente de `F-PSEA-14`.
