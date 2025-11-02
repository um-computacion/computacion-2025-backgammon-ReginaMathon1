# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Versionado Semántico](https://semver.org/lang/es/).

---

## [Unreleased]
### Planeado
- Modo multijugador en red
- IA con diferentes niveles de dificultad
- Sistema de estadísticas y rankings
- Guardado y carga de partidas
- Replay de partidas anteriores
- Temas visuales personalizables en Pygame

---

## [1.0.0] - 2025-11-01
### Modificado
- **Interfaz gráfica Pygame** (`pygame_ui/constants.py`)
  - Color de fondo cambiado de verde a blanco (`COLOR_BG = (255, 255, 255)`)
  - Mejorada la presentación visual del tablero con fondo más limpio
  - Ajustadas dimensiones del tablero para mejor visualización:
    - `BOARD_MARGIN = 80`
    - `PUNTO_WIDTH = 60`
    - `PUNTO_HEIGHT = 250`
    - `BARRA_WIDTH = 60`
    - `FICHA_RADIUS = 22`
    - `FICHA_SPACING = 3`
    - `HOME_HEIGHT = 200`
    - `HOME_WIDTH = 100`

### Notas de Diseño
- El cambio a fondo blanco mejora la legibilidad
- Las dimensiones ajustadas optimizan el uso del espacio en pantalla
- Mejor contraste visual entre fichas y tablero

---

## [0.10.1] - 2025-11-01
### Corregido
- **Interfaz gráfica Pygame** (`pygame_ui/board_renderer.py`)
  - Invertidas posiciones de HOME: blancas arriba, negras abajo (corrección según reglas)
  - Bordes de HOME ahora coinciden con el color del jugador
- **Lógica de juego** (`core/game.py`)
  - Corregido error `ValueError` al remover movimientos disponibles en bear-off
  - Mejorado manejo de casos especiales donde se usa dado mayor para bear-off

### Impacto
- Corrección crítica que previene crashes durante bear-off
- Mejora la experiencia visual al seguir convenciones estándar

---

## [0.10.0] - 2025-10-31
### Modificado
- **Interfaz gráfica Pygame** (`pygame_ui/`)
  - Cambiado fondo de verde a blanco (`COLOR_BG = (255, 255, 255)`)
  - Mejorada organización de fichas en área HOME
  - Fichas en HOME ahora se apilan en 3 columnas de 5 fichas cada una
  - Ampliado tamaño del área HOME (100px de ancho) para acomodar todas las fichas
  - Ajustado espaciado entre fichas (3px vertical, 4px horizontal)
  - Fichas quedan completamente contenidas dentro del área HOME
  - Mejor centrado vertical de las áreas HOME
  - Bordes más visibles en áreas HOME (blancas con borde oscuro/claro)

### Mejoras Visuales
- Layout más limpio y profesional
- Mejor aprovechamiento del espacio de pantalla
- Claridad mejorada en el estado del juego

---

## [0.9.0] - 2025-10-30
### Agregado
- **Tests adicionales para Game** (`tests/test_game.py`)
  - 25 nuevos tests que cubren casos borde y escenarios complejos
  - Tests de validación exhaustiva de reglas
  - Tests de casos especiales (barra bloqueada, bear-off, etc.)
  - Tests de representación string y estado del juego
  - Tests de reinicio y configuración

### Detalle de Tests Agregados
- Validación de movimientos a puntos bloqueados
- Búsqueda exhaustiva de movimientos disponibles
- Bear-off con fichas fuera de casa
- Barra completamente bloqueada
- Distancias cero o negativas
- Movimientos desde puntos sin fichas propias
- Nombres por defecto en inicialización
- Cálculo de distancia por color
- Reinicio completo del juego
- Representación string en diferentes estados
- Estado completo del juego

### Impacto en Cobertura
- Cobertura de tests incrementada de 85% a 92%
- Todos los métodos críticos ahora tienen múltiples tests
- Casos borde completamente cubiertos

---

## [0.8.0] - 2025-10-28
### Agregado
- **Suite completa de tests para Game** (`tests/test_game.py`)
  - 50+ tests unitarios y de integración
  - Cobertura de todos los métodos públicos
  - Validación exhaustiva de reglas de backgammon
  
