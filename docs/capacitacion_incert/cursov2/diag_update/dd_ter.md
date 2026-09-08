# Diagnóstico final integrado y propuesta de arquitectura documental

## Curso de incertidumbre de medición para operadores de redes de calidad del aire

**Directorio evaluado:** `docs/capacitacion_incert/cursov2/`  
**Fecha:** 2026-08-28  
**Alcance:** arquitectura pedagógica, documental y de producción de los módulos, handouts, solucionarios, protocolos y futuras diapositivas.  
**Estado:** propuesta de diagnóstico; no modifica el contenido didáctico existente.

---

## 1. Conclusión ejecutiva

El curso no presenta una carencia técnica sustantiva ni necesita reconstruirse desde cero. El problema principal es que sus productos documentales tienen **funciones y audiencias diferentes, pero esas funciones no están declaradas ni gobernadas como una cadena de derivación**.

Los módulos M1–M8 ya contienen gran parte de la capa más completa del curso: teoría, secuencia pedagógica, minutaje, instrucciones de facilitación, ejercicios, resultados esperados, errores frecuentes y referencias. Al mismo tiempo, en esos mismos archivos está embebida una parte importante de la explicación que debería recibir el participante. El handout O₃ intenta suplir esa explicación, pero mezcla narrativa básica con consulta avanzada; el handout NOx funciona de hecho como referencia operativa, aunque su función aún no se declara. Las diapositivas aún no existen como capas separadas.

Por tanto, el trabajo prioritario es editorial y arquitectónico:

1. declarar una fuente meta canónica para autor e instructor;
2. derivar de ella un material teórico continuo para el participante;
3. reclasificar los handouts según su uso real;
4. corregir el orden de introducción de los conceptos metrológicos críticos;
5. establecer reglas y, después, mecanismos reproducibles de derivación hacia referencias, solucionarios y diapositivas.

---

## 2. Modelo documental objetivo

La arquitectura propuesta distingue cuatro capas en secuencia y cuatro productos auxiliares. La relación entre la capa meta y el material del participante es de **superconjunto**: no son documentos hermanos que se reescriben por separado.

| Capa o producto | Audiencia | Función | Estado actual |
|---|---|---|---|
| **0. Meta maestro** | Autor e instructor | Fuente pedagógica completa: teoría, discurso, tiempos, decisiones docentes, ejercicios, respuestas y referencias. | Existe de forma distribuida en M1–M8 y solucionarios; no está declarado como tal. |
| **1. Material teórico del participante** | Participante | Narrativa completa, limpia y conservable; permite comprender el curso después de la sesión. | Existe parcialmente, mezclado con capa 0 y con el handout O₃. |
| **2. Guion textual de diapositivas** | Instructor / producción | Síntesis telegráfica de la capa 1: títulos, ideas y puntos esenciales. | No existe como producto separado. |
| **3. Diapositivas visuales** | Participante en aula | Diseño, diagramas, imágenes y jerarquía visual sin teoría nueva. | No existe como producto separado. |
| **R. Referencias, anexos y fichas** | Participante e instructor según uso | Consulta, profundización y apoyo operativo; no reemplaza el relato principal. | Existe, pero bajo el rótulo ambiguo de “handout”. |
| **Protocolos prácticos** | Participante e instructor en campo/laboratorio | Conducen una actividad completa y autónoma. | Existen; requieren reglas de autonomía controlada. |
| **Solucionarios** | Instructor | Resolución, corrección y variantes aceptables. | Existen; deben conservarse privados y no duplicar doctrina. |
| **Salidas de lectura/compilación** | Distribución | Versiones generadas para consulta o entrega. | `solo_md/` existe fuera de control de derivación. |

La cadena deseada es:

```text
META MAESTRO
    ├── MATERIAL TEÓRICO DEL PARTICIPANTE
    │       └── GUION TEXTUAL DE DIAPOSITIVAS
    │               └── DIAPOSITIVAS VISUALES
    ├── ANEXOS TÉCNICOS Y REFERENCIAS
    ├── FICHAS OPERATIVAS
    ├── PROTOCOLOS PRÁCTICOS
    └── SOLUCIONARIOS DEL INSTRUCTOR
```

Si se necesita una lectura continua del meta maestro, debe ensamblarse desde M1–M8; no debe crearse una copia manual adicional.

