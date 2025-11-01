"""
Renderer para el tablero de Backgammon.
"""

import pygame
from .constants import *


class BoardRenderer:
    """Renderiza el tablero de backgammon."""
    
    def __init__(self, surface):
        """
        Inicializa el renderer del tablero.
        
        Args:
            surface: Superficie de pygame donde dibujar
        """
        self.surface = surface
        self.font = pygame.font.Font(None, 20)
        self.font_large = pygame.font.Font(None, 32)
    
    def draw_board(self):
        """Dibuja el tablero completo."""
        self.surface.fill(COLOR_BG)
        self._draw_background()
        self._draw_barra()
        self._draw_puntos()
        self._draw_labels()
        self._draw_home_areas()
    
    def _draw_background(self):
        """Dibuja el fondo del tablero."""
        # Tablero principal
        board_width = 12 * PUNTO_WIDTH + BARRA_WIDTH
        board_height = 2 * PUNTO_HEIGHT
        
        pygame.draw.rect(
            self.surface,
            (101, 67, 33),
            (BOARD_MARGIN, BOARD_MARGIN, board_width, board_height),
            border_radius=10
        )
        
        # Borde decorativo
        pygame.draw.rect(
            self.surface,
            (139, 69, 19),
            (BOARD_MARGIN - 5, BOARD_MARGIN - 5, board_width + 10, board_height + 10),
            5,
            border_radius=10
        )
    
    def _draw_puntos(self):
        """Dibuja los 24 puntos triangulares del tablero."""
        for i in range(24):
            self._draw_punto(i)
    
    def _draw_punto(self, punto_num):
        """
        Dibuja un punto triangular.
        
        Disposición del tablero (vista desde jugador blanco):
        Arriba: 13 14 15 16 17 18 | BAR | 19 20 21 22 23 24
        Abajo:  12 11 10  9  8  7 | BAR |  6  5  4  3  2  1
        
        Args:
            punto_num: Número del punto (0-23, correspondiente a puntos 1-24)
        """
        punto_real = punto_num + 1  # punto_num es 0-23, punto_real es 1-24
        
        # Determinar cuadrante y posición
        if 1 <= punto_real <= 6:
            # Inferior derecha (puntos 1-6): de derecha a izquierda
            col = 6 - punto_real  # 6->0, 5->1, 4->2, 3->3, 2->4, 1->5
            x = BOARD_MARGIN + BARRA_WIDTH + 6 * PUNTO_WIDTH + col * PUNTO_WIDTH
            y_base = BOARD_MARGIN + 2 * PUNTO_HEIGHT
            direction = -1  # Apunta hacia arriba
        elif 7 <= punto_real <= 12:
            # Inferior izquierda (puntos 7-12): de derecha a izquierda
            col = 12 - punto_real  # 12->0, 11->1, 10->2, 9->3, 8->4, 7->5
            x = BOARD_MARGIN + col * PUNTO_WIDTH
            y_base = BOARD_MARGIN + 2 * PUNTO_HEIGHT
            direction = -1  # Apunta hacia arriba
        elif 13 <= punto_real <= 18:
            # Superior izquierda (puntos 13-18): de izquierda a derecha
            col = punto_real - 13  # 13->0, 14->1, 15->2, 16->3, 17->4, 18->5
            x = BOARD_MARGIN + col * PUNTO_WIDTH
            y_base = BOARD_MARGIN
            direction = 1  # Apunta hacia abajo
        else:  # 19 <= punto_real <= 24
            # Superior derecha (puntos 19-24): de izquierda a derecha
            col = punto_real - 19  # 19->0, 20->1, 21->2, 22->3, 23->4, 24->5
            x = BOARD_MARGIN + BARRA_WIDTH + 6 * PUNTO_WIDTH + col * PUNTO_WIDTH
            y_base = BOARD_MARGIN
            direction = 1  # Apunta hacia abajo
        
        # Color alternado
        color = COLOR_PUNTO_CLARO if punto_num % 2 == 0 else COLOR_PUNTO_OSCURO
        
        # Dibujar triángulo
        if direction == 1:
            points = [
                (x, y_base),
                (x + PUNTO_WIDTH, y_base),
                (x + PUNTO_WIDTH // 2, y_base + PUNTO_HEIGHT)
            ]
        else:
            points = [
                (x, y_base),
                (x + PUNTO_WIDTH, y_base),
                (x + PUNTO_WIDTH // 2, y_base - PUNTO_HEIGHT)
            ]
        
        pygame.draw.polygon(self.surface, color, points)
        pygame.draw.polygon(self.surface, (80, 50, 20), points, 2)
    
    def _draw_barra(self):
        """Dibuja la barra central."""
        x = BOARD_MARGIN + 6 * PUNTO_WIDTH
        pygame.draw.rect(
            self.surface,
            COLOR_BARRA,
            (x, BOARD_MARGIN, BARRA_WIDTH, 2 * PUNTO_HEIGHT)
        )
        
        # Texto "BAR"
        text = self.font_large.render("BAR", True, COLOR_TEXTO)
        text_rect = text.get_rect(center=(x + BARRA_WIDTH // 2, BOARD_MARGIN + PUNTO_HEIGHT))
        self.surface.blit(text, text_rect)
    
    def _draw_labels(self):
        """Dibuja las etiquetas de los puntos."""
        for i in range(24):
            punto_num = i + 1
            pos = self.get_punto_position(i)
            
            # Determinar si está arriba o abajo
            if punto_num >= 13:
                y_offset = -25
            else:
                y_offset = 35
            
            label = self.font.render(str(punto_num), True, (255, 255, 200))
            label_rect = label.get_rect(center=(pos[0], pos[1] + y_offset))
            
            # Fondo semi-transparente
            bg_surface = pygame.Surface((30, 25))
            bg_surface.set_alpha(150)
            bg_surface.fill((50, 50, 50))
            bg_rect = bg_surface.get_rect(center=label_rect.center)
            self.surface.blit(bg_surface, bg_rect)
            
            self.surface.blit(label, label_rect)
    
    def _draw_home_areas(self):
        """Dibuja las áreas HOME para fichas sacadas."""
        board_width = 12 * PUNTO_WIDTH + BARRA_WIDTH
        
        # HOME más amplio y centrado verticalmente
        home_x = BOARD_MARGIN + board_width + 20
        home_y_top = BOARD_MARGIN + 20
        home_y_bottom = BOARD_MARGIN + 2 * PUNTO_HEIGHT - HOME_HEIGHT - 20
        
        # HOME superior (blancas) - CORREGIDO
        pygame.draw.rect(self.surface, (255, 255, 255), 
                        (home_x, home_y_top, HOME_WIDTH, HOME_HEIGHT))
        pygame.draw.rect(self.surface, COLOR_PUNTO_CLARO, 
                        (home_x, home_y_top, HOME_WIDTH, HOME_HEIGHT), 3)
        
        # HOME inferior (negras) - CORREGIDO
        pygame.draw.rect(self.surface, (255, 255, 255), 
                        (home_x, home_y_bottom, HOME_WIDTH, HOME_HEIGHT))
        pygame.draw.rect(self.surface, COLOR_PUNTO_OSCURO, 
                        (home_x, home_y_bottom, HOME_WIDTH, HOME_HEIGHT), 3)
        
        # Etiquetas
        font = pygame.font.Font(None, 24)
        label_top = font.render("HOME", True, (50, 50, 50))
        label_bottom = font.render("HOME", True, (50, 50, 50))
        
        self.surface.blit(label_top, (home_x + 25, home_y_top - 25))
        self.surface.blit(label_bottom, (home_x + 25, home_y_bottom + HOME_HEIGHT + 5))
    
    def get_punto_position(self, punto_num):
        """
        Obtiene la posición central de un punto.
        
        Args:
            punto_num: Número del punto (0-23)
            
        Returns:
            tuple: (x, y) posición central del punto base
        """
        punto_real = punto_num + 1
        
        if 1 <= punto_real <= 6:
            # Inferior derecha
            col = 6 - punto_real
            x = BOARD_MARGIN + BARRA_WIDTH + 6 * PUNTO_WIDTH + col * PUNTO_WIDTH + PUNTO_WIDTH // 2
            y = BOARD_MARGIN + 2 * PUNTO_HEIGHT
        elif 7 <= punto_real <= 12:
            # Inferior izquierda
            col = 12 - punto_real
            x = BOARD_MARGIN + col * PUNTO_WIDTH + PUNTO_WIDTH // 2
            y = BOARD_MARGIN + 2 * PUNTO_HEIGHT
        elif 13 <= punto_real <= 18:
            # Superior izquierda
            col = punto_real - 13
            x = BOARD_MARGIN + col * PUNTO_WIDTH + PUNTO_WIDTH // 2
            y = BOARD_MARGIN
        else:  # 19 <= punto_real <= 24
            # Superior derecha
            col = punto_real - 19
            x = BOARD_MARGIN + BARRA_WIDTH + 6 * PUNTO_WIDTH + col * PUNTO_WIDTH + PUNTO_WIDTH // 2
            y = BOARD_MARGIN
        
        return (x, y)
    
    def get_bar_position(self, color):
        """
        Obtiene la posición de la barra para un color.
        
        Args:
            color: 'white' o 'black'
            
        Returns:
            tuple: (x, y) posición de la barra
        """
        x = BOARD_MARGIN + 6 * PUNTO_WIDTH + BARRA_WIDTH // 2
        if color == 'white':
            y = BOARD_MARGIN + 3 * PUNTO_HEIGHT // 2
        else:
            y = BOARD_MARGIN + PUNTO_HEIGHT // 2
        return (x, y)
    
    def get_home_position(self, color):
        """
        Retorna la posición del área HOME para un color.
        
        Args:
            color: 'white' o 'black'
            
        Returns:
            tuple: (x, y) posición inicial para apilar fichas en HOME
        """
        board_width = 12 * PUNTO_WIDTH + BARRA_WIDTH
        home_x = BOARD_MARGIN + board_width + 30  # Más margen interno
        
        # CORREGIDO: blancas arriba, negras abajo
        if color == 'white':
            home_y = BOARD_MARGIN + 30  # Arriba para blancas
        else:
            home_y = BOARD_MARGIN + 2 * PUNTO_HEIGHT - HOME_HEIGHT - 10  # Abajo para negras
        
        return (home_x, home_y)
