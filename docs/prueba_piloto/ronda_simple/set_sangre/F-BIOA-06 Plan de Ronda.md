# F-BIOA-06 Plan de Ronda

| Campo | Valor |
|-------|-------|
| **Código** | F-BIOA-06 |
| **Nombre** | Plan de Ronda de Ensayo de Aptitud — Bioanálisis Clínico |
| **Nivel** | 4 |
| **Estado** | Borrador |
| **Prioridad** | 🔴 Crítica |
| **Responsable** | Coordinador de Ronda |
| **Alcance** | Ronda Simple — Set de Sangre |
| **Laboratorio** | Laboratorio de Bioanálisis Clínico — Hospital Universitario San Vicente |

---

## 1. Objeto

El presente documento establece el plan operativo y logístico para la ejecución de la ronda simple del programa piloto de ensayos de aptitud en el ámbito de bioanálisis clínico. Define las actividades, responsabilidades, cronograma y criterios de aceptación para el conjunto de muestras de sangre (suero/plasma) distribuidas a los laboratorios participantes.

## 2. Alcance y Campo de Aplicación

### 2.1 Análitos Evaluados

| # | Analito | Unidad | Rango de Concentración Esperado |
|---|---------|--------|---------------------------------|
| 1 | Glucosa | mg/dL | 50 – 400 |
| 2 | Colesterol Total | mg/dL | 100 – 400 |
| 3 | Triglicéridos | mg/dL | 50 – 500 |
| 4 | Hemoglobina | g/dL | 8.0 – 20.0 |
| 5 | Hematocrito | % | 20 – 60 |
| 6 | Creatinina | mg/dL | 0.5 – 10.0 |

### 2.2 Matrices Muestrales

- Suero humano (cubetas de vacutainer con gel separador)
- Plasma EDTA-K₂ (para hemograma)

### 2.3 Materiales de Referencia

| Material | Proveedor | Uso |
|----------|-----------|-----|
| CRM para glucosa (NIST SRM 917c) | NIST | Calibración y verificación |
| CRM para colesterol (NIST SRM 1951b) | NIST | Calibración y verificación |
| CRM para triglicéridos (NIST SRM 1951b) | NIST | Calibración y verificación |
| CRM para hemoglobina (NIST SRM 956c) | NIST | Calibración y verificación |
| CRM para creatinina (NIST SRM 967) | NIST | Calibración y verificación |

## 3. Referencia Normativa

| Norma | Descripción | Aplicación |
|-------|-------------|------------|
| ISO 15189:2022 | Laboratorios clínicos — Requisitos de calidad y competencia | Gestión de calidad del laboratorio participante |
| ISO 13528:2016 | Métodos estadísticos para resultados de PT | Cálculo de valores asignados, z-scores y desempeño |
| ISO/IEC 17043:2023 | Conformidad — Requisitos generales para ensayos de aptitud | Proveedores de programas de ensayo |
| NC-ISO 15189:2023 | Norma colombiana equivalente | Acreditación de laboratorios clínicos en Colombia |
| Resolución 1022 de 2015 (MinSalud) | Requisitos para laboratorios clínicos | Marco regulatorio nacional |

## 4. Plan Operativo

### 4.1 Cronograma de Actividades

| # | Actividad | Fecha Inicio | Fecha Fin | Responsable | Estado |
|---|-----------|--------------|-----------|-------------|--------|
| 1 | Preparación y estabilización de ítems | — | — | Coordinador Técnico | Pendiente |
| 2 | Verificación de homogeneidad | — | — | QA | Pendiente |
| 3 | Verificación de estabilidad | — | — | QA | Pendiente |
| 4 | Envío a participantes | — | — | Logística | Pendiente |
| 5 | Ventana de análisis por participantes | — | — | Participantes | Pendiente |
| 6 | Recepción de resultados | — | — | Coordinador | Pendiente |
| 7 | Análisis estadístico | — | — | Estadístico | Pendiente |
| 8 | Emisión de informes | — | — | Coordinador | Pendiente |

### 4.2 Logística de Distribución

| Aspecto | Especificación |
|---------|----------------|
| Tipo de embalaje | Contenedor termoaislante con gel refrigerante |
| Temperatura de transporte | 2 – 8 °C |
| Tiempo máximo de tránsito | 48 horas |
| Transportador autorizado | Servicio de paquetería con rastreo |
| Documentación adjunta | F-BIOA-05, F-BIOA-07, instrucciones de manejo |

### 4.3 Condiciones de Conservación

| Fase | Temperatura | Tiempo Máximo |
|------|-------------|---------------|
| Almacenamiento previo al envío | 2 – 8 °C | 30 días |
| Transporte | 2 – 8 °C | 48 horas |
| Recepción en participante | 2 – 8 °C | Analizar en ≤ 24 horas |
| Análisis por el participante | Ambiente (según SOP) | Según protocolo |

## 5. Responsabilidades

| Rol | Responsabilidades |
|-----|-------------------|
| Coordinador de Ronda | Planificación, seguimiento, comunicación con participantes |
| Coordinador Técnico | Preparación de ítems, verificación de condiciones |
| QA | Control de calidad interno, verificación documental |
| Estadístico | Cálculo de valores asignados, análisis de z-scores |
| Logística | Empaque, envío, rastreo de muestras |
| Participante | Recepción, análisis, reporte de resultados dentro de ventana |

## 6. Criterios de Aceptación

### 6.1 Criterios para el Ítem

| Criterio | Requisito | Método de Verificación |
|----------|-----------|------------------------|
| Homogeneidad | σs < 0.333 × EP | ISO 13528 Anexo A |
| Estabilidad | Desviación ≤ 2 × EP durante ventana de uso | Mediciones en t=0, t=medio, t=final |
| Concentración asignada | Media de ≥ 10 determinaciones con CV ≤ 2% | ISO 13528 §8 |

### 6.2 Criterios para el Participante

| Criterio | Requisito |
|----------|-----------|
| |z| ≤ 2.0 | Satisfactorio |
| 2.0 < |z| < 3.0 | Cuestionable |
| |z| ≥ 3.0 | Insatisfactorio |

## 7. Flujo de Información

```
Preparación de Ítems
        ↓
Verificación de Homogeneidad (F-BIOA-09)
        ↓
Verificación de Estabilidad (F-BIOA-10)
        ↓
Envío a Participantes (F-BIOA-11)
        ↓
Análisis por Participantes
        ↓
Reporte de Resultados (F-BIOA-12)
        ↓
Revisión de Datos (F-BIOA-13)
        ↓
Cálculo y Aprobación Estadística (F-BIOA-14)
        ↓
Emisión de Informes Finales
```

## 8. Checklist de Aprobación del Plan

| # | Ítem | Verificado |
|---|------|------------|
| 1 | Analitos definidos y concordantes con capacidades participantes | ☐ |
| 2 | Materiales de referencia disponibles y trazables | ☐ |
| 3 | Cronograma aprobado por dirección | ☐ |
| 4 | Logística de transporte validada | ☐ |
| 5 | Plantilla de reporte de participantes distribuida (F-BIOA-12) | ☐ |
| 6 | Criterios estadísticos definidos | ☐ |
| 7 | Contactos de participantes actualizados (F-BIOA-07) | ☐ |
| 8 | Procedimiento de emergencia documentado | ☐ |

---

**Aprobación:**

| Rol | Nombre | Firma | Fecha |
|-----|--------|-------|-------|
| Coordinador de Ronda | | | |
| Responsable QA | | | |
| Dirección Técnica | | | |
