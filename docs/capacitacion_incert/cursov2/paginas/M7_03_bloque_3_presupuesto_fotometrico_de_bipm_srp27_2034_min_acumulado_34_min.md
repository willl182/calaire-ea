# M7 — Página 03 — Bloque 3 — Presupuesto fotométrico de BIPM-SRP27 — 20–34 min (acumulado: 34 min)

- **Sesión:** M7
- **Fuente:** [`modulos/M7_taller.md`](../modulos/M7_taller.md)
- **Tipo:** página/diapositiva del libreto

## Libreto

### Bloque 3 — Presupuesto fotométrico de BIPM-SRP27 — 20–34 min (acumulado: 34 min)

**Idea fuerza:** la fotometría UV combina una contribución absoluta y contribuciones proporcionales a la fracción de ozono.

**Apoyo en el handout:** ver `handout_teorico_gum_o3.md`, §3.2 — Distribución rectangular, §3.3 — Distribución normal y §3.4 — Distribución triangular, para leer la columna de distribuciones publicadas, y §4.4 — Presupuesto y contribuciones, para la estructura de la tabla.

El presupuesto se declara aplicable a BIPM-SRP27 y BIPM-SRP28 entre 0 y 500 nmol mol⁻¹ (BIPM.QM-K1 protocol v2.1, App. 1 §1, p. 21).

| Componente | Fuentes publicadas | Distribuciones publicadas | Incertidumbre estándar combinada | Contribución a \(u(x)\) |
|---|---|---|---:|---:|
| Longitud óptica \(L_{opt}\) | escala, repetibilidad, sesgo | rectangular, normal, rectangular | 0.52 cm | \(2.89\times10^{-3}x\) |
| Presión \(P\) | manómetro, diferencia entre celdas | rectangular, rectangular | 0.034 kPa | \(3.37\times10^{-4}x\) |
| Temperatura \(T\) | sonda, sesgo residual | rectangular, rectangular | 0.07 K | \(2.29\times10^{-4}x\) |
| Cociente de intensidades \(D\) | resolución, repetibilidad | rectangular, triangular | \(1.4\times10^{-5}\) | 0.28 nmol mol⁻¹ |
| Sección eficaz \(\sigma\) | valor convencional CCQM.O3.2019 | no indicada | \(0.35\times10^{-19}\ \mathrm{cm^2\ molecule^{-1}}\) | “–” en esta comparación |

Fuente: BIPM.QM-K1 protocol v2.1, App. 1 §1, pp. 21–22. Al comparar fotómetros UV que usan el mismo valor de sección eficaz, su incertidumbre común puede fijarse en cero; debe incluirse al comparar métodos o valores diferentes, o al evaluar el método completo (protocolo §4.1, p. 3).

La expresión simplificada publicada es

\[
u(x)=\sqrt{(0.28)^2+\left(2.92\times10^{-3}x\right)^2},
\]

con \(x\) en nmol mol⁻¹ (App. 1 §2, ecuación 14, p. 23). A 100 nmol mol⁻¹, el participante debe comprobar que \(u(x)\approx0.405\ \mathrm{nmol\ mol^{-1}}\).

Etiquetas de lectura: `D` aporta término absoluto; `L`, `P` y `T` aportan términos proporcionales; `σ` es común y se cancela solo bajo condiciones declaradas de comparación. Forma se conecta con QUAM App. E.5 y ejemplo A6:

\[
u(x)=\sqrt{u_0^2+(u_r x)^2}.
\]

No reutilizar expresión resumida y filas que ya contiene: produciría doble conteo.
