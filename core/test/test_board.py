import unittest
import sys
import os

# este código hace que Python pueda encontrar e importar archivos para usarlos
current_dir = os.path.dirname(os.path.abspath(__file__))  # .github/core/test/
parent_dir = os.path.dirname(current_dir)  # .github/core/
sys.path.insert(0, parent_dir)

from board import Board


class TestBoard(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test."""
        self.board = Board()
    
    def test_puntos_attribute_initialization(self):
        """Test que verifica que __puntos__ se inicializa como lista de 24 elementos."""
        puntos = self.board.get_puntos()
        self.assertEqual(len(puntos), 24)
        self.assertIsInstance(puntos, list)
    
    def test_initial_piece_positions(self):
        """Test que verifica las posiciones iniciales de ambos jugadores."""
        # Verificar posiciones clave de fichas blancas usando get_punto()
        self.assertEqual(self.board.get_punto(1), ('white', 2))   # Punto 1
        self.assertEqual(self.board.get_punto(12), ('white', 5))  # Punto 12
        
        # Verificar posiciones clave de fichas negras
        self.assertEqual(self.board.get_punto(6), ('black', 5))   # Punto 6
        self.assertEqual(self.board.get_punto(24), ('black', 2))  # Punto 24
        
        # Verificar que hay posiciones vacías
        self.assertIsNone(self.board.get_punto(2))   # Punto 2
        self.assertIsNone(self.board.get_punto(10))  # Punto 10
    
    def test_total_pieces_count(self):
        """Test que verifica que cada jugador tiene 15 fichas en total."""
        puntos = self.board.get_puntos()
        white_count = 0
        black_count = 0
        
        for punto in puntos:
            if punto:
                color, cantidad = punto
                if color == 'white':
                    white_count += cantidad
                elif color == 'black':
                    black_count += cantidad
        
        self.assertEqual(white_count, 15)
        self.assertEqual(black_count, 15)


if __name__ == '__main__':
    unittest.main()