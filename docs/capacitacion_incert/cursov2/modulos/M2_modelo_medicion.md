# M2 — Modelo de medición: fotometría UV y Beer–Lambert

## 1. Ficha

**Título:** M2 — Modelo de medición: fotometría UV y Beer–Lambert  
**Duración total:** 48 min  
**Distribución:** exposición guiada, 36 min; ejercicio de sensibilidad y especificación del mensurando, 12 min.  
**Posición en la jornada:** segundo módulo del curso, inmediatamente después de M1 y antes de la introducción sistemática a los conceptos GUM de M3.  
**Prerrequisito:** M1, en particular la distinción entre mensurando, referencia, instrumento y cadena de trazabilidad.  
**Materiales:** diapositiva o pizarra para las ecuaciones; calculadora básica; hoja del ejercicio; extractos de 40 CFR 50 Appendix D, NISTIR 6963, JCGM GUM-6:2020 y handout teórico del curso.

**Idea fuerza del módulo:** una ecuación de medición no es solo una fórmula para obtener un número. Es una representación física que permite identificar qué magnitudes influyen, en qué dirección lo hacen y cuánto aporta la incertidumbre de cada una. En fotometría UV, la temperatura, la presión, la longitud óptica y el coeficiente de absorción producen dependencias proporcionales a la fracción molar; el cociente de intensidades entra mediante un logaritmo y requiere especial atención cuando la transmitancia se aproxima a uno.

## 2. Objetivos específicos

Al finalizar el módulo, la persona participante podrá:

1. **Explicar** cómo la disminución de intensidad UV se relaciona con la cantidad de ozono mediante la ley de Beer–Lambert.
2. **Formular** el modelo de fracción molar \(x=-k_BT\ln(D)/(\sigma LP)\), identificando el significado y las unidades de sus magnitudes de entrada.
3. **Derivar** los coeficientes de sensibilidad respecto de \(L\), \(T\), \(P\), \(D\) y \(\sigma\).
4. **Clasificar** fuentes físicas de incertidumbre como aproximadamente constantes o proporcionales a la fracción molar, cuando el modelo y la evidencia sustenten esa clasificación.
5. **Calcular y comparar** las contribuciones estándar asociadas a temperatura y presión en un punto de medición dado.
6. **Redactar** una especificación completa del mensurando y declarar las fronteras del sistema de medición.

## 3. Guion de exposición con tiempos

El libreto de exposición está organizado en páginas/diapositivas Markdown independientes. Cada página conserva el texto dictable, el minutaje y sus apoyos; este apartado funciona como índice.

1. [M2 — Página 01 — 3.1 Subbloque 1 — De la absorción UV al mensurando (0–10 min; acumulado: 10 min)](../paginas/M2_01_3_1_subbloque_1_de_la_absorcion_uv_al_mensurando_010_min_acumulado_10_min.md)
2. [M2 — Página 02 — 3.2 Subbloque 2 — Modelo de fracción molar y condiciones físicas (10–21 min; acumulado: 21 min)](../paginas/M2_02_3_2_subbloque_2_modelo_de_fraccion_molar_y_condiciones_fisicas_1021_min_acumulado_21_min.md)
3. [M2 — Página 03 — 3.3 Subbloque 3 — Coeficientes de sensibilidad (21–29 min; acumulado: 29 min)](../paginas/M2_03_3_3_subbloque_3_coeficientes_de_sensibilidad_2129_min_acumulado_29_min.md)
4. [M2 — Página 04 — 3.4 Subbloque 4 — Fuentes físicas y componentes constantes o proporcionales (29–36 min; acumulado: 36 min)](../paginas/M2_04_3_4_subbloque_4_fuentes_fisicas_y_componentes_constantes_o_proporcionales_2936_min_acumulado_36_min.md)

## 4. Ejercicio/actividad

**Título:** Sensibilidad de la fracción molar a temperatura y presión  
**Tiempo:** 12 min, del minuto 36 al 48.  
**Organización sugerida:** 2 min para especificar mensurando y fronteras; 5 min de cálculo individual; 3 min de comparación en parejas; 2 min de puesta en común.

