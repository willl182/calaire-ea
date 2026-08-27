#!/usr/bin/env python3
"""Construye el paquete HTML autocontenido del curso de incertidumbre en O₃ y NOx."""

from __future__ import annotations

import base64
import csv
import html
import re
import shutil
import subprocess
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
COURSE_DIR = BASE_DIR.parent
OUTPUT = BASE_DIR / "curso_paquete_completo.html"
TITLE = "Curso de dos días — Incertidumbre en analizadores de O₃ y NOx · Paquete completo"
# Pandoc no permite tex_math_single_backslash sobre lector gfm. El lector
# markdown conserva tablas de tubería y admite ambos delimitadores usados aquí.
PANDOC_FROM = "markdown+tex_math_dollars+tex_math_single_backslash"

DESIGN = BASE_DIR / "diseno_curso_v2.md"
HANDOUTS = [
    ("O₃ — GUM y fotometría UV", BASE_DIR / "handout/handout_teorico_gum_o3.md"),
    ("NOx — quimioluminiscencia", BASE_DIR / "handout/handout_no_nox.md"),
]
MODULES = [
    ("m1", "M1 Trazabilidad", BASE_DIR / "modulos/M1_trazabilidad.md"),
    ("m2", "M2 Modelo de medición", BASE_DIR / "modulos/M2_modelo_medicion.md"),
    ("m3", "M3 Conceptos GUM", BASE_DIR / "modulos/M3_conceptos_gum.md"),
    ("m4", "M4 Presupuesto analizador O₃", BASE_DIR / "modulos/M4_presupuesto_analizador.md"),
    ("m5", "M5 Patrones de transferencia", BASE_DIR / "modulos/M5_patrones_transferencia.md"),
    ("m6", "M6 NO/NO₂/NOx por quimioluminiscencia", BASE_DIR / "modulos/M6_no_nox_quimioluminiscencia.md"),
    ("m7", "M7 Taller integrador", BASE_DIR / "modulos/M7_taller.md"),
    ("m8", "M8 Monte Carlo (opcional)", BASE_DIR / "modulos/M8_opcional_monte_carlo.md"),
]
PAGES = [
    ("m1", "m1-p01", BASE_DIR / "paginas/M1_01_3_1_que_significa_trazabilidad_0_a_4_min.md"),
    ("m1", "m1-p02", BASE_DIR / "paginas/M1_02_3_2_por_que_el_ozono_exige_generacion_dinamica_4_a_9_min.md"),
    ("m1", "m1-p03", BASE_DIR / "paginas/M1_03_3_3_la_cadena_documentada_e_ininterrumpida_9_a_14_min.md"),
    ("m1", "m1-p04", BASE_DIR / "paginas/M1_04_3_4_jerarquia_srp_patrones_de_transferencia_y_analizador_14_a_20_min.md"),
    ("m1", "m1-p05", BASE_DIR / "paginas/M1_05_3_5_tres_incertidumbres_que_no_deben_confundirse_20_a_27_min.md"),
    ("m2", "m2-p01", BASE_DIR / "paginas/M2_01_3_1_subbloque_1_de_la_absorcion_uv_al_mensurando_010_min_acumulado_10_min.md"),
    ("m2", "m2-p02", BASE_DIR / "paginas/M2_02_3_2_subbloque_2_modelo_de_fraccion_molar_y_condiciones_fisicas_1021_min_acumulado_21_min.md"),
    ("m2", "m2-p03", BASE_DIR / "paginas/M2_03_3_3_subbloque_3_coeficientes_de_sensibilidad_2129_min_acumulado_29_min.md"),
    ("m2", "m2-p04", BASE_DIR / "paginas/M2_04_3_4_subbloque_4_fuentes_fisicas_y_componentes_constantes_o_proporcionales_2936_min_acumulado_36_min.md"),
    ("m3", "m3-p01", BASE_DIR / "paginas/M3_01_3_1_tipo_a_y_tipo_b_0_00_a_0_09_acumulado_0_09_9_min.md"),
    ("m3", "m3-p02", BASE_DIR / "paginas/M3_02_3_2_tipo_a_que_representan_s_y_s_sqrt_n_0_09_a_0_18_acumulado_0_18_9_min.md"),
    ("m3", "m3-p03", BASE_DIR / "paginas/M3_03_3_3_tipo_b_y_pdfs_que_reaparecen_en_el_curso_0_18_a_0_29_acumulado_0_29_11_min.md"),
    ("m3", "m3-p04", BASE_DIR / "paginas/M3_04_3_4_contribuciones_combinacion_cuadratica_y_doble_conteo_0_29_a_0_38_acumulado_0_38_9_min.md"),
    ("m4", "m4-p01", BASE_DIR / "paginas/M4_01_3_0_del_proceso_al_presupuesto_0_00_a_0_06_acumulado_0_06_6_min.md"),
    ("m4", "m4-p02", BASE_DIR / "paginas/M4_02_3_1_del_dato_documental_a_la_fila_del_presupuesto_0_06_a_0_16_acumulado_0_16_10_min.md"),
    ("m4", "m4-p03", BASE_DIR / "paginas/M4_03_3_2_combinacion_clasificacion_y_doble_conteo_0_16_a_0_26_acumulado_0_26_10_min.md"),
    ("m4", "m4-p04", BASE_DIR / "paginas/M4_04_3_3_lectura_critica_del_thermo_49i_0_26_a_0_35_acumulado_0_35_9_min.md"),
    ("m4", "m4-p05", BASE_DIR / "paginas/M4_05_3_4_comparacion_con_apoa_370_y_presupuestos_de_laboratorio_campo_0_35_a_0_43_acumulado_0_43_8_min.md"),
    ("m5", "m5-p01", BASE_DIR / "paginas/M5_01_bloque_08_min_verificacion_calibracion_y_estado_encontrado.md"),
    ("m5", "m5-p02", BASE_DIR / "paginas/M5_02_bloque_818_min_diseno_de_una_comparacion_multipunto.md"),
    ("m5", "m5-p03", BASE_DIR / "paginas/M5_03_bloque_1828_min_correccion_por_certificado_regresion_y_residuos.md"),
    ("m5", "m5-p04", BASE_DIR / "paginas/M5_04_bloque_2838_min_estabilidad_deriva_y_decision_de_ajustar.md"),
    ("m5", "m5-p05", BASE_DIR / "paginas/M5_05_bloque_6068_min_puesta_en_comun_y_sintesis_posterior_al_ejercicio.md"),
    ("m6", "m6-p01", BASE_DIR / "paginas/M6_01_3_1_que_mide_analizador_nox_0_00_a_0_12_acumulado_0_12_12_min.md"),
    ("m6", "m6-p02", BASE_DIR / "paginas/M6_02_3_2_modelo_convertidor_y_covarianza_0_12_a_0_27_acumulado_0_27_15_min.md"),
    ("m6", "m6-p03", BASE_DIR / "paginas/M6_03_3_3_fuentes_especificas_0_27_a_0_47_acumulado_0_47_20_min.md"),
    ("m6", "m6-p04", BASE_DIR / "paginas/M6_04_3_4_presupuesto_informativo_en_14211_0_47_a_1_02_acumulado_1_02_15_min.md"),
    ("m7", "m7-p01", BASE_DIR / "paginas/M7_01_bloque_1_encuadre_del_caso_y_flujo_maestro_010_min_acumulado_10_min.md"),
    ("m7", "m7-p02", BASE_DIR / "paginas/M7_02_bloque_2_mensurando_y_modelo_1020_min_acumulado_20_min.md"),
    ("m7", "m7-p03", BASE_DIR / "paginas/M7_03_bloque_3_presupuesto_fotometrico_de_bipm_srp27_2034_min_acumulado_34_min.md"),
    ("m7", "m7-p04", BASE_DIR / "paginas/M7_04_bloque_4_covarianza_y_cobertura_3448_min_acumulado_48_min.md"),
    ("m7", "m7-p05", BASE_DIR / "paginas/M7_05_bloque_5_trabajo_de_equipos_4872_min_acumulado_72_min.md"),
    ("m7", "m7-p06", BASE_DIR / "paginas/M7_06_bloque_6_revision_cruzada_y_cierre_7285_min_acumulado_85_min.md"),
    ("m8", "m8-p01", BASE_DIR / "paginas/M8_01_0_000_03_apertura_y_proposito_3_min_acumulado_3_min.md"),
    ("m8", "m8-p02", BASE_DIR / "paginas/M8_02_0_030_08_procedimiento_de_propagacion_5_min_acumulado_8_min.md"),
    ("m8", "m8-p03", BASE_DIR / "paginas/M8_03_0_080_13_numero_de_ensayos_estabilidad_y_tolerancia_5_min_acumulado_13_min.md"),
    ("m8", "m8-p04", BASE_DIR / "paginas/M8_04_0_130_23_demostracion_en_vivo_10_min_acumulado_23_min.md"),
    ("m8", "m8-p05", BASE_DIR / "paginas/M8_05_0_230_26_interpretacion_metrologica_3_min_acumulado_26_min.md"),
    ("m8", "m8-p06", BASE_DIR / "paginas/M8_06_0_260_30_sintesis_y_enlace_4_min_acumulado_30_min.md"),
]
CONTROL_DOC = BASE_DIR / "control_documental_md.md"
PRACTICE = [
    ("p0", "P0 Agenda del Día 2", BASE_DIR / "practica/P0_agenda_dia2.md"),
    ("e01", "E01 Ruido y repetibilidad de cero", BASE_DIR / "practica/E01_ruido_cero.md"),
    ("e02", "E02 Verificación multipunto O₃", BASE_DIR / "practica/E02_verificacion_multipunto.md"),
    ("e03", "E03 Covarianza NO/NOx", BASE_DIR / "practica/E03_covarianza_no_nox.md"),
    ("e04", "E04 GPT y eficiencia del convertidor", BASE_DIR / "practica/E04_gpt_eficiencia_convertidor.md"),
    ("e05", "E05 Corrección de firmware", BASE_DIR / "practica/E05_correccion_firmware.md"),
    ("e06", "E06 Transmisión de línea", BASE_DIR / "practica/E06_transmision_linea.md"),
    ("e07", "E07 Formación de NO₂ en línea", BASE_DIR / "practica/E07_formacion_no2_linea.md"),
    ("e08", "E08 Deriva de cero y span", BASE_DIR / "practica/E08_deriva_cero_span.md"),
    ("e09", "E09 Calidad de aire cero", BASE_DIR / "practica/E09_calidad_aire_cero.md"),
    ("e11", "E11 Tiempo de respuesta", BASE_DIR / "practica/E11_tiempo_respuesta.md"),
    ("e14", "E14 Recorrido documental", BASE_DIR / "practica/E14_recorrido_documental.md"),
    ("e15", "E15 Presupuesto híbrido", BASE_DIR / "practica/E15_presupuesto_hibrido.md"),
    ("e16", "E16 MCM con covarianza", BASE_DIR / "practica/E16_mcm_covarianza.md"),
    ("registro-campo", "Hoja de registro de campo", BASE_DIR / "practica/hoja_registro_campo.md"),
    ("checklist-seguridad", "Checklist de montaje y seguridad", BASE_DIR / "practica/checklist_montaje_seguridad.md"),
]
SOLUTIONS = [
    ("m1", BASE_DIR / "modulos/soluciones/SOL_M1.md"),
    ("m2", BASE_DIR / "modulos/soluciones/SOL_M2.md"),
    ("m3", BASE_DIR / "modulos/soluciones/SOL_M3.md"),
    ("m4", BASE_DIR / "modulos/soluciones/SOL_M4.md"),
    ("m5", BASE_DIR / "modulos/soluciones/SOL_M5.md"),
    ("m6", BASE_DIR / "modulos/soluciones/SOL_M6.md"),
    ("m7", BASE_DIR / "modulos/soluciones/SOL_M7.md"),
]
DATASET_METADATA = BASE_DIR / "datasets/dataset_metadata.md"
DATASET_CSV = BASE_DIR / "datasets/dataset_verificacion_multipunto.csv"
DATASET_R = BASE_DIR / "datasets/generar_dataset.R"
NOX_METADATA = BASE_DIR / "datasets/dataset_nox_metadata.md"
NOX_GPT_CSV = BASE_DIR / "datasets/dataset_nox_gpt_convertidor.csv"
NOX_LINE_CSV = BASE_DIR / "datasets/dataset_nox_linea_muestreo.csv"
NOX_DATASET_R = BASE_DIR / "datasets/generar_dataset_nox.R"
TEMPLATE_CSV = BASE_DIR / "plantillas/plantilla_presupuesto_casos.csv"
TEMPLATE_R = BASE_DIR / "plantillas/plantilla_presupuesto.R"
TEMPLATE_PY = BASE_DIR / "plantillas/generar_plantilla_xlsx.py"
TEMPLATE_XLSX = BASE_DIR / "plantillas/plantilla_presupuesto.xlsx"
NOX_TEMPLATE_CSV = BASE_DIR / "plantillas/plantilla_presupuesto_nox.csv"
NOX_TEMPLATE_R = BASE_DIR / "plantillas/plantilla_presupuesto_nox.R"
MCM_R = BASE_DIR / "scripts/demo_mcm_beer_lambert.R"
MCM_PNG = BASE_DIR / "scripts/demo_mcm_pdf_salida.png"
KRISS = BASE_DIR / "casos/extracto_kriss_2024.md"

