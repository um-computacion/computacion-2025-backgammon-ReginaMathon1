import unittest
from core.player import Player



class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test."""
        self.player = Player("Ana", "white")
    
    def test_nombre_attribute_initialization(self):
        """Test que verifica que __nombre__ se inicializa correctamente."""
        self.assertEqual(self.player.get_nombre(), "Ana")
    
    def test_color_attribute_initialization(self):
        """Test que verifica que __color__ se inicializa correctamente."""
        self.assertEqual(self.player.get_color(), "white")
    
    def test_fichas_attribute_initialization(self):
        """Test que verifica que __fichas__ se inicializa en 15."""
        self.assertEqual(self.player.get_fichas(), 15)
    
    def test_set_fichas_valid_amount(self):
        """Test que verifica que set_fichas funciona con valores válidos."""
        self.player.set_fichas(10)
        self.assertEqual(self.player.get_fichas(), 10)
        
        self.player.set_fichas(0)
        self.assertEqual(self.player.get_fichas(), 0)
    
    def test_set_fichas_invalid_amount(self):
        """Test que verifica que set_fichas lanza excepción con valores negativos."""
        with self.assertRaises(ValueError):
            self.player.set_fichas(-1)
    
    def test_reset_fichas(self):
        """Test que verifica que reset_fichas reinicia las fichas a 15."""
        self.player.set_fichas(5)
        self.player.reset_fichas()
        self.assertEqual(self.player.get_fichas(), 15)
    
    def test_quitar_ficha_successful(self):
        """Test que verifica que quitar_ficha funciona correctamente."""
        result = self.player.quitar_ficha()
        self.assertTrue(result)
        self.assertEqual(self.player.get_fichas(), 14)
    
    def test_quitar_ficha_no_fichas(self):
        """Test que verifica que quitar_ficha falla cuando no hay fichas."""
        self.player.set_fichas(0)
        result = self.player.quitar_ficha()
        self.assertFalse(result)
        self.assertEqual(self.player.get_fichas(), 0)
    
    def test_agregar_ficha(self):
        """Test que verifica que agregar_ficha incrementa las fichas."""
        self.player.agregar_ficha()
        self.assertEqual(self.player.get_fichas(), 16)
    
    def test_ha_ganado_true(self):
        """Test que verifica que ha_ganado retorna True cuando no hay fichas."""
        self.player.set_fichas(0)
        self.assertTrue(self.player.ha_ganado())
    
    def test_ha_ganado_false(self):
        """Test que verifica que ha_ganado retorna False cuando hay fichas."""
        self.assertFalse(self.player.ha_ganado())
    
    def test_str_representation(self):
        """Test que verifica la representación en string del jugador."""
        expected = "Jugador: Ana (white) - Fichas: 15"
        self.assertEqual(str(self.player), expected)
    
    def test_equality_same_player(self):
        """Test que verifica que dos jugadores iguales son considerados iguales."""
        player2 = Player("Ana", "white")
        self.assertEqual(self.player, player2)
    
    def test_equality_different_player(self):
        """Test que verifica que jugadores diferentes no son iguales."""
        player2 = Player("Carlos", "black")
        self.assertNotEqual(self.player, player2)


if __name__ == '__main__':
    unittest.main()