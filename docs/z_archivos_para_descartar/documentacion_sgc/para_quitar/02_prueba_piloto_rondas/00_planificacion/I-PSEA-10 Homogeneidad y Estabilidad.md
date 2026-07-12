# I-PSEA-10 — Homogeneidad y Estabilidad

**Código:** I-PSEA-10  
**Nivel:** 3b — Instructivo Técnico  
**Estado:** skeleton ← en redacción  
**Versión:** 0.1-draft  
**Cláusulas ISO/IEC 17043:2023:** 7.3.2; ISO 13528:2022 Anexo B  
**Oleada:** 1  
**Prioridad:** 🔴 Crítica  
**Depende de:** P-PSEA-06 (σ_pt fijado), I-PSEA-02 (ítem generado)  
**Alimenta a:** F-PSEA-09 (registro homogeneidad), F-PSEA-10 (registro estabilidad)

---

## 1. Objeto

> **Instrucción:** Redactar en 1–2 oraciones el propósito. Debe responder: ¿qué evalúa este instructivo y por qué es necesario antes de la ronda?
>
> _Ejemplo base:_ "Este instructivo establece los pasos operativos para verificar la homogeneidad y estabilidad de los ítems de ensayo de aptitud generados in situ mediante dilución dinámica, previo al inicio de cada ronda del esquema CALAIRE-EA."

[TEXTO]

---

## 2. Alcance

> **Instrucción:** Delimitar a qué rondas, analitos y condiciones aplica. Especificar si aplica también a cilindros transportados.
>
> _Incluir:_ analitos (CO, SO₂, O₃, NO, NO₂), tipo de ítem (atmósfera generada in situ / cilindro), fase del proceso (pre-ronda).

[TEXTO]

---

## 3. Documentos de referencia

| Código / Norma | Título | Cláusula relevante |
|---|---|---|
| ISO/IEC 17043:2023 | Ensayos de aptitud para laboratorios | 7.3.2 |
| ISO 13528:2022 | Métodos estadísticos para EA | Anexo B |
| P-PSEA-06 | Procedimiento de Diseño Estadístico | σ_pt, criterios |
| I-PSEA-02 | Producción PT Items | Generación ítem |
| F-PSEA-09 | Registro de Homogeneidad | Registro |
| F-PSEA-10 | Registro de Estabilidad | Registro |

---

## 4. Definiciones y abreviaturas

| Término | Definición |
|---|---|
| σ_pt | Desviación estándar para evaluación de desempeño (calculada según P-PSEA-06) |
| s_hom | Desviación estándar de la prueba de homogeneidad entre atmósferas independientes |
| x̄_inicio | Media de mediciones al inicio del periodo de medición |
| x̄_fin | Media de mediciones al final del periodo de medición |
| CRM | Material de referencia certificado |
| Ítem PT | Atmósfera generada in situ o cilindro de gas certificado |
| Método de referencia | > _Instrucción: definir el equipo/método usado como referencia interna (ej. fotómetro UV, analizador NDIR trazable)_ |

---

## 5. Responsabilidades

| Rol | Responsabilidad en este instructivo |
|---|---|
| Ingeniero Operativo | Ejecutar las pruebas de H/E y diligenciar F-PSEA-09 y F-PSEA-10 |
| Estadístico | Calcular s_hom, verificar criterios y aprobar el ítem |
| Coordinador EA | Autorizar el inicio de la ronda una vez aprobadas las pruebas |

---

## 6. Procedimiento

### 6.1 Prerrequisitos antes de ejecutar

> **Instrucción:** Listar las condiciones que deben cumplirse antes de comenzar las pruebas. Incluir:
> - σ_pt definido y documentado (P-PSEA-06 aprobado)
> - Ítem PT disponible y generado (I-PSEA-02 completado)
> - Método de referencia calibrado y en buen funcionamiento
> - F-PSEA-09 y F-PSEA-10 impresos/abiertos y rotulados con código de ronda

