Como experto en gestión de proyectos, he elaborado esta guía práctica para formalizar los cinco artefactos clave del proyecto **CALAIRE-EA**. Esta guía sigue los estándares del **PMI** (PMBOK® y estándares prácticos) para asegurar que transformes la información actual de @proyecto.md en documentos de gestión robustos.

### 1\. Acta de Constitución del Proyecto (Project Charter)

Este documento no es un mero trámite; es el instrumento que confiere la autoridad formal al Director del Proyecto y alinea a los interesados sobre "qué es el éxito".

1. **Objetivo:** Autorizar formalmente la existencia del proyecto y dar autoridad a la Directora (Carmen Elena Zapata) para aplicar recursos organizacionales a las actividades del proyecto 1, 2\.  
2. **Entradas necesarias:** Caso de negocio, acuerdos (contratos internos/externos), factores ambientales de la empresa (normativa ISO) 3\.  
3. **Pasos para la elaboración:**  
4. **Definir el Propósito y Justificación:** Escribe por qué se hace el proyecto (cumplimiento normativo ISO 17043, acreditación ONAC).  
5. **Objetivos Medibles:** Establece criterios de éxito claros (ej. "Validar la App CALAIRE con el 100% de los algoritmos de la norma ISO 13528 para noviembre 2026") 4\.  
6. **Alcance de Alto Nivel:** Resume los límites. Qué incluye (Diseño, Piloto, QMS) y qué **no** incluye (ej. comercialización masiva en esta fase) 5\.  
7. **Riesgos Generales:** Menciona los riesgos estratégicos (ej. fallas en la adopción por parte de los laboratorios piloto) 4\.  
8. **Hitos Clave:** Fecha de inicio, rondas piloto, fecha de cierre 6\.  
9. **Presupuesto Pre-aprobado:** Indica el monto de inversión ($437M COP) 4\.  
10. **Autoridad:** Define explícitamente qué decisiones puede tomar la Directora sin consultar al patrocinador 7\.

### 2\. EDT / WBS Gráfica (Estructura de Desglose del Trabajo)

La EDT es la columna vertebral de la gestión del alcance. Si no está en la EDT, no es parte del proyecto.

* **Objetivo:** Descomponer jerárquicamente la totalidad del alcance del trabajo para lograr los objetivos del proyecto y crear los entregables requeridos 8, 9\.  
* **Regla de Oro:** La **Regla del 100%**. La suma del trabajo de los niveles inferiores debe ser igual al 100% del trabajo del nivel superior. No debe faltar nada, ni sobrar nada 10\.  
* **Pasos para la elaboración:**  
* **Nivel 1 (Raíz):** Nombre del Proyecto "CALAIRE-EA".  
* **Nivel 2 (Descomposición Principal):** Usa el ciclo de vida o fases principales:
* 1.1 Gestión del Proyecto.
* 1.2 Diseño y Protocolos (Fase I).
* 1.3 Desarrollo Tecnológico (CALAIRE-APP: R/Shiny).
* 1.4 Ejecución Piloto (Rondas).
* 1.5 Sistema de Gestión de Calidad (QMS).
* **Nivel 3 (Entregables):** Desglosa los componentes tangibles. Ej. Bajo "1.3 Desarrollo Tecnológico" irían "1.3.1 Módulo de Validación", "1.3.2 Interfaz de Usuario", "1.3.3 Manual de Usuario" 11, 12\.  
* **Paquetes de Trabajo:** El nivel más bajo debe ser asignable a una persona y estimable en costo y tiempo 13\.  
* **Formato:** Debe ser visual (diagrama de árbol u organigrama), no solo una lista indentada 14\.

### 3\. Cronograma del Proyecto (Diagrama de Gantt)

El cronograma conecta los entregables de la EDT con el tiempo, creando un modelo dinámico para la ejecución.

