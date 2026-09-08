# Diagnóstico final y arquitectura documental propuesta

## Curso de incertidumbre de medición para operadores de redes de calidad del aire

**Directorio evaluado:** `docs/capacitacion_incert/cursov2/`  
**Alcance:** arquitectura pedagógica y documental del curso; relación entre módulos, handouts, solucionarios, prácticas y futuras diapositivas.  
**Propósito:** consolidar el diagnóstico alcanzado después de aclarar el flujo real de autoría y uso del material.

---

## 1. Punto de partida

La evaluación comenzó con tres inquietudes:

1. si los términos metrológicos debían aclararse antes de iniciar los módulos;
2. si los módulos omitían contenido importante que había quedado únicamente en los handouts;
3. si los módulos ya funcionaban, en la práctica, como su propio handout.

La primera lectura mostraba una mezcla de funciones. Los módulos contienen teoría, discurso, minutaje, instrucciones docentes, ejercicios, resultados y errores frecuentes. El handout de O₃ contiene tanto conceptos básicos como desarrollos avanzados. El handout de NOx resume parte de M6, pero no alcanza su profundidad. Los protocolos prácticos vuelven a explicar algunos conceptos para poder utilizarse de forma autónoma.

Con esa información, parecía que los módulos estaban sobrecargados y que competían con los handouts como material del participante. Esa interpretación era incompleta porque faltaba declarar una pieza central del método de trabajo: la **versión meta del curso**.

---

## 2. Aclaración decisiva: la función meta ya existe

El flujo de autoría no comienza con el material que recibe el participante. Comienza con una capa más amplia, privada y cargada, que sirve al autor y al instructor.

En el estado actual, esa función meta existe de manera distribuida, principalmente en los módulos M1–M8, pero todavía no está declarada ni gobernada como sistema. La decisión propuesta es tratarlos como capítulos coordinados del **meta maestro canónico**. Si se necesita una lectura continua, debe producirse mediante un ensamblado generado desde M1–M8, nunca mediante otra copia mantenida manualmente.

El meta maestro objetivo debe contener:

- teoría completa;
- hilo narrativo cercano al discurso oral;
- propósito de cada bloque;
- secuencia pedagógica;
- transiciones;
- minutaje;
- instrucciones de facilitación;
- preguntas para el grupo;
- ejercicios y respuestas;
- resultados esperados;
- errores frecuentes;
- advertencias y puntos de énfasis;
- variantes según tiempo o nivel del grupo;
- contenido opcional;
- referencias y justificaciones;
- decisiones sobre qué incluir, simplificar o dejar como consulta.

Su pregunta rectora es:

> ¿Qué necesito saber, recordar y tener disponible para enseñar bien este bloque?

Esta pieza no es un handout ni debe entregarse directamente al participante. Es la fuente pedagógica superior del curso.

Al reconocer esta capa, cambia el diagnóstico: la densidad de los módulos, sus respuestas, su minutaje y sus instrucciones no son defectos por sí mismos. Son características coherentes con una versión meta. El problema real es que ese rol no está declarado y no existe todavía una derivación limpia y sistemática hacia los demás productos.

---

## 3. Flujo autoral correcto

El flujo deseado tiene cuatro capas principales y varios productos auxiliares.

### 3.1 Capa 0: versión meta del autor e instructor

Es la fuente pedagógica más completa. Conserva teoría, relato oral y decisiones docentes. Debe permitir preparar, impartir, ajustar y actualizar el curso.

Actualmente, los módulos M1–M8 forman una fuente meta distribuida. El estado objetivo debe tratarlos como capítulos coordinados de un meta maestro y, si se necesita una lectura continua, ensamblarlos sin crear otra copia mantenida manualmente.

### 3.2 Capa 1: material teórico del participante

Se deriva de la versión meta. Mantiene:

- explicación completa;
- hilo narrativo lógico y consecuente;
- conceptos y definiciones;
- ecuaciones necesarias;
- ejemplos;
- figuras y tablas útiles;
- síntesis;
- ejercicios apropiados;
- referencias pertinentes.

Elimina o separa:

- minutaje;
- instrucciones como “dictar”, “preguntar” o “mostrar”;
- estrategia de facilitación;
- respuestas anticipadas;
- soluciones completas;
- resultados de demostraciones antes de realizarlas;
- comentarios editoriales;
- decisiones internas del autor.

