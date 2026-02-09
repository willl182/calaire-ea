/**
 * Google Apps Script para Alertas de Tareas CALAIRE-EA
 * 
 * Instalación:
 * 1. Abre tu Google Sheet con tareas_calaire.csv
 * 2. Ve a Extensiones > Apps Script
 * 3. Copia este código al editor
 * 4. Ejecuta configurarTrigger() para activar alertas diarias
 * 
 * Funcionalidades:
 * - Envía alertas por email 3 días antes del deadline
 * - Colorea filas según estado: rojo=vencido, amarillo=próximo (≤3 días), verde=completado
 * - Trigger automático diario a las 8am
 */

// Constantes de configuración
const CONFIG = {
  // Columnas del CSV (índice 0-based)
  COLUMNS: {
    ID: 0,
    TAREA: 1,
    DEADLINE: 2,
    PRIORIDAD: 3,
    PROYECTO: 4,
    FUENTE: 5,
    ESTADO: 6,
    NOTAS: 7
  },
  // Días de anticipación para alertas
  ALERT_DAYS: 3,
  // Email del destinatario
  EMAIL: 'tu-email@ejemplo.com' // ← CAMBIAR ESTO
};

/**
 * Envía alertas de tareas próximas a vencer
 */
function enviarAlertas() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const data = sheet.getDataRange().getValues();
  
  // Ignorar encabezado
  const rows = data.slice(1);
  
  const hoy = new Date();
  const tareasAlerta = [];
  
  // Revisar cada fila
  rows.forEach((row, rowIndex) => {
    const deadlineStr = row[CONFIG.COLUMNS.DEADLINE];
    const estado = row[CONFIG.COLUMNS.ESTADO];
    const id = row[CONFIG.COLUMNS.ID];
    const tarea = row[CONFIG.COLUMNS.TAREA];
    const prioridad = row[CONFIG.COLUMNS.PRIORIDAD];
    const proyecto = row[CONFIG.COLUMNS.PROYECTO];
    
    // Solo procesar tareas con deadline y no completadas
    if (!deadlineStr || estado === 'done' || estado === 'DONE') {
      return;
    }
    
    const deadline = new Date(deadlineStr);
    const diasRestantes = Math.ceil((deadline - hoy) / (1000 * 60 * 60 * 24));
    
    // Alertar si faltan ≤ días de configuración
    if (diasRestantes >= 0 && diasRestantes <= CONFIG.ALERT_DAYS) {
      tareasAlerta.push({
        fila: rowIndex + 2, // +2 por encabezado y 0-indexing
        id,
        tarea,
        prioridad,
        proyecto,
        deadline: deadline.toLocaleDateString('es-ES'),
        diasRestantes
      });
    }
  });
  
  // Enviar email con alertas
  if (tareasAlerta.length > 0) {
    enviarEmailAlerta(tareasAlerta);
  }
  
  // Actualizar formato condicional
  formatoCondicional();
}

/**
 * Envía email con lista de tareas próximas
 */
function enviarEmailAlerta(tareas) {
  const hoy = new Date().toLocaleDateString('es-ES');
  
  let cuerpo = `
<h2>📋 Alertas de Tareas CALAIRE-EA</h2>
<p><strong>Fecha:</strong> ${hoy}</p>
<p>Tienes <strong>${tareas.length} tarea(s)</strong> próxima(s) a vencer en los próximos ${CONFIG.ALERT_DAYS} días:</p>
<table border="1" cellpadding="8" style="border-collapse: collapse;">
  <tr style="background-color: #f0f0f0;">
    <th>ID</th>
    <th>Prioridad</th>
    <th>Proyecto</th>
    <th>Tarea</th>
    <th>Deadline</th>
    <th>Días Restantes</th>
  </tr>
`;
  
  tareas.forEach(t => {
    const prioridadColor = t.prioridad === 'high' ? '🔴' : t.prioridad === 'medium' ? '🟡' : '🟢';
    cuerpo += `
  <tr>
    <td>${t.id}</td>
    <td>${prioridadColor} ${t.prioridad || 'N/A'}</td>
    <td>${t.proyecto || 'N/A'}</td>
    <td>${t.tarea}</td>
    <td>${t.deadline}</td>
    <td style="font-weight: bold; color: ${t.diasRestantes <= 1 ? 'red' : 'orange'}">${t.diasRestantes}</td>
  </tr>`;
  });
  
  cuerpo += `
</table>
<p>Revisa tu hoja de tareas: <a href="${SpreadsheetApp.getActiveSpreadsheet().getUrl()}">Ver en Google Sheets</a></p>
<hr>
<p style="font-size: 12px; color: #666;">
Este es un mensaje automático del sistema de seguimiento de tareas CALAIRE-EA.
</p>
`;
  
  MailApp.sendEmail({
    to: CONFIG.EMAIL,
    subject: `📋 ${tareas.length} tarea(s) próxima(s) a vencer`,
    htmlBody: cuerpo
  });
  
  console.log(`Email enviado con ${tareas.length} alertas`);
}

