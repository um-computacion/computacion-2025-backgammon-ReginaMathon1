# Justificación del Proyecto Backgammon

## 1. Resumen del Diseño General

El proyecto implementa el juego de Backgammon siguiendo una arquitectura en capas que separa completamente la lógica de negocio de las interfaces de usuario. El diseño se basa en los siguientes principios:

- **Separación de responsabilidades**: Cada componente tiene una función específica y bien definida
- **Independencia de la interfaz**: La lógica central (core/) puede ser utilizada por cualquier tipo de interfaz (CLI, Pygame, web, etc.)
- **Modularidad**: Los componentes son independientes y pueden ser probados y modificados sin afectar otros módulos
- **Orientación a objetos pura**: Todo el código sigue el paradigma POO sin componentes procedurales

### Flujo de Ejecución

1. El jugador inicia el juego desde CLI o Pygame
2. La interfaz crea una instancia de `BackgammonGame`
3. `BackgammonGame` inicializa el `Board`, los dos `Player` y el `Dice`
4. En cada turno:
   - El jugador tira los dados
   - Selecciona fichas y destinos para mover
   - El sistema valida los movimientos según las reglas
   - Se actualiza el estado del tablero
   - Se verifica la condición de victoria

## 2. Justificación de Clases Elegidas

### 2.1. Clase Checker (`core/checker.py`)

**Responsabilidad**: Representar y gestionar una ficha individual del juego.

**Justificación**: 
- Cada ficha tiene un color específico que la identifica con un jugador
- Las fichas pueden ser capturadas y deben llevar control de su estado
- Encapsula la lógica específica de interacción entre fichas (captura)
- Permite validar pertenencia a jugadores de forma clara

**Métodos principales**:
- `__init__(__color__)`: Inicializa la ficha con su color
- `belongs_to(__player__)`: Verifica si pertenece a un jugador específico
- `can_capture(__other__)`: Determina si puede capturar otra ficha

### 2.2. Clase Board (`core/board.py`)

**Responsabilidad**: Mantener y gestionar el estado completo del tablero de juego.

**Justificación**:
- El tablero es el elemento central que contiene toda la información del estado del juego
- Gestiona los 24 puntos, la barra y las zonas de bear-off
- Implementa las reglas estructurales del backgammon (no mezclar colores, orden de movimiento)
- Provee métodos para consultar y modificar posiciones de fichas

**Estructura de datos**:
- `__points__`: Lista de 24 posiciones, cada una conteniendo una lista de fichas
- `__bar__`: Diccionario con fichas capturadas por color
- `__off__`: Diccionario con fichas sacadas del tablero por color

### 2.3. Clase Player (`core/player.py`)

**Responsabilidad**: Representar a un jugador y su estado en la partida.

**Justificación**:
- Necesitamos distinguir entre los dos jugadores
- Cada jugador tiene un color asignado que determina sus fichas
- Mantenemos información del estado (nombre, fichas disponibles)
- Facilita la verificación de condiciones de victoria

**Atributos clave**:
- `__name__`: Identificador del jugador
- `__color__`: Color de las fichas del jugador
- `__checkers_count__`: Cantidad de fichas en juego

### 2.4. Clase Dice (`core/dice.py`)

**Responsabilidad**: Simular la tirada de dados y gestionar los valores disponibles.

**Justificación**:
- Los dados son un componente esencial del backgammon
- Manejo especial de dobles (4 movimientos en lugar de 2)
- Encapsula la lógica de números aleatorios
- Mantiene el control de dados usados/disponibles durante un turno

**Características especiales**:
- Detección automática de dobles
- Gestión de movimientos disponibles

### 2.5. Clase Game (`core/game.py`)

**Responsabilidad**: Coordinar el flujo general del juego y aplicar las reglas globales.

**Justificación**:
- Necesitamos un controlador central que orqueste todos los componentes
- Gestiona los turnos entre jugadores
- Aplica las reglas de movimiento y validaciones
- Determina el ganador de la partida
- Punto de entrada único para las interfaces