Su pregunta rectora es:

> ¿Qué necesita leer y conservar el participante para comprender el curso después de la sesión?

Este material debe poder leerse como un manual breve y continuo. Puede conservar la división M1–M8, pero cada módulo debe funcionar como capítulo de una sola narrativa, no como documento independiente que obliga a consultar otra fuente para completar ideas básicas.

### 3.3 Capa 2: guion textual de diapositivas

Se deriva del material teórico, no directamente de una colección dispersa de módulos y handouts.

Mantiene:

- mismo orden conceptual;
- mismas conclusiones;
- mismos ejemplos esenciales;
- mismas definiciones operativas.

Reduce:

- longitud;
- detalle;
- derivaciones;
- explicaciones secundarias;
- densidad verbal.

Su estilo es telegráfico y de alta síntesis: frases cortas, una idea principal por diapositiva y texto suficiente para orientar sin reemplazar la exposición oral.

Su pregunta rectora es:

> ¿Qué necesita estar escrito en pantalla mientras se explica esta idea?

### 3.4 Capa 3: diapositivas visuales

Se deriva del guion textual. Añade:

- imágenes;
- diagramas;
- composición;
- jerarquía visual;
- tablas simplificadas;
- señales de énfasis;
- revelado progresivo, cuando sea útil.

No debe introducir teoría nueva. Si una idea aparece por primera vez en la diapositiva visual, existe una ruptura en el flujo de derivación.

Su pregunta rectora es:

> ¿Cómo hacer visible la idea sin convertir la diapositiva en una página del manual?

---

## 4. Ubicación de los materiales actuales dentro del flujo

### 4.1 Módulos M1–M8

Los módulos actuales se acercan principalmente a la **versión meta**. Incluyen guion dictable, minutaje, exposición, ejercicios, resultados esperados, errores frecuentes y conexiones con otros materiales.

Ejemplos:

- M2 publica el resultado numérico del ejercicio en `modulos/M2_modelo_medicion.md`;
- M4 entrega valores esperados de `u_c`, `U` y contribución dominante en `modulos/M4_presupuesto_analizador.md`;
- M8 anticipa resultados y conclusiones de la demostración en `modulos/M8_opcional_monte_carlo.md`.

Ese contenido es útil para el instructor, pero no corresponde íntegramente al material entregable. Por tanto, los módulos no deben tratarse como un error editorial ni convertirse directamente en handout. Deben reconocerse como fuente meta y servir para producir una versión teórica limpia.

### 4.2 Handout de GUM (Guía para la Expresión de la Incertidumbre de Medida) y O₃

El handout de O₃ mezcla dos funciones:

1. contiene piezas básicas que deberían formar parte del relato principal del participante;
2. contiene desarrollos avanzados que funcionan correctamente como anexos técnicos.

Pertenecen al material teórico principal, por ejemplo:

- relación entre incertidumbre estándar, combinada y expandida;
- significado de `u`, `u_c`, `U` y `k`;
- vocabulario metrológico mínimo;
- noción de cobertura;
- reglas de presentación y redondeo;
- elementos mínimos de un informe conforme a GUM.

Pueden permanecer como referencia avanzada:

- tratamiento detallado de autocorrelación;
- distribución t desplazada;
- funciones de densidad de probabilidad (PDF) arcoseno y trapezoidal;
- Welch–Satterthwaite detallado;
- Cholesky;
- desarrollos extendidos del método de Monte Carlo (MCM).

Criterio general: pertenece al material principal todo lo necesario para seguir los módulos obligatorios y resolver las actividades requeridas. Pertenece a anexos aquello que amplía, deriva o trata casos especiales sin ser necesario para completar el recorrido principal.

El handout O₃ no debe desaparecer. Debe dejar de completar silenciosamente huecos básicos de los módulos y asumir un papel explícito como conjunto de anexos o referencia técnica.

### 4.3 Handout de NOx

El handout de NOx no es equivalente al handout O₃. Es mucho más breve y, en varios puntos, contiene menos información que M6. Su utilidad real se parece más a:

- ficha operativa;
- referencia rápida;
- checklist de auditoría;
- ayuda de campo;
- recordatorio de fórmulas y controles documentales.

No necesita mantener una simetría artificial con el handout O₃. Puede ser un producto distinto y legítimo, siempre que su función se declare correctamente.

### 4.4 Solucionarios

