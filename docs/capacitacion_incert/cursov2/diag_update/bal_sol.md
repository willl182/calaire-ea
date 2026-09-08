# Balance final de propuestas — `diag_update`

**Fecha:** 2026-08-28  
**Alcance:** archivos Markdown de `docs/capacitacion_incert/cursov2/diag_update/`  
**Método:** cuatro revisiones independientes de primera ronda y tres comparaciones cruzadas de los cinco finalistas, ejecutadas mediante `claude-luna -p`.  
**Exclusiones:** no se revisaron archivos HTML.  
**Estado:** balance comparativo; no modifica las propuestas evaluadas.

---

## 1. Veredicto

La propuesta recomendada como base canónica es **`dd_qw38.md`**.

Dos de los tres jueces de la ronda final la eligieron como ganadora. El tercer juez eligió `dd_g46oc.md`. La diferencia entre las tres primeras propuestas es estrecha; `dd_grk46.md` mostró la mayor regularidad probatoria, pero menor economía editorial.

`dd_qw38.md` ofrece el mejor equilibrio entre:

- diagnóstico;
- decisiones explícitas;
- arquitectura documental;
- problemas pedagógicos;
- gobernanza;
- plan ejecutable.

Su fortaleza central es distinguir el flujo `0 → 1 → 2 → 3` de los productos perpendiculares y definir la relación entre capa 0 y capa 1 como superconjunto y derivación gobernada.

---

## 2. Clasificación general

### Nivel A — candidatas canónicas

#### 1. `dd_qw38.md` — ganadora

**Fortalezas**

- Mejor balance global.
- Buena síntesis sin perder decisiones.
- Distingue claramente capas, anexos, fichas, protocolos y solucionarios.
- Reconoce que la extracción necesita un pase de continuidad editorial.
- Separa el diagnóstico pedagógico de la arquitectura documental.
- Incluye dueños conceptuales, inventario de deuda y plan por dependencias.

**Debilidades**

- Automatiza mediante `build_capas.py` antes de cerrar todo el contenido y el contrato de extracción.
- M0 queda descrito, pero no desarrollado como producto didáctico.
- La cadena `u_i → u_c → U` tiene dueños propuestos, pero no una secuencia docente completa.
- Faltan criterios de aceptación y gobernanza de cambios.

**Decisión:** adoptar como base única.

#### 2. `dd_grk46.md` — mejor fuente complementaria

**Fortalezas**

- Mejor resolución explícita de tensiones entre diagnósticos previos.
- Excelente distinción entre eje de derivación y productos perpendiculares.
- Mejor tratamiento de `cobertura` frente a `alcance de la evidencia`.
- Inventario de deuda más completo.
- Buena separación entre anexos, fichas, protocolos y solucionarios.
- Buen tratamiento del recorte mecánico seguido por continuidad editorial.

**Debilidades**

- Documento largo y repetitivo.
- Menor economía de mantenimiento.
- No fija criterios verificables de cierre.
- Mantiene ambigüedad sobre cómo canonizar en capa 0 el contenido básico que hoy vive en el handout.

**Decisión:** conservar como fuente probatoria y de deuda; no como segundo documento canónico.

#### 3. `dd_g46oc.md` — alternativa canónica

**Fortalezas**

- Un juez la ubicó en primer lugar.
- Buena gobernanza y separación de funciones documentales.
- Regla fuerte: los derivados se generan, no se copian.
- Explica bien las diferencias entre O₃, NOx, protocolos y solucionarios.
- Trata `solo_md/` como evidencia de drift por copia manual.
- Buen balance entre evidencia cuantitativa y propuesta editorial.

**Debilidades**

- Algunas fronteras son menos precisas que en `dd_qw38.md`.
- La tabla de dueños no separa introducción, definición formal, aplicación y profundización.
- No incorpora criterios de aceptación ni validación semántica del pipeline.

**Decisión:** extraer sus reglas anti-drift e incorporarlas a la ganadora.

### Nivel B — buenas, pero no deben gobernar

#### 4. `dd_mmxm3.md`

**Fortalezas**

- Muy completo.
- Mejor descripción extensa de las funciones documentales.
- Identifica que M5, M6 y M8 necesitan redacción, no simple extracción.
- Buena delimitación entre material principal, anexos técnicos, fichas, protocolos y solucionarios.
- Explica con detalle qué conserva y qué elimina la capa 1.

**Debilidades**

