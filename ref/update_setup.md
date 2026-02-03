# Plan de Estandarizacion - Journals, Guia del Agente y Tags de Correo

**Estado:** ✅ Todas las fases completadas
**Fecha:** 2026-02-03
**Ultima actualizacion:** 2026-02-03 19:30

## Objetivo

1. Estandarizar la estructura de los journals diarios para que el grafo se vea consistente y sea facil de consultar.
2. Ajustar las directrices del agente para que convierta notas rapidas en registro tecnico (sin copiar literal).
3. Alinear la clasificacion de correos (tags) con las categorias del grafo (Logseq) para trazabilidad correo <-> nota.

## Alcance

**Archivos a intervenir**

- `pages/templates.md`
- `AGENTS.md`
- `journals/*.md` (inventario actual: 6 archivos)
- `docs/tags_project.csv`
- `ref/setup.md`
- `logs/CURRENT_SESSION.md`

## Parte 1: Categorias estandar para Journals (Logseq) ✅ Completada

Categorias definidas para el registro diario:

- **Prueba Piloto**: rondas EA, confirmaciones de laboratorios, coordinacion operativa, cadena de custodia de equipos.
- **Gestion Administrativa**: cartas oficiales, comunicacion institucional, contratacion, licitaciones, dependencias administrativas.
- **Desarrollo Tecnico**: CALAIRE-APP, protocolos, calibracion, validacion/aseguramiento metrologico.
- **SGC / Calidad**: auditorias, control documental, requisitos ISO 17043/13528, acciones correctivas.
- **Infraestructura**: instalaciones, espacios, TI, transporte y soporte logistico.

Criterio: solo se crean las secciones que apliquen ese dia (no forzar secciones vacias). Las secciones extensas van con `collapsed:: true`.

## Parte 2: Template `journal-daily` ✅ Completada

**Archivo:** `pages/templates.md`

Agregar un template para estandarizar captura diaria:

```markdown
- **Journal Diario**
	- template:: journal-daily
	- # Registro del Dia
	  project:: [[CALAIRE-EA]]
	- ## Prueba Piloto
	  collapsed:: true
		- 
	- ## Gestion Administrativa
	  collapsed:: true
		- 
	- ## Desarrollo Tecnico
	  collapsed:: true
		- 
	- ## SGC / Calidad
	  collapsed:: true
		- 
	- ## Infraestructura
	  collapsed:: true
		- 
```

Uso:
- En el journal del dia: `/template journal-daily`
- Eliminar secciones que no apliquen.
- Reuniones formales se registran como `#[[Reunion: Tema]]` y se usa el template `reunion`.

## Parte 3: Ajuste de `AGENTS.md` para desarrollo de contenido ✅ Completada

**Archivo:** `AGENTS.md`

Agregar una seccion explicita para transformar notas rapidas en registro tecnico (sin transcripcion literal):

- Reformular en tercera persona o voz impersonal.
- Expandir con contexto operativo/metrologico (sin inventar datos no confirmados).
- Conectar con MOCs: `[[CALAIRE-EA]]`, `[[Prueba Piloto]]`, `[[QMS]]`, `[[CALAIRE-APP]]`.
- Convertir hechos en hitos y acciones: que paso, por que importa, impacto, proximo control.

Regla: **no copiar literalmente** frases del usuario; siempre reescribir y enriquecer.

## Parte 4: Homogeneizacion de journals existentes ✅ Completada

**Objetivo tecnico:** todos los bloques raiz deben iniciar con `- ` y la jerarquia debe usar tabs; propiedades en linea siguiente con indentacion (2 espacios) bajo su bloque.

Inventario actual:

- `journals/2026_02_03.md`
- `journals/2026_02_02.md`
- `journals/2026_01_30.md`
- `journals/2026_01_28.md`
- `journals/2026_01_12.md`
- `journals/2026_01_11.md`

Criterios acordados:

1. `2026_01_11.md` y `2026_01_12.md`: mantener como notas minimas; solo marcar como `#nota-historica`.
2. `2026_01_30.md`: conservar como version historica; colapsar cronogramas/diagramas y etiquetar como historico.

Acciones por archivo:

- `journals/2026_02_03.md`
  - Reencuadrar el contenido en categorias estandar:
    - Comunicaciones/correspondencia -> **Gestion Administrativa**
    - Espacio contiguo / logistica -> **Infraestructura**
    - Confirmacion de laboratorios -> **Prueba Piloto**
  - Corregir sintaxis Logseq (bloques raiz con `- `; propiedades bajo su bloque).

