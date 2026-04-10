# Plan Final de Revision del SGC frente a ISO/IEC 17043:2023 e ISO 13528:2022

**Fecha**: 2026-03-27  
**Estado**: final  
**Alcance**: `docs/docs_sgc/` contrastado contra `docs/referencias/iso 17043_2023.md`, `docs/referencias/iso 13528_2022.md`, `docs/ppsea09/ppsea09/P-PSEA-09.md`, `docs/ppsea09/ppsea06/p-psea-06.md`, y los insumos `gpt_sgc.md`, `gem_sgc.md`, `claude_sgc.md`, `z_sgc.md`.

---

## 1. Objetivo

Definir un plan de revision y cierre de brechas del Sistema de Gestion de Calidad del proveedor de ensayos de aptitud CALAIRE-EA, identificando:

- documentacion ya resuelta o avanzada;
- documentacion pendiente para cumplir de forma consistente ISO/IEC 17043:2023;
- instructivos y formatos minimos requeridos;
- priorizacion por oleadas para ejecucion documental.

---

## 2. Criterio de evaluacion adoptado

La revision parte de cuatro conclusiones base:

1. `P-PSEA-09` ya cubre de forma solida la **planificacion de la ronda**, incluyendo buena parte de 7.2.1 y elementos operativos de 7.3.
2. `P-PSEA-06` ya cubre el **nucleo estadistico**, incluyendo diseño estadistico, valor asignado, homogeneidad, estabilidad y puntajes de desempeño, aunque requiere mejora editorial.
3. La mayor brecha actual no esta en la metodologia tecnica del esquema, sino en la **arquitectura del SGC**, especialmente en clausulas 4, 6, 7.1, 7.4.3, 7.5 y 8 de ISO/IEC 17043:2023.
4. ISO 13528:2022 queda materialmente cubierta en su parte central si se conserva `P-PSEA-06` como procedimiento troncal y se complementa con validacion formal del software y reglas de reporte a participantes.

---

## 3. Estado actual resumido

### 3.1 Documentacion con avance utilizable

- `P-PSEA-09 Procedimiento de Planificacion Ronda EA`
  Cubre personal, participantes, riesgos, metodos, cronograma, criterios de participacion, control de proveedores externos, instrucciones previas, homogeneidad y estabilidad a nivel de planificacion.
- `P-PSEA-06 Procedimiento Diseno Estadistico`
  Cubre objetivo estadistico, tipo de datos, numero de participantes, Algoritmo A, MADe, nIQR, valor asignado, sigma_pt, incertidumbre, homogeneidad, estabilidad y scores.
- `P-PSEA-01 Protocolo General EA`
  Sirve como documento marco, pero requiere realineacion con 17043:2023.
- `P-PSEA-04 Procedimiento O3`
  Existe como procedimiento especifico operativo.
- `F-PSEA-05 Formulario Confirmacion Participacion`
  Ya aporta evidencia operativa puntual.
- Plantillas e informes de resultados existentes
  Aportan base para estructurar `P-PSEA-07` y el formato de informe.

### 3.2 Debilidades estructurales actuales

- Inventario, matriz y backlog tienen **inconsistencias de codificacion** respecto a `P-PSEA-06` y `P-PSEA-07`.
- Falta separar claramente:
  - procedimiento;
  - instructivo tecnico;
  - formato / registro;
  - documento general.
- No existe todavia un paquete documental completo para:
  - imparcialidad;
  - confidencialidad;
  - competencia/autorizacion;
  - proveedores externos;
  - control documental y de registros;
  - no conformidades;
  - auditorias internas;
  - revision por la direccion;
  - quejas y apelaciones;
  - validacion del software/app estadistica.

---

## 4. Cobertura normativa: que ya esta cubierto y que no

### 4.1 ISO/IEC 17043:2023 con cobertura avanzada

**Cubierto o parcialmente cubierto con base fuerte:**

