class Checker:
    def __init__(self, color):
        """
        Inicializa una ficha de backgammon.
        
        Args:
            color (str): Color de la ficha ('white' o 'black')
        """
        if color not in ['white', 'black']:
            raise ValueError("El color debe ser 'white' o 'black'")
        self.__color__ = color
    
    def get_color(self):
        """Retorna el color de la ficha."""
        return self.__color__
    
    def es_del_jugador(self, color_jugador):
        """
        Verifica si la ficha pertenece a un jugador específico.
        
        Args:
            color_jugador (str): Color del jugador a verificar
            
        Returns:
            bool: True si la ficha pertenece al jugador
        """
        return self.__color__ == color_jugador
    
    def puede_ser_capturada_por(self, color_oponente):
        """
        Verifica si esta ficha puede ser capturada por un oponente.
        
        Args:
            color_oponente (str): Color del jugador oponente
            
        Returns:
            bool: True si puede ser capturada (colores diferentes)
        """
        return self.__color__ != color_oponente
    
    def __str__(self):
        """Representación en string de la ficha."""
        return f"Ficha {self.__color__}"
    
    def __eq__(self, other):
        """Compara dos fichas por color."""
        if isinstance(other, Checker):
            return self.__color__ == other.__color__
        return False
    
    def __repr__(self):
        """Representación para debugging."""
        return f"Checker('{self.__color__}')"
