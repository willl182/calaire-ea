# I-PSEA-02 — Producción PT Items

**Código:** I-PSEA-02  
**Nivel:** 3b — Instructivo Técnico  
**Estado:** skeleton ← en redacción  
**Versión:** 0.1-draft  
**Cláusulas ISO/IEC 17043:2023:** 7.3.1  
**Oleada:** 1  
**Prioridad:** 🔴 Crítica (Sprint 2)  
**Depende de:** F-PSEA-06 (Plan de Ronda: niveles y analitos), CRM vigente  
**Alimenta a:** I-PSEA-10 (H/E), I-PSEA-08 (x_pt), F-PSEA-08 (registro preparación)

---

## 1. Objeto

> **Instrucción:** Describir que este instructivo establece los pasos operativos para generar las atmósferas de gas de referencia (ítems PT) mediante dilución dinámica a partir de CRM, para uso en las rondas del esquema CALAIRE-EA.

[TEXTO]

---

## 2. Alcance

> **Instrucción:** Indicar que aplica a la generación in situ de atmósferas de CO, SO₂, O₃, NO y NO₂ en las instalaciones de la Universidad. No aplica a la preparación de cilindros transportables.

[TEXTO]

---

## 3. Documentos de referencia

| Código / Norma | Título | Sección relevante |
|---|---|---|
| ISO/IEC 17043:2023 | Ensayos de aptitud para laboratorios | 7.3.1 |
| ISO 13528:2022 | Métodos estadísticos para EA | §6.1 |
| F-PSEA-06 | Plan de Ronda EA | Analitos, niveles, setpoints |
| F-PSEA-08 | Registro de Preparación del Ítem | Registro de generación |
| I-PSEA-10 | Homogeneidad y Estabilidad | Criterios H/E |
| I-PSEA-08 | Valor Asignado | Cálculo de x_pt con datos de generación |
| Certificado CRM vigente | — | Concentración y u_CRM |

---

## 4. Definiciones y abreviaturas

| Término | Definición |
|---|---|
| CRM | Material de referencia certificado (cilindro de gas con concentración certificada trazable al SI) |
| Dilución dinámica | Técnica de generación de atmósferas por mezcla continua de gas del CRM con diluyente limpio |
| MFC | Controlador de flujo másico (Mass Flow Controller) |
| Setpoint | Concentración objetivo del ítem PT, definida en F-PSEA-06 |
| Diluyente | Gas limpio de dilución (aire sintético o nitrógeno) libre de interferentes |
| Manifold | Distribuidor de flujo que divide la atmósfera generada hacia múltiples puntos de muestreo |
| Estabilización | Periodo de espera tras ajustar caudales para que la concentración alcance estado estacionario |

---

## 5. Responsabilidades

| Rol | Responsabilidad |
|---|---|
| Ingeniero Operativo | Ejecutar todos los pasos de generación; diligenciar F-PSEA-08 |
| Coordinador EA | Verificar CRM vigente y aprobar el ítem generado (firma en F-PSEA-08) |
| Estadístico | Usar los valores de caudal y CRM registrados en F-PSEA-08 para calcular x_pt (I-PSEA-08) |

---

## 6. Recursos y equipos requeridos

> **Instrucción:** Listar los equipos del laboratorio CALAIRE que intervienen en la generación. Incluir número de serie y calibración vigente para los críticos.

