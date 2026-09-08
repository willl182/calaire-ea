Diagnóstico

Tu intuición correcta. Problema no es falta general de contenido. Problema: roles pedagógicos mezclados.

Hoy existen cuatro capas explicando teoría:

1. módulos;
2. handouts;
3. solucionarios;
4. protocolos prácticos.

Pero falta capa más básica: vocabulario mínimo de entrada.

1. ¿Aclarar primero términos metrológicos?

Sí, pero no enseñar todo handout antes de M1.

Separaría:

Vocabulario previo mínimo

Antes de M1 o durante apertura:

- mensurando;
- resultado de medición;
- trazabilidad metrológica;
- error, incertidumbre y falla;
- corrección;
- incertidumbre estándar u;
- incertidumbre combinada u_c;
- incertidumbre expandida U;
- factor de cobertura k;
- calibración, verificación y ajuste;
- repetibilidad, precisión intermedia y reproducibilidad;
- patrón de transferencia;
- SRP;
- deriva de cero y span;
- escala completa frente a lectura.

Actualmente glosario está enterrado en handout/gum_o3/O3_H08_glosario.mtenido técnico. Ningún módulo enlaza ese glosario.

Además glosario define términos poco usados como GUF, pero omite términconteo, escala completa, precisión intermedia y verificación frente aajuste.

Conceptos justo cuando se necesitan

No todo debe ir al principio. PDFs, coeficientes de sensibilidad, covarianza, regresión y MCM deben aparecer dentro de módulo dueño.

Regla útil:

▎ Si participante necesita operar con concepto durante ejercicio, módulo debe enseñarlo antes del ejercicio.

Hoy regla se incumple. Ejemplo:

- M2 trabaja con u(T) y u(P) en modulos/M2_modelo_medicion.md:164.
- Definición de incertidumbre estándar aparece después, en modulos/M3_c

Otro salto:

- U = k·u_c está en handout, handout/gum_o3/O3_H01_conceptos_basicos.md
- M4 y M7 ya usan U, en modulos/M4_presupuesto_analizador.md:174 y modulos/M7_taller.md:26.
- Ningún módulo introduce claramente cadena u_i → u_c → U.

Eso sí necesita corregirse conceptualmente.

2. ¿Módulos carecen de contenido de handouts?

En general, no.

Mucho contenido omitido está bien omitido:

- distribución t desplazada;
- autocorrelación detallada;
- Welch–Satterthwaite;
- PDFs arcoseno y trapezoidal;
- Cholesky;
- desarrollos avanzados de MCM.

Eso pertenece a material de consulta, no necesariamente a curso presencial de seis horas.

Dos omisiones sí parecen pedagógicamente importantes:

Expansión U = k·u_c

Se usa y evalúa, pero no tiene módulo dueño.

Informe conforme a GUM §7

M7 pide resultado auditable conforme a GUM:

modulos/M7_taller.md:28

Pero estructura completa del informe vive solo en:

handout/gum_o3/O3_H07_informe_gum.md:5                                                                                                                  
M7 remite al handout durante revisión final, cuando participante ya redactó entrega. También se evalúan redondeo, cobertura y coherencia del informe en diseno_curso_v2.md:135, sin enseñanza previa suficientemente explícita.

Eso sí es contenido esencial faltante en secuencia docente.

3. ¿Módulos ya son su propio handout?

Sí, pero son más exactamente guiones docentes autocontenidos.

Contienen:

- objetivos;
- prerrequisitos;
- exposición dictable;
- minutaje;
- tablas;
- fórmulas;
- ejercicios;
- resultados esperados;
- errores frecuentes;
- respuestas.

Ejemplos:

- M2 publica resultado numérico del ejercicio en modulos/M2_modelo_medicion.md:184.
- M4 publica u_c, U y contribución dominante en modulos/M4_presupuesto_
- M8 anticipa resultados completos de demo en modulos/M8_opcional_monte_carlo.md:62.

Por eso módulos sirven como handout técnico, pero no como material limpio para participante. Revelan soluciones, conclusiones y decisiones del instructor.

Problema central:

▎ Mismo archivo intenta ser guion de instructor y material de participante.

Esos roles chocan.

4. Handouts no tienen rol uniforme

Handout O₃

Sí tiene valor independiente. Funciona como manual de referencia avanzada. Módulos lo citan muchas veces y deja fuera correctamente desarrollos extensos.

No debería competir con módulos. Debería declararse como:

▎ Referencia para consulta durante y después del curso; no lectura lineal obligatoria.

Handout NOx

Caso distinto. Está mucho más resumido que M6. M6 contiene más información sobre:

- interferentes;
- quenching;
- ramas del diagrama causa–efecto;
- presupuesto EN 14211;
- defectos de datasets;
- advertencias metrológicas.

Handout NOx casi repite M6, pero con menos detalle. Su aporte real estáde auditoría y algunas fórmulas de campo.

Por tanto, hoy no funciona como equivalente NOx del handout O₃.

Mejor concepto para ese material:

▎ ficha de campo / guía rápida de auditoría NOx

No “handout teórico NOx” simétrico al O₃.

5. Problema terminológico importante: “cobertura”

Curso usa “cobertura” con varios sentidos:

1. factor, intervalo o probabilidad de cobertura GUM;
2. alcance cubierto por evidencia;
3. “matriz de cobertura” del curso.

Ejemplos:

- alcance de evidencia: modulos/M3_conceptos_gum.md:167
- cobertura aproximada del 95 %: modulos/M7_taller.md:157

Participante puede interpretar ambos como mismo concepto.

Conviene reservar cobertura para sentido GUM y usar alcance de evidencia para segundo sentido.

6. Arquitectura pedagógica más coherente

Sin cambiar contenido todavía, modelo correcto sería:

A. Vocabulario mínimo de apertura

Documento corto. Una o dos frases por término. Solo conceptos necesarios para comprender M1–M2.

B. Módulos como guiones de enseñanza

Cada concepto operativo tiene módulo dueño. Módulo introduce concepto antes de usarlo.

Ejemplo:

- M1: trazabilidad y vocabulario base;
- M2: modelo de medición y sensibilidad;
- M3: Tipo A/B, PDFs y combinación;
- M4: presupuesto, doble conteo, U = k·u_c, cobertura y redondeo;
- M5: patrones, regresión y alcance de evidencia;
- M6: modelo NOx y covarianza;
- M7: integración e informe GUM;
- M8: MCM opcional.

C. Handout O₃ como referencia

Derivaciones, casos especiales y material avanzado. No necesita duplica

D. Material NOx como guía de campo

Checklist, residencia, interferencias, control documental y modelo difeetría artificial con handout O₃.

E. Protocolos autocontenidos solo cuando campo lo exige

Duplicación permitida cuando participante necesita ejecutar protocolo sro debe ser decisión explícita, no duplicación accidental.

Conclusión

Sí: enfoque actual está algo invertido.

- Falta vocabulario mínimo inicial.
- Módulos ya contienen enseñanza principal.
- Handout O₃ sirve como referencia avanzada.
- Handout NOx carece de función clara y queda por debajo de M6.
- Módulos no deberían entregarse sin tratamiento como handout de particestas y guion docente.
- No hace falta trasladar todo handout a módulos. Solo incorporar conceptos operativos actualmente usados sin introducción: u, u_c, U, k, redondeo e informe GUM.
- Decisión más importante: declarar quién recibe cada documento, cuándo

No cambié archivos.
