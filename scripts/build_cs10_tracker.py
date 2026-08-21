#!/usr/bin/env python3
"""Build the protected CS-10 enrollment tracker with LibreOffice UNO.

Run from the repository root. The generated workbooks contain no real data.
"""

from __future__ import annotations

import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

import uno
from com.sun.star.beans import PropertyValue


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "servicio_comercial" / "04_inscripcion_restringida"
TEMPLATE = OUT / "CS-10_seguimiento_inscripciones_ingresos.xlsx"
SYNTHETIC = OUT / "CS-10_simulacion_sintetica.xlsx"
PASSWORD = "CAMBIAR-CS10"
ROWS = 200

NAVY = 0x17365D
BLUE = 0xD9EAF7
LIGHT = 0xF3F6F9
GREEN = 0xC6EFCE
AMBER = 0xFFEB9C
RED = 0xFFC7CE
WHITE = 0xFFFFFF
GRAY = 0x666666
VALIDATION_LIST = 6
JUSTIFY_CENTER = 2


def prop(name, value):
    p = PropertyValue()
    p.Name, p.Value = name, value
    return p


def connect():
    local = uno.getComponentContext()
    resolver = local.ServiceManager.createInstanceWithContext(
        "com.sun.star.bridge.UnoUrlResolver", local
    )
    try:
        return resolver.resolve(
            "uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext"
        )
    except Exception:
        subprocess.Popen(
            [
                "libreoffice", "--headless", "--accept=socket,host=localhost,port=2002;urp;StarOffice.ServiceManager",
                "--norestore", "--nodefault", "--nofirststartwizard",
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        for _ in range(40):
            time.sleep(0.25)
            try:
                return resolver.resolve(
                    "uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext"
                )
            except Exception:
                pass
        raise RuntimeError("Could not start LibreOffice UNO listener")


def set_text(sheet, col, row, value):
    sheet.getCellByPosition(col, row).String = str(value)


def set_formula(sheet, col, row, formula):
    sheet.getCellByPosition(col, row).Formula = formula


def style_title(sheet, address):
    r = sheet.getCellRangeByName(address)
    r.CellBackColor = NAVY
    r.CharColor = WHITE
    r.CharWeight = 150
    r.CharHeight = 14


def style_header(sheet, address):
    r = sheet.getCellRangeByName(address)
    r.CellBackColor = NAVY
    r.CharColor = WHITE
    r.CharWeight = 150
    r.IsTextWrapped = True
    r.HoriJustify = JUSTIFY_CENTER


def list_validation(doc, sheet, address, values):
    target = sheet.getCellRangeByName(address)
    v = target.Validation
    v.Type = VALIDATION_LIST
    v.ShowErrorMessage = True
    v.ErrorTitle = "Valor no permitido"
    v.ErrorMessage = "Seleccione un valor de la lista controlada."
    v.ShowList = 1
    v.Formula1 = '"' + ";".join(values) + '"'
    target.Validation = v


def unlock(sheet, address):
    r = sheet.getCellRangeByName(address)
    p = r.CellProtection
    p.IsLocked = False
    r.CellProtection = p


def build_book(ctx, synthetic=False):
    smgr = ctx.ServiceManager
    desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
    doc = desktop.loadComponentFromURL("private:factory/scalc", "_blank", 0, ())
    sheets = doc.Sheets
    sheets.getByIndex(0).Name = "LEAME"
    for name in ["Tracker", "Pipeline", "Enrollment", "Viability", "Receivables", "Exceptions", "Lists"]:
        sheets.insertNewByName(name, sheets.Count)

    readme = sheets.getByName("LEAME")
    readme.getCellRangeByName("A1:H1").merge(True)
    set_text(readme, 0, 0, "CS-10 — Seguimiento de inscripciones e ingresos")
    style_title(readme, "A1:H1")
    notes = [
        ("Clasificación", "RESTRINGIDO — identidad, datos comerciales y pagos"),
        ("Versión", "0.3 — plantilla operativa"),
        ("Propietario", "Coordinación de ronda"),
        ("Uso", "Registrar una fila por organización/ronda. No almacenar resultados técnicos."),
        ("Confirmación", "Solo procede con CS-09 aprobado y pago u orden aceptada."),
        ("Capacidad", "Individual: máximo 4 analizadores por bloque. CO/SO₂ simultáneo: máximo 3 organizaciones y 6 analizadores."),
        ("Comunicaciones", "Solo cala​​ire_med@unal.edu.co o carpeta institucional controlada.".replace("​​", "")),
        ("Protección", f"Clave inicial: {PASSWORD}. Debe cambiarla la coordinación antes del uso real. La protección de hoja no sustituye el control de acceso institucional."),
        ("Retención", "5 años, conforme al control documental aplicable."),
    ]
    for i, (a, b) in enumerate(notes, 2):
        set_text(readme, 0, i, a)
        set_text(readme, 1, i, b)
        readme.getCellByPosition(0, i).CharWeight = 150
    readme.Columns.getByIndex(0).Width = 4500
    readme.Columns.getByIndex(1).Width = 22000
    readme.getCellRangeByName("A1:H14").IsTextWrapped = True

    headers = [
        "ID del cliente potencial/cliente", "Organización", "País", "Idioma preferido", "ID de ronda",
        "Analizadores de CO", "Analizadores de SO₂", "Analizadores de O₃", "Analizadores de NO/NO₂", "Cantidad de analizadores",
        "Número de cotización", "Revisión de cotización", "Valor cotizado (COP)", "Valor comprometido actual (COP)",
        "Vencimiento de cotización", "Fecha límite de aceptación", "Fecha límite de pago/orden de compra", "Fecha de inscripción",
        "Fecha y hora de aceptación", "Canal de aceptación", "Laboratorio acreditado", "Elegibilidad completa",
        "Estado de revisión del contrato", "Fecha de revisión del contrato", "Revisor del contrato",
        "Estado de orden/pago/factura", "Valor recibido (COP)", "Saldo pendiente (COP)", "% pagado",
        "Vencimiento de próxima cuota", "Número de factura", "Código de participante", "Configuración operativa",
        "Estado comercial", "Grupo de lista de espera", "Fecha y hora de lista de espera", "Posición en lista de espera",
        "Último cupo disponible", "Alerta de capacidad", "Alerta de pago", "Estado de cancelación/reembolso",
        "Fecha de cancelación", "Referencia de reembolso/nota crédito", "Exposición cambiaria", "Responsable", "Próxima acción",
        "Enlace/ubicación de comunicación", "Fecha de expresión de interés", "Vencimiento de expresión de interés", "Indicador de interés obsoleto",
        "Consentimiento de mercadeo", "Referencia CS-09", "Referencia CS-12", "Notas",
    ]
    tr = sheets.getByName("Tracker")
    for c, h in enumerate(headers):
        set_text(tr, c, 0, h)
        tr.Columns.getByIndex(c).Width = 3500 if c not in (1, 45, 46, 53) else 6000
    style_header(tr, f"A1:{col(len(headers)-1)}1")
    tr.Rows.getByIndex(0).Height = 1800
    tr.getCellRangeByName(f"A2:{col(len(headers)-1)}{ROWS+1}").CellBackColor = WHITE

    # Row formulas. COUNTIFS count only Confirmed records, enforcing commercial capacity.
    for r in range(2, ROWS + 2):
        set_formula(tr, 9, r-1, f"=SUM(F{r}:I{r})")
        set_formula(tr, 27, r-1, f'=IF(N{r}="";"";MAX(0;N{r}-AA{r}))')
        set_formula(tr, 28, r-1, f'=IF(N{r}="";"";IF(N{r}=0;0;AA{r}/N{r}))')
        set_formula(tr, 34, r-1, f'=IF(A{r}="";"";IF(V{r}="Yes";IF(U{r}="Yes";1;2);""))')
        set_formula(tr, 36, r-1, f'=IF(A{r}="";"";IF(AJ{r}="";"";COUNTIFS($E$2:$E$201;E{r};$AI$2:$AI$201;AI{r};$AJ$2:$AJ$201;"<="&AJ{r})))')
        set_formula(tr, 37, r-1, f'=IF(A{r}="";"";IF(AI{r}<>"Confirmed";"No";IF(AG{r}="Simultaneous CO/SO₂";IF(OR(COUNTIFS($E$2:$E$201;E{r};$AI$2:$AI$201;"Confirmed";$AG$2:$AG$201;"Simultaneous CO/SO₂")=3;SUMIFS($J$2:$J$201;$E$2:$E$201;E{r};$AI$2:$AI$201;"Confirmed";$AG$2:$AG$201;"Simultaneous CO/SO₂")=6);"Yes";"No");IF(OR(AND(F{r}>0;SUMIFS($F$2:$F$201;$E$2:$E$201;E{r};$AI$2:$AI$201;"Confirmed")=4);AND(G{r}>0;SUMIFS($G$2:$G$201;$E$2:$E$201;E{r};$AI$2:$AI$201;"Confirmed")=4);AND(H{r}>0;SUMIFS($H$2:$H$201;$E$2:$E$201;E{r};$AI$2:$AI$201;"Confirmed")=4);AND(I{r}>0;SUMIFS($I$2:$I$201;$E$2:$E$201;E{r};$AI$2:$AI$201;"Confirmed")=4));"Yes";"No"))))')
        set_formula(tr, 38, r-1, f'=IF(A{r}="";"";IF(AI{r}<>"Confirmed";"";IF(AG{r}="Simultaneous CO/SO₂";IF(OR(COUNTIFS($E$2:$E$201;E{r};$AI$2:$AI$201;"Confirmed";$AG$2:$AG$201;"Simultaneous CO/SO₂")>3;SUMIFS($J$2:$J$201;$E$2:$E$201;E{r};$AI$2:$AI$201;"Confirmed";$AG$2:$AG$201;"Simultaneous CO/SO₂")>6);"OVER CAPACITY";"OK");IF(OR(SUMIFS($F$2:$F$201;$E$2:$E$201;E{r};$AI$2:$AI$201;"Confirmed")>4;SUMIFS($G$2:$G$201;$E$2:$E$201;E{r};$AI$2:$AI$201;"Confirmed")>4;SUMIFS($H$2:$H$201;$E$2:$E$201;E{r};$AI$2:$AI$201;"Confirmed")>4;SUMIFS($I$2:$I$201;$E$2:$E$201;E{r};$AI$2:$AI$201;"Confirmed")>4);"OVER CAPACITY";"OK"))))')
        set_formula(tr, 39, r-1, f'=IF(A{r}="";"";IF(AND(AC{r}<1;Q{r}<TODAY();AI{r}="Accepted pending payment/PO");"DEADLINE EXPIRED";IF(AND(AC{r}<1;AD{r}<>"";AD{r}<TODAY());"OVERDUE";"OK")))')
        set_text(tr, 43, r-1, "No aplica — solo COP")
        set_formula(tr, 48, r-1, f'=IF(AV{r}="";"";AV{r}+60)')
        set_formula(tr, 49, r-1, f'=IF(A{r}="";"";IF(AND(AV{r}<>"";AW{r}<TODAY();OR(AI{r}="Interest";AI{r}="Quoted"));"Yes";"No"))')
        # Commercial status is column AH; AI is the calculated wait-list group.
        for c in (37, 38, 39, 49):
            cell = tr.getCellByPosition(c, r-1)
            cell.Formula = cell.Formula.replace("$AI$2:$AI$201", "$AH$2:$AH$201").replace(f"AI{r}", f"AH{r}")
            for source, target in {
                "Confirmed": "Confirmado", "Simultaneous CO/SO₂": "CO/SO₂ simultáneos",
                "Accepted pending payment/PO": "Aceptado pendiente de pago/orden",
                "Interest": "Interés", "Quoted": "Cotizado", "Yes": "Sí",
                "OVER CAPACITY": "CAPACIDAD EXCEDIDA", "DEADLINE EXPIRED": "PLAZO VENCIDO",
                "OVERDUE": "VENCIDO",
            }.items():
                cell.Formula = cell.Formula.replace(source, target)

    # Formats and validation.
    for rng in ["O2:S201", "X2:X201", "AD2:AD201", "AJ2:AJ201", "AP2:AP201", "AW2:AX201"]:
        tr.getCellRangeByName(rng).NumberFormat = doc.NumberFormats.getStandardFormat(2, doc.CharLocale)
    tr.getCellRangeByName("M2:N201").NumberFormat = doc.NumberFormats.getStandardFormat(4, doc.CharLocale)
    tr.getCellRangeByName("AA2:AB201").NumberFormat = doc.NumberFormats.getStandardFormat(4, doc.CharLocale)
    tr.getCellRangeByName("AC2:AC201").NumberFormat = doc.NumberFormats.getStandardFormat(10, doc.CharLocale)
    list_validation(doc, tr, "D2:D201", ["Español"])
    list_validation(doc, tr, "T2:T201", ["Correo institucional", "Cotización firmada", "Orden de compra aceptada"])
    list_validation(doc, tr, "U2:V201", ["Sí", "No"])
    list_validation(doc, tr, "W2:W201", ["Pendiente", "Aprobada", "Rechazada"])
    list_validation(doc, tr, "Z2:Z201", ["Pendiente", "Parcial", "Recibido", "Facturado", "Pagado", "Vencido"])
    list_validation(doc, tr, "AG2:AG201", ["Gas individual", "CO/SO₂ simultáneos"])
    list_validation(doc, tr, "AH2:AH201", ["Interés", "Cotizado", "Inscrito", "En revisión", "Revisión de cotización en curso", "Aceptado pendiente de pago/orden", "Confirmado", "En lista de espera", "Rechazado", "Retirado"])
    list_validation(doc, tr, "AO2:AO201", ["", "Abierto", "Cancelado", "Reembolsado", "En disputa"])
    list_validation(doc, tr, "AY2:AY201", ["Sí", "No", "No solicitado"])
    # Input cells unlocked; formula/control cells remain locked.
    unlock(tr, "A2:I201")
    unlock(tr, "K2:Z201")
    unlock(tr, "AA2:AA201")
    unlock(tr, "AD2:AH201")
    unlock(tr, "AH2:AH201")
    unlock(tr, "AJ2:AJ201")
    unlock(tr, "AO2:AW201")
    unlock(tr, "AY2:BB201")
    unlock(tr, "BD2:BD201")
    tr.getCellRangeByName("AL2:AN201").CellBackColor = BLUE
    tr.getCellRangeByName("AM2:AM201").CellBackColor = AMBER
    tr.getCellRangeByName("AN2:AN201").CellBackColor = AMBER
    tr.getCellRangeByName("AX2:AX201").CellBackColor = BLUE
    tr.getCellRangeByName("A1:BD201").IsTextWrapped = True
    tr.getCellRangeByName("A1:BD201").createFilterDescriptor(True)
    tr.protect(PASSWORD)

    # Dashboards / required views.
    make_view(sheets.getByName("Pipeline"), "Flujo de oportunidades", "Interés hasta cotización; excluye intereses obsoletos.", [
        ("Intereses activos", '=COUNTIFS(Tracker.AH2:AH201;"Interés";Tracker.AX2:AX201;"No")'),
        ("Cotizaciones activas", '=COUNTIFS(Tracker.AH2:AH201;"Cotizado";Tracker.AX2:AX201;"No")'),
        ("Revisiones de cotización en curso", '=COUNTIF(Tracker.AH2:AH201;"Revisión de cotización en curso")'),
        ("Intereses obsoletos", '=COUNTIF(Tracker.AX2:AX201;"Sí")'),
    ])
    make_view(sheets.getByName("Enrollment"), "Inscripción", "Capacidad confirmada para la ronda indicada en B3.", [])
    en = sheets.getByName("Enrollment")
    set_text(en, 0, 2, "ID de ronda")
    unlock(en, "B3")
    for c, h in enumerate(["Indicador", "Confirmado", "Límite", "Residual", "Alerta"]): set_text(en, c, 4, h)
    style_header(en, "A5:E5")
    metrics = [("Analizadores de CO", "F", 4), ("Analizadores de SO₂", "G", 4), ("Analizadores de O₃", "H", 4), ("Analizadores de NO/NO₂", "I", 4)]
    for i, (label, letter, limit) in enumerate(metrics, 5):
        set_text(en, 0, i, label); set_formula(en, 1, i, f'=SUMIFS(Tracker.{letter}2:{letter}201;Tracker.E2:E201;$B$3;Tracker.AH2:AH201;"Confirmed")'); set_text(en, 2, i, limit); set_formula(en, 3, i, f'=C{i+1}-B{i+1}'); set_formula(en, 4, i, f'=IF(D{i+1}<0;"OVER CAPACITY";IF(D{i+1}=0;"LAST SLOT";"OK"))')
    set_text(en, 0, 10, "Organizaciones con CO/SO₂ simultáneos")
    set_formula(en, 1, 10, '=COUNTIFS(Tracker.E2:E201;$B$3;Tracker.AH2:AH201;"Confirmed";Tracker.AG2:AG201;"Simultaneous CO/SO₂")')
    set_text(en, 2, 10, 3); set_formula(en, 3, 10, "=C11-B11"); set_formula(en, 4, 10, '=IF(D11<0;"OVER CAPACITY";IF(D11=0;"LAST SLOT";"OK"))')
    set_text(en, 0, 11, "Analizadores de CO/SO₂ simultáneos")
    set_formula(en, 1, 11, '=SUMIFS(Tracker.J2:J201;Tracker.E2:E201;$B$3;Tracker.AH2:AH201;"Confirmed";Tracker.AG2:AG201;"Simultaneous CO/SO₂")')
    set_text(en, 2, 11, 6); set_formula(en, 3, 11, "=C12-B12"); set_formula(en, 4, 11, '=IF(D12<0;"OVER CAPACITY";IF(D12=0;"LAST SLOT";"OK"))')

    make_view(sheets.getByName("Viability"), "Viabilidad", "Ingresos confirmados frente al umbral. Indique la ronda y el umbral aprobado en CS-04.", [])
    vi = sheets.getByName("Viability")
    for row, (label, formula) in enumerate([
        ("ID de ronda", ""), ("Ingreso mínimo aprobado (COP)", ""),
        ("Organizaciones confirmadas", '=COUNTIFS(Tracker.E2:E201;B3;Tracker.AH2:AH201;"Confirmado")'),
        ("Ingreso comprometido confirmado (COP)", '=SUMIFS(Tracker.N2:N201;Tracker.E2:E201;B3;Tracker.AH2:AH201;"Confirmado")'),
        ("Brecha/superávit (COP)", "=B6-B4"), ("Decisión", '=IF(B4="";"PENDIENTE CS-04";IF(B6>=B4;"CUMPLE EL UMBRAL";"POR DEBAJO DEL UMBRAL"))')
    ], 2):
        set_text(vi, 0, row, label)
        if formula: set_formula(vi, 1, row, formula)
    unlock(vi, "B3:B4")

    make_view(sheets.getByName("Receivables"), "Cuentas por cobrar", "Resumen de caja y vencimientos de los registros del rastreador.", [
        ("Committed COP", "=SUM(Tracker.N2:N201)"), ("Received COP", "=SUM(Tracker.AA2:AA201)"),
        ("Outstanding COP", "=SUM(Tracker.AB2:AB201)"), ("Overdue accounts", '=COUNTIF(Tracker.AN2:AN201;"OVERDUE")'),
        ("Expired payment/PO deadlines", '=COUNTIF(Tracker.AN2:AN201;"DEADLINE EXPIRED")'),
    ])
    make_view(sheets.getByName("Exceptions"), "Excepciones", "Registros en lista de espera, rechazados, retirados, cancelados, reembolsados o en disputa.", [
        ("Wait-listed", '=COUNTIF(Tracker.AH2:AH201;"Wait-listed")'), ("Rejected", '=COUNTIF(Tracker.AH2:AH201;"Rejected")'),
        ("Withdrawn", '=COUNTIF(Tracker.AH2:AH201;"Withdrawn")'), ("Cancelled", '=COUNTIF(Tracker.AO2:AO201;"Cancelled")'),
        ("Refunded", '=COUNTIF(Tracker.AO2:AO201;"Refunded")'), ("Disputed", '=COUNTIF(Tracker.AO2:AO201;"Disputed")'),
    ])

    lists = sheets.getByName("Lists")
    set_text(lists, 0, 0, "Los valores controlados están incorporados en las validaciones del rastreador. Esta hoja se reserva para ampliaciones institucionales.")
    lists.IsVisible = False

    for name in ["LEAME", "Pipeline", "Viability", "Receivables", "Exceptions"]:
        sheets.getByName(name).protect(PASSWORD)
    en.protect(PASSWORD)

    if synthetic:
        populate_synthetic(tr)
        set_text(readme, 0, 14, "COPIA DE PRUEBA SINTÉTICA — NO USAR COMO REGISTRO REAL")
        readme.getCellRangeByName("A15:H15").merge(True)
        readme.getCellRangeByName("A15:H15").CellBackColor = AMBER
        readme.getCellRangeByName("A15:H15").CharWeight = 150

    for i in range(sheets.Count):
        enforce_contrast(sheets.getByIndex(i))

    path = SYNTHETIC if synthetic else TEMPLATE
    url = uno.systemPathToFileUrl(str(path))
    doc.storeAsURL(url, (prop("FilterName", "Calc MS Excel 2007 XML"), prop("Overwrite", True)))
    doc.close(True)


def make_view(sheet, title, subtitle, metrics):
    sheet.getCellRangeByName("A1:E1").merge(True)
    set_text(sheet, 0, 0, title)
    style_title(sheet, "A1:E1")
    set_text(sheet, 0, 1, subtitle)
    sheet.getCellRangeByName("A2:E2").merge(True)
    for i, (label, formula) in enumerate(metrics, 3):
        set_text(sheet, 0, i, label)
        set_formula(sheet, 1, i, formula)
    sheet.Columns.getByIndex(0).Width = 9000
    sheet.Columns.getByIndex(1).Width = 6000


def populate_synthetic(tr):
    rows = [
        {0:"SYN-001",1:"Laboratorio Andino",2:"Colombia",3:"Español",4:"R-TEST-01",5:1,6:1,7:0,8:0,10:"COT-SYN-001",11:0,12:5928000,13:5928000,14:"2026-08-15",15:"2026-08-15",16:"2026-08-10",17:"2026-07-20",18:"2026-07-21 09:00",19:"Orden de compra aceptada",20:"Sí",21:"Sí",22:"Aprobada",23:"2026-07-21",24:"Revisor A",25:"Pagado",26:5928000,29:"2026-08-01",30:"FAC-SYN-001",31:"P-SYN-001",32:"CO/SO₂ simultáneos",33:"Confirmado",44:"Coordinación",45:"Incorporación",46:"calaire_med@unal.edu.co",47:"2026-07-10",50:"Sí",51:"CS09-SYN-001",53:"Caso sintético satisfactorio"},
        {0:"SYN-002",1:"Metrología Norte",2:"Colombia",3:"Español",4:"R-TEST-01",5:0,6:0,7:1,8:1,10:"COT-SYN-002",11:0,12:5928000,13:5928000,14:"2026-08-15",15:"2026-08-15",16:"2026-08-10",17:"2026-07-22",18:"2026-07-23 10:00",19:"Cotización firmada",20:"No",21:"Sí",22:"Aprobada",23:"2026-07-23",24:"Revisor A",25:"Parcial",26:2964000,29:"2026-08-01",32:"Gas individual",33:"Aceptado pendiente de pago/orden",44:"Comercial",45:"Cobrar saldo",46:"calaire_med@unal.edu.co",47:"2026-07-12",50:"No",51:"CS09-SYN-002",53:"Caso sintético de pago parcial"},
        {0:"SYN-003",1:"Aire Pacífico",2:"Ecuador",3:"Español",4:"R-TEST-01",5:1,6:0,7:0,8:0,11:0,12:0,13:0,20:"Sí",21:"Sí",22:"Pendiente",25:"Pendiente",26:0,32:"Gas individual",33:"En lista de espera",35:"2026-07-24 08:00",44:"Comercial",45:"Vigilar cupo",46:"calaire_med@unal.edu.co",47:"2026-05-01",50:"No solicitado",53:"Caso sintético de lista de espera/interés obsoleto"},
    ]
    numeric = {5,6,7,8,11,12,13,26}
    dates = {14,15,16,17,18,23,29,35,41,47}
    for rr, data in enumerate(rows, 1):
        for cc, value in data.items():
            cell = tr.getCellByPosition(cc, rr)
            if cc in numeric:
                cell.Value = float(value)
            elif cc in dates:
                dt = datetime.fromisoformat(value)
                cell.Value = (dt - datetime(1899, 12, 30)).total_seconds() / 86400
            else:
                cell.String = str(value)


def col(n):
    s = ""
    while n >= 0:
        s = chr(n % 26 + 65) + s
        n = n // 26 - 1
    return s


def enforce_contrast(sheet):
    """Normaliza el libro a presentación monocromática."""
    was_protected = sheet.isProtected()
    if was_protected:
        sheet.unprotect(PASSWORD)
    cursor = sheet.createCursor()
    cursor.gotoEndOfUsedArea(True)
    end = cursor.RangeAddress
    for row in range(end.StartRow, end.EndRow + 1):
        for column in range(end.StartColumn, end.EndColumn + 1):
            cell = sheet.getCellByPosition(column, row)
            cell.CellBackColor = 0xFFFFFF
            cell.CharColor = 0x000000
    if was_protected:
        sheet.protect(PASSWORD)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    ctx = connect()
    build_book(ctx, False)
    build_book(ctx, True)
    print(TEMPLATE)
    print(SYNTHETIC)


if __name__ == "__main__":
    main()