| Equipo | Modelo / Referencia | Nro. Serie | Calibración vigente hasta |
|---|---|---|---|
| CRM — analito principal | [Proveedor, Gas, C_cert] | [Lote #] | [Fecha vencimiento] |
| MFC gas CRM | [Fabricante, modelo, rango] | | |
| MFC diluyente | [Fabricante, modelo, rango] | | |
| Fotómetro UV (O₃) / NDIR (CO, SO₂) referencia | | | |
| Manifold de distribución | [Material: Teflón/acero inox] | | |
| Sistema de control / software | | | |
| Sensor T/P/HR sala | | | |

---

## 7. Procedimiento

### 7.1 Preparación previa a la generación

> **Instrucción:** Listar las verificaciones antes de encender el sistema. Incluir tiempos de estabilización del sistema y umbrales de limpieza del diluyente.

- [ ] Revisar F-PSEA-06: analito a generar, nivel(es) de concentración, código de ronda
- [ ] Verificar que el CRM es el especificado en F-PSEA-06 y está vigente (ver §6)
- [ ] Verificar conexiones del manifold: sin fugas (prueba de hermeticidad con _____)
- [ ] Verificar que las líneas de teflón estén limpias (purgar con diluyente durante ___ min)
- [ ] Encender equipos: precalentar MFC durante ___ min, instrumento de referencia durante ___ min
- [ ] Registrar condiciones ambientales iniciales: T = ___°C, P = ___ kPa, HR = ___%

---

### 7.2 Cálculo de setpoints de caudal

> **Instrucción:** Describir cómo se calculan los caudales Q_gas y Q_diluyente para alcanzar cada nivel de concentración objetivo. Incluir la fórmula de dilución y la tabla de setpoints por nivel.

**Fórmula:**

```
Q_gas = x_pt_objetivo × Q_total / C_CRM
Q_diluyente = Q_total − Q_gas
```

> **Instrucción:** Completar la tabla para cada nivel de concentración de la ronda (tomar de F-PSEA-06).

| Nivel | x_pt objetivo (nmol/mol) | C_CRM (nmol/mol) | Q_total (mL/min) | Q_gas calculado | Q_diluyente calculado |
|---|---|---|---|---|---|
| Nivel 1 | | | | | |
| Nivel 2 | | | | | |
| Nivel 3 (si aplica) | | | | | |

---

### 7.3 Configuración del sistema de dilución

> **Instrucción:** Paso a paso para configurar los MFC y el sistema de distribución.

1. Ajustar MFC_gas al setpoint de Q_gas calculado en §7.2
2. Ajustar MFC_diluyente al setpoint de Q_diluyente calculado
3. Verificar caudal total: Q_total_medido = ___ mL/min (debe coincidir ±___% con Q_total_calculado)
4. Esperar estabilización: ___ minutos (criterio: señal del instrumento de referencia varía ≤ ___% durante 5 min consecutivos)
5. Registrar caudales reales en F-PSEA-08

---

### 7.4 Verificación de la concentración generada

> **Instrucción:** Describir cómo se verifica que la concentración real coincide con el setpoint usando el instrumento de referencia. Incluir criterio de aceptación para la concentración generada.

1. Leer la concentración en el instrumento de referencia: ___ mediciones, cada ___ segundos
2. Calcular promedio x̄_ref y desviación estándar s_ref
3. Calcular x_pt por dilución (I-PSEA-08 §6.2) con los caudales reales
4. Comparar: |x̄_ref − x_pt_calculado| / x_pt_calculado ≤ ___% (criterio a definir)

> **Nota:** Si la diferencia supera el criterio, investigar fugas o desviación de los MFC antes de continuar.

---

### 7.5 Distribución a puntos de muestreo (manifold)

> **Instrucción:** Describir cómo se distribuye la atmósfera generada a los puertos del manifold donde se conectan los equipos de los participantes. Incluir el número máximo de puertos simultáneos y criterio de uniformidad de concentración entre puertos.

> **Instrucción:** Para la prueba piloto: describir el esquema de conexión para P1 (SIATA) y P2 (UPB) y el instrumento de referencia del laboratorio.

| Puerto manifold | Asignado a | Observaciones |
|---|---|---|
| Puerto 1 | Instrumento de referencia CALAIRE | Monitoreo continuo |
| Puerto 2 | P1 — SIATA | Ronda Simple y F1 |
| Puerto 3 | P2 — UPB | Ronda F1 y F2 |
| Puerto 4 | Reserva | — |

---

### 7.6 Registro y entrega del ítem

> **Instrucción:** Describir los pasos de cierre de la etapa de generación y la entrega formal del ítem para el inicio de la ronda.

1. Diligenciar F-PSEA-08 completamente: caudales reales, x_pt, u(x_pt), T/P/HR, CRM usado, hora inicio
2. Firma del Ingeniero Operativo en F-PSEA-08
3. Notificar al Coordinador EA → revisión y firma de aprobación en F-PSEA-08
4. Proceder con pruebas H/E (I-PSEA-10) antes de conectar participantes
5. Una vez H/E aprobadas → autorizar conexión de equipos de participantes

---

## 8. Criterios de aceptación del ítem generado

| Verificación | Criterio | Formato |
|---|---|---|
| Concentración generada vs. setpoint | \|x̄_ref − x_pt\| / x_pt ≤ ___% | F-PSEA-08 |
| Homogeneidad verificada | s_hom ≤ 0,3·σ_pt (I-PSEA-10) | F-PSEA-09 |
| Estabilidad verificada | \|x̄_i − x̄_f\| ≤ 0,3·σ_pt (I-PSEA-10) | F-PSEA-10 |
| CRM vigente y trazable | Certificado en vigor | Adjunto F-PSEA-08 |
| F-PSEA-08 firmado por Coordinador | Aprobación formal | F-PSEA-08 |

---

## 9. Condiciones ambientales de operación

> **Instrucción:** Especificar los rangos aceptables de temperatura, presión y humedad relativa durante la generación. Si la sala no cumple, documentar la condición y evaluar impacto en u(x_pt).

| Parámetro | Rango aceptable | Acción si fuera de rango |
|---|---|---|
| Temperatura sala | ___ °C a ___ °C | Ajustar climatización; documentar desviación |
| Presión atmosférica | ___ kPa a ___ kPa | Aplicar corrección en cálculo de dilución |
| Humedad relativa | ___ % a ___ % | Verificar que el diluyente esté seco; documentar |

---

## 10. Registros generados

| Formato | Descripción | Cuándo |
|---|---|---|
| F-PSEA-08 | Registro de preparación del ítem (caudales, CRM, T/P/HR, aprobación) | Durante cada generación |
| F-PSEA-09 | Registro de homogeneidad (tras generación — ver I-PSEA-10) | Post-generación |
| F-PSEA-10 | Registro de estabilidad (durante la ronda — ver I-PSEA-10) | Durante la ronda |

---

## Control de versiones

| Versión | Fecha | Descripción del cambio | Elaboró | Revisó | Aprobó |
|---|---|---|---|---|---|
| 0.1 | [FECHA] | Skeleton inicial | [Nombre] | — | — |
| 1.0 | [FECHA] | Versión aprobada para prueba piloto | [Nombre] | [Nombre] | [Nombre] |
