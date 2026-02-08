# Mapa de Estructura - Fase 2

**Created**: 2026-02-08 16:45
**Updated**: 2026-02-08 18:30
**Status**: completed
**Fase**: 2 - Mapeo de Comunicación Actual
**Documento base**: docs/docs_sgc/M.LCAFMi-## Comunicacion Detallada EAdocx.md

---

## Estructura Actual del Documento

| # | Título | Líneas aprox. | Contenido Principal | Brecha Relacionada |
|---|--------|---------------|-------------------|-------------------|
| **Encabezado** | Asunto y Referencia EA | 1-7 | Datos de identificación | - |
| **1** | OBJETIVO DEL ENSAYO DE APTITUD | 13-15 | Propósito del EA | - |
| **2** | ALCANCE Y PARÁMETROS DE MEDICIÓN | 17-31 | Mensurandos (SO₂, NO/NO₂, CO, O₃) y niveles | - |
| **3** | ÍTEM DE ENSAYO DE APTITUD | 33-41 | Descripción generación dinámica, manifold | - |
| **4** | CRONOGRAMA | 43-50 | Referencia a F-PSEA-01 y F-PSEA-02 | - |
| **5** | INSTRUCCIONES GENERALES Y TRANSPORTE | 52-71 | Equipamiento, operación, embalaje | 🔴 **B1** (parcial) |
| **6** | PROTOCOLO DE MEDICIÓN EN SITIO | 73-112 | Día 1-3, instalación, conexión al manifold | - |
| **7** | EVALUACIÓN DE DESEMPEÑO | 114-138 | Valor asignado, estadísticos ζ y Eₙ, criterios | 🔴 **B2** (omisión) |
| **8** | CONFIDENCIALIDAD E IMPARCIALIDAD | 140-141 | Códigos, no confabulación, excepciones | 🔴 **B4** (omisión) |
| **8** | DECLARACIÓN | 143-145 | Aceptación de condiciones | ⚠️ **ERROR**: Duplicidad de numeración |
| **Cierre** | Agradecimientos, firma y anexos | 147-161 | Agradecimiento, firma, documentos | - |

---

## Ubicación de las 4 Brechas

### Brecha 1: Seguridad Industrial (Crítica)

**Estado actual:** Parcialmente abordado
- Sección 5 menciona embalaje y transporte (líneas 66-71), referencia a I-PSEA-01
- ❌ Omite: normas de seguridad industrial dentro de instalaciones, EPP, rutas evacuación, manejo cilindros a presión

**Opción de ubicación:**

| Opción | Ubicación | Ventajas | Desventajas |
|--------|-----------|----------|-------------|
| A | Nueva sección **5.5** dentro de Sección 5 | Mantenimiento de contexto logístico/operativo | Inserta en medio de sección existente |
| B | Nueva sección **9** después de "DECLARACIÓN" | Independiente, fácil de localizar | Desvinculado de contexto operativo |
| C | Ampliar Sección 6 (Protocolo de Medición) | Contexto in-situ de seguridad | Sección 6 es muy larga ya |

**Nota revisión:** El revisor recomienda ubicar Seguridad Industrial antes de DECLARACIÓN para mantener la lógica de aceptación. Se ajusta la ubicación propuesta.

**Recomendación ajustada:** Opción A - Nueva sección 9 (entre Sección 8 y DECLARACIÓN)

---

### Brecha 2: Definición σpt (Alta)

**Estado actual:** Omisión
- Sección 7 menciona ζ-score y Eₙ-score (líneas 126-127)
- ❌ No especifica origen de σpt (¿fija? ¿del grupo?)

**Opción de ubicación:**

| Opción | Ubicación | Texto a insertar |
|--------|-----------|------------------|
| A | Ampliar Sección 7, después de "Fuentes de incertidumbre" | Párrafo definiendo origen de σpt |
| B | Ampliar Sección 7, en subsección "Criterios de Calificación" | Nota a pie o párrafo previo a criterios |

**Recomendación:** Opción A - Párrafo nuevo después de línea 122 (Fuentes de incertidumbre)

---