**Métodos de coordinación**:
- `__init__()`: Inicializa todos los componentes del juego
- `roll_dice()`: Gestiona la tirada de dados
- `move_checker(__from__, __to__)`: Coordina movimientos validando reglas
- `get_winner()`: Verifica condición de victoria

## 3. Justificación de Atributos

Todos los atributos siguen la convención de doble guión bajo (`__atributo__`) como se requiere en las especificaciones del proyecto.

### Board
- `__points__`: Lista necesaria para representar los 24 triángulos del tablero
- `__bar__`: Diccionario para gestionar fichas capturadas por color
- `__off__`: Diccionario para fichas que han salido del tablero
- Estructura elegida: Listas para permitir múltiples fichas por punto, diccionarios para acceso rápido por color

### Player
- `__name__`: String para identificación humana del jugador
- `__color__`: Constante que vincula al jugador con sus fichas
- `__checkers_count__`: Entero para tracking rápido de fichas en juego

### Checker
- `__color__`: Único atributo necesario, define la identidad de la ficha

### Dice
- `__values__`: Lista de enteros con los valores de la última tirada
- `__available__`: Lista de valores aún no utilizados en el turno actual

### Game
- `__board__`: Instancia de Board, el estado central del juego
- `__players__`: Lista de dos Player objects
- `__dice__`: Instancia de Dice compartida
- `__current_player__`: Índice del jugador activo

## 4. Decisiones de Diseño Relevantes

### 4.1. Separación Core vs Interfaces

**Decisión**: Mantener la lógica del juego completamente independiente de las interfaces.

**Razones**:
- Permite implementar múltiples interfaces (CLI, Pygame, web) sin duplicar código
- Facilita el testing de la lógica sin dependencias gráficas
- Cumple con el principio de responsabilidad única (SOLID)
- Permite reutilizar el core en diferentes contextos

**Alternativas descartadas**:
- Mezclar lógica y presentación: Descartada por violar SOLID y dificultar testing
- UI como parámetro del Game: Descartada por crear acoplamiento innecesario

### 4.2. Estructura de Datos del Tablero

**Decisión**: Usar lista de listas para los puntos del tablero.

**Razones**:
- Refleja la estructura física del backgammon (24 puntos secuenciales)
- Permite apilar múltiples fichas en un punto
- Facilita la iteración y validación de movimientos
- Orden natural para cálculos de distancia

**Alternativas descartadas**:
- Diccionario de posiciones: Descartado por no reflejar el orden secuencial
- Matriz 2D: Descartado por no representar la naturaleza unidimensional del tablero

### 4.3. Validación de Movimientos

**Decisión**: Validación en múltiples capas (Checker, Board, Game).

**Razones**:
- Checker valida interacciones entre fichas
- Board valida reglas estructurales del tablero
- Game valida reglas del flujo (turnos, dados)
- Separación de concerns facilita mantenimiento

### 4.4. Manejo de Estado de Dados

**Decisión**: Clase Dice gestiona sus propios valores disponibles.

**Razones**:
- Encapsula la complejidad de dobles (4 movimientos)
- Simplifica la lógica en Game
- Facilita el tracking de dados usados

## 5. Excepciones y Manejo de Errores

### 5.1. Excepciones Definidas

```python
class InvalidMoveError(Exception):
    """Movimiento inválido según las reglas del juego"""
    pass

class InvalidColorError(Exception):
    """Color de ficha inválido"""
    pass

class NoCheckerError(Exception):
    """No hay ficha en la posición especificada"""
    pass

class InvalidPositionError(Exception):
    """Posición fuera de rango del tablero"""
    pass
```

### 5.2. Justificación de Excepciones

**InvalidMoveError**: 
- Se lanza cuando se intenta un movimiento que viola las reglas
- Casos: mover ficha de otro jugador, punto ocupado por oponente, valor de dado no disponible
- Permite a las interfaces informar al usuario de forma específica

**InvalidColorError**:
- Se lanza al crear Checker con color no válido
- Previene estados inconsistentes en el juego
- Validación temprana de datos

**NoCheckerError**:
- Se lanza al intentar mover desde posición vacía
- Evita errores de referencia nula
- Facilita debugging

