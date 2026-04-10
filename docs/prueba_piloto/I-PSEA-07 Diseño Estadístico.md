# I-PSEA-07 — Diseño Estadístico

**Código:** I-PSEA-07  
**Nivel:** 3b — Instructivo Técnico  
**Estado:** skeleton ← en redacción  
**Versión:** 0.1-draft  
**Cláusulas ISO/IEC 17043:2023:** 7.2.2; ISO 13528:2022 §4–5  
**Oleada:** 1  
**Prioridad:** 🔴 Crítica  
**Depende de:** P-PSEA-06 (marco estadístico), I-PSEA-08 (x_pt y u(x_pt))  
**Alimenta a:** F-PSEA-14 (hoja de cálculo estadístico), aplicativo R/Shiny

---

## 1. Objeto

> **Instrucción:** Describir que este instructivo operacionaliza P-PSEA-06 con los pasos concretos del diseño estadístico de cada ronda. Responder: ¿qué decide el estadístico con este documento y cuándo?

[TEXTO]

---

## 2. Alcance

> **Instrucción:** Indicar que aplica a todas las rondas del esquema CALAIRE-EA. Mencionar las condiciones especiales de la prueba piloto (n reducido: 1–2 participantes por ronda).

[TEXTO]

---

## 3. Documentos de referencia

| Código / Norma | Título | Sección relevante |
|---|---|---|
| ISO/IEC 17043:2023 | Ensayos de aptitud para laboratorios | 7.2.2 |
| ISO 13528:2022 | Métodos estadísticos para EA | §4, §5, §7, Anexo C |
| P-PSEA-06 | Procedimiento de Diseño Estadístico | Todo |
| I-PSEA-08 | Valor Asignado | x_pt, u(x_pt) |
| I-PSEA-13 | Validación de Software | Aplicativo R/Shiny |
| F-PSEA-06 | Plan de Ronda EA | Analitos, niveles, n previsto |

---

## 4. Definiciones y abreviaturas

| Término | Definición |
|---|---|
| σ_pt | Desviación estándar para evaluación de desempeño (aptitud para el propósito) |
| δ_E | Diferencia mínima de desempeño esperada (base para calcular σ_pt) |
| x_pt | Valor asignado del ítem PT (ver I-PSEA-08) |
| u(x_pt) | Incertidumbre estándar del valor asignado |
| n | Número de resultados válidos de participantes en la ronda |
| z-score | Indicador de desempeño cuando u(x_pt) < 0,3·σ_pt |
| z'-score | Indicador de desempeño cuando u(x_pt) ≥ 0,3·σ_pt (incluye u(x_pt)) |
| ζ-score | Indicador cuando participante reporta incertidumbre expandida U_lab |
| Algoritmo A | Promedio y desviación estándar robustos (ISO 13528 §7.7) para n ≥ ~7 |
| NIQR | Rango intercuartílico normalizado (alternativa robusta para n bajo) |
| MADe | Mediana de desviaciones absolutas escalada (alternativa para n muy bajo) |

---

## 5. Responsabilidades

| Rol | Responsabilidad en este instructivo |
|---|---|
| Estadístico | Ejecutar todos los pasos del diseño; documentar decisiones en F-PSEA-14 |
| Coordinador EA | Aprobar los parámetros estadísticos antes de iniciar la ronda |
| Ingeniero Operativo | Suministrar valores de x_pt y condiciones del ítem (I-PSEA-08) |

---

## 6. Procedimiento

> **Nota general para el redactor:** Este instructivo se ejecuta **antes de cada ronda**, en dos momentos: (A) diseño previo (pasos 6.1–6.3) y (B) cálculo post-ronda (pasos 6.4–6.5). Marcar claramente en el texto a cuál momento corresponde cada paso.

---

### 6.1 Paso 1 — Definición de σ_pt (pre-ronda)

> **Instrucción:** Describir el procedimiento para calcular σ_pt según la fórmula de aptitud para el propósito prescrita en P-PSEA-06. Incluir la fórmula, los valores de a% y b% para cada analito, y cómo se documenta.

**Fórmula:**