---

## 3. Hallazgos que sustentan el diagnóstico

### 3.1 La capa meta y la capa del participante comparten archivos

Los módulos actuales contienen, además de contenido conceptual, ficha, objetivos, distribución de tiempo, indicaciones de aula, preguntas, resultados esperados, errores frecuentes y transiciones. El inventario realizado sobre los ocho módulos estima que el **42 % de `modulos/` corresponde a meta pura** (información dirigida solo al instructor). El resto sigue siendo mixto: por ejemplo, los guiones de exposición incluyen minutajes, apuntes al handout y respuestas anticipadas.

Esto no significa que los módulos estén mal escritos. Significa que funcionan como una versión meta distribuida. El defecto es no haber declarado ese papel ni disponer de una extracción limpia para el participante.

Ejemplos de información apropiada para la capa meta, no para el entregable principal, son los resultados numéricos anticipados de ejercicios en M2 y M4, y las conclusiones previstas de la demostración de M8.

### 3.2 El handout O₃ tiene dos roles incompatibles

El handout de GUM/O₃ combina:

- contenido básico indispensable para seguir el curso: significado de `u`, `u_c`, `U`, `k`, cobertura, redondeo, vocabulario metrológico y elementos de informe;
- consulta avanzada legítima: tratamiento detallado de autocorrelación, distribuciones especiales, Welch–Satterthwaite, Cholesky y desarrollo extendido del método de Monte Carlo.

También se verifican solapamientos claros entre módulos y handout: PDFs y divisores (M3 / `O3_H03`), coeficientes de sensibilidad y propagación (M2 / `O3_H04`), informe GUM (M7 / `O3_H07`) y trazabilidad (M1 / `O3_H01`). La causa del problema no es la repetición por sí misma, sino que hoy no se sabe qué versión es canónica, cuál es resumen y cuál es ampliación.

La consecuencia propuesta es conservar el handout O₃, pero dividir explícitamente su función:

- integrar al material teórico del participante todo lo necesario para el recorrido obligatorio;
- conservar como anexos técnicos los desarrollos que amplían, derivan o cubren casos especiales;
- mantener glosario, tablas, fórmulas y checklist como referencias localizables.

### 3.3 El handout NOx ya se comporta como una ficha de referencia

El handout NOx es mucho más breve y no equivale funcionalmente al de O₃. Resume, apoya controles documentales y sirve como recordatorio de fórmulas y verificaciones; en varios temas M6 contiene más profundidad.

No conviene forzar una simetría artificial entre ambos. Debe declararse como **ficha operativa o referencia rápida**, útil durante práctica, operación, auditoría y consulta posterior.

### 3.4 Hay una inversión en el orden de los términos metrológicos

La inquietud original es válida: en M1 y M2 aparecen incertidumbre estándar, corrección, incertidumbre residual, doble conteo, covarianza, mensurando y coeficientes de sensibilidad antes de que varios de ellos se definan formalmente. La secuencia `u_i → u_c → U = k·u_c` tampoco tiene hoy un dueño docente plenamente explícito.

El glosario y parte de las definiciones existen, pero aparecen tarde o se delegan a una referencia cuya lectura previa no está indicada. En particular, M1 se presenta como fundamento de vocabulario, pero remite al handout para distinciones fundamentales; M3 introduce formalmente Tipo A/B, PDF y combinación cuando ya se han usado conceptos relacionados.

La recomendación no es anteponer un glosario extenso. Es combinar tres mecanismos:

1. un **bloque M0 breve** (15–20 min, recomendado cuando no haya prelectura garantizada) con mensurando, error/corrección/incertidumbre, trazabilidad, `u`, `u_c`, `U`, `k` y la distinción mínima Tipo A/B;
2. una definición completa de cada concepto inmediatamente antes de que se aplique de forma exigente;
3. un glosario de consulta para repaso y trabajo posterior.

Si se opta por prelectura en vez de M0, `O3_H00`, `O3_H01` y el glosario deben declararse de forma explícita como obligatorios. Para operadores de red, M0 es la opción más robusta.

### 3.5 Existen otros saltos conceptuales y ambigüedades de lenguaje

