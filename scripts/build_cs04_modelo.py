#!/usr/bin/env python3
"""Genera el libro CS-04 (modelo de costos y precios) sobre la plantilla F-PSEA-01.

Ejecutar desde la raíz del repositorio. Cada pestaña reproduce la estructura
definida en servicio_comercial/02_precios_restringidos/CS-04_modelo_costos_precios.md.
Usa LibreOffice UNO (igual que build_cs10_tracker.py).
"""

from __future__ import annotations

import subprocess
import time
from pathlib import Path

import uno
from com.sun.star.beans import PropertyValue

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = (
    ROOT
    / "docs/qms/01_bloque_general/00_plantillas_base/F-PSEA-01 Plantilla Formato_Excel.xlsx"
)
OUT = ROOT / "servicio_comercial/02_precios_restringidos/CS-04_modelo_costos_precios.xlsx"

NAVY = 0xD9EAF7
LIGHT = 0xF3F6F9
WHITE = 0x000000
TARIFA = 5_928_000
PD = "[POR DILIGENCIAR]"
START = 5  # fila 6, bajo el encabezado institucional de la plantilla


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
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
        for _ in range(40):
            time.sleep(0.25)
            try:
                return resolver.resolve(url)
            except Exception:
                pass
        raise RuntimeError("No se pudo iniciar el listener UNO de LibreOffice")


