# Historia de evolución del Sistema de Gestión de Calidad PEA

## Propósito

Este documento consolida la evolución del Sistema de Gestión de Calidad del Programa de Ensayos de Aptitud (SGC PEA) de CALAIRE-EA, a partir de los registros en `logs/`, `docs/documentacion_sgc/logs/` y el historial de commits del repositorio. No reemplaza los documentos controlados del SGC; funciona como memoria técnica de cómo se construyó, reorganizó, corrigió y normalizó la documentación.

## Fuentes revisadas

- `logs/CURRENT_SESSION.md`
- `logs/history/*_findings.md`
- `logs/history/*_problems.md`
- `logs/plans/*`
- `docs/documentacion_sgc/logs/CURRENT_SESSION.md`
- `docs/documentacion_sgc/logs/history/260627_1159_findings.md`
- `docs/documentacion_sgc/logs/history/260627_1159_problems.md`
- Historial Git de commits sobre `docs/documentacion_sgc`, `docs/docs_sgc` y `logs`

## Línea de tiempo ejecutiva

### 1. Diagnóstico normativo inicial y brechas ISO

El punto de partida del SGC PEA fue la revisión técnica del protocolo general, de comunicaciones y de informes frente a ISO/IEC 17043:2023 e ISO 13528:2022. En los registros de febrero se identificó que el sistema documental ya tenía una base operativa, pero requería formalizar criterios estadísticos, trazabilidad metrológica, comunicación con participantes y tratamiento de escenarios de bajo número de laboratorios.

Los hallazgos más relevantes fueron:

- El protocolo general mencionaba estadísticas robustas, pero no definía formalmente si se aplicaría Algoritmo A, MADe o nIQR.
- Faltaban criterios cuantitativos explícitos de homogeneidad y estabilidad, incluyendo el umbral `ss <= 0.3 sigma_pt` y acciones ante incumplimiento.
- El uso de `z` y `z'` no estaba gobernado por un umbral formal de incertidumbre del valor asignado.
- No existía una política suficientemente documentada para rondas con pocos participantes.
- La compatibilidad metrológica se reconocía como necesidad, pero debía conectarse mejor con decisiones sobre valor asignado y acciones de investigación.

Un aprendizaje crítico de esta fase fue separar dos conceptos que inicialmente tendían a mezclarse: la incertidumbre del valor asignado no debe usarse como sustituto de `sigma_pt`. Para el piloto, `sigma_pt` debía documentarse como criterio fitness-for-purpose o criterio prescrito, no como una derivación automática de la incertidumbre expandida.

### 2. Mejora de comunicaciones y reglas de relación con participantes

En la misma fase se trabajó la comunicación detallada del ensayo de aptitud. La documentación fue contrastada con modelos internacionales y con los requisitos de ISO/IEC 17043 sobre información pre-ronda.

Se incorporaron o prepararon mejoras sobre:

- Seguridad industrial y manejo de gases contaminantes criterio.
- Definición de `sigma_pt` y criterios estadísticos aplicables.
- Quejas y apelaciones, con plazos, canales, imparcialidad y protección del reclamante.
- Declaración explícita de no subcontratación o, cuando aplique, control de actividades subcontratadas.

En esta etapa también se corrigieron errores de exactitud normativa y técnica, como la referencia al Decreto 1072 de 2015 y la descripción de extintores ABC. El control de estos detalles es importante porque el SGC no solo debe ser técnicamente correcto, sino auditable.

### 3. Revisión del informe de resultados EA y plantilla Rmd

La revisión del informe de resultados `EA-2025-12-10_13-z-3-3` produjo una matriz normativa y una lista de hallazgos específicos por sección. El informe tenía una estructura técnica razonable y uso de Algoritmo A, pero se detectaron brechas de conformidad que podían afectar la interpretación de resultados.

Hallazgos principales:

- Fallos de homogeneidad/estabilidad aparecían reportados sin acción mitigatoria documentada.
- `sigma_pt` se derivaba de la variabilidad del grupo, lo que limita comparabilidad entre rondas.
- Faltaba una política explícita para grupos pequeños, con preferencia por valor de referencia trazable cuando no hay masa crítica de participantes.
- La compatibilidad metrológica se calculaba, pero no siempre generaba conclusión o acción.
- No estaban incorporados como alternativas documentadas `z'`, `zeta` o `En`.

También se registraron problemas de calidad documental en los borradores de instrucciones Rmd: citaciones ISO incorrectas, severidades no normalizadas, bloques Markdown/Rmd mal cerrados, símbolos `|` no escapados en tablas, dependencias de código no documentadas y placeholders sin responsable. El aprendizaje fue que las instrucciones técnicas deben ser ejecutables, trazables y renderizables, no solo conceptualmente correctas.

