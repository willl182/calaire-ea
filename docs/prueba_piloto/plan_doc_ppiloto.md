# Plan Documental de la Prueba Piloto PSEA

## Objetivo

Este documento consolida la documentación mínima y complementaria requerida para ejecutar, registrar, analizar y cerrar la prueba piloto del esquema PSEA de gases contaminantes criterio. La priorización se basa en la evaluación consolidada del SGC contenida en `docs/docs_sgc/202510 Documentacion SGC/evaluacion_planificacion_sgc.md`, con énfasis en los documentos que habilitan la operación real de las rondas piloto antes de la acreditación formal.

## Alcance del plan

El presente plan aplica a la prueba piloto actualmente estructurada en dos rondas activas:

- **Ronda simple:** CO y SO2 con un participante (`P1 = SIATA`)
- **Ronda doble:** O3, NO y NO2 con dos participantes (`P1 = SIATA`, `P2 = Universidad Pontificia Bolivariana`)

El criterio de este plan no es completar todo el SGC del proveedor de ensayos de aptitud, sino asegurar que la prueba piloto quede:

- técnicamente ejecutable;
- documentalmente trazable;
- consistente con ISO/IEC 17043:2023 e ISO 13528:2022;
- utilizable como evidencia para cierre de brechas del PSEA.

## Criterios de priorización

La documentación se organiza en tres niveles:

1. **Crítica para ejecutar la prueba piloto:** sin estos documentos no es posible planificar, operar, analizar o reportar la ronda de forma controlada.
2. **Necesaria para cierre documental del piloto:** documentos que formalizan aceptación, tratamiento de datos, registros de soporte y control de incidencias.
3. **Complementaria para robustecimiento SGC:** documentos necesarios para dejar el piloto plenamente alineado con la estructura del SGC, aunque no todos bloquean el arranque operativo inmediato.

## Paquete documental crítico para ejecutar la prueba piloto

### Procedimientos

| Código | Documento | Estado de referencia | Función en la prueba piloto | Acción requerida |
|---|---|---|---|---|
| `P-PSEA-09` | Procedimiento de Planificación de Ronda EA | Existente, con duplicidad de versión | Define calendario, cronograma, recursos, secuencia de actividades y control de cambios de la ronda | Consolidar una sola versión vigente y expandirla según el piloto activo |
| `P-PSEA-06` | Procedimiento de Diseño Estadístico | Existente en borrador | Define valor asignado, `σ_pt`, criterio de aptitud, scoring y tratamiento de datos | Revisar y fijar criterios específicos para gases y n bajo |
| `P-PSEA-07` | Procedimiento de Informe de Resultados | Existente en borrador | Establece estructura, aprobación y emisión del informe final del piloto | Actualizar contenido mínimo conforme a 7.4.3 |
| `P-PSEA-02` | Procedimiento NO-NO2 | Existente en borrador | Soporta la operación técnica de la ronda doble | Verificar coherencia con secuencia piloto |
| `P-PSEA-03` | Procedimiento CO | Existente en borrador | Soporta la ronda simple | Verificar coherencia con secuencia piloto |
| `P-PSEA-04` | Procedimiento O3 | Existente en borrador | Soporta la ronda doble | Verificar coherencia con secuencia piloto |
| `P-PSEA-05` | Procedimiento SO2 | Existente en borrador | Soporta la ronda simple | Verificar coherencia con secuencia piloto |

### Instructivos