- `journals/2026_02_02.md`
  - Mantener decisiones (#decision) y reordenar por categorias estandar.
  - Separar claramente: reprogramacion rondas (Prueba Piloto), contratacion (Gestion Administrativa), IT (Infraestructura).

- `journals/2026_01_30.md`
  - Agregar encabezado `# Registro del Dia`.
  - Encapsular el contenido de Gantt/Timeline bajo un bloque marcado como `#version-historica` y `collapsed:: true`.

- `journals/2026_01_28.md`
  - Agregar encabezado `# Registro del Dia`.
  - Conservar bloque de reunion con su estructura.

- `journals/2026_01_12.md`
  - Agregar `- #nota-historica` y conservar contenido.

- `journals/2026_01_11.md`
  - Agregar `- #nota-historica` y conservar contenido.

## Parte 5: Actualizacion de `ref/setup.md` ✅ Completada

**Archivo:** `ref/setup.md`

Se agregó referencia a:

- nuevas categorias estandar del journal
- template `journal-daily`
- recomendacion de uso: solo secciones aplicables y uso de `collapsed:: true`

## Parte 6: Enriquecimiento de tags para correos ✅ Completada

**Archivo:** `docs/tags_project.csv`

Cambios:

1. Agregar columna `Categoria_Journal` para habilitar mapeo explicito correo <-> grafo.
2. Incluir nuevos grupos alineados con categorias del journal.
3. Agregar subtags para mejorar granularidad (sin romper los grupos existentes).

Nuevos grupos:

- **7. OPERACION TECNICA**
  - `[TECH] Pilot Round` / `[TECH] Ronda Piloto`
  - `[TECH] Pilot Round - Lab Confirmation` / `[TECH] Ronda - Confirmacion Lab`
  - `[TECH] Pilot Round - Equipment` / `[TECH] Ronda - Equipos`
  - `[TECH] Calibration` / `[TECH] Calibracion`
  - `[TECH] App Development` / `[TECH] Desarrollo App`

- **8. CALIDAD / SGC**
  - `[QMS] Audit` / `[SGC] Auditoria`
  - `[QMS] Procedure` / `[SGC] Procedimiento`
  - `[QMS] Accreditation` / `[SGC] Acreditacion`

- **9. INFRAESTRUCTURA**
  - `[INFRA] IT` / `[INFRA] TI`
  - `[INFRA] Facilities` / `[INFRA] Instalaciones`
  - `[INFRA] Transport` / `[INFRA] Transporte`

- **10. ACTIVIDADES TRANSVERSALES**
  - `[EVENT] Training` / `[EVENTO] Capacitacion`
  - `[EVENT] Workshop` / `[EVENTO] Taller`
  - `[EVENT] Presentation` / `[EVENTO] Socializacion`
  - `[EVENT] Conference` / `[EVENTO] Congreso/Evento`

Subtags (grupos existentes):

- **2. GESTION FINANCIERA**
  - `[Finance] Quote - Equipment` / `[Finanzas] Cotizacion - Equipos`
  - `[Finance] Contracting - Service` / `[Finanzas] Contratacion - Servicio`

- **3. SEGUIMIENTO Y ENTREGAS**
  - `[Tracking] Deliverable - Technical` / `[Seguimiento] Entregable - Tecnico`
  - `[Tracking] Deliverable - Administrative` / `[Seguimiento] Entregable - Administrativo`

Mapeo recomendado (columna `Categoria_Journal`):

- Prueba Piloto: tags `[TECH] Ronda*`, `[EVENTO] Taller`
- Gestion Administrativa: `[ACCION] *`, `[Finanzas] *`, `[EVENTO] Socializacion`, `[EVENTO] Congreso/Evento`, `[Seguimiento] Entregable - Administrativo`
- Desarrollo Tecnico: `[TECH] Desarrollo App`, `[TECH] Calibracion`, `[EVENTO] Capacitacion`
- SGC / Calidad: `[SGC] *`
- Infraestructura: `[INFRA] *`

## Orden de ejecucion

1. Crear `ref/update_setup.md` (este documento)
2. Actualizar `AGENTS.md`
3. Actualizar `pages/templates.md`
4. Homogeneizar `journals/*.md`
5. Actualizar `docs/tags_project.csv`
6. Actualizar `ref/setup.md`
7. Actualizar `logs/CURRENT_SESSION.md`

## Validacion

- Journals: sintaxis Logseq valida (bloques `- `, tabs, propiedades bajo bloque)
- Estructura diaria consistente (mismas categorias)
- Template `journal-daily` disponible
- Tags de correo ampliados y con columna `Categoria_Journal`
