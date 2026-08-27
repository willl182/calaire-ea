# M7 — Página 04 — Bloque 4 — Covarianza y cobertura — 34–48 min (acumulado: 48 min)

- **Sesión:** M7
- **Fuente:** [`modulos/M7_taller.md`](../modulos/M7_taller.md)
- **Tipo:** página/diapositiva del libreto

## Libreto

### Bloque 4 — Covarianza y cobertura — 34–48 min (acumulado: 48 min)

**Idea fuerza:** dependencia y cobertura son decisiones visibles del modelo y del informe.

El protocolo señala que las mediciones realizadas con el mismo SRP a distintas fracciones están correlacionadas y desarrolla la covarianza fotométrica en el App. 1 §3, pp. 24–25. En este ejercicio de un solo nivel no se construye una matriz entre niveles; se conserva la covarianza publicada entre \(a_0\) y \(a_1\):

\[
u_c^2(y)=a_1^2u^2(x)+u^2(a_0)+x^2u^2(a_1)+2x\operatorname{cov}(a_0,a_1).
\]

**Apoyo en el handout:** ver `handout_teorico_gum_o3.md`, §4.2 — Ley de propagación de incertidumbre, para el término cruzado de covarianza con su signo, y §4.3 — Doble conteo: GUM §4.3.10.

QUAM cap. 8 recomienda representar entradas que comparten patrón, calibración o datos como dependientes cuando corresponda. Covarianza es término cruzado del modelo, no nueva fila positiva. Si se usa valor absoluto o se agrega como componente independiente, cambia modelo y varianza.

El signo negativo no se elimina ni se reemplaza por valor absoluto. Para el ejercicio obligatorio se fija **\(k=2\)** como aproximación convencional a una cobertura de aproximadamente 95 %, adecuada para practicar construcción e interpretación del presupuesto cuando no se dispone de grados de libertad documentados para todas las entradas. Debe declararse que esta elección no sustituye una evaluación de cobertura más detallada cuando el uso previsto la exija.

**Material avanzado opcional, fuera de la actividad de 24 min:** revisar JCGM 100:2008, Anexo G.4, y `handout_teorico_gum_o3.md`, §4.5, para estudiar Welch–Satterthwaite y la selección de un cuantil t cuando existan grados de libertad sustentados. No se asignan grados de libertad ficticios ni se calcula \(\nu_{eff}\) en el entregable obligatorio.
