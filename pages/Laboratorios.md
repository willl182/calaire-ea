- tags:: [[MOC]], [[Database]]
- # Registro de Laboratorios Participantes
- Este MOC centraliza el registro de todos los laboratorios participantes en las rondas de Ensayo de Aptitud del proyecto CALAIRE-EA.
- ## Laboratorios Confirmados
    - [[Universidad de Medellín]]
- ## Laboratorios Contactados
    - [[Universidad Pontificia Bolivariana]]
- ## Candidatos
    - [[SIATA]]
- ## Plantilla para Nuevos Laboratorios

Cada laboratorio debe tener su propia página individual con la siguiente estructura:

```
- tags:: [[Laboratorio]]
- # Nombre del Laboratorio
  type:: [[Laboratorio]]
  status:: #confirmado | #contactado | #candidato | #inactivo
  institution:: Nombre de la institución
  location:: Ciudad
- ## Participación en Rondas EA
    - [[Ronda 1]]: #confirmado | #pendiente
    - [[Ronda 2]]: #confirmado | #pendiente
    - [[Ronda 3]]: #confirmado | #pendiente
    - [[Ronda 4]]: #confirmado | #pendiente
    - [[Ronda 5]]: #confirmado | #pendiente
- ## Equipos
    - CO: [[Analizador Modelo X]]
    - NOx: [[Analizador Modelo Y]]
    - SO2: [[Analizador Modelo Z]]
    - O3: [[Analizador Modelo W]]
- ## Observaciones
    - 
- ## Documentación
    - 
```

## Estatus de Laboratorio

| Status | Significado |
|--------|-------------|
| `#confirmado` | Ha confirmado participación explícita |
| `#contactado` | Se ha enviado carta/invitación oficial |
| `#candidato` | En lista de posibles participantes |
| `#inactivo` | Participó anteriormente pero no en esta ronda |

## Trazabilidad

Para seguimiento de confirmaciones por ronda, referirse a [[Prueba Piloto]].
