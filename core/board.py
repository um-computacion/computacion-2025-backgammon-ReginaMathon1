from .checker import Checker


class Board:
    def __init__(self):
        """
        Se arma el tablero de backgammon con la posición inicial de las fichas.
        El tablero tiene 24 puntos numerados del 1 al 24.
        Cada punto contiene una lista de fichas (objetos Checker).
        """
        self.__puntos__ = [[] for _ in range(24)]  # 24 listas vacías
        
        # Configuración inicial del backgammon usando objetos Checker
        # Jugador blanco (white)
        self.__puntos__[0] = [Checker('white') for _ in range(2)]   # Punto 1: 2 fichas blancas
        self.__puntos__[11] = [Checker('white') for _ in range(5)]  # Punto 12: 5 fichas blancas
        self.__puntos__[16] = [Checker('white') for _ in range(3)]  # Punto 17: 3 fichas blancas
        self.__puntos__[18] = [Checker('white') for _ in range(5)]  # Punto 19: 5 fichas blancas
        
        # Jugador negro (black)
        self.__puntos__[5] = [Checker('black') for _ in range(5)]   # Punto 6: 5 fichas negras
        self.__puntos__[7] = [Checker('black') for _ in range(3)]   # Punto 8: 3 fichas negras
        self.__puntos__[12] = [Checker('black') for _ in range(5)]  # Punto 13: 5 fichas negras
        self.__puntos__[23] = [Checker('black') for _ in range(2)]  # Punto 24: 2 fichas negras
    
    def get_puntos(self):
        """Retorna la lista de puntos del tablero."""
        return self.__puntos__
    
    def get_punto(self, posicion):
        """
        Retorna las fichas de un punto específico.
        
        Args:
            posicion (int): Número del punto (1-24)
            
        Returns:
            list: Lista de objetos Checker en ese punto, o lista vacía si no hay fichas
        """
        if 1 <= posicion <= 24:
            return self.__puntos__[posicion - 1]
        else:
            raise ValueError("La posición debe estar entre 1 y 24")
    
    def tiene_fichas(self, posicion):
        """
        Verifica si un punto tiene fichas.
        
        Args:
            posicion (int): Número del punto (1-24)
            
        Returns:
            bool: True si el punto tiene fichas
        """
        return len(self.get_punto(posicion)) > 0
    
    def get_color_punto(self, posicion):
        """
        Retorna el color de las fichas en un punto (todas deben ser del mismo color).
        
        Args:
            posicion (int): Número del punto (1-24)
            
        Returns:
            str or None: Color de las fichas o None si el punto está vacío
        """
        fichas = self.get_punto(posicion)
        if fichas:
            return fichas[0].get_color()
        return None
    
    def get_cantidad_fichas(self, posicion):
        """
        Retorna la cantidad de fichas en un punto específico.
        
        Args:
            posicion (int): Número del punto (1-24)
            
        Returns:
            int: Cantidad de fichas en el punto
        """
        return len(self.get_punto(posicion))
    
    def agregar_ficha(self, posicion, ficha):
        """
        Agrega una ficha a un punto específico.
        
        Args:
            posicion (int): Número del punto (1-24)
            ficha (Checker): Ficha a agregar
        """
        if not isinstance(ficha, Checker):
            raise ValueError("Solo se pueden agregar objetos Checker")
        
        punto = self.get_punto(posicion)
        if punto and punto[0].get_color() != ficha.get_color():
            raise ValueError("No se pueden mezclar fichas de diferentes colores en un punto")
        
        self.__puntos__[posicion - 1].append(ficha)
    
    def quitar_ficha(self, posicion):
        """
        Quita una ficha de un punto específico.
        
        Args:
            posicion (int): Número del punto (1-24)
            
        Returns:
            Checker or None: La ficha quitada o None si el punto está vacío
        """
        punto = self.get_punto(posicion)
        if punto:
            return self.__puntos__[posicion - 1].pop()
        return None
    
    def __str__(self):
        """Representación en string del tablero."""
        resultado = "Tablero de Backgammon:\n"
        for i in range(24):
            punto_num = i + 1
            fichas = self.__puntos__[i]
            if fichas:
                color = fichas[0].get_color()
                cantidad = len(fichas)
                resultado += f"Punto {punto_num:2d}: {cantidad} fichas {color}\n"
            else:
                resultado += f"Punto {punto_num:2d}: vacío\n"
        return resultado