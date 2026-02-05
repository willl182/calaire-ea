- tags:: [[MOC]], [[Inventory]]
- # Equipos de Medición y Calibración
- Este MOC centraliza el registro de todos los equipos de medición, analizadores de gases y sistemas de calibración utilizados en el proyecto CALAIRE-EA para las rondas de Ensayo de Aptitud.
- ## Equipos de Medición
	- [[Analizador CO]]
	- [[Analizador NOx]]
	- [[Analizador SO2]]
	- [[Analizador O3]]
- ## Sistemas de Calibración
	- [[Calibrador T700]]
- ## Plantilla para Nuevos Equipos
	- Cada equipo debe tener su propia página individual con la siguiente estructura:
		```
		- tags:: [[Equipo]], [[Medición]] | [[Calibración]]
		- # Nombre del Equipo
		  type:: [[Analizador]] | [[Calibrador]]
		  model:: Modelo del fabricante
		  serial:: Número de serie
		  owner:: [[Laboratorio]] | CALAIRE
		  status:: #operativo | #en_calibracion | #en_mantenimiento | #fuera_de_servicio
		- ## Especificaciones Técnicas
		    - Gas de interés: CO | NOx | SO2 | O3
		    - Rango de medición: [rango]
		    - Incertidumbre: ±[valor]
		    - Resolución: [valor]
		- ## Calibración
		    - Última calibración: [fecha]
		    - Próxima calibración: [fecha]
		    - Certificado: [[Certificado Calibración]]
		- ## Asignación por Ronda
		    - [[Ronda 1]]: [laboratorio]
		    - [[Ronda 2]]: [laboratorio]
		    - [[Ronda 3]]: [laboratorio]
		    - [[Ronda 4]]: [laboratorio]
		    - [[Ronda 5]]: [laboratorio]
		- ## Observaciones
		    - 
		- ## Documentación
		    - Manual de usuario: [[Manual]]
		    - Hoja de datos: [[Datasheet]]
		    - Fotos de equipo: [[Fotos]]
		```
- ## Estatus de Equipo
	- | Status | Significado |
	  |--------|-------------|
	  | `#operativo` | Disponible para uso en rondas EA |
	  | `#en_calibracion` | Proceso de calibración en curso |
	  | `#en_mantenimiento` | Mantenimiento preventivo o correctivo |
	  | `#fuera_de_servicio` | No disponible temporalmente |
- ## Trazabilidad
	- Para seguimiento de asignación de equipos por laboratorio y ronda, referirse a:
		- [[Prueba Piloto]] - Coordinación logística y transporte
		- [[Laboratorios]] - Registro de participantes y sus equipos
- ## Protocolos Asociados
	- [[Protocolo de Calibración Multipunto]] - Procedimiento para calibración de analizadores
	- [[Protocolo de Transporte de Equipos]] - Manejo seguro y acreditado
