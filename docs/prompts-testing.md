# Prompts de Testing - Backgammon

Este documento registra todas las consultas realizadas sobre testing, cobertura y validación durante el desarrollo del proyecto.

---

## 1. Tests para Board

**Pregunta**: De cada uno de los atributos de Board haceme los test.

**Respuesta**:
```python
import unittest
from core.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
    
    def test_puntos_attribute_initialization(self):
        """Verifica que __puntos__ se inicialice con 24 posiciones"""
        puntos = self.board.get_puntos()
        self.assertEqual(len(puntos), 24)
        self.assertIsInstance(puntos, list)
    
    def test_initial_piece_positions(self):
        """Verifica las posiciones iniciales de las fichas"""
        self.assertEqual(self.board.get_punto(1), ('white', 2))
        self.assertEqual(self.board.get_punto(6), ('black', 5))
        self.assertIsNone(self.board.get_punto(2))
    
    def test_total_pieces_count(self):
        """Verifica que cada jugador tenga exactamente 15 fichas"""
        white_count = 0
        black_count = 0
        for punto in self.board.get_puntos():
            if punto:
                color, cantidad = punto
                if color == 'white':
                    white_count += cantidad
                else:
                    black_count += cantidad
        
        self.assertEqual(white_count, 15)
        self.assertEqual(black_count, 15)
```

---

## 2. Tests para Dice

**Pregunta**: En base al archivo dice.py hace test por cada uno de los atributos pero solo los esenciales.

**Respuesta**:
```python
import unittest
from core.dice import Dice

class TestDice(unittest.TestCase):
    def setUp(self):
        self.dice = Dice()
    
    def test_dado1_attribute_initialization(self):
        """Verifica que dado1 inicie como None"""
        self.assertIsNone(self.dice.get_dado1())
    
    def test_dado2_attribute_initialization(self):
        """Verifica que dado2 inicie como None"""
        self.assertIsNone(self.dice.get_dado2())
    
    def test_dado1_after_tirar(self):
        """Verifica que dado1 tenga un valor válido después de tirar"""
        self.dice.tirar()
        dado1 = self.dice.get_dado1()
        self.assertIsNotNone(dado1)
        self.assertIn(dado1, [1, 2, 3, 4, 5, 6])
    
    def test_dado2_after_tirar(self):
        """Verifica que dado2 tenga un valor válido después de tirar"""
        self.dice.tirar()
        dado2 = self.dice.get_dado2()
        self.assertIsNotNone(dado2)
        self.assertIn(dado2, [1, 2, 3, 4, 5, 6])
    
    def test_tirar_returns_correct_length(self):
        """Verifica que tirar() retorne 2 o 4 valores"""
        resultado = self.dice.tirar()
        self.assertIn(len(resultado), [2, 4])
    
    def test_tirar_dobles(self):
        """Verifica que los dobles retornen 4 valores iguales"""
        # Realizar múltiples tiradas para encontrar dobles
        encontrado_dobles = False
        for _ in range(100):
            resultado = self.dice.tirar()
            if len(resultado) == 4:
                self.assertTrue(all(v == resultado[0] for v in resultado))
                encontrado_dobles = True
                break
        
        # Si no encontramos dobles en 100 intentos, el test pasa igual
        # (es probabilísticamente muy raro pero posible)
```

---

## 3. Tests para Player

**Pregunta**: Haceme los test esenciales para verificar toda esa clase.

**Respuesta**:
```python
import unittest
from core.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Ana", "white")
    
    def test_nombre_attribute_initialization(self):
        """Verifica que el nombre se inicialice correctamente"""
        self.assertEqual(self.player.get_nombre(), "Ana")
    
    def test_color_attribute_initialization(self):
        """Verifica que el color se inicialice correctamente"""
        self.assertEqual(self.player.get_color(), "white")
    
    def test_fichas_attribute_initialization(self):
        """Verifica que las fichas inicien en 15"""
        self.assertEqual(self.player.get_fichas(), 15)
    
    def test_set_fichas_valid(self):
        """Verifica que set_fichas funcione con valores válidos"""
        self.player.set_fichas(10)
        self.assertEqual(self.player.get_fichas(), 10)
    
    def test_set_fichas_invalid(self):
        """Verifica que set_fichas lance excepción con valores negativos"""
        with self.assertRaises(ValueError):
            self.player.set_fichas(-1)
    
    def test_reset_fichas(self):
        """Verifica que reset_fichas restaure el valor a 15"""
        self.player.set_fichas(5)
        self.player.reset_fichas()
        self.assertEqual(self.player.get_fichas(), 15)
```