SECTIONS = [
    ("portada", "Portada e índice"),
    ("diseno-curso", "Diseño del curso"),
    ("handout", "Handouts"),
    ("guiones", "Guiones M1–M7 obligatorios + M8 opcional"),
    ("practica", "Práctica de laboratorio (Día 2)"),
    ("materiales", "Materiales"),
    ("solucionarios", "Solucionarios — solo instructor"),
    ("reproducibilidad", "Apéndice de reproducibilidad"),
]

MATERIALS = [
    ("material-dataset", "Dataset sintético O₃"),
    ("material-nox-gpt", "Dataset GPT NOx"),
    ("material-nox-linea", "Línea de muestreo NOx"),
    ("material-plantilla", "Plantilla de presupuesto O₃"),
    ("material-plantilla-nox", "Plantilla de presupuesto NOx"),
    ("material-mcm", "Demostración MCM (opcional)"),
    ("material-kriss", "Caso KRISS 2024"),
]

CSS = r"""
:root{
  --bg:#f7f8fa;--surface:#fff;--ink:#1c2330;--muted:#5a6478;
  --accent:#0e6ba8;--accent-soft:#e3f0f9;--line:#dfe3ea;
  --ok:#2e7d52;--warn:#9b5210;--chip:#eef1f6;--code:#f3f5f8;
  color-scheme:light dark;
}
@media(prefers-color-scheme:dark){:root{
  --bg:#12161d;--surface:#1a2029;--ink:#e6e9ef;--muted:#a8b1c0;
  --accent:#5db3e8;--accent-soft:#173142;--line:#354052;
  --ok:#6fc79a;--warn:#f0ad68;--chip:#232b37;--code:#10151c;
}}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:1rem}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.62 "Segoe UI",system-ui,-apple-system,sans-serif}
a{color:var(--accent)}
a:focus-visible,summary:focus-visible{outline:3px solid var(--accent);outline-offset:3px}
.sidebar{position:fixed;inset:0 auto 0 0;width:17rem;overflow-y:auto;padding:1.25rem 1rem;background:var(--surface);border-right:1px solid var(--line);z-index:10}
.sidebar strong{display:block;color:var(--accent);margin-bottom:.75rem}
.sidebar ul{list-style:none;margin:0;padding:0}
.sidebar li{margin:.15rem 0}
.sidebar a{display:block;padding:.38rem .55rem;border-radius:6px;text-decoration:none;color:var(--ink)}
.sidebar a:hover{background:var(--accent-soft);color:var(--accent)}
main{max-width:1060px;margin-left:max(17rem,calc((100vw - 1400px)/2));padding:2rem 2rem 5rem}
.hero{border-left:5px solid var(--accent);padding:1.25rem 1.5rem;margin:0 0 2rem;background:var(--surface);border-radius:0 10px 10px 0;box-shadow:0 1px 3px rgba(0,0,0,.08)}
.hero h1{font-size:clamp(1.65rem,3vw,2.35rem);line-height:1.2;margin:.15rem 0 .65rem}
.meta{color:var(--muted);font-size:.92rem}
.chip{display:inline-block;background:var(--chip);border:1px solid var(--line);border-radius:999px;padding:.18rem .7rem;margin:.6rem .25rem 0 0;font-size:.82rem;color:var(--muted)}
section.major{margin:3rem 0 4rem;scroll-margin-top:1rem}
section.major>h2{font-size:1.55rem;border-bottom:3px solid var(--accent);padding-bottom:.45rem;margin-bottom:1.3rem}
.source-block{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:1.15rem 1.35rem;margin:1.25rem 0;box-shadow:0 1px 2px rgba(0,0,0,.04)}
.source-block>h3:first-child{margin-top:0;color:var(--accent)}
h1,h2,h3,h4,h5,h6{line-height:1.28;scroll-margin-top:1rem}
h1{font-size:1.65rem}h2{font-size:1.38rem;margin-top:2.2rem}h3{font-size:1.16rem;margin-top:1.7rem}h4{font-size:1.02rem}
.index-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(14rem,1fr));gap:.65rem;padding:0;list-style:none}
.index-grid a{display:block;height:100%;padding:.8rem 1rem;background:var(--surface);border:1px solid var(--line);border-radius:8px;text-decoration:none;font-weight:600}
.tablewrap{overflow-x:auto;margin:1rem 0;border:1px solid var(--line);border-radius:8px}
table{border-collapse:collapse;width:100%;min-width:38rem;background:var(--surface);font-size:.9rem}
th,td{border:1px solid var(--line);padding:.48rem .65rem;text-align:left;vertical-align:top}
th{background:var(--accent-soft);position:sticky;top:0}
pre{overflow-x:auto;max-width:100%;padding:1rem;background:var(--code);border:1px solid var(--line);border-radius:8px;line-height:1.45;tab-size:2}
code{font-family:"Cascadia Code","SFMono-Regular",Consolas,monospace;font-size:.88em}
:not(pre)>code{background:var(--chip);padding:.08rem .34rem;border-radius:4px}
figure{margin:1.25rem 0;text-align:center}
figure img{max-width:100%;height:auto;background:#fff;border:1px solid var(--line);border-radius:8px}
figcaption{color:var(--muted);font-size:.9rem;margin-top:.4rem}
.notice{border-left:5px solid var(--warn);background:color-mix(in srgb,var(--warn) 12%,var(--surface));padding:.85rem 1rem;border-radius:0 8px 8px 0;margin:1rem 0}
details{background:var(--surface);border:1px solid var(--line);border-radius:9px;margin:1rem 0;padding:.2rem 1rem 1rem}
summary{cursor:pointer;font-weight:700;color:var(--accent);padding:.8rem 0}
.math.display{overflow-x:auto;display:block;padding:.35rem 0}
hr{border:0;border-top:1px solid var(--line);margin:2rem 0}
.path-list code{overflow-wrap:anywhere}
footer{margin-top:3rem;color:var(--muted);font-size:.88rem;border-top:1px solid var(--line);padding-top:1rem}
.sidebar ul.sub{list-style:none;margin:.1rem 0 .4rem;padding-left:.8rem;border-left:1px solid var(--line)}
.sidebar ul.sub li{margin:.05rem 0}
.sidebar ul.sub a{padding:.26rem .5rem;font-size:.85rem;color:var(--muted)}
.sidebar ul.sub a:hover{background:var(--accent-soft);color:var(--accent)}
.sidebar details{background:none;border:0;margin:0;padding:0}
.sidebar details>summary{list-style:none;padding:0;font-weight:400;color:var(--ink);display:flex;align-items:center;gap:.3rem;border-radius:6px}
.sidebar details>summary::-webkit-details-marker{display:none}
.sidebar details>summary::before{content:"▸";font-size:.7em;color:var(--muted);transition:transform .15s}
.sidebar details[open]>summary::before{transform:rotate(90deg)}
.sidebar details>summary:hover{background:var(--accent-soft);color:var(--accent)}
.sidebar details>summary>a{flex:1;padding:.38rem .1rem .38rem 0}
@media(max-width:900px){.sidebar{position:static;width:auto;border-right:0;border-bottom:1px solid var(--line)}.sidebar>ul{display:flex;gap:.25rem;overflow-x:auto}.sidebar>ul>li{flex:0 0 auto}.sidebar a{white-space:nowrap}.sidebar ul.sub{display:none}.sidebar details>summary::before{display:none}main{margin:0;padding:1.25rem}}
@media print{
  :root{--bg:#fff;--surface:#fff;--ink:#000;--muted:#333;--accent:#245b7a;--accent-soft:#eef4f7;--line:#aaa;--code:#f5f5f5}
  body{background:#fff;color:#000;font-size:10.5pt}.sidebar{display:none}main{max-width:none;margin:0;padding:0}
  .hero,.source-block{box-shadow:none}section.major{break-before:page;margin:0 0 1.2rem}.source-block{break-inside:auto}
  a{color:#000;text-decoration:none}pre,.tablewrap{overflow:visible}table{min-width:0;font-size:8.5pt}th{position:static}
  details{display:block}details>summary{display:none}details>*{display:block!important}figure img{max-height:22cm}
  .index-grid{display:block}.index-grid li{margin:.3rem 0}
}
"""


