Revisado. Diagnóstico y respuestas. Nada cambiado.

Lo que hay

┌─────────────────┬───────────────────────────────────────────────────┬───────────────────┬─────────────────────────────────────────────────────────────────┐
│      Capa       │                      Volumen                      │   Rol declarado   │                            Rol real                             │
├─────────────────┼───────────────────────────────────────────────────┼───────────────────┼─────────────────────────────────────────────────────────────────┤
│ modulos/M1–M8   │ 1489 líneas, guion dictable completo              │ "guiones de aula" │ material autosuficiente: explica, define, ejemplifica, ejercita │
├─────────────────┼───────────────────────────────────────────────────┼───────────────────┼─────────────────────────────────────────────────────────────────┤
│ handout/gum_o3/ │ 869 líneas, 10 secciones                          │ "Materiales" #1   │ apéndice citado 30 veces con "Apoyo en el handout"              │
├─────────────────┼───────────────────────────────────────────────────┼───────────────────┼─────────────────────────────────────────────────────────────────┤
│ handout/no_nox/ │ 120 líneas, 10 archivos (H03 = 7 líneas, H08 = 3) │ igual que arriba  │ esqueleto; M6 lo cita 1 vez                                     │
└─────────────────┴───────────────────────────────────────────────────┴────────────────────────────────────────────────────────┘

Tus tres intuiciones

1. ¿Aclarar términos primero? — Sí, hay inversión real.

Vocabulario formal vive en O3_H01 (mensurando, modelo, error vs incertidumbre, estándar/combinada/expandida, trazabilidad) y O3_H08 (glosario, 23 entradas). Pero secuencia de aula introduce operativamente:
                                                                                                                                                                           - M1 usa incertidumbre del patrón / del analizador / del valor transfere residual, falla, doble conteo, covarianza — y remite a H01 §1.3/§1.4"para el vocabulario" (modulos/M1_trazabilidad.md:111).                                                                                                                  - M2 usa mensurando, coeficiente de sensibilidad.
- M3 recién define Tipo A/B, PDF, combinación cuadrática (M3:24).                                                                                                          
O sea: M1 pide prestado vocabulario que llega formalmente 82 min después. M1 se autodeclara "establece el vocabulario" (M1:6) pero no lo define — lo delega al handout que nadie dijo cuándo se lee.
                                                                                                                                                                           2. ¿Módulos no tienen lo del handout? — Al revés en O₃, cierto en NOx.
                                                                                                                                                                           O₃: módulo y handout se solapan casi 1:1 (M3 §3.3 PDFs ≈ H03; M2 §3.3 sme ≈ H07). Solapamiento sin jerarquía declarada: no dice quién escanónico, qué se lee antes, qué se consulta después.                                                                                                                       
NOx: al revés. M6 (204 líneas) carga todo; handout NOx es stub. Las dos familias no juegan el mismo rol, pero README las presenta como equivalentes.                       
3. ¿Módulos son su propio handout? — Sí, de facto.                                                                                                                         
"Guion dictable" en prosa completa + referencias exactas + ejercicio + errores frecuentes = el módulo ya es documento de lectura. El handout no agrega capa; agrega        redundancia con anclas.
                                                                                                                                                                           El vacío que explica todo
                                                                                                                                                                           Cero instrucción de uso del handout en todo el paquete. grep de "preleces del curso": 0 resultados. README lo lista bajo Materiales;diseno_curso_v2.md igual. Nadie dice si se entrega antes, durante o después, ni si el participante debe leerlo.                                                            
Sin esa decisión, "¿términos primero?" no tiene respuesta: depende de si el handout es prelectura (entonces sí, y M1 puede asumirlo) o consulta en aula (entonces falta un M0 de vocabulario).

Tres arquitecturas posibles

A — Handout = prelectura obligatoria. Se envía días antes con H00–H01 +ra mínima. M1 arranca asumiendo términos. Costo: depende de que lean;riesgo alto en operadores.

B — M0 de vocabulario, 15–20 min. Bloque nuevo antes de M1: mensurando, error/corrección/incertidumbre, estándar/combinada/expandida, trazabilidad, Tipo A/B en versión
mínima. M3 pasa a profundizar, no a introducir. Costo: −20 min de la reintuición 1 directo.

C — Fusionar. Handout O₃ deja de ser paralelo: se vuelve anexo de referulas), y su prosa expositiva se absorbe en módulos. Resuelve intuición3. Costo: reescritura grande + rehacer 30 anclas + build_paquete_html.py.

No excluyentes: B + C es la combinación coherente con "los módulos son su propio handout".

Preguntas para decidir

1. ¿El participante recibe algo antes del curso? Si no, A queda descartada y B es casi obligatoria.
2. ¿El handout es para el aula o para después (referencia en el puesto , el solapamiento con módulos no es defecto, es intencional — pero hayque declararlo en README.                                                                                                                                       ¿El handout NOx se completa a nivel de O₃, o se acepta que M6 sea lasolo checklist/auditoría? Hoy es lo segundo de facto.
4. ¿Los módulos se entregan al participante, o solo los usa el instructor? Si solo instructor, entonces el handout sí es el único material del participante — y el diagnóstico cambia por completo: el problema no es redundancia, es qente.
