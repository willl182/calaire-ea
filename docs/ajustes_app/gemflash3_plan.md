# Plan de Implementación - Ajustes Estadísticos (GemFlash3)

Este plan detalla las acciones necesarias para corregir los errores de cálculo estadístico y mejorar la gestión de datos en el aplicativo, basándose en la revisión técnica del 23 de febrero de 2026.

## 1. Correcciones de Cálculos Estadísticos (ISO 13528:2022)

### 1.1. Ajuste en Cálculo de Homogeneidad ($s_s$)
*   **Problema:** Error en la fórmula B.10 cuando el valor dentro de la raíz cuadrada es negativo.
*   **Acción:** Implementar la lógica de seguridad según la norma:
    *   Fórmula: $s_s^2 = s_x^2 - (s_w^2 / m)$
    *   **Condicional:** Si $s_s^2 < 0$, entonces asignar $s_s = 0$.
*   **Validación:** Probar con los datos de la revisión donde el aplicativo actualmente arroja "Err:502".

### 1.2. Reestructuración del Cálculo MADe
*   **Problema:** El cálculo está utilizando datos de homogeneidad en lugar de datos de participantes y presenta discrepancias numéricas.
*   **Acción:** 
    *   Cambiar la fuente de datos a la tabla de **Resultados de Participantes**.
    *   Revisar la fórmula de la Mediana de las Diferencias Absolutas para asegurar que coincida con el valor esperado (0.041 para el set de prueba).
    *   Asegurar que el factor de escala (normalmente 1.4826) esté correctamente aplicado.

### 1.3. Implementación/Ajuste de Algoritmo A
*   **Problema:** Falta validación y claridad sobre cuándo aplicar el Algoritmo A.
*   **Acción:** 
    *   Implementar el Algoritmo A (media robusta y desviación estándar robusta) para procesar datos de participantes cuando $n > 10$.
    *   Integrar este algoritmo como alternativa al MADe/niRQ según la cantidad de datos.

## 2. Mejoras en Gestión y Visualización de Datos

### 2.1. Módulos Independientes de Carga (UI/UX)
*   **Acción:** Crear secciones separadas y claramente etiquetadas en la interfaz para la carga de:
    1.  Datos de Homogeneidad.
    2.  Datos de Estabilidad.
    3.  Resultados de Participantes.
*   **Objetivo:** Eliminar la confusión actual donde se mezclan los datos de homogeneidad con los de la ronda.

### 2.2. Tablas de Trazabilidad de Cálculos
*   **Acción:** Implementar una vista de "Detalle de Cálculos" que muestre:
    *   Valores intermedios (medianas, diferencias absolutas, desviaciones).
    *   Fórmulas aplicadas en cada paso.
*   **Objetivo:** Facilitar la validación manual por parte de los expertos sin depender únicamente del resultado final.

### 2.3. Mejora en Exportación para Validación
*   **Acción:** Optimizar el formato CSV/Excel de exportación para que las columnas sean legibles y sigan el orden lógico de los cálculos realizados en el aplicativo.

## 3. Cronograma Sugerido

| Fase | Tarea | Prioridad |
| :--- | :--- | :--- |
| **Fase 1** | Corrección fórmula Homogeneidad ($s_s$) | Crítica |
| **Fase 2** | Cambio de fuente MADe (Participantes) y corrección fórmula | Crítica |
| **Fase 3** | Implementación/Validación Algoritmo A | Alta |
| **Fase 4** | Rediseño de módulos de carga y tablas de trazabilidad | Media |
| **Fase 5** | Pruebas de aceptación con datos del informe de revisión | Alta |

## 4. Criterios de Aceptación
1.  El cálculo de $s_s$ no debe generar errores cuando la varianza entre muestras es menor a la varianza dentro de las muestras.
2.  El valor de MADe debe coincidir exactamente con las hojas de validación externas (ej. 0.041 con el set de datos 1).
3.  Los datos de los participantes deben estar claramente diferenciados de los datos de control (homogeneidad/estabilidad) en toda la plataforma.