- M7 exige un resultado auditable conforme a GUM §7, pero la guía más completa de informe, cobertura, redondeo y coherencia vive fuera de la narrativa principal. Debe enseñarse antes del taller integrador.
- “Cobertura” se usa tanto en sentido GUM como para alcance de evidencia y matriz documental. Se propone reservar **cobertura** para el significado metrológico y usar **alcance de la evidencia** en los demás casos.
- M5, M6 y M8 no tienen el mismo grado de discurso redactado que los demás módulos. Para convertirlos en material del participante no basta con extraer bloques: habrá que completar la narrativa.
- Existen tres convenciones para la misma función (`Guion dictable`, `Párrafo dictable` y prosa sin etiqueta), lo que dificulta una derivación uniforme.

### 3.6 Hay riesgo de divergencia en copias derivadas

`solo_md/` replica el árbol de documentos para lectura externa, pero no está generado por el proceso de compilación ni está controlado en git; ya presenta diferencias con `modulos/`. El cambio actual parece benigno —enlaces desanclados—, pero el patrón es el mismo que genera drift: dos copias de un mismo discurso mantenidas por separado.

Existe un precedente técnico útil: `build_paquete_html.py` ya valida archivos, tablas, anclas, IDs y recursos. La futura derivación puede aprovechar ese enfoque en vez de sostener copias manuales.

---

## 4. Autoridad y contenido de cada producto

### 4.1 Meta maestro privado

Debe conservar:

- teoría completa y secuencia argumental;
- propósito de cada bloque, transiciones y minutaje;
- instrucciones de facilitación, preguntas, variantes y puntos de énfasis;
- ejercicios, respuestas breves, resultados esperados y errores frecuentes;
- referencias exactas y justificación de decisiones didácticas;
- criterios de evaluación y vínculos con prácticas.

Su pregunta rectora es: **¿qué necesita saber y tener disponible el instructor para enseñar bien este bloque?**

### 4.2 Material teórico del participante

Se deriva del meta maestro y debe conservar explicación, definiciones, ecuaciones necesarias, ejemplos, figuras, síntesis, ejercicios sin solución anticipada y referencias pertinentes. Elimina minutaje, instrucciones de aula, comentarios editoriales, respuestas, resultados de demostraciones y decisiones internas.

Debe leerse como un manual breve y continuo. Puede estar dividido en capítulos M1–M8, pero no debe requerir otra fuente para completar conceptos básicos obligatorios.

### 4.3 Anexos técnicos y fichas operativas

Los anexos técnicos amplían el recorrido principal sin repararlo. Las fichas contienen solo lo necesario para consulta rápida: fórmulas, controles, criterios de aceptación y advertencias. Ambos deben declarar destinatario y momento de uso.

### 4.4 Protocolos y solucionarios

Los protocolos pueden repetir fórmulas, criterios y advertencias para permitir ejecución autónoma, pero deben remitir al material teórico para el fundamento y conservar idéntica notación. Los solucionarios permanecen privados: incluyen cálculo paso a paso, criterios de corrección y variantes aceptables, sin convertirse en una fuente teórica paralela.

### 4.5 Diapositivas

El guion textual reduce el material teórico a ideas y frases esenciales. Las diapositivas visuales agregan composición, diagramas, imágenes y tablas simplificadas. Ninguna debe introducir teoría por primera vez: las diapositivas **reducen e ilustran; no amplían**.

---

## 5. Reglas de gobierno y derivación

1. **Una idea nueva nace en la capa meta.** Ningún protocolo, solucionario o diapositiva introduce silenciosamente un concepto ajeno a ella.
2. **Autoridad definida.** El meta maestro es canónico para contenido técnico, definiciones, ecuaciones, notación e intención pedagógica; el material teórico lo es para orden y experiencia de lectura del participante.
3. **Anexos sin dependencia oculta.** El recorrido obligatorio debe ser comprensible sin leer anexos avanzados.
4. **Repetición deliberada.** Fichas y protocolos solo duplican lo indispensable para su propósito operativo.
5. **Respuestas fuera del entregable.** El participante recibe enunciados, criterios y orientación, no soluciones reveladas de antemano.
6. **Un dueño por concepto.** Los demás módulos recuerdan o aplican, pero no redefinen de forma paralela.
7. **Derivación verificable.** Toda salida destinada a distribuirse debe poder reproducirse desde fuentes declaradas; no se mantienen copias narrativas manuales.

