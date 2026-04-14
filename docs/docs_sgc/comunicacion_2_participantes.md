# Segunda Comunicación a Participantes — Ensayo de Aptitud CALAIRE-EA

**De:** Wilson Rafael Salas Chávez — Equipo Técnico, Proyecto CALAIRE-EA
**Para:** Laboratorios participantes invitados
**Asunto:** Información detallada y actualización de fechas — Ensayo de Aptitud para Gases Contaminantes Criterio (Prueba Piloto 2026)

---

Estimados participantes,

Reciban un cordial saludo del equipo del Laboratorio CALAIRE y del proyecto de investigación **"Implementación de ensayos de aptitud en la matriz aire — Caso gases contaminantes criterio" (Código 61134)**, de la Universidad Nacional de Colombia, Sede Medellín.

Esta comunicación tiene dos propósitos: (1) informarles sobre una **actualización en las fechas** de la prueba piloto, y (2) brindarles una **explicación detallada de cómo funciona el ensayo**, para que puedan prepararse de la mejor manera. Próximamente les estaremos convocando a una **reunión informativa** donde podremos resolver todas las dudas que surjan.

---

## 1. Actualización de Fechas

### ¿Qué cambió y por qué?

Debido a la situación de **anormalidad académica en la Universidad Nacional de Colombia**, las fechas originales de la prueba piloto han sido reprogramadas. La nueva ventana de ejecución será durante la **tercera y cuarta semana de abril de 2026**.

Las nuevas fechas tentativas son:

| Ronda | Montaje (miércoles) | Días de prueba (jue-sáb) | Recolección (lunes) |
|-------|---------------------|--------------------------|---------------------|
| **Ronda A** | Miércoles 15 de abril | Jueves 16 a Sábado 18 de abril | Lunes 20 de abril |
| **Ronda B** | Miércoles 22 de abril | Jueves 23 a Sábado 25 de abril | Lunes 27 de abril |

> **Nota:** La asignación de cada laboratorio a una ronda específica se confirmará una vez recibamos sus formularios de confirmación (ver sección 9). Si hay necesidad de rondas adicionales, se podrían habilitar fechas en la última semana de abril o primera de mayo.

---

## 2. ¿Qué es un Ensayo de Aptitud y para qué sirve?

Un Ensayo de Aptitud (EA) es un ejercicio de **comparación interlaboratorio** organizado conforme a la norma **ISO/IEC 17043:2023**. En términos sencillos: varios laboratorios miden **la misma muestra de gas** bajo condiciones controladas, y luego se comparan los resultados para evaluar qué tan bien está midiendo cada uno.

**¿Por qué participar?**

- Permite identificar si sus equipos y procedimientos están generando resultados confiables.
- Sirve como evidencia de competencia técnica ante organismos de acreditación (IDEAM, ONAC).
- Ayuda a detectar problemas de calibración, deriva instrumental o errores sistemáticos que de otro modo podrían pasar desapercibidos.
- Es un requisito cada vez más relevante para laboratorios que realizan vigilancia de calidad del aire en Colombia.

En esta prueba piloto, estamos validando la metodología del ensayo antes de ofrecerlo como servicio regular. Por eso **la participación es completamente gratuita** — los participantes solo asumen el transporte de sus equipos y consumibles propios.

---

## 3. ¿Qué se mide?

Se evaluarán los **cuatro gases contaminantes criterio** más relevantes para la vigilancia de la calidad del aire:

| Gas | Símbolo | Unidades |
|-----|---------|----------|
| Ozono | O₃ | nmol/mol |
| Monóxido de Nitrógeno | NO | nmol/mol |
| Dióxido de Nitrógeno | NO₂ | nmol/mol |
| Dióxido de Azufre | SO₂ | nmol/mol |
| Monóxido de Carbono | CO | µmol/mol |

Para cada gas se generarán **cinco niveles de concentración más un nivel cero**, dentro de rangos relevantes para la vigilancia ambiental (0–500 nmol/mol para SO₂, NO, NO₂ y O₃; 0–10 µmol/mol para CO). Los niveles exactos están documentados en el **Cronograma Detallado (F-PSEA-02)** que se adjunta.

---

## 4. ¿Cómo se genera la muestra que van a medir? (El Ítem de Ensayo)

Esta es la parte central del ejercicio y lo que lo diferencia de una calibración rutinaria. Queremos explicarlo con claridad para que entiendan exactamente qué van a medir y cómo se garantiza que la comparación sea justa.