- [ ] σ_pt definido en P-PSEA-06 para el analito de la ronda: ___________
- [ ] Sistema de dilución dinámica verificado (ver I-PSEA-02)
- [ ] Método de referencia (equipo): ___________ Nro. serie: ___________  Calibración vigente hasta: ___________
- [ ] F-PSEA-09 y F-PSEA-10 listos con código de ronda

---

### 6.2 Prueba de Homogeneidad

> **Objetivo:** Verificar que el ítem puede reproducirse con variabilidad aceptable entre generaciones independientes.

#### 6.2.1 Diseño de la prueba

> **Instrucción:** Especificar:
> - Número mínimo de atmósferas independientes: **≥ 10**
> - Número de réplicas por atmósfera con el método de referencia: **≥ 2**
> - Pausa mínima entre generaciones (para asegurar independencia): ___ min
> - Setpoint de concentración objetivo: se toma del F-PSEA-06 (Plan de Ronda)

| Parámetro | Valor requerido |
|---|---|
| N° de atmósferas independientes | ≥ 10 |
| Réplicas por atmósfera | ≥ 2 |
| Setpoint analito | Ver F-PSEA-06 |
| Pausa entre atmósferas | ___ min (definir según estabilización del sistema) |

#### 6.2.2 Ejecución

> **Instrucción:** Describir paso a paso:
> 1. Ajustar el sistema al setpoint definido
> 2. Estabilizar durante ___ minutos
> 3. Registrar ___ lecturas con el método de referencia
> 4. Perturbar el sistema (purgar, cambiar caudal, volver a setpoint)
> 5. Repetir para cada atmósfera independiente i = 1…n

1. Ajustar sistema al setpoint de concentración objetivo (ver F-PSEA-06, campo "Nivel _")
2. Esperar estabilización: ___ minutos (criterio: señal estable ±___%)
3. Tomar ___ lecturas consecutivas con el método de referencia → calcular promedio x̄_i
4. Registrar en F-PSEA-09: x̄_i, condiciones T/P/HR, hora
5. Perturbar el sistema: ___________________________________
6. Repetir pasos 1–5 hasta completar ≥ 10 atmósferas

#### 6.2.3 Cálculo y criterio

> **Instrucción:** Describir el cálculo de s_hom a partir de los n promedios x̄_i.

**Cálculo de s_hom:**

```
s_hom = √[ Σ(x̄_i − x̄)² / (n − 1) ]
```

donde x̄ = media global de las n atmósferas.

**Criterio de aceptación:**

| Condición | Resultado |
|---|---|
| s_hom ≤ 0,3 × σ_pt | ✅ APROBADO — proceder con la ronda |
| s_hom > 0,3 × σ_pt | ❌ NO APROBADO — ver §6.2.4 |

> **Instrucción:** Añadir nota sobre cómo se calcula 0,3 × σ_pt con el valor del analito específico.

#### 6.2.4 Acción ante no aprobación de homogeneidad

> **Instrucción:** Describir qué hacer si el criterio no se cumple:
> - Revisar fuentes de variabilidad (fugas, fluctuaciones de flujo, temperatura)
> - Documentar como trabajo no conforme
> - Evaluar si se puede repetir o si hay que ajustar el sistema

---

### 6.3 Prueba de Estabilidad

> **Objetivo:** Verificar que el ítem no cambia significativamente durante el tiempo de uso (intrajornada y durante la ventana de medición).

#### 6.3.1 Modalidad 1 — Estabilidad intrajornada

> **Instrucción:** Describir cómo se verifica que el sistema es estable dentro de una sesión de medición (ej. 4 horas). Definir:
> - Frecuencia de medición con el método de referencia durante la jornada
> - Criterio: |x̄_inicio − x̄_fin| ≤ 0,3 × σ_pt

| Parámetro | Valor |
|---|---|
| Duración de la ventana | ___ horas |
| Frecuencia de lecturas de referencia | Cada ___ minutos |
| N° lecturas al inicio (para x̄_inicio) | ___ |
| N° lecturas al final (para x̄_fin) | ___ |

**Criterio:**