### Brecha 3: Quejas y Apelaciones (Alta)

**Estado actual:** Omisión total
- ❌ No hay ninguna referencia a quejas, apelaciones, procedimiento de objeciones

**Opción de ubicación:**

| Opción | Ubicación | Ventajas | Desventajas |
|--------|-----------|----------|-------------|
| A | Nueva sección **9** (antes de "DECLARACIÓN") | Contexto administrativo, pre-firma | - |
| B | Nueva sección **10** (después de "DECLARACIÓN") | Final del documento, fácil acceso | - |
| C | Ampliar Sección 8 (Confidencialidad) | Agrupa gestión administrativa | Sección 8 es corta (2 líneas) |

**Recomendación:** Opción B - Nueva sección 10 (después de DECLARACIÓN)

---

### Brecha 4: Declaración Subcontratación (Media)

**Estado actual:** Omisión
- Sección 8 menciona confidencialidad e imparcialidad
- ❌ No declara si hay actividades subcontratadas

**Opción de ubicación:**

| Opción | Ubicación | Texto a insertar |
|--------|-----------|------------------|
| A | Ampliar Sección 8 (Confidencialidad e Imparcialidad) | Párrafo declarando subcontratación |
| B | Ampliar Sección 3 (Ítem de Ensayo) | Párrafo sobre trazabilidad y subcontratación |

**Recomendación:** Opción A - Párrafo nuevo en Sección 8, antes de línea 142

---

## Propuesta de Estructura Final

### Orden Propuesto de Mejoras

| # | Mejora | Acción | Ubicación Final |
|---|--------|--------|----------------|
| 1 | Seguridad Industrial | Nueva sección | **Sección 9** (antes de "DECLARACIÓN") |
| 2 | Definición σpt | Ampliar | Sección 7, después de "Fuentes de incertidumbre" |
| 3 | Quejas y Apelaciones | Nueva sección | **Sección 10** (después de "DECLARACIÓN") |
| 4 | Subcontratación | Ampliar | Sección 8, antes de "CALAIRE garantiza..." |

### Estructura Renumerada (post-implementación)

| # | Título (Propuesto) | Modificación |
|---|-------------------|--------------|
| 1 | OBJETIVO DEL ENSAYO DE APTITUD | Sin cambio |
| 2 | ALCANCE Y PARÁMETROS DE MEDICIÓN | Sin cambio |
| 3 | ÍTEM DE ENSAYO DE APTITUD | Sin cambio |
| 4 | CRONOGRAMA | Sin cambio |
| 5 | INSTRUCCIONES GENERALES Y TRANSPORTE | Sin cambio |
| 6 | PROTOCOLO DE MEDICIÓN EN SITIO | Sin cambio |
| 7 | EVALUACIÓN DE DESEMPEÑO | ✏️ Ampliar (definición σpt) |
| 8 | CONFIDENCIALIDAD E IMPARCIALIDAD | ✏️ Ampliar (subcontratación) |
| 9 | SEGURIDAD INDUSTRIAL | ➕ Nueva |
| 10 | QUEJAS Y APELACIONES | ➕ Nueva |
| 11 | DECLARACIÓN | Renumerado (was 8) |
| - | Firma y anexos | Sin cambio |

---

## Detalle de Inserciones

### Inserción 1: Definición σpt (Sección 7)

**Punto de inserción:** Después de línea 122 ("3. Homogeneidad"), antes de línea 124 ("Estadísticos de Desempeño:")

**Texto propuesto (lineamiento):**
> Origen de la Desviación Estándar para la Aptitud (σpt): La desviación estándar para la evaluación de la aptitud (σpt) se determina según [método a definir en Fase 4]. Este valor se aplica de manera consistente en todas las rondas del esquema para garantizar una evaluación objetiva del desempeño.

---

### Inserción 2: Subcontratación (Sección 8)

**Punto de inserción:** Después de línea 140 ("...impedancia en todas las fases del EA."), antes de línea 141 ("CALAIRE garantiza...")

**Texto propuesto (lineamiento):**
> Subcontratación: [Declaración sobre si hay actividades subcontratadas en el EA].

