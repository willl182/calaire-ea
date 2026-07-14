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
    set_text(readme, 0, 0, "CS-10 — Enrollment and Revenue Tracker")
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
        "Prospect/customer ID", "Organization", "Country", "Preferred language", "Round ID",
        "CO analyzers", "SO₂ analyzers", "O₃ analyzers", "NO/NO₂ analyzers", "Analyzer count",
        "Quote number", "Quote revision", "Quote value COP", "Current committed value COP",
        "Quote expiry", "Quote acceptance deadline", "Payment / PO deadline", "Registration date",
        "Acceptance timestamp", "Acceptance channel", "Accredited laboratory", "Eligibility complete",
        "Contract-review status", "Contract-review date", "Contract reviewer",
        "PO/payment/invoice status", "Amount received COP", "Amount outstanding COP", "% paid",
        "Next installment due", "Invoice number", "Participant code", "Operating configuration",
        "Commercial status", "Wait-list group", "Wait-list timestamp", "Wait-list rank",
        "Last available slot", "Capacity alert", "Payment alert", "Cancellation/refund status",
        "Cancellation date", "Refund/credit note reference", "FX exposure", "Owner", "Next action",
        "Communication link/location", "EoI date", "EoI expiry date", "Stale-EoI flag",
        "Marketing consent", "CS-09 reference", "CS-12 reference", "Notes",
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
        set_text(tr, 43, r-1, "No aplica — COP only")
        set_formula(tr, 48, r-1, f'=IF(AV{r}="";"";AV{r}+60)')
        set_formula(tr, 49, r-1, f'=IF(A{r}="";"";IF(AND(AV{r}<>"";AW{r}<TODAY();OR(AI{r}="Interest";AI{r}="Quoted"));"Yes";"No"))')
        # Commercial status is column AH; AI is the calculated wait-list group.
        for c in (37, 38, 39, 49):
            cell = tr.getCellByPosition(c, r-1)
            cell.Formula = cell.Formula.replace("$AI$2:$AI$201", "$AH$2:$AH$201").replace(f"AI{r}", f"AH{r}")

    # Formats and validation.
    for rng in ["O2:S201", "X2:X201", "AD2:AD201", "AJ2:AJ201", "AP2:AP201", "AW2:AX201"]:
        tr.getCellRangeByName(rng).NumberFormat = doc.NumberFormats.getStandardFormat(2, doc.CharLocale)
    tr.getCellRangeByName("M2:N201").NumberFormat = doc.NumberFormats.getStandardFormat(4, doc.CharLocale)
    tr.getCellRangeByName("AA2:AB201").NumberFormat = doc.NumberFormats.getStandardFormat(4, doc.CharLocale)
    tr.getCellRangeByName("AC2:AC201").NumberFormat = doc.NumberFormats.getStandardFormat(10, doc.CharLocale)
    list_validation(doc, tr, "D2:D201", ["Español"])
    list_validation(doc, tr, "T2:T201", ["Institutional email", "Signed quote", "Accepted PO"])
    list_validation(doc, tr, "U2:V201", ["Yes", "No"])
    list_validation(doc, tr, "W2:W201", ["Pending", "Passed", "Failed"])
    list_validation(doc, tr, "Z2:Z201", ["Pending", "Partial", "Received", "Invoiced", "Paid", "Overdue"])
    list_validation(doc, tr, "AG2:AG201", ["Individual gas", "Simultaneous CO/SO₂"])
    list_validation(doc, tr, "AH2:AH201", ["Interest", "Quoted", "Registered", "Under review", "Quote-revision in progress", "Accepted pending payment/PO", "Confirmed", "Wait-listed", "Rejected", "Withdrawn"])
    list_validation(doc, tr, "AO2:AO201", ["", "Open", "Cancelled", "Refunded", "Disputed"])
    list_validation(doc, tr, "AY2:AY201", ["Yes", "No", "Not requested"])
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
    make_view(sheets.getByName("Pipeline"), "Pipeline", "Interest through quotation; exclude Stale-EoI = Yes.", [
        ("Active interests", '=COUNTIFS(Tracker.AH2:AH201;"Interest";Tracker.AX2:AX201;"No")'),
        ("Active quotes", '=COUNTIFS(Tracker.AH2:AH201;"Quoted";Tracker.AX2:AX201;"No")'),
        ("Quote revision in progress", '=COUNTIF(Tracker.AH2:AH201;"Quote-revision in progress")'),
        ("Stale EoI", '=COUNTIF(Tracker.AX2:AX201;"Yes")'),
    ])
    make_view(sheets.getByName("Enrollment"), "Enrollment", "Confirmed capacity for the round entered in B3.", [])
    en = sheets.getByName("Enrollment")
    set_text(en, 0, 2, "Round ID")
    unlock(en, "B3")
    for c, h in enumerate(["Metric", "Confirmed", "Limit", "Residual", "Alert"]): set_text(en, c, 4, h)
    style_header(en, "A5:E5")
    metrics = [("CO analyzers", "F", 4), ("SO₂ analyzers", "G", 4), ("O₃ analyzers", "H", 4), ("NO/NO₂ analyzers", "I", 4)]
    for i, (label, letter, limit) in enumerate(metrics, 5):
        set_text(en, 0, i, label); set_formula(en, 1, i, f'=SUMIFS(Tracker.{letter}2:{letter}201;Tracker.E2:E201;$B$3;Tracker.AH2:AH201;"Confirmed")'); set_text(en, 2, i, limit); set_formula(en, 3, i, f'=C{i+1}-B{i+1}'); set_formula(en, 4, i, f'=IF(D{i+1}<0;"OVER CAPACITY";IF(D{i+1}=0;"LAST SLOT";"OK"))')
    set_text(en, 0, 10, "Simultaneous CO/SO₂ organizations")
    set_formula(en, 1, 10, '=COUNTIFS(Tracker.E2:E201;$B$3;Tracker.AH2:AH201;"Confirmed";Tracker.AG2:AG201;"Simultaneous CO/SO₂")')
    set_text(en, 2, 10, 3); set_formula(en, 3, 10, "=C11-B11"); set_formula(en, 4, 10, '=IF(D11<0;"OVER CAPACITY";IF(D11=0;"LAST SLOT";"OK"))')
    set_text(en, 0, 11, "Simultaneous CO/SO₂ analyzers")
    set_formula(en, 1, 11, '=SUMIFS(Tracker.J2:J201;Tracker.E2:E201;$B$3;Tracker.AH2:AH201;"Confirmed";Tracker.AG2:AG201;"Simultaneous CO/SO₂")')
    set_text(en, 2, 11, 6); set_formula(en, 3, 11, "=C12-B12"); set_formula(en, 4, 11, '=IF(D12<0;"OVER CAPACITY";IF(D12=0;"LAST SLOT";"OK"))')

    make_view(sheets.getByName("Viability"), "Viability", "Confirmed revenue versus threshold. Enter round and approved CS-04 threshold.", [])
    vi = sheets.getByName("Viability")
    for row, (label, formula) in enumerate([
        ("Round ID", ""), ("Approved minimum revenue COP", ""),
        ("Confirmed organizations", '=COUNTIFS(Tracker.E2:E201;B3;Tracker.AH2:AH201;"Confirmed")'),
        ("Confirmed committed revenue COP", '=SUMIFS(Tracker.N2:N201;Tracker.E2:E201;B3;Tracker.AH2:AH201;"Confirmed")'),
        ("Gap / surplus COP", "=B6-B4"), ("Decision", '=IF(B4="";"PENDING CS-04";IF(B6>=B4;"MEETS THRESHOLD";"BELOW THRESHOLD"))')
    ], 2):
        set_text(vi, 0, row, label)
        if formula: set_formula(vi, 1, row, formula)
    unlock(vi, "B3:B4")

    make_view(sheets.getByName("Receivables"), "Receivables", "Cash and overdue summary from tracker rows.", [
        ("Committed COP", "=SUM(Tracker.N2:N201)"), ("Received COP", "=SUM(Tracker.AA2:AA201)"),
        ("Outstanding COP", "=SUM(Tracker.AB2:AB201)"), ("Overdue accounts", '=COUNTIF(Tracker.AN2:AN201;"OVERDUE")'),
        ("Expired payment/PO deadlines", '=COUNTIF(Tracker.AN2:AN201;"DEADLINE EXPIRED")'),
    ])
    make_view(sheets.getByName("Exceptions"), "Exceptions", "Wait-listed, rejected, withdrawn, cancelled, refunded or disputed records.", [
        ("Wait-listed", '=COUNTIF(Tracker.AH2:AH201;"Wait-listed")'), ("Rejected", '=COUNTIF(Tracker.AH2:AH201;"Rejected")'),
        ("Withdrawn", '=COUNTIF(Tracker.AH2:AH201;"Withdrawn")'), ("Cancelled", '=COUNTIF(Tracker.AO2:AO201;"Cancelled")'),
        ("Refunded", '=COUNTIF(Tracker.AO2:AO201;"Refunded")'), ("Disputed", '=COUNTIF(Tracker.AO2:AO201;"Disputed")'),
    ])

    lists = sheets.getByName("Lists")
    set_text(lists, 0, 0, "Controlled values are embedded in Tracker validations. This sheet is reserved for institutional extensions.")
    lists.IsVisible = False

    for name in ["LEAME", "Pipeline", "Viability", "Receivables", "Exceptions"]:
        sheets.getByName(name).protect(PASSWORD)
    en.protect(PASSWORD)

    if synthetic:
        populate_synthetic(tr)
        set_text(readme, 0, 14, "SYNTHETIC TEST COPY — DO NOT USE AS A LIVE REGISTER")
        readme.getCellRangeByName("A15:H15").merge(True)
        readme.getCellRangeByName("A15:H15").CellBackColor = AMBER
        readme.getCellRangeByName("A15:H15").CharWeight = 150

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
        {0:"SYN-001",1:"Laboratorio Andino",2:"Colombia",3:"Español",4:"R-TEST-01",5:1,6:1,7:0,8:0,10:"COT-SYN-001",11:0,12:5928000,13:5928000,14:"2026-08-15",15:"2026-08-15",16:"2026-08-10",17:"2026-07-20",18:"2026-07-21 09:00",19:"Accepted PO",20:"Yes",21:"Yes",22:"Passed",23:"2026-07-21",24:"Revisor A",25:"Paid",26:5928000,29:"2026-08-01",30:"FAC-SYN-001",31:"P-SYN-001",32:"Simultaneous CO/SO₂",33:"Confirmed",44:"Coordinación",45:"Onboarding",46:"calaire_med@unal.edu.co",47:"2026-07-10",50:"Yes",51:"CS09-SYN-001",53:"Synthetic happy path"},
        {0:"SYN-002",1:"Metrología Norte",2:"Colombia",3:"Español",4:"R-TEST-01",5:0,6:0,7:1,8:1,10:"COT-SYN-002",11:0,12:5928000,13:5928000,14:"2026-08-15",15:"2026-08-15",16:"2026-08-10",17:"2026-07-22",18:"2026-07-23 10:00",19:"Signed quote",20:"No",21:"Yes",22:"Passed",23:"2026-07-23",24:"Revisor A",25:"Partial",26:2964000,29:"2026-08-01",32:"Individual gas",33:"Accepted pending payment/PO",44:"Comercial",45:"Collect balance",46:"calaire_med@unal.edu.co",47:"2026-07-12",50:"No",51:"CS09-SYN-002",53:"Synthetic partial payment"},
        {0:"SYN-003",1:"Aire Pacífico",2:"Ecuador",3:"Español",4:"R-TEST-01",5:1,6:0,7:0,8:0,11:0,12:0,13:0,20:"Yes",21:"Yes",22:"Pending",25:"Pending",26:0,32:"Individual gas",33:"Wait-listed",35:"2026-07-24 08:00",44:"Comercial",45:"Monitor slot",46:"calaire_med@unal.edu.co",47:"2026-05-01",50:"Not requested",53:"Synthetic wait-list/stale case"},
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


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    ctx = connect()
    build_book(ctx, False)
    build_book(ctx, True)
    print(TEMPLATE)
    print(SYNTHETIC)


if __name__ == "__main__":
    main()
