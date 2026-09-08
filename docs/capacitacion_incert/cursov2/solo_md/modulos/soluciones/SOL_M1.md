# SOL_M1 — Cadena de trazabilidad del resultado de ozono

## 1. Enunciado resumido

Dibujar, de arriba hacia abajo, cadena documentada que respalda un resultado de ozono: SRP de Nivel 1, patrón de transferencia de Nivel 2, patrón de Nivel 3 cuando exista y analizador. Cada enlace debe mostrar evidencia, vigencia, intervalo e incertidumbre. Cada instrumento debe mostrar control de estabilidad. Deben marcarse `C` para correcciones aplicadas y `F` para fallas o controles operativos que no pertenecen al presupuesto. Datos desconocidos se marcan **«por confirmar»**, nunca se inventan.

## 2. Solución paso a paso

Actividad no tiene solución numérica única. Solución correcta es diagrama completo, coherente y auditable. Modelo mínimo:

```text
SRP de Nivel 1
  Identificación: ____________________
  Referencia/realización: fotometría UV
  Intervalo: _________________________
  Incertidumbre del valor: ___________
  Estabilidad controlada por: ________
  Verificación entre calibraciones: __
                 │
                 │ Comparación documentada N1–N2
                 │ Evidencia: ___________________
                 │ Fecha/vigencia: ______________
                 │ Intervalo: ___________________
                 │ Incertidumbre de transferencia: ______
                 ▼
Patrón de transferencia de Nivel 2
  Identificación: ____________________
  Función o resultado de calibración: __________
  Incertidumbre del patrón: ____________________
  Estabilidad controlada por: __________________
  Verificación entre calibraciones: ____________
                 │
                 │ Comparación documentada N2–N3
                 │ Evidencia: ___________________
                 │ Fecha/vigencia: ______________
                 │ Intervalo: ___________________
                 │ Incertidumbre de transferencia: ______
                 ▼
Patrón de transferencia de Nivel 3 [si existe]
  Identificación: ____________________
  Función o resultado de calibración: __________
  Incertidumbre del patrón: ____________________
  Estabilidad controlada por: __________________
  Verificación entre calibraciones: ____________
                 │
                 │ Calibración/transferencia al analizador
                 │ Evidencia: ___________________
                 │ Fecha/vigencia: ______________
                 │ Intervalo: ___________________
                 │ Incertidumbre del valor transferido: __
                 ▼
Analizador
  Identificación: ____________________
  Resultado y unidad: _______________
  Intervalo y condiciones: __________
  Incertidumbre propia: _____________
  Estabilidad controlada por: _______
  Verificación entre calibraciones: __
```

Si organización no usa Nivel 3, enlace válido es:

```text
SRP Nivel 1 — comparación documentada — Nivel 2 — calibración documentada — analizador
```

No debe agregarse Nivel 3 ficticio.

### 2.1 Ubicar niveles

1. Parte superior: **SRP de Nivel 1**, referencia UV de orden superior.
2. Segundo nivel: **patrón de transferencia de Nivel 2**, calibrado frente al Nivel 1.
3. Tercer nivel, solo si existe: **patrón de transferencia de Nivel 3**, calibrado frente al Nivel 2.
4. Parte inferior: **analizador** que produce resultado de rutina.

Orden correcto conserva jerarquía. Patrón de nivel inferior no puede aparecer como referencia de nivel superior sin evidencia adicional.

### 2.2 Documentar cada flecha

Cada flecha representa comparación o calibración. Debe incluir:

- certificado, informe, procedimiento o registro que prueba comparación;
- fecha y vigencia;
- magnitud y unidad transferidas;
- intervalo cubierto;
- resultado, función de calibración o corrección aplicable;
- incertidumbre declarada de comparación o valor transferido;
- condiciones pertinentes: matriz gaseosa, temperatura, presión, promedio y configuración.

Flecha sin evidencia o sin incertidumbre identifica vacío. Acción correcta: escribir **«por confirmar»** y registrar seguimiento.

### 2.3 Separar tres clases de incertidumbre

Usar colores o símbolos distintos:

- **P — incertidumbre del patrón:** acompaña valor entregado por patrón. Incluye incertidumbre recibida desde nivel superior y componentes propias ya integradas por certificado o evaluación aplicable.
- **A — incertidumbre propia del analizador:** repetibilidad, resolución, función de calibración, deriva, influencias ambientales y otros efectos de indicación.
- **T — incertidumbre de transferencia:** comparación concreta entre patrón y analizador o entre patrones; puede incluir estabilidad durante comparación, pérdidas, aire cero, repetibilidad de puntos, regresión y condiciones operativas.

Ubicación correcta:

```text
[Patrón: P] ── [comparación: T] ── [Analizador: A]
```

Incertidumbre de patrón no reemplaza incertidumbre del analizador. Incertidumbre recibida tampoco desaparece al bajar de nivel.

### 2.4 Marcar correcciones y fallas

- **`C` — corrección aplicada:** indique valor corregido, ecuación o procedimiento y evidencia. Incertidumbre de corrección permanece en enlace correspondiente.
- **`F` — falla o control operativo:** fuga accidental, transcripción errónea, equipo averiado u otra condición de operación inválida. Se investiga y previene; no se incorpora como componente para normalizar falla.

Ejemplo:

```text
Nivel 2 ── C: función vigente y evidencia del certificado ── Analizador
           F: prueba de fugas; si falla, detener e investigar
```

Respuestas esperadas a preguntas de revisión:

1. valor corregido debe identificarse en cada enlace; si no existe corrección, indicarlo;
2. cobertura de estabilidad o repetibilidad se obtiene del certificado, no se supone;
3. cualquier fuga catastrófica, transcripción errónea o avería propuesta como componente debe reclasificarse `F`.

### 2.5 Mostrar control de estabilidad

Junto a cada patrón y analizador debe aparecer:

1. responsable o función que controla estabilidad;
2. verificación realizada entre calibraciones;
3. frecuencia o criterio de aceptación;
4. registro donde queda evidencia;
5. acción ante resultado fuera de control.

Si alguno falta, marcarlo **«por confirmar»**.

### 2.6 Comprobar compatibilidad metrológica

Revisión final de cada enlace:

- misma magnitud o conversión documentada;
- unidades compatibles;
- misma matriz gaseosa o efecto de matriz evaluado;
- intervalo del instrumento inferior cubierto por calibración superior;
- condiciones de referencia y promedio compatibles;
- valor atribuido al mismo punto físico del sistema;
- calibración vigente y estabilidad demostrada.

Certificados aislados no bastan si existe salto entre ellos.

## 3. Resultado final

> **Resultado esperado:** diagrama continuo desde SRP de Nivel 1 hasta analizador, con Nivel 2 y Nivel 3 cuando corresponda; identificación de instrumentos; evidencia, fecha, intervalo e incertidumbre sobre cada flecha; controles de estabilidad junto a cada instrumento; separación visible entre incertidumbre del patrón, del analizador y de transferencia; correcciones `C`; fallas o controles `F`; vacíos marcados «por confirmar».

## 4. Criterios de valoración

### Logro completo

- Ordena correctamente Nivel 1, Nivel 2, Nivel 3 si existe y analizador.
- Representa cada comparación mediante flecha documentada.
- Incluye evidencia, fecha o vigencia, intervalo e incertidumbre en cada enlace.
- Identifica responsable y verificación de estabilidad de cada instrumento.
- Distingue incertidumbres P, A y T sin duplicarlas ni intercambiarlas.
- Comprueba magnitud, unidad, intervalo y condiciones.
- Marca correcciones `C`, fallas o controles `F` y datos faltantes como «por confirmar».

### Logro parcial

- Cadena y niveles correctos, pero falta uno o más datos documentales.
- Reconoce incertidumbres, pero ubica alguna de forma ambigua.
- Incluye controles de estabilidad sin responsable, frecuencia o evidencia.
- Detecta vacíos, pero no los marca como acciones de seguimiento.

### No logrado

- Presenta certificado como prueba suficiente sin construir cadena.
- Omite nivel existente o inventa nivel no documentado.
- Deja flechas sin evidencia e incertidumbre y no marca vacíos.
- Asigna incertidumbre del patrón como incertidumbre total del analizador.
- Usa magnitudes, unidades o intervalos incompatibles sin corrección documentada.

## 5. Errores esperables del participante

- Dibujar analizador conectado directamente al Nivel 1 por creer que cadena ininterrumpida exige comparación directa.
- Confundir generador con referencia que asigna valor; generador produce mezcla, sistema fotométrico asigna valor.
- Escribir solo nombres de equipos, sin documentos, vigencias, intervalos ni incertidumbres.
- Copiar incertidumbre certificada del patrón junto al analizador como si fueran iguales.
- Sumar nuevamente componentes ya integradas en incertidumbre certificada del patrón.
- Omitir estabilidad entre calibraciones.
- Usar «trazable» como propiedad permanente del instrumento y no del resultado bajo condiciones definidas.
- Inferir datos faltantes. Corrección: escribir «por confirmar».
- Aceptar misma palabra «ozono» como prueba de compatibilidad, sin revisar magnitud, unidad, matriz, promedio y condiciones de referencia.
