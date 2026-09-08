# Control documental Markdown — curso v2

Este inventario verifica la correspondencia entre sesiones, páginas/diapositivas, libretos y prácticas de `cursov2`. La fuente editable y trazable es Markdown; `curso_paquete_completo.html` es un artefacto derivado generado por `build_paquete_html.py`.

## Regla de correspondencia

- Cada sesión M1–M8 tiene un libreto principal en `modulos/`.
- Cada unidad temporal de exposición tiene exactamente un archivo individual en `paginas/`.
- Los módulos conservan el contexto, objetivos, actividades, errores frecuentes y cierre; su sección de guion funciona como índice de las páginas individuales.
- No existen archivos independientes PPT, PPTX u ODP en esta versión. Las páginas/diapositivas se representan por `paginas/*.md` y se ensamblan en HTML para consulta e impresión.

## Sesiones, libretos y páginas

| Sesión | Libreto principal | Páginas Markdown | Estado |
|---|---|---:|---|
| M1 | [`modulos/M1_trazabilidad.md`](modulos/M1_trazabilidad.md) | 5 | Completo |
| M2 | [`modulos/M2_modelo_medicion.md`](modulos/M2_modelo_medicion.md) | 4 | Completo |
| M3 | [`modulos/M3_conceptos_gum.md`](modulos/M3_conceptos_gum.md) | 4 | Completo |
| M4 | [`modulos/M4_presupuesto_analizador.md`](modulos/M4_presupuesto_analizador.md) | 5 | Completo |
| M5 | [`modulos/M5_patrones_transferencia.md`](modulos/M5_patrones_transferencia.md) | 5 | Completo |
| M6 | [`modulos/M6_no_nox_quimioluminiscencia.md`](modulos/M6_no_nox_quimioluminiscencia.md) | 4 | Completo |
| M7 | [`modulos/M7_taller.md`](modulos/M7_taller.md) | 6 | Completo |
| M8 | [`modulos/M8_opcional_monte_carlo.md`](modulos/M8_opcional_monte_carlo.md) | 6 | Completo; opcional |
| **Total** | **8 libretos** | **39 páginas** | **Completo** |

### Inventario por sesión

#### M1 — Metrología del ozono y cadena de trazabilidad

1. [`paginas/M1_01_3_1_que_significa_trazabilidad_0_a_4_min.md`](paginas/M1_01_3_1_que_significa_trazabilidad_0_a_4_min.md)
2. [`paginas/M1_02_3_2_por_que_el_ozono_exige_generacion_dinamica_4_a_9_min.md`](paginas/M1_02_3_2_por_que_el_ozono_exige_generacion_dinamica_4_a_9_min.md)
3. [`paginas/M1_03_3_3_la_cadena_documentada_e_ininterrumpida_9_a_14_min.md`](paginas/M1_03_3_3_la_cadena_documentada_e_ininterrumpida_9_a_14_min.md)
4. [`paginas/M1_04_3_4_jerarquia_srp_patrones_de_transferencia_y_analizador_14_a_20_min.md`](paginas/M1_04_3_4_jerarquia_srp_patrones_de_transferencia_y_analizador_14_a_20_min.md)
5. [`paginas/M1_05_3_5_tres_incertidumbres_que_no_deben_confundirse_20_a_27_min.md`](paginas/M1_05_3_5_tres_incertidumbres_que_no_deben_confundirse_20_a_27_min.md)

#### M2 — Modelo de medición: fotometría UV y Beer–Lambert