# (nombre de pestaña, título del bloque, encabezados, filas)
SHEETS = [
    ("01 Supuestos", "PESTAÑA 1 — SUPUESTOS",
     ["Supuesto", "Valor", "Fuente / responsable"],
     [
         ["Tasa de cambio de referencia",
          "TRM USD/COP × referencia BCE USD/EUR, solo para convertir valores de referencia", "CS-01"],
         ["Frecuencia de actualización del tipo de cambio",
          "En la fecha de revisión de la referencia comparativa", "CS-01"],
         ["Asignación del riesgo cambiario",
          "No aplica a clientes: cotización y facturación únicamente en COP", "CS-01"],
         ["Capacidad por gas (individual)", "4 analizadores", "CS-01"],
         ["Capacidad simultánea de CO/SO₂", "3 participantes, 6 analizadores", "CS-01"],
         ["Inscripción prevista", PD, "Estimación de mercado"],
         ["Impuestos (IVA, retenciones, etc.)", PD, "Asesor tributario"],
         ["Diferencial tributario para clientes internacionales", PD, "Asesor tributario"],
         ["Margen / objetivo previsto",
          "Lanzamiento y validación; sin margen ni subsidio; no cotizar bajo el costo directo", "CS-01"],
         ["Factor de uso por ronda (fracción 0–1)", PD, "Responsable técnico"],
         ["Momento de cobro del pago (predeterminado)", PD, "Política financiera"],
         ["Calendario de cobro de pagos (institucional)", PD, "Política financiera"],
     ]),
    ("02 Costo comun", "PESTAÑA 2 — COSTO COMÚN",
     ["Elemento de costo", "Importe anual (COP)", "Asignación por ronda (COP)", "Notas"],
     [
         ["Coordinación", PD, PD, ""],
         ["Preparación de instalaciones", PD, PD, ""],
         ["Registro y administración de datos", PD, PD, ""],
         ["Entrega de informes", PD, PD, ""],
         ["Equipo compartido (calibrador, generador de aire cero)", PD, PD, "Desde la pestaña 04"],
     ]),
    ("03 Costo por gas", "PESTAÑA 3 — COSTO POR GAS",
     ["Bloque", "Costo cilindro / generación (COP)",
      "Ciclo de vida específico del analizador (COP)", "Asignación de costos (COP)", "Notas"],
     [
         ["CO", PD, PD, "=FORMULA(B{r}+C{r})", ""],
         ["SO₂", PD, PD, "=FORMULA(B{r}+C{r})", ""],
         ["NO/NO₂", PD, PD, "=FORMULA(B{r}+C{r})", "Un solo bloque NOx"],
         ["O₃", PD, PD, "=FORMULA(B{r}+C{r})", ""],
     ]),
    ("04 Ciclo de vida", "PESTAÑA 4 — CICLO DE VIDA DE LOS EQUIPOS",
     ["Activo", "Mantenimiento planificado (COP)", "Consumibles (COP)",
      "Calibración / servicio (COP)", "Provisión reparación correctiva (COP)",
      "Provisión anual total (COP)", "Factor de uso por ronda (0–1)", "Asignación por ronda (COP)"],
     [
         [a, PD, PD, PD, PD, "=FORMULA(SUM(B{r}:E{r}))", PD, "=FORMULA(F{r}*G{r})"]
         for a in ["Analizador / sistema de referencia de O₃", "Analizador de SO₂",
                   "Analizador de CO", "Analizador de NOx",
                   "Calibrador dinámico", "Generador de aire cero"]
     ]),
    ("05 Estrategia cilindros", "PESTAÑA 5 — ESTRATEGIA DE CILINDROS",
     ["Criterio", "Mezcla multicomponente", "Cilindros individuales", "Híbrida (si aplica)"],
     [
         ["Adquisición", "Menos pedidos / cilindros", "Varios pedidos / cilindros", PD],
         ["Concentraciones", "Una especificación para todas las diluciones", "Optimizado por gas", PD],
         ["Estabilidad / compatibilidad", "Debe ser certificablemente estable", "Gestionado por separado", PD],
         ["Trazabilidad", "Un certificado, valores por componente", "Certificados separados", PD],
         ["Costeo del paquete", "Más difícil de asignar a ventas de un solo gas",
          "Se asigna directamente al paquete de gases", PD],
         ["Falla / vencimiento", "Un problema puede afectar varios gases", "Aislado a un solo gas", PD],
         ["Equipos / almacenamiento", "Menos reguladores / conexiones",
          "Más reguladores, almacenamiento y manipulación", PD],
         ["Plazo de entrega", "Disponibilidad de mezclas personalizadas", "Varía según el gas", PD],
         ["Costo estimado por ronda (COP)", PD, PD, PD],
         ["Recomendación", PD, PD, PD],
         ["Estrategia aprobada", PD, "", ""],
         ["Aprobador técnico", PD, "", ""],
         ["Aprobador comercial/financiero", PD, "", ""],
     ]),
    ("06 Tarifa participacion", "PESTAÑA 6 — TARIFA FIJA DE PARTICIPACIÓN",
     ["Bloques seleccionados", "Analizadores incluidos", "Tarifa provisional sin impuestos (COP)",
      "Analizador adicional con capacidad residual (COP)", "Notas"],
     [
         ["Cualquier 1 bloque", "Hasta 1", TARIFA, 0, "Solo propuesta"],
         ["Cualquier 2 bloques", "Hasta 2, uno por bloque", TARIFA, 0, "Solo propuesta"],
         ["3 bloques cualesquiera", "Hasta 3, uno por bloque", TARIFA, 0, "Solo propuesta"],
         ["Los 4 bloques", "Hasta 4, uno por bloque", TARIFA, 0, "CO, SO₂, O₃ y NO/NO₂"],
     ]),
    ("06A Validacion referencia", "PESTAÑA 6.A — VALIDACIÓN DEL VALOR DE REFERENCIA",
     ["Medida", "Valor (COP)", "Fuente / cálculo"],
     [
         ["Costo directo, 1 bloque", PD, "Pestañas 02–04"],
         ["Costo directo, 2 bloques", PD, "Pestañas 02–04"],
         ["Costo directo, 3 bloques", PD, "Pestañas 02–04"],
         ["Costo directo, 4 bloques", PD, "Pestañas 02–04"],
         ["Costo total asignado, 4 bloques", PD, "Pestañas 02–04"],
         ["Tarifa plana provisional", TARIFA, "CS-01"],
         ["Contribución / déficit por escenario", "=FORMULA(B$11-B9)", "tarifa − costo (ajustar por escenario)"],
         ["Interpretación / decisión", PD, "Aprobación de la dirección antes de la cotización"],
     ]),
    ("07 Inscripcion", "PESTAÑA 7 — ESCENARIOS DE INSCRIPCIÓN",
     ["Escenario", "Participantes", "Analizadores", "Ingresos (COP)", "Costos (COP)",
      "Contribución (COP)", "Momento de entrada del efectivo", "¿Viable?"],
     [
         ["Baja (1 participante, 1 gas)", 1, 1, f"=FORMULA(B{{r}}*{TARIFA})", PD, "=FORMULA(D{r}-E{r})", PD, PD],
         ["Previsto", PD, PD, f"=FORMULA(B{{r}}*{TARIFA})", PD, "=FORMULA(D{r}-E{r})", PD, PD],
         ["Capacidad total, gas individual", 4, 4, f"=FORMULA(B{{r}}*{TARIFA})", PD, "=FORMULA(D{r}-E{r})", PD, PD],
         ["Capacidad total simultánea CO/SO₂", 3, 6, f"=FORMULA(B{{r}}*{TARIFA})", PD, "=FORMULA(D{r}-E{r})", PD, PD],
         ["Selección mixta", PD, PD, f"=FORMULA(B{{r}}*{TARIFA})", PD, "=FORMULA(D{r}-E{r})", PD, PD],
     ]),
    ("08 Escenarios", "PESTAÑA 8 — ESCENARIOS DE VIABILIDAD",
     ["Escenario", "Descripción", "Resultado"],
     [
         ["Punto de equilibrio, gas individual", "Cupos pagados mínimos para cubrir el costo", PD],
         ["Punto de equilibrio, CO/SO₂ simultáneos", "Cupos pagados mínimos para cubrir el costo", PD],
         ["Punto de equilibrio, paquete completo", "Cupos pagados mínimos para cubrir el costo", PD],
         ["Capacidad baja", "1–2 participantes", PD],
         ["Capacidad prevista", PD, PD],
         ["Capacidad total", "Según los límites de CS-01", PD],
         ["Flujo de caja, peor caso", "Inscripción baja + pagos atrasados", PD],
     ]),
    ("09 Aprobacion", "PESTAÑA 9 — APROBACIÓN",
     ["Campo", "Valor"],
     [
         ["Cuota fija de participación aprobada", PD],
         ["Ajuste de bloque seleccionado aprobado", "COP 0 a menos que se revise CS-01"],
         ["Tarifa de analizador adicional aprobada",
          "COP 0 durante la etapa de propuesta, sujeto a capacidad residual"],
         ["Estrategia de cilindro aprobada (pestaña 05)", PD],
         ["Paquetes aprobados (pestaña 06)", PD],
         ["Política cambiaria aprobada (pestaña 01)", PD],
         ["Calendario de cobro aprobado (pestaña 01)", PD],
         ["Precios aprobados válidos desde", PD],
         ["Precios aprobados válidos hasta", PD],
         ["Aprobador (comercial/financiero) — nombre, fecha, firma", PD],
         ["Aprobador (técnico) — nombre, fecha, firma", PD],
         ["Aprobador (dirección) — nombre, fecha, firma", PD],
     ]),
]