### El concepto

El **ítem de ensayo** (la "muestra" que miden los analizadores) es una **atmósfera de gas contaminante en aire cero**, generada dinámicamente por el Laboratorio CALAIRE. No es un cilindro que se reparte: es un flujo continuo de gas a una concentración conocida que se distribuye **simultáneamente** a todos los analizadores conectados.

### ¿Cómo se genera cada gas?

La generación depende del tipo de contaminante:

**Para SO₂, CO, NO y NO₂:**

1. Se parte de un **cilindro de Material de Referencia Certificado (MRC)** — un gas patrón con concentración conocida y trazabilidad metrológica internacional.
2. Un **calibrador dinámico** mezcla ese gas patrón con **aire cero** (aire limpio, libre de contaminantes) en proporciones precisas.
3. Al variar la proporción de dilución, se generan los diferentes **niveles de concentración** del ensayo (desde cero hasta el nivel más alto).

**Para Ozono (O₃):**

1. Se utiliza un **generador de ozono** que produce O₃ a partir de aire u oxígeno mediante descarga UV.
2. La concentración generada se mide y controla con un **fotómetro de referencia nivel 2**, que es el instrumento de referencia en la cadena de trazabilidad internacional de ozono.
3. Al ajustar la potencia del generador, se obtienen los distintos niveles de concentración.

### ¿Cómo se asegura que todos midan lo mismo?

Una vez generada la atmósfera de gas a la concentración deseada, esta se alimenta a un **manifold de distribución de vidrio**. El vidrio es un material inerte — no reacciona ni absorbe los gases — lo que garantiza que la muestra no se contamine ni se altere.

Del manifold salen **líneas individuales de teflón** (también inerte) hacia cada puesto de medición. Todos los analizadores reciben la misma muestra, al mismo tiempo, a la misma concentración. El sistema opera con un ligero exceso de flujo para evitar contrapresión en las líneas.

```
                    ┌─────────────────────────────────┐
                    │  Generación del gas              │
                    │  (MRC + Calibrador dinámico)     │
                    │  o (Generador O₃ + Fotómetro)    │
                    └───────────┬─────────────────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │  Manifold de vidrio    │
                    │  (distribución         │
                    │   homogénea)           │
                    └──┬────┬────┬────┬─────┘
                       │    │    │    │
                       ▼    ▼    ▼    ▼
                     Líneas de teflón 1/4"
                       │    │    │    │
                       ▼    ▼    ▼    ▼
                    ┌────┐┌────┐┌────┐┌────┐
                    │Lab ││Lab ││Lab ││Lab │
                    │ A  ││ B  ││ C  ││Ref │
                    └────┘└────┘└────┘└────┘
                    Analizadores participantes + referencia CALAIRE
```

> **En resumen:** CALAIRE genera una concentración conocida y trazable → la distribuye por igual a todos los analizadores → cada laboratorio mide con su propio equipo y procedimiento → se comparan los resultados. Si un analizador lee algo distinto, la diferencia está en el equipo o procedimiento del participante, no en la muestra.

### Homogeneidad y estabilidad

Antes de iniciar las mediciones con participantes, CALAIRE verifica que:

- **Homogeneidad:** Todas las salidas del manifold entregan la misma concentración (la variación entre líneas debe ser menor a 0,3 veces la desviación estándar de aptitud, σpt).
- **Estabilidad:** La concentración se mantiene constante durante todo el tiempo de medición de cada nivel.

Estas pruebas se realizan conforme a la norma **ISO 13528:2022** y quedan documentadas.

---

## 5. ¿Cómo se desarrolla una ronda? (Día a día)

Cada ronda sigue un ciclo semanal en el **Laboratorio CALAIRE** (Bloque 19A, 4º piso/azotea, Campus El Volador, Universidad Nacional de Colombia, Sede Medellín, Cra 65 No 59A-110):

### Día 1 — Miércoles: Recepción, Instalación y Calibración

- **Hora de llegada: 08:00 a.m.** (es importante ser puntuales para no retrasar el cronograma de la ronda).
- Cada laboratorio instala su equipo en el **salón contiguo** al laboratorio principal, en el puesto asignado y etiquetado con su código.
- El participante realiza sus conexiones eléctricas y de gases según su propio procedimiento interno (POE).
- Se hacen las **verificaciones pre-ensayo**: estabilidad del equipo, verificación de fugas, tiempos de respuesta, registro correcto de datos.
- El participante ejecuta su **calibración multipunto** (cero, span y puntos intermedios) de acuerdo con su procedimiento interno vigente.
- Al final del día, los equipos quedan **encendidos y estabilizados** (condición continua) para garantizar repetibilidad al día siguiente.

