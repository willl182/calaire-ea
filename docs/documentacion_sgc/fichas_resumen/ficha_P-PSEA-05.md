# Ficha Resumen: P-PSEA-05

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `P-PSEA-05` |
| **Nombre decidido** | Comunicaciones del PEA |
| **Tipo documental** | Procedimiento |
| **Estado** | Mantener / Actualizar |
| **Prioridad** | Media-alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Gobierna los canales, formatos, responsables y registros de comunicaciones oficiales del PEA. Define cuando se usa `calaire-app` (notificaciones automaticas, casos SGC) y cuando se usa correo electronico formal institucional. Conecta con participantes, quejas, apelaciones, informes y control de valores sensibles.

### Rol en el flujo

- [x] Criterio tecnico
- [x] Procedimiento
- [ ] Entrada
- [ ] Salida
- [ ] Registro oficial
- [ ] Evidencia
- [ ] Instructivo
- [ ] Matriz
- [ ] Soporte documental

---

## Aplicativos y tecnologia

#### Aplicativo asociado

- [x] `calaire-app`
- [ ] `pt_app`
- [ ] Ambos
- [ ] Ninguno

Las comunicaciones principales usan `calaire-app`; algunas usan correo segun aplique.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `I-PSEA-02` | Instructivo para participante | Referencia |
| `P-PSEA-16` | Divulgacion y control de valores sensibles | Referencia |
| `P-PSEA-17` | Quejas del PEA | Referencia |
| `P-PSEA-18` | Apelaciones del PEA | Referencia |
| `P-PSEA-09` | Generacion del informe | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-13` | Informe final comunicado | Referencia |
| `F-PSEA-14` | Casos de queja/NC comunicados | Referencia |
| `F-PSEA-15` | Registro de apelaciones comunicadas | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `I-PSEA-02` | Instructivo de comunicaciones a participantes | Obligatorio |
| `P-PSEA-16` | Control de valores sensibles en comunicaciones | Obligatorio |
| `P-PSEA-17` | Quejas gestionadas como comunicaciones | Obligatorio |
| `P-PSEA-18` | Apelaciones gestionadas como comunicaciones | Obligatorio |
| `P-PSEA-09` | Informe como comunicacion oficial | Obligatorio |
| `DG-PSEA-02` | Aplicativo de comunicaciones | Obligatorio |

---

## Limites y riesgos

#### Limites de alcance

- No es un instructivo de uso de `calaire-app` (eso es `I-PSEA-02`).
- No es un procedimiento de quejas (eso es `P-PSEA-17`); conecta con el.
- No es un procedimiento de apelaciones (eso es `P-PSEA-18`); conecta con el.
- No es un procedimiento de control de valores sensibles (eso es `P-PSEA-16`); conecta con el.

#### Riesgos de interpretacion

- **Omitir canal de correo:** Algunas comunicaciones (apelaciones, comunicaciones formales) van por correo, no solo por `calaire-app`.
- **Confundir con I-PSEA-02:** `I-PSEA-02` explica como usar el aplicativo; `P-PSEA-05` gobierna que, cuando y por que canal comunicar.
- **Omitir registro:** Las comunicaciones oficiales deben quedar registradas.
- **Incluir comunicaciones internas informales:** Este procedimiento gobierna comunicaciones oficiales del PEA.

---

## Criterio minimo de elaboracion

El procedimiento define canales (`calaire-app` vs correo), responsables, registros y conexiones con `P-PSEA-16`, `P-PSEA-17`, `P-PSEA-18` y `P-PSEA-09`, sin duplicar instructivos ni procedimientos de quejas/apelaciones.
