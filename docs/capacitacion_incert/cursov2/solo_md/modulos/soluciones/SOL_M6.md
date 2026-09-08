# Solución M6 — NO/NO₂/NOₓ por quimioluminiscencia

## 1 Modelo y lectura correcta

NO₂ no se obtiene como señal directa. Modelo mínimo:

\[
c_{NO_2}=c_{NO_x}-c_{NO}.
\]

Si arquitectura exige corrección explícita de eficiencia:

\[
c_{NO_2}=\frac{c_{NO_x}-c_{NO}}{\eta_c}.
\]

Aplicar solo si software no la incorpora. Eficiencia cuantifica fracción convertida; selectividad trata conversión de especies distintas de NO₂; estabilidad trata cambio temporal/ambiental.

## 2 Resultado GPT sintético

Ejecutar:

```bash
Rscript datasets/generar_dataset_nox.R
```

Para cada ciclo, ajustar:

```r
lm(lectura_no2_nmol_mol ~ no2_gpt_nmol_mol, data = subconjunto)
```

Con semilla 20260819, resultados redondeados son: ciclo 1, intercepto 0.442 y pendiente 0.9707; ciclo 2, intercepto 0.145 y pendiente 0.9720; ciclo 3, intercepto 0.072 y pendiente 0.9719. Diferencias frente a parámetros generadores provienen del ruido sintético y cuatro niveles por ciclo. La deriva programada de η, −0.0015 por ciclo, es inobservable frente a la dispersión de las pendientes ajustadas con cuatro niveles y ruido sintético; no debe inferirse una tendencia a partir de estas tres pendientes. Pendiente se interpreta como eficiencia solo dentro del modelo generado; no equivale por sí sola a aprobación del equipo.

Chequeos correctos:

- `lectura_no2_nmol_mol = lectura_nox_nmol_mol - lectura_no_nmol_mol` salvo redondeo;
- concentración cero no entra en estimación de pendiente de niveles GPT;
- caudal de NO en mL/min debe convertirse a L/min antes de mezclar con dilución;
- incertidumbre de eficiencia requiere regresión, repetición y trazabilidad de GPT; `1-eta` no es `u(eta)`.

## 3 Diagnóstico de línea

| Configuración | Residencia total (s) | Cambio (%) | Decisión esperada |
|---|---:|---:|---|
| A corta | 3.01 | 0.90 | aceptar y vigilar |
| B larga | 9.34 | 2.15 | reducir residencia y repetir |
| C larga caliente | 10.56 | 3.10 | invalidar hasta corregir |

Criterio 2 % pertenece al ejercicio, no a EN 14211 ni a regla universal. Controles: reducir longitud/volumen, aumentar caudal dentro de diseño, medir residencia externa e interna, controlar temperatura, revisar filtro y depósitos, verificar caída de presión y repetir prueba.

## 4 Caso diferencial con covarianza

Datos: NOₓ=205, NO=200, η=0.97, u(NOₓ)=1.2, u(NO)=1.0, u(η)=0.01 nmol/mol/fracción.

Resultado:

\[
y=\frac{5}{0.97}=5.1546\ \mathrm{nmol/mol}.
\]

Coeficientes:

\[
c_{NO_x}=1.03093,\quad c_{NO}=-1.03093,\quad c_\eta=-5.3141.
\]

### Sin covarianza, ρ=0

\[
u^2_{canales}=\frac{1.2^2+1.0^2}{0.97^2}=2.5933,
\]

\[
u^2_\eta=(5.3141\times0.01)^2=0.00282,
\]

\[
u_c=1.611\ \mathrm{nmol/mol},\qquad U(k=2)=3.222\ \mathrm{nmol/mol}.
\]

### Correlación positiva, ρ=0.70

\[
\operatorname{cov}=0.70(1.2)(1.0)=0.84\ (\mathrm{nmol/mol})^2,
\]

\[
u^2_{canales}=\frac{1.2^2+1.0^2-2(0.84)}{0.97^2}=0.8077,
\]

