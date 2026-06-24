# Instrucciones - F-PSEA-08 Datos reportados por participante

**Codigo:** `F-PSEA-08`  
**Tipo:** Formato / registro digital  
**Sistema fuente:** `calaire-app`  
**Estado:** pendiente de consolidacion como maestro documental  
**Ubicacion esperada:** `01_bloque_general/04_formatos_maestros/F-PSEA-08 Datos reportados por participante.docx`

---

## Proposito

Documentar los datos reportados por cada participante durante una ronda del ensayo de aptitud, conservando la trazabilidad entre laboratorio, ronda, contaminante, nivel, corrida, instrumento y valores enviados.

`F-PSEA-08` representa el dato capturado o recibido por `calaire-app`. No es todavia el paquete oficial exportado a `pt_app`; esa funcion corresponde a `F-PSEA-09`.

---

## Alcance

Aplica a los resultados y datos tecnicos que el participante entrega al PEA mediante `calaire-app` o mediante un flujo controlado que posteriormente se registra en el aplicativo.

Incluye:

- identificacion de ronda;
- identificacion anonimizada del participante;
- contaminante;
- nivel o corrida;
- instrumento declarado;
- unidad;
- valores horarios o replicas reportadas;
- promedio reportado;
- desviacion o incertidumbre declarada cuando aplique;
- fecha y responsable del envio;
- estado de validacion en `calaire-app`.

---

## Campos minimos recomendados

| Campo | Descripcion |
|---|---|
| `round_id` | Identificador de la ronda en `calaire-app`. |
| `participant_id` | Identificador interno del participante. |
| `Codigo_Lab` | Codigo anonimizado usado en la ronda. |
| `pollutant` | Contaminante reportado: CO, SO2, O3, NO, NO2 u otro definido. |
| `level` | Nivel de concentracion o identificador de nivel. |
| `run` | Corrida asociada al nivel. |
| `unit` | Unidad de reporte. |
| `instrument` | Instrumento o analizador declarado para la medicion. |
| `mean_h1` | Primer promedio horario o valor equivalente. |
| `mean_h2` | Segundo promedio horario o valor equivalente. |
| `mean_h3` | Tercer promedio horario o valor equivalente. |
| `mean_value` | Promedio consolidado reportado por participante. |
| `sd_value` | Desviacion estandar reportada o calculada sobre valores enviados. |
| `u_value` | Incertidumbre estandar o valor equivalente informado. |
| `k_factor` | Factor de cobertura asociado a la incertidumbre expandida. |
| `u_exp` | Incertidumbre expandida reportada o derivada. |
| `n_hours` | Numero de horas o mediciones usadas para el promedio. |
| `hour_starts` | Fechas/horas de inicio asociadas a cada medicion. |
| `submitted_at` | Fecha y hora de envio. |
| `submitted_by` | Usuario o responsable del envio. |
| `validation_status` | Estado de validacion: `recibido`, `incompleto`, `observado`, `validado`, `rechazado`. |
| `observations` | Observaciones tecnicas o administrativas. |

---

## Reglas de captura

- El dato original reportado por el participante debe conservarse sin sobrescritura destructiva.
- Toda correccion debe quedar trazada con fecha, usuario, campo corregido, valor anterior, valor nuevo y justificacion.
- El codigo de laboratorio debe mantenerse anonimizado.
- El sistema debe validar que contaminante, nivel, corrida y unidad correspondan al plan de ronda.
- No se deben incluir calculos estadisticos de desempeno en este registro.
- No se deben mezclar datos de referencia, consenso, robustos o resultados de evaluacion.

---

## Validaciones minimas en calaire-app

`calaire-app` debe verificar:

- participante habilitado para la ronda;
- contaminante y nivel esperados;
- unidad de medida permitida;
- completitud de valores requeridos;
- coherencia entre `n_hours` y valores horarios diligenciados;
- presencia de instrumento declarado;
- fecha de envio dentro del periodo permitido o justificacion si aplica;
- duplicados por participante, contaminante, nivel y corrida.

---

## Relacion con otros registros

| Registro | Relacion |
|---|---|
| `F-PSEA-04` | Provee informacion de equipos e instrumentos del participante. |
| `F-PSEA-05A` | Identifica participante y datos de registro. |
| `F-PSEA-09` | Recibe la exportacion oficial derivada de `F-PSEA-08`. |
| `F-PSEA-10` | Registra el preprocesamiento posterior en `pt_app`. |
| `F-PSEA-12` | Dataset oficial consolidado posterior al procesamiento. |

---

## Criterio de completitud

`F-PSEA-08` se considera completo para una ronda cuando:

1. todos los participantes esperados reportaron sus datos o existe justificacion documentada;
2. cada registro tiene contaminante, nivel, corrida, unidad, instrumento y valores requeridos;
3. las validaciones de `calaire-app` estan cerradas;
4. las observaciones tecnicas fueron resueltas o transferidas a una accion documentada;
5. el conjunto esta listo para generar `F-PSEA-09`.