**InvalidPositionError**:
- Se lanza al acceder a posiciones fuera de rango (< 0 o >= 24)
- Previene IndexError en listas
- Mejora claridad de errores

### 5.3. Estrategia de Manejo

- Validación preventiva: Se verifican condiciones antes de realizar cambios de estado
- Excepciones específicas: Cada error tiene su tipo para manejo granular
- Propagación controlada: Las excepciones se capturan en las interfaces para mostrar mensajes al usuario
- Estado consistente: Las operaciones son atómicas (todo o nada)

## 6. Estrategias de Testing y Cobertura

### 6.1. Estructura de Tests

```
tests/
├── test_checker.py    → Tests unitarios de Checker
├── test_board.py      → Tests unitarios de Board
├── test_player.py     → Tests unitarios de Player
├── test_dice.py       → Tests unitarios de Dice
├── test_game.py       → Tests de integración de Game
└── test_rules.py      → Tests de reglas específicas
```

### 6.2. Casos de Prueba Principales

**test_checker.py**:
- Creación de fichas con colores válidos
- Validación de colores inválidos (excepción)
- Pertenencia a jugadores
- Lógica de captura entre fichas

**test_board.py**:
- Configuración inicial correcta (posiciones estándar)
- Movimientos básicos de fichas
- Validación de reglas de puntos (no mezclar colores)
- Gestión de barra (fichas capturadas)
- Bear-off (sacar fichas)

**test_player.py**:
- Creación de jugadores
- Asignación de colores
- Conteo de fichas

**test_dice.py**:
- Generación de valores (rango 1-6)
- Detección de dobles
- Gestión de valores disponibles

**test_game.py**:
- Inicialización completa del juego
- Flujo de turnos
- Validación de movimientos completos
- Condiciones de victoria
- Secuencias de juego reales

### 6.3. Cobertura Objetivo

- **Meta**: 90% de cobertura mínima (según requisitos)
- **Actual**: Se mide con `coverage.py`
- **Comando**: `coverage run -m unittest discover && coverage report`

### 6.4. Qué se Probó y Por Qué

1. **Lógica de negocio completa**: Es el core del juego, debe ser 100% confiable
2. **Validaciones de reglas**: Garantiza que no se permiten movimientos ilegales
3. **Casos borde**: Situaciones límite (tablero vacío, todos en barra, etc.)
4. **Excepciones**: Verifica que se lanzan en las condiciones correctas
5. **Integración**: Asegura que los componentes funcionan juntos correctamente

**No se probó extensivamente**:
- Interfaces (CLI/Pygame): Son capas de presentación, la lógica está en core
- Generación aleatoria específica de Dice: Se mockea en tests para reproducibilidad

## 7. Cumplimiento de Principios SOLID

### 7.1. Single Responsibility Principle (SRP)

✅ **Cumplido**: Cada clase tiene una única responsabilidad claramente definida.

- `Checker`: Solo gestiona fichas individuales
- `Board`: Solo gestiona el estado del tablero
- `Player`: Solo representa información del jugador
- `Dice`: Solo gestiona generación y tracking de dados
- `Game`: Solo coordina el flujo del juego

**Evidencia**: Ninguna clase mezcla responsabilidades. Por ejemplo, Board no sabe de turnos ni jugadores, solo de posiciones de fichas.

### 7.2. Open/Closed Principle (OCP)

✅ **Cumplido**: El sistema está abierto a extensión pero cerrado a modificación.

**Ejemplos**:
- Nuevas interfaces (web, mobile) pueden agregarse sin modificar core
- Nuevas reglas (variantes de backgammon) pueden implementarse extendiendo Game
- Validaciones adicionales pueden agregarse sin cambiar la estructura base

**Implementación**:
- Uso de herencia donde apropiado
- Métodos públicos bien definidos como API estable
- Lógica interna protegida

### 7.3. Liskov Substitution Principle (LSP)

✅ **Cumplido**: Las subclases (si existieran) pueden sustituir a sus clases base.

**Aplicación**:
- Todas las instancias de Checker son intercambiables
- Cualquier implementación de interfaz (CLI, Pygame) puede usar Game de la misma forma
- No hay comportamientos sorpresivos en jerarquías

