import unittest
from core.checker import Checker


class TestChecker(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test."""
        self.checker_white = Checker('white')
        self.checker_black = Checker('black')
    
    def test_color_attribute_initialization_white(self):
        """Test que verifica que __color__ se inicializa correctamente para fichas blancas."""
        self.assertEqual(self.checker_white.get_color(), 'white')
    
    def test_color_attribute_initialization_black(self):
        """Test que verifica que __color__ se inicializa correctamente para fichas negras."""
        self.assertEqual(self.checker_black.get_color(), 'black')
    
    def test_invalid_color_raises_exception(self):
        """Test que verifica que colores inválidos lanzan excepción."""
        with self.assertRaises(ValueError):
            Checker('red')
        
        with self.assertRaises(ValueError):
            Checker('blue')
    
    def test_es_del_jugador_white(self):
        """Test que verifica es_del_jugador para fichas blancas."""
        self.assertTrue(self.checker_white.es_del_jugador('white'))
        self.assertFalse(self.checker_white.es_del_jugador('black'))
    
    def test_es_del_jugador_black(self):
        """Test que verifica es_del_jugador para fichas negras."""
        self.assertTrue(self.checker_black.es_del_jugador('black'))
        self.assertFalse(self.checker_black.es_del_jugador('white'))
    
    def test_puede_ser_capturada_por_white(self):
        """Test que verifica captura para fichas blancas."""
        self.assertFalse(self.checker_white.puede_ser_capturada_por('white'))
        self.assertTrue(self.checker_white.puede_ser_capturada_por('black'))
    
    def test_puede_ser_capturada_por_black(self):
        """Test que verifica captura para fichas negras."""
        self.assertFalse(self.checker_black.puede_ser_capturada_por('black'))
        self.assertTrue(self.checker_black.puede_ser_capturada_por('white'))
    
    def test_str_representation(self):
        """Test que verifica la representación en string."""
        self.assertEqual(str(self.checker_white), "Ficha white")
        self.assertEqual(str(self.checker_black), "Ficha black")
    
    def test_equality_same_color(self):
        """Test que verifica igualdad entre fichas del mismo color."""
        another_white = Checker('white')
        self.assertEqual(self.checker_white, another_white)
    
    def test_equality_different_color(self):
        """Test que verifica desigualdad entre fichas de diferente color."""
        self.assertNotEqual(self.checker_white, self.checker_black)
    
    def test_repr_representation(self):
        """Test que verifica la representación para debugging."""
        self.assertEqual(repr(self.checker_white), "Checker('white')")
        self.assertEqual(repr(self.checker_black), "Checker('black')")

    def test_equality_with_non_checker(self):
        """Test que verifica comparación con objetos que no son Checker."""
        self.assertNotEqual(self.checker_white, "white")
        self.assertNotEqual(self.checker_white, None)
        self.assertNotEqual(self.checker_white, 123)


if __name__ == '__main__':
    unittest.main()