def require_files(paths: list[Path]) -> None:
    missing = [str(path) for path in paths if not path.is_file()]
    if missing:
        raise FileNotFoundError("Faltan archivos requeridos:\n" + "\n".join(missing))


def pandoc_fragment(path: Path, id_prefix: str = "") -> str:
    command = [
        "pandoc",
        "--from",
        PANDOC_FROM,
        "--to",
        "html5",
        "--mathml",
        "--wrap=none",
        str(path),
    ]
    if id_prefix:
        command.insert(-1, f"--id-prefix={id_prefix}")
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return wrap_tables(result.stdout)


def wrap_tables(fragment: str) -> str:
    return re.sub(r"(?s)(<table(?:\s[^>]*)?>.*?</table>)", r'<div class="tablewrap">\1</div>', fragment)


def strip_tags(fragment: str) -> str:
    return re.sub(r"<[^>]+>", "", fragment).strip()


def extract_h2_headings(fragment: str) -> list[tuple[str, str]]:
    matches = re.findall(r'<h2 id="([^"]+)"[^>]*>(.*?)</h2>', fragment, flags=re.DOTALL)
    return [(hid, strip_tags(label)) for hid, label in matches]


def code_block(path: Path, language: str) -> str:
    content = path.read_text(encoding="utf-8")
    return (
        f'<pre><code class="language-{html.escape(language, quote=True)}">'
        f"{html.escape(content)}"
        "</code></pre>"
    )