- Demasiado largo y repetitivo.
- Costoso de mantener.
- Riesgo de convertirse en otra fuente paralela.
- Menor control sobre decisiones y criterios de cierre.

**Decisión:** rescatar definiciones de productos y listas de contenido; no conservar como propuesta rectora.

#### 5. `dd_glm53f.md`

**Fortalezas**

- Claro y relativamente compacto.
- Buen diagnóstico pedagógico.
- Buen mapa de capas y deuda.
- Explica que los módulos actuales son meta, no material mal escrito.
- Formula bien que separar capas no resuelve por sí solo los problemas pedagógicos.

**Debilidades**

- Menos resolutivo en autoridad, gobernanza y criterios de cierre.
- M0 y M1 conservan solapamientos conceptuales.
- Menor accionabilidad que los cuatro primeros.

**Decisión:** rescatar formulaciones pedagógicas compactas.

### Nivel C — insumos secundarios

#### 6. `dd_muse12.md`

- Integración sólida y legible.
- Buena separación de audiencias.
- Pocas ideas exclusivas frente a los finalistas.
- Variaciones cuantitativas reducen confianza.

#### 7. `dd_ter.md`

- Expediente cuantitativo útil.
- Declara cifras como reverificadas.
- Presenta discrepancias frente a otras propuestas: 749/869 líneas, 26/27 ideas fuerza y 607/1489 líneas.
- Requiere reconciliar método de conteo antes de reutilizar sus cifras.

#### 8. `dd_op5.md`

- Explica bien la función meta y el flujo documental.
- Buena versión para lectura ejecutiva.
- Menor desarrollo de deuda, gobernanza y criterios verificables.

#### 9. `dd_gem.md`

- Buen resumen ejecutivo de 35 líneas.
- Útil como nota breve de decisión.
- Insuficiente como diagnóstico canónico: poca evidencia, pocos riesgos y sin criterios de aceptación.

### Nivel D — descartar como propuestas finales

#### 10. `dd_k3.md`

- Estructura clara.
- Omite problemas pedagógicos, solucionarios, protocolos y varias deudas importantes.
- Puede conservarse únicamente como resumen temprano.

#### 11. `dd_dsv4p.md`

- Detecta el problema principal.
- Menor profundidad, evidencia y accionabilidad.
- Funciona más como borrador inicial que como propuesta consolidada.

---

## 3. Estrategia de consolidación

Usar **`dd_qw38.md` como único documento canónico**. No fusionar documentos completos. Una fusión íntegra recrearía el mismo problema diagnosticado: múltiples formulaciones de una doctrina casi idéntica y mayor superficie de mantenimiento.

### Aportes que deben incorporarse desde `dd_grk46.md`

- Inventario de deuda más completo.
- Distinción formal entre:
  - anexos técnicos;
  - fichas operativas;
  - protocolos;
  - solucionarios.
- Tabla de dueños conceptuales.
- Reserva de `cobertura` para el sentido GUM.
- Tratamiento de continuidad posterior a la extracción.
- Observación sobre ausencia de instrucciones de uso del handout.

### Aportes que deben incorporarse desde `dd_g46oc.md`

- Regla: **los derivados se generan, no se copian**.
- `solo_md/` como evidencia de drift.
- Diferencia entre contenido básico O₃ que debe migrar y contenido avanzado que debe permanecer como anexo.
- Regla formal de autoridad por capa.

### Aportes que deben incorporarse desde `dd_mmxm3.md`

- Descripción precisa de qué conserva y qué elimina la capa 1.
- Explicación de autonomía controlada para protocolos.
- Lista de contenido O₃ básico que debe entrar al relato principal.
- Lista de contenido avanzado que debe quedar como anexo.

### Aportes que deben incorporarse desde `dd_glm53f.md`

- Explicación compacta de que los módulos actuales son una versión meta y no material mal escrito.
- Advertencia de que separar capas no resuelve automáticamente los problemas pedagógicos.
- Formulación breve del problema de continuidad entre módulos.

---

## 4. Correcciones obligatorias antes de adoptar la propuesta ganadora

### 4.1 Revalidar cifras

Las propuestas repiten cifras sin presentar siempre un método plenamente reproducible:

- 42 % de meta pura;
- ~520 líneas duplicadas;
- ~350 líneas de referencia real;
- 26 o 27 ideas fuerza;
- ~120 subbloques;
- 150–200 diapositivas;
- desfase de una capa y media.