1. [`paginas/M2_01_3_1_subbloque_1_de_la_absorcion_uv_al_mensurando_010_min_acumulado_10_min.md`](paginas/M2_01_3_1_subbloque_1_de_la_absorcion_uv_al_mensurando_010_min_acumulado_10_min.md)
2. [`paginas/M2_02_3_2_subbloque_2_modelo_de_fraccion_molar_y_condiciones_fisicas_1021_min_acumulado_21_min.md`](paginas/M2_02_3_2_modelo_de_fraccion_molar_y_condiciones_fisicas_1021_min_acumulado_21_min.md)
3. [`paginas/M2_03_3_3_subbloque_3_coeficientes_de_sensibilidad_2129_min_acumulado_29_min.md`](paginas/M2_03_3_3_subbloque_3_coeficientes_de_sensibilidad_2129_min_acumulado_29_min.md)
4. [`paginas/M2_04_3_4_subbloque_4_fuentes_fisicas_y_componentes_constantes_o_proporcionales_2936_min_acumulado_36_min.md`](paginas/M2_04_3_4_subbloque_4_fuentes_fisicas_y_componentes_constantes_o_proporcionales_2936_min_acumulado_36_min.md)

#### M3 — Conceptos GUM

1. [`paginas/M3_01_3_1_tipo_a_y_tipo_b_0_00_a_0_09_acumulado_0_09_9_min.md`](paginas/M3_01_3_1_tipo_a_y_tipo_b_0_00_a_0_09_acumulado_0_09_9_min.md)
2. [`paginas/M3_02_3_2_tipo_a_que_representan_s_y_s_sqrt_n_0_09_a_0_18_acumulado_0_18_9_min.md`](paginas/M3_02_3_2_tipo_a_que_representan_s_y_s_sqrt_n_0_09_a_0_18_acumulado_0_18_9_min.md)
3. [`paginas/M3_03_3_3_tipo_b_y_pdfs_que_reaparecen_en_el_curso_0_18_a_0_29_acumulado_0_29_11_min.md`](paginas/M3_03_3_3_tipo_b_y_pdfs_que_reaparecen_en_el_curso_0_18_a_0_29_acumulado_0_29_11_min.md)
4. [`paginas/M3_04_3_4_contribuciones_combinacion_cuadratica_y_doble_conteo_0_29_a_0_38_acumulado_0_38_9_min.md`](paginas/M3_04_3_4_contribuciones_combinacion_cuadratica_y_doble_conteo_0_29_a_0_38_acumulado_0_38_9_min.md)

#### M4 — Presupuesto del analizador O₃

1. [`paginas/M4_01_3_0_del_proceso_al_presupuesto_0_00_a_0_06_acumulado_0_06_6_min.md`](paginas/M4_01_3_0_del_proceso_al_presupuesto_0_00_a_0_06_acumulado_0_06_6_min.md)
2. [`paginas/M4_02_3_1_del_dato_documental_a_la_fila_del_presupuesto_0_06_a_0_16_acumulado_0_16_10_min.md`](paginas/M4_02_3_1_del_dato_documental_a_la_fila_del_presupuesto_0_06_a_0_16_acumulado_0_16_10_min.md)
3. [`paginas/M4_03_3_2_combinacion_clasificacion_y_doble_conteo_0_16_a_0_26_acumulado_0_26_10_min.md`](paginas/M4_03_3_2_combinacion_clasificacion_y_doble_conteo_0_16_a_0_26_acumulado_0_26_10_min.md)
4. [`paginas/M4_04_3_3_lectura_critica_del_thermo_49i_0_26_a_0_35_acumulado_0_35_9_min.md`](paginas/M4_04_3_3_lectura_critica_del_thermo_49i_0_26_a_0_35_acumulado_0_35_9_min.md)
5. [`paginas/M4_05_3_4_comparacion_con_apoa_370_y_presupuestos_de_laboratorio_campo_0_35_a_0_43_acumulado_0_43_8_min.md`](paginas/M4_05_3_4_comparacion_con_apoa_370_y_presupuestos_de_laboratorio_campo_0_35_a_0_43_acumulado_0_43_8_min.md)

#### M5 — Patrones de transferencia

