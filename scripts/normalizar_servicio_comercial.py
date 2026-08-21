#!/usr/bin/env python3
"""Normalización editorial de artefactos servicio_comercial.

- Unifica placeholders [RELLENO]/[LLENAR]/[FECHA POR COMPLETAR] en [POR DILIGENCIAR].
- Corrige artefactos de traducción automática (redonda, coste, restos en inglés).
- Convierte el encabezado de líneas en negrita a tabla de control de documento (estilo SOP).
"""
import re
import sys
from pathlib import Path

BASE = Path("/home/w182/w421/calaire-ea/servicio_comercial")

FILES = sorted(
    p for d in ("00_control", "01_mercado", "02_precios_restringidos",
                "03_ventas_contratacion", "04_inscripcion_restringida",
                "05_cambios_finanzas", "06_entrega_retencion")
    for p in (BASE / d).glob("*.md")
) + [BASE / "README.md"]

LITERAL = [
    # restos en inglés
    ("Gases offered", "Gases ofrecidos"),
    ("[LIST]", "[LISTA]"),
    ("[PRE-ACCREDITATION STATEMENT]", "[DECLARACIÓN DE PREACREDITACIÓN]"),
    ("Wait-list priority criteria", "Criterios de prioridad de la lista de espera"),
    ("**Wait-list priority**", "**Prioridad en lista de espera**"),
    # "round" mal traducido como "redonda"
    ("Identificación redonda", "Identificación de la ronda"),
    ("Asignación redonda", "Asignación por ronda"),
    ("asignación redonda", "asignación por ronda"),
    ("Fórmula de asignación redonda", "Fórmula de asignación por ronda"),
    ("cuotas redondas", "cuotas por ronda"),
    ("Planificación redonda", "Planificación de ronda"),
    ("Línea de tiempo redonda", "Cronograma de la ronda"),
    ("ejecución redonda", "ejecución de la ronda"),
    ("planificación circular existente", "planificación de rondas existente"),
    ("revisiones de costos, asuntos legales y cilindros",
     "las revisiones de costos, jurídica y de cilindros"),
    # castellano de España / calcos
    ("costes", "costos"),
    ("coste", "costo"),
    ("Sólo", "Solo"),
    ("sólo", "solo"),
    ("participante\norganización", "organización participante"),
    ("Convierta el servicio genérico en una ronda programada adquirible.",
     "Convertir el servicio genérico en una ronda programada y adquirible."),
    # mayúscula tras punto y coma
    ("; Los costos comerciales", "; los costos comerciales"),
    ("; Esta tabla es una ayuda", "; esta tabla es una ayuda"),
    ("; El contenido puede cambiar.", "; el contenido puede cambiar."),
    ("; Las puertas de liberación", "; las puertas de liberación"),
    ("; No hay precio aprobado.", "; no hay precio aprobado."),
    ("; Se puede aceptar", "; se puede aceptar"),
]

REGEX = [
    # placeholders → [POR DILIGENCIAR]
    (re.compile(r"\[RELLENO\s*[—:-]\s*([^\]]+)\]"), r"[POR DILIGENCIAR — \1]"),
    (re.compile(r"\[RELLENO\]"), "[POR DILIGENCIAR]"),
    (re.compile(r"`\[RELLENO\]`"), "`[POR DILIGENCIAR]`"),
    (re.compile(r"\[LLENAR NOMBRE, FECHA, FIRMA\]", re.I),
     "[POR DILIGENCIAR — nombre, fecha y firma]"),
    (re.compile(r"\[FECHA POR COMPLETAR\]"), "[POR DILIGENCIAR — fecha]"),
]

HEADER_KEYS = re.compile(r"^\*\*([^*]+):\*\*\s*(.*)$")


def convertir_encabezado(lines, code):
    """Convierte bloque inicial **Clave:** valor en tabla de control de documento."""
    if not lines or not lines[0].startswith("# "):
        return lines
    i = 1
    while i < len(lines) and not lines[i].strip():
        i += 1
    rows, j = [], i
    while j < len(lines):
        m = HEADER_KEYS.match(lines[j])
        if not m:
            break
        rows.append((m.group(1).strip(), m.group(2).strip()))
        j += 1
    if not rows:
        return lines
    table = ["", "| Control del documento | |", "|---|---|"]
    if code:
        table.append(f"| **Código** | {code} |")
    for k, v in rows:
        table.append(f"| **{k}** | {v} |")
    table.append("")
    return lines[:1] + table + lines[j:]


def main():
    for path in FILES:
        text = path.read_text(encoding="utf-8")
        orig = text
        for a, b in LITERAL:
            text = text.replace(a, b)
        for rx, rep in REGEX:
            text = rx.sub(rep, text)
        m = re.match(r"CS-\d{2}", path.name)
        lines = text.split("\n")
        lines = convertir_encabezado(lines, m.group(0) if m else None)
        text = "\n".join(lines)
        if text != orig:
            path.write_text(text, encoding="utf-8")
            print(f"editado: {path.relative_to(BASE)}")


if __name__ == "__main__":
    sys.exit(main())