Cada cifra debe incorporar:

- comando o método;
- archivos incluidos;
- denominador;
- fecha o commit evaluado;
- clasificación como cifra exacta o estimación.

Cuando no pueda reproducirse, debe escribirse como aproximación pendiente de validación.

### 4.2 Corregir el orden del plan

El generador `build_capas.py` aparece demasiado pronto. M5, M6 y M8 todavía no tienen discurso extraíble; además faltan cierres conceptuales y un contrato formal de marcado.

Orden recomendado:

1. declarar capas y autoridad;
2. pilotar M5 manualmente;
3. redactar y normalizar M6 y M8;
4. resolver vocabulario, GUM, cobertura y dueños conceptuales;
5. definir contrato de marcado y extracción;
6. construir un validador mínimo;
7. construir el generador;
8. generar capa 1;
9. revisar continuidad editorial;
10. crear capas 2 y 3.

La primera herramienta debe validar el contrato, no generar todo el sistema.

### 4.3 Resolver la autoridad entre capas

Regla recomendada:

- **capa 0:** autoridad técnica y pedagógica;
- **capa 1:** producto editorial derivado;
- se permiten cambios de continuidad aprobados;
- cualquier cambio conceptual detectado durante la edición de capa 1 debe incorporarse primero a capa 0;
- ningún handout puede funcionar como fuente normativa paralela;
- protocolos y solucionarios pueden repetir contenido, pero no redefinirlo.

Sin esta regla, el “recorte más pase corto” puede volver a convertirse en reescritura manual y drift.

### 4.4 Limitar M0

M0 no debe convertirse en una versión comprimida de M1, M3 y M4.

Contrato recomendado:

- duración máxima de 15–20 minutos;
- 3–5 conceptos;
- definiciones operativas, no desarrollo formal;
- ningún cálculo completo;
- ningún concepto que no se use inmediatamente;
- tabla `se introduce aquí / se profundiza en módulo X`;
- validación real de duración en aula.

### 4.5 Mejorar el mapa de conceptos

La tabla de dueños debe separar cuatro roles:

| Concepto | Introduce | Define formalmente | Aplica | Profundiza |
|---|---|---|---|---|

Secuencia mínima recomendada:

- **M0:** mapa terminológico;
- **M1:** trazabilidad y cadena de transferencia;
- **M3:** `u_i` y combinación en `u_c`;
- **M4:** `U = k·u_c`, cobertura y redondeo;
- **M7:** declaración del resultado e informe GUM.

### 4.6 Añadir criterios de aceptación

El pipeline debe comprobar, como mínimo:

- concepto definido antes de su primer uso exigente;
- símbolos definidos;
- soluciones ausentes de capa 1;
- ecuaciones conservadas;
- referencias y anclas válidas;
- requisitos GUM presentes antes de M7;
- módulos sin discurso detectados;
- marcadores desconocidos producen fallo cerrado;
- correspondencia módulo–referencia–protocolo;
- dueño conceptual único o solapamiento declarado;
- ausencia de teoría nueva en capas 2 y 3.

### 4.7 No renombrar `handout/` todavía

Secuencia recomendada:

1. declarar funciones;
2. migrar contenido básico;
3. separar anexos y fichas;
4. preservar anclas;
5. validar enlaces;
6. decidir el cambio físico de nombre.

### 4.8 Separar anexos técnicos de referencia operativa

Ambos pueden relacionarse con la capa R, pero no cumplen la misma función:

- **anexo técnico:** profundización y casos especiales;
- **referencia operativa:** consulta rápida, tablas, fórmulas, checklist y criterios de aceptación.

Deben tener reglas de contenido, destinatario y mantenimiento distintas.

---

## 5. Decisión final

- **Base única:** `dd_qw38.md`.
- **Complemento probatorio y de deuda:** `dd_grk46.md`.
- **Reglas anti-drift:** extraer de `dd_g46oc.md`.
- **Detalle de productos:** extraer de `dd_mmxm3.md`.
- **Redacción pedagógica compacta:** extraer de `dd_glm53f.md`.

No deben conservarse cinco diagnósticos activos. Los aportes únicos deben consolidarse en `dd_qw38.md`; después deben verificarse cifras, cerrar criterios de aceptación y archivar las propuestas restantes. Ninguna propuesta debe eliminarse antes de confirmar que todos sus aportes exclusivos fueron migrados.