> **¿Por qué la calibración el primer día?** Porque queremos que cada laboratorio opere exactamente como lo haría en su rutina normal. El EA evalúa el desempeño completo: equipo + calibración + procedimiento.

### Días 2 y 3 — Jueves a Sábado: Medición

- Cada participante traslada su analizador al **laboratorio principal** y lo instala en el rack designado, bajo supervisión del equipo técnico de CALAIRE.
- Los analizadores se conectan al **manifold de distribución** a través del puerto de teflón 1/4" asignado.
- Comienza la secuencia de medición, **gas por gas**, siguiendo el cronograma F-PSEA-02:
  1. El operador de CALAIRE genera el **primer nivel de concentración** del primer gas (típicamente O₃).
  2. Los analizadores censan esa concentración durante el tiempo establecido (1–2 horas por nivel).
  3. Se pasa al siguiente nivel de concentración, y así sucesivamente hasta completar los 5 niveles + cero.
  4. Al terminar un gas, los participantes **descargan los datos** de su instrumento y los entregan al equipo organizador.
  5. Se prepara la conexión para el **siguiente gas** (O₃ → NO → NO₂ → SO₂/CO) y se repite el ciclo.
- Los analizadores **permanecen encendidos entre días** para mantener estabilidad.
- Cada laboratorio registra **datos minutales** continuos y consolida el **promedio horario** por cada nivel.

> **Secuencia típica de gases:** O₃ (Día 2) → NO y NO₂ (Día 2–3) → SO₂ y CO (Día 3). Los tiempos exactos dependen de la ronda y están en el Cronograma Detallado F-PSEA-02.

### Día 5 — Lunes: Recolección

- Cada participante desmonta y embala sus equipos de forma segura.
- Se limpia el área para la siguiente ronda.

### Medidas anti-colusión

Para garantizar la imparcialidad del ensayo:
- Se asigna un **código único** a cada laboratorio; durante las mediciones no se comparten identidades.
- Se restringe la **visibilidad de pantallas/displays** entre participantes.
- Cada participante firma un **acuerdo de confidencialidad y no confabulación** antes de iniciar.

---

## 6. ¿Qué equipos deben traer?

Cada laboratorio participante debe contar con su **sistema de medición completo**:

| Elemento | Detalle |
|----------|---------|
| **Analizador de gases** | Específico para el/los mensurando(s) de interés |
| **Calibrador dinámico** | Con calibración vigente (incluido fotómetro si aplica) |
| **Sistema de aire cero** | Generador o cilindro de aire cero |
| **Generador de ozono** | Con fotómetro nivel 2 para trazabilidad (si mide O₃) |
| **Cilindro de gas patrón** | Con certificado vigente, regulador doble tapa y conectores |
| **Sistema de adquisición de datos** | Datalogger o computador con software de exportación |
| **Conexiones y accesorios** | Mangueras, conectores, adaptadores para su sistema |
| **EPP** | Guantes resistentes a químicos, calzado de seguridad, gafas protectoras, bata de laboratorio |

> **Importante:** El Laboratorio CALAIRE **no suministra** consumibles, repuestos ni EPP. Cada participante es responsable de traer todo lo necesario para operar su sistema.

**Lo que CALAIRE proporciona:**
- Espacio de trabajo etiquetado con clima controlado
- Suministro eléctrico regulado (110V AC, regleta con mínimo 4 tomas por puesto)
- Puerto de conexión de 1/4" en teflón al manifold de distribución
- Sistema completo de generación y distribución de mezclas gaseosas (MRC, calibrador, manifold)

**Transporte de equipos:**
- Los instrumentos deben llegar al Laboratorio (Bloque 19A, Campus El Volador, Cra 65 No 59A-110) **tres (3) días antes** del inicio de la ronda.
- Instrucciones detalladas de empaque y envío en el documento adjunto **I-PSEA-01 — Instructivo de Embalaje y Transporte**.
- La responsabilidad sobre la integridad de los equipos durante el transporte, instalación y operación es de cada participante. CALAIRE no abrirá las cajas ni manipulará los instrumentos.

---

## 7. ¿Cómo se reportan los resultados?