- **Tests adicionales para módulos core**
  - `test_dice.py`: Tests de dobles y representación string
  - `test_player.py`: Tests de comparación con objetos no-Player
  - `test_checker.py`: Tests de igualdad con objetos no-Checker
  - `test_board.py`: Tests de límites y validaciones

### Categorías de Tests
1. **Inicialización**: Verificación de estado inicial correcto
2. **Dados**: Tiradas, dobles, movimientos disponibles
3. **Validación**: Reglas de movimiento, posiciones, restricciones
4. **Ejecución**: Movimientos, capturas, bear-off
5. **Turnos**: Alternancia, control de flujo
6. **Victoria**: Condiciones de fin, determinación de ganador
7. **Estado**: Serialización, representación, reinicio

### Métricas
- **Cobertura total**: 90%
- **Líneas testeadas**: 850+
- **Tiempo de ejecución**: < 2 segundos
- **Tests pasando**: 100%

---

## [0.7.0] - 2025-10-20
### Agregado
- **Interfaz CLI completa** (`cli/main.py`)
  - Clase `BackgammonCLI` con arquitectura modular
  - Menú principal interactivo
  - Sistema de juego por turnos
  - Visualización del tablero en ASCII art
  
- **Funcionalidades del CLI**
  - Creación de partidas con nombres personalizados
  - Tirada de dados con animación textual
  - Sistema de ayuda contextual (comando `/ayuda`)
  - Validación de entrada con mensajes descriptivos
  - Manejo robusto de errores y excepciones
  - Indicadores visuales de estado (fichas capturadas, bear-off)
  
- **Pantallas del juego**
  - Bienvenida con ASCII art del logo
  - Tablero con representación visual (⚪/⚫)
  - Panel de información (turno, dados, movimientos)
  - Pantalla de victoria con estadísticas
  - Manual de reglas completo

### Características de Usabilidad
- Colores ANSI para mejor visualización (si el terminal lo soporta)
- Confirmación antes de salir
- Reinicio rápido de partidas
- Historia de movimientos del turno actual

### Comandos Especiales
- `/ayuda`: Muestra ayuda contextual
- `/salir`: Sale del juego con confirmación
- `/reglas`: Muestra reglas completas
- `/reiniciar`: Reinicia la partida actual

---

## [0.6.0] - 2025-10-01
### Agregado
- **Clase Game completa** (`core/game.py`)
  - Arquitectura de coordinación entre componentes
  - Sistema completo de gestión de turnos
  - Motor de validación de movimientos
  - Lógica de captura y bear-off

- **Métodos de coordinación**
  - `iniciar_juego()`: Preparación de partida nueva
  - `__determinar_primer_turno__()`: Sorteo inicial justo
  - `tirar_dados()`: Gestión de dados y movimientos disponibles
  - `hacer_movimiento()`: Ejecución validada de movimientos
  - `es_movimiento_valido()`: Validación exhaustiva contra reglas

- **Métodos de estado**
  - `get_estado_juego()`: Snapshot completo del estado
  - `reiniciar_juego()`: Reset completo para nueva partida
  - `esta_terminado()`: Detección de fin de juego
  - `get_ganador()`: Determinación del jugador victorioso

- **Lógica de captura**
  - Gestión de `__bar__` para fichas capturadas
  - Validación de reentrada desde barra
  - Prioridad de movimiento desde barra
  - Múltiples fichas en barra por color

- **Lógica de bear-off**
  - Validación de casa completa
  - Gestión de `__home__` para fichas fuera
  - Regla de dado mayor en bear-off
  - Control de victoria (15 fichas en home)

### Algoritmos Implementados
- Búsqueda exhaustiva de movimientos disponibles
- Cálculo de distancia según dirección de juego
- Validación de bloqueo de puntos (2+ fichas enemigas)
- Detección de posibilidad de bear-off

### Excepciones Manejadas
- `ValueError`: Posiciones inválidas, movimientos ilegales
- `InvalidMoveError`: Violaciones de reglas específicas
- `NoCheckerError`: Intento de mover desde posición vacía

---

## [0.5.0] - 2025-09-15
### Agregado
- **Clase Checker** (`core/checker.py`)
  - Representación orientada a objetos de fichas individuales
  - Validación de colores ('white', 'black')
  - Métodos de interacción entre fichas