def csv_table(path: Path, caption: str) -> tuple[str, int]:
    with path.open(newline="", encoding="utf-8-sig") as stream:
        rows = list(csv.reader(stream))
    if not rows:
        raise ValueError(f"CSV vacío: {path}")
    head, body = rows[0], rows[1:]
    parts = [f'<div class="tablewrap"><table><caption>{html.escape(caption)}</caption><thead><tr>']
    parts.extend(f"<th scope=\"col\">{html.escape(cell)}</th>" for cell in head)
    parts.append("</tr></thead><tbody>")
    for row in body:
        parts.append("<tr>")
        parts.extend(f"<td>{html.escape(cell)}</td>" for cell in row)
        parts.append("</tr>")
    parts.append("</tbody></table></div>")
    return "".join(parts), len(body)


def data_uri(path: Path) -> str:
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def section(section_id: str, title: str, body: str) -> str:
    return f'<section class="major" id="{section_id}"><h2>{html.escape(title)}</h2>{body}</section>'


def source_block(title: str, body: str, block_id: str | None = None) -> str:
    id_attr = f' id="{html.escape(block_id, quote=True)}"' if block_id else ""
    return f'<article class="source-block"{id_attr}><h3>{html.escape(title)}</h3>{body}</article>'


def page_label(path: Path) -> str:
    first_line = path.read_text(encoding="utf-8").splitlines()[0]
    if not first_line.startswith("# "):
        raise ValueError(f"Página sin título Markdown: {path}")
    return first_line[2:].strip()