- `7.2.1` Diseno y planificacion de rondas: principalmente en `P-PSEA-09`.
- `7.2.2` Diseno estadistico: principalmente en `P-PSEA-06`.
- `7.2.3` Valor asignado y su incertidumbre: principalmente en `P-PSEA-06`.
- `7.3.1` y `7.3.2` Produccion, seleccion, homogeneidad y estabilidad del item: cubierto entre `P-PSEA-09` y `P-PSEA-06`, aunque requiere instructivo operativo de soporte.
- `7.4.1` y `7.4.2` Registro, analisis y evaluacion del desempeño: base metodologica presente en `P-PSEA-06`.

### 4.2 ISO/IEC 17043:2023 con brecha importante

**Pendiente o insuficientemente formalizado:**

- `4.1` Imparcialidad
- `4.2` Confidencialidad
- `5.5` a `5.7` Estructura, autoridad y comunicacion del sistema
- `6.2` Gestion de competencia y autorizacion formal
- `6.3` Condiciones ambientales, separacion de areas y control de acceso
- `6.4` Control de productos y servicios externos
- `7.1.1` Revision de solicitudes, ofertas y contratos
- `7.3.3` y `7.3.4` Identificacion, almacenamiento, despacho, rotulado, transporte y confirmacion de entrega de items
- `7.3.5` Instrucciones a participantes y comunicacion previa
- `7.4.3` Requisitos del informe
- `7.5.1` Registros tecnicos
- `7.5.2` Gestion de datos y validacion de sistemas
- `8.3` a `8.11` Sistema de gestion completo

### 4.3 ISO 13528:2022

**Cobertura fuerte ya existente:**

- cap. 4 principios generales;
- cap. 5 diseno estadistico;
- cap. 6 revision inicial, homogeneidad y estabilidad;
- cap. 7 valor asignado;
- cap. 8 y 9 evaluacion del desempeño y scores.

**Pendiente de formalizacion documental:**

- validacion del software utilizado en el analisis;
- descripcion formal y disponible para participantes de los calculos e interpretacion;
- mejora editorial y trazabilidad de registros del procedimiento estadistico.

---

## 5. Documentacion pendiente recomendada

Se propone racionalizar el sistema y no multiplicar documentos sin necesidad. La meta debe ser un sistema compacto, auditable y coherente con la evidencia disponible.

### 5.1 Documentos generales

#### 1. `DG-PSEA-01 Manual del SGC para EA`

Debe consolidar:

- alcance del proveedor;
- estructura organizacional;
- politica de imparcialidad;
- politica de confidencialidad;
- relacion entre CALAIRE 17025 y el proveedor EA;
- mapa documental del sistema;
- referencia cruzada a todos los procedimientos.

**Prioridad**: critica

### 5.2 Procedimientos obligatorios o muy recomendables

#### 2. `P-PSEA-07 Procedimiento de Elaboracion y Emision de Informes de Resultados`

Para cubrir 7.4.3:

- contenido minimo;
- plazos de emision;
- informes corregidos;
- declaraciones de participacion;
- politica de uso del informe.

#### 3. `P-PSEA-13 Procedimiento de Control Documental`

Para cubrir 8.3.

#### 4. `P-PSEA-14 Procedimiento de Control de Registros`

Para cubrir 7.5.1 y 8.4.

#### 5. `P-PSEA-17 Procedimiento de No Conformidades y Acciones Correctivas`

Para cubrir 8.7.

#### 6. `P-PSEA-18 Procedimiento de Auditorias Internas`

Para cubrir 8.8.

#### 7. `P-PSEA-19 Procedimiento de Revision por la Direccion`

Para cubrir 8.9.

#### 8. `P-PSEA-20 Procedimiento de Imparcialidad`

Para cubrir 4.1.

#### 9. `P-PSEA-27 Procedimiento de Confidencialidad`

Para cubrir 4.2.

#### 10. `P-PSEA-30 Procedimiento de Proveedores Externos`

Para cubrir 6.4.

#### 11. `P-PSEA-28 Procedimiento de Competencia y Autorizacion del Personal`

