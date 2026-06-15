#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"
template_dir="${HOME}/.local/share/pandoc/templates"
mkdir -p "$template_dir"
cp ficha_resumen_template.html "$template_dir/ficha_resumen_template.html"

field_value() {
  local field="$1"
  local source="$2"
  sed -n "s/| \\*\\*${field}\\*\\* | \\(.*\\) |/\\1/p" "$source" | head -1
}

{
  printf '%s\n' 'window.fichaNames = {'
  first=1
  for source in ficha_*.md; do
    base="${source%.md}"
    code="${base#ficha_}"
    ficha_name="$(field_value "Nombre decidido" "$source")"
    ficha_name="${ficha_name:-Ficha resumen}"
    ficha_name="$(printf '%s' "$ficha_name" | sed 's/\\/\\\\/g; s/"/\\"/g')"
    if [ "$first" -eq 0 ]; then
      printf '%s\n' ','
    fi
    first=0
    printf '  "%s": "%s"' "$code" "$ficha_name"
  done
  printf '%s\n' ''
  printf '%s\n' '};'
} > ficha_names.js

for source in ficha_*.md; do
  base="${source%.md}"
  code="${base#ficha_}"
  ficha_name="$(field_value "Nombre decidido" "$source")"
  ficha_type="$(field_value "Tipo documental" "$source")"
  ficha_state="$(field_value "Estado" "$source")"
  ficha_priority="$(field_value "Prioridad" "$source")"
  ficha_class="$(field_value "Clase de ficha" "$source")"
  ficha_name="${ficha_name:-Ficha resumen}"
  pandoc "$source" \
    --from=gfm \
    --to=html5 \
    --standalone \
    --toc \
    --toc-depth=3 \
    --template=ficha_resumen_template.html \
    --metadata title="$code" \
    --metadata pagetitle="$code - $ficha_name" \
    --metadata ficha_name="$ficha_name" \
    --metadata ficha_type="$ficha_type" \
    --metadata ficha_state="$ficha_state" \
    --metadata ficha_priority="$ficha_priority" \
    --metadata ficha_class="$ficha_class" \
    --metadata source="$source" \
    -o "${base}.html"
done

{
  printf '%s\n' '<!doctype html>'
  printf '%s\n' '<html lang="es">'
  printf '%s\n' '<head>'
  printf '%s\n' '  <meta charset="utf-8">'
  printf '%s\n' '  <meta name="viewport" content="width=device-width, initial-scale=1">'
  printf '%s\n' '  <title>Indice de fichas resumen SGC PEA</title>'
  printf '%s\n' '  <link rel="stylesheet" href="ficha_resumen.css">'
  printf '%s\n' '  <script defer src="ficha_names.js"></script>'
  printf '%s\n' '</head>'
  printf '%s\n' '<body>'
  printf '%s\n' '  <div class="page-shell">'
  printf '%s\n' '    <header class="hero">'
  printf '%s\n' '      <div class="eyebrow">CALAIRE-EA · Fichas resumen SGC PEA</div>'
  printf '%s\n' '      <h1>Indice de fichas resumen</h1>'
  printf '%s\n' '      <div class="hero-actions">'
  printf '%s\n' '        <a class="button primary" href="../mapa_navegacion_sgc_pea.html">Volver al mapa</a>'
  printf '%s\n' '        <a class="button" href="00_inventario_maestro_fichas.md">Ver inventario maestro</a>'
  printf '%s\n' '      </div>'
  printf '%s\n' '    </header>'
  printf '%s\n' '    <main class="layout index-layout">'
  printf '%s\n' '      <section class="content index-content">'
  printf '%s\n' '        <h2>Fichas disponibles</h2>'
  printf '%s\n' '        <p>Version HTML navegable generada desde las fichas Markdown del SGC PEA. El mapa principal enlaza las fichas asociadas a nodos; este indice permite revisar tambien las fichas sin nodo directo.</p>'
  printf '%s\n' '        <div class="ficha-grid">'
  for source in ficha_*.md; do
    base="${source%.md}"
    code="${base#ficha_}"
    family="${code%%-*}"
    title="$(field_value "Nombre decidido" "$source")"
    state="$(field_value "Estado" "$source")"
    type="$(field_value "Tipo documental" "$source")"
    title="${title:-Ficha resumen}"
    state="${state:-Sin estado}"
    type="${type:-Documento}"
    printf '          <a class="ficha-card" href="%s.html" data-family="%s">\n' "$base" "$family"
    printf '            <span class="ficha-code">%s</span>\n' "$code"
    printf '            <strong>%s</strong>\n' "$title"
    printf '            <span class="ficha-meta">%s · %s</span>\n' "$type" "$state"
    printf '%s\n' '          </a>'
  done
  printf '%s\n' '        </div>'
  printf '%s\n' '      </section>'
  printf '%s\n' '    </main>'
  printf '%s\n' '  </div>'
  printf '%s\n' '</body>'
  printf '%s\n' '</html>'
} > index.html
