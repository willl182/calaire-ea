#!/usr/bin/env python3
"""Genera páginas desde módulos intactos o valida el índice ya materializado."""

from __future__ import annotations

import re
import unicodedata
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PAGES_DIR = BASE_DIR / "paginas"

MODULES = {
    "M1": BASE_DIR / "modulos/M1_trazabilidad.md",
    "M2": BASE_DIR / "modulos/M2_modelo_medicion.md",
    "M3": BASE_DIR / "modulos/M3_conceptos_gum.md",
    "M4": BASE_DIR / "modulos/M4_presupuesto_analizador.md",
    "M5": BASE_DIR / "modulos/M5_patrones_transferencia.md",
    "M6": BASE_DIR / "modulos/M6_no_nox_quimioluminiscencia.md",
    "M7": BASE_DIR / "modulos/M7_taller.md",
    "M8": BASE_DIR / "modulos/M8_opcional_monte_carlo.md",
}

HEADING_PAGES = {
    "M1": ["3.1", "3.2", "3.3", "3.4", "3.5"],
    "M2": ["3.1", "3.2", "3.3", "3.4"],
    "M3": ["3.1", "3.2", "3.3", "3.4"],
    "M4": ["3.0", "3.1", "3.2", "3.3", "3.4"],
    "M6": ["3.1", "3.2", "3.3", "3.4"],
    "M7": ["Bloque 1", "Bloque 2", "Bloque 3", "Bloque 4", "Bloque 5", "Bloque 6"],
}

BLOCK_PAGES = {
    "M5": [
        "Bloque 0–8 min",
        "Bloque 8–18 min",
        "Bloque 18–28 min",
        "Bloque 28–38 min",
        "Bloque 60–68 min",
    ],
    "M8": [
        "0:00–0:03",
        "0:03–0:08",
        "0:08–0:13",
        "0:13–0:23",
        "0:23–0:26",
        "0:26–0:30",
    ],
}


def slug(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    value = re.sub(r"[^a-zA-Z0-9]+", "_", value).strip("_").lower()
    return value


def find_heading(text: str, marker: str) -> tuple[int, str]:
    pattern = re.compile(rf"^###\s+{re.escape(marker)}(?:\s+.*)?\s*$", re.MULTILINE)
    match = pattern.search(text)
    if not match:
        raise ValueError(f"No se encontró página {marker}")
    return match.start(), match.group(0).strip()[4:].strip()


def extract_heading_page(text: str, marker: str) -> tuple[str, str]:
    start, title = find_heading(text, marker)
    body_start = text.find("\n", start) + 1
    end_match = re.search(r"^###\s+|^##\s+", text[body_start:], re.MULTILINE)
    end = body_start + end_match.start() if end_match else len(text)
    body = text[start:end].strip()
    return title, body


def extract_block_page(text: str, marker: str) -> tuple[str, str]:
    start_match = re.search(rf"^\*\*{re.escape(marker)}[^*]*\*\*\s*$", text, re.MULTILINE)
    if not start_match:
        raise ValueError(f"No se encontró bloque {marker}")
    title = start_match.group(0).strip()[2:-2].strip()
    end_match = re.search(r"^\*\*(?:Bloque|0:|0\:)[^*]*\*\*\s*$|^##\s+", text[start_match.end() :], re.MULTILINE)
    end = start_match.end() + end_match.start() if end_match else len(text)
    body = text[start_match.start() : end].strip()
    return title, body


def write_page(module: str, number: int, title: str, body: str, source: Path) -> Path:
    filename = f"{module}_{number:02d}_{slug(title)}.md"
    path = PAGES_DIR / filename
    content = (
        f"# {module} — Página {number:02d} — {title}\n\n"
        f"- **Sesión:** {module}\n"
        f"- **Fuente:** [`{source.relative_to(BASE_DIR).as_posix()}`](../{source.relative_to(BASE_DIR).as_posix()})\n"
        "- **Tipo:** página/diapositiva del libreto\n\n"
        "## Libreto\n\n"
        f"{body}\n"
    )
    path.write_text(content, encoding="utf-8")
    return path


def indexed_pages(module: str, source: Path) -> list[Path]:
    text = source.read_text(encoding="utf-8")
    filenames = re.findall(r"\]\(\.\./paginas/([^\)]+\.md)\)", text)
    if not filenames:
        return []
    paths = [PAGES_DIR / filename for filename in filenames]
    if len(paths) != len(set(paths)):
        raise ValueError(f"Páginas duplicadas en el índice de {module}")
    for path in paths:
        if not path.is_file():
            raise FileNotFoundError(f"Página indexada inexistente: {path}")
        content = path.read_text(encoding="utf-8")
        if "## Libreto" not in content:
            raise ValueError(f"Página sin sección Libreto: {path}")
    return paths


def main() -> None:
    generated = []
    for module, source in MODULES.items():
        indexed = indexed_pages(module, source)
        if indexed:
            generated.extend(indexed)
            continue
        text = source.read_text(encoding="utf-8")
        markers = HEADING_PAGES.get(module)
        if markers:
            pages = [extract_heading_page(text, marker) for marker in markers]
        else:
            pages = [extract_block_page(text, marker) for marker in BLOCK_PAGES[module]]
        for number, (title, body) in enumerate(pages, start=1):
            generated.append(write_page(module, number, title, body, source))
    print(f"Páginas verificadas/generadas: {len(generated)}")
    for path in generated:
        print(path.relative_to(BASE_DIR))


if __name__ == "__main__":
    main()