Al finalizar cada bloque de medición por contaminante, cada laboratorio debe entregar:

1. **Promedios horarios** para cada nivel de concentración, reportados con **tres (3) cifras decimales**.
2. **Datos crudos minutales** exportados directamente desde los analizadores (el formato específico se indicará antes de la ronda).
3. **Incertidumbre de medición expandida** (con factor de cobertura k=2) para cada nivel de concentración evaluado.

> El reporte de la incertidumbre es **obligatorio**. Sin este dato no es posible calcular uno de los indicadores de desempeño (el En-score), lo que afectaría la evaluación. Los resultados finales consolidados deben enviarse al organizador **dentro de los 15 días posteriores** a la finalización de las mediciones.

---

## 8. ¿Cómo se evalúa el desempeño?

Los resultados de cada laboratorio se comparan contra **valores de referencia** determinados por CALAIRE. Estos valores son trazables a estándares internacionales: Materiales de Referencia Certificados (para SO₂, CO, NO, NO₂) y fotómetro de ozono nivel 2 (para O₃). No dependen del consenso de los participantes, lo que hace la evaluación robusta incluso con pocos laboratorios.

La norma **ISO 13528:2022** establece cuatro indicadores estadísticos de desempeño. La selección de cuál(es) se aplicarán en cada ronda se definirá conforme a los resultados obtenidos y las condiciones metrológicas del ensayo (particularmente, la magnitud de la incertidumbre del valor asignado respecto a la desviación estándar de aptitud). A continuación se explican los cuatro:

### 1. Puntuación z (z-score)

Es el indicador más directo. Mide qué tan lejos está el resultado del participante respecto al valor de referencia, expresado en unidades de la desviación estándar de aptitud (σpt).

**Se utiliza cuando** la incertidumbre del valor asignado es despreciable — es decir, cuando u(xpt) ≤ 0,3·σpt. En ese caso, la referencia es tan precisa que la única fuente relevante de variación es el desempeño del participante.

| Resultado | Interpretación |
|-----------|---------------|
| \|z\| ≤ 2.0 | **Satisfactorio** — El resultado está dentro del rango esperado |
| 2.0 < \|z\| < 3.0 | **Señal de advertencia** — Conviene revisar el proceso |
| \|z\| ≥ 3.0 | **No satisfactorio** — Se requiere acción correctiva |

### 2. Puntuación z' (z'-score)

Es una variante del z-score que **incorpora la incertidumbre del valor asignado** en el denominador. Se utiliza cuando esa incertidumbre **no es despreciable** — es decir, cuando u(xpt) > 0,3·σpt. Esto amplía ligeramente los límites de aceptación, reconociendo que parte de la diferencia observada puede deberse a la incertidumbre de la propia referencia y no solo al desempeño del participante.