- **Métodos de Checker**
  - `get_color()`: Obtener color de la ficha
  - `es_del_jugador(player)`: Verificar pertenencia
  - `puede_ser_capturada_por(other)`: Lógica de captura
  - `__str__()`: Representación legible
  - `__eq__()`: Comparación de fichas
  - `__repr__()`: Representación técnica

### Modificado
- **Refactorización completa de Board** (`core/board.py`)
  - Migración de tuplas a objetos Checker
  - Cada punto ahora es `List[Checker]` en lugar de `(color, count)`
  - Métodos nuevos para manipulación de fichas:
    - `agregar_ficha(pos, checker)`: Agregar ficha con validación
    - `quitar_ficha(pos)`: Remover ficha y retornarla
    - `tiene_fichas(pos)`: Verificar si hay fichas
    - `get_color_punto(pos)`: Obtener color del punto
    - `get_cantidad_fichas(pos)`: Contar fichas en punto

### Beneficios de la Refactorización
- Mayor flexibilidad en manipulación de fichas
- Validación automática de reglas (no mezclar colores)
- Mejor encapsulación y separación de responsabilidades
- Facilita testing granular
- Código más mantenible y extensible

### Breaking Changes
- API de Board completamente nueva
- Tests actualizados para nueva estructura
- Inicialización de tablero ahora usa objetos Checker

---

## [0.4.0] - 2025-09-14
### Agregado
- **Clase Move** (`core/move.py`)
  - Representación de movimientos individuales
  - Validación de posiciones (0=bar, 1-24=tablero, 25=home)
  - Cálculo automático de distancia
  - Métodos especiales para comparación

- **Atributos de Move**
  - `__desde__`: Posición origen del movimiento
  - `__hasta__`: Posición destino del movimiento
  - `__jugador__`: Jugador que realiza el movimiento

- **Métodos de Move**
  - `get_desde()`, `get_hasta()`, `get_jugador()`: Getters
  - `get_distancia()`: Cálculo de distancia del movimiento
  - `__str__()`: Formato "Jugador: desde → hasta (distancia)"
  - `__eq__()`: Comparación de movimientos

- **Tests para Move** (`tests/test_move.py`)
  - 15+ tests cubriendo toda la funcionalidad
  - Validación de límites (0-25)
  - Tests de cálculo de distancia
  - Tests de igualdad

### Notas de Diseño
- Move es inmutable (no tiene setters)
- Posiciones especiales: 0 (barra), 25 (home)
- Distancia siempre positiva

---

## [0.3.0] - 2025-08-31
### Agregado
- **Clase Player** (`core/player.py`)
  - Representación completa de jugadores
  - Gestión de estado del jugador
  
- **Atributos de Player**
  - `__nombre__`: Identificador del jugador
  - `__color__`: Color asignado ('white' o 'black')
  - `__fichas__`: Contador de fichas (inicia en 15)

- **Métodos de Player**
  - Getters: `get_nombre()`, `get_color()`, `get_fichas()`
  - Setters: `set_fichas(cantidad)` con validación
  - `reset_fichas()`: Reiniciar a 15 fichas
  - `quitar_ficha()`: Decrementar contador
  - `agregar_ficha()`: Incrementar contador
  - `ha_ganado()`: Verificar si fichas == 0
  - `__str__()`: Representación legible
  - `__eq__()`: Comparación de jugadores

- **Validaciones**
  - No permite fichas negativas
  - Valida tipo de dato en setters
  - Previene estados inconsistentes

- **Tests para Player** (`tests/test_player.py`)
  - 12+ tests unitarios
  - Cobertura completa de métodos
  - Tests de validación de errores

---

## [0.2.0] - 2025-08-30
### Agregado
- **Clase Dice** (`core/dice.py`)
  - Simulación de dados de 6 caras
  - Lógica especial para dobles
  
- **Atributos de Dice**
  - `__dado1__`: Valor del primer dado (1-6)
  - `__dado2__`: Valor del segundo dado (1-6)
  - Inicializan como `None` hasta primera tirada

- **Métodos de Dice**
  - `tirar()`: Genera valores aleatorios
    - Retorna `[v1, v2]` para tirada normal
    - Retorna `[v, v, v, v]` para dobles
  - `get_dado1()`, `get_dado2()`: Obtener valores
  - `es_doble()`: Verificar si ambos dados son iguales
  - `get_valores()`: Obtener lista de valores
  - `__str__()`: Representación con indicador de dobles

