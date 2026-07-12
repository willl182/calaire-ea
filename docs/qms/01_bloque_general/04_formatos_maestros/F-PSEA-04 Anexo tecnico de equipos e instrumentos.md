# F-PSEA-04 Anexo tecnico de equipos e instrumentos

**Codigo:** F-PSEA-04  
**Version:** 0  
**Tipo:** Formato maestro  
**Fuente base definida:** `ronda_1_equipos.csv`  
**Aplicacion:** Exportacion desde `F-PSEA-03` / `calaire-app` de los equipos e instrumentos declarados por laboratorio participante para una ronda de ensayo de aptitud.

---

## 1. Objetivo

Registrar, como anexo tecnico exportado desde `calaire-app`, los equipos, analizadores e instrumentos declarados por cada laboratorio participante en `F-PSEA-03`, manteniendo trazabilidad entre ronda, codigo de laboratorio, contaminante y equipo utilizado.

---

## 2. Alcance

Este formato aplica a los instrumentos reportados por los participantes en `F-PSEA-03` y al equipo de referencia cuando corresponda. La informacion registrada se exporta desde `calaire-app`, sirve para validar datos reportados y prepara archivos usados por `pt_app`.

---

## 3. Fuente de datos

La estructura inicial se basa en `ronda_1_equipos.csv`, con el siguiente esquema observado:

| Campo | Descripcion |
|---|---|
| `Codigo_Lab` | Codigo anonimizado del laboratorio o fila de referencia. |
| `Analizador_SO2` | Marca/modelo del analizador usado para SO2. |
| `Analizador_CO` | Marca/modelo del analizador usado para CO. |

Ejemplo de fuente:

| Codigo_Lab | Analizador_SO2 | Analizador_CO |
|---|---|---|
| REFERENCIA | HORIBA APSA- 370 | Teledyne T300 |
| p1 | Teledyne T100 | Teledyne T300 |

---

## 4. Campos minimos del formato maestro

| Campo | Obligatorio | Descripcion |
|---|---|---|
| Ronda | Si | Identificador de la ronda. |
| Codigo_Lab | Si | Codigo anonimizado del laboratorio. |
| Contaminante | Si | Gas asociado al instrumento: SO2, CO, O3, NO, NO2 u otro definido. |
| Instrumento | Si | Marca/modelo del analizador o equipo usado. |
| Metodo | No | Metodo declarado por el participante si aplica. |
| Serie / identificacion | No | Numero de serie o identificador interno cuando este disponible. |
| Estado de calibracion | No | Vigente, vencido, no informado o no aplica. |
| Observaciones | No | Comentarios tecnicos del registro. |

---

## 5. Reglas de diligenciamiento

- Cada laboratorio participante debe tener al menos un registro por contaminante que vaya a reportar.
- El codigo de laboratorio debe mantenerse anonimizado.
- La fila `REFERENCIA`, cuando exista, debe distinguirse de los participantes.
- No se deben incluir nombres comerciales o datos de contacto del laboratorio si comprometen la confidencialidad.
- Las modificaciones posteriores al cierre de la recepcion de datos deben quedar justificadas.

---

## 6. Relacion documental

| Documento | Relacion |
|---|---|
| `F-PSEA-03` | Registro de participacion desde el cual se exportan los equipos. |
| `F-PSEA-06` | Planificacion completa que usa la informacion tecnica de equipos. |
| `F-PSEA-08` | Usa la informacion de instrumento para validar datos reportados. |
| `F-PSEA-09` | Exporta datos hacia `pt_app` con identificacion de instrumento. |
| `DG-PSEA-02` | Control funcional en `calaire-app`. |
| `DG-PSEA-03` | Uso posterior en `pt_app`. |

---

## 7. Criterio de completitud

El formato se considera completo cuando todos los laboratorios participantes tienen equipos/instrumentos declarados para los contaminantes que reportan, la informacion esta asociada a una ronda y no existen campos obligatorios vacios.