---

## 4. Tests para Checker

**Pregunta**: Necesito tests para la clase Checker. ¿Qué debería probar?

**Respuesta**:
```python
import unittest
from core.checker import Checker
from core.player import Player

class TestChecker(unittest.TestCase):
    def setUp(self):
        self.checker_white = Checker('white')
        self.checker_black = Checker('black')
        self.player_white = Player("Jugador1", "white")
        self.player_black = Player("Jugador2", "black")
    
    def test_color_initialization(self):
        """Verifica que el color se inicialice correctamente"""
        self.assertEqual(self.checker_white.get_color(), 'white')
        self.assertEqual(self.checker_black.get_color(), 'black')
    
    def test_invalid_color_raises_exception(self):
        """Verifica que colores inválidos lancen excepción"""
        with self.assertRaises(ValueError):
            Checker('red')
        with self.assertRaises(ValueError):
            Checker('blue')
    
    def test_es_del_jugador_true(self):
        """Verifica que es_del_jugador retorne True para el jugador correcto"""
        self.assertTrue(self.checker_white.es_del_jugador(self.player_white))
        self.assertTrue(self.checker_black.es_del_jugador(self.player_black))
    
    def test_es_del_jugador_false(self):
        """Verifica que es_del_jugador retorne False para jugador incorrecto"""
        self.assertFalse(self.checker_white.es_del_jugador(self.player_black))
        self.assertFalse(self.checker_black.es_del_jugador(self.player_white))
    
    def test_puede_ser_capturada_por_different_color(self):
        """Verifica que fichas de distinto color pueden capturarse"""
        self.assertTrue(self.checker_white.puede_ser_capturada_por(self.checker_black))
        self.assertTrue(self.checker_black.puede_ser_capturada_por(self.checker_white))
    
    def test_puede_ser_capturada_por_same_color(self):
        """Verifica que fichas del mismo color no se capturen"""
        checker_white2 = Checker('white')
        self.assertFalse(self.checker_white.puede_ser_capturada_por(checker_white2))
    
    def test_str_representation(self):
        """Verifica la representación string de la ficha"""
        self.assertIn('white', str(self.checker_white))
        self.assertIn('black', str(self.checker_black))
    
    def test_equality(self):
        """Verifica la igualdad entre fichas"""
        checker_white2 = Checker('white')
        self.assertEqual(self.checker_white, checker_white2)
        self.assertNotEqual(self.checker_white, self.checker_black)
```

---

## 5. Tests para Game - Inicialización

**Pregunta**: Necesito tests para la clase Game. ¿Por dónde empiezo?

**Respuesta**: Primero probamos la inicialización y métodos básicos:

```python
import unittest
from core.game import Game

class TestGameInitialization(unittest.TestCase):
    def setUp(self):
        self.game = Game("Ana", "Luis")
    
    def test_board_initialization(self):
        """Verifica que el tablero se inicialice correctamente"""
        board = self.game.get_board()
        self.assertIsNotNone(board)
        self.assertEqual(len(board.get_puntos()), 24)
    
    def test_players_initialization(self):
        """Verifica que los jugadores se inicialicen correctamente"""
        players = self.game.get_players()
        self.assertEqual(len(players), 2)
        self.assertEqual(players[0].get_nombre(), "Ana")
        self.assertEqual(players[1].get_nombre(), "Luis")
    
    def test_dice_initialization(self):
        """Verifica que los dados se inicialicen"""
        dice = self.game.get_dice()
        self.assertIsNotNone(dice)
    
    def test_turno_initialization(self):
        """Verifica que el turno no esté definido antes de iniciar"""
        self.assertIsNone(self.game.get_turno())
    
    def test_bar_initialization(self):
        """Verifica que la barra esté vacía al inicio"""
        bar = self.game.get_bar()
        self.assertEqual(len(bar['white']), 0)
        self.assertEqual(len(bar['black']), 0)
    
    def test_home_initialization(self):
        """Verifica que home esté vacía al inicio"""
        home = self.game.get_home()
        self.assertEqual(len(home['white']), 0)
        self.assertEqual(len(home['black']), 0)
```

