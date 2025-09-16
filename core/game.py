from .board import Board
from .player import Player
from .dice import Dice


class Game:
    def __init__(self):
        """Inicializa una nueva partida de Backgammon."""
        self.__board__ = None
        self.__players__ = []
        self.__dice__ = None
        self.__turno__ = 0
        self.__ultimo_roll__ = None
        self.__movimientos_disponibles__ = []
        self.__bar__ = {'white': [], 'black': []}  # Fichas capturadas
        self.__home__ = {'white': [], 'black': []}  # Fichas que salieron
    
    def iniciar_juego(self, nombre_jugador1="Jugador 1", nombre_jugador2="Jugador 2"):
        """Prepara e inicializa todos los componentes del juego."""
        self.__board__ = Board()
        self.__players__ = [Player(nombre_jugador1, "white"), Player(nombre_jugador2, "black")]
        self.__dice__ = Dice()
        self.__determinar_primer_turno__()
        self.__ultimo_roll__ = None
        self.__movimientos_disponibles__ = []
        self.__bar__ = {'white': [], 'black': []}
        self.__home__ = {'white': [], 'black': []}
    
    def __determinar_primer_turno__(self):
        """Determina qué jugador comienza la partida."""
        while True:
            dados = [self.__dice__.tirar()[0] for _ in range(2)]
            if dados[0] != dados[1]:
                self.__turno__ = 0 if dados[0] > dados[1] else 1
                break
    
    # Getters simplificados
    def get_board(self): return self.__board__
    def get_players(self): return self.__players__
    def get_dice(self): return self.__dice__
    def get_turno_actual(self): return self.__turno__
    def get_jugador_actual(self): return self.__players__[self.__turno__]
    def get_ultimo_roll(self): return self.__ultimo_roll__
    def get_movimientos_disponibles(self): return self.__movimientos_disponibles__.copy()
    def get_bar(self, color): return self.__bar__[color].copy()
    def get_home(self, color): return self.__home__[color].copy()
    
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
        """Ejecuta un movimiento de ficha."""
        if not self.es_movimiento_valido(desde, hasta):
            return False
        
        color_jugador = self.get_jugador_actual().get_color()
        distancia = self.__calcular_distancia__(desde, hasta, color_jugador)
        
        # Mover ficha
        ficha = self.__bar__[color_jugador].pop() if desde == 0 else self.__board__.quitar_ficha(desde)
        
        if hasta == 25:
            self.__home__[color_jugador].append(ficha)
        else:
            # Capturar ficha enemiga si existe
            if (self.__board__.tiene_fichas(hasta) and 
                self.__board__.get_color_punto(hasta) != color_jugador and 
                self.__board__.get_cantidad_fichas(hasta) == 1):
                ficha_capturada = self.__board__.quitar_ficha(hasta)
                self.__bar__[ficha_capturada.get_color()].append(ficha_capturada)
            
            self.__board__.agregar_ficha(hasta, ficha)
        
        self.__movimientos_disponibles__.remove(distancia)
        return True
    
    def __calcular_distancia__(self, desde, hasta, color):
        """Calcula la distancia del movimiento."""
        if color == 'white':
            return hasta - desde if desde != 0 else hasta
        else:
            return desde - hasta if desde != 0 else 25 - hasta
    
    def es_movimiento_valido(self, desde, hasta):
        """Verifica si un movimiento es válido."""
        if not self.__movimientos_disponibles__ or desde < 0 or desde > 24 or hasta < 1 or hasta > 25:
            return False
        
        color_jugador = self.get_jugador_actual().get_color()
        
        # Verificar origen
        if desde == 0:
            if not self.__bar__[color_jugador]:
                return False
        else:
            if (not self.__board__.tiene_fichas(desde) or 
                self.__board__.get_color_punto(desde) != color_jugador):
                return False
            # Debe mover desde bar primero si hay fichas allí
            if self.__bar__[color_jugador] and desde != 0:
                return False
        
        distancia = self.__calcular_distancia__(desde, hasta, color_jugador)
        if distancia <= 0 or distancia not in self.__movimientos_disponibles__:
            return False
        
        # Verificar destino
        if hasta == 25:
            return self.__puede_bear_off__(color_jugador)
        else:
            return not (self.__board__.tiene_fichas(hasta) and 
                       self.__board__.get_color_punto(hasta) != color_jugador and 
                       self.__board__.get_cantidad_fichas(hasta) >= 2)
    
    def __puede_bear_off__(self, color):
        """Verifica si puede sacar fichas del tablero."""
        if self.__bar__[color]:
            return False
        
        home_board = range(19, 25) if color == 'white' else range(1, 7)
        
        for i in range(1, 25):
            if (self.__board__.tiene_fichas(i) and 
                self.__board__.get_color_punto(i) == color and 
                i not in home_board):
                return False
        return True
    
    def tiene_movimientos_disponibles(self):
        """Verifica si hay movimientos disponibles."""
        if not self.__movimientos_disponibles__:
            return False
        
        color_jugador = self.get_jugador_actual().get_color()
        
        # Verificar movimientos desde bar
        if self.__bar__[color_jugador]:
            for distancia in self.__movimientos_disponibles__:
                punto_entrada = distancia if color_jugador == 'white' else 25 - distancia
                if self.es_movimiento_valido(0, punto_entrada):
                    return True
            return False
        
        # Verificar movimientos desde tablero
        for i in range(1, 25):
            if (self.__board__.tiene_fichas(i) and 
                self.__board__.get_color_punto(i) == color_jugador):
                
                for distancia in self.__movimientos_disponibles__:
                    if color_jugador == 'white':
                        destino = min(i + distancia, 25)
                    else:
                        destino = max(i - distancia, 1) if i - distancia >= 1 else 25
                    
                    if self.es_movimiento_valido(i, destino):
                        return True
        return False
    
    def esta_terminado(self):
        """Verifica si el juego terminó."""
        return any(len(self.__home__[jugador.get_color()]) == 15 for jugador in self.__players__)
    
    def get_ganador(self):
        """Retorna el ganador."""
        for jugador in self.__players__:
            if len(self.__home__[jugador.get_color()]) == 15:
                return jugador
        return None
    
    def reiniciar_juego(self):
        """Reinicia el juego."""
        self.__init__()
    
    def get_estado_juego(self):
        """Estado actual del juego."""
        return {
            'jugador_actual': self.get_jugador_actual().get_nombre() if self.__players__ else None,
            'ultimo_roll': self.__ultimo_roll__,
            'movimientos_disponibles': self.__movimientos_disponibles__.copy(),
            'bar_white': len(self.__bar__['white']),
            'bar_black': len(self.__bar__['black']),
            'home_white': len(self.__home__['white']),
            'home_black': len(self.__home__['black']),
            'terminado': self.esta_terminado(),
            'ganador': self.get_ganador().get_nombre() if self.get_ganador() else None
        }
    
    def __str__(self):
        """Representación string del juego."""
        if not self.__players__:
            return "Juego no iniciado"
        
        estado = self.get_estado_juego()
        return (f"Backgammon - {estado['jugador_actual']} | "
                f"Roll: {estado['ultimo_roll']} | "
                f"Movimientos: {estado['movimientos_disponibles']} | "
                f"Bar B/N: {estado['bar_white']}/{estado['bar_black']} | "
                f"Home B/N: {estado['home_white']}/{estado['home_black']} | "
                f"{'Terminado' if estado['terminado'] else 'En progreso'}")