# Instrucciones para cálculo y reporte de resultados — Ronda 3

## 1. Fuente para selección de datos

Use el archivo `cronograma_periodos_niveles_estabilizacion.csv` para identificar, según el contaminante asignado:

- inicio y fin de cada nivel;
- periodos de estabilización;
- duración disponible para cálculo.

Use la columna de tiempo de ejecución (`runtime`) de sus datos para ubicar cada medición dentro del cronograma.

No incluya datos de los periodos marcados como `estabilizacion` en los cálculos de los niveles. Tampoco mezcle datos de niveles diferentes.

## 2. Identificación del nivel cero

Para efectos del ejercicio, el **nivel 1 corresponde al nivel cero**.

Calcule y reporte **un promedio horario** para este nivel. El promedio debe representar 60 minutos de datos válidos pertenecientes exclusivamente al nivel cero.

## 3. Cálculos para los demás niveles

Para cada nivel diferente del nivel cero, calcule y reporte **tres promedios horarios**.

Cada promedio horario debe:

- corresponder a un periodo de 60 minutos;
- usar únicamente datos válidos del nivel evaluado;
- excluir periodos de estabilización;
- conservar trazabilidad sobre hora o runtime de inicio y fin;
- calcularse según el procedimiento interno vigente del participante.

Cuando la duración disponible del nivel no permita obtener tres periodos independientes de 60 minutos, el participante podrá seleccionar ventanas horarias con superposición, si su procedimiento interno lo permite. Debe identificar claramente las ventanas usadas y declarar la superposición. No debe completar periodos con datos de estabilización, de otro nivel ni con datos estimados.

## 4. Ejercicio con solo dos niveles

Uno de los ejercicios asignados contiene únicamente dos niveles. Para este caso aplique la misma regla:

- nivel cero: un promedio horario;
- nivel diferente de cero: tres promedios horarios.

No deben crearse, interpolarse ni suponerse niveles adicionales.

## 5. Estadísticos por cada promedio horario

Para cada promedio horario reporte, como mínimo:

1. contaminante;
2. nivel;
3. runtime de inicio;
4. runtime de fin;
5. número de datos válidos utilizados (`n`);
6. promedio horario;
7. desviación estándar;
8. incertidumbre estándar;
9. factor de cobertura (`k`);
10. incertidumbre expandida (`U`).

Si el procedimiento interno exige estadísticas adicionales, inclúyalas en el reporte.

## 6. Promedio horario

Calcule el promedio aritmético de los resultados válidos incluidos en la ventana seleccionada:

\[
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i
\]

Donde:

- \(x_i\): cada resultado válido;
- \(n\): número de resultados válidos;
- \(\bar{x}\): promedio horario.

No sustituya valores faltantes ni excluya resultados sin aplicar los criterios definidos en su procedimiento interno.

## 7. Desviación estándar

Reporte la desviación estándar asociada a los datos usados en cada promedio horario. Salvo que su procedimiento interno establezca otra definición documentada, use la desviación estándar muestral:

\[
s=\sqrt{\frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}}
\]

Informe unidades y cantidad de datos usados. Si aplica tratamiento de valores atípicos, datos no válidos o resultados bajo límite de cuantificación, describa el criterio y conserve evidencia de su aplicación.

## 8. Incertidumbre de medición

Estime y reporte la incertidumbre para **cada promedio horario**, de acuerdo con su procedimiento interno vigente.

El participante debe:

- identificar las fuentes de incertidumbre consideradas;
- indicar el método de evaluación usado;
- combinar las contribuciones según su procedimiento;
- reportar la incertidumbre estándar combinada \(u_c\);
- mantener disponibles el presupuesto de incertidumbre, cálculos y registros de soporte.

No se exige reemplazar el modelo de incertidumbre interno por un modelo común para la ronda. El resultado debe ser técnicamente sustentable y trazable al procedimiento aplicado.

## 9. Factor de cobertura e incertidumbre expandida

Reporte el factor de cobertura \(k\) aplicado en cada punto.

Calcule la incertidumbre expandida mediante:

\[
U=k\,u_c
\]

Donde:

- \(u_c\): incertidumbre estándar combinada;
- \(k\): factor de cobertura;
- \(U\): incertidumbre expandida.

Además, indique el nivel de confianza asociado o el criterio usado para seleccionar \(k\). No reporte únicamente la incertidumbre expandida sin informar el factor de cobertura.

## 10. Reglas de expresión de resultados

- Use la misma unidad para promedio, desviación estándar, incertidumbre estándar e incertidumbre expandida.
- Identifique claramente la unidad reportada.
- Aplique criterios de redondeo según su procedimiento interno.
- Mantenga coherencia entre cifras decimales del resultado y su incertidumbre.
- Declare correcciones, conversiones de unidad o factores aplicados.
- No modifique los límites de los niveles definidos en el cronograma.

## 11. Estructura mínima de entrega

Entregue una fila por cada promedio horario calculado, con esta estructura mínima:

| Contaminante | Nivel | Promedio horario | Runtime inicio | Runtime fin | n | Desviación estándar | Incertidumbre estándar combinada | k | Incertidumbre expandida | Unidad | Observaciones |
|---|---:|---:|---|---|---:|---:|---:|---:|---:|---|---|

En `Observaciones`, declare como mínimo:

- ventanas superpuestas;
- datos excluidos;
- interrupciones o faltantes;
- tratamiento de valores atípicos;
- desviaciones frente al procedimiento interno;
- cualquier condición que pueda afectar la interpretación del resultado.