### 4. Diseño de documentos técnicos PSEA para prueba piloto

En abril se produjo una expansión importante de documentos operativos para la prueba piloto. Varios placeholders fueron convertidos en esqueletos estructurados de procedimientos, instructivos y formatos.

Documentos destacados:

- `I-PSEA-07 Diseno Estadistico`: formalizó el tratamiento de rondas con `n` bajo, valor de referencia trazable, `sigma_pt` prescrito y uso potencial de `z'` o `zeta`.
- `I-PSEA-08 Valor Asignado`: incorporó el modelo de incertidumbre combinada del valor asignado, incluyendo componentes de caracterización, homogeneidad y estabilidad.
- `I-PSEA-10 Homogeneidad y Estabilidad`: estructuró los controles para verificar el ítem de ensayo gaseoso.
- `I-PSEA-13 Validacion de Software`: definió datasets de referencia, incluyendo ejemplos de ISO 13528, y criterios de tolerancia numérica para revalidación.
- `F-PSEA-05A Hoja de Registro del Participante`: fue creado como formato nuevo para capturar información de participante y datos internos del coordinador.

También se hizo una distinción documental importante:

- `P-PSEA-20` gobierna comunicaciones: quién aprueba, cuándo se envía y por qué canal.
- `I-PSEA-09` operacionaliza instrucciones a participantes: qué contenido técnico debe recibir el laboratorio.

Otro aprendizaje clave fue la definición del ítem de ensayo en CALAIRE-EA: no es un cilindro físico enviado al participante, sino la atmósfera generada dinámicamente en el manifold. Los cilindros de referencia o de calibración son materiales auxiliares, no el ítem PT.

### 5. Reorganización por rondas y separación entre gestión y operación

La documentación de prueba piloto fue reorganizada para separar documentos de gobernanza, documentos operativos y formatos por ronda. La estructura permitió diferenciar:

- Ronda simple.
- Ronda compleja fase 1.
- Ronda compleja fase 2.
- Documentos de gestión transversal.

Los formatos `F-PSEA-05` a `F-PSEA-14` fueron adaptados por ronda, con campos específicos, trazabilidad normativa preservada y checkboxes de control para ejecución. La reorganización dejó explícita la comparabilidad entre rondas, especialmente para CO/SO2, al permitir contrastar resultados de diferentes participantes bajo una lógica documental común.

Esta fase fortaleció el vínculo entre el SGC y la ejecución real de la prueba piloto: la documentación dejó de ser un inventario genérico y pasó a modelar las rutas de trabajo por ronda.

### 6. Migración y consolidación en `docs/documentacion_sgc`

Durante las fases posteriores, el sistema documental activo pasó a concentrarse en `docs/documentacion_sgc`. La estructura actual incluye:

- `01_bloque_general/00_plantillas_base`
- `01_bloque_general/01_documentos_marco`
- `01_bloque_general/02_procedimientos`
- `01_bloque_general/03_instructivos`
- `01_bloque_general/04_formatos_maestros`
- `01_bloque_general/05_matrices_inventarios`
- `01_bloque_general/06_procedimientos_gestion`
- `02_prueba_piloto_rondas`

El historial Git registra hitos como:

- `7fb16a9` y `c8dbcdf`: cierre de fases del sistema de gestión documental ISO 17025/17043/13528.
- `bccafb7`: reorganización de documentos del SGC y depuración de duplicados.
- `f770e58`: revisión de fichas SGC PEA.
- `4fde0c2`: auditoría e integración de homogeneidad/estabilidad y `P-PSEA-23`.
- `42ce5fc`: copia de revisión como revisión A.
- `f5a937f`: aplicación de plantillas a documentos controlados SGC.
- `818ae00`: actualización de la estructura documental restante.

### 7. Fichas resumen y mapa de navegación del SGC PEA

En junio se elaboraron 56 fichas resumen para cubrir el universo documental del PEA. Estas fichas permitieron documentar propósito, rol en el flujo, aplicativo asociado, entradas, salidas, relaciones documentales, límites de alcance, riesgos de interpretación y criterio mínimo de elaboración.

Controles relevantes que quedaron preservados:

- `DG-PSEA-02` y `DG-PSEA-03` se tratan como documentos marco de aplicativos, no como formatos.
- `F-PSEA-10` se trata como registro de preprocesamiento, no como aplicativo.
- `F-PSEA-12` se distingue de `F-PSEA-14`.
- Homogeneidad y estabilidad se documentan mediante `F-PSEA-11` y subformatos `F-PSEA-11A-D`.
- Quejas y apelaciones se diferencian documentalmente.
- Los archivos técnicos internos se mapean dentro del flujo de datos y mejora continua, no como reemplazo de procedimientos controlados.

El mapa de navegación `mapa_navegacion_sgc_pea.html` fue desagrupado para mejorar trazabilidad. Se eliminaron nodos compuestos como `P-PSEA-02-05`, `P-PSEA-20-28` y `F-PSEA-13A-D`, reemplazándolos por nodos individuales con relaciones documentales propias. Esto mejora la lectura del sistema por código documental y reduce ambigüedad en auditorías.

### 8. Corrección de inconsistencias documentales

La revisión del mapeo detectó documentos cuyo nombre, ficha o contenido no estaban alineados. El caso `P-PSEA-14 Colusion y falsificacion` es representativo: el archivo existía bajo ese nombre, pero su contenido describía gestión de riesgos y oportunidades. La corrección reemplazó ese contenido por controles de colusión, falsificación, valores sensibles, confidencialidad y escalamiento a trabajo no conforme.

Este episodio dejó una regla operativa importante: cuando exista desalineación entre nombre y contenido, las fichas resumen pueden usarse como fuente primaria de criterio documental, pero no deben usarse para reconstruir documentos originales por analito o documentos fuente que el usuario haya identificado como válidos.

### 9. Problema crítico: sustitución indebida de procedimientos originales por gas

En junio se identificó una desviación importante: los procedimientos técnicos por analito habían sido sustituidos por documentos generados o transcritos bajo la numeración `P-PSEA-10` a `P-PSEA-13`. El usuario aclaró que estos archivos no debían reemplazar los procedimientos originales.

Fuentes originales válidas:

- `0P-PSEA-02 Procedimiento NO-NO2.docx`
- `0P-PSEA-03 Procedimiento CO_v2.docx`
- `0P-PSEA-04 Procedimiento O3_v2.docx`
- `0P-PSEA-05 Procedimiento SO2_v2.docx`

Corrección aplicada:

- Se eliminaron los procedimientos activos generados para gases en `.docx` y `.md`.
- Se copiaron los cuatro originales a la carpeta activa `01_bloque_general/02_procedimientos/`.
- Se renombraron como:
  - `P-PSEA-10 Procedimiento tecnico NO-NO2.docx`
  - `P-PSEA-11 Procedimiento tecnico CO.docx`
  - `P-PSEA-12 Procedimiento tecnico O3.docx`
  - `P-PSEA-13 Procedimiento tecnico SO2.docx`
- Se verificó con `cmp` que cada copia activa era byte-a-byte idéntica a su fuente original.

Aprendizaje preservado: los procedimientos por gas no deben reconstruirse desde fichas, Markdown generado ni transcripciones. Si se requiere cambiar numeración o ubicación, debe hacerse por copia o renombrado de los `.docx` originales.

### 10. Normalización documental con plantillas institucionales

La fase más reciente aplicó plantillas institucionales a documentos controlados. El trabajo se cerró en dos commits:

- `f5a937f Aplicar plantillas a documentos controlados SGC`
- `818ae00 Actualizar estructura documental SGC restante`

Para DOCX se usó Pandoc con `--reference-doc`. Para procedimientos e instructivos cuyas plantillas base estaban en `.doc`, se convirtieron copias temporales a `.docx` mediante LibreOffice. Para XLSX se partió de `F-PSEA-01 Plantilla Formato_Excel.xlsx`, incorporando una hoja `Datos` con filas de los CSV fuente.

Hubo un problema metodológico en esta fase: inicialmente se trató la conversión automática como equivalente a copiar y pegar manualmente contenido dentro de plantillas Word/Excel. El usuario rechazó el enfoque inicial. La solución fue restaurar desde respaldo, registrar el intento descartado y reaplicar la conversión con Pandoc como método pragmático explícitamente aceptado.

Aprendizajes:

- Pandoc con plantilla de referencia no equivale a copia manual en Word; aplica estilos y estructura, pero puede no preservar formato fino.
- En reemplazos masivos de Office deben mantenerse respaldos temporales.
- Los commits deben separarse por alcance: primero documentos controlados, luego reorganización, auxiliares y vistas derivadas.
- Si aparece una objeción de formato, se debe revisar el archivo específico antes de rehacer masivamente.

## Estado actual del SGC PEA