def page_link_map() -> dict[str, str]:
    return {path.name: f"#guion-{page_id}" for _, page_id, path in PAGES}


def rewrite_page_links(fragment: str) -> str:
    for filename, anchor in page_link_map().items():
        fragment = fragment.replace(f'href="../paginas/{filename}"', f'href="{anchor}"')
    return fragment


def validate_pages() -> None:
    page_ids = [page_id for _, page_id, _ in PAGES]
    page_paths = [path for _, _, path in PAGES]
    if len(page_ids) != len(set(page_ids)):
        raise ValueError("Hay identificadores de páginas duplicados")
    if len(page_paths) != len(set(page_paths)):
        raise ValueError("Hay rutas de páginas duplicadas")
    declared_modules = {module_id for module_id, _, _ in MODULES}
    for module_id, page_id, path in PAGES:
        if module_id not in declared_modules:
            raise ValueError(f"Página {page_id} referencia módulo inexistente: {module_id}")
        if path.suffix.lower() != ".md":
            raise ValueError(f"La página {page_id} no es Markdown: {path}")
        if not path.is_file():
            raise FileNotFoundError(f"Falta página declarada: {path}")
        if "## Libreto" not in path.read_text(encoding="utf-8"):
            raise ValueError(f"Página sin sección Libreto: {path}")