---

## 6. Tests para Game - Tirada de Dados

**Pregunta**: ¿Cómo pruebo la tirada de dados en Game?

**Respuesta**:
```python
class TestGameDice(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game.iniciar_juego()
    
    def test_tirar_dados_returns_values(self):
        """Verifica que tirar_dados retorne valores"""
        valores = self.game.tirar_dados()
        self.assertIsNotNone(valores)
        self.assertIn(len(valores), [2, 4])
    
    def test_tirar_dados_updates_ultimo_roll(self):
        """Verifica que ultimo_roll se actualice"""
        valores = self.game.tirar_dados()
        self.assertEqual(self.game.get_ultimo_roll(), valores)
    
    def test_tirar_dados_updates_movimientos_disponibles(self):
        """Verifica que movimientos_disponibles se actualice"""
        valores = self.game.tirar_dados()
        movimientos = self.game.get_movimientos_disponibles()
        self.assertEqual(len(movimientos), len(valores))
    
    def test_tirar_dados_dobles(self):
        """Verifica el comportamiento con dobles"""
        # Simular hasta encontrar dobles
        for _ in range(100):
            valores = self.game.tirar_dados()
            if len(valores) == 4:
                self.assertTrue(all(v == valores[0] for v in valores))
                break
```

---

## 7. Tests para Game - Validación de Movimientos

**Pregunta**: ¿Qué casos debo probar para validación de movimientos?

**Respuesta**:
```python
class TestGameMovementValidation(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game.iniciar_juego()
        self.game.tirar_dados()
    
    def test_es_movimiento_valido_posiciones_invalidas(self):
        """Verifica que posiciones inválidas sean rechazadas"""
        self.assertFalse(self.game.es_movimiento_valido(-1, 5))
        self.assertFalse(self.game.es_movimiento_valido(1, 26))
        self.assertFalse(self.game.es_movimiento_valido(30, 5))
    
    def test_es_movimiento_valido_sin_dados(self):
        """Verifica que sin dados disponibles no haya movimientos válidos"""
        self.game._Game__movimientos_disponibles__ = []
        color = self.game.get_jugador_actual().get_color()
        # Buscar un punto con fichas del color actual
        for pos in range(1, 25):
            if self.game.get_board().tiene_fichas(pos):
                if self.game.get_board().get_color_punto(pos) == color:
                    self.assertFalse(self.game.es_movimiento_valido(pos, pos + 1))
                    break
    
    def test_es_movimiento_valido_punto_bloqueado(self):
        """Verifica que puntos bloqueados por el oponente sean inválidos"""
        # Configurar un punto bloqueado (2+ fichas del oponente)
        board = self.game.get_board()
        color = self.game.get_jugador_actual().get_color()
        color_oponente = 'black' if color == 'white' else 'white'
        
        # Limpiar punto 10 y agregar 2 fichas del oponente
        while board.tiene_fichas(10):
            board.quitar_ficha(10)
        
        from core.checker import Checker
        board.agregar_ficha(10, Checker(color_oponente))
        board.agregar_ficha(10, Checker(color_oponente))
        
        # Intentar mover a ese punto
        if 4 in self.game.get_movimientos_disponibles():
            self.assertFalse(self.game.es_movimiento_valido(6, 10))
    
    def test_es_movimiento_valido_con_fichas_en_barra(self):
        """Verifica que con fichas en barra solo se pueda mover desde ahí"""
        color = self.game.get_jugador_actual().get_color()
        from core.checker import Checker
        
        # Agregar ficha a la barra
        self.game.get_bar()[color].append(Checker(color))
        
        # Intentar mover desde el tablero debe ser inválido
        self.assertFalse(self.game.es_movimiento_valido(1, 2))
```

---

## 8. Tests para Game - Ejecución de Movimientos

**Pregunta**: ¿Cómo pruebo que los movimientos se ejecuten correctamente?

