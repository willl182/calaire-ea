# Plan de Implementación: Ajustes al Aplicativo Estadístico (Revisión 2)

Basado en el "Informe No. 2 de revision" (2026-02-23), se proponen las siguientes acciones de implementación para corregir los cálculos y mejorar la experiencia de usuario en el aplicativo. Este plan se enfoca en la lógica de negocio y la interfaz, sin estar atado a una arquitectura de código específica por el momento.

## 1. Correcciones en Cálculos Estadísticos

### 1.1. Cálculo de Homogeneidad (Varianza entre muestras - $s_s$)
*   **Problema reportado:** La fórmula actual utiliza un valor absoluto de manera incorrecta cuando la resta para hallar la varianza da un valor negativo, contraviniendo la ISO 13528:2022 (Fórmula B.10).
*   **Acción:** 
    *   Remover cualquier función de valor absoluto en el paso previo a la raíz cuadrada.
    *   Implementar la condición normativa estricta: Si la varianza entre muestras calculada ($s_s^2$) es menor que cero ($< 0$), entonces la desviación estándar entre muestras ($s_s$) debe asignarse como cero ($0$).

### 1.2. Origen de Datos para Medidas de Dispersión
*   **Problema reportado:** El aplicativo está utilizando los datos de homogeneidad para calcular la desviación estándar (MADe, nIQR, Algoritmo A), cuando debería usar los datos de los participantes.
*   **Acción:** Redirigir el flujo de datos para que todas las métricas de desviación estándar para la evaluación de desempeño (MADe, nIQR, Algoritmo A) consuman estrictamente la matriz de **datos de los participantes**.

### 1.3. Lógica de Selección de Algoritmo de Dispersión
*   **Problema reportado:** Falta de claridad o implementación de la regla de cantidad de participantes para el Algoritmo A.
*   **Acción:** Implementar o verificar la regla de negocio que condicione el estadístico a usar: Si la cantidad de datos (participantes) es **mayor o igual a 12**, el sistema debe aplicar automáticamente el **Algoritmo A**.

### 1.4. Corrección de Mapeo de Columnas (Bug específico)
*   **Problema reportado:** Se evidenció un cruce donde el cálculo de la mediana se hizo con "DATOS 1", pero el ejercicio usaba la información de "Datos 2".
*   **Acción:** Revisar y corregir la lógica de iteración o indexación de columnas en las rutinas estadísticas para garantizar que los cálculos por iteración/corrida se apliquen a la columna de datos correspondiente de principio a fin.

---

## 2. Mejoras en la Interfaz de Usuario (UI/UX)

### 2.1. Segmentación en la Carga de Datos
*   **Problema reportado:** Es difícil entender el proceso de carga actual (todo combinado).
*   **Acción:** Crear espacios, pestañas o formularios claramente separados en la interfaz web para cargar de forma independiente:
    1.  Datos de entrada para Homogeneidad.
    2.  Datos de entrada para Estabilidad.
    3.  Datos de los participantes.

---

## 3. Mejoras en la Exportación y Auditoría de Datos

### 3.1. Tablas de Resumen de Cálculos (En pantalla)
*   **Problema reportado:** Es confuso observar qué datos exactos está tomando el aplicativo para hacer las corridas y cálculos.
*   **Acción:** Desarrollar una vista (tabla de resultados detallados) dentro de la aplicación donde el usuario pueda visualizar claramente los datos crudos y resultados intermedios de los cálculos realizados.

### 3.2. Formato de Exportación (Descargables)
*   **Problema reportado:** El archivo de validación que se descarga (CSV) no tiene un formato tabular claro, presenta errores de codificación (caracteres extraños como ``) y su estructura (ej: `co,corrida_1,0-mol/mol,1,1,0.0067...`) es difícil de llevar a Excel para validación cruzada.
*   **Acción:** 
    *   Estandarizar el exportador CSV/Excel con encabezados de columna claros.
    *   Sanitizar la codificación de caracteres (usar UTF-8 con BOM o exportar directamente a formato `.xlsx` de ser posible) para evitar problemas con las unidades de medida.
    *   Estructurar el archivo en formato de tabla (columnas de: Magnitud, Corrida, Identificador, Unidad, Valor, etc.).

---

## 4. Tareas de Soporte y Validación (Inmediatas)

*   **Acción:** Extraer de manera manual o a través de un script temporal los datos exactos que el aplicativo utilizó internamente para el cálculo del **Algoritmo A** y compartirlos con la revisora, para que ella pueda completar su validación manual en Excel.
*   **Estado de confirmación:** Confirmar internamente que los módulos de **Estabilidad** y **niRQ** no requieren refactorización en sus fórmulas matemáticas, ya que fueron reportados como correctos.