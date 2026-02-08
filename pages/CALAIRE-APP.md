- tags:: [[MOC]], [[Software]]
- # CALAIRE-APP: Aplicativo Estadístico ISO 13528
- **Estado**
	- status:: [[EN PROGRESO]]
	- deadline:: 2026-02-20
	- repo:: [Pending GitHub URL]
- **Hallazgos Recientes**
	- Validación de resultados reportada por César Yate (2026-02-07): el error de imputación de datos fue cometido por César Yate durante la verificación manual, no por el aplicativo CALAIRE-APP. El aplicativo funciona correctamente para preprocesamiento, homogeneidad, estabilidad, nIQR y MADe según ISO 13528:2017.
	- **Estado validado:** Preprocesamiento ✅, Homogeneidad ✅, Estabilidad ✅, nIQR ✅, MADe ✅
	- **Estado pendiente de revisión:** Incertidumbre de homogeneidad y estabilidad, Algoritmo A, Compatibilidad metrológica, Puntuaciones z, z', zeta, En
- **Backlog Inmediato**
	- TODO Enviar informe de hallazgos a César Yate
	  project:: [[CALAIRE-APP]]
	  priority:: high
	  deadline:: 2026-02-15
	- TODO Completar informe de validación
	  project:: [[CALAIRE-APP]]
	  priority:: high
	  deadline:: 2026-02-20
	- TODO Documentación de uso para participantes
	  project:: [[CALAIRE-APP]]
	  deadline:: 2026-02-18
	- TODO Testing con datos simulados (Rondas 1-4)
	  project:: [[CALAIRE-APP]]
	  deadline:: 2026-02-15
	- TODO Migrar repositorio a GitHub del grupo
	  project:: [[CALAIRE-APP]]
- **Especificaciones Técnicas**
	- Lenguaje: Python 3
	- Normativa: ISO 13528:2017
	- Cálculo: homogeneidad, estabilidad, nIQR, algoritmos robustos (A).
