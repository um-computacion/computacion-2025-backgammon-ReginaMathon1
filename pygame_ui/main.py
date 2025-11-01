"""
Interfaz gráfica principal con Pygame para Backgammon.
"""

import pygame
import sys
from core.game import Game
from .constants import *
from .board_renderer import BoardRenderer
from .checker_sprite import CheckerSprite
from .ui_elements import Button, DiceDisplay, InfoPanel, TextInput


class BackgammonPygame:
    """Interfaz gráfica de Backgammon con Pygame."""
    
    def __init__(self):
        """Inicializa la interfaz Pygame."""
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Backgammon")
        self.clock = pygame.time.Clock()
        
        # Game core
        self.game = Game()
        self.game_started = False
        self.show_start_screen = True
        
        # Renderers
        self.board_renderer = BoardRenderer(self.screen)
        
        # Sprites
        self.checker_sprites = []
        self.selected_checker = None
        
        # UI Elements
        self.dice_display = DiceDisplay(WINDOW_WIDTH - 250, 100)
        self.info_panel = InfoPanel(WINDOW_WIDTH - 300, 200, 250, 400)
        self._create_buttons()
        self._create_start_screen_elements()
        
        self.running = True
    
    def _create_start_screen_elements(self):
        """Crea los elementos de la pantalla de inicio."""
        center_x = WINDOW_WIDTH // 2
        center_y = WINDOW_HEIGHT // 2
        
        # Campos de texto para nombres
        self.input_player1 = TextInput(
            center_x - 200, center_y - 80, 400, 50,
            "Jugador 1 (Blancas)"
        )
        
        self.input_player2 = TextInput(
            center_x - 200, center_y + 20, 400, 50,
            "Jugador 2 (Negras)"
        )
        
        # Botón para comenzar
        self.btn_start = Button(
            center_x - 100, center_y + 120, 200, 50,
            "COMENZAR", self._on_start_game
        )
    
    def _create_buttons(self):
        """Crea los botones de la interfaz de juego."""
        self.buttons = []
        
        # Botón tirar dados
        self.btn_roll = Button(
            WINDOW_WIDTH - 280, 650, BOTON_WIDTH, BOTON_HEIGHT,
            "Tirar Dados", self._on_roll_dice
        )
        self.buttons.append(self.btn_roll)
        
        # Botón cambiar turno
        self.btn_change_turn = Button(
            WINDOW_WIDTH - 280, 710, BOTON_WIDTH, BOTON_HEIGHT,
            "Cambiar Turno", self._on_change_turn
        )
        self.buttons.append(self.btn_change_turn)
        
        # Botón nueva partida
        self.btn_new_game = Button(
            WINDOW_WIDTH - 280, 770, BOTON_WIDTH, BOTON_HEIGHT,
            "Nueva Partida", self._on_new_game
        )
        self.buttons.append(self.btn_new_game)
    
    def _on_start_game(self):
        """Callback para comenzar el juego desde la pantalla de inicio."""
        nombre1 = self.input_player1.get_text()
        nombre2 = self.input_player2.get_text()
        
        self.game.iniciar_juego(nombre1, nombre2)
        self.game_started = True
        self.show_start_screen = False
        self._create_checker_sprites()
        self.dice_display.set_valores(None)
    
    def _on_roll_dice(self):
        """Callback para tirar dados."""
        if self.game_started and not self.game.get_ultimo_roll():
            dados = self.game.tirar_dados()
            self.dice_display.set_valores(dados)
    
    def _on_change_turn(self):
        """Callback para cambiar turno."""
        if self.game_started:
            self.game.cambiar_turno()
            self.dice_display.set_valores(None)
    
    def _on_new_game(self):
        """Callback para nueva partida."""
        self.show_start_screen = True
        self.game_started = False
        self.input_player1.reset()
        self.input_player2.reset()
        self.dice_display.set_valores(None)
    
    def _create_checker_sprites(self):
        """Crea los sprites de las fichas según el estado del tablero."""
        self.checker_sprites = []
        board = self.game.get_board()
        
        for punto_num in range(24):
            fichas = board.get_punto(punto_num + 1)
            pos = self.board_renderer.get_punto_position(punto_num)
            
            for idx, ficha in enumerate(fichas):
                # Calcular posición vertical con apilamiento
                punto_real = punto_num + 1
                
                if punto_real <= 12:
                    # Puntos inferiores (1-12) - fichas suben
                    y = pos[1] - 40 - idx * (FICHA_RADIUS * 2 + FICHA_SPACING)
                else:
                    # Puntos superiores (13-24) - fichas bajan
                    y = pos[1] + 40 + idx * (FICHA_RADIUS * 2 + FICHA_SPACING)
                
                sprite = CheckerSprite(ficha.get_color(), (pos[0], y), punto_num)
                self.checker_sprites.append(sprite)
        
        # Fichas en barra
        for color in ['white', 'black']:
            bar_fichas = self.game.get_bar(color)
            bar_pos = self.board_renderer.get_bar_position(color)
            for idx, ficha in enumerate(bar_fichas):
                x = bar_pos[0] + (idx % 2) * (FICHA_RADIUS + 3) - FICHA_RADIUS // 2
                y = bar_pos[1] + (idx // 2) * (FICHA_RADIUS * 2 + FICHA_SPACING)
                sprite = CheckerSprite(color, (x, y), None)
                self.checker_sprites.append(sprite)
            
            # Fichas en HOME - organizadas en columnas de 5
            home_fichas = self.game.get_home(color)
            home_pos = self.board_renderer.get_home_position(color)
            
            for idx, ficha in enumerate(home_fichas):
                # 3 columnas, 5 fichas por columna
                col = idx // 5  # 0, 1, 2
                row = idx % 5   # 0-4
                
                x = home_pos[0] + col * (FICHA_RADIUS * 2 + 4)
                y = home_pos[1] + row * (FICHA_RADIUS * 2 + 3)
                
                sprite = CheckerSprite(color, (x, y), None)
                self.checker_sprites.append(sprite)
    
    def _update_info_panel(self):
        """Actualiza el panel de información."""
        if not self.game_started:
            self.info_panel.update_info({'': 'Presiona Nueva Partida'})
            return
        
        jugador = self.game.get_jugador_actual()
        estado = self.game.get_estado_juego()
        
        info = {
            'jugador': f"{jugador.get_nombre()}\n({jugador.get_color()})",
            'Dados': str(estado['ultimo_roll']) if estado['ultimo_roll'] else 'Sin tirar',
            'Movimientos': str(estado['movimientos_disponibles']),
            'Barra B/N': f"{estado['bar_white']} / {estado['bar_black']}",
            'Casa B/N': f"{estado['home_white']} / {estado['home_black']}"
        }
        
        if estado['terminado']:
            info['Estado'] = f"¡¡GANÓ {estado['ganador']}!!"
        
        self.info_panel.update_info(info)
    
    def handle_events(self):
        """Maneja los eventos de Pygame."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            # Eventos de pantalla de inicio
            if self.show_start_screen:
                # Procesar inputs de texto
                if self.input_player1.handle_event(event):
                    # Enter presionado en player1, pasar al siguiente
                    self.input_player1.active = False
                    self.input_player2.active = True
                elif self.input_player2.handle_event(event):
                    # Enter presionado en player2, iniciar juego
                    self._on_start_game()
                else:
                    # Procesar botón solo si no se procesaron los inputs
                    self.btn_start.handle_event(event)
            
            # Eventos de juego
            else:
                # Eventos de botones
                for button in self.buttons:
                    button.handle_event(event)
                
                # Eventos de arrastre de fichas
                if self.game_started and not self.game.esta_terminado():
                    self._handle_checker_events(event)
    
    def _handle_checker_events(self, event):
        """Maneja eventos de arrastre de fichas."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            # Buscar ficha clickeada (de arriba hacia abajo)
            for sprite in reversed(self.checker_sprites):
                if sprite.contains_point(mouse_pos):
                    # Verificar que sea del jugador actual
                    jugador = self.game.get_jugador_actual()
                    if sprite.color == jugador.get_color():
                        self.selected_checker = sprite
                        sprite.start_drag(mouse_pos)
                        break
        
        elif event.type == pygame.MOUSEMOTION:
            if self.selected_checker:
                self.selected_checker.update_drag(event.pos)
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.selected_checker:
                # Intentar hacer movimiento
                if not self._try_move_checker(self.selected_checker, event.pos):
                    self.selected_checker.return_to_original()
                
                self.selected_checker.end_drag()
                self.selected_checker = None
    
    def _try_move_checker(self, sprite, drop_pos):
        """
        Intenta mover una ficha a una nueva posición.
        
        Returns:
            bool: True si el movimiento fue exitoso
        """
        # Determinar punto de destino
        punto_destino = self._get_punto_at_position(drop_pos)
        
        if punto_destino is None:
            return False
        
        # Determinar punto de origen
        punto_origen = sprite.punto_num + 1 if sprite.punto_num is not None else 0
        
        # Intentar movimiento en el game
        if self.game.hacer_movimiento(punto_origen, punto_destino):
            # Movimiento exitoso - recrear sprites
            self._create_checker_sprites()
            return True
        
        return False
    
    def _get_punto_at_position(self, pos):
        """
        Determina qué punto del tablero está en una posición.
        
        Returns:
            int or None: Número del punto (1-25) o None
        """
        # Revisar cada punto con tolerancia
        for punto_num in range(24):
            punto_pos = self.board_renderer.get_punto_position(punto_num)
            dx = abs(pos[0] - punto_pos[0])
            dy = abs(pos[1] - punto_pos[1])
            
            # Tolerancia más amplia
            if dx < PUNTO_WIDTH // 2 + 10 and dy < PUNTO_HEIGHT + 20:
                return punto_num + 1
        
        # Revisar home (posición 25)
        board_width = 12 * PUNTO_WIDTH + BARRA_WIDTH
        home_x = BOARD_MARGIN + board_width + 20
        
        # Área HOME más amplia que incluye ambas zonas
        if (home_x < pos[0] < home_x + 100):
            # Verificar si está en el área completa del HOME (arriba o abajo)
            if BOARD_MARGIN < pos[1] < BOARD_MARGIN + 2 * PUNTO_HEIGHT:
                return 25
        
        return None
    
    def update(self):
        """Actualiza el estado del juego."""
        if self.show_start_screen:
            self.input_player1.update()
            self.input_player2.update()
        else:
            self._update_info_panel()
    
    def draw(self):
        """Dibuja todo en la pantalla."""
        if self.show_start_screen:
            self._draw_start_screen()
        else:
            self._draw_game_screen()
        
        pygame.display.flip()
    
    def _draw_start_screen(self):
        """Dibuja la pantalla de inicio."""
        self.screen.fill(COLOR_BG)
        
        # Título
        font_title = pygame.font.Font(None, 80)
        title = font_title.render("BACKGAMMON", True, (255, 215, 0))
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 150))
        self.screen.blit(title, title_rect)
        
        # Subtítulo
        font_subtitle = pygame.font.Font(None, 40)
        subtitle = font_subtitle.render("Ingresa los nombres de los jugadores", True, COLOR_TEXTO)
        subtitle_rect = subtitle.get_rect(center=(WINDOW_WIDTH // 2, 250))
        self.screen.blit(subtitle, subtitle_rect)
        
        # Etiquetas
        font_label = pygame.font.Font(None, 30)
        label1 = font_label.render("Jugador 1 (Fichas Blancas ⚪):", True, COLOR_TEXTO)
        label1_rect = label1.get_rect(midleft=(WINDOW_WIDTH // 2 - 200, 350))
        self.screen.blit(label1, label1_rect)
        
        label2 = font_label.render("Jugador 2 (Fichas Negras ⚫):", True, COLOR_TEXTO)
        label2_rect = label2.get_rect(midleft=(WINDOW_WIDTH // 2 - 200, 450))
        self.screen.blit(label2, label2_rect)
        
        # Campos de texto
        self.input_player1.draw(self.screen)
        self.input_player2.draw(self.screen)
        
        # Botón
        self.btn_start.draw(self.screen)
        
        # Instrucciones
        font_hint = pygame.font.Font(None, 24)
        hint = font_hint.render("Presiona ENTER o click en COMENZAR para iniciar", True, (200, 200, 200))
        hint_rect = hint.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 100))
        self.screen.blit(hint, hint_rect)
    
    def _draw_game_screen(self):
        """Dibuja la pantalla de juego."""
        # Tablero
        self.board_renderer.draw_board()
        
        # Fichas
        jugador_actual_color = self.game.get_jugador_actual().get_color() if self.game_started else None
        for sprite in self.checker_sprites:
            highlight = (sprite == self.selected_checker or 
                        (sprite.color == jugador_actual_color and sprite != self.selected_checker))
            sprite.draw(self.screen, highlight and not sprite.dragging)
        
        # UI Elements
        self.dice_display.draw(self.screen)
        self.info_panel.draw(self.screen)
        
        for button in self.buttons:
            button.draw(self.screen)
    
    def run(self):
        """Loop principal del juego."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()


def main():
    """Función principal para ejecutar el juego con Pygame."""
    game = BackgammonPygame()
    game.run()


if __name__ == "__main__":
    main()