```
σ_pt = δ_E = max( a% × x_pt ,  b% × span )
```

> **Instrucción:** Completar la siguiente tabla con los valores de a%, b% y span para cada analito, según lo definido en P-PSEA-06 y la normativa US-EPA aplicable.

| Analito | a (%) | b (%) | Span de referencia | Observaciones |
|---|---|---|---|---|
| CO | | | | |
| SO₂ | | | | |
| O₃ | | | | |
| NO | | | | |
| NO₂ | | | | |

**Pasos:**
1. Obtener x_pt preliminar de I-PSEA-08 (valor asignado calculado o estimado)
2. Calcular σ_pt = max(a% × x_pt, b% × span)
3. Registrar σ_pt en F-PSEA-06 (Plan de Ronda, campo "σ_pt aprobado")
4. Verificar que u(x_pt) ≤ 0,3 × σ_pt (condición de trazabilidad; ver I-PSEA-08)

---

### 6.2 Paso 2 — Selección del algoritmo estadístico según n (pre-ronda)

> **Instrucción:** Describir cómo se selecciona el método de cálculo del valor de consenso y la dispersión según el número esperado de participantes. Incluir tabla de decisión.

| n esperado | Algoritmo | x_pt consenso | σ_pt consenso | Justificación ISO |
|---|---|---|---|---|
| ≥ 12 | Algoritmo A (§7.7) | Promedio robusto | s* robusto | ISO 13528 §7.7 |
| 5–11 | Mediana | Mediana | NIQR o MADe | ISO 13528 §7.7, nota |
| 2–4 | Mediana | Mediana | MADe o σ_pt prescrito | Piloto: usar σ_pt de fórmula |
| 1 | N/A consenso | x_pt = valor de referencia | σ_pt = valor prescrito | Solo z' o ζ aplicable |

> **Nota para prueba piloto (n=1-2):** En la prueba piloto CALAIRE-EA, n es muy bajo (1–2 participantes por ronda). El valor asignado debe ser **siempre el valor de referencia trazable** (I-PSEA-08 Método 1), y σ_pt el valor prescrito. El score aplicable es z'-score o ζ-score. Documentar esta decisión explícitamente en F-PSEA-14.

---

### 6.3 Paso 3 — Selección del indicador de desempeño (pre-ronda)

> **Instrucción:** Definir qué score se calculará para cada participante según el tipo de x_pt y si se reporta incertidumbre.

| Condición | Score seleccionado | Fórmula |
|---|---|---|
| x_pt trazable, u(x_pt) < 0,3·σ_pt, sin U_lab | z-score | z = (x_lab − x_pt) / σ_pt |
| x_pt trazable, u(x_pt) ≥ 0,3·σ_pt | z'-score | z' = (x_lab − x_pt) / √(σ²_pt + u²(x_pt)) |
| Participante reporta U_lab (k=2) | ζ-score | ζ = (x_lab − x_pt) / √(u²_lab + u²(x_pt)) |

> **Instrucción:** Para la prueba piloto, documentar en F-PSEA-06 qué score se usará y la justificación (con referencia a la cláusula ISO 13528 correspondiente).

---

### 6.4 Paso 4 — Criterios de decisión (aplicar post-ronda)

> **Instrucción:** Copiar o referenciar los criterios de interpretación del score. Incluir también qué hacer con valores extremos (outliers).

| Rango del |score| | Clasificación | Acción recomendada |
|---|---|---|
| |score| ≤ 2 | ✅ Satisfactorio | Ninguna |
| 2 < |score| ≤ 3 | ⚠️ Cuestionable | Investigar causa; no acción obligatoria |
| |score| > 3 | ❌ No satisfactorio | Notificar participante; solicitar acción correctiva |

> **Instrucción:** Si el score es ζ o z', revisar si los límites ±2 / ±3 siguen siendo apropiados o si se adopta el criterio de En-score (±1 / >1). Documentar la elección y su base normativa.

---

### 6.5 Paso 5 — Configuración del aplicativo R/Shiny (pre-ronda + post-ronda)