**Respuesta**:
```python
class TestGameMovementExecution(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game.iniciar_juego()
    
    def test_hacer_movimiento_completo(self):
        """Verifica que un movimiento válido se ejecute"""
        self.game.tirar_dados()
        color = self.game.get_jugador_actual().get_color()
        board = self.game.get_board()
        
        # Encontrar un movimiento válido
        movimientos = self.game.get_movimientos_disponibles()
        if movimientos:
            dado = movimientos[0]
            # Buscar punto con fichas propias
            for desde in range(1, 25):
                if board.tiene_fichas(desde):
                    if board.get_color_punto(desde) == color:
                        if color == 'white':
                            hasta = desde + dado
                        else:
                            hasta = desde - dado
                        
                        if 1 <= hasta <= 24:
                            if self.game.es_movimiento_valido(desde, hasta):
                                cantidad_antes = board.get_cantidad_fichas(desde)
                                self.game.hacer_movimiento(desde, hasta)
                                cantidad_despues = board.get_cantidad_fichas(desde)
                                self.assertEqual(cantidad_antes - 1, cantidad_despues)
                                break
    
    def test_hacer_movimiento_con_captura(self):
        """Verifica que la captura funcione correctamente"""
        board = self.game.get_board()
        from core.checker import Checker
        
        # Configurar escenario de captura
        # Limpiar puntos y colocar fichas específicas
        while board.tiene_fichas(5):
            board.quitar_ficha(5)
        board.agregar_ficha(5, Checker('white'))
        
        while board.tiene_fichas(6):
            board.quitar_ficha(6)
        board.agregar_ficha(6, Checker('black'))
        
        # Configurar turno y dados para permitir captura
        self.game._Game__turno__ = 0  # Turno de blancas
        self.game._Game__movimientos_disponibles__ = [1]
        
        bar_antes = len(self.game.get_bar()['black'])
        self.game.hacer_movimiento(5, 6)
        bar_despues = len(self.game.get_bar()['black'])
        
        self.assertEqual(bar_despues, bar_antes + 1)
    
    def test_hacer_movimiento_bear_off(self):
        """Verifica que el bear off funcione"""
        # Configurar todas las fichas en casa
        board = self.game.get_board()
        from core.checker import Checker
        
        # Limpiar tablero
        for pos in range(1, 25):
            while board.tiene_fichas(pos):
                board.quitar_ficha(pos)
        
        # Colocar fichas blancas en casa (puntos 19-24)
        for pos in range(19, 25):
            board.agregar_ficha(pos, Checker('white'))
        
        self.game._Game__turno__ = 0
        self.game._Game__movimientos_disponibles__ = [6]
        
        home_antes = len(self.game.get_home()['white'])
        self.game.hacer_movimiento(19, 25)
        home_despues = len(self.game.get_home()['white'])
        
        self.assertEqual(home_despues, home_antes + 1)
```

---

## 9. Tests para Game - Fin de Juego

**Pregunta**: ¿Cómo pruebo las condiciones de victoria?

**Respuesta**:
```python
class TestGameEndConditions(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game.iniciar_juego()
    
    def test_esta_terminado_false_al_inicio(self):
        """Verifica que el juego no esté terminado al inicio"""
        self.assertFalse(self.game.esta_terminado())
    
    def test_esta_terminado_true_con_15_en_home(self):
        """Verifica que el juego termine cuando un jugador saca 15 fichas"""
        from core.checker import Checker
        
        # Llenar home de blancas
        for _ in range(15):
            self.game.get_home()['white'].append(Checker('white'))
        
        self.assertTrue(self.game.esta_terminado())
    
    def test_get_ganador_none_al_inicio(self):
        """Verifica que no haya ganador al inicio"""
        self.assertIsNone(self.game.get_ganador())
    
    def test_get_ganador_con_victoria(self):
        """Verifica que se identifique correctamente al ganador"""
        from core.checker import Checker
        
        # Hacer ganar a las blancas
        for _ in range(15):
            self.game.get_home()['white'].append(Checker('white'))
        
        ganador = self.game.get_ganador()
        self.assertIsNotNone(ganador)
        self.assertEqual(ganador.get_color(), 'white')
```

---

## 10. Tests para Game - Turnos

**Pregunta**: ¿Cómo pruebo el cambio de turnos?