1. [`paginas/M5_01_bloque_08_min_verificacion_calibracion_y_estado_encontrado.md`](paginas/M5_01_bloque_08_min_verificacion_calibracion_y_estado_encontrado.md)
2. [`paginas/M5_02_bloque_818_min_diseno_de_una_comparacion_multipunto.md`](paginas/M5_02_bloque_818_min_diseno_de_una_comparacion_multipunto.md)
3. [`paginas/M5_03_bloque_1828_min_correccion_por_certificado_regresion_y_residuos.md`](paginas/M5_03_bloque_1828_min_correccion_por_certificado_regresion_y_residuos.md)
4. [`paginas/M5_04_bloque_2838_min_estabilidad_deriva_y_decision_de_ajustar.md`](paginas/M5_04_bloque_2838_min_estabilidad_deriva_y_decision_de_ajustar.md)
5. [`paginas/M5_05_bloque_6068_min_puesta_en_comun_y_sintesis_posterior_al_ejercicio.md`](paginas/M5_05_bloque_6068_min_puesta_en_comun_y_sintesis_posterior_al_ejercicio.md)

#### M6 — NO/NO₂/NOx por quimioluminiscencia

1. [`paginas/M6_01_3_1_que_mide_analizador_nox_0_00_a_0_12_acumulado_0_12_12_min.md`](paginas/M6_01_3_1_que_mide_analizador_nox_0_00_a_0_12_acumulado_0_12_12_min.md)
2. [`paginas/M6_02_3_2_modelo_convertidor_y_covarianza_0_12_a_0_27_acumulado_0_27_15_min.md`](paginas/M6_02_3_2_modelo_convertidor_y_covarianza_0_12_a_0_27_acumulado_0_27_15_min.md)
3. [`paginas/M6_03_3_3_fuentes_especificas_0_27_a_0_47_acumulado_0_47_20_min.md`](paginas/M6_03_3_3_fuentes_especificas_0_27_a_0_47_acumulado_0_47_20_min.md)
4. [`paginas/M6_04_3_4_presupuesto_informativo_en_14211_0_47_a_1_02_acumulado_1_02_15_min.md`](paginas/M6_04_3_4_presupuesto_informativo_en_14211_0_47_a_1_02_acumulado_1_02_15_min.md)

#### M7 — Taller integrador

1. [`paginas/M7_01_bloque_1_encuadre_del_caso_y_flujo_maestro_010_min_acumulado_10_min.md`](paginas/M7_01_bloque_1_encuadre_del_caso_y_flujo_maestro_010_min_acumulado_10_min.md)
2. [`paginas/M7_02_bloque_2_mensurando_y_modelo_1020_min_acumulado_20_min.md`](paginas/M7_02_bloque_2_mensurando_y_modelo_1020_min_acumulado_20_min.md)
3. [`paginas/M7_03_bloque_3_presupuesto_fotometrico_de_bipm_srp27_2034_min_acumulado_34_min.md`](paginas/M7_03_bloque_3_presupuesto_fotometrico_de_bipm_srp27_2034_min_acumulado_34_min.md)
4. [`paginas/M7_04_bloque_4_covarianza_y_cobertura_3448_min_acumulado_48_min.md`](paginas/M7_04_bloque_4_covarianza_y_cobertura_3448_min_acumulado_48_min.md)
5. [`paginas/M7_05_bloque_5_trabajo_de_equipos_4872_min_acumulado_72_min.md`](paginas/M7_05_bloque_5_trabajo_de_equipos_4872_min_acumulado_72_min.md)
6. [`paginas/M7_06_bloque_6_revision_cruzada_y_cierre_7285_min_acumulado_85_min.md`](paginas/M7_06_bloque_6_revision_cruzada_y_cierre_7285_min_acumulado_85_min.md)

#### M8 — Monte Carlo (opcional)

