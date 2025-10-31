"""
Sprite para las fichas de Backgammon.
"""

import pygame
from .constants import *


class CheckerSprite:
    """Sprite para una ficha de backgammon."""
    
    def __init__(self, color, position, punto_num=None):
        """
        Inicializa una ficha.
        
        Args:
            color: 'white' o 'black'
            position: tupla (x, y) posición inicial
            punto_num: número del punto donde está la ficha (0-23) o None para barra/home
        """
        self.color = color
        self.position = list(position)
        self.punto_num = punto_num
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0
        self.original_position = list(position)
    
    def draw(self, surface, highlight=False):
        """
        Dibuja la ficha.
        
        Args:
            surface: Superficie donde dibujar
            highlight: Si debe resaltarse la ficha
        """
        color = COLOR_FICHA_WHITE if self.color == 'white' else COLOR_FICHA_BLACK
        
        if highlight:
            # Dibujar halo dorado
            pygame.draw.circle(surface, COLOR_HIGHLIGHT, 
                             (int(self.position[0]), int(self.position[1])), 
                             FICHA_RADIUS + 4)
        
        # Dibujar ficha
        pygame.draw.circle(surface, color, 
                         (int(self.position[0]), int(self.position[1])), 
                         FICHA_RADIUS)
        pygame.draw.circle(surface, COLOR_FICHA_BORDE, 
                         (int(self.position[0]), int(self.position[1])), 
                         FICHA_RADIUS, 2)
    
    def contains_point(self, point):
        """
        Verifica si un punto está dentro de la ficha.
        
        Args:
            point: tupla (x, y)
            
        Returns:
            bool: True si el punto está dentro
        """
        dx = point[0] - self.position[0]
        dy = point[1] - self.position[1]
        return dx * dx + dy * dy <= FICHA_RADIUS * FICHA_RADIUS
    
    def start_drag(self, mouse_pos):
        """Inicia el arrastre de la ficha."""
        self.dragging = True
        self.offset_x = self.position[0] - mouse_pos[0]
        self.offset_y = self.position[1] - mouse_pos[1]
        self.original_position = list(self.position)
    
    def update_drag(self, mouse_pos):
        """Actualiza la posición durante el arrastre."""
        if self.dragging:
            self.position[0] = mouse_pos[0] + self.offset_x
            self.position[1] = mouse_pos[1] + self.offset_y
    
    def end_drag(self):
        """Finaliza el arrastre."""
        self.dragging = False
    
    def return_to_original(self):
        """Devuelve la ficha a su posición original."""
        self.position = list(self.original_position)
        self.dragging = False
    
    def move_to(self, position, punto_num=None):
        """
        Mueve la ficha a una nueva posición.
        
        Args:
            position: tupla (x, y)
            punto_num: nuevo número de punto
        """
        self.position = list(position)
        self.original_position = list(position)
        if punto_num is not None:
            self.punto_num = punto_num