def build() -> tuple[str, int, int, int, int]:
    validate_pages()
    required = [
        DESIGN,
        CONTROL_DOC,
        *(path for _, path in HANDOUTS),
        *(path for _, _, path in MODULES),
        *(path for _, _, path in PAGES),
        *(path for _, _, path in PRACTICE),
        *(path for _, path in SOLUTIONS),
        DATASET_METADATA,
        DATASET_CSV,
        DATASET_R,
        NOX_METADATA,
        NOX_GPT_CSV,
        NOX_LINE_CSV,
        NOX_DATASET_R,
        TEMPLATE_CSV,
        TEMPLATE_R,
        TEMPLATE_PY,
        TEMPLATE_XLSX,
        NOX_TEMPLATE_CSV,
        NOX_TEMPLATE_R,
        MCM_R,
        MCM_PNG,
        KRISS,
    ]
    require_files(required)
    if shutil.which("pandoc") is None:
        raise RuntimeError("pandoc no está disponible en PATH")

    top_nav_items = "".join(f'<li><a href="#{sid}">{html.escape(label)}</a></li>' for sid, label in SECTIONS)
    index = f'<ul class="index-grid">{top_nav_items}</ul>'
    portada = section(
        "portada",
        "Portada e índice",
        f'<header class="hero"><h1>{html.escape(TITLE)}</h1>'
        '<p class="meta">Curso técnico · Día 1 conceptual de 9 h + M8 opcional · Día 2 de laboratorio · material integrado y reproducible · 2026-08-26</p>'
        '<span class="chip">GUM + QUAM</span><span class="chip">Fotometría UV O₃</span>'
        '<span class="chip">Quimioluminiscencia NOx</span><span class="chip">Monte Carlo opcional</span>'
        '</header><p>Documento único para consulta en pantalla, trabajo de aula e impresión. '
        'Incluye contenido de participante y material identificado para instructor.</p>'
        f'<h3>Índice general</h3>{index}',
    )

    design_fragment = pandoc_fragment(DESIGN)
    design = section("diseno-curso", "Diseño del curso", design_fragment)
    design_headings = extract_h2_headings(design_fragment)

    handout_blocks = []
    handout_headings = []
    for index, (title, path) in enumerate(HANDOUTS, start=1):
        fragment = pandoc_fragment(path, f"handout-{index}-")
        block_id = f"handout-{index}"
        handout_blocks.append(source_block(title, fragment, block_id))
        handout_headings.append((block_id, title))
    handout = section("handout", "Handouts O₃ y NOx", "".join(handout_blocks))

    pages_by_module: dict[str, list[tuple[str, Path]]] = {module_id: [] for module_id, _, _ in MODULES}
    for module_id, page_id, path in PAGES:
        pages_by_module[module_id].append((page_id, path))
    module_blocks = []
    for module_id, title, path in MODULES:
        module_fragment = rewrite_page_links(pandoc_fragment(path, f"guion-{module_id}-"))
        page_fragments = []
        for page_id, page_path in pages_by_module[module_id]:
            page_fragments.append(
                source_block(
                    page_label(page_path),
                    pandoc_fragment(page_path, f"guion-{page_id}-"),
                    f"guion-{page_id}",
                )
            )
        module_blocks.append(
            source_block(
                f"Guion {title}",
                module_fragment + "".join(page_fragments),
                f"guion-{module_id}",
            )
        )
    modules = section("guiones", "Guiones M1–M7 obligatorios + M8 opcional", "".join(module_blocks))

    practice_blocks = []
    for practice_id, title, path in PRACTICE:
        block_id = f"practica-{practice_id}"
        practice_blocks.append(source_block(title, pandoc_fragment(path, f"{block_id}-"), block_id))
    practice = section("practica", "Práctica de laboratorio (Día 2)", "".join(practice_blocks))

    dataset_table, dataset_rows = csv_table(DATASET_CSV, "Dataset sintético de verificación multipunto")
    nox_gpt_table, nox_gpt_rows = csv_table(NOX_GPT_CSV, "Dataset GPT y convertidor NOx")
    nox_line_table, nox_line_rows = csv_table(NOX_LINE_CSV, "Dataset de línea de muestreo NOx")
    template_table, template_rows = csv_table(TEMPLATE_CSV, "Casos precargados de la plantilla de presupuesto O₃")
    nox_template_table, nox_template_rows = csv_table(NOX_TEMPLATE_CSV, "Plantilla de presupuesto NOx")
    materials_body = "".join(
        [
            source_block(
                "Dataset sintético",
                pandoc_fragment(DATASET_METADATA)
                + f'<p><strong>Tabla completa:</strong> {dataset_rows} filas de datos.</p>'
                + dataset_table
                + '<h4>Código R del generador</h4>'
                + code_block(DATASET_R, "r"),
                "material-dataset",
            ),
            source_block(
                "Dataset GPT NOx",
                pandoc_fragment(NOX_METADATA)
                + f'<p><strong>Tabla completa:</strong> {nox_gpt_rows} filas.</p>'
                + nox_gpt_table
                + '<h4>Código R del generador NOx</h4>'
                + code_block(NOX_DATASET_R, "r"),
                "material-nox-gpt",
            ),
            source_block(
                "Línea de muestreo NOx",
                f'<p><strong>Tabla completa:</strong> {nox_line_rows} configuraciones sintéticas.</p>'
                + nox_line_table,
                "material-nox-linea",
            ),
            source_block(
                "Plantilla de presupuesto O₃",
                '<p>Plantilla para componentes, PDF, divisor, coeficiente de sensibilidad, contribución y clasificación. '
                f'Existe también archivo de hoja de cálculo <code>{html.escape(TEMPLATE_XLSX.name)}</code>, '
                'no embebido como descarga para mantener navegación autocontenida y auditable.</p>'
                f'<p><strong>Tabla de casos:</strong> {template_rows} filas.</p>'
                + template_table
                + '<h4>Código R de la plantilla</h4>'
                + code_block(TEMPLATE_R, "r")
                + '<h4>Código Python que genera el XLSX</h4>'
                + code_block(TEMPLATE_PY, "python"),
                "material-plantilla",
            ),
            source_block(
                "Plantilla de presupuesto NOx",
                '<p>Plantilla auditable para presupuesto EN 14211, modelo diferencial NOx−NO, eficiencia del convertidor y covarianza.</p>'
                f'<p><strong>Tabla base:</strong> {nox_template_rows} filas.</p>'
                + nox_template_table
                + '<h4>Código R de la plantilla NOx</h4>'
                + code_block(NOX_TEMPLATE_R, "r"),
                "material-plantilla-nox",
            ),
            source_block(
                "Demostración MCM — material avanzado opcional",
                '<p>Implementación reproducible del método de Monte Carlo para modelo Beer–Lambert. Material opcional conducido por el facilitador después del cierre obligatorio.</p>'
                + code_block(MCM_R, "r")
                + f'<figure><img src="{data_uri(MCM_PNG)}" alt="Salida gráfica de la demostración Monte Carlo Beer–Lambert">'
                '<figcaption>Distribución de salida y comparación GUF–MCM generada por script del curso.</figcaption></figure>',
                "material-mcm",
            ),
            source_block("Caso KRISS 2024", pandoc_fragment(KRISS), "material-kriss"),
        ]
    )
    materials = section("materiales", "Materiales", materials_body)

    solution_details = [
        '<div class="notice" role="note"><strong>Solo instructor.</strong> '
        'Bloques colapsados para evitar exposición accidental durante ejercicios. En impresión se muestran abiertos.</div>'
    ]
    solutions_nav: list[tuple[str, str]] = []
    for module_id, path in SOLUTIONS:
        module_name = module_id.upper()
        sol_id = f"sol-{module_id}"
        solutions_nav.append((sol_id, f"Solucionario {module_name}"))
        solution_details.append(
            f'<details id="{sol_id}"><summary>Solucionario {html.escape(module_name)} — solo instructor</summary>'
            f'{pandoc_fragment(path, f"sol-{module_id}-")}</details>'
        )
    solution_details.append(
        '<p class="meta">M8 es material avanzado opcional y corresponde a demostración del facilitador; no requiere solucionario separado.</p>'
    )
    solutions = section("solucionarios", "Solucionarios — solo instructor", "".join(solution_details))

    paths = [path.relative_to(COURSE_DIR).as_posix() for path in required]
    path_items = "".join(f"<li><code>{html.escape(path)}</code></li>" for path in paths)
    reproducibility_body = (
        '<p>Construcción usa Python 3, biblioteca estándar y ejecutable <code>pandoc</code> del sistema. No requiere pip.</p>'
        '<h3>Regeneración</h3>'
        '<pre><code class="language-bash">cd docs/capacitacion_incert/cursov2\npython3 build_paquete_html.py</code></pre>'
        '<h3>Semillas y artefactos</h3>'
        '<ul><li>Dataset O₃: semilla R <code>20260817</code>; regenerar con <code>Rscript datasets/generar_dataset.R</code>.</li>'
        '<li>Datasets NOx: semilla R <code>20260819</code>; regenerar con <code>Rscript datasets/generar_dataset_nox.R</code>.</li>'
        '<li>Plantilla NOx: comprobar con <code>Rscript plantillas/plantilla_presupuesto_nox.R</code>.</li>'
        '<li>Demo MCM: semilla y criterio adaptativo definidos en <code>scripts/demo_mcm_beer_lambert.R</code>.</li>'
        '<li>PNG: regenerar con <code>Rscript scripts/demo_mcm_beer_lambert.R</code>.</li>'
        '<li>Plantilla XLSX O₃: regenerar con <code>python3 plantillas/generar_plantilla_xlsx.py</code>.</li></ul>'
        '<h3>Fuentes ensambladas</h3>'
        f'<ul class="path-list">{path_items}</ul>'
        '<h3>Conversión matemática</h3>'
        f'<p>Markdown convertido con <code>pandoc --from {html.escape(PANDOC_FROM)} --to html5 --mathml</code>. '
        'Se aceptan delimitadores reales <code>\\(...\\)</code>, <code>\\[...\\]</code> y <code>$...$</code>.</p>'
        '<h3>Controles automáticos</h3><ul><li>Archivos requeridos presentes.</li>'
        '<li>Dataset O₃ conserva 24 filas; GPT NOx conserva 15 filas.</li>'
        '<li>Columnas obligatorias NOx presentes.</li><li>MathML presente.</li><li>Anclas internas resueltas.</li>'
        '<li>Nota documental APOA-370 presente.</li><li>Sin atributos <code>src</code> o <code>href</code> externos.</li></ul>'
    )
    reproducibility = section("reproducibilidad", "Apéndice de reproducibilidad", reproducibility_body)

    guiones_nav = [(f"guion-{module_id}", title) for module_id, title, _ in MODULES]
    guiones_nav.extend((f"guion-{page_id}", page_label(path)) for _, page_id, path in PAGES)
    practica_nav = [(f"practica-{practice_id}", title) for practice_id, title, _ in PRACTICE]
    subnav_map = {
        "diseno-curso": design_headings,
        "handout": handout_headings,
        "guiones": guiones_nav,
        "practica": practica_nav,
        "materiales": MATERIALS,
        "solucionarios": solutions_nav,
    }
    nav_li_parts = []
    for sid, label in SECTIONS:
        subs = subnav_map.get(sid)
        if subs:
            sub_lis = "".join(
                f'<li><a href="#{sub_id}">{html.escape(sub_label)}</a></li>' for sub_id, sub_label in subs
            )
            nav_li_parts.append(
                f'<li><details><summary><a href="#{sid}">{html.escape(label)}</a></summary>'
                f'<ul class="sub">{sub_lis}</ul></details></li>'
            )
        else:
            nav_li_parts.append(f'<li><a href="#{sid}">{html.escape(label)}</a></li>')
    sidebar_nav_items = "".join(nav_li_parts)
    nav = f'<nav class="sidebar" aria-label="Navegación principal"><strong>Paquete completo</strong><ul>{sidebar_nav_items}</ul></nav>'

    body = portada + design + handout + modules + practice + materials + solutions + reproducibility
    document = (
        '<!DOCTYPE html>\n<html lang="es"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        f'<title>{html.escape(TITLE)}</title><style>{CSS}</style></head><body>{nav}<main>{body}'
        '<footer>Paquete autocontenido generado por <code>cursov2/build_paquete_html.py</code>.</footer>'
        '</main></body></html>\n'
    )
    return document, dataset_rows, nox_gpt_rows, nox_line_rows, len(SECTIONS)


