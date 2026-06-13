# Ficha Resumen: DG-PSEA-01

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `DG-PSEA-01` |
| **Nombre decidido** | Protocolo general de participacion EA |
| **Tipo documental** | Documento general |
| **Estado** | Mantener |
| **Prioridad** | Cierre |
| **Clase de ficha** | Ficha diferida |

---

## Proposito y rol

### Proposito operativo

Documento general que describe el protocolo de participacion en los ensayos de aptitud del PEA. Se mantiene vigente conceptualmente pero se revisara al final del ciclo de estabilizacion del sistema documental, cuando las fichas base (`P-PSEA-12`, `P-PSEA-13`, `P-PSEA-23`) y los aplicativos (`DG-PSEA-02`, `DG-PSEA-03`) ya esten definidos. No se interviene en esta fase.

### Rol en el flujo

- [x] Soporte documental
- [ ] Entrada
- [ ] Salida
- [ ] Registro oficial
- [ ] Evidencia
- [ ] Criterio tecnico
- [ ] Instructivo
- [ ] Matriz

Es un documento marco que requiere cierre al final.

---

## Aplicativos y tecnologia

#### Aplicativo asociado

- [ ] `calaire-app`
- [ ] `pt_app`
- [ ] Ambos
- [x] Ninguno

Documento general marco; no depende de aplicativo.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `P-PSEA-12` | Matriz documental (al cierre) | Referencia |
| `P-PSEA-13` | Matriz de evidencias (al cierre) | Referencia |
| `P-PSEA-23` | Flujo de datos (al cierre) | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `P-PSEA-01` | Protocolo general EA (referencia al cierre) | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-01` | Protocolo general EA (documento marco paralelo) | Obligatorio |
| `P-PSEA-12` | Matriz documental que se citara al cierre | Referencia |
| `DG-PSEA-02` | Aplicativo que se citara al cierre | Referencia |
| `DG-PSEA-03` | Aplicativo que se citara al cierre | Referencia |

---

## Limites y riesgos

#### Limites de alcance

- No se desarrolla ni actualiza en esta fase; es diferida para cierre global.
- No debe editarse hasta que el sistema de fichas y documentos base este estabilizado.
- No es un procedimiento operativo; es un documento general de marco.

#### Riesgos de interpretacion

- **Editar prematuramente:** Puede romper la secuencia de estabilizacion si se edita antes de cerrar las fichas base.
- **Confundir con P-PSEA-01:** `P-PSEA-01` es el protocolo general como procedimiento; `DG-PSEA-01` es el protocolo como documento general.
- **Omitir cierre:** Debe quedar programado para revision posterior.

---

## Criterio minimo de elaboracion

La ficha diferida registra la decision de mantener `DG-PSEA-01` sin intervencion hasta el cierre global, cuando se citaran las fichas base estabilizadas, sin editar en esta fase.