Para cubrir 6.2.

#### 12. `P-PSEA-25 Procedimiento de Quejas`

Para cubrir 8.10.

#### 13. `P-PSEA-26 Procedimiento de Apelaciones`

Para cubrir 8.11.

#### 14. `P-PSEA-21 Procedimiento de Revision de Solicitudes, Ofertas y Contratos`

Para cubrir 7.1.1.

#### 15. `P-PSEA-22 Procedimiento de Comunicacion con Participantes`

Para cubrir 7.3.5 y articular convocatorias, instrucciones y trazabilidad de comunicaciones.

### 5.3 Instructivos tecnicos requeridos

#### 16. `I-PSEA-10 Instructivo de Preparacion, Embalaje, Rotulado, Transporte y Recepcion de Items`

Debe operativizar:

- 7.3.3;
- 7.3.4;
- seguridad;
- confirmacion de entrega;
- control de condicion de recepcion.

#### 17. `I-PSEA-11 Instructivo de Homogeneidad y Estabilidad`

Aunque la base estadistica ya esta en `P-PSEA-06`, este instructivo debe dejar claro el flujo operativo:

- muestreo;
- numero de unidades;
- replicas;
- tiempos de medicion;
- aceptacion del lote;
- registros.

#### 18. `I-PSEA-12 Instructivo de Instrucciones a Participantes`

Debe contener:

- preparacion del equipo;
- condiciones de medicion;
- formato de reporte;
- manejo de unidades;
- plazos;
- declaracion de incertidumbre cuando aplique.

#### 19. `I-PSEA-14 Instructivo de Validacion de Software y Sistemas`

Critico para 7.5.2 y 13528:

- alcance de validacion de CALAIRE-APP;
- pruebas funcionales;
- pruebas con datasets de referencia;
- control de versiones;
- trazabilidad de cambios;
- criterios de aceptacion.

#### 20. `I-PSEA-15 Instructivo de Gestion y Revision de Datos`

Para reforzar 7.4.1:

- depuracion;
- deteccion de errores groseros;
- manejo de NA;
- agrupacion por metodo si aplica;
- criterios de exclusion justificada.

---

## 6. Formatos minimos requeridos

A continuacion se listan los formatos que deberian existir para que el sistema sea auditable y operativo.

### 6.1 Formatos de gobierno y gestion

#### `F-PSEA-01 Matriz de Competencia y Autorizacion`

Evidencia:

- cargo;
- actividad autorizada;
- formacion;
- experiencia;
- fecha de autorizacion;
- vigencia;
- aprobador.

#### `F-PSEA-02 Matriz de Riesgos de Imparcialidad`

Evidencia:

- riesgo;
- origen;
- control;
- responsable;
- seguimiento;
- decision.

#### `F-PSEA-03 Evaluacion de Proveedores Externos`

Evidencia:

- proveedor;
- servicio;
- competencia;
- trazabilidad;
- aprobacion;
- seguimiento.

#### `F-PSEA-04 Control de Documentos y Cambios`

Evidencia:

- codigo;
- version;
- cambio;
- aprobacion;
- fecha;
- distribucion.

#### `F-PSEA-05 Control de Registros`

Evidencia:

- nombre del registro;
- ubicacion;
- responsable;
- tiempo de retencion;
- respaldo.

### 6.2 Formatos de planificacion y operacion de la ronda

#### `F-PSEA-06 Plan de Ronda EA`

Debe consolidar los literales operativos de `P-PSEA-09`:

- personal;
- participantes;
- cronograma;
- concentraciones objetivo;
- criterios estadisticos;
- riesgos;
- proveedores;
- evidencia requerida.

#### `F-PSEA-07 Lista Maestra de Participantes`

Evidencia:

- codigo de participante;
- laboratorio;
- metodo;
- contacto;
- estado de confirmacion;
- fecha de comunicacion.

#### `F-PSEA-08 Confirmacion de Participacion`

