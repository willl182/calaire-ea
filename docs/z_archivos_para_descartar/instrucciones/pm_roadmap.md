Como experto en gestión de proyectos, he analizado la documentación actual de **CALAIRE-EA** y, aunque existe información técnica y de estado valiosa, carece de la estructura formal de **artefactos de gestión** que prescribe el PMI para asegurar la gobernanza y el control.

Para formalizar el proyecto, es necesario transformar la información dispersa en **entregables de gestión** específicos. A continuación, detallo qué hace falta crear o consolidar, basándome en el *PMBOK® Guide 7ma Edición* y el *Estándar Práctico para Estructuras de Desglose de Trabajo (WBS)*.

### 1\. Artefactos de Estrategia e Inicio (Formalización)

Actualmente, tienes una lista de "Equipo y Roles" y una descripción general, pero no hay un documento que autorice formalmente el proyecto o defina a los interesados con precisión.

* **Acta de Constitución del Proyecto (Project Charter):**  
* **Estado:** **No existe / Debe elaborarse.**  
* **Por qué es necesario:** La información de la sección "Equipo y Roles" (Directora Carmen Elena Zapata, etc.) y los objetivos generales deben consolidarse en un documento firmado que autorice el uso de recursos y defina la autoridad del Director del Proyecto. Sin esto, el proyecto carece de nacimiento formal 1, 2\.  
* **Registro de Interesados (Stakeholder Register):**  
* **Estado:** **Información dispersa / Debe elaborarse.**  
* **Acción:** Tienes identificados a la U. de Medellín, UPB y SIATA en la sección "Prueba Piloto", y al equipo interno en "Equipo y Roles". Debes consolidarlos en una matriz que evalúe su **poder, interés e influencia**. Esto es vital para gestionar, por ejemplo, la "pendiente confirmación" del SIATA 3, 4\.

### 2\. Artefactos de Planificación (El "Qué" y el "Cuándo")

La sección "Entregables del Proyecto" es una lista, no una estructura de gestión.

* **Estructura de Desglose del Trabajo (EDT/WBS):**  
* **Estado:** **No existe / Debe elaborarse.**  
* **Por qué es necesario:** La lista actual (Estado del Arte, Protocolos, App) es plana. Según el *Estándar Práctico para WBS*, necesitas una descomposición jerárquica que cumpla la **regla del 100%** (todo el alcance del proyecto).  
* **Entregable Sugerido:** Crear una EDT gráfica donde:  
* Nivel 1: Proyecto CALAIRE-EA.  
* Nivel 2: Fases (Diseño, Piloto, QMS/Lanzamiento).  
* Nivel 3: Entregables (ej. bajo "Piloto" irían los laboratorios; bajo "App" irían los módulos de validación) 5, 6, 7\.  
* **Diccionario de la EDT (WBS Dictionary):**  
* **Estado:** **No existe / Debe elaborarse.**  
* **Acción:** Para entregables complejos como "CALAIRE-APP", necesitas un documento que detalle los criterios de aceptación técnicos (ej. "Algoritmo A robusto validado según ISO 13528"). La lista de funcionalidades actual es un buen insumo para esto 8, 9\.  
* **Cronograma del Proyecto (Project Schedule):**  
* **Estado:** **Parcial / Debe elaborarse.**  
* **Acción:** Tienes *deadlines* aislados (ej. "2026-02-15 confirmación laboratorios"). Necesitas un cronograma integrado (Gantt) que muestre las **dependencias**. Por ejemplo, ¿puede iniciar la "Ronda 6" si no se ha completado la "validación del aplicativo"? El PMI exige secuenciar actividades para calcular la ruta crítica 10, 11\.

### 3\. Artefactos de Incertidumbre y Calidad

El proyecto menciona "Brechas críticas" y "SGC", pero faltan los planes de gestión que expliquen cómo se abordarán.

* **Registro de Riesgos (Risk Register):**  
* **Estado:** **Información existente no consolidada / Debe elaborarse.**  
* **Acción:** La sección "Aprendizajes Clave" menciona "Brechas críticas identificadas (ISO 17043 cap. 7 y 8)". Esto no es solo un aprendizaje, es un **Riesgo Activo**. Debes trasladar estas brechas a un Registro de Riesgos formal que incluya:  
* *Riesgo:* Incumplimiento del cap. 7 de ISO 17043\.  
* *Impacto:* Falla en la acreditación.  
* *Respuesta:* El plan de acción específico (que parece ser la contratación del Consultor César Yate) 12, 4\.  
* **Plan de Gestión de Calidad (Quality Management Plan):**  
* **Estado:** **Parcial / Debe elaborarse.**  
* **Diferenciación:** Tienes los protocolos técnicos (P-PSEA-01 a 30). El *Plan de Gestión de Calidad* del proyecto es diferente: es el documento que dice *cómo* se asegurará que esos 30 procedimientos se redacten y aprueben a tiempo (gestión de las "oleadas" mencionadas en el SGC) 13, 14\.

### 4\. Artefactos de Monitoreo y Control

Para las fases "En Progreso" y "Pendiente", necesitas herramientas para medir el avance real.

* **Registro de Asuntos/Incidentes (Issue Log):**  
* **Estado:** **No existe / Debe elaborarse.**  
* **Acción:** El "Error de validación fue de verificación manual" mencionado en Aprendizajes es un incidente cerrado. Necesitas un registro vivo para nuevos problemas que surjan durante la prueba piloto (ej. si un analizador falla en la Universidad de Medellín) 15\.  
* **Registro de Lecciones Aprendidas (Lessons Learned Register):**  
* **Estado:** **Información existente / Debe formalizarse.**  
* **Acción:** Ya tienes una sección de "Aprendizajes Clave". Formalízala en un documento repositorio para que el conocimiento (como la "Declaración de NO Subcontratación") no se pierda al finalizar el proyecto 16, 15\.

### Resumen de Entregables a Elaborar (Prioridad Alta)

Para alinear @proyecto.md con el PMI, debes crear los siguientes documentos físicos o digitales:

1. **Project Charter:** Autorización formal firmada.  
2. **EDT (WBS) Gráfica:** Desglose visual de todo el alcance (Fases I, II, III).  
3. **Cronograma (Gantt):** Vinculando los hitos de la App con las fechas de las rondas piloto.  
4. **Registro de Riesgos:** Convirtiendo las "brechas normativas" en riesgos gestionables con planes de respuesta.  
5. **Presupuesto/Línea Base de Costos:** Consolidando la información que maneja el "Especialista de Costeo" en un presupuesto aprobado por fases.