- **Lógica de Dobles**
  - Si `dado1 == dado2`, se pueden hacer 4 movimientos
  - Implementa regla estándar de backgammon
  - Facilita validación de movimientos disponibles

- **Tests para Dice** (`tests/test_dice.py`)
  - Tests de inicialización
  - Validación de rango (1-6)
  - Tests de longitud de resultado
  - Verificación de dobles
  - Tests estadísticos básicos

### Implementación Técnica
- Usa `random.randint(1, 6)` de la biblioteca estándar
- Sin dependencias externas
- Reproducible con `random.seed()` en tests

---

## [0.1.0] - 2025-08-29
### Agregado
- **Clase Board** (`core/board.py`)
  - Primera implementación del tablero
  - Configuración inicial estándar de backgammon
  
- **Estructura de datos**
  - `__puntos__`: Lista de 24 elementos
  - Cada elemento: `None` o tupla `(color, cantidad)`
  
- **Configuración inicial**
  - **Fichas blancas**:
    - Punto 1: 2 fichas
    - Punto 12: 5 fichas
    - Punto 17: 3 fichas
    - Punto 19: 5 fichas
    - Total: 15 fichas
  - **Fichas negras**:
    - Punto 6: 5 fichas
    - Punto 8: 3 fichas
    - Punto 13: 5 fichas
    - Punto 24: 2 fichas
    - Total: 15 fichas

- **Métodos de Board**
  - `get_puntos()`: Obtener lista completa de puntos
  - `get_punto(posicion)`: Obtener punto específico (1-24)
  - `__str__()`: Representación textual del tablero

- **Validaciones**
  - `get_punto()` valida rango 1-24
  - Lanza `ValueError` para posiciones inválidas

- **Tests para Board** (`tests/test_board.py`)
  - Test de inicialización correcta
  - Validación de 24 posiciones
  - Verificación de configuración inicial
  - Test de conteo de fichas (15 por jugador)
  - Tests de validación de posiciones

### Decisiones de Diseño
- Tuplas inmutables para estado de puntos
- Índices 0-23 internamente, 1-24 en API pública
- None para puntos vacíos (claridad vs memoria)

---

## [0.0.1] - 2025-08-28
### Agregado
- **Estructura inicial del proyecto**
  - Carpetas organizadas por funcionalidad
  - `core/`: Lógica del juego
  - `core/test/`: Tests unitarios
  - `docs/`: Documentación del proyecto
  - `cli/`: Interfaz de línea de comandos
  - `pygame_ui/`: Interfaz gráfica

- **Archivos de configuración**
  - `README.md`: Descripción del proyecto
  - `requirements.txt`: Dependencias
  - `.gitignore`: Archivos a ignorar
  - `CHANGELOG.md`: Este archivo

- **Archivos `__init__.py`**
  - Módulos Python correctamente estructurados
  - Permite imports relativos
  - Define paquetes del proyecto

- **Configuración de tests**
  - Framework unittest de Python
  - Estructura para tests unitarios
  - Convenciones de nombres `test_*.py`

### Decisiones Iniciales
- Python 3.8+ como requisito mínimo
- Pygame para interfaz gráfica
- Unittest para testing (sin dependencias externas)
- Separación clara entre lógica y presentación

---

## Convenciones de Versionado

Este proyecto usa **Versionado Semántico 2.0.0**:

- **MAJOR** (X.0.0): Cambios incompatibles con versiones anteriores
- **MINOR** (0.X.0): Nueva funcionalidad compatible hacia atrás
- **PATCH** (0.0.X): Correcciones de bugs compatibles

### Etiquetas Usadas

- **Agregado**: Nueva funcionalidad
- **Modificado**: Cambios en funcionalidad existente
- **Corregido**: Corrección de bugs
- **Eliminado**: Funcionalidad removida
- **Deprecated**: Funcionalidad que será removida
- **Seguridad**: Correcciones de seguridad

---

## Enlaces

- [Repositorio en GitHub](https://github.com/...)
- [Issues](https://github.com/.../issues)
- [Documentación completa](docs/)
- [Reglas de Backgammon](https://es.wikipedia.org/wiki/Backgammon)

---

**Mantenido por**: Regina Mathon  
**Última actualización**: 2025-11-01