#!/usr/bin/env python3
import csv
import math
from pathlib import Path
from statistics import NormalDist

from openpyxl import Workbook, load_workbook
from openpyxl.formatting.rule import ColorScaleRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

BASE = Path(__file__).resolve().parent
CSV_PATH = BASE / "plantilla_presupuesto_casos.csv"
XLSX_PATH = BASE / "plantilla_presupuesto.xlsx"
CONFIDENCE = 0.9545
DIVISORS = {
    "normal_u": 1.0,
    "normal_U_k2": 2.0,
    "rectangular": math.sqrt(3),
    "triangular": math.sqrt(6),
    "arcoseno": math.sqrt(2),
}
SHEETS = {
    "analizador_M4": ("Caso1_analizador", 120.0, "ppb"),
    "patron_M7": ("Caso2_patron", 100.0, "ppb"),
    "en14625_lab_selftest": ("Caso3_EN14625", 120.0, "nmol/mol"),
}
HEADERS = [
    "componente", "descripción", "valor", "PDF", "divisor",
    "u estándar", "c_i", "gl", "u_i(y)", "varianza %", "ranking",
]
MAX_ROWS = 20
HEADER_FILL = PatternFill("solid", fgColor="1F4E78")
SUB_FILL = PatternFill("solid", fgColor="D9EAF7")
INPUT_FILL = PatternFill("solid", fgColor="FFF2CC")
TOTAL_FILL = PatternFill("solid", fgColor="E2F0D9")
THIN = Side(style="thin", color="B7B7B7")


def read_cases():
    cases = {key: [] for key in SHEETS}
    with CSV_PATH.open(encoding="utf-8-sig", newline="") as source:
        for row in csv.DictReader(source):
            gl = row["gl"]
            cases[row["caso"]].append({
                "componente": row["componente"],
                "descripcion": row["descripcion"],
                "valor": float(row["valor"]),
                "pdf": row["pdf"],
                "ci": float(row["ci"]),
                "gl": math.inf if gl == "Inf" else float(gl),
            })
    return cases


def student_t_ppf(probability, degrees_freedom):
    z = NormalDist().inv_cdf(probability)
    v = degrees_freedom
    return (
        z
        + (z ** 3 + z) / (4 * v)
        + (5 * z ** 5 + 16 * z ** 3 + 3 * z) / (96 * v ** 2)
        + (3 * z ** 7 + 19 * z ** 5 + 17 * z ** 3 - 15 * z) / (384 * v ** 3)
    )


def calculate(rows, nominal):
    contributions = []
    denominator = 0.0
    for row in rows:
        u_std = row["valor"] / DIVISORS[row["pdf"]]
        contribution = abs(row["ci"]) * u_std
        contributions.append(contribution)
        if math.isfinite(row["gl"]):
            denominator += contribution ** 4 / row["gl"]
    u_c = math.sqrt(sum(value ** 2 for value in contributions))
    nu_eff = math.inf if denominator == 0 else u_c ** 4 / denominator
    probability = (1 + CONFIDENCE) / 2
    k = NormalDist().inv_cdf(probability) if math.isinf(nu_eff) else student_t_ppf(probability, nu_eff)
    expanded = k * u_c
    return {
        "u_c": u_c,
        "nu_eff": nu_eff,
        "k": k,
        "U": expanded,
        "W": 100 * expanded / nominal,
    }


def divisor_formula(row):
    return (
        f'=IF(D{row}="","",IF(D{row}="normal_u",1,'
        f'IF(D{row}="normal_U_k2",2,IF(D{row}="rectangular",SQRT(3),'
        f'IF(D{row}="triangular",SQRT(6),IF(D{row}="arcoseno",SQRT(2),""))))))'
    )


