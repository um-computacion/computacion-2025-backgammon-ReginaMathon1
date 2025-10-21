# Changelog

## [0.7.0] - 2025-10-20
### Agregado
- **Interfaz CLI** (`cli/main.py`)
  - Clase `BackgammonCLI` para manejar la interfaz de línea de comandos
  - Menú principal con opciones: Nueva Partida, Ver Reglas, Salir
  - Sistema completo de juego con turnos y movimientos
  - Visualización del tablero en formato texto
  - Indicadores de fichas capturadas (barra) y fichas sacadas (casa)
  - Sistema de ayuda interactivo durante el juego
  - Validación de entrada del usuario
  - Manejo de excepciones y errores
  - Pantalla de bienvenida y resultado final
  - Representación visual con símbolos: ⚪ (blancas), ⚫ (negras)
- **Funcionalidad de movimientos**
  - Sistema de tirada de dados con visualización
  - Validación de movimientos según reglas de backgammon
  - Manejo de fichas en la barra (capturadas)
  - Sistema de "bear off" (sacar fichas)
  - Detección automática de movimientos disponibles
- **Documentación de juego**
  - Pantalla de reglas completas del backgammon
  - Ayuda contextual durante los movimientos
  - Instrucciones de dirección de movimiento para cada color

## [0.6.0] - 2025-10-01
### Agregado
- **Clase Game completa** (`core/game.py`)
  - Atributos: `__board__`, `__players__`, `__dice__`, `__turno__`, `__ultimo_roll__`
  - Atributos adicionales: `__movimientos_disponibles__`, `__bar__`, `__home__`
  - Método `iniciar_juego()` para preparar una nueva partida
  - Método `__determinar_primer_turno__()` para sorteo inicial
  - Getters para todos los atributos del juego
  - Método `cambiar_turno()` para alternar entre jugadores
  - Método `tirar_dados()` con actualización de movimientos disponibles
  - Método `hacer_movimiento()` para ejecutar movimientos válidos
  - Método `es_movimiento_valido()` con validación completa de reglas
  - Método `__calcular_distancia__()` según color del jugador
  - Método `tiene_movimientos_disponibles()` para verificar jugabilidad
  - Método `__puede_bear_off__()` para validar salida de fichas
  - Métodos de finalización: `esta_terminado()`, `get_ganador()`
  - Método `get_estado_juego()` para obtener snapshot del estado
  - Método `reiniciar_juego()` para comenzar nueva partida
  - Método especial `__str__()` para representación del estado
- **Lógica de captura**
  - Manejo de fichas capturadas en `__bar__`
  - Validación de reentrada desde la barra
  - Obligación de mover fichas de la barra antes que otras
- **Lógica de bear off**
  - Validación de casa completa antes de sacar fichas
  - Manejo de fichas sacadas en `__home__`
  - Control de victoria (15 fichas en home)

## [0.6.0] - 2025-09-16
### Agregado
- **Nuevas funcionalidades para el proyecto**
  - Completar clase game 

## [0.5.0] - 2025-09-15
### Agregado
- **Clase Checker** (`core/checker.py`)
  - Atributo: `__color__` (validado como 'white' o 'black')
  - Métodos de información: `get_color()`
  - Métodos de lógica de juego: `es_del_jugador()`, `puede_ser_capturada_por()`
  - Validación de colores en constructor
  - Métodos especiales: `__str__()`, `__eq__()`, `__repr__()`
### Modificado
- **Clase Board** (`core/board.py`)
  - Refactorizada para usar objetos Checker en lugar de tuplas
  - Cada punto ahora contiene una lista de objetos Checker
  - Nuevos métodos: `tiene_fichas()`, `get_color_punto()`, `get_cantidad_fichas()`
  - Nuevos métodos: `agregar_ficha()`, `quitar_ficha()`
  - Validación para evitar mezclar colores en un punto
  - Separación clara de responsabilidades: Board maneja tablero, Checker maneja fichas

## [0.4.0] - 2025-09-14
### Agregado
- **Clase Game** (`core/game.py`)
  - Atributos: `__tablero__`, `__jugador1__`, `__jugador2__`, `__jugador_actual__`, `__dados__`, `__estado__`
  - Estado inicial: "esperando_dados"
  - Métodos de configuración: `get_tablero()`, `get_jugador1()`, `get_jugador2()`, `get_jugador_actual()`, `get_dados()`, `get_estado()`
  - Métodos de juego: `tirar_dados()`, `cambiar_turno()`, `hacer_movimiento()`, `es_movimiento_valido()`, `juego_terminado()`
  - Validaciones de movimientos según reglas de backgammon
  - Manejo de estados del juego
  - Métodos especiales: `__str__()`
- **Clase Move** (`core/move.py`)
  - Atributos: `__desde__`, `__hasta__`, `__jugador__`
  - Validación de posiciones (0-25, donde 0=bar, 25=home)
  - Métodos: `get_desde()`, `get_hasta()`, `get_jugador()`, `get_distancia()`
  - Cálculo automático de distancia del movimiento
  - Métodos especiales: `__str__()`, `__eq__()`
- **Tests para Game** (`core/test/test_game.py`)
  - Tests de inicialización de todos los atributos
  - Validación de configuración inicial del juego
  - Tests de tirada de dados y cambio de estado
  - Tests de cambio de turno entre jugadores
  - Tests de validación de movimientos
  - Tests de detección de fin de juego
- **Tests para Move** (`core/test/test_move.py`)
  - Tests de inicialización de atributos
  - Validación de posiciones válidas (0-25)
  - Tests de cálculo de distancia
  - Tests de igualdad entre movimientos
  - Validación de representación string

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