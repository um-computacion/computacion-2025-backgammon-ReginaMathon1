import unittest
from core.board import Board
from core.checker import Checker


class TestBoard(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test."""
        self.board = Board()
    
    def test_puntos_attribute_initialization(self):
        """Test que verifica que __puntos__ se inicializa como lista de 24 elementos."""
        puntos = self.board.get_puntos()
        self.assertEqual(len(puntos), 24)
        self.assertIsInstance(puntos, list)
        
        # Verificar que cada punto es una lista
        for punto in puntos:
            self.assertIsInstance(punto, list)
    
    def test_initial_piece_positions(self):
        """Test que verifica las posiciones iniciales de ambos jugadores."""
        # Verificar posiciones clave de fichas blancas
        self.assertEqual(self.board.get_color_punto(1), 'white')
        self.assertEqual(self.board.get_cantidad_fichas(1), 2)
        
        self.assertEqual(self.board.get_color_punto(12), 'white')
        self.assertEqual(self.board.get_cantidad_fichas(12), 5)
        
        # Verificar posiciones clave de fichas negras
        self.assertEqual(self.board.get_color_punto(6), 'black')
        self.assertEqual(self.board.get_cantidad_fichas(6), 5)
        
        self.assertEqual(self.board.get_color_punto(24), 'black')
        self.assertEqual(self.board.get_cantidad_fichas(24), 2)
        
        # Verificar que hay posiciones vacías
        self.assertFalse(self.board.tiene_fichas(2))
        self.assertEqual(self.board.get_cantidad_fichas(2), 0)
    
    def test_total_pieces_count(self):
        """Test que verifica que cada jugador tiene 15 fichas en total."""
        white_count = 0
        black_count = 0
        
        for i in range(1, 25):  # Puntos 1 a 24
            fichas = self.board.get_punto(i)
            for ficha in fichas:
                if ficha.get_color() == 'white':
                    white_count += 1
                elif ficha.get_color() == 'black':
                    black_count += 1
        
        self.assertEqual(white_count, 15)
        self.assertEqual(black_count, 15)
    
    def test_agregar_ficha(self):
        """Test que verifica que se pueden agregar fichas correctamente."""
        nueva_ficha = Checker('white')
        self.board.agregar_ficha(2, nueva_ficha)  # Punto vacío
        
        self.assertTrue(self.board.tiene_fichas(2))
        self.assertEqual(self.board.get_cantidad_fichas(2), 1)
        self.assertEqual(self.board.get_color_punto(2), 'white')
    
    def test_agregar_ficha_mismo_color(self):
        """Test que verifica que se pueden agregar fichas del mismo color."""
        nueva_ficha = Checker('white')
        self.board.agregar_ficha(1, nueva_ficha)  # Punto con fichas blancas
        
        self.assertEqual(self.board.get_cantidad_fichas(1), 3)  # Era 2, ahora 3
        self.assertEqual(self.board.get_color_punto(1), 'white')
    
    def test_agregar_ficha_diferente_color_raises_error(self):
        """Test que verifica que no se pueden mezclar colores."""
        nueva_ficha = Checker('black')
        
        with self.assertRaises(ValueError):
            self.board.agregar_ficha(1, nueva_ficha)  # Punto 1 tiene fichas blancas
    
    def test_quitar_ficha(self):
        """Test que verifica que se pueden quitar fichas."""
        ficha_quitada = self.board.quitar_ficha(1)
        
        self.assertIsNotNone(ficha_quitada)
        self.assertEqual(ficha_quitada.get_color(), 'white')
        self.assertEqual(self.board.get_cantidad_fichas(1), 1)  # Era 2, ahora 1
    
    def test_quitar_ficha_punto_vacio(self):
        """Test que verifica comportamiento al quitar de punto vacío."""
        ficha_quitada = self.board.quitar_ficha(2)  # Punto vacío
        
        self.assertIsNone(ficha_quitada)
        self.assertEqual(self.board.get_cantidad_fichas(2), 0)


if __name__ == '__main__':
    unittest.main()