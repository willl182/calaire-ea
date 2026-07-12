# I-PSEA-08 — Valor Asignado

**Código:** I-PSEA-08  
**Nivel:** 3b — Instructivo Técnico  
**Estado:** skeleton ← en redacción  
**Versión:** 0.1-draft  
**Cláusulas ISO/IEC 17043:2023:** 7.2.3; ISO 13528:2022 §7  
**Oleada:** 1  
**Prioridad:** 🔴 Crítica  
**Depende de:** I-PSEA-02 (ítem generado), datos del CRM vigente  
**Alimenta a:** I-PSEA-07 (x_pt y u(x_pt) para diseño estadístico), F-PSEA-14

---

## 1. Objeto

> **Instrucción:** Describir que este instructivo establece la jerarquía de métodos y el procedimiento de cálculo para determinar el valor asignado (x_pt) y su incertidumbre u(x_pt) en cada ronda de CALAIRE-EA.

[TEXTO]

---

## 2. Alcance

> **Instrucción:** Especificar que aplica a todos los analitos del esquema (CO, SO₂, O₃, NO, NO₂) para rondas in situ. Indicar que el Método 1 (dilución dinámica + CRM) es el método primario para CALAIRE-EA.

[TEXTO]

---

## 3. Documentos de referencia

| Código / Norma | Título | Sección relevante |
|---|---|---|
| ISO/IEC 17043:2023 | Ensayos de aptitud para laboratorios | 7.2.3 |
| ISO 13528:2022 | Métodos estadísticos para EA | §7 |
| ISO 6143 | Mezclas de gas — Métodos de comparación para calibración | Todo |
| JCGM 100:2008 (GUM) | Guía para expresión de incertidumbre de medida | §5 propagación |
| I-PSEA-02 | Producción PT Items | Dilución, CRM, caudales |
| I-PSEA-07 | Diseño Estadístico | Uso de x_pt, u(x_pt) |
| Certificado CRM vigente | Emitido por proveedor (nombre: ___, lote: ___) | Concentración, u_CRM |

---

## 4. Definiciones y abreviaturas

| Término | Definición |
|---|---|
| x_pt | Valor asignado al ítem PT — concentración de referencia entregada al participante |
| u(x_pt) | Incertidumbre estándar combinada del valor asignado |
| C_CRM | Concentración certificada del CRM (valor del certificado) |
| u_CRM | Incertidumbre estándar del CRM = U_CRM / k (donde k=2 normalmente) |
| Q_gas | Caudal volumétrico del gas puro del CRM (entrada al mezclador) |
| Q_diluente | Caudal volumétrico del gas de dilución (aire limpio) |
| Q_total | Caudal total = Q_gas + Q_diluente |
| u_hom | Componente de incertidumbre por homogeneidad del ítem |
| u_stab | Componente de incertidumbre por estabilidad del ítem durante la ronda |
| u_char | Incertidumbre de caracterización (incluye u_CRM, u_flujos) |
| CRM | Material de referencia certificado |
| INM | Instituto Nacional de Metrología (Colombia: INM/INMETRO/NIST para trazabilidad) |

---

## 5. Responsabilidades

| Rol | Responsabilidad |
|---|---|
| Estadístico | Calcular y documentar x_pt y u(x_pt); verificar criterio u(x_pt) ≤ 0,3·σ_pt |
| Ingeniero Operativo | Registrar caudales, condiciones ambientales durante la generación (I-PSEA-02) |
| Coordinador EA | Verificar vigencia del CRM y trazabilidad antes de cada ronda |

---

## 6. Procedimiento

### 6.1 Jerarquía de métodos para x_pt

> **Instrucción:** Explicar que CALAIRE-EA usa primariamente el Método 1. Los métodos 2 y 3 son respaldo o verificación. Nunca usar Método 3 (consenso) como único x_pt en esta etapa del esquema.

| Prioridad | Método | Cuándo se usa | Base normativa |
|---|---|---|---|
| **1 (primario)** | Cálculo metrológico: dilución dinámica + CRM trazable | Siempre — generación in situ | ISO 13528 §7.2, ISO 6143 |
| 2 (verificación) | Confirmación por instrumento de referencia interno | Para validar Método 1 | ISO 13528 §7.3 |
| 3 (no usar solo) | Valor de consenso robusto (resultados de participantes) | Solo como verificación cruzada ex post | ISO 13528 §7.7 |

---

### 6.2 Cálculo de x_pt por dilución dinámica (Método 1)

> **Instrucción:** Describir el modelo matemático de dilución dinámica. Adaptar a la configuración del sistema de CALAIRE (tipo de mezclador, controladores de flujo, etc.). Especificar unidades y número de cifras significativas.

**Modelo:**

```
x_pt = C_CRM × (Q_gas / Q_total)

donde:
  Q_total = Q_gas + Q_diluente
```

> **Instrucción:** Si el sistema de CALAIRE usa controladores másicos (MFC), el caudal se expresa en condiciones estándar. Especificar condiciones de referencia (ej. 20°C, 101,325 kPa). Agregar corrección por T y P ambientales si aplica.

**Ejemplo de cálculo:**

| Parámetro | Símbolo | Valor ejemplo | Unidad |
|---|---|---|---|
| Concentración CRM | C_CRM | ___ | nmol/mol (ppb) o μmol/mol (ppm) |
| Caudal gas CRM | Q_gas | ___ | mL/min (o sccm) |
| Caudal diluyente | Q_diluente | ___ | mL/min |
| Caudal total | Q_total | ___ | mL/min |
| **Valor asignado** | **x_pt** | **___** | **nmol/mol** |