Puede integrarse o reemplazar el actual `F-PSEA-05 Formulario Confirmacion Participacion`, segun decidan mantener o renumerar.

#### `F-PSEA-09 Registro de Preparacion del Item`

Evidencia:

- lote;
- patron;
- fecha;
- equipos;
- condiciones;
- responsable.

#### `F-PSEA-10 Registro de Homogeneidad`

Evidencia:

- unidades ensayadas;
- replicas;
- resultados;
- calculos;
- conclusion.

#### `F-PSEA-11 Registro de Estabilidad`

Evidencia:

- tiempos;
- resultados;
- delta;
- criterio 0.3 sigma_pt;
- conclusion.

#### `F-PSEA-12 Registro de Envio y Recepcion`

Evidencia:

- fecha de despacho;
- transportador;
- condiciones;
- fecha de recepcion;
- conformidad del participante.

#### `F-PSEA-13 Formato de Reporte de Resultados del Participante`

Evidencia:

- codigo;
- analito;
- resultado;
- unidad;
- incertidumbre;
- metodo;
- observaciones.

### 6.3 Formatos de evaluacion y cierre

#### `F-PSEA-14 Hoja de Revision de Datos`

Evidencia:

- validacion de unidades;
- consistencia;
- exclusiones;
- observaciones tecnicas.

#### `F-PSEA-15 Hoja de Calculo y Aprobacion Estadistica`

Evidencia:

- metodo usado;
- x_pt;
- sigma_pt;
- u(x_pt);
- score aplicado;
- revisor;
- aprobador.

#### `F-PSEA-16 Plantilla de Informe de Resultados`

Debe alinearse con `P-PSEA-07`.

#### `F-PSEA-17 Registro de No Conformidad / CAPA`

#### `F-PSEA-18 Registro de Quejas`

#### `F-PSEA-19 Registro de Apelaciones`

#### `F-PSEA-20 Acta de Revision por la Direccion`

#### `F-PSEA-21 Lista de Verificacion de Auditoria Interna ISO/IEC 17043:2023`

#### `F-PSEA-22 Protocolo de Validacion de Software`

Critico para demostrar cumplimiento de 7.5.2.2 y 4.1.4 de ISO 13528.

---

## 7. Racionalizacion propuesta de la arquitectura documental

Para evitar duplicidades, se recomienda la siguiente logica:

### 7.1 Mantener como documentos troncales

- `P-PSEA-09` como procedimiento de planificacion y preparacion de rondas.
- `P-PSEA-06` como procedimiento estadistico troncal.
- `P-PSEA-01` como protocolo general del esquema, orientado al participante y al alcance del programa.

### 7.2 No duplicar contenido tecnico en exceso

- No conviene crear otro procedimiento estadistico separado si `P-PSEA-06` ya cumple ese rol.
- No conviene duplicar en `DG-PSEA-01` el contenido operativo detallado de `P-PSEA-09`.
- Los procedimientos por analito (`P-PSEA-02` a `P-PSEA-05`) deben conservar solo particularidades tecnicas por gas.

### 7.3 Ajustes de codificacion necesarios

Debe corregirse el desfase entre inventario y realidad documental:

- el inventario antiguo asigna a `P-PSEA-06` un rol que ya no corresponde;
- `P-PSEA-07` debe quedar reservado al informe de resultados;
- `P-PSEA-13` y `P-PSEA-14` deben distinguir claramente documento vs registro;
- la matriz maestra y backlog deben sincronizarse con la codificacion final adoptada.

---

## 8. Priorizacion por oleadas

### Oleada 1: cierre de brecha critica para acreditacion / transicion

Documentos a desarrollar primero:

- `DG-PSEA-01`
- `P-PSEA-07`
- `P-PSEA-13`
- `P-PSEA-14`
- `P-PSEA-17`
- `P-PSEA-18`
- `P-PSEA-19`
- `P-PSEA-20`
- `P-PSEA-27`
- `P-PSEA-28`
- `P-PSEA-30`
- `I-PSEA-14`