| Código | Documento | Estado de referencia | Función en la prueba piloto | Acción requerida |
|---|---|---|---|---|
| `I-PSEA-10` | Instrucciones a Participantes | Faltante en la arquitectura consolidada | Comunica requisitos previos, datos a reportar, formato, plazos, cifras significativas y reglas de participación | Redactar y emitir como instructivo formal pre-ronda |
| `I-PSEA-11` | Homogeneidad y Estabilidad para atmósferas generadas | Faltante en la arquitectura consolidada | Define la verificación previa del desempeño del sistema generador y la aceptabilidad del ítem PT | Redactar con adaptación explícita al contexto in situ |
| `I-PSEA-12` | Revisión y Gestión de Datos | Faltante en la arquitectura consolidada | Define revisión de consistencia, unidades, exclusiones justificadas y preparación del análisis | Redactar antes del procesamiento oficial de resultados |
| `I-PSEA-01` | Embalaje y Transporte | Existente en borrador | Da soporte a logística, manipulación, entrega, recepción o retiro de equipos/items cuando aplique | Ajustar al flujo real del piloto in situ |

### Formatos y registros

| Código | Documento | Estado de referencia | Función en la prueba piloto | Acción requerida |
|---|---|---|---|---|
| `F-PSEA-01` | Calendario Tipo | Existente | Base de programación general de la ronda | Ajustar a las dos rondas activas |
| `F-PSEA-02` | Cronograma Detallado | Existente | Secuencia operativa diaria de montaje, calibración, medición y cierre | Mantener como formato maestro del piloto |
| `F-PSEA-03` | Registro de Planificación de Ronda | Existente | Evidencia de decisiones, versiones y ajustes de planificación | Usar como registro oficial del piloto |
| `F-PSEA-04` | Formato Informe de Resultados | Existente | Plantilla base del informe emitido al cierre | Completar contenido mínimo y responsables de aprobación |
| `F-PSEA-05` | Confirmación de Participación | Parcialmente identificado | Evidencia aceptación del participante y condiciones de ejecución | Formalizar formato vigente |
| `F-PSEA-06` | Plan de Ronda EA | Faltante | Consolidación de participantes, analitos, recursos, fechas y responsables por ronda | Crear |
| `F-PSEA-07` | Lista Maestra de Participantes | Faltante | Control de participantes, códigos, contactos y estado de confirmación | Crear |
| `F-PSEA-08` | Registro de Preparación del Ítem | Faltante | Evidencia preparación del sistema generador, mezclas, setpoints y condiciones operativas | Crear |
| `F-PSEA-09` | Registro de Homogeneidad | Faltante | Evidencia resultados y aceptación de homogeneidad | Crear |
| `F-PSEA-10` | Registro de Estabilidad | Faltante | Evidencia estabilidad intrajornada o durante ventana de medición | Crear |
| `F-PSEA-11` | Registro de Envío y Recepción | Faltante | Trazabilidad logística de entrega, instalación, retiro o recepción | Adaptar al piloto in situ |
| `F-PSEA-12` | Formato de Reporte del Participante | Faltante | Captura estructurada de resultados reportados por cada laboratorio | Crear |
| `F-PSEA-13` | Hoja de Revisión de Datos | Faltante | Evidencia revisión técnica previa al análisis estadístico | Crear |
| `F-PSEA-14` | Hoja de Cálculo y Aprobación Estadística | Faltante | Evidencia técnica del cálculo, revisión y aprobación de resultados | Crear |

## Paquete documental necesario para cierre documental del piloto

Estos documentos no siempre bloquean el inicio de la ronda, pero sí son necesarios para que el piloto quede administrativamente sólido y usable como evidencia formal del PSEA.

### Procedimientos

| Código | Documento | Justificación |
|---|---|---|
| `P-PSEA-21` | Revisión de Solicitudes, Contratos y Comunicación con Participantes | Formaliza aceptación de participantes, condiciones del servicio y comunicaciones previas |
| `P-PSEA-15` | Gestión de Riesgos y Oportunidades | Permite documentar riesgos operativos, logísticos y de imparcialidad asociados al piloto |
| `P-PSEA-25` | Quejas | Requerido para recepción y tratamiento de inconformidades de participantes |
| `P-PSEA-26` | Apelaciones | Requerido para revisión formal de controversias sobre resultados o tratamiento del piloto |

### Formatos