**Enunciado completo:** Para una medición de fracción molar, calcule los coeficientes de sensibilidad respecto de temperatura y presión y sus contribuciones estándar. Interprete el signo de cada coeficiente y compare las magnitudes obtenidas. La comparación debe hacerse después de convertir ambas incertidumbres de entrada a la unidad del mensurando.

**Datos de entrada:**

- \(x=100\ \text{nmol/mol}\)
- \(T=298.15\ \text{K}\)
- \(P=101.325\ \text{kPa}\)
- \(u(T)=0.15\ \text{K}\)
- \(u(P)=0.05\ \text{kPa}\)
- \(c_T=x/T\)
- \(c_P=-x/P\)
- \(u_T(x)=|c_T|u(T)\)
- \(u_P(x)=|c_P|u(P)\)

**Tareas:**

1. Calcule \(c_T\) en \(\text{nmol mol}^{-1}\text{K}^{-1}\).
2. Calcule \(c_P\) en \(\text{nmol mol}^{-1}\text{kPa}^{-1}\).
3. Calcule \(u_T(x)\) y \(u_P(x)\) en \(\text{nmol/mol}\).
4. Explique por qué \(c_T\) es positivo y \(c_P\) es negativo.
5. Indique cuál contribución es mayor y si la diferencia es relevante para este ejemplo.
6. Complete esta frase: «fracción molar de O₃ en ________, atribuida al punto ________, expresada en ________, obtenida mediante ________ y promediada durante ________; línea, filtro, acondicionamiento y representatividad quedan [incluidos/excluidos]».
7. Indique si los valores de T y P representan el sensor, el gas real dentro de la celda o ambos; anote la evidencia o el vacío.
8. Añada una fuente que no aparezca explícita en la ecuación básica e indique si entraría como factor unitario, término aditivo u otra entrada del modelo.

**Recurso opcional para comprobar sensibilidades:** QUAM App. E.2 propone perturbar una entrada en \(u(x_i)\), recalcular la salida y comparar el cambio con \(|c_i|u(x_i)\). Esta comprobación por hoja de cálculo ayuda cuando las derivadas son menos accesibles, pero no reemplaza la derivación principal (QUAM App. E.2, pp. editoriales 106–107; PDF pp. 112–113).

**Resultado esperado, en una línea:** \(c_T\approx0.335\ \text{nmol mol}^{-1}\text{K}^{-1}\), \(c_P\approx-0.987\ \text{nmol mol}^{-1}\text{kPa}^{-1}\), \(u_T\approx0.0503\ \text{nmol/mol}\), \(u_P\approx0.0494\ \text{nmol/mol}\); las magnitudes son similares.

## 5. Errores frecuentes y preguntas típicas

1. **¿Se puede usar temperatura en grados Celsius dentro del modelo?** No. La ecuación requiere temperatura termodinámica expresada en kelvin.
2. **¿El signo negativo de \(c_P\) significa incertidumbre negativa?** No. El signo indica la dirección del cambio de \(x\); la incertidumbre estándar y la magnitud de la contribución son no negativas.
3. **¿El valor nominal de la longitud de la celda siempre es \(L\)?** No necesariamente. Debe representar la longitud óptica efectiva y considerar la corrección aplicable por pérdidas.
4. **¿La mayor incertidumbre numérica de entrada produce siempre la mayor contribución?** No. Primero debe multiplicarse cada incertidumbre por su coeficiente de sensibilidad y comparar en la unidad de salida.
5. **¿Basta escribir “concentración de ozono” como mensurando?** No. Deben declararse especie, matriz, punto físico, unidad, condiciones, procedimiento, promedio y fronteras pertinentes.
6. **¿Todos los efectos son proporcionales a la fracción molar?** No. Los efectos de escala suelen ser proporcionales, mientras que la resolución, el ruido o el cero pueden comportarse aproximadamente como componentes constantes en un intervalo definido.

## 6. Cierre y transición al M3

El modelo físico nos permitió identificar magnitudes de entrada, signos y factores de conversión hacia la fracción molar. En M3 se usará esta estructura para asignar incertidumbres estándar a las magnitudes de entrada, distinguir evaluaciones Tipo A y Tipo B y comenzar a construir un presupuesto de incertidumbre defendible.