---

### Inserción 3: Seguridad Industrial (Sección 9 - Nueva)

**Punto de inserción:** Después de línea 141 ("...impedancia en todas las fases del EA."), antes de línea 143 ("**8. DECLARACIÓN**")

**Nota:** Esta ubicación coloca Seguridad Industrial antes de la DECLARACIÓN, manteniendo la lógica de que el participante conozca todos los términos (incluidos los de seguridad) antes de aceptarlos.

**Estructura propuesta (lineamiento):**
> **9. SEGURIDAD INDUSTRIAL**
>
> El presente EA se realiza bajo un esquema in-situ en las instalaciones de CALAIRE. Se aplican las siguientes normas de seguridad:
> - [EPP obligatorios]
> - [Normas manejo cilindros a presión]
> - [Rutas de evacuación]
> - [Normativas transporte mercancías peligrosas]

---

### Inserción 4: Quejas y Apelaciones (Sección 10 - Nueva)

**Punto de inserción:** Después de línea 145 ("...indicadores de desempeño."), antes de línea 147 ("Agradecemos su interés...")

**Nota:** Esta ubicación coloca Quejas y Apelaciones después de la DECLARACIÓN, al final del documento, facilitando la accesibilidad de este derecho del participante.

**Estructura propuesta (lineamiento):**
> **10. QUEJAS Y APELACIONES**
>
> Los participantes tienen derecho a [plazo días] para presentar quejas o apelaciones sobre los resultados del EA. El procedimiento está documentado en [procedimiento y referencia].

---

## Registro de Revisiones

### Revisión 1 - 2026-02-08 16:47 (Revisor-fase)

**Hallazgos incorporados:**
- ✅ Unificada ubicación de Seguridad Industrial: antes de DECLARACIÓN (Sección 9)
- ✅ Unificada ubicación de Quejas y Apelaciones: después de DECLARACIÓN (Sección 10)
- ✅ Corregidos puntos de inserción para coincidir con flujo real del documento
- ✅ Añadida nota explícita sobre duplicidad de Sección 8 en tabla principal
- ✅ Actualizado mapeo del cierre para incluir línea 147 ("Agradecemos...")

**Ajustes realizados:**
- Inserción 1 (σpt): línea 122-124
- Inserción 2 (Subcontratación): línea 140-141
- Inserción 3 (Seguridad): línea 141-143 (antes de DECLARACIÓN)
- Inserción 4 (Quejas): línea 145-147 (después de DECLARACIÓN)

---

## Notas de Implementación

1. **Corrección de numeración:** Actualmente hay dos secciones "8". Esto debe corregirse al renumerar.
2. **Referencias a documentos adjuntos:** Mantener consistencia con F-PSEA-01, F-PSEA-02, I-PSEA-01.
3. **Tablas y listas:** Preservar formato de listas y tablas existentes.
4. **Imágenes:** Las imágenes embedidas (image1, image2) deben mantener su posición relativa.

---

## Análisis de Longitud

| Sección | Líneas actuales | Líneas post-implementación | Cambio |
|---------|----------------|---------------------------|--------|
| 1 | 3 | 3 | 0 |
| 2 | 15 | 15 | 0 |
| 3 | 9 | 9 | 0 |
| 4 | 8 | 8 | 0 |
| 5 | 20 | 20 | 0 |
| 6 | 40 | 40 | 0 |
| 7 | 25 | 28 | +3 (σpt) |
| 8 | 2 | 4 | +2 (subcontratación) |
| 9 | 0 | 8-10 | +8-10 (seguridad) |
| 10 | 0 | 5-7 | +5-7 (quejas) |
| 11 | 3 | 3 | 0 |
| Cierre | 13 | 13 | 0 |
| **Total** | **138** | **153-159** | **+15-21** |

**Impacto estimado:** El documento crecerá aproximadamente 15-21 líneas (11-15%).

---

## Validación de Implementación (Post-Fase 5)

### Verificación de Inserciones

