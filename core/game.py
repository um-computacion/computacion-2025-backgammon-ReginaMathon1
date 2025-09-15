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
        self.__ultimo_roll__ = None
        self.__movimientos_disponibles__ = []
        self.__bar_white__ = []  # Fichas blancas capturadas
        self.__bar_black__ = []  # Fichas negras capturadas
        self.__home_white__ = []  # Fichas blancas que salieron
        self.__home_black__ = []  # Fichas negras que salieron
    
    def iniciar_juego(self, nombre_jugador1="Jugador 1", nombre_jugador2="Jugador 2"):
        """Prepara e inicializa todos los componentes del juego."""
        self.__board__ = Board()
        
        jugador1 = Player(nombre_jugador1, "white")
        jugador2 = Player(nombre_jugador2, "black")
        self.__players__ = [jugador1, jugador2]
        
        self.__dice__ = Dice()
        self.__determinar_primer_turno__()
        
        # Limpiar estado del juego
        self.__ultimo_roll__ = None
        self.__movimientos_disponibles__ = []
        self.__bar_white__ = []
        self.__bar_black__ = []
        self.__home_white__ = []
        self.__home_black__ = []
    
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
    
    def get_ultimo_roll(self):
        return self.__ultimo_roll__
    
    def get_movimientos_disponibles(self):
        return self.__movimientos_disponibles__.copy()
    
    def get_bar(self, color):
        """Retorna las fichas capturadas de un color."""
        if color == 'white':
            return self.__bar_white__.copy()
        elif color == 'black':
            return self.__bar_black__.copy()
        else:
            raise ValueError("Color debe ser 'white' o 'black'")
    
    def get_home(self, color):
        """Retorna las fichas que salieron del tablero de un color."""
        if color == 'white':
            return self.__home_white__.copy()
        elif color == 'black':
            return self.__home_black__.copy()
        else:
            raise ValueError("Color debe ser 'white' o 'black'")
    
    def cambiar_turno(self):
        self.__turno__ = 1 - self.__turno__
        self.__ultimo_roll__ = None
        self.__movimientos_disponibles__ = []
    
    def tirar_dados(self):
        """Tira los dados y actualiza los movimientos disponibles."""
        self.__ultimo_roll__ = self.__dice__.tirar()
        self.__movimientos_disponibles__ = self.__ultimo_roll__.copy()
        return self.__ultimo_roll__
    
    def hacer_movimiento(self, desde, hasta):
        """
        Ejecuta un movimiento de ficha.
        
        Args:
            desde (int): Posición origen (1-24, 0 para bar)
            hasta (int): Posición destino (1-24, 25 para home)
            
        Returns:
            bool: True si el movimiento fue exitoso
        """
        if not self.es_movimiento_valido(desde, hasta):
            return False
        
        jugador_actual = self.get_jugador_actual()
        color_jugador = jugador_actual.get_color()
        
        # Calcular distancia del movimiento
        if color_jugador == 'white':
            distancia = hasta - desde if desde != 0 else hasta
        else:
            distancia = desde - hasta if desde != 0 else 25 - hasta
        
        # Verificar que la distancia esté en movimientos disponibles
        if distancia not in self.__movimientos_disponibles__:
            return False
        
        # Ejecutar el movimiento
        if desde == 0:  # Desde bar
            ficha = self.__sacar_de_bar__(color_jugador)
        else:
            ficha = self.__board__.quitar_ficha(desde)
        
        if hasta == 25:  # A home
            self.__agregar_a_home__(ficha)
        else:
            # Verificar si hay ficha enemiga solitaria para capturar
            if (self.__board__.tiene_fichas(hasta) and 
                self.__board__.get_color_punto(hasta) != color_jugador and 
                self.__board__.get_cantidad_fichas(hasta) == 1):
                
                ficha_capturada = self.__board__.quitar_ficha(hasta)
                self.__agregar_a_bar__(ficha_capturada)
            
            self.__board__.agregar_ficha(hasta, ficha)
        
        # Remover el movimiento usado
        self.__movimientos_disponibles__.remove(distancia)
        
        return True
    
    def es_movimiento_valido(self, desde, hasta):
        """
        Verifica si un movimiento es válido según las reglas de backgammon.
        
        Args:
            desde (int): Posición origen (1-24, 0 para bar)
            hasta (int): Posición destino (1-24, 25 para home)
            
        Returns:
            bool: True si el movimiento es válido
        """
        if not self.__movimientos_disponibles__:
            return False
        
        jugador_actual = self.get_jugador_actual()
        color_jugador = jugador_actual.get_color()
        
        # Validar posiciones
        if desde < 0 or desde > 24 or hasta < 1 or hasta > 25:
            return False
        
        # Si hay fichas en el bar, debe mover desde el bar primero
        if len(self.get_bar(color_jugador)) > 0 and desde != 0:
            return False
        
        # Verificar que hay ficha en posición origen
        if desde == 0:
            if len(self.get_bar(color_jugador)) == 0:
                return False
        else:
            if (not self.__board__.tiene_fichas(desde) or 
                self.__board__.get_color_punto(desde) != color_jugador):
                return False
        
        # Calcular distancia requerida
        if color_jugador == 'white':
            distancia = hasta - desde if desde != 0 else hasta
            if distancia <= 0:
                return False
        else:
            distancia = desde - hasta if desde != 0 else 25 - hasta
            if distancia <= 0:
                return False
        
        # Verificar que la distancia está disponible
        if distancia not in self.__movimientos_disponibles__:
            return False
        
        # Verificar destino
        if hasta == 25:  # Bear off
            return self.__puede_bear_off__(color_jugador, desde)
        else:
            # No puede moverse a punto ocupado por 2+ fichas enemigas
            if (self.__board__.tiene_fichas(hasta) and 
                self.__board__.get_color_punto(hasta) != color_jugador and 
                self.__board__.get_cantidad_fichas(hasta) >= 2):
                return False
        
        return True
    
    def __puede_bear_off__(self, color, desde):
        """Verifica si un jugador puede sacar fichas del tablero."""
        # Solo puede bear off si todas las fichas están en home board
        if color == 'white':
            home_board = range(19, 25)  # Puntos 19-24
        else:
            home_board = range(1, 7)    # Puntos 1-6
        
        # Verificar que no hay fichas fuera del home board
        for i in range(1, 25):
            if (self.__board__.tiene_fichas(i) and 
                self.__board__.get_color_punto(i) == color and 
                i not in home_board):
                return False
        
        # Verificar que no hay fichas en el bar
        if len(self.get_bar(color)) > 0:
            return False
        
        return True
    
    def __sacar_de_bar__(self, color):
        """Saca una ficha del bar."""
        if color == 'white':
            return self.__bar_white__.pop()
        else:
            return self.__bar_black__.pop()
    
    def __agregar_a_bar__(self, ficha):
        """Agrega una ficha al bar."""
        if ficha.get_color() == 'white':
            self.__bar_white__.append(ficha)
        else:
            self.__bar_black__.append(ficha)
    
    def __agregar_a_home__(self, ficha):
        """Agrega una ficha al home (fuera del tablero)."""
        if ficha.get_color() == 'white':
            self.__home_white__.append(ficha)
        else:
            self.__home_black__.append(ficha)
    
    def tiene_movimientos_disponibles(self):
        """Verifica si el jugador actual tiene movimientos disponibles."""
        if not self.__movimientos_disponibles__:
            return False
        
        jugador_actual = self.get_jugador_actual()
        color_jugador = jugador_actual.get_color()
        
        # Si hay fichas en el bar, verificar si puede entrar
        if len(self.get_bar(color_jugador)) > 0:
            for distancia in self.__movimientos_disponibles__:
                if color_jugador == 'white':
                    punto_entrada = distancia
                else:
                    punto_entrada = 25 - distancia
                
                if self.es_movimiento_valido(0, punto_entrada):
                    return True
            return False
        
        # Verificar movimientos desde el tablero
        for i in range(1, 25):
            if (self.__board__.tiene_fichas(i) and 
                self.__board__.get_color_punto(i) == color_jugador):
                
                for distancia in self.__movimientos_disponibles__:
                    if color_jugador == 'white':
                        destino = i + distancia
                    else:
                        destino = i - distancia
                    
                    if destino > 24:
                        destino = 25  # Bear off
                    
                    if destino >= 1 and self.es_movimiento_valido(i, destino):
                        return True
        
        return False
    
    def esta_terminado(self):
        """Verifica si el juego ha terminado."""
        for jugador in self.__players__:
            if len(self.get_home(jugador.get_color())) == 15:
                return True
        return False
    
    def get_ganador(self):
        """Retorna el jugador ganador si el juego terminó."""
        for jugador in self.__players__:
            if len(self.get_home(jugador.get_color())) == 15:
                return jugador
        return None
    
    def reiniciar_juego(self):
        """Reinicia el juego a su estado inicial."""
        self.__board__ = None
        self.__players__ = []
        self.__dice__ = None
        self.__turno__ = 0
        self.__ultimo_roll__ = None
        self.__movimientos_disponibles__ = []
        self.__bar_white__ = []
        self.__bar_black__ = []
        self.__home_white__ = []
        self.__home_black__ = []
    
    def get_estado_juego(self):
        """Retorna un diccionario con el estado actual del juego."""
        return {
            'jugador_actual': self.get_jugador_actual().get_nombre() if self.__players__ else None,
            'ultimo_roll': self.__ultimo_roll__,
            'movimientos_disponibles': self.__movimientos_disponibles__.copy(),
            'bar_white': len(self.__bar_white__),
            'bar_black': len(self.__bar_black__),
            'home_white': len(self.__home_white__),
            'home_black': len(self.__home_black__),
            'terminado': self.esta_terminado(),
            'ganador': self.get_ganador().get_nombre() if self.get_ganador() else None
        }
    
    def __str__(self):
        """Representación en string del juego."""
        if not self.__players__:
            return "Juego no iniciado"
        
        estado = self.get_estado_juego()
        return (f"Backgammon Game\n"
                f"Jugador actual: {estado['jugador_actual']}\n"
                f"Último roll: {estado['ultimo_roll']}\n"
                f"Movimientos disponibles: {estado['movimientos_disponibles']}\n"
                f"Bar - Blancas: {estado['bar_white']}, Negras: {estado['bar_black']}\n"
                f"Home - Blancas: {estado['home_white']}, Negras: {estado['home_black']}\n"
                f"Estado: {'Terminado' if estado['terminado'] else 'En progreso'}")