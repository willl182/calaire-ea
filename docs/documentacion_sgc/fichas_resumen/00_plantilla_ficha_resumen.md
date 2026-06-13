# Plantilla Base de Ficha Resumen del SGC PEA

**Estado:** activo  
**Fecha:** 2026-06-13  
**Proposito:** plantilla unica para que todos los subagentes elaboren fichas resumen con criterio uniforme, trazabilidad y consistencia documental.

---

## Instrucciones de uso para subagentes

1. Copiar esta plantilla para cada documento asignado.
2. Nombrar el archivo: `ficha_[CODIGO].md` (ejemplo: `ficha_P-PSEA-06.md`).
3. Llenar todos los campos obligatorios marcados con `*`.
4. Respetar las reglas de redaccion y el checklist de calidad al final.
5. No editar `sgc_res.md`, `README.md` ni `P-PSEA-01`.
6. No desarrollar contenido completo de procedimientos o formatos; producir solo ficha resumen.

---

## Estructura de la ficha

### Identificacion

| Campo | Valor |
|---|---|
| **Codigo** * | `[CODIGO]` |
| **Nombre decidido** * | `[Nombre operativo consolidado en el mapa documental]` |
| **Tipo documental** * | Documento general / Procedimiento / Instructivo / Formato / Registro / Matriz / Exportacion / Salida |
| **Estado** * | Mantener / Actualizar / Elaborar / Revisar / Reservar / Retirar / Absorber |
| **Prioridad** * | Alta / Media-alta / Media / Baja / Cierre / No priorizar |
| **Clase de ficha** * | Ficha activa / Ficha preliminar / Ficha diferida / Registro de no activo |

---

### Proposito y rol

#### Proposito operativo *

[Que controla, guia, registra, evidencia o produce dentro del PEA. Maximo 3-5 oraciones.]

#### Rol en el flujo *

- [ ] Entrada
- [ ] Salida
- [ ] Registro oficial
- [ ] Evidencia
- [ ] Criterio tecnico
- [ ] Instructivo
- [ ] Matriz
- [ ] Soporte documental

[Describir el rol en una oracion si no queda claro con las casillas.]

---

### Aplicativos y tecnologia

#### Aplicativo asociado *

- [ ] `calaire-app`
- [ ] `pt_app`
- [ ] Ambos
- [ ] Ninguno

[Justificar si la respuesta no es obvia.]

---

### Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `[Codigo o nombre]` | [Breve descripcion] | [Entrada / Referencia / Insumo] |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `[Codigo o nombre]` | [Breve descripcion] | [Salida / Producto / Evidencia] |

---

### Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `[Codigo]` | [Cita / Alimenta / Genera / Controla / Soporta] | [Obligatorio / Opcional / Referencia] |

---

### Limites y riesgos

#### Limites de alcance

[Que no debe duplicar, que no gobierna o que queda fuera de esta ficha. Ser explicito.]

#### Riesgos de interpretacion

[Confusiones conocidas que deben evitarse. Listar como bullets.]

- [Riesgo 1]: [Explicacion y control.]
- [Riesgo 2]: [Explicacion y control.]

---

### Criterio minimo de elaboracion

[Condicion para considerar lista esta ficha. Debe ser verificable.]

---

## Reglas de redaccion

### Voz y tono
- Usar voz tecnica, impersonal o en tercera persona.
- No usar primera persona ni coloquialismos.
- Ser preciso en las referencias a codigos documentales (`Codigo` en formato de codigo).

### Alcance
- No duplicar contenido que pertenece a otro documento.
- Si un procedimiento por analito debe citar `P-PSEA-06`, usar "Cita `P-PSEA-06` para..." en lugar de replicar la definicion.
- No incluir procedimientos de aprobacion, retencion, obsolescencia ni control documental macro.

### No duplicacion
- `calaire-app` y `pt_app` son documentos generales (`DG-PSEA-02`, `DG-PSEA-03`), no formatos.
- Los archivos tecnicos internos del preprocesador se mapean en `P-PSEA-23`, no se convierten en `F-PSEA`.
- `F-PSEA-10` es un registro, no el aplicativo.
- `F-PSEA-12` es la exportacion desde `calaire-app`; `F-PSEA-14` es el dataset consolidado desde `pt_app`.
- `P-PSEA-06` es procedimiento tecnico; `I-PSEA-17` e `I-PSEA-18` son instructivos de uso.

### Trazabilidad documental
- Toda referencia a un codigo documental debe existir en el inventario maestro.
- Si un documento relacionado no esta aun fichado, anotarlo como "ficha pendiente" en la columna de notas.
- Preferir el flujo de datos oficial sobre capacidades internas alternativas.

---

## Checklist de calidad de ficha

### Antes de entregar la ficha

- [ ] Codigo, nombre, tipo, estado, prioridad y clase estan completos.
- [ ] Aplicativo asociado es correcto (ninguno, `calaire-app`, `pt_app` o ambos).
- [ ] Entradas y salidas indican codigo documental o fuente concreta.
- [ ] No se confunde `F-PSEA-12` con `F-PSEA-14`.
- [ ] No se trata `F-PSEA-10` como aplicativo.
- [ ] No se afirma que H/E no aplica; H/E se documenta en `F-PSEA-13` y subformatos.
- [ ] Si la ficha es preliminar, se indica claramente la restriccion de contenido.
- [ ] Si el documento es retirado/reservado/absorbido, se indica decision, razon y documento sustituto.
- [ ] No se propone aprobacion, retencion, obsolescencia ni control documental macro.
- [ ] No se edita `sgc_res.md`, `README.md` ni `P-PSEA-01`.
- [ ] Procedimientos por analito (`P-PSEA-02` a `P-PSEA-05`) citan transversales y no duplican estadistica, H/E, informe ni flujo de datos.
- [ ] La ficha se guarda con nombre: `ficha_[CODIGO].md` en `docs/documentacion_sgc/fichas_resumen/`.
