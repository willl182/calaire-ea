#!/usr/bin/env bash
set -euo pipefail

usage() {
  printf 'Uso: %s <codigo_ronda>\n' "$(basename "$0")" >&2
  printf 'Patron esperado: EA-[A-Z0-9]+-[0-9]{4}-R[0-9]+\n' >&2
}

if [ "$#" -ne 1 ]; then
  usage
  exit 1
fi

round_code="$1"
if [[ ! "$round_code" =~ ^EA-[A-Z0-9]+-[0-9]{4}-R[0-9]+$ ]]; then
  printf 'Codigo de ronda invalido: %s\n' "$round_code" >&2
  usage
  exit 1
fi

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/../.." && pwd)"
template="$script_dir/plantilla_checklist_ronda.md"
deploy_root="$repo_root/02_despliegue_rondas"
round_root="$deploy_root/$round_code"

if [ ! -f "$template" ]; then
  printf 'No existe la plantilla requerida: %s\n' "$template" >&2
  exit 1
fi

stages=(
  "01_planificacion_ronda"
  "02_comunicaciones_participantes"
  "03_preparacion_item"
  "04_datos_y_preprocesamiento"
  "05_homogeneidad_estabilidad"
  "06_analisis_e_informe"
  "07_cierre_sgc"
)

mkdir -p "$round_root"

for stage in "${stages[@]}"; do
  mkdir -p "$round_root/$stage"
  touch "$round_root/$stage/.gitkeep"
done

checklist="$round_root/checklist_ronda.md"
if [ ! -f "$checklist" ]; then
  cp "$template" "$checklist"
  checklist_status="creado"
else
  checklist_status="existente, no sobrescrito"
fi

printf 'Ronda: %s\n' "$round_code"
printf 'Destino: %s\n' "$round_root"
printf 'Checklist: %s\n' "$checklist_status"
printf 'Carpetas de etapa: %s\n' "${#stages[@]}"
