class Board:
    def __init__(self):
        """
        Se arma el tablero de backgammon con la posición inicial de las fichas.
        El tablero tiene 24 puntos numerados del 1 al 24:
        Del 1 al 6: zona interna del jugador 1.
        Del 7 al 12: zona externa del jugador 1.
        Del 13 al 18: zona externa del jugador 2.
        Del 19 al 24: zona interna del jugador 2.
        En cada punto se guarda una tupla con dos datos:
        El color de las fichas (black, white o None). 
        La cantidad de fichas que hay en ese punto.
        """
        self.__puntos__ = [None] * 24  # 24 posiciones (índices 0-23 para puntos 1-24)
        
        # Configuracion inicial del backgammon
        # Jugador blanco (white)
        self.__puntos__[0] = ('white', 2)   # Punto 1: 2 fichas blancas
        self.__puntos__[11] = ('white', 5)  # Punto 12: 5 fichas blancas
        self.__puntos__[16] = ('white', 3)  # Punto 17: 3 fichas blancas
        self.__puntos__[18] = ('white', 5)  # Punto 19: 5 fichas blancas
        
        # Jugador negro (black)
        self.__puntos__[5] = ('black', 5)   # Punto 6: 5 fichas negras
        self.__puntos__[7] = ('black', 3)   # Punto 8: 3 fichas negras
        self.__puntos__[12] = ('black', 5)  # Punto 13: 5 fichas negras
        self.__puntos__[23] = ('black', 2)  # Punto 24: 2 fichas negras
        
        # Las demás posiciones quedan como None (vacías)
    
    def get_puntos(self):
        """Retorna la lista de puntos del tablero"""
        return self.__puntos__
    
    def get_punto(self, posicion):
        """
        Retorna el contenido de un punto específico
        
        Args:
            posicion (int): Número del punto (1-24)
            
        Returns:
            tuple or None: (color, cantidad) o None si está vacío
        """
        if 1 <= posicion <= 24:
            return self.__puntos__[posicion - 1]
        else:
            raise ValueError("La posición debe estar entre 1 y 24")
    
    def __str__(self):
        """Representación en string del tablero"""
        resultado = "Tablero de Backgammon:\n"
        for i, punto in enumerate(self.__puntos__, 1):
            if punto:
                color, cantidad = punto
                resultado += f"Punto {i:2d}: {cantidad} fichas {color}\n"
            else:
                resultado += f"Punto {i:2d}: vacío\n"
        return resultado