1. [`paginas/M8_01_0_000_03_apertura_y_proposito_3_min_acumulado_3_min.md`](paginas/M8_01_0_000_03_apertura_y_proposito_3_min_acumulado_3_min.md)
2. [`paginas/M8_02_0_030_08_procedimiento_de_propagacion_5_min_acumulado_8_min.md`](paginas/M8_02_0_030_08_procedimiento_de_propagacion_5_min_acumulado_8_min.md)
3. [`paginas/M8_03_0_080_13_numero_de_ensayos_estabilidad_y_tolerancia_5_min_acumulado_13_min.md`](paginas/M8_03_0_080_13_numero_de_ensayos_estabilidad_y_tolerancia_5_min_acumulado_13_min.md)
4. [`paginas/M8_04_0_130_23_demostracion_en_vivo_10_min_acumulado_23_min.md`](paginas/M8_04_0_130_23_demostracion_en_vivo_10_min_acumulado_23_min.md)
5. [`paginas/M8_05_0_230_26_interpretacion_metrologica_3_min_acumulado_26_min.md`](paginas/M8_05_0_230_26_interpretacion_metrologica_3_min_acumulado_26_min.md)
6. [`paginas/M8_06_0_260_30_sintesis_y_enlace_4_min_acumulado_30_min.md`](paginas/M8_06_0_260_30_sintesis_y_enlace_4_min_acumulado_30_min.md)

## Práctica de laboratorio (contenido aparte del curso de 9 h)

| Unidad | Archivo Markdown | Estado |
|---|---|---|
| Agenda | [`practica/P0_agenda_practica.md`](practica/P0_agenda_practica.md) | Completo |
| E01 | [`practica/E01_ruido_cero.md`](practica/E01_ruido_cero.md) | Protocolo |
| E02 | [`practica/E02_verificacion_multipunto.md`](practica/E02_verificacion_multipunto.md) | Protocolo |
| E03 | [`practica/E03_covarianza_no_nox.md`](practica/E03_covarianza_no_nox.md) | Protocolo |
| E04 | [`practica/E04_gpt_eficiencia_convertidor.md`](practica/E04_gpt_eficiencia_convertidor.md) | Protocolo |
| E05 | [`practica/E05_correccion_firmware.md`](practica/E05_correccion_firmware.md) | Protocolo |
| E06 | [`practica/E06_transmision_linea.md`](practica/E06_transmision_linea.md) | Protocolo |
| E07 | [`practica/E07_formacion_no2_linea.md`](practica/E07_formacion_no2_linea.md) | Protocolo |
| E08 | [`practica/E08_deriva_cero_span.md`](practica/E08_deriva_cero_span.md) | Protocolo |
| E09 | [`practica/E09_calidad_aire_cero.md`](practica/E09_calidad_aire_cero.md) | Protocolo |
| E11 | [`practica/E11_tiempo_respuesta.md`](practica/E11_tiempo_respuesta.md) | Protocolo |
| E14 | [`practica/E14_recorrido_documental.md`](practica/E14_recorrido_documental.md) | Protocolo |
| E15 | [`practica/E15_presupuesto_hibrido.md`](practica/E15_presupuesto_hibrido.md) | Protocolo y entregable |
| E16 | [`practica/E16_mcm_covarianza.md`](practica/E16_mcm_covarianza.md) | Protocolo |
| Registro | [`practica/hoja_registro_campo.md`](practica/hoja_registro_campo.md) | Plantilla |
| Seguridad | [`practica/checklist_montaje_seguridad.md`](practica/checklist_montaje_seguridad.md) | Checklist |

### Excepciones explícitas

- **E10, E12 y E13:** aparecen en el diagnóstico de la práctica, pero no tienen protocolo diseñado en esta versión; quedan fuera de P1/P2. No se crean archivos ficticios para aparentar cobertura.
- **M8:** tiene libreto y seis páginas Markdown, pero no `SOL_M8.md` porque es una demostración opcional conducida por el facilitador y no una actividad con solucionario separado.
- **PPT/PPTX/ODP:** no hay fuentes independientes. La representación documental equivalente es `paginas/*.md`; el HTML completo es generado, no fuente editable.

## Validación reproducible

Desde esta carpeta:

```bash
python3 paginas/generar_paginas.py
python3 build_paquete_html.py
```

El constructor valida que las 39 páginas declaradas existan, tengan extensión `.md`, sean únicas y contengan la sección `## Libreto`; además valida datasets, MathML, anclas, recursos embebidos y referencias externas.
