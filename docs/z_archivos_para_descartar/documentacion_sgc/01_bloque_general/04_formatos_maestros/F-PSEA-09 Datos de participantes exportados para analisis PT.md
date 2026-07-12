# F-PSEA-09 Datos de participantes exportados para analisis PT

**Codigo:** F-PSEA-09  
**Version:** 0  
**Tipo:** Formato maestro  
**Sistema fuente:** `calaire-app`  
**Sistema destino:** `pt_app`  
**Aplicacion:** Registro de la exportacion oficial de datos de participantes para analisis estadistico.

---

## 1. Objetivo

Formalizar el paquete de datos exportado desde `calaire-app` hacia `pt_app`, garantizando que el conjunto enviado para analisis PT sea identificable, reproducible y trazable.

---

## 2. Alcance

Aplica a cada exportacion oficial de datos de participantes asociada a una ronda. No corresponde al dato capturado originalmente (`F-PSEA-08`) ni al dataset consolidado posterior (`F-PSEA-12`).

---

## 3. Campos minimos del registro de exportacion

| Campo | Obligatorio | Descripcion |
|---|---|---|
| Ronda | Si | Identificador de ronda. |
| Fecha de exportacion | Si | Fecha y hora de generacion del paquete. |
| Responsable | Si | Usuario que ejecuta o autoriza la exportacion. |
| Archivo exportado | Si | Nombre y ruta del archivo generado. |
| Version de esquema | Si | Version del esquema de columnas usado. |
| Numero de participantes | Si | Participantes incluidos. |
| Numero de registros | Si | Filas exportadas. |
| Contaminantes incluidos | Si | Lista de contaminantes incluidos. |
| Hash / checksum | No | Identificador de integridad si aplica. |
| Estado | Si | `generado`, `validado`, `enviado`, `rechazado`, `reemplazado`. |
| Observaciones | No | Comentarios sobre restricciones o incidencias. |

---

## 4. Estructura esperada del archivo exportado

El archivo exportado debe contener, como minimo, los campos validados en `F-PSEA-08`:

- identificador de ronda;
- codigo de laboratorio;
- contaminante;
- nivel;
- corrida;
- unidad;
- instrumento;
- valores reportados;
- promedio;
- desviacion;
- incertidumbre si aplica;
- fechas/horas asociadas;
- estado de validacion.

---

## 5. Reglas de exportacion

- Solo deben exportarse datos validados o aceptados con observacion.
- La exportacion debe congelar el conjunto enviado a `pt_app`.
- Cualquier nueva exportacion debe quedar versionada y no sobrescribir la evidencia anterior.
- La estructura de columnas debe ser estable o documentar cambios de version.
- La exportacion no debe incluir identidad real del laboratorio si no es necesaria para `pt_app`.

---

## 6. Relacion documental

| Documento | Relacion |
|---|---|
| `F-PSEA-08` | Fuente de datos reportados por participante. |
| `F-PSEA-10` | Registra preprocesamiento posterior en `pt_app`. |
| `F-PSEA-12` | Dataset oficial consolidado resultante. |
| `DG-PSEA-02` | Define el control funcional de `calaire-app`. |
| `DG-PSEA-03` | Define el control funcional de `pt_app`. |

---

## 7. Criterio de completitud

El formato se considera completo cuando existe un archivo exportado, con version, responsable, fecha, numero de registros y estado validado para envio o procesamiento en `pt_app`.
