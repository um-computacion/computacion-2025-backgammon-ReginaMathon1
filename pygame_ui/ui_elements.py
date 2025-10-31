"""
Elementos de UI para el juego.
"""

import pygame
from .constants import *


class Button:
    """Botón clickeable."""
    
    def __init__(self, x, y, width, height, text, callback):
        """
        Inicializa un botón.
        
        Args:
            x, y: posición
            width, height: dimensiones
            text: texto del botón
            callback: función a llamar al hacer click
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.callback = callback
        self.hovered = False
        self.font = pygame.font.Font(None, 28)
    
    def draw(self, surface):
        """Dibuja el botón."""
        color = COLOR_BOTON_HOVER if self.hovered else COLOR_BOTON
        pygame.draw.rect(surface, color, self.rect, border_radius=5)
        pygame.draw.rect(surface, COLOR_TEXTO, self.rect, 2, border_radius=5)
        
        text_surface = self.font.render(self.text, True, COLOR_TEXTO)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
    
    def handle_event(self, event):
        """Maneja eventos del botón."""
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()
                return True
        return False


class DiceDisplay:
    """Display para los dados."""
    
    def __init__(self, x, y):
        """
        Inicializa el display de dados.
        
        Args:
            x, y: posición
        """
        self.x = x
        self.y = y
        self.valores = None
        self.font = pygame.font.Font(None, 48)
    
    def set_valores(self, valores):
        """Establece los valores de los dados."""
        self.valores = valores
    
    def draw(self, surface):
        """Dibuja los dados."""
        if not self.valores:
            return
        
        for i, valor in enumerate(self.valores[:2]):  # Mostrar solo los 2 primeros
            x = self.x + i * (DADO_SIZE + DADO_MARGIN)
            self._draw_dado(surface, x, self.y, valor)
        
        # Si hay dobles, mostrar indicador
        if len(self.valores) == 4:
            text = self.font.render("x4", True, COLOR_TEXTO)
            surface.blit(text, (self.x + 2 * (DADO_SIZE + DADO_MARGIN), self.y + DADO_SIZE // 4))
    
    def _draw_dado(self, surface, x, y, valor):
        """Dibuja un dado individual."""
        # Fondo blanco
        pygame.draw.rect(surface, COLOR_DADO_BG, 
                        (x, y, DADO_SIZE, DADO_SIZE), 
                        border_radius=5)
        pygame.draw.rect(surface, COLOR_DADO_PUNTO, 
                        (x, y, DADO_SIZE, DADO_SIZE), 2, 
                        border_radius=5)
        
        # Dibujar puntos según el valor
        self._draw_dado_puntos(surface, x, y, valor)
    
    def _draw_dado_puntos(self, surface, x, y, valor):
        """Dibuja los puntos del dado."""
        radius = 4
        margin = 12
        
        # Posiciones de los puntos
        positions = {
            1: [(DADO_SIZE // 2, DADO_SIZE // 2)],
            2: [(margin, margin), (DADO_SIZE - margin, DADO_SIZE - margin)],
            3: [(margin, margin), (DADO_SIZE // 2, DADO_SIZE // 2), (DADO_SIZE - margin, DADO_SIZE - margin)],
            4: [(margin, margin), (DADO_SIZE - margin, margin), 
                (margin, DADO_SIZE - margin), (DADO_SIZE - margin, DADO_SIZE - margin)],
            5: [(margin, margin), (DADO_SIZE - margin, margin), (DADO_SIZE // 2, DADO_SIZE // 2),
                (margin, DADO_SIZE - margin), (DADO_SIZE - margin, DADO_SIZE - margin)],
            6: [(margin, margin), (DADO_SIZE - margin, margin), 
                (margin, DADO_SIZE // 2), (DADO_SIZE - margin, DADO_SIZE // 2),
                (margin, DADO_SIZE - margin), (DADO_SIZE - margin, DADO_SIZE - margin)]
        }
        
        for px, py in positions.get(valor, []):
            pygame.draw.circle(surface, COLOR_DADO_PUNTO, (x + px, y + py), radius)


class InfoPanel:
    """Panel de información del juego."""
    
    def __init__(self, x, y, width, height):
        """Inicializa el panel de información."""
        self.rect = pygame.Rect(x, y, width, height)
        self.font_title = pygame.font.Font(None, 36)
        self.font_text = pygame.font.Font(None, 24)
        self.info = {}
    
    def update_info(self, info_dict):
        """Actualiza la información a mostrar."""
        self.info = info_dict
    
    def draw(self, surface):
        """Dibuja el panel."""
        # Fondo semi-transparente
        s = pygame.Surface((self.rect.width, self.rect.height))
        s.set_alpha(200)
        s.fill((50, 50, 50))
        surface.blit(s, (self.rect.x, self.rect.y))
        
        # Borde
        pygame.draw.rect(surface, COLOR_TEXTO, self.rect, 2)
        
        y_offset = self.rect.y + 20
        
        # Título
        if 'jugador' in self.info:
            title = self.font_title.render(f"Turno: {self.info['jugador']}", True, COLOR_TEXTO)
            surface.blit(title, (self.rect.x + 20, y_offset))
            y_offset += 50
        
        # Información adicional
        for key, value in self.info.items():
            if key != 'jugador':
                text = self.font_text.render(f"{key}: {value}", True, COLOR_TEXTO)
                surface.blit(text, (self.rect.x + 20, y_offset))
                y_offset += 30


class TextInput:
    """Campo de texto para entrada de usuario."""
    
    def __init__(self, x, y, width, height, placeholder=""):
        """
        Inicializa un campo de texto.
        
        Args:
            x, y: posición
            width, height: dimensiones
            placeholder: texto de ejemplo
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.placeholder = placeholder
        self.text = ""
        self.active = False
        self.font = pygame.font.Font(None, 32)
        self.cursor_visible = True
        self.cursor_timer = 0
    
    def draw(self, surface):
        """Dibuja el campo de texto."""
        # Fondo
        color = (70, 130, 180) if self.active else (100, 100, 100)
        pygame.draw.rect(surface, color, self.rect, border_radius=5)
        pygame.draw.rect(surface, COLOR_TEXTO, self.rect, 2, border_radius=5)
        
        # Texto
        display_text = self.text if self.text else self.placeholder
        text_color = COLOR_TEXTO if self.text else (150, 150, 150)
        text_surface = self.font.render(display_text, True, text_color)
        
        # Centrar texto verticalmente
        text_rect = text_surface.get_rect(midleft=(self.rect.x + 10, self.rect.centery))
        surface.blit(text_surface, text_rect)
        
        # Cursor parpadeante
        if self.active and self.cursor_visible:
            cursor_x = text_rect.right + 2
            cursor_y = self.rect.centery - 12
            pygame.draw.line(surface, COLOR_TEXTO, 
                           (cursor_x, cursor_y), 
                           (cursor_x, cursor_y + 24), 2)
    
    def handle_event(self, event):
        """Maneja eventos del campo de texto."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        
        if self.active and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                return True  # Enter presionado
            elif len(self.text) < 15:  # Límite de caracteres
                if event.unicode.isprintable():
                    self.text += event.unicode
        
        return False
    
    def update(self):
        """Actualiza el cursor parpadeante."""
        self.cursor_timer += 1
        if self.cursor_timer >= 30:  # Parpadea cada 30 frames
            self.cursor_visible = not self.cursor_visible
            self.cursor_timer = 0
    
    def get_text(self):
        """Retorna el texto ingresado."""
        return self.text if self.text else self.placeholder
    
    def reset(self):
        """Limpia el campo de texto."""
        self.text = ""
        self.active = False