def fill_sheet(sheet, title, headers, rows):
    # limpia el área de datos bajo el encabezado institucional
    sheet.getCellRangeByName("A6:Z400").clearContents(1023)
    cell = sheet.getCellByPosition(0, START)
    cell.String = title
    band = sheet.getCellRangeByPosition(0, START, len(headers) - 1, START)
    band.CellBackColor = NAVY
    band.CharColor = WHITE
    band.CharWeight = 150
    hr = START + 1
    for j, h in enumerate(headers):
        c = sheet.getCellByPosition(j, hr)
        c.String = h
        c.CellBackColor = NAVY
        c.CharColor = WHITE
        c.CharWeight = 150
        c.IsTextWrapped = True
    for i, row in enumerate(rows):
        r = hr + 1 + i
        for j, v in enumerate(row):
            c = sheet.getCellByPosition(j, r)
            if isinstance(v, str) and v.startswith("=FORMULA("):
                c.Formula = "=" + v[len("=FORMULA("):-1].format(r=r + 1)
            elif isinstance(v, (int, float)):
                c.Value = v
            else:
                c.String = v
        if i % 2 == 1:
            sheet.getCellRangeByPosition(0, r, len(headers) - 1, r).CellBackColor = LIGHT


def enforce_contrast(sheet):
    """Normaliza el libro a presentación monocromática."""
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
    doc = desktop.loadComponentFromURL(
        TEMPLATE.as_uri(), "_blank", 0, (prop("Hidden", True),)
    )
    sheets = doc.Sheets
    for idx, (name, title, headers, rows) in enumerate(SHEETS):
        sheets.copyByName("Hoja 1", name, idx)
        sh = sheets.getByName(name)
        sh.getCellRangeByName("B3").String = "CS-04 MODELO DE COSTOS Y PRECIOS — ACCESO RESTRINGIDO"
        fill_sheet(sh, title, headers, rows)
    for old in ("Hoja 1", "Hoja 2"):
        if sheets.hasByName(old):
            sheets.removeByName(old)
    for i in range(sheets.Count):
        enforce_contrast(sheets.getByIndex(i))
    OUT.unlink(missing_ok=True)
    doc.storeToURL(OUT.as_uri(), (prop("FilterName", "Calc MS Excel 2007 XML"),))
    doc.close(False)
    print(f"generado: {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
