# Estructura Técnica Mayo 2026 - OSE 88

**Objetivo**: arrancar la organización de mayo 2026 como mes base de evidencias técnicas y de SGC para la OSE 88, con nomenclatura uniforme `aaaammdd-a##_nombre-archivo` y trazabilidad por actividad contractual.

---

## Criterio operativo

El mes de mayo no se va a tratar como un registro administrativo de reuniones. Se va a tratar como el primer bloque de control técnico del proyecto, centrado en:

- revisión y ajuste del SGC
- identificación de brechas documentales
- control de versiones y documentos vigentes
- ajuste operacional de `CALAIRE-APP` y `pt_app`
- soporte a la dirección técnica del proyecto
- preparación de insumos para el informe oficial de cobro

Lectura funcional de los aplicativos:

- `CALAIRE-APP`: portal transaccional para captura, administración de rondas, registro de participantes y envío de datos.
- `pt_app`: motor de análisis estadístico offline en R/Shiny para homogeneidad, estabilidad, valores asignados, puntajes y reportes.

---

## Nomenclatura

Formato obligatorio para evidencias y archivos de trabajo:

`aaaammdd-a##_nombre-archivo`

Ejemplos:

- `20260501-a01-matriz-trazabilidad-sgc`
- `20260502-a03-control-version-documentos`
- `20260505-a05-seguimiento-tecnico-semanal`
- `20260508-a02-ajuste-protocolo-general`

Reglas:

1. `aaaammdd` ordena cronológicamente.
2. `a##` identifica la actividad contractual.
3. `nombre-archivo` describe el contenido técnico y debe ser corto.
4. No usar títulos genéricos como `acta`, `reunión`, `avance` si el contenido real es técnico.

---

## Mayo por bloques de trabajo

### Bloque 1: Diagnóstico y trazabilidad del SGC

**Objetivo:** ubicar qué documentos del SGC están vigentes, cuáles requieren ajuste y cuáles sirven como soporte directo para la OSE 88.

**Actividades asociadas:**

- A2 ajustes documentales
- A3 control documental
- A11 apoyo al sistema de gestión
- A12 imparcialidad, integridad, independencia y confidencialidad

**Primeras salidas esperadas:**

- matriz de documentos priorizados
- lista de brechas por norma y por documento
- control de versiones de los documentos que se van a tocar

**Evidencias sugeridas:**

- `20260501-a03-matriz-documentos-sgc`
- `20260503-a02-brechas-documentales`
- `20260506-a11-control-vigencia-sgc`

---

### Bloque 2: Dirección técnica del proyecto

**Objetivo:** dejar explícito el control técnico del proyecto y la forma en que se van a registrar decisiones, desviaciones y acciones de control.

**Actividades asociadas:**

- A1 dirección de la prueba piloto
- A5 seguimiento técnico
- A6 coordinación con el equipo
- A7 presencia en actividades requeridas
- A8 participación activa en convocatorias

**Primeras salidas esperadas:**

- mapa técnico de seguimiento
- secuencia de decisiones técnicas
- registro de riesgos o desviaciones

**Evidencias sugeridas:**

- `20260504-a05-seguimiento-tecnico`
- `20260507-a01-control-piloto`
- `20260510-a06-coordinacion-tecnica`

---

### Bloque 3: Ajustes normativos y documentales

**Objetivo:** aterrizar los cambios del SGC y de los protocolos a una versión controlada, sin perder rastreo de qué cambió y por qué.

**Actividades asociadas:**

- A2 ajustes a documentos
- A3 control documental
- A10 creación y actualización de procedimientos e instructivos

**Primeras salidas esperadas:**

- lista de documentos a revisar
- registro de cambios por documento
- evidencia de solicitud o control de cambio

**Evidencias sugeridas:**

- `20260508-a10-ajuste-instructivo`
- `20260512-a03-control-cambios`
- `20260514-a02-version-controlada`

---

### Bloque 4: Ajuste operacional de aplicativos

**Objetivo:** revisar y ajustar el comportamiento operativo de `CALAIRE-APP` y `pt_app` como soporte técnico del proyecto y del SGC.

**Actividades asociadas:**

- A2 ajustes documentales cuando el cambio implique actualización de guías, instructivos o manuales
- A3 control documental cuando el cambio afecte versiones controladas
- A5 seguimiento técnico
- A10 actualización de procedimientos e instructivos
- A11 soporte al SGC cuando el cambio impacte el sistema de gestión

**Primeras salidas esperadas:**

- registro de ajustes operativos
- lista de incidencias funcionales o de flujo
- decisión sobre qué cambios quedan documentados en SGC y cuáles quedan solo como soporte técnico
- separación clara entre hallazgos de `CALAIRE-APP` y de `pt_app`
- priorización de correcciones que afecten trazabilidad, cálculo o captura de datos

**Evidencias sugeridas:**

- `20260509-a05-ajuste-calaire-app`
- `20260511-a05-ajuste-pt-app`
- `20260513-a10-actualizacion-instructivo-app`
- `20260516-a03-control-version-apps`
- `20260518-a11-impacto-sgc-app`

---

### Bloque 5: Insumos para costeo y preparación de cobro

**Objetivo:** generar insumos técnicos que luego alimenten el formato oficial de cobro, sin confundirlo con el control interno.

**Actividades asociadas:**

- A4 apoyo al costeo

**Primeras salidas esperadas:**

- supuestos técnicos de costo
- actividades que consumen recursos
- criterios para justificar horas o esfuerzo técnico

**Evidencias sugeridas:**

- `20260515-a04-insumo-costeo`
- `20260520-a04-resumen-tecnico-costos`

---

## Orden de trabajo recomendado para empezar mayo

1. Construir la matriz de trazabilidad de documentos SGC y actividades contractuales.
2. Identificar 5 a 10 documentos priorizados para ajuste.
3. Definir qué evidencias quedarán por actividad y no por reunión.
4. Crear la primera evidencia codificada con la convención nueva.
5. Redactar el resumen interno de mayo a partir de esas evidencias.

---

## Riesgos de orientación

- Mezclar evidencia técnica con evidencias administrativas.
- Usar nombres genéricos que después no permitan búsqueda rápida.
- Registrar reuniones sin conectar el contenido con actividad, norma o documento.
- Enfocar mayo solo en informes de cobro y dejar débil el control interno.

---

## Resultado esperado de mayo

Al cierre del mes debe existir:

- una base de evidencias con nomenclatura uniforme
- una matriz de control por actividad
- un primer conjunto de documentos SGC priorizados y trazables
- un registro separado de ajustes técnicos de `CALAIRE-APP` y `pt_app`
- material suficiente para completar el informe oficial de cobro y el informe interno
