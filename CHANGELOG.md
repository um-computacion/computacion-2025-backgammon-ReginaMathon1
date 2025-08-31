# Changelog

## [0.3.0] - 2025-08-31
### Agregado
- **Clase Player** (`core/player.py`)
  - Atributos: `__nombre__`, `__color__`, `__fichas__` (inicia en 15)
  - Métodos: `get_nombre()`, `get_color()`, `get_fichas()`, `set_fichas()`
  - Método `reset_fichas()` para reiniciar fichas a 15
  - Métodos de juego: `quitar_ficha()`, `agregar_ficha()`, `ha_ganado()`
  - Métodos especiales: `__str__()`, `__eq__()`
- **Tests para Player** (`core/test/test_player.py`)
  - Tests para todos los atributos y métodos
  - Validación de valores negativos en `set_fichas()`
  - Tests de igualdad entre jugadores

## [0.2.0] - 2025-08-30
### Agregado
- **Clase Dice** (`core/dice.py`)
  - Atributos: `__dado1__`, `__dado2__` (inician como None)
  - Método `tirar()` que genera números aleatorios 1-6
  - Manejo de dobles: si ambos dados iguales, retorna 4 valores
  - Métodos auxiliares: `get_dado1()`, `get_dado2()`, `es_doble()`, `get_valores()`
  - Representación string con indicador de dobles
- **Tests para Dice** (`core/test/test_dice.py`)
  - Tests de inicialización de atributos
  - Validación de valores después de tirar
  - Tests de longitud correcta del resultado (2 o 4 valores)
  - Validación de rango de valores (1-6)

## [0.1.0] - 2025-08-29
### Agregado
- **Clase Board** (`core/board.py`)
  - Atributo `__puntos__` con 24 posiciones inicializadas
  - Configuración inicial estándar de backgammon:
    - Fichas blancas: puntos 1(2), 12(5), 17(3), 19(5)
    - Fichas negras: puntos 6(5), 8(3), 13(5), 24(2)
  - Métodos: `get_puntos()`, `get_punto(posicion)`, `__str__()`
  - Validación de posiciones (1-24)
- **Tests para Board** (`core/test/test_board.py`)
  - Test de inicialización de atributo `__puntos__`
  - Validación de posiciones iniciales de fichas
  - Verificación de conteo total (15 fichas por jugador)

## [0.1.0] - 2025-08-28
### Estructura del Proyecto
- Creada estructura de carpetas:
  - `core/` - Lógica principal del juego
  - `core/test/` - Tests unitarios
  - `docs/` - Documentación
  - `cli/` - Interfaz de línea de comandos
  - `pygame_ui/` - Interfaz gráfica
- Archivos `__init__.py` para módulos Python
- Configuración inicial de tests con unittest

## [0.1.0] - 2025-08-28
### Notas Técnicas
- Todos los tests ejecutables con `python3 core/test/test_*.py`
- Implementación siguiendo reglas estándar de backgammon
- Atributos privados con doble guión bajo (`__atributo__`)
- Documentación con docstrings en español