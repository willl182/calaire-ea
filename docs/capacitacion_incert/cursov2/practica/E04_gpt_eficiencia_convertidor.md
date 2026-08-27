# E04 — GPT y eficiencia del convertidor con escalera rediseñada

Enlaza con **M6**. Corrige el defecto D4 del brief (titulación demasiado profunda del diseño anterior). Alimenta la eficiencia `η` usada en **E05**, **E15** (transferencia a NOx) y **E16**.

## Objetivo

Generar NO₂ por titulación en fase gaseosa, estimar la eficiencia `η` del convertidor en cinco niveles, evaluar linealidad y repetibilidad entre dos días, y eliminar el defecto de titulación profunda del diseño anterior.

## Fundamento del rediseño (defecto D4)

El diseño anterior usaba NO inicial cercano a 160 nmol/mol y nivel N150 cercano a 150 nmol/mol, dejando aproximadamente 10 nmol/mol de NO residual: solo 6.25 % del NO inicial, margen demasiado pequeño (errores de O₃, mezcla, impureza y caudal dominan el resultado).

Nueva condición: NO antes de GPT `N₀=450 nmol/mol`; NO₂ GPT nominal `0, 40, 80, 120, 160 nmol/mol`; NO residual esperado `450, 410, 370, 330, 290 nmol/mol`. En el nivel máximo, `N_res/N₀=(450-160)/450=64.4 %` y `N_res/NO2,GPT=290/160=1.81`: exceso holgado de NO, y 160 nmol/mol cubre 80 % del rango didáctico 0–200 nmol/mol.

Para cilindro de 50 µmol/mol y flujo total de 5.000 L/min: `q_NO=45.0 mL/min`, `q_dil=4955.0 mL/min` antes de ajustes GPT. Si la concentración certificada difiere, recalcular el caudal; no copiar 45.0 mL/min.

## Instrumentos

Instrumentos comunes; calibrador GPT con cámara de mezcla; analizador de O₃ o fotómetro de transferencia para asignar O₃ cuando la arquitectura lo permita; patrón de flujo; cilindro NO certificado.

## Procedimiento

### Día 1, aproximadamente 100 min

1. **Montaje y seguridad, 15 min.** Comprobaciones comunes, venteo, fugas y caudal total.
2. **Verificación de caudales, 10 min.** Medir caudal de NO y dilución en los puntos de trabajo.
3. **Cero, 10 min.** Aire cero: 5 min de acondicionamiento y 5 min de registro.
4. **NO base, 15 min.** Generar 450 nmol/mol de NO sin O₃; acondicionar 10 min o hasta <1 nmol/mol en 5 min; registrar cinco promedios de 1 min.
5. **Escalera ascendente, 40 min.** Aplicar niveles GPT 40, 80, 120 y 160 nmol/mol. En cada nivel: 5 min de acondicionamiento mínimo y 5 promedios de 1 min. Exigir NO residual >250 nmol/mol.
6. **Retorno, 10 min.** Repetir nivel 80 nmol/mol y luego cero para detectar memoria o deriva.
7. **Cierre, 5 min.** Desactivar O₃, mantener NO/aire cero hasta eliminar O₃, cerrar NO y purgar.

### Día 2, aproximadamente 100 min

Repetir preparación, cero y NO base; aplicar orden descendente 160, 120, 80, 40 nmol/mol; repetir nivel 80 y cero final; analizar pendientes por día y pendiente combinada con efecto de día.

**Nota logística:** ver `P0_agenda_dia2.md` — el día 2 de E04 se agenda como continuación fuera de la jornada principal si el curso no dispone de una segunda sesión.

## Tabla de registro

| campo | unidad/forma |
|---|---|
| día, ciclo, orden, hora | texto/entero |
| concentración NO del certificado y U,k | µmol/mol |
| impureza NO₂ del cilindro y U,k | nmol/mol en cilindro |
| q_NO, q_dil, caudal total | mL/min |
| NO generado antes de GPT | nmol/mol |
| O₃ asignado/NO₂ GPT | nmol/mol |
| NO residual | nmol/mol |
| NO, NOx, diferencia NOx−NO | nmol/mol |
| temperatura, presión, residencia GPT | °C, kPa, s |
| temperatura convertidor | °C |
| estabilidad, alarma, observación | texto |

## Modelo de cálculo

NO diluido: `N₀=c_cil·q_NO/(q_NO+q_dil)`. Corrección por impureza de NO₂ del cilindro: `I_mezcla=I_cil·q_NO/q_T` (ver defecto D5, valores en `dataset_nox_metadata.md`). Bajo GPT estequiométrica y O₃ limitante: `G_i=c_NO2,GPT,i=c_O3,i`, `N_res,i=N₀-G_i`. Respuesta diferencial observada: `R_i=X_i-N_i`. Ajuste recomendado:

\[
R_i=b+\eta G_i+\varepsilon_i.
\]

La pendiente `η` estima la eficiencia si la asignación GPT, sincronización y selectividad son adecuadas. La incertidumbre debe incluir certificado de NO/O₃, caudales, impureza, repetibilidad, ajuste y condiciones GPT. No interpretar selectividad frente a NOy desde este ensayo.

## Ejemplo numérico trabajado

