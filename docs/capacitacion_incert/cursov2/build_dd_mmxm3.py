"""Genera dd_mmxm3.html a partir de dd_mmxm3.md usando el mismo estilo del paquete."""
import re
import subprocess
from html import escape
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / "dd_mmxm3.md"
OUT = HERE / "dd_mmxm3.html"

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
a:focus-visible{outline:3px solid var(--accent);outline-offset:3px}
.sidebar{position:fixed;inset:0 auto 0 0;width:17rem;overflow-y:auto;padding:1.25rem 1rem;background:var(--surface);border-right:1px solid var(--line);z-index:10}
.sidebar strong{display:block;color:var(--accent);margin-bottom:.75rem}
.sidebar ul{list-style:none;margin:0;padding:0}
.sidebar li{margin:.15rem 0}
.sidebar a{display:block;padding:.38rem .55rem;border-radius:6px;text-decoration:none;color:var(--ink);font-size:.92rem}
.sidebar a:hover{background:var(--accent-soft);color:var(--accent)}
.sidebar .l2{padding-left:1.1rem;font-size:.85rem;color:var(--muted)}
main{max-width:1060px;margin-left:max(17rem,calc((100vw - 1400px)/2));padding:2rem 2rem 5rem}
.hero{border-left:5px solid var(--accent);padding:1.25rem 1.5rem;margin:0 0 2rem;background:var(--surface);border-radius:0 10px 10px 0;box-shadow:0 1px 3px rgba(0,0,0,.08)}
.hero h1{font-size:clamp(1.65rem,3vw,2.35rem);line-height:1.2;margin:.15rem 0 .65rem}
.meta{color:var(--muted);font-size:.92rem}
section.major{margin:2.5rem 0 3rem;scroll-margin-top:1rem}
section.major>h2{font-size:1.55rem;border-bottom:3px solid var(--accent);padding-bottom:.45rem;margin-bottom:1.3rem}
h1,h2,h3,h4,h5,h6{line-height:1.28;scroll-margin-top:1rem}
h1{font-size:1.65rem}h2{font-size:1.38rem;margin-top:2.2rem}h3{font-size:1.16rem;margin-top:1.7rem}h4{font-size:1.02rem}
.tablewrap{overflow-x:auto;margin:1rem 0;border:1px solid var(--line);border-radius:8px}
table{border-collapse:collapse;width:100%;min-width:38rem;background:var(--surface);font-size:.9rem}
th,td{border:1px solid var(--line);padding:.48rem .65rem;text-align:left;vertical-align:top}
th{background:var(--accent-soft);position:sticky;top:0}
pre{overflow-x:auto;max-width:100%;padding:1rem;background:var(--code);border:1px solid var(--line);border-radius:8px;line-height:1.45;tab-size:2}
code{font-family:"Cascadia Code","SFMono-Regular",Consolas,monospace;font-size:.88em}
:not(pre)>code{background:var(--chip);padding:.08rem .34rem;border-radius:4px}
hr{border:0;border-top:1px solid var(--line);margin:2rem 0}
blockquote{border-left:4px solid var(--accent);background:var(--surface);padding:.75rem 1rem;margin:1rem 0;border-radius:0 8px 8px 0;color:var(--ink)}
ul,ol{padding-left:1.4rem}
li{margin:.2rem 0}
footer{margin-top:3rem;color:var(--muted);font-size:.88rem;border-top:1px solid var(--line);padding-top:1rem}
@media(max-width:900px){.sidebar{position:static;width:auto;border-right:0;border-bottom:1px solid var(--line)}.sidebar>ul{display:flex;gap:.25rem;overflow-x:auto;flex-wrap:wrap}.sidebar>ul>li{flex:0 0 auto}.sidebar a{white-space:nowrap}main{margin:0;padding:1.25rem}}
@media print{
  :root{--bg:#fff;--surface:#fff;--ink:#000;--muted:#333;--accent:#245b7a;--accent-soft:#eef4f7;--line:#aaa;--code:#f5f5f5}
  body{background:#fff;color:#000;font-size:10.5pt}.sidebar{display:none}main{max-width:none;margin:0;padding:0}
  .hero{box-shadow:none}section.major{break-before:page;margin:0 0 1.2rem}
  a{color:#000;text-decoration:none}pre,.tablewrap{overflow:visible}table{min-width:0;font-size:8.5pt}th{position:static}
}
"""


def slug(text: str) -> str:
    s = text.lower()
    s = re.sub(r"[áàä]", "a", s)
    s = re.sub(r"[éèë]", "e", s)
    s = re.sub(r"[íìï]", "i", s)
    s = re.sub(r"[óòö]", "o", s)
    s = re.sub(r"[úùü]", "u", s)
    s = re.sub(r"ñ", "n", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def build_sidebar(headings: list[tuple[int, str]]) -> str:
    items = []
    for level, text, anchor in headings:
        if level == 1:
            continue
        cls = "l2" if level == 3 else ""
        items.append(f'<li><a class="{cls}" href="#{anchor}">{escape(text)}</a></li>')
    return (
        '<nav class="sidebar" aria-label="Navegación"><strong>Diagnóstico final</strong>'
        f'<ul>{"".join(items)}</ul></nav>'
    )


def main() -> None:
    result = subprocess.run(
        [
            "pandoc",
            "--from", "gfm",
            "--to", "html5",
            "--wrap=none",
            "--standalone",
            "--section-divs",
            "--shift-heading-level-by=0",
            str(SRC),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    body_match = re.search(r"<body[^>]*>(.*)</body>", result.stdout, re.S)
    assert body_match, "no se encontró <body>"
    body = body_match.group(1)

    h1_match = re.search(r"<h1[^>]*>(.*?)</h1>", body)
    title = re.sub(r"<[^>]+>", "", h1_match.group(1)).strip() if h1_match else "Diagnóstico"

    headings: list[tuple[int, str, str]] = []
    for m in re.finditer(r"<(h[1-6])[^>]*>(.*?)</\1>", body):
        level = int(m.group(1)[1])
        text = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        anchor = slug(text)
        headings.append((level, text, anchor))

    seen: dict[str, int] = {}
    id_map: dict[str, str] = {}
    for level, text, anchor in headings:
        n = seen.get(anchor, 0)
        seen[anchor] = n + 1
        id_map[text] = anchor if n == 0 else f"{anchor}-{n}"

    def add_id(m: re.Match) -> str:
        text = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        return f'<{m.group(1)} id="{id_map.get(text, slug(text))}">{m.group(2)}</{m.group(1)}>'

    body = re.sub(r"<(h[1-6])([^>]*)>(.*?)</\1>", add_id, body, flags=re.S)

    body = re.sub(
        r"(?s)(<table(?:[^>]*)?>.*?</table>)",
        r'<div class="tablewrap">\1</div>',
        body,
    )

    sidebar_headings = [(lvl, txt, id_map.get(txt, slug(txt))) for lvl, txt, _ in headings]
    sidebar = build_sidebar(sidebar_headings)

    html_doc = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title)}</title>
<style>{CSS}</style>
</head>
<body>
{sidebar}
<main>
{body}
<footer>Generado desde <code>dd_mmxm3.md</code> · {escape(SRC.name)} → {escape(OUT.name)}</footer>
</main>
</body>
</html>
"""
    OUT.write_text(html_doc, encoding="utf-8")
    print(f"escrito: {OUT} ({OUT.stat().st_size:,} bytes, {len(headings)} secciones)")


if __name__ == "__main__":
    main()