> **Instrucción:** Describir paso a paso cómo se configuran los parámetros en el aplicativo R/Shiny antes de la ronda y cómo se ejecuta el análisis después. Incluir:
> - Dónde se ingresan: analito, n, x_pt, u(x_pt), σ_pt, algoritmo seleccionado, tipo de score
> - Cómo se carga el archivo de resultados de participantes (formato, nombre de columnas)
> - Qué salidas genera el aplicativo (tabla z-scores, gráfico de Youden/Norfolk, informe)
> - Validación de la corrida (ver I-PSEA-13)

**Pre-ronda — configuración:**

| Campo en aplicativo | Fuente del valor |
|---|---|
| Analito | F-PSEA-06 |
| Código de ronda | F-PSEA-06 |
| x_pt | I-PSEA-08 |
| u(x_pt) | I-PSEA-08 |
| σ_pt | §6.1 de este instructivo |
| Algoritmo | §6.2 de este instructivo |
| Tipo de score | §6.3 de este instructivo |

**Post-ronda — ejecución:**

1. Importar archivo de resultados de participantes (formato: _________; columnas: código_participante, resultado, unidad, u_lab)
2. Ejecutar módulo de cálculo → verificar salida vs. cálculo manual de al menos 1 z-score (ver I-PSEA-13, criterio tolerancia ≤ 1×10⁻⁹)
3. Exportar tabla de scores y gráficos para F-PSEA-14

---

## 7. Criterios de aceptación del diseño estadístico

| Verificación | Criterio | ¿Quién verifica? |
|---|---|---|
| σ_pt calculado correctamente | Reproducible por cálculo manual independiente | Coordinador EA |
| u(x_pt) ≤ 0,3 × σ_pt | Verificado en F-PSEA-14, campo "condición u(x_pt)" | Estadístico |
| Algoritmo seleccionado documentado | En F-PSEA-06 con justificación | Estadístico |
| Score seleccionado documentado | En F-PSEA-06 con justificación | Estadístico |
| Aplicativo R/Shiny validado | I-PSEA-13 completado para esta versión del software | Estadístico |

---

## 8. Registros generados

| Formato | Descripción | Cuándo |
|---|---|---|
| F-PSEA-06 | Plan de ronda (incluye decisiones estadísticas pre-ronda) | Antes de la ronda |
| F-PSEA-14 | Hoja de cálculo y aprobación estadística | Post-ronda |
| Salidas R/Shiny | Tabla z-scores, gráficos, informe automático | Post-ronda |

---

## 9. Caso especial — Prueba piloto CALAIRE-EA (n=1-2)

> **Instrucción:** Redactar esta sección como guía específica para la prueba piloto, reconociendo las limitaciones estadísticas de n bajo y documentando las decisiones tomadas.

Dado que la prueba piloto opera con n=1 (Ronda Simple: solo P1-SIATA) y n=2 (Ronda Compleja F1: P1+P2), se aplican las siguientes decisiones:

| Ronda | n | Método x_pt | Método σ_pt | Score | Justificación |
|---|---|---|---|---|---|
| Ronda Simple (CO/SO₂) | 1 | Referencia trazable (I-PSEA-08 M1) | σ_pt prescrito (fórmula) | z' o ζ | n=1: solo verificación de desempeño relativo a referencia |
| Ronda Compleja F1 (O₃/NO/NO₂) | 2 | Referencia trazable | σ_pt prescrito | z' o ζ | n=2: consenso no estadísticamente válido |
| Ronda Compleja F2 (CO/SO₂) | 1 | Referencia trazable | σ_pt prescrito | z' o ζ | Misma justificación que Ronda Simple |

> **Nota:** Los resultados de la prueba piloto son formativos, no normativos. El objetivo es validar el sistema operativo, no evaluar definitivamente la competencia de los laboratorios. Comunicar esto a participantes (ver P-PSEA-20).

---

## Control de versiones

| Versión | Fecha | Descripción del cambio | Elaboró | Revisó | Aprobó |
|---|---|---|---|---|---|
| 0.1 | [FECHA] | Skeleton inicial | [Nombre] | — | — |
| 1.0 | [FECHA] | Versión aprobada para prueba piloto | [Nombre] | [Nombre] | [Nombre] |