def build_budget_sheet(ws, rows, nominal, unit):
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = f"A1:K{MAX_ROWS + 1}"
    for col, header in enumerate(HEADERS, 1):
        cell = ws.cell(1, col, header)
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = HEADER_FILL
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = Border(bottom=THIN)

    pdf_validation = DataValidation(
        type="list",
        formula1='"normal_u,normal_U_k2,rectangular,triangular,arcoseno"',
        allow_blank=True,
    )
    pdf_validation.error = "Seleccione un PDF de la lista."
    pdf_validation.errorTitle = "PDF no válido"
    ws.add_data_validation(pdf_validation)

    for index in range(MAX_ROWS):
        row = index + 2
        data = rows[index] if index < len(rows) else None
        if data:
            ws.cell(row, 1, data["componente"])
            ws.cell(row, 2, data["descripcion"])
            ws.cell(row, 3, data["valor"])
            ws.cell(row, 4, data["pdf"])
            ws.cell(row, 7, data["ci"])
            if math.isfinite(data["gl"]):
                ws.cell(row, 8, data["gl"])
        ws.cell(row, 5, divisor_formula(row))
        ws.cell(row, 6, f'=IFERROR(IF(OR(C{row}="",E{row}=""),"",C{row}/E{row}),"")')
        ws.cell(row, 9, f'=IFERROR(IF(OR(F{row}="",G{row}=""),"",ABS(G{row})*F{row}),"")')
        ws.cell(row, 10, f'=IFERROR(IF(I{row}="","",100*I{row}^2/$B${MAX_ROWS + 4}^2),"")')
        ws.cell(row, 11, f'=IF(J{row}="","",RANK(J{row},$J$2:$J${MAX_ROWS + 1},0))')
        ws.cell(row, 12, f'=IFERROR(IF(H{row}="",0,I{row}^4/H{row}),0)')
        pdf_validation.add(ws.cell(row, 4))
        for col in (1, 2, 3, 4, 7, 8):
            ws.cell(row, col).font = Font(color="0000FF")
            ws.cell(row, col).fill = INPUT_FILL
        for col in range(1, 12):
            ws.cell(row, col).border = Border(bottom=THIN)
            ws.cell(row, col).alignment = Alignment(vertical="top", wrap_text=col == 2)

    total_start = MAX_ROWS + 3
    total_rows = {
        "nominal": total_start,
        "u_c": total_start + 1,
        "nu_eff": total_start + 2,
        "k": total_start + 3,
        "U": total_start + 4,
        "W": total_start + 5,
    }
    labels = {
        "nominal": f"y nominal ({unit})",
        "u_c": f"u_c ({unit})",
        "nu_eff": "nu_eff",
        "k": "k (95.45 %)",
        "U": f"U ({unit})",
        "W": "W (%)",
    }
    for key, row in total_rows.items():
        ws.cell(row, 1, labels[key])
        ws.cell(row, 1).font = Font(bold=True)
        ws.cell(row, 1).fill = TOTAL_FILL
        ws.cell(row, 2).fill = TOTAL_FILL
        ws.cell(row, 1).border = Border(bottom=THIN)
        ws.cell(row, 2).border = Border(bottom=THIN)

    ws.cell(total_rows["nominal"], 2, nominal)
    ws.cell(total_rows["nominal"], 2).font = Font(color="0000FF")
    ws.cell(total_rows["u_c"], 2, f'=SQRT(SUMSQ(I2:I{MAX_ROWS + 1}))')
    denominator = f'SUM(L2:L{MAX_ROWS + 1})'
    ws.cell(
        total_rows["nu_eff"], 2,
        f'=IFERROR(IF({denominator}=0,"",B{total_rows["u_c"]}^4/{denominator}),"")',
    )
    ws.cell(
        total_rows["k"], 2,
        f'=IF(B{total_rows["nu_eff"]}="",2,_xlfn.T.INV.2T(1-{CONFIDENCE},B{total_rows["nu_eff"]}))',
    )
    ws.cell(total_rows["U"], 2, f'=B{total_rows["k"]}*B{total_rows["u_c"]}')
    ws.cell(
        total_rows["W"], 2,
        f'=IFERROR(100*B{total_rows["U"]}/B{total_rows["nominal"]},"")',
    )

    widths = {"A": 29, "B": 54, "C": 13, "D": 18, "E": 13, "F": 14,
              "G": 10, "H": 10, "I": 14, "J": 14, "K": 11}
    for column, width in widths.items():
        ws.column_dimensions[column].width = width
    ws.row_dimensions[1].height = 30
    for row in range(2, MAX_ROWS + 2):
        ws.cell(row, 3).number_format = "0.0000"
        for col in (5, 6, 7, 8, 9):
            ws.cell(row, col).number_format = "0.0000"
        ws.cell(row, 10).number_format = "0.0"
        ws.cell(row, 11).number_format = "0"
    for row in total_rows.values():
        ws.cell(row, 2).number_format = "0.0000"
    ws.cell(total_rows["W"], 2).number_format = "0.0"
    ws.conditional_formatting.add(
        f"J2:J{MAX_ROWS + 1}",
        ColorScaleRule(start_type="min", start_color="FFFFFF", end_type="max", end_color="63BE7B"),
    )
    ws.column_dimensions["L"].hidden = True
    ws.sheet_view.showGridLines = False


