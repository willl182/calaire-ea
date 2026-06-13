# Ficha Resumen: P-PSEA-01

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `P-PSEA-01` |
| **Nombre decidido** | Protocolo general EA |
| **Tipo documental** | Procedimiento |
| **Estado** | Mantener |
| **Prioridad** | Cierre |
| **Clase de ficha** | Ficha diferida |

---

## Proposito y rol

### Proposito operativo

Procedimiento general de ensayos de aptitud del PEA. Se mantiene vigente conceptualmente pero se revisara al final del ciclo de estabilizacion del sistema documental, cuando las fichas base (`P-PSEA-12`, `P-PSEA-13`, `P-PSEA-23`) y los aplicativos (`DG-PSEA-02`, `DG-PSEA-03`) ya esten definidos. No se interviene en esta fase.

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

Es un procedimiento marco que requiere cierre al final.

---

## Aplicativos y tecnologia

#### Aplicativo asociado

- [ ] `calaire-app`
- [ ] `pt_app`
- [ ] Ambos
- [x] Ninguno

Procedimiento marco; no depende de aplicativo especifico.

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
| `DG-PSEA-01` | Protocolo general de participacion (referencia al cierre) | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `DG-PSEA-01` | Protocolo general de participacion (documento paralelo) | Obligatorio |
| `P-PSEA-12` | Matriz documental que se citara al cierre | Referencia |
| `P-PSEA-13` | Matriz de evidencias que se citara al cierre | Referencia |
| `P-PSEA-23` | Flujo de datos que se citara al cierre | Referencia |

---

## Limites y riesgos

#### Limites de alcance

- No se desarrolla ni actualiza en esta fase; es diferida para cierre global.
- No debe editarse hasta que el sistema de fichas y documentos base este estabilizado.
- No es un procedimiento especifico por analito; es el protocolo general.

#### Riesgos de interpretacion

- **Editar prematuramente:** Puede romper la secuencia de estabilizacion si se edita antes de cerrar las fichas base.
- **Confundir con DG-PSEA-01:** `DG-PSEA-01` es el protocolo como documento general; `P-PSEA-01` es el protocolo como procedimiento.
- **Omitir cierre:** Debe quedar programado para revision posterior.

---

## Criterio minimo de elaboracion

La ficha diferida registra la decision de mantener `P-PSEA-01` sin intervencion hasta el cierre global, cuando se citaran las fichas base estabilizadas, sin editar en esta fase.
