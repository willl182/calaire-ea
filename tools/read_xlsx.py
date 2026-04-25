import zipfile, xml.etree.ElementTree as ET, re, sys

path = sys.argv[1] if len(sys.argv) > 1 else '/home/w182/w421/calaire-ea/docs/prueba_piloto/F-PSEA-05A-P2.xlsx'

with zipfile.ZipFile(path) as z:
    shared = []
    if 'xl/sharedStrings.xml' in z.namelist():
        tree = ET.parse(z.open('xl/sharedStrings.xml'))
        root = tree.getroot()
        ns = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'
        for si in root.findall('{'+ns+'}si'):
            text = ''.join(t.text or '' for t in si.iter('{'+ns+'}t'))
            shared.append(text)

    tree = ET.parse(z.open('xl/worksheets/sheet1.xml'))
    root = tree.getroot()
    ns = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'

    rows = {}
    for row in root.findall('.//{'+ns+'}row'):
        r_num = int(row.get('r'))
        cols = {}
        for c in row.findall('{'+ns+'}c'):
            ref = c.get('r')
            t = c.get('t', '')
            v = c.find('{'+ns+'}v')
            if v is not None and v.text:
                if t == 's':
                    val = shared[int(v.text)]
                else:
                    val = v.text
                col_letters = re.match(r'([A-Z]+)', ref).group(1)
                cols[col_letters] = val
        if cols:
            rows[r_num] = cols

    for r in sorted(rows.keys()):
        print(f"Fila {r}: {rows[r]}")
