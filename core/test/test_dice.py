import unittest

from core.dice import Dice


class TestDice(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.dice = Dice()
    
    def test_dado1_attribute_initialization(self):
        """Test que verifica que __dado1__ se inicializa como None"""
        self.assertIsNone(self.dice.get_dado1())
    
    def test_dado2_attribute_initialization(self):
        """Test que verifica que __dado2__ se inicializa como None"""
        self.assertIsNone(self.dice.get_dado2())
    
    def test_dado1_after_tirar(self):
        """Test que verifica que __dado1__ tiene un valor válido después de tirar"""
        self.dice.tirar()
        dado1 = self.dice.get_dado1()
        self.assertIsNotNone(dado1)
        self.assertIn(dado1, [1, 2, 3, 4, 5, 6])
    
    def test_dado2_after_tirar(self):
        """Test que verifica que __dado2__ tiene un valor válido después de tirar"""
        self.dice.tirar()
        dado2 = self.dice.get_dado2()
        self.assertIsNotNone(dado2)
        self.assertIn(dado2, [1, 2, 3, 4, 5, 6])
    
    def test_tirar_returns_correct_length(self):
        """Test que verifica que tirar() retorna la cantidad correcta de valores"""
        resultado = self.dice.tirar()
        # Debe retornar 2 valores (normal) o 4 valores (dobles)
        self.assertIn(len(resultado), [2, 4])
    
    def test_tirar_returns_valid_values(self):
        """Test que verifica que tirar() retorna valores válidos (1-6)"""
        resultado = self.dice.tirar()
        for valor in resultado:
            self.assertIn(valor, [1, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()