Formatos minimos de Oleada 1:

- `F-PSEA-01 Matriz de Competencia y Autorizacion`
- `F-PSEA-02 Matriz de Riesgos de Imparcialidad`
- `F-PSEA-03 Evaluacion de Proveedores Externos`
- `F-PSEA-04 Control de Documentos y Cambios`
- `F-PSEA-05 Control de Registros`
- `F-PSEA-15 Hoja de Calculo y Aprobacion Estadistica`
- `F-PSEA-16 Plantilla de Informe`
- `F-PSEA-17 Registro de NC/CAPA`
- `F-PSEA-20 Acta de Revision por la Direccion`
- `F-PSEA-21 Lista de Verificacion de Auditoria`
- `F-PSEA-22 Protocolo de Validacion de Software`

### Oleada 2: robustecimiento operativo de la ronda

Documentos:

- `P-PSEA-21`
- `P-PSEA-22`
- `P-PSEA-25`
- `P-PSEA-26`
- `I-PSEA-10`
- `I-PSEA-11`
- `I-PSEA-12`
- `I-PSEA-15`

Formatos:

- `F-PSEA-06 Plan de Ronda`
- `F-PSEA-07 Lista Maestra de Participantes`
- `F-PSEA-08 Confirmacion de Participacion`
- `F-PSEA-09 Registro de Preparacion del Item`
- `F-PSEA-10 Registro de Homogeneidad`
- `F-PSEA-11 Registro de Estabilidad`
- `F-PSEA-12 Registro de Envio y Recepcion`
- `F-PSEA-13 Reporte del Participante`
- `F-PSEA-14 Revision de Datos`

### Oleada 3: consolidacion y depuracion del sistema

- ajustar editorialmente `P-PSEA-06`;
- armonizar inventario, backlog y matriz maestra;
- retirar duplicados;
- unificar nomenclatura;
- consolidar plantillas de comunicacion y de informes historicos.

---

## 9. Entregables concretos que quedan pendientes

### Pendiente critico

- Manual del SGC para EA.
- Procedimiento de informes.
- Procedimiento de imparcialidad.
- Procedimiento de confidencialidad.
- Procedimiento de competencia/autorizacion.
- Procedimiento de proveedores externos.
- Procedimiento de control documental.
- Procedimiento de control de registros.
- Procedimiento de no conformidades.
- Procedimiento de auditorias internas.
- Procedimiento de revision por la direccion.
- Instructivo de validacion de software.

### Pendiente alto

- Procedimiento de revision de solicitudes/contratos.
- Procedimiento de comunicacion con participantes.
- Procedimiento de quejas.
- Procedimiento de apelaciones.
- Instructivo operativo de items PT.
- Instructivo de instrucciones a participantes.
- Instructivo de revision y gestion de datos.

### Pendiente medio

- depuracion editorial de `P-PSEA-06`;
- consolidacion de formatos historicos;
- alineacion de inventario, backlog y matriz maestra.

---

## 10. Recomendacion final

El proyecto no necesita reconstruir todo el SGC desde cero. Ya existe un nucleo tecnico suficientemente util en `P-PSEA-09` y `P-PSEA-06`. La estrategia correcta es:

1. **conservar el nucleo tecnico existente**;
2. **cerrar primero las brechas de sistema de gestion y evidencia** exigidas por ISO/IEC 17043:2023;
3. **formalizar los formatos de registro y la validacion del software**;
4. **sincronizar codificacion e inventario** para que la documentacion sea auditable.

En terminos practicos, la documentacion pendiente no es tanto "mas metodologia estadistica", sino sobre todo:

- gobernanza del proveedor;
- trazabilidad documental;
- competencia y autorizacion;
- control de proveedores;
- informes;
- registros;
- tratamiento de desvíos, quejas y apelaciones;
- validacion del sistema informatico.

Ese es el camino mas corto y defensable para cerrar la revision del SGC frente a ISO/IEC 17043:2023 e ISO 13528:2022.