Una distribución conceptual inicial razonable es:

| Módulo | Conceptos de los que es dueño principal |
|---|---|
| M0 | Vocabulario de orientación: mensurando, error, corrección, incertidumbre, trazabilidad, `u`, `u_c`, `U`, `k`, Tipo A/B mínimo. |
| M1 | Trazabilidad aplicada y arquitectura metrológica. |
| M2 | Modelo de medición y coeficientes de sensibilidad. |
| M3 | Incertidumbre estándar, Tipo A/B, PDFs y combinación. |
| M4 | Presupuesto, contribuciones, doble conteo, cobertura, `U`, `k` y redondeo. |
| M5 | Patrones, regresión, residuos y alcance de la evidencia. |
| M6 | Modelo NOx, interferencias y covarianza. |
| M7 | Integración, declaración del resultado e informe GUM. |
| M8 | Validación opcional mediante Monte Carlo. |

---

## 6. Mecanismo de implementación recomendado

Antes de automatizar, conviene estabilizar una convención editorial única por bloque. Por ejemplo:

```markdown
### N. Título — minutaje                         ← capa 0

**Idea fuerza:**                                  ← semilla de capa 2
**Guion para participante:**                      ← capas 0 y 1
**Puntos para diapositiva:**                      ← capa 2
**Apoyo visual:**                                 ← capa 3
**Nota de facilitación:**                         ← capa 0
**Referencias:**                                  ← completa en 0; versión breve en 1
**Referencia de consulta:**                       ← puntero a R
```

No es obligatorio que la primera implementación sea un generador automático. Pero la estructura debe permitirlo, y evitar que cada producto se convierta en una reescritura no rastreable. Cuando los módulos estén normalizados, un único proceso de compilación puede generar el material del participante, guiones de diapositiva y `solo_md/`, aprovechando el patrón de validación ya presente en `build_paquete_html.py`.

---

## 7. Plan de trabajo por dependencia

| Prioridad | Acción | Resultado esperado |
|---|---|---|
| 1 | Declarar en `README.md` las capas, su audiencia y el uso de cada familia documental. | Se elimina la ambigüedad sobre módulos, handouts y referencias. |
| 2 | Decidir e introducir M0, o declarar prelectura obligatoria; se recomienda M0. | Ningún concepto crítico se exige antes de una orientación mínima. |
| 3 | Fijar plantilla editorial común y aplicarla primero a M5. | Piloto en el módulo con mayor déficit de narrativa y estructura. |
| 4 | Normalizar M1–M4 y M7; redactar el discurso faltante en M5, M6 y M8. | Material del participante extraíble y coherente en los ocho módulos. |
| 5 | Construir el material teórico continuo; integrar en él el contenido básico de O₃ y la preparación para M7. | Entregable principal autónomo, sin soluciones anticipadas. |
| 6 | Reclasificar O₃ como anexos/glosario/checklists y NOx como ficha operativa. | Las referencias complementan, no compiten con la narrativa. |
| 7 | Gobernar o generar `solo_md/`; después implementar compilación de capas 1–3. | Salidas reproducibles y sin drift. |
| 8 | Producir guion textual y luego diapositivas visuales. | Presentación consistente con la narrativa ya estabilizada. |

Las capas de diapositivas deben comenzar al final de esta secuencia. Con aproximadamente 462 minutos de curso obligatorio, una referencia razonable es del orden de 150–200 diapositivas a 2–3 minutos por diapositiva; producirlas antes de fijar la narrativa multiplicaría el trabajo de revisión.

---

## 8. Valoración final

El contenido técnico, la trazabilidad de fuentes, los datasets reproducibles y la separación entre curso teórico y práctica están bien encaminados. El desfase es principalmente **de una capa y media**, no de fundamento: la capa meta está avanzada, la narrativa entregable está incompleta y las capas de presentación aún no han sido formalizadas.

La decisión clave es reconocer que los módulos no son un handout defectuoso: son la materia prima madura de un meta maestro. A partir de esa decisión, el curso puede pasar de documentos valiosos pero superpuestos a una familia coherente de productos, cada uno con una audiencia, profundidad, autoridad y método de actualización claros.
