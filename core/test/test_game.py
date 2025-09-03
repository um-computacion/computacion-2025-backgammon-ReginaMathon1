import unittest

from core.game import Game


class TestBackgammonGame(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test."""
        self.game = Game()
    
    def test_board_attribute_initialization(self):
        """Test que verifica que __board__ se inicializa como None."""
        self.assertIsNone(self.game.get_board())
    
    def test_players_attribute_initialization(self):
        """Test que verifica que __players__ se inicializa como lista vacía."""
        players = self.game.get_players()
        self.assertEqual(len(players), 0)
        self.assertIsInstance(players, list)
    
    def test_dice_attribute_initialization(self):
        """Test que verifica que __dice__ se inicializa como None."""
        self.assertIsNone(self.game.get_dice())
    
    def test_turno_attribute_initialization(self):
        """Test que verifica que __turno__ se inicializa en 0."""
        self.assertEqual(self.game.get_turno_actual(), 0)
    
    def test_board_after_iniciar_juego(self):
        """Test que verifica que __board__ se crea correctamente después de iniciar."""
        self.game.iniciar_juego("Ana", "Carlos")
        board = self.game.get_board()
        self.assertIsNotNone(board)
        # Verificar que el tablero tiene 24 puntos
        self.assertEqual(len(board.get_puntos()), 24)
    
    def test_players_after_iniciar_juego(self):
        """Test que verifica que __players__ se crea correctamente después de iniciar."""
        self.game.iniciar_juego("Ana", "Carlos")
        players = self.game.get_players()
        
        # Verificar que hay 2 jugadores
        self.assertEqual(len(players), 2)
        
        # Verificar nombres y colores
        self.assertEqual(players[0].get_nombre(), "Ana")
        self.assertEqual(players[0].get_color(), "white")
        self.assertEqual(players[1].get_nombre(), "Carlos")
        self.assertEqual(players[1].get_color(), "black")
        
        # Verificar fichas iniciales
        self.assertEqual(players[0].get_fichas(), 15)
        self.assertEqual(players[1].get_fichas(), 15)
    
    def test_dice_after_iniciar_juego(self):
        """Test que verifica que __dice__ se crea correctamente después de iniciar."""
        self.game.iniciar_juego("Ana", "Carlos")
        dice = self.game.get_dice()
        self.assertIsNotNone(dice)
        
        # Verificar que los dados funcionan
        resultado = self.game.tirar_dados()
        self.assertIsInstance(resultado, list)
        self.assertIn(len(resultado), [2, 4])  # 2 valores normales o 4 si hay dobles
    
    def test_turno_after_iniciar_juego(self):
        """Test que verifica que __turno__ se determina correctamente después de iniciar."""
        self.game.iniciar_juego("Ana", "Carlos")
        turno = self.game.get_turno_actual()
        
        # El turno debe ser 0 o 1
        self.assertIn(turno, [0, 1])
        
        # El jugador actual debe ser válido
        jugador_actual = self.game.get_jugador_actual()
        self.assertIn(jugador_actual, self.game.get_players())
    
    def test_cambiar_turno(self):
        """Test que verifica que cambiar_turno alterna correctamente."""
        self.game.iniciar_juego("Ana", "Carlos")
        turno_inicial = self.game.get_turno_actual()
        
        self.game.cambiar_turno()
        turno_nuevo = self.game.get_turno_actual()
        
        # El turno debe cambiar
        self.assertNotEqual(turno_inicial, turno_nuevo)
        self.assertIn(turno_nuevo, [0, 1])
    
    def test_esta_terminado_false(self):
        """Test que verifica que el juego no está terminado al inicio."""
        self.game.iniciar_juego("Ana", "Carlos")
        self.assertFalse(self.game.esta_terminado())
    
    def test_get_ganador_none(self):
        """Test que verifica que no hay ganador al inicio."""
        self.game.iniciar_juego("Ana", "Carlos")
        self.assertIsNone(self.game.get_ganador())


if __name__ == '__main__':
    unittest.main()