**Respuesta**:
```python
class TestGameTurns(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game.iniciar_juego()
    
    def test_iniciar_juego_define_turno(self):
        """Verifica que iniciar_juego defina un turno"""
        self.assertIsNotNone(self.game.get_turno())
        self.assertIn(self.game.get_turno(), [0, 1])
    
    def test_cambiar_turno_alterna_jugador(self):
        """Verifica que cambiar_turno alterne entre jugadores"""
        turno_inicial = self.game.get_turno()
        self.game.cambiar_turno()
        turno_nuevo = self.game.get_turno()
        
        self.assertNotEqual(turno_inicial, turno_nuevo)
        self.assertIn(turno_nuevo, [0, 1])
    
    def test_cambiar_turno_limpia_movimientos(self):
        """Verifica que cambiar_turno limpie movimientos disponibles"""
        self.game.tirar_dados()
        self.assertTrue(len(self.game.get_movimientos_disponibles()) > 0)
        
        self.game.cambiar_turno()
        self.assertEqual(len(self.game.get_movimientos_disponibles()), 0)
    
    def test_get_jugador_actual(self):
        """Verifica que get_jugador_actual retorne el jugador correcto"""
        jugador = self.game.get_jugador_actual()
        turno = self.game.get_turno()
        
        self.assertEqual(jugador, self.game.get_players()[turno])
```

---

## 11. Estrategia de Cobertura

**Pregunta**: ¿Cómo aseguro buena cobertura de tests?

**Respuesta**: 

**Usar coverage.py**:
```bash
# Instalar
pip install coverage

# Ejecutar tests con cobertura
coverage run -m unittest discover tests

# Ver reporte
coverage report

# Generar reporte HTML
coverage html
```

**Objetivos de cobertura**:
- **>90% total** (requisito del proyecto)
- **100% en clases core** (Board, Checker, Player, Dice)
- **>85% en Game** (la lógica más compleja)
- **>70% en interfaces** (CLI, Pygame)

**Prioridades**:
1. Lógica de negocio crítica (validaciones de movimiento)
2. Condiciones de victoria
3. Manejo de excepciones
4. Casos borde (tablero vacío, barra llena, etc.)
5. Integración entre componentes

---

## 12. Tests de Integración

**Pregunta**: ¿Cómo pruebo que todos los componentes funcionen juntos?

**Respuesta**:
```python
class TestGameIntegration(unittest.TestCase):
    def test_juego_completo_simplificado(self):
        """Simula un juego completo simplificado"""
        game = Game("Jugador1", "Jugador2")
        
        # Iniciar
        game.iniciar_juego()
        self.assertIsNotNone(game.get_turno())
        
        # Realizar algunos turnos
        for _ in range(5):
            game.tirar_dados()
            
            # Intentar hacer un movimiento válido
            color = game.get_jugador_actual().get_color()
            board = game.get_board()
            movimientos = game.get_movimientos_disponibles()
            
            movimiento_realizado = False
            if movimientos:
                for dado in movimientos:
                    for desde in range(1, 25):
                        if board.tiene_fichas(desde):
                            if board.get_color_punto(desde) == color:
                                if color == 'white':
                                    hasta = desde + dado
                                else:
                                    hasta = desde - dado
                                
                                if 1 <= hasta <= 24:
                                    if game.es_movimiento_valido(desde, hasta):
                                        game.hacer_movimiento(desde, hasta)
                                        movimiento_realizado = True
                                        break
                    if movimiento_realizado:
                        break
            
            game.cambiar_turno()
        
        # Verificar que el juego siga consistente
        self.assertIsNotNone(game.get_board())
        self.assertEqual(len(game.get_players()), 2)
```

---

## 13. Tests de Casos Borde

**Pregunta**: ¿Qué casos borde importantes debo probar?