/**
 * Aplica formato condicional a la hoja
 * - Rojo: tareas vencidas
 * - Amarillo: tareas próximas (≤3 días)
 * - Verde: tareas completadas
 */
function formatoCondicional() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const range = sheet.getDataRange();
  
  // Limpiar reglas existentes
  sheet.getConditionalFormatRules().forEach(rule => {
    sheet.removeConditionalFormatRule(rule);
  });
  
  // Nuevas reglas
  const rules = [];
  
  // Regla 1: Tareas completadas (DONE/done) - Verde
  rules.push(
    SpreadsheetApp.newConditionalFormatRule()
      .whenTextSatisfies('DONE|done')
      .setBackground('#d4edda')
      .setRanges([range])
      .build()
  );
  
  // Regla 2: Tareas vencidas - Rojo
  rules.push(
    SpreadsheetApp.newConditionalFormatRule()
      .whenDateBefore(SpreadsheetApp.RelativeDate.TODAY)
      .setBackground('#f8d7da')
      .setRanges([range])
      .build()
  );
  
  // Regla 3: Alta prioridad (high) - Naranja claro
  rules.push(
    SpreadsheetApp.newConditionalFormatRule()
      .whenTextSatisfies('high')
      .setBackground('#fff3cd')
      .setRanges([range])
      .build()
  );
  
  // Aplicar reglas
  sheet.setConditionalFormatRules(rules);
  
  console.log('Formato condicional actualizado');
}

/**
 * Configura trigger diario automático
 * Ejecuta esta función una vez para activar las alertas
 */
function configurarTrigger() {
  // Eliminar triggers existentes
  const triggers = ScriptApp.getProjectTriggers();
  triggers.forEach(trigger => {
    if (trigger.getHandlerFunction() === 'enviarAlertas') {
      ScriptApp.deleteTrigger(trigger);
    }
  });
  
  // Crear nuevo trigger diario a las 8am
  ScriptApp.newTrigger('enviarAlertas')
    .timeBased()
    .everyDays(1)
    .atHour(8)
    .create();
  
  console.log('Trigger configurado: alertas diarias a las 8am');
}

/**
 * Función de prueba - ejecuta para verificar configuración
 */
function testAlertas() {
  console.log('Ejecutando prueba de alertas...');
  enviarAlertas();
  console.log('Prueba completada');
}

/**
 * Muestra estadísticas de la hoja actual
 */
function estadisticas() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const data = sheet.getDataRange().getValues();
  const rows = data.slice(1);
  
  const hoy = new Date();
  
  let total = rows.length;
  let conDeadline = 0;
  let vencidas = 0;
  let proximas = 0;
  let completadas = 0;
  let highPriority = 0;
  
  rows.forEach(row => {
    const deadlineStr = row[CONFIG.COLUMNS.DEADLINE];
    const estado = row[CONFIG.COLUMNS.ESTADO];
    const prioridad = row[CONFIG.COLUMNS.PRIORIDAD];
    
    if (deadlineStr) {
      conDeadline++;
      const deadline = new Date(deadlineStr);
      const diasRestantes = (deadline - hoy) / (1000 * 60 * 60 * 24);
      
      if (diasRestantes < 0) {
        vencidas++;
      } else if (diasRestantes <= 3) {
        proximas++;
      }
    }
    
    if (estado === 'done' || estado === 'DONE') {
      completadas++;
    }
    
    if (prioridad === 'high') {
      highPriority++;
    }
  });
  
  console.log('📊 Estadísticas de Tareas:');
  console.log(`Total: ${total}`);
  console.log(`Con deadline: ${conDeadline}`);
  console.log(`Vencidas: ${vencidas}`);
  console.log(`Próximas (≤3 días): ${proximas}`);
  console.log(`Completadas: ${completadas}`);
  console.log(`Alta prioridad: ${highPriority}`);
  
  return {
    total,
    conDeadline,
    vencidas,
    proximas,
    completadas,
    highPriority
  };
}
