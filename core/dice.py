import random


class Dice:
    def __init__(self):
        """
        Inician los dados del backgammon
        En backgammon se usan dos dados de 6 caras
        """
        self.__dado1__ = None
        self.__dado2__ = None
    
    def tirar(self):
        """
        Tira los dos dados y devuelve una lista con los valores.
        En backgammon, si ambos dados muestran el mismo valor (dobles),
        el jugador puede mover ese valor 4 veces.
        
        Returns:
            list: Lista con los valores de los dados. Si hay dobles, 
                  retorna 4 elementos iguales.
        """
        self.__dado1__ = random.randint(1, 6)
        self.__dado2__ = random.randint(1, 6)
        
        # Si ambos dados son iguales (dobles), se repite el valor 4 veces
        if self.__dado1__ == self.__dado2__:
            return [self.__dado1__, self.__dado1__, self.__dado1__, self.__dado1__]
        else:
            return [self.__dado1__, self.__dado2__]
    
    def get_dado1(self):
        """Retorna el valor del primer dado."""
        return self.__dado1__
    
    def get_dado2(self):
        """Retorna el valor del segundo dado."""
        return self.__dado2__
    
    def es_doble(self):
        """
        Verifica si la tirada actual es un doble.
        
        Returns:
            bool: True si ambos dados tienen el mismo valor, False en caso contrario.
        """
        if self.__dado1__ is not None and self.__dado2__ is not None:
            return self.__dado1__ == self.__dado2__
        return False
    
    def get_valores(self):
        """
        Retorna los valores actuales de ambos dados.
        
        Returns:
            tuple: (dado1, dado2) o (None, None) si no se han tirado aún.
        """
        return (self.__dado1__, self.__dado2__)
    
    def __str__(self):
        """Representación en string de los dados."""
        if self.__dado1__ is not None and self.__dado2__ is not None:
            if self.es_doble():
                return f"Dados: {self.__dado1__} - {self.__dado2__} (DOBLES!)"
            else:
                return f"Dados: {self.__dado1__} - {self.__dado2__}"
        else:
            return "Dados: No se han tirado aún"