def csv_columns(path: Path) -> set[str]:
    with path.open(newline="", encoding="utf-8-sig") as stream:
        reader = csv.reader(stream)
        return set(next(reader, []))


def validate(document: str, dataset_rows: int, nox_gpt_rows: int, nox_line_rows: int) -> None:
    if dataset_rows != 24:
        raise ValueError(f"Dataset O₃ debe tener 24 filas; tiene {dataset_rows}")
    if nox_gpt_rows != 15:
        raise ValueError(f"Dataset GPT NOx debe tener 15 filas; tiene {nox_gpt_rows}")
    if nox_line_rows < 2:
        raise ValueError(f"Dataset línea NOx debe tener al menos 2 filas; tiene {nox_line_rows}")
    required_gpt = {
        "ciclo", "nivel", "timestamp", "no_cilindro_umol_mol", "u_no_cilindro_umol_mol",
        "flujo_no_ml_min", "flujo_dilucion_l_min", "flujo_o3_l_min", "temperatura_K",
        "presion_kPa", "no_generado_nmol_mol", "no2_gpt_nmol_mol", "lectura_no_nmol_mol",
        "lectura_nox_nmol_mol", "lectura_no2_nmol_mol", "temperatura_convertidor_C",
        "presion_camara_kPa", "caudal_muestra_l_min", "observacion",
    }
    required_line = {
        "configuracion", "longitud_m", "diametro_interno_mm", "volumen_interno_ml",
        "caudal_l_min", "tiempo_residencia_externo_s", "tiempo_residencia_interno_s",
        "tiempo_residencia_total_s", "temperatura_C", "no_entrada_nmol_mol",
        "o3_entrada_nmol_mol", "no2_entrada_nmol_mol", "no2_formado_estimado_nmol_mol",
        "cambio_relativo_pct", "criterio_pct", "decision_esperada",
    }
    missing_gpt = sorted(required_gpt - csv_columns(NOX_GPT_CSV))
    missing_line = sorted(required_line - csv_columns(NOX_LINE_CSV))
    if missing_gpt:
        raise ValueError("Faltan columnas GPT NOx: " + ", ".join(missing_gpt))
    if missing_line:
        raise ValueError("Faltan columnas línea NOx: " + ", ".join(missing_line))
    if "<math" not in document or "</math>" not in document:
        raise ValueError("No se encontró MathML; revise formato pandoc y delimitadores matemáticos")
    if not re.search(r'<math[^>]*>.*?<mi[^>]*>x</mi>', document, flags=re.DOTALL):
        raise ValueError("Prueba MathML falló: fórmula real con x no fue convertida")
    ids = set(re.findall(r'\bid="([^"]+)"', document))
    hrefs = re.findall(r'\bhref="([^"]+)"', document)
    missing = sorted({href[1:] for href in hrefs if href.startswith("#") and href[1:] not in ids})
    if missing:
        raise ValueError("Anclas internas inexistentes: " + ", ".join(missing))
    external_attributes = re.findall(
        r'\b(?:src|href)\s*=\s*["\']\s*(?:https?:)?//[^"\']+["\']', document, flags=re.IGNORECASE
    )
    if external_attributes:
        raise ValueError("Referencias externas encontradas: " + "; ".join(external_attributes[:5]))
    if not re.search(r'<img\s+src="data:image/png;base64,', document):
        raise ValueError("PNG MCM no quedó embebido como data URI")
    for section_id, _ in SECTIONS:
        if f'id="{section_id}"' not in document:
            raise ValueError(f"Falta sección requerida: {section_id}")
    for module_id, title, _ in MODULES:
        if f'id="guion-{module_id}"' not in document:
            raise ValueError(f"Falta guion {title}")
    for _, page_id, path in PAGES:
        if f'id="guion-{page_id}"' not in document:
            raise ValueError(f"Falta página {path.name}")
    for practice_id, title, _ in PRACTICE:
        if f'id="practica-{practice_id}"' not in document:
            raise ValueError(f"Falta práctica {title}")
    if 'id="guion-m8"' not in document:
        raise ValueError("Falta ancla guion-m8")
    apoa_context = re.search(r"APOA-370.{0,300}(?:O₃|ozono|descartad)", strip_tags(document), flags=re.IGNORECASE | re.DOTALL)
    if not apoa_context:
        raise ValueError("Falta nota que identifica APOA-370 como equipo O₃ o fuente descartada para NOx")
    solution_detail_count = len(re.findall(r'<details id="sol-', document))
    if solution_detail_count != len(SOLUTIONS):
        raise ValueError("Conteo inesperado de solucionarios colapsados")
    if "Solo instructor" not in document:
        raise ValueError("Falta aviso de solo instructor")


def main() -> int:
    try:
        document, dataset_rows, nox_gpt_rows, nox_line_rows, section_count = build()
        validate(document, dataset_rows, nox_gpt_rows, nox_line_rows)
        OUTPUT.write_text(document, encoding="utf-8")
    except (FileNotFoundError, RuntimeError, ValueError, subprocess.CalledProcessError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        if isinstance(error, subprocess.CalledProcessError) and error.stderr:
            print(error.stderr.strip(), file=sys.stderr)
        return 1
    size = OUTPUT.stat().st_size
    print(f"Generado: {OUTPUT}")
    print(f"Tamaño: {size:,} bytes ({size / 1024 / 1024:.2f} MiB)")
    print(f"Secciones principales: {section_count}")
    print(f"Filas dataset O₃: {dataset_rows}")
    print(f"Filas GPT NOx: {nox_gpt_rows}")
    print(f"Filas línea NOx: {nox_line_rows}")
    print(f"Solucionarios: {len(SOLUTIONS)}")
    print("Validaciones: datasets NOx, MathML, anclas, APOA-370, secciones, data URI y referencias externas OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
