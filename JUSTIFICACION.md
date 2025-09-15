# Justificación del Proyecto Backgammon

## Arquitectura del Sistema

### Separación de Responsabilidades

El proyecto sigue el principio de responsabilidad única, donde cada clase tiene una función específica y bien definida:

#### Clase Checker (`core/checker.py`)
**Responsabilidad**: Lógica específica de las fichas
- Gestión del color de la ficha
- Verificación de pertenencia a jugadores
- Lógica de captura entre fichas
- Validación de colores válidos

#### Clase Board (`core/board.py`)
**Responsabilidad**: Lógica del tablero de juego
- Estructura de 24 puntos del tablero
- Configuración inicial de posiciones
- Gestión de movimiento de fichas entre puntos
- Validación de reglas del tablero (no mezclar colores)

#### Clase Player (`core/player.py`)
**Responsabilidad**: Información y estado del jugador
- Datos del jugador (nombre, color)
- Conteo de fichas disponibles
- Estado de victoria

#### Clase Dice (`core/dice.py`)
**Responsabilidad**: Generación de números aleatorios
- Simulación de dados de 6 caras
- Manejo especial de dobles en backgammon

#### Clase Game (`core/game.py`)
**Responsabilidad**: Coordinación del juego completo
- Inicialización de partidas
- Control de turnos
- Aplicación de reglas generales

### Beneficios de esta Arquitectura

1. **Mantenibilidad**: Cada clase es independiente y puede modificarse sin afectar otras
2. **Testabilidad**: Cada componente puede probarse de forma aislada
3. **Reutilización**: Las clases pueden usarse en diferentes contextos
4. **Claridad**: El código es más fácil de entender y documentar
5. **Extensibilidad**: Nuevas funcionalidades se pueden agregar sin romper el código existente
