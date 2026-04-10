# I-PSEA-13 — Validación de Software y Sistemas

**Código:** I-PSEA-13  
**Nivel:** 3b — Instructivo Técnico  
**Estado:** skeleton ← en redacción  
**Versión:** 0.1-draft  
**Cláusulas ISO/IEC 17043:2023:** 7.5.2; ISO 13528:2022 §4.2, 5.5  
**Oleada:** 1  
**Prioridad:** 🔴 Crítica — brecha identificada en evaluación del SGC  
**Depende de:** I-PSEA-07 (algoritmos a validar), I-PSEA-08 (cálculos a verificar)  
**Alimenta a:** F-PSEA-20 (Protocolo de Validación de Software), aplicativo R/Shiny en producción

---

## 1. Objeto

> **Instrucción:** Describir que este instructivo establece el proceso de validación formal del aplicativo R/Shiny (y cualquier script auxiliar) usado en el cálculo estadístico del esquema CALAIRE-EA, conforme a 17043:2023 §7.5.2. Incluir que la validación es obligatoria antes del primer uso y ante cada cambio funcional.

[TEXTO]

---

## 2. Alcance

> **Instrucción:** Especificar qué software cubre: aplicativo R/Shiny de análisis estadístico, scripts R auxiliares, y herramientas de verificación cruzada (Python). Indicar qué queda fuera de alcance (ej. software de analizadores de campo de los participantes).

[TEXTO]

---

## 3. Documentos de referencia

| Código / Norma | Título | Sección relevante |
|---|---|---|
| ISO/IEC 17043:2023 | Ensayos de aptitud para laboratorios | 7.5.2 (equipos y software) |
| ISO 13528:2022 | Métodos estadísticos para EA | §4.2, §5.5, Anexo C (ejemplos numéricos) |
| EURACHEM/CITAC Guide | Software Used in Analytical Laboratories | Todo |
| I-PSEA-07 | Diseño Estadístico | Algoritmos a validar |
| I-PSEA-08 | Valor Asignado | Cálculos de x_pt y u(x_pt) |
| F-PSEA-20 | Protocolo de Validación de Software | Registro del expediente |

---

## 4. Definiciones y abreviaturas

| Término | Definición |
|---|---|
| Aplicativo | Software R/Shiny desarrollado por CALAIRE-EA para cálculos estadísticos |
| Dataset de referencia | Conjunto de datos con resultados conocidos para verificar los cálculos del software |
| Tolerancia numérica | Diferencia máxima aceptable entre resultado del software y valor de referencia (≤ 1×10⁻⁹) |
| Validación cruzada | Ejecución del mismo cálculo en dos implementaciones independientes (R y Python) |
| Expediente de validación | Conjunto de documentos que evidencian la validación: plan, ejecución, resultados |
| Revalidación | Validación repetida tras cambios en el software o su entorno de ejecución |
| Control de versiones | Sistema de gestión de cambios al código fuente (ej. git) |
| Bug | Error en el software que produce un resultado incorrecto o un fallo de ejecución |

---

## 5. Responsabilidades

| Rol | Responsabilidad |
|---|---|
| Estadístico | Ejecutar el plan de validación; documentar en F-PSEA-20; autorizar la versión para uso |
| Desarrollador R/Shiny | Suministrar el código fuente, documentación técnica y registro de cambios |
| Coordinador EA | Aprobar el expediente de validación antes de que el software entre en producción |

---

## 6. Procedimiento

### 6.1 Paso 1 — Especificación de requisitos del software

> **Instrucción:** Documentar qué debe hacer el aplicativo. Esta lista de requisitos es la base del plan de pruebas. Incluir:
> - Funciones estadísticas que debe implementar
> - Formatos de entrada y salida
> - Requisitos de trazabilidad (qué debe quedar en el log/informe del aplicativo)

**Requisitos funcionales mínimos:**

| # | Requisito | Referencia normativa |
|---|---|---|
| RF-01 | Calcular promedio robusto y s* mediante Algoritmo A (ISO 13528 §7.7) | ISO 13528 §7.7 |
| RF-02 | Calcular mediana y NIQR/MADe para n bajo | ISO 13528 §7.7 |
| RF-03 | Calcular z-score, z'-score y ζ-score | ISO 13528 §5.3–5.5 |
| RF-04 | Clasificar desempeño según |score| ≤ 2 / 2–3 / >3 | ISO 13528 §5.3 |
| RF-05 | Generar tabla resumen de resultados con códigos de participantes | ISO/IEC 17043 §7.4.3 |
| RF-06 | Generar gráfico de Norfolk (z-score por participante) | Buena práctica EA |
| RF-07 | Exportar informe en formato reproducible (HTML/PDF/CSV) | ISO/IEC 17043 §7.4 |
| RF-08 | Registrar en log: versión del software, fecha, parámetros de entrada, usuario | ISO/IEC 17043 §7.5.2 |