> **Instrucción:** Para cada nivel de concentración de la ronda (ver F-PSEA-06), completar una tabla separada con los caudales configurados en el sistema.

---

### 6.3 Cálculo de u(x_pt) — Modelo de incertidumbre combinada

> **Instrucción:** Describir el modelo de propagación de incertidumbre. El modelo general es:

**Modelo:**

```
u²(x_pt) = u²_char + u²_hom + u²_stab
```

> **Instrucción:** Desarrollar cada componente:

#### 6.3.1 Componente de caracterización u_char

> **Instrucción:** Incluir todas las fuentes de incertidumbre de la cadena de generación:
> - Incertidumbre del CRM: u_CRM = U_CRM / k
> - Incertidumbre de los controladores de flujo Q_gas y Q_diluente (calibración, repetibilidad, resolución)
> - Modelo de propagación por la fórmula de dilución

```
u²_char = (∂x_pt/∂C_CRM)² · u²_CRM + (∂x_pt/∂Q_gas)² · u²(Q_gas) + (∂x_pt/∂Q_diluente)² · u²(Q_diluente)
```

> **Instrucción:** Calcular las derivadas parciales de la fórmula de dilución y expresarlas en función de C_CRM, Q_gas, Q_diluente. Agregar tabla con fuentes de incertidumbre del laboratorio.

| Fuente | Símbolo | Distribución | Valor | u_i |
|---|---|---|---|---|
| Incertidumbre CRM | u_CRM | Normal (k=2) | U_CRM/2 | |
| Controlador flujo gas | u(Q_gas) | Rectangular | especif. / √3 | |
| Controlador flujo diluyente | u(Q_dil) | Rectangular | especif. / √3 | |
| Repetibilidad de flujo | u_rep | Normal | s / √n | |

#### 6.3.2 Componente de homogeneidad u_hom

> **Instrucción:** Usar el resultado de la prueba de homogeneidad (I-PSEA-10, F-PSEA-09):
>
> ```
> u_hom = s_hom / √n_items
> ```
>
> Donde s_hom es la desviación estándar de las n_items atmósferas generadas independientemente.

#### 6.3.3 Componente de estabilidad u_stab

> **Instrucción:** Usar el resultado de la prueba de estabilidad (I-PSEA-10, F-PSEA-10). Si la estabilidad es verificada intrajornada y se considera despreciable relativa a u_char:
>
> ```
> u_stab ≈ |x̄_inicio − x̄_fin| / (2·√3)     [distribución rectangular]
> ```
>
> Documentar si se asume u_stab ≈ 0 y la justificación.

---

### 6.4 Verificación del criterio de trazabilidad

> **Instrucción:** Verificar que la incertidumbre del valor asignado es suficientemente pequeña para que el z-score sea informativo. Si la condición no se cumple, cambiar a z'-score.

**Criterio:**

| Condición | Cumple | Acción |
|---|---|---|
| u(x_pt) ≤ 0,3 × σ_pt | ✅ | Usar z-score ordinario |
| u(x_pt) > 0,3 × σ_pt | ⚠️ | Usar z'-score (incluye u(x_pt) en denominador) |

> **Nota:** El resultado de esta verificación se documenta en F-PSEA-14 y define el tipo de score que usa I-PSEA-07.

---

### 6.5 Trazabilidad al INM/SI

> **Instrucción:** Documentar la cadena de trazabilidad metrológica del CRM usado. Incluir:
> - Nombre del proveedor y número de lote del CRM
> - Organismo de acreditación del proveedor (ISO 17034)
> - Trazabilidad al SI a través del INM nacional o laboratorio de referencia reconocido
> - Fecha de vencimiento del CRM y acciones ante vencimiento

| Campo | Información |
|---|---|
| Proveedor CRM | [Nombre] |
| Número de certificado | [___] |
| Concentración certificada | [___] nmol/mol / μmol/mol |
| Incertidumbre expandida (k=2) | [___] % o nmol/mol |
| Organismo de acreditación del proveedor | [___] (ISO 17034) |
| Trazabilidad declarada al | [NIST / PTB / BIPM / INM Colombia] |
| Fecha de vencimiento | [DD/MM/AAAA] |
| Próximo CRM (si se acerca vencimiento) | [Gestionar con ≥ 3 meses de anticipación] |

---

## 7. Criterios de aceptación

| Verificación | Criterio | Quién verifica |
|---|---|---|
| x_pt calculado y reproducible | Resultado idéntico a cálculo independiente (tolerancia ≤ 0,01%) | Estadístico |
| u(x_pt) documentada con modelo | Modelo completo en F-PSEA-14 | Estadístico |
| Condición u(x_pt) ≤ 0,3·σ_pt | Documentada en F-PSEA-14 con decisión de score | Estadístico |
| CRM vigente y trazable | Certificado en vigor; proveedor ISO 17034 | Coordinador EA |

---

## 8. Registros generados

| Formato | Descripción | Cuándo |
|---|---|---|
| F-PSEA-08 | Registro de preparación del ítem (incluye caudales y condiciones) | Durante generación (ver I-PSEA-02) |
| F-PSEA-14 | Hoja de cálculo: x_pt, u(x_pt), criterio de score | Post-generación, pre-ronda |
| Certificado CRM adjunto | Copia del certificado del CRM usado | Archivar con F-PSEA-08 |

---

## Control de versiones

| Versión | Fecha | Descripción del cambio | Elaboró | Revisó | Aprobó |
|---|---|---|---|---|---|
| 0.1 | [FECHA] | Skeleton inicial | [Nombre] | — | — |
| 1.0 | [FECHA] | Versión aprobada para prueba piloto | [Nombre] | [Nombre] | [Nombre] |
