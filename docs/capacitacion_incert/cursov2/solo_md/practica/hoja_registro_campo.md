# Hoja de registro de campo — genérica

Base común para todos los experimentos E01–E16. Cada protocolo especifica columnas adicionales; estas son las mínimas que deben estar presentes siempre, en el orden indicado. Unidades de fracción molar: **nmol/mol**. No sobrescribir datos crudos: las correcciones por certificado o firmware se registran en columnas nuevas.

## Encabezado de sesión (una vez por jornada/equipo)

| Campo | Valor |
|---|---|
| Fecha | |
| Equipo (nombres) | |
| Experimento(s) ejecutado(s) | |
| Analizador(es) UUT: fabricante/modelo/serie/firmware | |
| Patrón/fotómetro: fabricante/modelo/serie/certificado vigente hasta | |
| Calibrador-diluidor: modelo/serie | |
| Cilindro de NO: serie/concentración certificada/vigencia | |
| Hora de encendido de equipos | |
| Checklist de montaje y seguridad completado (sí/no, hora) | |

## Tabla de registro por punto

| fecha_hora | experimento | ciclo/bloque | punto/nivel_nominal_nmol_mol | replica_1min | lectura_cruda_nmol_mol | valor_corregido_nmol_mol | canal (NO/NOx/O3/otro) | T_C | P_kPa | flujo_L_min | tiempo_purga_min | tiempo_estabilizacion_min | estado_estable (sí/no) | ajuste_o_intervencion | incidencia |
|---|---|---:|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---|---|

## Reglas de diligenciamiento

1. Un registro por lectura o media reportada; no promediar antes de escribir el dato crudo cuando el protocolo pide series completas.
2. `estado_estable` se marca solo cuando se cumplió el criterio de estabilización del checklist (cambio <1.0 nmol/mol en 5 min y `s` de las últimas cinco medias ≤0.5 nmol/mol), salvo que el experimento defina un criterio propio (por ejemplo E11).
3. `ajuste_o_intervencion` registra cualquier cambio de configuración, ajuste de cero/span o modificación de firmware, con hora. Ninguna serie continúa después de un ajuste no documentado.
4. `incidencia` registra alarmas, olores, fugas, pérdida de extracción, caudal insuficiente o cualquier evento que pueda invalidar el punto. No se elimina un punto sin nota aquí.
5. Los campos numéricos se registran con las cifras que entrega el instrumento; el redondeo se aplica solo al final del análisis.
6. Cada hoja física o digital indica el nombre del archivo/experimento que la reemplaza en la tabla de registro específica (por ejemplo, E02 usa además las columnas de regresión definidas en `E02_verificacion_multipunto.md`).