### 7.4. Interface Segregation Principle (ISP)

✅ **Cumplido**: Las interfaces son específicas y no obligan a implementar métodos innecesarios.

**Evidencia**:
- Game expone solo los métodos necesarios para jugar
- Board expone solo operaciones relevantes al tablero
- Las interfaces (CLI/Pygame) solo usan los métodos que necesitan

### 7.5. Dependency Inversion Principle (DIP)

✅ **Cumplido**: Las dependencias apuntan hacia abstracciones, no hacia detalles.

**Implementación**:
- Game depende de las abstracciones Board, Player, Dice (no de implementaciones específicas)
- Las interfaces dependen de Game (la abstracción) no de detalles internos
- Ningún módulo de alto nivel depende de módulos de bajo nivel directamente

## 8. Anexos

### 8.1. Diagrama de Clases UML

```
┌─────────────────┐
│  BackgammonGame │
├─────────────────┤
│ __board__       │
│ __players__     │
│ __dice__        │
│ __current__     │
├─────────────────┤
│ roll_dice()     │
│ move_checker()  │
│ get_winner()    │
└────────┬────────┘
         │
         │ uses
         ├──────────────┬──────────────┬─────────────┐
         │              │              │             │
         ▼              ▼              ▼             ▼
┌────────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
│   Board    │  │  Player  │  │   Dice   │  │ Checker  │
├────────────┤  ├──────────┤  ├──────────┤  ├──────────┤
│ __points__ │  │ __name__ │  │ __values__│  │ __color__│
│ __bar__    │  │ __color__│  │ __avail__│  └──────────┘
│ __off__    │  └──────────┘  └──────────┘       ▲
├────────────┤                                    │
│ move()     │                            contains
│ get_point()│                                    │
│ is_valid() │────────────────────────────────────┘
└────────────┘

         ▲
         │
         │ uses
         │
┌────────┴────────┬──────────────┐
│                 │              │
┌─────────┐  ┌────────────┐  ┌────────────┐
│   CLI   │  │  PygameUI  │  │   Redis    │
└─────────┘  └────────────┘  └────────────┘
(Interfaces)
```

### 8.2. Diagrama de Flujo de Juego

```
[Inicio] → [Inicializar Game] → [Configurar Board]
                ↓
         [Jugador tira dados]
                ↓
         [Selecciona movimiento] ←──────┐
                ↓                       │
         [Validar movimiento]           │
                ↓                       │
            ¿Válido?                    │
           /        \                   │
         Sí          No                 │
         ↓           ↓                  │
    [Ejecutar]  [Mostrar error]        │
         ↓                              │
    ¿Más dados?                         │
         ↓                              │
        Sí ─────────────────────────────┘
         │
        No
         ↓
    ¿Ganador?
         ↓
        Sí → [Fin]
         │
        No
         ↓
    [Cambiar turno] ──→ [Jugador tira dados]
```

### 8.3. Ejemplo de Configuración Inicial del Tablero

```
Punto:  24 23 22 21 20 19    18 17 16 15 14 13
        ─────────────────    ─────────────────
Blancas: 2              5     3
Negras:              5        5                3  2

Punto:   1  2  3  4  5  6     7  8  9 10 11 12
        ─────────────────    ─────────────────
```

## 9. Evolución del Proyecto

Este documento se actualiza en cada sprint para reflejar:
- Nuevas decisiones de diseño
- Refactorizaciones realizadas
- Lecciones aprendidas
- Cambios en la arquitectura

### Versión 1.0 (Sprint 1)
- Diseño inicial de clases core
- Implementación básica de Board y Checker

### Versión 2.0 (Sprint 2)
- Integración de Game como coordinador
- Implementación de reglas de movimiento
- Primera versión de CLI

### Versión 3.0 (Sprint 3)
- Implementación completa de reglas de backgammon
- Testing con >90% cobertura
- Interfaz Pygame funcional

---

**Última actualización**: [2020-10-31]
**Autor**: [Regina Mathon]
**Repositorio**: computacion-2025-backgammon-ReginaMathon1
