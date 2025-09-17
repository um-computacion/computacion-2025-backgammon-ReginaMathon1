# Backgammon - Regina Mathon

## Descripción
Implementación del juego Backgammon en Python con arquitectura orientada a objetos.

## Estructura del Proyecto

### Core (`core/`)
- **`checker.py`**: Lógica de fichas individuales
- **`board.py`**: Tablero de juego con 24 puntos
- **`player.py`**: Información y estado de jugadores
- **`dice.py`**: Generación de dados con manejo de dobles
- **`game.py`**: Coordinación del juego completo

### Tests (`core/test/`)
- Tests unitarios para cada clase principal
- Cobertura completa de funcionalidades

### Interfaces
- **`cli/`**: Interfaz de línea de comandos (futuro)
- **`pygame_ui/`**: Interfaz gráfica con Pygame (futuro)

## Características Principales

### Arquitectura Modular
- Separación clara de responsabilidades
- Cada clase tiene una función específica
- Fácil mantenimiento y extensión

### Validaciones
- Colores de fichas válidos ('white', 'black')
- Posiciones de tablero válidas (1-24)
- Reglas de backgammon implementadas

### Testing
- Tests unitarios completos
- Validación de casos límite
- Integración con GitHub Actions

## Uso

```bash
# Ejecutar tests
python3 -m unittest discover core/test/

# Ejecutar test específico
python3 core/test/test_checker.py
```

## Desarrollo
Proyecto desarrollado siguiendo metodología incremental con commits frecuentes y documentación detallada.