> **Instrucción:** Agregar requisitos no funcionales (rendimiento, compatibilidad de SO, R version mínima requerida, dependencias de paquetes con versiones fijadas).

---

### 6.2 Paso 2 — Preparación del plan de pruebas

> **Instrucción:** Definir, antes de ejecutar, qué se va a probar, con qué datos y cuál es el resultado esperado para cada prueba. Registrar en F-PSEA-20.

**Tipos de prueba:**

| Tipo | Descripción | Fuente de datos |
|---|---|---|
| Prueba de exactitud numérica | Comparar resultado del software con cálculo manual o referencia publicada | ISO 13528 Anexo C; cálculo manual con hoja de cálculo independiente |
| Prueba de casos límite | Probar con n mínimo (n=1, n=2), valores iguales, un outlier extremo | Datasets sintéticos construidos por el estadístico |
| Prueba de formato de entrada | Cargar archivos con formatos válidos e inválidos | Archivos de prueba diseñados |
| Prueba de clasificación | Verificar que los scores limítrofes (|z|=2,0 y |z|=3,0) clasifican correctamente | Datos calculados hacia atrás desde los límites |
| Prueba de reproducibilidad | Ejecutar el mismo análisis dos veces y verificar resultados idénticos | Mismo dataset |
| Validación cruzada R/Python | Ejecutar en Python con la misma lógica y comparar resultados | Dataset compartido |

---

### 6.3 Paso 3 — Datasets de referencia

> **Instrucción:** Preparar al menos 3 datasets de referencia con resultados conocidos. Usar los ejemplos del Anexo C de ISO 13528:2022 como base.

**Dataset obligatorio — ISO 13528:2022 Anexo C:**

> **Instrucción:** Transcribir o referenciar los datos del Anexo C de ISO 13528. Incluir los valores de x_pt, σ_pt, resultados de participantes y los scores esperados. Estos son la referencia primaria de aceptación.

| Dataset | Origen | Algoritmo cubierto | Scores esperados disponibles |
|---|---|---|---|
| DS-01 | ISO 13528:2022 Anexo C, Ejemplo 1 | Algoritmo A, z-score | Sí — en la norma |
| DS-02 | ISO 13528:2022 Anexo C, Ejemplo 2 | Algoritmo A, z-score | Sí — en la norma |
| DS-03 | Sintético: n=2 (prueba piloto) | Mediana, z'-score | Calculado manualmente |
| DS-04 | Sintético: un outlier fuerte (|z|=5) | Algoritmo A | Calculado manualmente |
| DS-05 | Sintético: n=1 | Solo z'-score con x_pt de referencia | Calculado manualmente |

---

### 6.4 Paso 4 — Ejecución de pruebas y registro de evidencias

> **Instrucción:** Para cada prueba del plan (§6.2), ejecutarla, registrar la salida del aplicativo y comparar contra el valor de referencia. Documentar en F-PSEA-20.

**Para cada prueba:**

1. Cargar el dataset de referencia en el aplicativo
2. Configurar los parámetros (x_pt, σ_pt, algoritmo, tipo de score)
3. Ejecutar el análisis
4. Registrar: captura de pantalla o exportación del resultado
5. Calcular diferencia: Δ = |resultado_software − valor_referencia|
6. Verificar criterio: **Δ ≤ 1×10⁻⁹** para cálculos numéricos

**Criterio de aceptación por prueba:**

| Tipo de verificación | Criterio de aceptación |
|---|---|
| Exactitud numérica (scores) | Δ ≤ 1×10⁻⁹ (relativo o absoluto, el más estricto aplicable) |
| Clasificación de desempeño | 100% correcto en todos los datasets |
| Formato de salida | Informe generado contiene todos los campos de RF-05 a RF-08 |
| Reproducibilidad | Resultados idénticos en 2 ejecuciones consecutivas |
| Validación cruzada R/Python | Diferencia ≤ 1×10⁻⁶ entre implementaciones |

---

### 6.5 Paso 5 — Validación cruzada R vs. Python

