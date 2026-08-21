#!/usr/bin/env python3
"""Genera el formulario CS-07 sobre la plantilla institucional F-PSEA-01."""

from __future__ import annotations

import subprocess
import time
from pathlib import Path

import uno
from com.sun.star.beans import PropertyValue

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "docs/qms/01_bloque_general/00_plantillas_base/F-PSEA-01 Plantilla Formato_Excel.xlsx"
OUT = ROOT / "servicio_comercial/03_ventas_contratacion/CS-07_formulario_inscripcion.xlsx"

NAVY = 0xD9EAF7
BLUE = 0xD9EAF7
INPUT = 0xFFF2CC
WHITE = 0x000000
GRAY = 0xE7E6E6
START = 5  # fila 6


def prop(name, value):
    p = PropertyValue()
    p.Name, p.Value = name, value
    return p


def connect():
    local = uno.getComponentContext()
    resolver = local.ServiceManager.createInstanceWithContext(
        "com.sun.star.bridge.UnoUrlResolver", local
    )
    url = "uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext"
    try:
        return resolver.resolve(url)
    except Exception:
        subprocess.Popen(
            [
                "libreoffice", "--headless",
                "--accept=socket,host=localhost,port=2002;urp;StarOffice.ServiceManager",
                "--norestore", "--nodefault", "--nofirststartwizard",
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        for _ in range(40):
            time.sleep(0.25)
            try:
                return resolver.resolve(url)
            except Exception:
                pass
        raise RuntimeError("No se pudo iniciar LibreOffice")


def merge_text(sheet, row, text, color=NAVY, font=WHITE, height=700):
    area = sheet.getCellRangeByPosition(0, row, 3, row)
    area.merge(True)
    cell = sheet.getCellByPosition(0, row)
    cell.String = text
    cell.CellBackColor = color
    cell.CharColor = font
    cell.CharWeight = 150
    cell.IsTextWrapped = True
    sheet.Rows.getByIndex(row).Height = height


def field(sheet, row, label, note="", height=650):
    label_cell = sheet.getCellByPosition(0, row)
    label_cell.String = label
    label_cell.CellBackColor = BLUE
    label_cell.CharWeight = 150
    label_cell.IsTextWrapped = True
    entry = sheet.getCellRangeByPosition(1, row, 2, row)
    entry.merge(True)
    sheet.getCellByPosition(1, row).CellBackColor = INPUT
    note_cell = sheet.getCellByPosition(3, row)
    note_cell.String = note
    note_cell.CharColor = 0x666666
    note_cell.IsTextWrapped = True
    sheet.Rows.getByIndex(row).Height = height


def option(sheet, row, text):
    area = sheet.getCellRangeByPosition(0, row, 3, row)
    area.merge(True)
    c = sheet.getCellByPosition(0, row)
    c.String = "☐ " + text
    c.CellBackColor = INPUT
    c.IsTextWrapped = True
    sheet.Rows.getByIndex(row).Height = 560


def build(sheet):
    sheet.getCellRangeByName("A6:Z300").clearContents(1023)
    sheet.getCellRangeByName("B3").String = "CS-07 — FORMULARIO DE INSCRIPCIÓN AL SERVICIO"
    widths = [5200, 5200, 5200, 5200]
    for i, width in enumerate(widths):
        sheet.Columns.getByIndex(i).Width = width

    r = START
    merge_text(sheet, r, "FORMULARIO DE INSCRIPCIÓN — ENSAYOS DE APTITUD PARA GASES CONTAMINANTES CRITERIO")
    r += 1
    merge_text(sheet, r, "Complete las celdas amarillas. Los datos técnicos de equipos se registran en F-PSEA-04.", GRAY, 0x000000, 620)

    sections = [
        ("1. IDENTIFICACIÓN DE LA INSCRIPCIÓN", [
            ("Código o nombre de la ronda", "Según la convocatoria vigente"),
            ("Número de cotización", "Cotización vigente asociada"),
            ("Número de orden de compra", "Si aplica"),
            ("Fecha de inscripción", "AAAA-MM-DD"),
        ]),
        ("2. DATOS DE LA ORGANIZACIÓN", [
            ("Razón social", "Nombre legal completo"),
            ("NIT / identificación tributaria", "Incluya dígito de verificación"),
            ("Dirección", ""),
            ("Ciudad y país", ""),
            ("Sitio web", "Opcional"),
        ]),
        ("3. CONTACTO CONTRACTUAL AUTORIZADO", [
            ("Nombre completo", ""),
            ("Cargo", ""),
            ("Correo electrónico", ""),
            ("Teléfono", "Incluya indicativo"),
        ]),
        ("4. CONTACTO TÉCNICO AUTORIZADO", [
            ("Nombre completo", ""),
            ("Cargo", ""),
            ("Correo electrónico", ""),
            ("Teléfono", "Incluya indicativo"),
        ]),
        ("5. DATOS DE FACTURACIÓN", [
            ("Dirección de facturación", ""),
            ("Nombre del contacto", ""),
            ("Correo para facturación", ""),
            ("Teléfono", ""),
            ("Portal o requisitos especiales", "Si aplica"),
            ("Documentos anexos", "Relacione los documentos enviados"),
        ]),
    ]
    for title, fields in sections:
        r += 1
        merge_text(sheet, r, title)
        for label, note in fields:
            r += 1
            field(sheet, r, label, note)

    r += 1
    merge_text(sheet, r, "6. ALCANCE SOLICITADO")
    for text in (
        "Monóxido de carbono (CO)",
        "Dióxido de azufre (SO₂)",
        "Óxidos de nitrógeno (NO/NO₂)",
        "Ozono (O₃)",
    ):
        r += 1
        option(sheet, r, text)
    r += 1
    field(sheet, r, "Cantidad total de analizadores", "Detalle los equipos en F-PSEA-04")
    r += 1
    field(sheet, r, "Idioma solicitado para el informe", "Español / otro acordado")

    r += 1
    merge_text(sheet, r, "7. CONFIDENCIALIDAD Y DIVULGACIÓN")
    for text in (
        "Solicito que la identidad de la organización y sus resultados se mantengan confidenciales.",
        "Autorizo la divulgación exigida por una autoridad competente, previa notificación cuando sea legalmente posible.",
        "Autorizo el uso del nombre de la organización con fines de divulgación institucional.",
        "No autorizo usos de divulgación adicionales a los exigidos legalmente.",
    ):
        r += 1
        option(sheet, r, text)

    r += 1
    merge_text(sheet, r, "8. TRATAMIENTO DE DATOS Y COMUNICACIONES")
    r += 1
    option(sheet, r, "Autorizo el tratamiento de los datos suministrados para gestionar la inscripción, prestación y seguimiento del servicio, conforme a la Ley 1581 de 2012 y la política institucional aplicable.")
    r += 1
    option(sheet, r, "Autorizo recibir información sobre futuras rondas y servicios relacionados. Esta autorización es opcional e independiente de la inscripción.")

    r += 1
    merge_text(sheet, r, "9. ACEPTACIÓN")
    r += 1
    option(sheet, r, "Declaro que la información suministrada es veraz y que conozco y acepto los términos y condiciones aplicables al servicio y a la cotización relacionada.")
    for label, note in (
        ("Nombre de quien acepta", "Representante o contacto autorizado"),
        ("Cargo", ""),
        ("Firma", "Firma manuscrita o electrónica"),
        ("Fecha de aceptación", "AAAA-MM-DD"),
        ("Canal de aceptación", "Portal / correo / PDF firmado / papel"),
        ("Marca de tiempo", "AAAA-MM-DDThh:mm:ss±hh:mm"),
        ("Origen IP", "Solo cuando la aceptación se realice en portal"),
    ):
        r += 1
        field(sheet, r, label, note)

    r += 1
    merge_text(sheet, r, "10. USO INTERNO DE CALAIRE-EA")
    for label, note in (
        ("Código de participante", "Asignado por CALAIRE-EA"),
        ("Inscripción verificada por", "Nombre y fecha"),
        ("Revisión de contrato CS-09", "Número o referencia"),
        ("Estado de la inscripción", "Inscrito / en revisión / confirmado / lista de espera / rechazado / retirado"),
        ("Observaciones", ""),
    ):
        r += 1
        field(sheet, r, label, note, 900 if label == "Observaciones" else 650)

    used = sheet.getCellRangeByPosition(0, START, 3, r)
    used.TableBorder = used.TableBorder
    sheet.getCellRangeByPosition(0, START, 3, r).IsTextWrapped = True
    sheet.createCursor().gotoEndOfUsedArea(True)


def enforce_contrast(sheet):
    """Normaliza el formulario a presentación monocromática."""
    cursor = sheet.createCursor()
    cursor.gotoEndOfUsedArea(True)
    end = cursor.RangeAddress
    for row in range(end.StartRow, end.EndRow + 1):
        for col in range(end.StartColumn, end.EndColumn + 1):
            cell = sheet.getCellByPosition(col, row)
            cell.CellBackColor = 0xFFFFFF
            cell.CharColor = 0x000000


def main():
    ctx = connect()
    desktop = ctx.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
    doc = desktop.loadComponentFromURL(TEMPLATE.as_uri(), "_blank", 0, (prop("Hidden", True),))
    sheets = doc.Sheets
    sheet = sheets.getByIndex(0)
    sheet.Name = "Formulario CS-07"
    for i in range(sheets.Count - 1, 0, -1):
        sheets.removeByName(sheets.getByIndex(i).Name)
    build(sheet)
    enforce_contrast(sheet)
    doc.storeAsURL(OUT.as_uri(), (prop("FilterName", "Calc MS Excel 2007 XML"), prop("Overwrite", True)))
    doc.close(True)
    print(OUT)


if __name__ == "__main__":
    main()