Cilindro `c_cil=50.000 µmol/mol=50 000 nmol/mol`; `q_NO=45.00 mL/min`, `q_T=5000.0 mL/min` → `N₀=450.0 nmol/mol`. Para nivel GPT 160: `N_res=450.0-160.0=290.0 nmol/mol`. Impureza de NO₂ del cilindro (defecto D5, ver `dataset_nox_metadata.md`): `I_mezcla=I_cil·q_NO/q_T=500(45/5000)=4.50 nmol/mol`.

**Corrección de impureza antes del ajuste (defecto M2):** en el nivel `G=0` (sin O₃), la lectura diferencial cruda `X-N` no es solo el blanco del instrumento; incluye la impureza de NO₂ del cilindro. Antes de corregir, `X₀-N₀≈4.5–5.3 nmol/mol` (dominado por `I_mezcla=4.50 nmol/mol`, más un blanco residual pequeño y ruido de medición), no `≈0.4 nmol/mol`. Debe restarse `I_mezcla=4.50 nmol/mol` de cada `R_i` **antes** de ajustar la recta `R_i=b+\eta G_i`; de lo contrario el intercepto ajustado se contamina con la impureza y el criterio "intercepto ≤2 nmol/mol después de cero e impureza" queda mal aplicado.

Tabla de trabajo, con lecturas ya corregidas por impureza y con perturbaciones de medición controladas (`+0.35, -0.18, -0.35, -0.18, +0.35` nmol/mol, ortogonales al diseño `G_i` para no desplazar la pendiente ajustada, usadas para que `s(pendiente)` sea derivable de los datos en vez de asumida — defecto M8):

| G_i | N_i | X_i,raw (incluye impureza) | X_i,corr (=X_i,raw−4.50) | R_i=X_i,corr−N_i |
|---:|---:|---:|---:|---:|
| 0 | 449.9 | 455.15 | 450.65 | 0.75 |
| 40 | 409.8 | 453.32 | 448.82 | 39.02 |
| 80 | 369.9 | 452.05 | 447.55 | 77.65 |
| 120 | 329.8 | 450.92 | 446.42 | 116.62 |
| 160 | 289.9 | 450.35 | 445.85 | 155.95 |

Por construcción, la perturbación aplicada es ortogonal a la constante y a `G_i` (patrón `[+3200,-1600,-3200,-1600,+3200]` escalado), de modo que el ajuste OLS reproduce exactamente `η̂=0.970` y `b̂=0.40 nmol/mol`, con residuos iguales a la perturbación: `[0.35,-0.18,-0.35,-0.18,0.35]` nmol/mol. Con `Σ(G-Ḡ)²=16000` (`Ḡ=80`) y 3 grados de libertad:

\[
SSE=\sum e_i^2=0.35^2+0.18^2+0.35^2+0.18^2+0.35^2=0.4323,\qquad
s_{y/x}=\sqrt{0.4323/3}=0.3796,
\]

\[
se(\eta)=\frac{s_{y/x}}{\sqrt{\Sigma(G-\bar G)^2}}=\frac{0.3796}{\sqrt{16000}}=\frac{0.3796}{126.49}=0.0030.
\]

Con este error estándar de pendiente derivado de los datos (`0.0030`) y un componente de asignación GPT de `0.0040` en eficiencia:

\[
u(\eta)=\sqrt{0.0030^2+0.0040^2}=0.0050,\qquad U(\eta)=2u(\eta)=0.010,
\]

es decir `η=0.970±0.010 (k=2)`. Si día 2 entrega 0.966, la diferencia entre días es 0.004, menor que `√(0.005²+0.005²)=0.0071`: sin cambio significativo detectado.

## Criterios de aceptación

- NO residual >250 nmol/mol y >20 % del NO inicial en todos los niveles; el diseño propuesto deja 64.4 % en el máximo.
- Caudal total mayor que la demanda del analizador y bypass visible.
- Estabilidad <1 nmol/mol en 5 min antes de registrar.
- Pendiente dentro del criterio aprobado por método, fabricante y sistema de calidad aplicable. Para la práctica, usar 0.95–1.05 como ventana didáctica, no como límite normativo universal.
- **Criterio normativo EN 14211:** capacidad mínima del convertidor `η≥0.98`. El ejemplo numérico de esta sección (`η=0.970`) **no** cumpliría ese criterio normativo — ilustra un convertidor que debería disparar una acción de mantenimiento o reemplazo, no un resultado aceptable en operación regular. La ventana didáctica 0.95–1.05 sirve para practicar el ajuste y el cálculo de incertidumbre, no para aprobar el convertidor.
- Intercepto absoluto ≤2 nmol/mol después de cero e impureza; un valor mayor exige investigar blanco, impureza, sincronización o NOy.
- `R²≥0.995` y residuos sin curvatura visible para aceptación didáctica.
- Diferencia de pendientes entre días compatible con sus incertidumbres; si no, incluir precisión intermedia o declarar inestabilidad.
- El ensayo mide eficiencia, no selectividad del convertidor.

## Seguridad

NO es tóxico y se oxida a NO₂. Cilindro sujeto, regulador correcto, extracción activa y prueba de fugas obligatoria. O₃ es oxidante y tóxico: bypass a destructor y extracción. Desactivar O₃ antes de cerrar NO; purgar cámara y líneas con aire cero. No abrir el sistema ni desconectar la línea mientras exista O₃ o presión.