\[
u_c=0.900\ \mathrm{nmol/mol},\qquad U(k=2)=1.800\ \mathrm{nmol/mol}.
\]

Correlación positiva reduce incertidumbre de diferencia por signos opuestos de coeficientes. No seleccionar ρ para obtener resultado favorable; estimarlo con datos o justificarlo desde fuentes compartidas.

## 5 Reconstrucción del Anexo F

Valores verificados contra BS EN 14211:2012, Anexo F, ejemplo F.4, p. impresa 88. Anexo es informativo; tabla siguiente parafrasea datos, no reproduce texto normativo.

| Componente | u (nmol/mol) | Varianza aproximada |
|---|---:|---:|
| Repetibilidad a cero | 0.09 | 0.00 (sumada) |
| Repetibilidad a Ct | — | No entra en la suma |
| Falta de ajuste | 0.90 | 0.81 |
| Presión muestra | 0.06 | ~0.00 |
| Temperatura muestra | 0.26 | 0.07 |
| Temperatura entorno | 0.44 | 0.19 |
| Tensión | 0.02 | ~0.00 |
| H₂O | 0.249 | 0.06 |
| Otros interferentes | 0.35 | 0.12 |
| Promediación | 2.70 | 7.30 |
| Reproducibilidad de campo | 3.22 | 10.4 |
| Deriva cero | 0.58 | 0.33 |
| Deriva span | 1.44 | 2.08 |
| Diferencia muestra/calibración | 1.04 | 1.08 |
| Convertidor | 2.08 | 4.33 |
| Gas de calibración | 2.08 | 4.33 |
| Gas cero | 0.60 | 0.36 |

Publicación conserva redondeos:

\[
\sum u_i^2=30.4,\quad u_c=5.5\ \mathrm{nmol/mol},
\]

\[
U=2u_c=11.0\ \mathrm{nmol/mol},\quad W=100(11/104)=10.6\%.
\]

Contribuciones dominantes aproximadas: reproducibilidad de campo 34 %, promediación 24 %, convertidor 14 %, gas de calibración 14 % y deriva span 7 %. La suma directa de las varianzas listadas da aproximadamente 31.5 (nmol/mol)², no 30.4. La norma publica 30.4 sin explicar esta diferencia de aproximadamente 1.0 (nmol/mol)², del orden de la fila diferencia muestra/calibración. Se conserva el valor publicado y se declara explícitamente la discrepancia; no se atribuye a simples redondeos.

Comparación con 15 % solo válida en contexto europeo de medición fija indicado por estándar. No usar como requisito colombiano sin fuente vigente.

## 6 Conclusión modelo

> NO₂ es diferencia corregida entre canales, no lectura directa. Datos GPT muestran eficiencia cercana a 97 %, pero decisión requiere incertidumbre, selectividad y criterio aplicable. Línea corta permanece bajo criterio didáctico; líneas larga y caliente requieren corrección y repetición. A 5 nmol/mol, incertidumbre de canales domina resultado relativo y cambia mucho al modelar covarianza positiva justificada. Presupuesto Anexo F da uc=5.5 nmol/mol y W=10.6 %, con reproducibilidad, promediación, convertidor y gas como fuentes dominantes.

## 7 Criterios de valoración

**Completa:** modelo y signos correctos; eficiencia por ciclo; decisiones de línea; cálculo con y sin covarianza; total Anexo F; separación criterio/incertidumbre; control APOA-370.

**Parcial:** cálculo principal correcto, pero omite trazabilidad, covarianza, selectividad o condición didáctica del criterio.

**Incorrecta:** NO₂ directo; doble corrección; `1-eta` tratado como incertidumbre; suma lineal; covarianza con signo incorrecto; uso de APOA-370 como NOx.

## 8 Nota de control documental

APOA-370 corresponde a O₃ por absorción UV. El manual local APNA-370 (HORIBA Ambient NOx Monitor, 2021) está disponible; verificar si corresponde al equipo realmente instalado queda a cargo del operador. Ninguna cifra APOA-370 entra en solución NOx.
