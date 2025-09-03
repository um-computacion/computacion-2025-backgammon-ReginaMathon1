from board import Board
from player import Player
from dice import Dice


class BackgammonGame:
    def __init__(self):
        """
        Inicializa una nueva partida de Backgammon.
        
        Prepara todos los componentes necesarios para el juego:
        - Tablero con posiciones iniciales
        - Dos jugadores (blanco y negro)
        - Dados para las tiradas
        - Control de turnos
        """
        self.__board__ = None
        self.__players__ = []
        self.__dice__ = None
        self.__turno__ = 0  # Índice del jugador actual (0 o 1)
    
    def iniciar_juego(self, nombre_jugador1="Jugador 1", nombre_jugador2="Jugador 2"):
        """
        Prepara e inicializa todos los componentes del juego.
        
        Args:
            nombre_jugador1 (str): Nombre del primer jugador (fichas blancas)
            nombre_jugador2 (str): Nombre del segundo jugador (fichas negras)
        """
        # Inicializar el tablero con posiciones estándar
        self.__board__ = Board()
        
        # Crear los dos jugadores
        jugador1 = Player(nombre_jugador1, "white")
        jugador2 = Player(nombre_jugador2, "black")
        self.__players__ = [jugador1, jugador2]
        
        # Inicializar los dados
        self.__dice__ = Dice()
        
        # Determinar quién empieza (el que saque mayor valor)
        self.__determinar_primer_turno__()
    
    def __determinar_primer_turno__(self):
        """
        Determina qué jugador comienza la partida.
        Cada jugador tira un dado, quien saque mayor valor empieza.
        En caso de empate, se vuelve a tirar.
        """
        while True:
            # Cada jugador tira un dado
            dado_jugador1 = self.__dice__.tirar()[0]  # Solo tomar el primer valor
            dado_jugador2 = self.__dice__.tirar()[0]  # Solo tomar el primer valor
            
            if dado_jugador1 > dado_jugador2:
                self.__turno__ = 0  # Empieza jugador 1
                break
            elif dado_jugador2 > dado_jugador1:
                self.__turno__ = 1  # Empieza jugador 2
                break
            # Si empatan, continúa el bucle y vuelven a tirar
    
    def get_board(self):
        """Retorna el tablero actual."""
        return self.__board__
    
    def get_players(self):
        """Retorna la lista de jugadores."""
        return self.__players__
    
    def get_dice(self):
        """Retorna los dados del juego."""
        return self.__dice__
    
    def get_turno_actual(self):
        """Retorna el índice del jugador cuyo turno es actualmente."""
        return self.__turno__
    
    def get_jugador_actual(self):
        """Retorna el jugador cuyo turno es actualmente."""
        return self.__players__[self.__turno__]
    
    def cambiar_turno(self):
        """Cambia el turno al siguiente jugador."""
        self.__turno__ = 1 - self.__turno__  # Alterna entre 0 y 1
    
    def tirar_dados(self):
        """
        El jugador actual tira los dados.
        
        Returns:
            list: Lista con los valores obtenidos en la tirada
        """
        return self.__dice__.tirar()
    
    def esta_terminado(self):
        """
        Verifica si el juego ha terminado.
        
        Returns:
            bool: True si algún jugador ha ganado, False en caso contrario
        """
        return any(jugador.ha_ganado() for jugador in self.__players__)
    
    def get_ganador(self):
        """
        Retorna el jugador ganador si el juego ha terminado.
        
        Returns:
            Player or None: El jugador ganador o None si el juego continúa
        """
        for jugador in self.__players__:
            if jugador.ha_ganado():
                return jugador
        return None
    
    def reiniciar_juego(self):
        """Reinicia el juego a su estado inicial."""
        if self.__board__:
            self.__board__ = Board()
        
        for jugador in self.__players__:
            jugador.reset_fichas()
        
        self.__turno__ = 0
        self.__determinar_primer_turno__()
    
    def __str__(self):
        """Representación en string del estado actual del juego."""
        if not self.__board__:
            return "Juego no iniciado"
        
        resultado = f"=== BACKGAMMON ===\n"
        resultado += f"Turno actual: {self.get_jugador_actual().get_nombre()}\n"
        resultado += f"Jugadores:\n"
        
        for i, jugador in enumerate(self.__players__):
            marca = ">>> " if i == self.__turno__ else "    "
            resultado += f"{marca}{jugador}\n"
        
        return resultado