def build_legend(ws):
    ws["A1"] = "Leyenda y uso"
    ws["A1"].font = Font(bold=True, color="FFFFFF", size=14)
    ws["A1"].fill = HEADER_FILL
    ws.merge_cells("A1:D1")
    ws.append([])
    ws.append(["PDF", "divisor", "uso", "fórmula"])
    for cell in ws[3]:
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = HEADER_FILL
    entries = [
        ("normal_u", 1, "u estándar dada directamente", "1"),
        ("normal_U_k2", 2, "incertidumbre expandida U con k=2", "2"),
        ("rectangular", math.sqrt(3), "semiancho a de distribución rectangular", "SQRT(3)"),
        ("triangular", math.sqrt(6), "semiancho a de distribución triangular", "SQRT(6)"),
        ("arcoseno", math.sqrt(2), "semiancho a de distribución arcoseno", "SQRT(2)"),
    ]
    for entry in entries:
        ws.append(entry)
    start = 10
    instructions = [
        "Instrucciones",
        "1. Ingrese componente, descripción, valor, PDF, c_i y gl en celdas amarillas.",
        "2. Deje gl vacío para componentes Tipo B con grados de libertad infinitos.",
        "3. divisor, u estándar, u_i(y), varianza %, ranking y totales se calculan con fórmulas vivas.",
        "4. valor representa u, U o semiancho según PDF seleccionado.",
        "5. Cambie y nominal para calcular W = 100·U/y nominal.",
        "6. k usa distribución normal para nu_eff infinito y T.INV.2T para nu_eff finito, igual que script R.",
        "Caso 3 es reconstrucción didáctica. Totales de referencia: u_c=4.3 nmol/mol y W=7.1 %.",
        "Celdas azules/amarillas: entradas editables. Texto negro: fórmulas.",
    ]
    for offset, text in enumerate(instructions):
        ws.cell(start + offset, 1, text)
        ws.merge_cells(start_row=start + offset, start_column=1, end_row=start + offset, end_column=4)
        ws.cell(start + offset, 1).alignment = Alignment(wrap_text=True, vertical="top")
        if offset == 0:
            ws.cell(start + offset, 1).font = Font(bold=True)
            ws.cell(start + offset, 1).fill = SUB_FILL
    ws.column_dimensions["A"].width = 30
    ws.column_dimensions["B"].width = 15
    ws.column_dimensions["C"].width = 56
    ws.column_dimensions["D"].width = 18
    ws.sheet_view.showGridLines = False


def verify(cases):
    expected = {
        "analizador_M4": {"u_c": (1.75, 0.01), "U": (3.5, 0.03), "W": (2.9, 0.1)},
        "patron_M7": {"u_c": (1.13, 0.01), "nu_eff": (105, 2), "k": (2.024, 0.002), "U": (2.29, 0.02)},
        "en14625_lab_selftest": {"u_c": (4.30, 0.01), "W": (7.2, 0.1)},
    }
    print("Verificación numérica Python (misma aritmética del script R):")
    all_ok = True
    for key, (_, nominal, _) in SHEETS.items():
        result = calculate(cases[key], nominal)
        checks = []
        for metric, (target, tolerance) in expected[key].items():
            ok = abs(result[metric] - target) <= tolerance
            all_ok &= ok
            checks.append(f"{metric}={result[metric]:.4f} [{'OK' if ok else 'FALLA'}]")
        print(f"- {SHEETS[key][0]}: " + ", ".join(checks))
    if not all_ok:
        raise SystemExit("Verificación numérica falló")


def verify_workbook():
    workbook = load_workbook(XLSX_PATH, data_only=False)
    expected_sheets = ["Plantilla", "Caso1_analizador", "Caso2_patron", "Caso3_EN14625", "Leyenda"]
    if workbook.sheetnames != expected_sheets:
        raise SystemExit(f"Hojas inesperadas: {workbook.sheetnames}")
    formulas = sum(
        1 for ws in workbook.worksheets for row in ws.iter_rows() for cell in row
        if isinstance(cell.value, str) and cell.value.startswith("=")
    )
    if formulas == 0:
        raise SystemExit("Libro sin fórmulas")
    print(f"Libro: {XLSX_PATH}")
    print(f"Hojas: {', '.join(workbook.sheetnames)}")
    print(f"Fórmulas vivas: {formulas}")


def main():
    cases = read_cases()
    verify(cases)
    workbook = Workbook()
    workbook.remove(workbook.active)
    build_budget_sheet(workbook.create_sheet("Plantilla"), [], 120.0, "nmol/mol")
    for key, (sheet_name, nominal, unit) in SHEETS.items():
        build_budget_sheet(workbook.create_sheet(sheet_name), cases[key], nominal, unit)
    build_legend(workbook.create_sheet("Leyenda"))
    workbook.calculation.fullCalcOnLoad = True
    workbook.calculation.forceFullCalc = True
    workbook.calculation.calcMode = "auto"
    workbook.save(XLSX_PATH)
    verify_workbook()


if __name__ == "__main__":
    main()