| Condición | Resultado |
|---|---|
| \|x̄_inicio − x̄_fin\| ≤ 0,3 × σ_pt | ✅ ESTABLE |
| \|x̄_inicio − x̄_fin\| > 0,3 × σ_pt | ❌ INESTABLE — ver §6.3.4 |

#### 6.3.2 Modalidad 2 — Estabilidad durante la ventana de medición del participante

> **Instrucción:** La ventana de medición es el periodo durante el cual el participante reporta resultados. El método de referencia debe demostrar estabilidad durante ese mismo periodo. Describir cómo se monitorea (ej. lectura de referencia al inicio, mitad y fin de cada sesión de participante).

[TEXTO — adaptar a la duración de sesión de la prueba piloto: ___ horas/día × ___ días]

#### 6.3.3 Modalidad 3 — Estabilidad por transporte (si aplica cilindros)

> **Instrucción:** Aplicar solo si se usan cilindros transportados. En la prueba piloto se generan atmósferas in situ, por lo que esta sección puede marcarse como "No aplica" justificando la generación in situ.

**En la prueba piloto CALAIRE-EA:** Las atmósferas se generan in situ mediante dilución dinámica. Esta modalidad **no aplica**.

> _Conservar sección para futuras rondas con ítems transportables._

#### 6.3.4 Acción ante inestabilidad

> **Instrucción:** Describir procedimiento de respuesta:
> - Identificar causa de inestabilidad (fuga, derivación del CRM, condición ambiental)
> - Registrar incidencia en F-PSEA-10 y abrir NC si corresponde
> - Decisión: corregir y repetir / suspender la sesión de esa jornada

---

## 7. Criterios de aceptación consolidados

| Prueba | Variable | Criterio | Formato de registro |
|---|---|---|---|
| Homogeneidad | s_hom | s_hom ≤ 0,3 × σ_pt | F-PSEA-09 |
| Estabilidad intrajornada | \|x̄_i − x̄_f\| | ≤ 0,3 × σ_pt | F-PSEA-10 |
| Estabilidad ventana participante | \|x̄_i − x̄_f\| | ≤ 0,3 × σ_pt | F-PSEA-10 |

> **Nota para el redactor:** Antes de la primera ronda, calcular el valor numérico de 0,3 × σ_pt para cada analito y nivel, y añadirlo a la columna "Criterio" de la tabla. Esto hace el documento autocontenido para el personal operativo.

---

## 8. Registros generados

| Formato | Descripción | Quién diligencia |
|---|---|---|
| F-PSEA-09 | Registro de Prueba de Homogeneidad | Ingeniero Operativo |
| F-PSEA-10 | Registro de Prueba de Estabilidad | Ingeniero Operativo |
| NC (si aplica) | Registro de No Conformidad (F-PSEA-15) | Coordinador EA |

---

## 9. Diagrama de flujo

> **Instrucción:** Agregar diagrama Mermaid o imagen mostrando el flujo: Inicio → Prerrequisitos → Homogeneidad → [¿Aprobado?] → Estabilidad → [¿Estable?] → Autorización de ronda / No conformidad

```mermaid
flowchart TD
    A[Inicio: ronda planificada] --> B[Verificar prerrequisitos §6.1]
    B --> C[Prueba de Homogeneidad §6.2]
    C --> D{s_hom ≤ 0,3·σ_pt?}
    D -- Sí --> E[Prueba de Estabilidad §6.3]
    D -- No --> F[Investigar causa → NC → Repetir]
    E --> G{|x̄_i - x̄_f| ≤ 0,3·σ_pt?}
    G -- Sí --> H[✅ Ítem APROBADO — Autorizar ronda]
    G -- No --> I[Investigar causa → NC → Corregir]
```

---

## Control de versiones

| Versión | Fecha | Descripción del cambio | Elaboró | Revisó | Aprobó |
|---|---|---|---|---|---|
| 0.1 | [FECHA] | Skeleton inicial | [Nombre] | — | — |
| 1.0 | [FECHA] | Versión aprobada para prueba piloto | [Nombre] | [Nombre] | [Nombre] |