El SGC PEA cuenta actualmente con una estructura documental amplia y navegable, documentos marco, procedimientos, instructivos, formatos maestros, matrices de inventario, fichas resumen, mapa de navegación y documentos por ronda piloto. El sistema ya no es solo un conjunto de archivos aislados: existe una arquitectura documental con relaciones entre planeación, comunicación, preparación de ítem, datos, análisis, informes, quejas, apelaciones, competencia, proveedores y mejora continua.

Los elementos más maduros son:

- Arquitectura documental y clasificación por bloques.
- Trazabilidad entre documentos, fichas y mapa de navegación.
- Integración de criterios ISO 17043 e ISO 13528 en diseño estadístico, valor asignado, homogeneidad/estabilidad e informes.
- Documentación de flujo digital de datos y relación con `calaire-app` y `pt_app`.
- Formatos de ronda piloto con estructura operativa reutilizable.
- Plantillas institucionales aplicadas a documentos controlados.

Los puntos que requieren control continuo son:

- Revisión visual fina de DOCX generados por Pandoc.
- Preservación estricta de procedimientos originales por gas.
- Consistencia entre fichas, mapa, inventario y documentos activos.
- Cierre de placeholders deliberadamente preliminares.
- Validación de que los criterios estadísticos documentados coincidan con el código y los informes generados.

## Problemas y aprendizajes transversales

| Tema | Problema detectado | Aprendizaje preservado |
|---|---|---|
| Estadística EA | Se confundía `sigma_pt` con incertidumbre expandida | Documentar `sigma_pt` como criterio de desempeño, preferiblemente fitness-for-purpose o prescrito |
| H/E | Fallos reportados sin acción mitigatoria | Documentar impacto, expansión de incertidumbre o decisión técnica ante incumplimiento |
| Rmd/Markdown | Fences, tablas y fórmulas podían romper renderizado | Validar estructura antes de usar instrucciones como fuente operativa |
| Mapeo documental | Nodos agrupados reducían trazabilidad | Desagrupar códigos documentales críticos en mapa y fichas |
| Procedimientos por gas | Se sustituyeron originales por documentos generados | Mantener `.docx` originales como fuente válida y no reconstruirlos |
| Plantillas Office | Conversión automática presentada como copia manual | Explicitar límites de Pandoc y conservar respaldos |
| JSON/checklists | Sustitución por campos repetidos escribió evidencia en entrada incorrecta | Editar por contexto completo o validar inmediatamente por `id` |

## Hitos rescatados del historial Git

- `c32998d Completar Fase 5: Implementar ajustes ISO en P-PSEA-01`: consolidó mejoras normativas en el protocolo general.
- `5546b41 correccion: declaracion explicita de NO subcontratacion en EA`: cerró una brecha de comunicación y responsabilidad.
- `7fb16a9 Fases 1-4 completadas: Sistema de Gestión Documental ISO 17025/17043/13528`: marcó una consolidación temprana del sistema documental.
- `bccafb7 docs: reorganizar documentos del SGC y depurar duplicados en raiz`: contribuyó a pasar de archivos dispersos a estructura documental más limpia.
- `4fde0c2 docs(sgc): completar Fase 10 (auditoria e integracion H/E y P-PSEA-23)`: integró el componente de homogeneidad/estabilidad y flujo técnico de datos.
- `f770e58 Completar revision de fichas SGC PEA`: cerró la revisión de fichas resumen como capa de navegación y control.
- `42ce5fc docs(sgc): guardar copia de la revision como revision a`: preservó una versión de revisión.
- `f5a937f Aplicar plantillas a documentos controlados SGC`: creó documentos controlados con plantillas institucionales.
- `818ae00 Actualizar estructura documental SGC restante`: completó reorganización, auxiliares, mapas, fichas y documentos asociados.

## Conclusión

La evolución del SGC PEA muestra un tránsito desde documentos técnicos y comunicaciones dispersas hacia un sistema documental controlado, trazable y alineado con ISO/IEC 17043:2023 e ISO 13528:2022. El avance principal no fue solo producir archivos, sino establecer reglas de interpretación: qué documento gobierna cada parte del proceso, qué registros evidencian cada actividad, qué criterios estadísticos aplican, cómo se tratan desviaciones, y qué fuentes originales no deben ser reemplazadas.

El principal riesgo actual no es la falta de documentación, sino la pérdida de consistencia entre documentos activos, fichas, mapas, plantillas y fuentes originales. Por eso el control futuro debe enfocarse en mantener sincronizados inventario, mapa de navegación, fichas resumen, documentos controlados y registros de ronda.
