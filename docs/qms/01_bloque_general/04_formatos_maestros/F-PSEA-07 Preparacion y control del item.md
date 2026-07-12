# F-PSEA-07 Preparacion y control del item

**Codigo:** F-PSEA-07  
**Version:** 0  
**Tipo:** Formato maestro  
**Fuente base definida:** tabla de valores/niveles del `F-PSEA-02 Cronograma Detallado_v0.xlsx`  
**Aplicacion:** Registro de valores programados, niveles y control operacional del item de ensayo gaseoso.

---

## 1. Objetivo

Documentar la preparacion y control del item de ensayo gaseoso mediante el registro de corridas, contaminantes, niveles, unidades, duraciones y valores programados o de referencia usados durante la ronda.

---

## 2. Alcance

Aplica a los items gaseosos generados dinamicamente para los contaminantes criterio incluidos en la ronda. El formato debe permitir reconstruir que niveles se programaron, durante cuanto tiempo, en que secuencia y con que valores esperados.

---

## 3. Fuente de datos

La fuente definida es el archivo `F-PSEA-02 Cronograma Detallado_v0.xlsx`, que contiene elementos como:

- corrida;
- componente;
- dia;
- inicio;
- duracion;
- contaminantes: O3, NO, NO2, SO2, CO;
- unidades: `nmol/mol`, `umol/mol`;
- nivel;
- gas;
- duracion en horas;
- valores por contaminante.

---

## 4. Campos minimos del formato maestro

| Campo | Obligatorio | Descripcion |
|---|---|---|
| Ronda | Si | Identificador de ronda. |
| Corrida | Si | Numero o codigo de corrida. |
| Dia | Si | Dia programado de ejecucion. |
| Hora de inicio | Si | Inicio programado de la corrida. |
| Duracion | Si | Duracion esperada del nivel o corrida. |
| Nivel | Si | Nivel de concentracion programado. |
| Gas / contaminante | Si | CO, SO2, O3, NO, NO2 u otro definido. |
| Valor programado | Si | Valor nominal o de referencia programado. |
| Unidad | Si | Unidad asociada al valor. |
| Fuente del valor | Si | Cronograma, calibrador, referencia, calculo u otro. |
| Observaciones | No | Comentarios operativos o tecnicos. |

---

## 5. Reglas de control

- Los valores deben coincidir con el cronograma aprobado o quedar justificados si fueron modificados.
- Cada contaminante incluido en la ronda debe tener valores definidos para las corridas aplicables.
- Los cambios de duracion, nivel o valor deben registrarse con fecha, responsable y justificacion.
- El formato debe distinguir valores programados de valores observados o calculados posteriormente.
- No debe mezclar resultados de participantes ni evaluacion estadistica.

---

## 6. Relacion documental

| Documento | Relacion |
|---|---|
| `F-PSEA-02` | Fuente de cronograma y valores programados. |
| `P-PSEA-06` | Procedimiento de preparacion y control del item gaseoso. |
| `P-PSEA-07` | Usa los valores para evaluacion estadistica cuando aplique. |
| `F-PSEA-11` | Usa informacion del item para homogeneidad y estabilidad. |
| `F-PSEA-13` | El informe final resume los niveles usados. |

---

## 7. Criterio de completitud

El formato se considera completo cuando todos los niveles y corridas de la ronda tienen contaminante, valor, unidad, duracion, fuente y estado de control documentado.