Los criterios de calificación son los mismos que para el z-score (\|z'\| ≤ 2.0 satisfactorio, etc.).

### 3. Puntuación ζ (zeta-score)

A diferencia de z y z', el zeta-score **no usa σpt**. En su lugar, evalúa la diferencia entre el resultado del participante y el valor de referencia considerando **las incertidumbres declaradas por ambos**: la del participante u(xi) y la del valor asignado u(xpt).

Es un indicador más exigente porque pone a prueba no solo si el resultado es cercano al valor de referencia, sino también si la **incertidumbre que el participante declara es realista**. Un laboratorio que reporta una incertidumbre muy pequeña pero se desvía del valor de referencia obtendrá un zeta-score alto.

| Resultado | Interpretación |
|-----------|---------------|
| \|ζ\| ≤ 2.0 | **Satisfactorio** — Resultado e incertidumbre coherentes con la referencia |
| 2.0 < \|ζ\| < 3.0 | **Señal de advertencia** |
| \|ζ\| ≥ 3.0 | **No satisfactorio** — Revisar resultado y/o estimación de incertidumbre |

### 4. Puntuación En (En-score)

Similar al zeta-score en concepto, pero utiliza las **incertidumbres expandidas** (U = k·u, con k=2) en lugar de las estándar. Evalúa si el resultado del participante y el valor de referencia son compatibles dentro de sus respectivos intervalos de incertidumbre expandida.

| Resultado | Interpretación |
|-----------|---------------|
| \|En\| ≤ 1.0 | **Satisfactorio** |
| \|En\| > 1.0 | **No satisfactorio** |

### ¿Cuál se usará en la prueba piloto?

La selección dependerá de las condiciones de cada ronda — en particular, de la relación entre la incertidumbre del valor asignado u(xpt) y la desviación estándar de aptitud σpt. Los resultados de la prueba piloto nos permitirán determinar cuál(es) indicador(es) son los más adecuados para el esquema CALAIRE-EA en su operación regular. En el informe de resultados se reportarán los indicadores aplicables con su interpretación.

> **Nota sobre σpt:** El valor de σpt no se comunica previamente a los participantes. Se determina de forma **post-ronda** a partir de los requisitos normativos aplicables (US EPA) para cada analito, y se publica junto con los resultados en el informe final de desempeño.

> **¿Qué pasa si un resultado no es satisfactorio?** No hay penalización. El propósito del ensayo es **identificar oportunidades de mejora**. Un resultado "no satisfactorio" es una señal para revisar calibraciones, procedimientos o condiciones de operación. Al finalizar, cada participante recibirá un **Informe de Desempeño** confidencial con el análisis detallado de sus resultados.

---

## 9. Confirmación de Participación

Para formalizar su participación y facilitar la planificación logística, les solicitamos diligenciar el **Formulario de Confirmación de Participación (F-PSEA-05)** que se adjunta a esta comunicación.

En el formulario les pedimos:
- Datos de contacto del laboratorio y persona responsable
- Equipos que traerán (modelo, serial, vigencia de certificados de calibración)
- Preferencia de ronda (Ronda A: abril 15–20 o Ronda B: abril 22–27)
- Número de personas que asistirán al montaje y operación

Les agradeceríamos enviar el formulario diligenciado a más tardar el **[FECHA LÍMITE]**, para poder asignar las rondas y coordinar la logística de espacios y permisos de acceso al campus.

---

## 10. Confidencialidad

- A cada laboratorio se le asignará un **código único y anónimo**. Los resultados individuales no se compartirán con otros participantes ni con terceros, salvo lo dispuesto por la normativa (IDEAM, organismos acreditadores).
- Antes de iniciar, se firmará un **Acuerdo de Confidencialidad y No Confabulación**.

---

## 11. Reunión Informativa

Estamos programando una **reunión informativa virtual** para explicar el protocolo en detalle, presentar el cronograma actualizado y resolver todas sus dudas antes de la ronda.

La fecha tentativa es el **viernes 20 de marzo de 2026**. Les solicitamos indicarnos su disponibilidad:

- **Opción A:** Viernes 20 de marzo — **en la mañana** (horario por definir)
- **Opción B:** Viernes 20 de marzo — **en la tarde** (horario por definir)

Por favor incluyan su preferencia de horario en la respuesta a este correo o en el Formulario de Confirmación (F-PSEA-05).

---

## 12. Próximos Pasos

1. **Revisar** esta comunicación y los documentos adjuntos.
2. **Diligenciar y enviar** el Formulario de Confirmación (F-PSEA-05) antes de la fecha límite.
3. **Indicarnos su disponibilidad** para la reunión del viernes 20 de marzo (mañana o tarde).
4. **Asistir a la reunión informativa** donde explicaremos el protocolo y resolveremos preguntas.
5. **Preparar sus equipos** según los requisitos técnicos descritos en las secciones 6 y 7.

---

## Documentos Adjuntos

| Código | Documento | Descripción |
|--------|-----------|-------------|
| **F-PSEA-01** | Calendario del Ensayo de Aptitud | Calendario general con las fechas clave actualizadas de cada ronda |
| **F-PSEA-02** | Cronograma Detallado | Niveles de concentración por gas, tiempos de corrida y actividades hora a hora |
| **I-PSEA-01** | Instructivo de Embalaje y Transporte | Guía para el empaque y envío seguro de instrumentos y cilindros al laboratorio |
| **F-PSEA-05** | Formulario de Confirmación de Participación | Formulario para confirmar datos del laboratorio, equipos y preferencia de ronda |

---

Para cualquier consulta, no duden en contactarnos:

**Wilson Rafael Salas Chávez**
Equipo Técnico — Proyecto CALAIRE-EA
Laboratorio CALAIRE, Facultad de Minas
Universidad Nacional de Colombia, Sede Medellín
[CORREO ELECTRÓNICO]
[TELÉFONO DE CONTACTO]

**Carmen Elena Zapata Sánchez**
Directora del Proyecto — Coordinadora Laboratorio CALAIRE
Facultad de Minas
Universidad Nacional de Colombia, Sede Medellín