Los solucionarios son material privado del instructor. Actualmente también reexplican parte de la teoría. Esa repetición puede ser útil para que la solución sea legible de forma autónoma, pero no debe convertirse en otra fuente conceptual paralela.

El meta maestro debe ser canónico para contenido técnico, respuestas breves, propósito pedagógico y resultados esperados. El solucionario debe contener la resolución completa, los cálculos paso a paso, los criterios de corrección y las variantes aceptables, sin crear una tercera versión doctrinal.

### 4.5 Protocolos prácticos

Los protocolos E01–E16 necesitan cierto grado de autonomía porque se usan durante trabajo de laboratorio o campo. Por ello, alguna repetición de fórmulas, criterios y advertencias es aceptable.

La duplicación debe ser deliberada:

- incluir lo necesario para ejecutar el protocolo sin abandonar la actividad;
- remitir al material teórico para fundamentos;
- evitar desarrollar una teoría alternativa o contradictoria;
- conservar la misma notación y terminología del material principal.

---

## 5. Diagnóstico pedagógico que permanece vigente

Reconocer la capa meta corrige la interpretación de los módulos, pero no elimina todos los problemas encontrados.

### 5.1 Falta una entrada terminológica clara

El glosario existe en `handout/gum_o3/O3_H08_glosario.md`, pero está ubicado como sección tardía del handout y no funciona como puerta de entrada al curso.

Además, define algunos términos avanzados y omite varios de alta frecuencia práctica:

- fotómetro de referencia estándar (SRP);
- repetibilidad;
- precisión intermedia;
- reproducibilidad;
- calibración, verificación y ajuste;
- doble conteo;
- escala completa;
- sesgo;
- patrón de transferencia;
- deriva de cero y de span.

La solución no es dictar un glosario extenso antes de M1. Conviene combinar:

1. un mapa inicial corto con términos indispensables para orientarse;
2. definiciones completas justo antes de operar con cada concepto;
3. un glosario final de consulta.

### 5.2 Existen conceptos usados antes de ser enseñados

M2 trabaja con expresiones como `u(T)` y `u(P)` antes de que M3 defina formalmente la incertidumbre estándar.

La cadena:

```text
u_i → u_c → U = k·u_c
```

no tiene todavía un dueño docente completamente claro. `U` y `k` aparecen en ejercicios y resultados, pero su introducción formal está principalmente en el handout.

En la arquitectura final, cada concepto operativo debe tener un módulo dueño. El material del participante debe introducirlo antes de exigir su uso.

### 5.3 El informe GUM se exige antes de enseñarse de manera suficiente

M7 solicita un resultado auditable conforme a GUM §7, mientras que la lista más completa de elementos del informe vive en `handout/gum_o3/O3_H07_informe_gum.md`.

También se evalúan cobertura, redondeo y coherencia entre presupuesto y resultado. Estos criterios deben aparecer dentro del material teórico antes del taller, no únicamente como apoyo consultado durante la revisión final.

### 5.4 “Cobertura” tiene varios sentidos

El curso usa “cobertura” para:

- factor, probabilidad o intervalo de cobertura en sentido GUM;
- alcance cubierto por una evidencia;
- “matriz de cobertura” como artefacto del curso.

Esta colisión puede confundir al participante. Conviene reservar **cobertura** para el sentido metrológico GUM y usar **alcance de la evidencia** para expresar qué condiciones o fuentes cubre un dato.

### 5.5 Existe duplicación no gobernada

Autocorrelación, covarianza, propagación y otros conceptos aparecen con distintos niveles de detalle en módulos, handouts, solucionarios y protocolos.

La repetición no es siempre incorrecta. Se vuelve problemática cuando no se sabe:

- cuál versión es canónica;
- cuál es resumen;
- cuál es ampliación;
- cuál se mantiene manualmente;
- cuál debe actualizarse cuando cambia la teoría.

---

## 6. Arquitectura documental objetivo

### A. Meta maestro privado

Base: módulos M1–M8.

Contenido:

- teoría completa;
- discurso;
- decisiones pedagógicas;
- notas de instructor;
- tiempos;
- preguntas;
- respuestas;
- errores frecuentes;
- variantes;
- referencias;
- criterios de evaluación.

Es fuente superior de intención pedagógica.

### B. Material teórico entregable

Derivado del meta maestro.

Contenido:

- relato limpio y continuo;
- conceptos necesarios;
- ejemplos;
- fórmulas;
- conexiones entre módulos;
- síntesis;
- ejercicios sin revelar anticipadamente soluciones.

Es fuente principal del participante.

### C. Anexos técnicos

Base: contenido avanzado del handout O₃.

Contenido:

- derivaciones;
- casos especiales;
- métodos opcionales;
- referencias normativas extensas;
- material para profundización posterior.

**Destinatario y uso:** participantes que necesiten profundizar e instructor durante preparación o consulta. No son lectura obligatoria para completar recorrido principal.

### D. Fichas operativas y ayudas de campo

Base: partes útiles del handout NOx y material práctico.

Contenido:

- checklists;
- fórmulas rápidas;
- criterios de aceptación;
- controles documentales;
- advertencias de montaje y seguridad.

**Destinatario y uso:** participantes durante práctica, operación o auditoría. Sirven para consulta rápida; no conducen por sí solas una actividad completa.

### E. Protocolos prácticos

Base: protocolos E01–E16.

Contenido:

- propósito y alcance de cada actividad;
- materiales y condiciones previas;
- secuencia completa de ejecución;
- datos que deben registrarse;
- criterios de aceptación y cierre;
- referencias al fundamento teórico correspondiente.

**Destinatario y uso:** participantes e instructor durante laboratorio o campo. A diferencia de una ficha, un protocolo conduce la ejecución completa de una actividad.

### F. Solucionarios privados

Contenido:

- resolución completa;
- cálculos paso a paso;
- criterios de corrección;
- errores típicos;
- variantes aceptables.

**Destinatario y uso:** instructor durante preparación, acompañamiento y evaluación. El meta maestro conserva respuesta breve, propósito pedagógico y resultado esperado; el solucionario conserva desarrollo completo.

### G. Guion textual de diapositivas

Derivado del material teórico.

Contenido:

- títulos;
- frases cortas;
- estructura por diapositiva;
- mensajes centrales;
- indicaciones básicas de apoyo visual.

### H. Diapositivas visuales

Derivadas del guion textual.

Contenido:

- diseño final;
- imágenes;
- diagramas;
- tablas simplificadas;
- composición y jerarquía visual.

---

## 7. Reglas de derivación y control

Para evitar drift entre productos, conviene adoptar reglas explícitas.

### Regla 1. Una idea nueva nace en la capa meta

Ninguna diapositiva, protocolo o solucionario debe introducir silenciosamente un concepto que no esté reconocido en la versión meta.

### Regla 2. Cada capa tiene autoridad definida

El meta maestro es canónico para contenido técnico, definiciones, ecuaciones, notación e intención pedagógica. El material teórico es canónico para orden, redacción y experiencia del participante. Toda corrección técnica debe incorporarse primero al meta maestro y después propagarse a productos derivados.

### Regla 3. Las diapositivas reducen, no amplían

Guion textual y diapositivas visuales pueden condensar, ilustrar y jerarquizar. No deben agregar teoría ausente del material teórico.

### Regla 4. Los anexos amplían sin interrumpir

El relato principal debe ser comprensible sin leer todos los anexos. Los anexos permiten profundidad adicional, no reparación de huecos básicos.

### Regla 5. Fichas y protocolos repiten según su función

Las fichas repiten solo lo necesario para consulta operativa rápida y no sustituyen una secuencia completa. Los protocolos repiten lo necesario para ejecutar una actividad de principio a fin. Ambos deben conservar notación, terminología y criterios del material principal.

### Regla 6. Las respuestas permanecen fuera del entregable principal

El meta maestro conserva respuesta breve, resultado esperado y propósito pedagógico. El solucionario conserva resolución completa, cálculos paso a paso, criterios de corrección y variantes aceptables. Ninguno de estos contenidos debe anticiparse en el material teórico entregable.

### Regla 7. Cada concepto operativo tiene un dueño

Distribución conceptual objetivo propuesta:

- M1: trazabilidad, mensurando y vocabulario base;
- M2: modelo de medición y coeficientes de sensibilidad;
- M3: incertidumbre estándar, Tipo A/B, PDFs y combinación;
- M4: presupuesto, contribuciones, doble conteo, `U`, `k`, cobertura y redondeo;
- M5: patrones, regresión, residuos y alcance de evidencia;
- M6: modelo NOx, interferencias y covarianza;
- M7: integración, declaración del resultado e informe GUM;
- M8: validación opcional mediante MCM.