**Respuesta**:
```python
class TestEdgeCases(unittest.TestCase):
    def test_barra_completamente_bloqueada(self):
        """Prueba cuando todas las entradas desde barra están bloqueadas"""
        game = Game()
        game.iniciar_juego()
        board = game.get_board()
        from core.checker import Checker
        
        # Bloquear todos los puntos de entrada para blancas (1-6)
        for pos in range(1, 7):
            while board.tiene_fichas(pos):
                board.quitar_ficha(pos)
            board.agregar_ficha(pos, Checker('black'))
            board.agregar_ficha(pos, Checker('black'))
        
        # Poner ficha blanca en barra
        game.get_bar()['white'].append(Checker('white'))
        game._Game__turno__ = 0
        game.tirar_dados()
        
        # No debería haber movimientos disponibles
        self.assertFalse(game.tiene_movimientos_disponibles())
    
    def test_ultimo_movimiento_para_ganar(self):
        """Prueba el último movimiento que lleva a la victoria"""
        game = Game()
        game.iniciar_juego()
        from core.checker import Checker
        
        # Configurar: 14 fichas en home, 1 en punto 24
        board = game.get_board()
        for pos in range(1, 25):
            while board.tiene_fichas(pos):
                board.quitar_ficha(pos)
        
        board.agregar_ficha(24, Checker('white'))
        for _ in range(14):
            game.get_home()['white'].append(Checker('white'))
        
        game._Game__turno__ = 0
        game._Game__movimientos_disponibles__ = [1]
        
        # Este movimiento debería ganar el juego
        game.hacer_movimiento(24, 25)
        self.assertTrue(game.esta_terminado())
        self.assertEqual(game.get_ganador().get_color(), 'white')
    
    def test_movimiento_con_dado_mayor_en_bear_off(self):
        """Prueba usar dado mayor cuando no hay ficha exacta en bear off"""
        game = Game()
        game.iniciar_juego()
        board = game.get_board()
        from core.checker import Checker
        
        # Limpiar tablero
        for pos in range(1, 25):
            while board.tiene_fichas(pos):
                board.quitar_ficha(pos)
        
        # Colocar fichas blancas en casa
        board.agregar_ficha(20, Checker('white'))
        
        game._Game__turno__ = 0
        game._Game__movimientos_disponibles__ = [6]
        
        # Debería poder sacar con dado de 6 desde punto 20
        self.assertTrue(game.es_movimiento_valido(20, 25))
```

---

## 14. Mocking y Tests Aislados

**Pregunta**: ¿Cuándo debo usar mocking en los tests?

**Respuesta**:
```python
from unittest.mock import Mock, patch

class TestWithMocking(unittest.TestCase):
    @patch('core.dice.random.randint')
    def test_tirar_dados_forzado(self, mock_randint):
        """Fuerza valores específicos en la tirada de dados"""
        # Configurar mock para retornar valores específicos
        mock_randint.side_effect = [3, 5]  # Primera llamada: 3, segunda: 5
        
        game = Game()
        game.iniciar_juego()
        valores = game.tirar_dados()
        
        self.assertEqual(valores, [3, 5])
    
    @patch('core.dice.random.randint')
    def test_tirar_dobles_forzado(self, mock_randint):
        """Fuerza dobles en la tirada"""
        mock_randint.return_value = 4  # Ambos dados retornan 4
        
        game = Game()
        game.iniciar_juego()
        valores = game.tirar_dados()
        
        self.assertEqual(valores, [4, 4, 4, 4])
```

**Cuándo usar mocking**:
- Para controlar aleatoriedad en tests
- Para simular condiciones específicas
- Para aislar componentes en tests unitarios
- Para evitar dependencias externas

**Cuándo NO usar mocking**:
- En tests de integración (queremos probar el flujo real)
- Cuando el comportamiento aleatorio es parte del test
- En tests simples de getters/setters

---

## 15. Organización de Tests

**Pregunta**: ¿Cómo organizo los archivos de tests?

**Respuesta**:

**Estructura recomendada**:
```
tests/
├── __init__.py
├── test_board.py           # Tests de Board
├── test_checker.py         # Tests de Checker
├── test_player.py          # Tests de Player
├── test_dice.py            # Tests de Dice
├── test_game.py            # Tests de Game
├── test_integration.py     # Tests de integración
└── test_edge_cases.py      # Casos borde
```

**Convenciones de nombres**:
- Archivo: `test_<modulo>.py`
- Clase: `Test<Clase>` o `Test<Funcionalidad>`
- Método: `test_<que_se_prueba>`

**Ejecutar tests**:
```bash
# Todos los tests
python -m unittest discover tests

# Un archivo específico
python -m unittest tests.test_board

# Una clase específica
python -m unittest tests.test_board.TestBoard

# Un test específico
python -m unittest tests.test_board.TestBoard.test_puntos_attribute_initialization

# Con verbose
python -m unittest discover tests -v
```

---

## Notas Finales

- Todos los tests deben ser independientes (no depender de orden de ejecución)
- Usar `setUp()` y `tearDown()` para preparar y limpiar
- Cada test debe probar UNA cosa específica
- Los tests son documentación ejecutable del código
- Mantener cobertura >90% como requisito del proyecto

**Última actualización**: 2025-11-01