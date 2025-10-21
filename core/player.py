class Player:
    def __init__(self, nombre, color):
        """
        Inicializa un jugador de backgammon.
        Args:
            nombre (str): Nombre del jugador
            color (str): Color de las fichas ('white' o 'black')
        """
        self.__nombre__ = nombre
        self.__color__ = color
        self.__fichas__ = 15  # Cada jugador empieza con 15 fichas
    
    def get_nombre(self):
        """Retorna el nombre del jugador."""
        return self.__nombre__
    
    def get_color(self):
        """Retorna el color de las fichas del jugador."""
        return self.__color__
    
    def get_fichas(self):
        """Retorna la cantidad de fichas restantes del jugador."""
        return self.__fichas__
    
    def set_fichas(self, cantidad):
        """
        Establece la cantidad de fichas del jugador.
        
        Args:
            cantidad (int): Nueva cantidad de fichas
        """
        if cantidad >= 0:
            self.__fichas__ = cantidad
        else:
            raise ValueError("La cantidad de fichas no puede ser negativa")
    
    def reset_fichas(self):
        """Reinicia las fichas del jugador a 15 (valor inicial)."""
        self.__fichas__ = 15
    
    def quitar_ficha(self):
        """
        Quita una ficha del jugador (cuando mueve una ficha del tablero).
        
        Returns:
            bool: True si se pudo quitar la ficha, False si no hay fichas disponibles
        """
        if self.__fichas__ > 0:
            self.__fichas__ -= 1
            return True
        return False
    
    def agregar_ficha(self):
        """Agrega una ficha al jugador (cuando una ficha es capturada)."""
        self.__fichas__ += 1
    
    def ha_ganado(self):
        """
        Verifica si el jugador ha ganado (no tiene fichas en el tablero).
        
        Returns:
            bool: True si el jugador ha ganado, False en caso contrario
        """
        return self.__fichas__ == 0
    
    def __str__(self):
        """Representación en string del jugador."""
        return f"Jugador: {self.__nombre__} ({self.__color__}) - Fichas: {self.__fichas__}"
    
    def __eq__(self, other):
        """Compara dos jugadores por nombre y color."""
        if isinstance(other, Player):
            return self.__nombre__ == other.__nombre__ and self.__color__ == other.__color__
        return False