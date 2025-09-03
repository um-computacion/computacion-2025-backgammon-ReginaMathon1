from .board import Board
from .player import Player
from .dice import Dice


class Game:
    def __init__(self):
        """
        Inicializa una nueva partida de Backgammon.
        """
        self.__board__ = None
        self.__players__ = []
        self.__dice__ = None
        self.__turno__ = 0
    
    def iniciar_juego(self, nombre_jugador1="Jugador 1", nombre_jugador2="Jugador 2"):
        """Prepara e inicializa todos los componentes del juego."""
        self.__board__ = Board()
        
        jugador1 = Player(nombre_jugador1, "white")
        jugador2 = Player(nombre_jugador2, "black")
        self.__players__ = [jugador1, jugador2]
        
        self.__dice__ = Dice()
        self.__determinar_primer_turno__()
    
    def __determinar_primer_turno__(self):
        """Determina qué jugador comienza la partida."""
        while True:
            dado_jugador1 = self.__dice__.tirar()[0]
            dado_jugador2 = self.__dice__.tirar()[0]
            
            if dado_jugador1 > dado_jugador2:
                self.__turno__ = 0
                break
            elif dado_jugador2 > dado_jugador1:
                self.__turno__ = 1
                break
    
    def get_board(self):
        return self.__board__
    
    def get_players(self):
        return self.__players__
    
    def get_dice(self):
        return self.__dice__
    
    def get_turno_actual(self):
        return self.__turno__
    
    def get_jugador_actual(self):
        return self.__players__[self.__turno__]
    
    def cambiar_turno(self):
        self.__turno__ = 1 - self.__turno__
    
    def tirar_dados(self):
        return self.__dice__.tirar()
    
    def esta_terminado(self):
        return any(jugador.ha_ganado() for jugador in self.__players__)
    
    def get_ganador(self):
        for jugador in self.__players__:
            if jugador.ha_ganado():
                return jugador
        return None