#!/usr/bin/env python3
"""
Exportador de Tareas de Logseq CALAIRE-EA a CSV

Este script extrae todas las tareas (TODO/DOING/DONE) del grafo Logseq
y genera un archivo CSV ordenado por deadline.

Uso:
    python tools/export_tareas.py
    python tools/export_tareas.py --output tareas_calaire.csv
    python tools/export_tareas.py --pages pages/ --journals journals/
"""

import re
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional

# Patrones regex para detectar bloques TODO/DOING/DONE
# Acepta tanto sin indentación como con tabulaciones
TODO_PATTERN = re.compile(r'^(\t*)-\s*(TODO|DOING|DONE)\s+(.+?)(?:\s+project::|$)', re.MULTILINE)

# Patrones para propiedades
PROPERTY_PATTERNS = {
    'deadline': re.compile(r'deadline::\s*(\d{4}-\d{2}-\d{2})'),
    'priority': re.compile(r'priority::\s*(high|medium|low)'),
    'project': re.compile(r'project::\s*\[\[([^\]]+)\]\]'),
    'status': re.compile(r'status::\s*(\w+)'),
}

def parse_markdown_file(file_path: Path) -> List[Dict]:
    """Parsea un archivo markdown y extrae tareas."""
    tareas = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Buscar bloques TODO/DOING/DONE
    matches = TODO_PATTERN.finditer(content)
    
    for match in matches:
        indent = match.group(1)
        estado = match.group(2)
        tarea_texto = match.group(3).strip()
        
        # Obtener el bloque completo (desde el match hasta el siguiente bloque)
        start = match.start()
        lines_from_match = content[start:].split('\n')
        
        # Capturar el bloque hasta encontrar otro bloque al mismo nivel o menos indentado
        block_content = match.group(0)
        for line in lines_from_match[1:]:
            # Si es una línea que empieza con - y tiene menos o igual indentación, termina el bloque
            if line.startswith('-') and (not line.startswith('\t' * (len(indent) + 1))):
                break
            block_content += '\n' + line
        
        # Extraer propiedades del bloque
        deadline = None
        priority = None
        project = None
        status = estado.lower()
        
        for prop_name, pattern in PROPERTY_PATTERNS.items():
            prop_match = pattern.search(block_content)
            if prop_match:
                if prop_name == 'deadline':
                    deadline = prop_match.group(1)
                elif prop_name == 'priority':
                    priority = prop_match.group(1)
                elif prop_name == 'project':
                    project = prop_match.group(1)
                elif prop_name == 'status':
                    status = prop_match.group(1)
        
        # Extraer notas (texto entre líneas)
        notas = ''
        for line in block_content.split('\n'):
            line = line.strip()
            if line and not line.startswith('deadline::') and not line.startswith('priority::') and not line.startswith('project::') and not line.startswith('status::') and not line.startswith('-'):
                notas += line + ' '
        notas = notas.strip()
        
        # Limpiar tarea_texto (remover texto de propiedades)
        for prop_name in ['deadline', 'priority', 'project', 'status']:
            tarea_texto = PROPERTY_PATTERNS[prop_name].sub('', tarea_texto)
        tarea_texto = tarea_texto.strip()
        
        # Generar ID
        if project and 'CALAIRE-APP' in project:
            prefix = 'APP'
        elif 'journals' in str(file_path):
            prefix = 'J'
        elif 'Prueba Piloto' in str(file_path):
            prefix = 'PI'
        else:
            prefix = 'EA'
        tarea_id = f"{prefix}-{len(tareas)+1:02d}"
        tarea_id = f"{prefix}-{len(tareas)+1:02d}"
        
        # Obtener la ruta base del proyecto (directorio padre de tools/)
        project_base = Path(__file__).parent.parent
        
        tareas.append({
            'id': tarea_id,
            'tarea': tarea_texto,
            'deadline': deadline,
            'prioridad': priority,
            'proyecto': project,
            'fuente': str(file_path.relative_to(project_base)),
            'estado': status,
            'notas': notas
        })
    
    return tareas

def export_to_csv(tareas: List[Dict], output_path: Path):
    """Escribe las tareas a un archivo CSV."""
    # Ordenar por deadline (las sin deadline van al final)
    def sort_key(t):
        if t['deadline']:
            return (0, t['deadline'], t['id'])
        return (1, t['id'])
    
    tareas_ordenadas = sorted(tareas, key=sort_key)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        # Escribir encabezado
        f.write('id,tarea,deadline,prioridad,proyecto,fuente,estado,notas\n')
        
        # Escribir tareas
        for tarea in tareas_ordenadas:
            # Escape comas en los campos
            tarea_escaped = {
                'id': tarea['id'],
                'tarea': tarea['tarea'].replace('"', '""').replace(',', ';'),
                'deadline': tarea['deadline'] or '',
                'prioridad': tarea['prioridad'] or '',
                'proyecto': tarea['proyecto'] or '',
                'fuente': tarea['fuente'],
                'estado': tarea['estado'],
                'notas': tarea['notas'].replace('"', '""').replace(',', ';')
            }
            
            linea = f"{tarea_escaped['id']},{tarea_escaped['tarea']},{tarea_escaped['deadline']},{tarea_escaped['prioridad']},{tarea_escaped['proyecto']},{tarea_escaped['fuente']},{tarea_escaped['estado']},{tarea_escaped['notas']}\n"
            f.write(linea)

def main():
    parser = argparse.ArgumentParser(description='Exportar tareas de Logseq a CSV')
    parser.add_argument('--pages', default='pages/', help='Directorio de páginas (default: pages/)')
    parser.add_argument('--journals', default='journals/', help='Directorio de journals (default: journals/)')
    parser.add_argument('--output', default='tareas_calaire.csv', help='Archivo CSV de salida (default: tareas_calaire.csv)')
    
    args = parser.parse_args()
    
    # Usar el directorio del script como base
    script_dir = Path(__file__).parent.parent
    
    # Buscar archivos markdown
    pages_dir = script_dir / args.pages
    journals_dir = script_dir / args.journals
    
    md_files = list(pages_dir.glob('*.md')) + list(journals_dir.glob('*.md'))
    
    print(f"Buscando tareas en {len(md_files)} archivos...")
    
    # Extraer tareas de todos los archivos
    todas_tareas = []
    for md_file in md_files:
        tareas = parse_markdown_file(md_file)
        todas_tareas.extend(tareas)
        if tareas:
            print(f"  ✓ {md_file}: {len(tareas)} tareas")
    
    print(f"\nTotal de tareas encontradas: {len(todas_tareas)}")
    
    # Exportar a CSV
    output_path = script_dir / args.output
    export_to_csv(todas_tareas, output_path)
    print(f"✓ CSV exportado a: {output_path.absolute()}")
    
    # Resumen
    with_deadline = sum(1 for t in todas_tareas if t['deadline'])
    todo_count = sum(1 for t in todas_tareas if t['estado'] == 'todo')
    doing_count = sum(1 for t in todas_tareas if t['estado'] == 'doing')
    done_count = sum(1 for t in todas_tareas if t['estado'] == 'done')
    
    print(f"\nResumen:")
    print(f"  Con deadline: {with_deadline}")
    print(f"  TODO: {todo_count}")
    print(f"  DOING: {doing_count}")
    print(f"  DONE: {done_count}")

if __name__ == '__main__':
    main()