* **Objetivo:** Representar cuándo ocurrirán las actividades, sus duraciones y dependencias lógicas 15\.  
* **Pasos para la elaboración:**  
* **Definir Actividades:** Toma los paquetes de trabajo de la EDT y divídelos en acciones específicas (verbo \+ objeto) 16\.  
* **Secuenciar Actividades:** Identifica las dependencias. ¿Qué debe terminar para que otra inicie?  
* *Ejemplo:* No se puede iniciar la "Ronda 6" (Sucesor) hasta que la "Validación del Algoritmo A" (Predecesor) haya terminado. Usa relaciones Fin-Comienzo (FS) principalmente 17\.  
* **Estimar Duraciones:** Usa el juicio de expertos (tu equipo técnico) para estimar cuánto tomará cada actividad (optimista, probable, pesimista) 18, 19\.  
* **Identificar la Ruta Crítica:** El software calculará la secuencia de actividades que determina la duración total del proyecto. Cualquier retraso aquí retrasa el proyecto final 20, 21\.  
* **Establecer Línea Base:** Una vez aprobado, guarda esta versión como tu estándar de comparación 22\.

### 4\. Registro de Riesgos (Manejo de Brechas)

Debes transformar las "brechas normativas" actuales en una gestión activa de la incertidumbre.

1. **Objetivo:** Identificar, analizar y responder a eventos inciertos que pueden afectar los objetivos del proyecto 23, 24\.  
2. **Diferencia Clave:** Una "brecha" es un hecho actual (issue); un "riesgo" es algo que *podría* pasar debido a esa brecha si no se cierra a tiempo.  
3. **Estructura del Registro (Columnas sugeridas) 25:**  
4. **ID:** Código único (ej. R-001).  
5. **Descripción del Riesgo:** Causa $\\to$ Evento de Riesgo $\\to$ Efecto. (Ej. "Debido a la falta de validación estadística (causa), los resultados de la ronda piloto podrían ser erróneos (riesgo), causando la no acreditación ante ONAC (efecto)").  
6. **Probabilidad (P) e Impacto (I):** Escala del 1 al 5\.  
7. **Puntuación (PxI):** Para priorizar cuáles atender primero.  
8. **Dueño del Riesgo:** Persona responsable de vigilarlo.  
9. **Estrategia de Respuesta:** Evitar, Mitigar, Transferir o Aceptar 26\. (Ej. Contratar al consultor César Yate es una estrategia de *Mitigación*).  
10. **Estado:** Activo, Cerrado, Realizado.

### 5\. Presupuesto (Línea Base de Costos)

El control de costos requiere saber no solo *cuánto* se gastará, sino *cuándo*.

* **Objetivo:** Establecer la versión aprobada del presupuesto distribuido en el tiempo, excluyendo las reservas de gestión 27, 28\.  
* **Pasos para la elaboración:**  
* **Estimación de Costos:** Asigna costos a cada paquete de trabajo de la EDT (Personal, Equipos, Software, Consultoría) 29\.  
* **Agregar Costos:** Suma los costos de las actividades hacia arriba para crear el presupuesto por entregable 30\.  
* **Análisis de Reserva:**  
* *Reserva de Contingencia:* Dinero para los "conocidos-desconocidos" (riesgos identificados en tu registro). Se incluye en la Línea Base 31\.  
* *Reserva de Gestión:* Dinero para "desconocidos-desconocidos" (imprevistos totales). No se incluye en la Línea Base, pero sí en el Presupuesto Total 31\.  
* **Curva S (Time-Phasing):** Distribuye el gasto en el calendario. No gastarás los $437M el primer día. Muestra el gasto acumulado mes a mes. Esto te permitirá medir el Valor Ganado (EVM) más adelante 32, 33\.

**Nota final de experto:** No intentes hacer estos documentos perfectos desde el primer borrador. Son documentos vivos. Lo importante es que la **EDT** esté completa (alcance), el **Cronograma** tenga lógica (dependencias) y el **Registro de Riesgos** sea honesto (realidad).