Otros módulos pueden recordar el concepto, pero no redefinirlo de manera paralela.

---

## 8. Valoración del desfase actual

En esta sección, **desfase** expresa esfuerzo editorial y de consolidación necesario para alcanzar arquitectura objetivo. No califica calidad técnica del contenido existente.

Escala usada:

- **bajo:** producto ya existe y requiere ajustes menores de declaración, consistencia o limpieza;
- **medio:** contenido existe, pero necesita consolidación, reclasificación o derivación significativa;
- **alto:** producto o pipeline todavía no existe como salida gobernada y debe construirse a partir de capas previas.

### 8.1 Contenido técnico

**Desfase bajo.** Gran parte del conocimiento requerido ya existe en módulos, handouts, prácticas y solucionarios.

### 8.2 Versión meta

**Desfase bajo a medio.** Los módulos ya constituyen una base sólida. Requieren declarar su rol, cerrar algunos saltos conceptuales y mejorar consistencia global.

### 8.3 Material teórico del participante

**Desfase medio a alto.** Su contenido existe parcialmente, pero está repartido entre varias fuentes. Falta una narrativa limpia, continua y explícitamente entregable.

### 8.4 Anexos y ayudas operativas

**Desfase medio.** Existe material valioso, pero las funciones de referencia avanzada, resumen y ficha de campo están mezcladas bajo el nombre “handout”.

### 8.5 Guion textual y diapositivas visuales

**Desfase alto como pipeline formal.** Deben construirse después de estabilizar el material teórico. Producirlas antes consolidaría inconsistencias y multiplicaría trabajo de revisión.

### 8.6 Diagnóstico global

No se requiere reconstruir el curso desde cero. Se requiere una reorganización editorial importante y una cadena de derivación explícita.

En términos cualitativos:

- conocimiento: avanzado;
- versión meta: avanzada;
- narrativa entregable: incompleta;
- clasificación de anexos: ambigua;
- pipeline hacia diapositivas: todavía no consolidado.

---

## 9. Solución conceptual

La solución no consiste en escoger entre módulos y handouts como si fueran productos rivales.

Consiste en reconocer que cumplen funciones distintas:

```text
META MAESTRO
    ├── MATERIAL TEÓRICO DEL PARTICIPANTE
    │       └── GUION TEXTUAL DE DIAPOSITIVAS
    │               └── DIAPOSITIVAS VISUALES
    ├── ANEXOS TÉCNICOS
    ├── FICHAS OPERATIVAS
    ├── PROTOCOLOS PRÁCTICOS
    └── SOLUCIONARIOS DEL INSTRUCTOR
```

Dentro de este modelo:

- módulos actuales alimentan principalmente el meta maestro;
- partes básicas del handout O₃ se integran al material teórico;
- partes avanzadas del handout O₃ se convierten en anexos;
- handout NOx se redefine como ayuda operativa o ficha de campo;
- protocolos conservan autonomía controlada;
- solucionarios permanecen privados;
- diapositivas se derivan después de estabilizar narrativa del participante.

---

## 10. Conclusión final

La inquietud inicial era válida: existía una sensación de que módulos y handouts se repetían, se completaban entre sí y no tenían fronteras claras. Sin embargo, causa principal no era exceso de contenido ni una mala concepción del curso. Era ausencia de una arquitectura documental explícita.

La aclaración sobre la versión meta permite interpretar correctamente el estado actual:

1. los módulos no están simplemente sobrecargados; son una base avanzada del documento meta del autor e instructor;
2. el material teórico entregable todavía no existe como producto único, limpio y continuo;
3. el handout O₃ mezcla contenido básico que debe incorporarse al relato principal con material avanzado que debe quedar como anexo;
4. el handout NOx tiene más sentido como ficha operativa que como tratado paralelo;
5. vocabulario inicial, cadena `u → u_c → U`, cobertura, redondeo e informe GUM requieren mejor ubicación dentro de la narrativa;
6. guion textual y diapositivas visuales deben derivarse del material teórico estabilizado, no de fuentes paralelas;
7. principal trabajo pendiente es editorial y arquitectónico, no una reconstrucción técnica.

El curso está avanzado en conocimiento y en preparación docente. Su siguiente etapa natural es convertir esa riqueza meta en una secuencia controlada de productos, cada uno con destinatario, propósito y profundidad definidos.
