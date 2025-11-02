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
    
    def test_dobles_returns_four_values(self):
        """Test que verifica que cuando salen dobles se retornan 4 valores iguales"""
        # Realizamos múltiples tiradas para aumentar probabilidad de obtener dobles
        dobles_encontrados = False
        for _ in range(100):  # Intentamos hasta 100 veces
            resultado = self.dice.tirar()
            dado1 = self.dice.get_dado1()
            dado2 = self.dice.get_dado2()
            
            if dado1 == dado2:  # Si son dobles
                self.assertEqual(len(resultado), 4)
                self.assertTrue(all(valor == dado1 for valor in resultado))
                dobles_encontrados = True
                break
        
        # Si no encontramos dobles en 100 intentos, al menos verificamos que el formato es correcto
        if not dobles_encontrados:
            resultado = self.dice.tirar()
            self.assertIn(len(resultado), [2, 4])
    
    def test_multiple_tiradas_independence(self):
        """Test que verifica que múltiples tiradas son independientes"""
        resultados = []
        for _ in range(10):
            resultado = self.dice.tirar()
            resultados.append((self.dice.get_dado1(), self.dice.get_dado2()))
        
        # Verificamos que no todos los resultados son iguales (muy improbable)
        valores_unicos = set(resultados)
        self.assertGreater(len(valores_unicos), 1, "Es extremadamente improbable que 10 tiradas sean idénticas")
        
        # Verificamos que cada resultado individual es válido
        for dado1, dado2 in resultados:
            self.assertIn(dado1, [1, 2, 3, 4, 5, 6])
            self.assertIn(dado2, [1, 2, 3, 4, 5, 6])

    def test_es_doble_sin_tirar(self):
        """Test que verifica es_doble cuando no se han tirado dados."""
        self.assertFalse(self.dice.es_doble())

    def test_get_valores_sin_tirar(self):
        """Test que verifica get_valores cuando no se han tirado dados."""
        valores = self.dice.get_valores()
        self.assertEqual(valores, (None, None))

    def test_str_sin_tirar(self):
        """Test que verifica __str__ sin tirar dados."""
        resultado = str(self.dice)
        self.assertEqual(resultado, "Dados: No se han tirado aún")

    def test_str_con_dados_normales(self):
        """Test que verifica __str__ con dados diferentes."""
        # Tirar hasta obtener dados diferentes
        for _ in range(50):
            self.dice.tirar()
            if not self.dice.es_doble():
                resultado = str(self.dice)
                self.assertIn("Dados:", resultado)
                self.assertNotIn("DOBLES", resultado)
                break

    def test_str_con_dobles(self):
        """Test que verifica __str__ con dobles."""
        # Tirar hasta obtener dobles
        for _ in range(100):
            self.dice.tirar()
            if self.dice.es_doble():
                resultado = str(self.dice)
                self.assertIn("Dados:", resultado)
                self.assertIn("DOBLES", resultado)
                break


if __name__ == '__main__':  
    unittest.main()