> **Instrucción:** Describir el proceso de verificación independiente. Un segundo implementador (o el mismo con lenguaje diferente) reproduce los cálculos estadísticos clave en Python y compara los resultados. Documentar el código Python usado en F-PSEA-20.

**Funciones a verificar en Python (numpy/scipy):**

| Función | Equivalente R | Dataset | Tolerancia |
|---|---|---|---|
| Algoritmo A (promedio robusto) | robustbase::hubers o implementación propia | DS-01, DS-02 | ≤ 1×10⁻⁶ |
| Mediana y NIQR | numpy.median, scipy.stats.iqr | DS-03 | ≤ 1×10⁻⁹ |
| z-score | Cálculo directo | DS-01..DS-05 | ≤ 1×10⁻⁹ |

> **Instrucción:** Adjuntar el script Python como anexo en F-PSEA-20.

---

### 6.6 Paso 6 — Documentación de resultados, bugs y correcciones

> **Instrucción:** Si durante las pruebas se detectan discrepancias o fallas, documentarlas como bugs. Para cada bug: descripción, dataset que lo reproduce, resultado obtenido vs. esperado, severidad, estado (pendiente/resuelto), versión en que se resolvió.

| ID Bug | Descripción | Dataset | Resultado obtenido | Resultado esperado | Severidad | Estado |
|---|---|---|---|---|---|---|
| BUG-01 | [Descripción] | DS-___ | ___ | ___ | [Crítica/Mayor/Menor] | [Pendiente/Resuelto en v___] |

> **Instrucción:** Bugs de severidad Crítica o Mayor deben resolverse **antes** de aprobar la versión para producción.

---

### 6.7 Paso 7 — Control de versiones del aplicativo

> **Instrucción:** Describir el esquema de versionado del aplicativo y los requisitos de trazabilidad.

**Requisitos:**

- El código fuente del aplicativo debe estar bajo control de versiones (ej. git)
- Cada versión en producción debe tener un tag/release identificable
- El log de ejecución del aplicativo debe registrar la versión usada en cada análisis
- Cambios al código deben documentarse en un CHANGELOG antes del despliegue

| Versión aplicativo | Fecha | Cambios principales | Estado validación |
|---|---|---|---|
| v___ | [FECHA] | [Descripción] | [En validación / Aprobado / Obsoleto] |

---

### 6.8 Paso 8 — Revalidación ante cambios

> **Instrucción:** Especificar qué tipo de cambios obligan a revalidar totalmente (Tipo A) vs. qué cambios requieren solo pruebas de regresión parciales (Tipo B).

| Tipo de cambio | Nivel de revalidación requerido |
|---|---|
| Cambio en algoritmo estadístico | Tipo A — Revalidación completa (§6.3–6.6) |
| Actualización de paquetes R/Python con posible impacto numérico | Tipo A — Revalidación completa |
| Cambio en interfaz gráfica (sin afectar cálculos) | Tipo B — Pruebas de regresión de RF-05 a RF-08 |
| Actualización de dependencias sin impacto numérico | Tipo B — Pruebas de reproducibilidad |
| Migración de SO o versión de R | Tipo A — Revalidación completa |

---

## 7. Criterios de aceptación del proceso de validación

| Verificación | Criterio | ¿Cumple? |
|---|---|---|
| Plan de pruebas documentado antes de ejecución | F-PSEA-20 §Plan firmado antes de ejecución | [ ] |
| 100% de pruebas ejecutadas | Sin pruebas omitidas (justificar si alguna no aplica) | [ ] |
| 0 bugs de severidad Crítica o Mayor pendientes | Todos resueltos y revalidados | [ ] |
| Validación cruzada R/Python completada | Script Python adjunto en F-PSEA-20 | [ ] |
| Expediente F-PSEA-20 aprobado y firmado | Coordinador EA firma autorización de producción | [ ] |

---

## 8. Registros generados

| Formato | Descripción | Cuándo |
|---|---|---|
| F-PSEA-20 | Protocolo de Validación de Software — expediente completo | Antes de poner el aplicativo en producción |
| Log del aplicativo | Registro automático de cada ejecución (fecha, versión, parámetros) | En cada uso productivo |

---

## Control de versiones

| Versión | Fecha | Descripción del cambio | Elaboró | Revisó | Aprobó |
|---|---|---|---|---|---|
| 0.1 | [FECHA] | Skeleton inicial | [Nombre] | — | — |
| 1.0 | [FECHA] | Versión aprobada para prueba piloto | [Nombre] | [Nombre] | [Nombre] |