| # | Inserción | Punto de Inserción Propuesto | Punto de Inserción Realizado | Estado |
|---|-----------|------------------------------|----------------------------|--------|
| 1 | Definición σpt | Línea 122-124 (Sección 7) | Líneas 124-138 (Sección 7) | ✅ Correcto |
| 2 | Subcontratación | Línea 140-141 (Sección 8) | Líneas 159-204 (Sección 8.1) | ✅ Correcto |
| 3 | Seguridad Industrial | Línea 141-143 (antes de DECLARACIÓN) | Líneas 206-277 (Sección 9) | ✅ Correcto |
| 4 | Quejas y Apelaciones | Línea 145-147 (después de DECLARACIÓN) | Líneas 283-365 (Sección 11) | ✅ Correcto |

---

### Verificación de Renumeración

**Estructura final implementada:**

| # | Título (Propuesto) | Título (Implementado) | Estado |
|---|-------------------|----------------------|--------|
| 1 | OBJETIVO DEL ENSAYO DE APTITUD | OBJETIVO DEL ENSAYO DE APTITUD | ✅ |
| 2 | ALCANCE Y PARÁMETROS DE MEDICIÓN | ALCANCE Y PARÁMETROS DE MEDICIÓN | ✅ |
| 3 | ÍTEM DE ENSAYO DE APTITUD | ÍTEM DE ENSAYO DE APTITUD | ✅ |
| 4 | CRONOGRAMA | CRONOGRAMA | ✅ |
| 5 | INSTRUCCIONES GENERALES Y TRANSPORTE | INSTRUCCIONES GENERALES Y TRANSPORTE | ✅ |
| 6 | PROTOCOLO DE MEDICIÓN EN SITIO | PROTOCOLO DE MEDICIÓN EN SITIO | ✅ |
| 7 | EVALUACIÓN DE DESEMPEÑO (ampliar) | EVALUACIÓN DE DESEMPEÑO | ✅ Ampliada |
| 8 | CONFIDENCIALIDAD E IMPARCIALIDAD (ampliar) | CONFIDENCIALIDAD E IMPARCIALIDAD | ✅ Ampliada |
| 8.1 | - | Subcontratación de Actividades | ✅ Nueva |
| 9 | SEGURIDAD INDUSTRIAL (nueva) | SEGURIDAD INDUSTRIAL | ✅ Nueva |
| 10 | DECLARACIÓN (renumerar) | DECLARACIÓN | ✅ Renumerada |
| 11 | QUEJAS Y APELACIONES (nueva) | QUEJAS Y APELACIONES | ✅ Nueva |

---

### Análisis de Longitud Final

| Sección | Líneas estimadas | Líneas implementadas | Variación |
|---------|------------------|---------------------|-----------|
| 1 | 3 | 3 | 0 |
| 2 | 15 | 15 | 0 |
| 3 | 9 | 9 | 0 |
| 4 | 8 | 8 | 0 |
| 5 | 20 | 20 | 0 |
| 6 | 40 | 40 | 0 |
| 7 | 28 (+3) | 28 (+3) | ✅ |
| 8 | 4 (+2) | 46 (+44) | ⚠️ Incluye 8.1 completa |
| 9 | 8-10 (nueva) | 72 (nueva) | ✅ |
| 10 | 3 (renumerado) | 3 | ✅ |
| 11 | 5-7 (nueva) | 83 (nueva) | ✅ |
| Cierre | 13 | 13 | 0 |
| **Total** | **153-159** | **340** | ⚠️ Mayor que estimado |

**Nota:** El crecimiento mayor al estimado se debe a que las nuevas secciones (9 y 11) incluyen subsecciones detalladas que no estaban completamente dimensionadas en la fase de planificación.

---

### Validación de Coherencia

- ✅ Referencias cruzadas a secciones internas (ej. F-PSEA-01, F-PSEA-02) preservadas
- ✅ Imágenes embebidas (image1, image2) intactas
- ✅ Términos técnicos consistentes (σₚₜ, ζ-score, Eₙ-score)
- ✅ Numeración de subsecciones correcta (9.1-9.7, 8.1.1-8.1.4, 11.1-11.7)

---

**Fin de Fase 2**