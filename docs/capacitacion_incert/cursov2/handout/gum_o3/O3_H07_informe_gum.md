# 7. Informe según GUM §7

## 7.1 Contenido mínimo {#gum-informe-contenido-minimo}

JCGM 100 §7 exige información suficiente para comprender el resultado y repetir la evaluación cuando sea necesario. La síntesis siguiente combina el contenido de §7 con la organización didáctica de este handout. El informe basado en GUM/GUF debe incluir:

1. la definición completa del mensurando;
2. la estimación \(y\) y su unidad;
3. el modelo de medición y la relación funcional;
4. las correcciones aplicadas y las constantes usadas;
5. las fuentes de incertidumbre y el método Tipo A o Tipo B;
6. los datos, certificados, especificaciones y referencias de origen;
7. las PDFs asignadas, sus parámetros y su justificación;
8. las incertidumbres estándar y los grados de libertad;
9. los coeficientes de sensibilidad y las covarianzas o correlaciones;
10. el método de propagación: GUF, MCM u otro;
11. la incertidumbre estándar combinada;
12. la incertidumbre expandida, el factor de cobertura y la probabilidad, si corresponden;
13. los extremos y el tipo de intervalo de cobertura;
14. las reglas de redondeo;
15. el análisis de la validez del modelo, sus limitaciones y sus condiciones de uso.

Como información adicional requerida para la transparencia de la implementación del MCM, se debe agregar:

- el software y su versión;
- el generador pseudoaleatorio o la biblioteca utilizada;
- el manejo de las dependencias;
- el criterio adaptativo y \(\delta\);
- el número final de ensayos;
- la evidencia de estabilización;
- el método del intervalo: probabilísticamente simétrico o más corto.

## 7.2 Forma de expresar el resultado {#gum-informe-expresion}

Caso aproximadamente simétrico:

> Fracción molar de ozono: \(y=80.4\ \text{nmol/mol}\). Incertidumbre estándar combinada: \(u_c=0.62\ \text{nmol/mol}\). Incertidumbre expandida: \(U=1.3\ \text{nmol/mol}\), con \(k=2.09\), correspondiente a probabilidad de cobertura aproximada de 95 % y \(\nu_{eff}=19\). Resultado: \((80.4\pm1.3)\ \text{nmol/mol}\).

Caso asimétrico MCM:

> Fracción molar de ozono estimada: \(80.5\ \text{nmol/mol}\). Incertidumbre estándar: \(0.65\ \text{nmol/mol}\). Intervalo de cobertura más corto de 95 %: [79.4, 81.9] nmol/mol, obtenido mediante MCM adaptativo con tolerancia numérica \(\delta=0.01\ \text{nmol/mol}\).

No debe escribirse “95 % de confianza” sin aclarar el marco estadístico. En el GUM se habla de una probabilidad de cobertura basada en la información disponible. Tampoco debe informarse \(k=2\) y “95 %” como una equivalencia exacta cuando la distribución o los grados de libertad no la sustentan.

## 7.3 Redondeo {#gum-informe-redondeo}

Los cálculos intermedios conservan una precisión suficiente. El redondeo se realiza al final. La práctica habitual es la siguiente:

- informar la incertidumbre con una o dos cifras significativas, según la política y la estabilidad;
- redondear la estimación a la misma posición decimal que la incertidumbre;
- evitar más dígitos de los justificados;
- no redondear los componentes antes de la combinación.

Si la decisión depende de un límite, la regla de decisión y el riesgo deben documentarse por separado. La incertidumbre no sustituye el criterio de conformidad.

## 7.4 Lista de comprobación {#gum-informe-checklist}

Antes de aprobar el informe:

- ¿El mensurando está especificado sin ambigüedad?
- ¿El modelo representa la operación real y las etapas de transferencia?
- ¿Los efectos conocidos se corrigieron cuando correspondía?
- ¿Los datos Tipo A son estables e independientes, o se trató la autocorrelación?
- ¿Las PDFs Tipo B corresponden a la información disponible?
- ¿Se incluyeron las correlaciones por fuentes compartidas?
- ¿Se evitó el doble conteo según GUM §4.3.10?
- ¿El factor de cobertura corresponde a los grados y a la distribución?
- ¿El MCM, si se usó, alcanzó la tolerancia adaptativa?
- ¿Están declarados el intervalo y la probabilidad?
- ¿La trazabilidad y las fuentes pueden auditarse?

---