| Código | Documento | Justificación |
|---|---|---|
| `F-PSEA-15` | Registro de No Conformidad / CAPA | Permite trazabilidad de desviaciones detectadas durante ejecución |
| `F-PSEA-16` | Registro de Quejas | Evidencia de tratamiento formal de reclamaciones |
| `F-PSEA-17` | Registro de Apelaciones | Evidencia de tratamiento formal de apelaciones |

## Paquete documental complementario para robustecimiento SGC

Estos documentos fortalecen la defensa del piloto ante revisión documental y ayudan a reutilizar la experiencia del piloto para la acreditación futura.

| Código | Documento | Justificación |
|---|---|---|
| `I-PSEA-14` | Validación de Software y Sistemas | Necesario si el aplicativo R/Shiny soporta el cálculo oficial del piloto |
| `P-PSEA-13` | Control Documental del PEA | Ordena emisión, cambios, codificación y vigencia de documentos del piloto |
| `P-PSEA-14` | Control de Registros del PEA | Define retención, respaldo y trazabilidad de los registros generados |
| `P-PSEA-17` | No Conformidades y Acciones Correctivas del PEA | Permite cierre sistémico de hallazgos surgidos en el piloto |
| `P-PSEA-20` | Imparcialidad | Necesario para separar funciones del proveedor y del laboratorio de referencia |
| `P-PSEA-27` | Confidencialidad | Necesario para codificación de participantes y control del uso de resultados |
| `P-PSEA-28` | Competencia y Autorización del Personal del PEA | Formaliza la habilitación del personal que participa en el piloto |
| `P-PSEA-30` | Proveedores Externos del PEA | Aplica si intervienen CRM, servicios externos, transporte o soporte subcontratado |

## Orden recomendado de elaboración

### Fase 1. Cierre del núcleo operativo

1. Consolidar `P-PSEA-09`
2. Revisar y fijar versión operativa de `P-PSEA-06`
3. Ajustar `P-PSEA-07`
4. Verificar coherencia técnica de `P-PSEA-02` a `P-PSEA-05`
5. Crear `I-PSEA-10`, `I-PSEA-11` e `I-PSEA-12`
6. Completar `F-PSEA-05` a `F-PSEA-14`

### Fase 2. Cierre de soporte documental del piloto

1. Formalizar `P-PSEA-21`
2. Formalizar `P-PSEA-15`
3. Formalizar `P-PSEA-25` y `P-PSEA-26`
4. Crear `F-PSEA-15`, `F-PSEA-16` y `F-PSEA-17`

### Fase 3. Robustecimiento para trazabilidad SGC

1. Formalizar `I-PSEA-14`
2. Integrar control documental y control de registros
3. Cerrar definiciones de imparcialidad, confidencialidad, competencia y proveedores

## Riesgos documentales identificados

- Existe duplicidad de versiones de `P-PSEA-09`, lo que impide definir con claridad el documento vigente.
- La codificación propuesta en la evaluación consolidada no coincide plenamente con otros inventarios y diccionarios documentales previos; antes de emitir nuevos controlados debe fijarse una nomenclatura única.
- Algunos instructivos y formatos aparecen en listas distintas con numeración diferente en documentos previos del SGC; conviene homologarlos antes de aprobación.
- Si el aplicativo produce el cálculo oficial del piloto, la ausencia de un instructivo de validación de software debilita la trazabilidad técnica del resultado.

## Resultado esperado del plan

Al cerrar este plan documental, la prueba piloto deberá contar con un paquete documental suficiente para:

- planificar las rondas con trazabilidad;
- ejecutar las actividades técnicas con instrucciones formales;
- registrar preparación, condiciones, resultados y revisión de datos;
- emitir el informe de resultados del piloto bajo una estructura controlada;
- documentar desviaciones, quejas o apelaciones si se presentan;
- reutilizar la experiencia del piloto como evidencia para el fortalecimiento del SGC del PSEA.
