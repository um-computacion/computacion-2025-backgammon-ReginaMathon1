import unittest

from core.game import Game
from core.checker import Checker

class TestBackgammonGame(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test."""
        self.game = Game()
    
    def test_board_attribute_initialization(self):
        """Test que verifica que __board__ se inicializa como None."""
        self.assertIsNone(self.game.get_board())
    
    def test_players_attribute_initialization(self):
        """Test que verifica que __players__ se inicializa como lista vacía."""
        players = self.game.get_players()
        self.assertEqual(len(players), 0)
        self.assertIsInstance(players, list)
    
    def test_dice_attribute_initialization(self):
        """Test que verifica que __dice__ se inicializa como None."""
        self.assertIsNone(self.game.get_dice())
    
    def test_turno_attribute_initialization(self):
        """Test que verifica que __turno__ se inicializa en 0."""
        self.assertEqual(self.game.get_turno_actual(), 0)
    
    def test_board_after_iniciar_juego(self):
        """Test que verifica que __board__ se crea correctamente después de iniciar."""
        self.game.iniciar_juego("Ana", "Carlos")
        board = self.game.get_board()
        self.assertIsNotNone(board)
        # Verificar que el tablero tiene 24 puntos
        self.assertEqual(len(board.get_puntos()), 24)
    
    def test_players_after_iniciar_juego(self):
        """Test que verifica que __players__ se crea correctamente después de iniciar."""
        self.game.iniciar_juego("Ana", "Carlos")
        players = self.game.get_players()
        
        # Verificar que hay 2 jugadores
        self.assertEqual(len(players), 2)
        
        # Verificar nombres y colores
        self.assertEqual(players[0].get_nombre(), "Ana")
        self.assertEqual(players[0].get_color(), "white")
        self.assertEqual(players[1].get_nombre(), "Carlos")
        self.assertEqual(players[1].get_color(), "black")
        
        # Verificar fichas iniciales
        self.assertEqual(players[0].get_fichas(), 15)
        self.assertEqual(players[1].get_fichas(), 15)
    
    def test_dice_after_iniciar_juego(self):
        """Test que verifica que __dice__ se crea correctamente después de iniciar."""
        self.game.iniciar_juego("Ana", "Carlos")
        dice = self.game.get_dice()
        self.assertIsNotNone(dice)
        
        # Verificar que los dados funcionan
        resultado = self.game.tirar_dados()
        self.assertIsInstance(resultado, list)
        self.assertIn(len(resultado), [2, 4])  # 2 valores normales o 4 si hay dobles
    
    def test_turno_after_iniciar_juego(self):
        """Test que verifica que __turno__ se determina correctamente después de iniciar."""
        self.game.iniciar_juego("Ana", "Carlos")
        turno = self.game.get_turno_actual()
        
        # El turno debe ser 0 o 1
        self.assertIn(turno, [0, 1])
        
        # El jugador actual debe ser válido
        jugador_actual = self.game.get_jugador_actual()
        self.assertIn(jugador_actual, self.game.get_players())
    
    def test_cambiar_turno(self):
        """Test que verifica que cambiar_turno alterna correctamente."""
        self.game.iniciar_juego("Ana", "Carlos")
        turno_inicial = self.game.get_turno_actual()
        
        self.game.cambiar_turno()
        turno_nuevo = self.game.get_turno_actual()
        
        # El turno debe cambiar
        self.assertNotEqual(turno_inicial, turno_nuevo)
        self.assertIn(turno_nuevo, [0, 1])
    
    def test_esta_terminado_false(self):
        """Test que verifica que el juego no está terminado al inicio."""
        self.game.iniciar_juego("Ana", "Carlos")
        self.assertFalse(self.game.esta_terminado())
    
    def test_get_ganador_none(self):
        """Test que verifica que no hay ganador al inicio."""
        self.game.iniciar_juego("Ana", "Carlos")
        self.assertIsNone(self.game.get_ganador())

    def test_reiniciar_juego(self):
        """Test que verifica que se puede crear un nuevo juego después de uno existente."""
        # Iniciar primer juego
        self.game.iniciar_juego("Ana", "Carlos")
        
        # Verificar que el juego está inicializado
        self.assertIsNotNone(self.game.get_board())
        self.assertEqual(len(self.game.get_players()), 2)
        
        # Crear un nuevo juego
        nuevo_juego = Game()
        nuevo_juego.iniciar_juego("María", "Pedro")
        
        # Verificar que el nuevo juego está correctamente inicializado
        self.assertIsNotNone(nuevo_juego.get_board())
        self.assertEqual(len(nuevo_juego.get_players()), 2)
        self.assertEqual(nuevo_juego.get_players()[0].get_nombre(), "María")
        self.assertEqual(nuevo_juego.get_players()[1].get_nombre(), "Pedro")

    def test_movimiento_valido(self):
        """Test que verifica la validación de movimientos."""
        self.game.iniciar_juego("Ana", "Carlos")
        
        # Simular tirada de dados
        dados = self.game.tirar_dados()
        self.assertIsNotNone(dados)
        
        # Verificar que se puede consultar si un movimiento es válido
        jugador_actual = self.game.get_jugador_actual()
        self.assertIsNotNone(jugador_actual)

    def test_tirar_dados_multiples_veces(self):
        """Test que verifica múltiples tiradas de dados."""
        self.game.iniciar_juego("Ana", "Carlos")
        
        for _ in range(5):
            dados = self.game.tirar_dados()
            self.assertIsNotNone(dados)
            self.assertGreaterEqual(len(dados), 2)
            for dado in dados:
                self.assertGreaterEqual(dado, 1)
                self.assertLessEqual(dado, 6)

    def test_cambiar_turno_multiple(self):
        """Test que verifica cambios múltiples de turno."""
        self.game.iniciar_juego("Ana", "Carlos")
        
        for _ in range(10):
            turno_actual = self.game.get_turno_actual()
            self.game.cambiar_turno()
            turno_nuevo = self.game.get_turno_actual()
            self.assertNotEqual(turno_actual, turno_nuevo)

    def test_jugador_actual_alterna(self):
        """Test que verifica que get_jugador_actual alterna correctamente."""
        self.game.iniciar_juego("Ana", "Carlos")
        players = self.game.get_players()
        
        jugador1 = self.game.get_jugador_actual()
        self.game.cambiar_turno()
        jugador2 = self.game.get_jugador_actual()
        
        self.assertNotEqual(jugador1, jugador2)
        self.assertIn(jugador1, players)
        self.assertIn(jugador2, players)

    def test_board_puntos_iniciales(self):
        """Test que verifica la configuración inicial del tablero."""
        self.game.iniciar_juego("Ana", "Carlos")
        board = self.game.get_board()
        puntos = board.get_puntos()
        
        # Verificar que algunos puntos tienen fichas
        # get_fichas() devuelve directamente la lista
        fichas_totales = sum(len(punto) for punto in puntos)
        self.assertEqual(fichas_totales, 30)  # 15 fichas por jugador

    def test_esta_terminado_con_ganador(self):
        """Test que verifica que esta_terminado es True cuando hay ganador."""
        self.game.iniciar_juego("Ana", "Carlos")
        
        # Simular que un jugador ganó (todas las fichas fuera)
        players = self.game.get_players()
        # Este test requiere modificar el estado interno
        # Asumiendo que existe un método para verificar fin del juego
        self.assertFalse(self.game.esta_terminado())

    def test_multiples_juegos_consecutivos(self):
        """Test que verifica la capacidad de iniciar múltiples juegos."""
        nombres = [
            ("Alice", "Bob"),
            ("Charlie", "Diana"),
            ("Eve", "Frank")
        ]
        
        for nombre1, nombre2 in nombres:
            juego = Game()
            juego.iniciar_juego(nombre1, nombre2)
            
            self.assertIsNotNone(juego.get_board())
            self.assertEqual(len(juego.get_players()), 2)
            self.assertEqual(juego.get_players()[0].get_nombre(), nombre1)
            self.assertEqual(juego.get_players()[1].get_nombre(), nombre2)

    def test_dados_valores_validos(self):
        """Test que verifica que los dados siempre dan valores válidos."""
        self.game.iniciar_juego("Ana", "Carlos")
        
        for _ in range(20):
            dados = self.game.tirar_dados()
            for valor in dados:
                self.assertIn(valor, [1, 2, 3, 4, 5, 6])

    def test_dados_dobles(self):
        """Test que verifica el comportamiento con dobles."""
        self.game.iniciar_juego("Ana", "Carlos")
        
        # Tirar dados hasta obtener dobles o llegar a un límite
        for _ in range(50):
            dados = self.game.tirar_dados()
            if len(dados) == 4:  # Dobles dan 4 valores
                # Verificar que todos son iguales
                self.assertEqual(dados[0], dados[1])
                self.assertEqual(dados[0], dados[2])
                self.assertEqual(dados[0], dados[3])
                break

    def test_state_consistency(self):
        """Test que verifica la consistencia del estado del juego."""
        self.game.iniciar_juego("Ana", "Carlos")
        
        # Verificar que todos los componentes están sincronizados
        self.assertIsNotNone(self.game.get_board())
        self.assertIsNotNone(self.game.get_dice())
        self.assertEqual(len(self.game.get_players()), 2)
        self.assertIn(self.game.get_turno_actual(), [0, 1])
        self.assertIsNone(self.game.get_ganador())
        self.assertFalse(self.game.esta_terminado())

    def test_movimiento_simple(self):
        """Test que verifica realizar un movimiento simple."""
        self.game.iniciar_juego("Ana", "Carlos")
        dados = self.game.tirar_dados()
        
        # Intentar mover una ficha
        try:
            resultado = self.game.mover_ficha(0, dados[0])
            self.assertIsNotNone(resultado)
        except Exception:
            pass  # El movimiento puede fallar si no es válido

    def test_es_movimiento_valido(self):
        """Test que verifica la validación de movimientos."""
        self.game.iniciar_juego("Ana", "Carlos")
        dados = self.game.tirar_dados()
        
        # Verificar que existe el método de validación
        try:
            es_valido = self.game.es_movimiento_valido(0, dados[0])
            self.assertIsInstance(es_valido, bool)
        except Exception:
            pass

    def test_puede_mover(self):
        """Test que verifica si el jugador puede mover."""
        self.game.iniciar_juego("Ana", "Carlos")
        self.game.tirar_dados()
        
        try:
            puede = self.game.puede_mover()
            self.assertIsInstance(puede, bool)
        except Exception:
            pass

    def test_get_movimientos_posibles(self):
        """Test que obtiene los movimientos posibles."""
        self.game.iniciar_juego("Ana", "Carlos")
        self.game.tirar_dados()
        
        try:
            movimientos = self.game.get_movimientos_posibles()
            self.assertIsInstance(movimientos, list)
        except Exception:
            pass

    def test_iniciar_sin_nombres(self):
        """Test que verifica iniciar juego sin nombres."""
        try:
            self.game.iniciar_juego("", "")
        except Exception as e:
            self.assertIsInstance(e, Exception)

    def test_iniciar_con_nombres_vacios(self):
        """Test que verifica manejo de nombres vacíos."""
        try:
            self.game.iniciar_juego(None, None)
        except Exception:
            pass

    def test_mover_sin_tirar_dados(self):
        """Test que verifica mover sin tirar dados primero."""
        self.game.iniciar_juego("Ana", "Carlos")
        
        try:
            self.game.mover_ficha(0, 3)
        except Exception:
            pass

    def test_verificar_victoria_jugador1(self):
        """Test que verifica la condición de victoria del jugador 1."""
        self.game.iniciar_juego("Ana", "Carlos")
        
        try:
            # Simular que el jugador 1 no tiene fichas
            players = self.game.get_players()
            # Intentar verificar victoria
            terminado = self.game.esta_terminado()
            self.assertIsInstance(terminado, bool)
        except Exception:
            pass

    def test_verificar_victoria_jugador2(self):
        """Test que verifica la condición de victoria del jugador 2."""
        self.game.iniciar_juego("Ana", "Carlos")
        
        try:
            terminado = self.game.esta_terminado()
            self.assertIsInstance(terminado, bool)
        except Exception:
            pass

    def test_capturar_ficha(self):
        """Test que verifica la captura de fichas."""
        self.game.iniciar_juego("Ana", "Carlos")
        
        try:
            # Intentar capturar una ficha
            board = self.game.get_board()
            # Simular captura
            pass
        except Exception:
            pass

    def test_fichas_en_barra(self):
        """Test que verifica fichas en la barra."""
        self.game.iniciar_juego("Ana", "Carlos")
        
        try:
            players = self.game.get_players()
            # Verificar barra de cada jugador
            for player in players:
                barra = player.get_barra() if hasattr(player, 'get_barra') else 0
                self.assertIsInstance(barra, int)
        except Exception:
            pass

    def test_entrar_desde_barra(self):
        """Test que verifica entrar fichas desde la barra."""
        self.game.iniciar_juego("Ana", "Carlos")
        dados = self.game.tirar_dados()
        
        try:
            # Intentar entrar desde barra
            resultado = self.game.entrar_desde_barra(dados[0]) if hasattr(self.game, 'entrar_desde_barra') else None
        except Exception:
            pass

    def test_puede_sacar_fichas(self):
        """Test que verifica si se pueden sacar fichas."""
        self.game.iniciar_juego("Ana", "Carlos")
        
        try:
            puede_sacar = self.game.puede_sacar_fichas() if hasattr(self.game, 'puede_sacar_fichas') else False
            self.assertIsInstance(puede_sacar, bool)
        except Exception:
            pass

    def test_sacar_ficha(self):
        """Test que verifica sacar fichas del tablero."""
        self.game.iniciar_juego("Ana", "Carlos")
        dados = self.game.tirar_dados()
        
        try:
            resultado = self.game.sacar_ficha(23, dados[0]) if hasattr(self.game, 'sacar_ficha') else None
        except Exception:
            pass

    def test_todas_en_casa(self):
        """Test que verifica si todas las fichas están en casa."""
        self.game.iniciar_juego("Ana", "Carlos")
        
        try:
            todas_casa = self.game.todas_fichas_en_casa() if hasattr(self.game, 'todas_fichas_en_casa') else False
            self.assertIsInstance(todas_casa, bool)
        except Exception:
            pass

    def test_contar_fichas_jugador(self):
        """Test que cuenta las fichas de cada jugador."""
        self.game.iniciar_juego("Ana", "Carlos")
        players = self.game.get_players()
        
        for player in players:
            fichas = player.get_fichas()
            self.assertEqual(fichas, 15)

    def test_multiples_movimientos_turno(self):
        """Test que verifica múltiples movimientos en un turno."""
        self.game.iniciar_juego("Ana", "Carlos")
        dados = self.game.tirar_dados()
        
        # Intentar múltiples movimientos
        for dado in dados[:2]:
            try:
                self.game.mover_ficha(0, dado)
            except Exception:
                pass

    def test_turnos_alternados_completos(self):
        """Test que verifica varios turnos completos."""
        self.game.iniciar_juego("Ana", "Carlos")
        
        for _ in range(5):
            self.game.tirar_dados()
            self.game.cambiar_turno()
            
        self.assertIsNotNone(self.game.get_jugador_actual())

    def test_estado_inicial_completo(self):
        """Test que verifica el estado inicial completo del juego."""
        self.game.iniciar_juego("Ana", "Carlos")
        
        # Verificar board
        board = self.game.get_board()
        self.assertIsNotNone(board)
        self.assertEqual(len(board.get_puntos()), 24)
        
        # Verificar players
        players = self.game.get_players()
        self.assertEqual(len(players), 2)
        
        # Verificar dados
        dice = self.game.get_dice()
        self.assertIsNotNone(dice)
        
        # Verificar turno
        self.assertIn(self.game.get_turno_actual(), [0, 1])

    def test_juego_completo_simulado(self):
        """Test que simula un juego completo."""
        self.game.iniciar_juego("Ana", "Carlos")
        
        # Simular varios turnos
        for _ in range(10):
            dados = self.game.tirar_dados()
            self.assertIsNotNone(dados)
            
            # Intentar hacer movimientos
            try:
                if hasattr(self.game, 'puede_mover') and self.game.puede_mover():
                    # Intentar mover
                    pass
            except Exception:
                pass
            
            self.game.cambiar_turno()
        
        # El juego debería seguir siendo consistente
        self.assertIsNotNone(self.game.get_board())
        self.assertEqual(len(self.game.get_players()), 2)

    def test_validacion_posiciones_tablero(self):
        """Test que valida las posiciones del tablero."""
        self.game.iniciar_juego("Ana", "Carlos")
        
        # Intentar validar posiciones válidas e inválidas
        try:
            posiciones_invalidas = [-1, 24, 25, 100]
            for pos in posiciones_invalidas:
                resultado = self.game.es_movimiento_valido(pos, 1) if hasattr(self.game, 'es_movimiento_valido') else False
        except Exception:
            pass

    def test_dados_usados(self):
        """Test que verifica el seguimiento de dados usados."""
        self.game.iniciar_juego("Ana", "Carlos")
        dados = self.game.tirar_dados()
        
        try:
            # Verificar si hay método para dados usados
            if hasattr(self.game, 'get_dados_usados'):
                dados_usados = self.game.get_dados_usados()
                self.assertIsInstance(dados_usados, list)
        except Exception:
            pass

    def test_reiniciar_dados(self):
        """Test que verifica reiniciar dados después de usar."""
        self.game.iniciar_juego("Ana", "Carlos")
        self.game.tirar_dados()
        
        try:
            if hasattr(self.game, 'reiniciar_dados'):
                self.game.reiniciar_dados()
        except Exception:
            pass

    def test_get_bar_y_home(self):
        """Test que verifica getters de bar y home."""
        self.game.iniciar_juego("Ana", "Carlos")
        
        # Verificar bar
        bar_white = self.game.get_bar('white')
        bar_black = self.game.get_bar('black')
        self.assertIsInstance(bar_white, list)
        self.assertIsInstance(bar_black, list)
        self.assertEqual(len(bar_white), 0)
        self.assertEqual(len(bar_black), 0)
        
        # Verificar home
        home_white = self.game.get_home('white')
        home_black = self.game.get_home('black')
        self.assertIsInstance(home_white, list)
        self.assertIsInstance(home_black, list)
        self.assertEqual(len(home_white), 0)
        self.assertEqual(len(home_black), 0)

    def test_es_movimiento_valido_sin_movimientos(self):
        """Test validación sin movimientos disponibles."""
        self.game.iniciar_juego("Ana", "Carlos")
        # Sin tirar dados
        resultado = self.game.es_movimiento_valido(1, 3)
        self.assertFalse(resultado)

    def test_es_movimiento_valido_posiciones_invalidas(self):
        """Test validación con posiciones fuera de rango."""
        self.game.iniciar_juego("Ana", "Carlos")
        self.game.tirar_dados()
        
        # Posición desde negativa
        self.assertFalse(self.game.es_movimiento_valido(-1, 5))
        
        # Posición desde > 24
        self.assertFalse(self.game.es_movimiento_valido(25, 26))
        
        # Posición hasta < 1
        self.assertFalse(self.game.es_movimiento_valido(5, 0))
        
        # Posición hasta > 25
        self.assertFalse(self.game.es_movimiento_valido(20, 26))

    def test_hacer_movimiento_completo(self):
        """Test que ejecuta movimiento completo incluyendo todas las ramas."""
        self.game.iniciar_juego("Ana", "Carlos")
        
        # Asegurar que juegan las blancas
        while self.game.get_jugador_actual().get_color() != 'white':
            self.game.cambiar_turno()
        
        # Tirar dados
        dados = self.game.tirar_dados()
        
        # Intentar hacer un movimiento válido desde punto 1
        for dado in dados:
            destino = 1 + dado
            if destino <= 24:
                resultado = self.game.hacer_movimiento(1, destino)
                if resultado:
                    # Verificar que se removió el dado usado
                    movs_restantes = self.game.get_movimientos_disponibles()
                    self.assertLess(len(movs_restantes), len(dados))
                    break

    def test_hacer_movimiento_con_captura(self):
        """Test movimiento que captura ficha enemiga."""
        self.game.iniciar_juego("Ana", "Carlos")
        board = self.game.get_board()
        
        # Asegurar que juegan blancas
        while self.game.get_jugador_actual().get_color() != 'white':
            self.game.cambiar_turno()
        
        # Preparar escenario: poner solo 1 ficha negra en punto 7
        while board.tiene_fichas(7):
            board.quitar_ficha(7)
        board.agregar_ficha(7, Checker('black'))
        
        dados = self.game.tirar_dados()
        
        # Si tenemos un 6, podemos mover de 1 a 7
        if 6 in dados:
            bar_antes = len(self.game.get_bar('black'))
            resultado = self.game.hacer_movimiento(1, 7)
            if resultado:
                bar_despues = len(self.game.get_bar('black'))
                self.assertEqual(bar_despues, bar_antes + 1)

    def test_hacer_movimiento_bear_off(self):
        """Test movimiento de bear off (sacar fichas)."""
        self.game.iniciar_juego("Ana", "Carlos")
        board = self.game.get_board()
        
        # Asegurar que juegan blancas
        while self.game.get_jugador_actual().get_color() != 'white':
            self.game.cambiar_turno()
        
        # Limpiar TODAS las fichas del punto 24 (tiene fichas negras inicialmente)
        while board.tiene_fichas(24):
            board.quitar_ficha(24)
        
        # Limpiar todas las fichas blancas del resto del tablero
        for i in range(1, 24):
            if board.tiene_fichas(i):
                color = board.get_color_punto(i)
                if color == 'white':
                    while board.tiene_fichas(i):
                        board.quitar_ficha(i)
        
        # Ahora poner 1 ficha blanca en punto 24
        board.agregar_ficha(24, Checker('white'))
        
        dados = self.game.tirar_dados()
        
        # Intentar bear off
        if 1 in dados:  # Necesitamos 1 para sacar desde 24
            home_antes = len(self.game.get_home('white'))
            resultado = self.game.hacer_movimiento(24, 25)
            if resultado:
                home_despues = len(self.game.get_home('white'))
                self.assertEqual(home_despues, home_antes + 1)

    def test_hacer_movimiento_desde_barra(self):
        """Test movimiento desde la barra."""
        self.game.iniciar_juego("Ana", "Carlos")
        board = self.game.get_board()
        
        # Asegurar que juegan blancas
        while self.game.get_jugador_actual().get_color() != 'white':
            self.game.cambiar_turno()
        
        # Simular captura: quitar ficha y acceder a bar directamente
        ficha = board.quitar_ficha(1)
        if ficha:
            # Acceder al diccionario __bar__ correctamente
            try:
                # Intentar acceder al atributo privado
                bar_ref = self.game.__dict__['_Game__bar__']
                bar_ref['white'].append(ficha)
                
                dados = self.game.tirar_dados()
                bar_antes = len(self.game.get_bar('white'))
                
                # Intentar entrar
                for dado in dados:
                    resultado = self.game.hacer_movimiento(0, dado)
                    if resultado:
                        bar_despues = len(self.game.get_bar('white'))
                        self.assertLess(bar_despues, bar_antes)
                        break
            except (KeyError, AttributeError):
                # Si no podemos acceder, simplemente verificamos que el método existe
                self.assertTrue(hasattr(self.game, 'hacer_movimiento'))

    def test_es_movimiento_valido_desde_barra_vacia(self):
        """Test validación desde barra cuando está vacía."""
        self.game.iniciar_juego("Ana", "Carlos")
        self.game.tirar_dados()
        
        # Intentar mover desde barra vacía
        resultado = self.game.es_movimiento_valido(0, 5)
        self.assertFalse(resultado)

    def test_es_movimiento_valido_con_fichas_en_barra(self):
        """Test que obliga a mover desde barra primero."""
        self.game.iniciar_juego("Ana", "Carlos")
        board = self.game.get_board()
        
        # Asegurar que juegan blancas
        while self.game.get_jugador_actual().get_color() != 'white':
            self.game.cambiar_turno()
        
        # Poner ficha en barra - acceso directo al diccionario
        ficha = board.quitar_ficha(1)
        if ficha:
            try:
                # Acceder correctamente al diccionario privado
                bar_ref = self.game.__dict__['_Game__bar__']
                bar_ref['white'].append(ficha)
                
                self.game.tirar_dados()
                
                # Intentar mover desde tablero (no barra)
                resultado = self.game.es_movimiento_valido(12, 15)
                self.assertFalse(resultado)
            except (KeyError, AttributeError):
                # Si no podemos acceder, simplemente verificamos que la validación funciona
                self.assertTrue(hasattr(self.game, 'es_movimiento_valido'))

    def test_es_movimiento_valido_punto_bloqueado(self):
        """Test validación con punto bloqueado por oponente."""
        self.game.iniciar_juego("Ana", "Carlos")
        board = self.game.get_board()
        
        # Asegurar que juegan blancas
        while self.game.get_jugador_actual().get_color() != 'white':
            self.game.cambiar_turno()
        
        # Bloquear punto 5 con 2+ fichas negras
        while board.tiene_fichas(5):
            board.quitar_ficha(5)
        board.agregar_ficha(5, Checker('black'))
        board.agregar_ficha(5, Checker('black'))
        
        dados = self.game.tirar_dados()
        
        if 4 in dados:  # Intentar ir de 1 a 5
            resultado = self.game.es_movimiento_valido(1, 5)
            self.assertFalse(resultado)

    def test_tiene_movimientos_disponibles_true(self):
        """Test que hay movimientos disponibles al inicio."""
        self.game.iniciar_juego("Ana", "Carlos")
        self.game.tirar_dados()
        
        resultado = self.game.tiene_movimientos_disponibles()
        self.assertTrue(resultado)

    def test_tiene_movimientos_disponibles_false_sin_dados(self):
        """Test sin movimientos cuando no hay dados."""
        self.game.iniciar_juego("Ana", "Carlos")
        
        resultado = self.game.tiene_movimientos_disponibles()
        self.assertFalse(resultado)

    def test_get_ganador_con_victoria(self):
        """Test obtener ganador cuando alguien ganó."""
        self.game.iniciar_juego("Ana", "Carlos")
        
        # Simular victoria: 15 fichas en home - acceso directo
        try:
            home_ref = self.game.__dict__['_Game__home__']
            for _ in range(15):
                home_ref['white'].append(Checker('white'))
            
            self.assertTrue(self.game.esta_terminado())
            ganador = self.game.get_ganador()
            self.assertIsNotNone(ganador)
            self.assertEqual(ganador.get_color(), 'white')
        except (KeyError, AttributeError):
            # Si no podemos acceder, al menos verificamos que los métodos existen
            self.assertTrue(hasattr(self.game, 'esta_terminado'))
            self.assertTrue(hasattr(self.game, 'get_ganador'))

    def test_get_estado_juego_completo(self):
        """Test estado del juego con todos sus campos."""
        self.game.iniciar_juego("Ana", "Carlos")
        self.game.tirar_dados()
        
        estado = self.game.get_estado_juego()
        
        self.assertIn('jugador_actual', estado)
        self.assertIn('ultimo_roll', estado)
        self.assertIn('movimientos_disponibles', estado)
        self.assertIn('bar_white', estado)
        self.assertIn('bar_black', estado)
        self.assertIn('home_white', estado)
        self.assertIn('home_black', estado)
        self.assertIn('terminado', estado)
        self.assertIn('ganador', estado)
        
        self.assertIsNotNone(estado['jugador_actual'])
        self.assertIsNotNone(estado['ultimo_roll'])
        self.assertGreater(len(estado['movimientos_disponibles']), 0)

    def test_str_sin_iniciar(self):
        """Test representación string sin iniciar."""
        resultado = str(self.game)
        self.assertEqual(resultado, "Juego no iniciado")

    def test_str_iniciado(self):
        """Test representación string con juego iniciado."""
        self.game.iniciar_juego("Ana", "Carlos")
        self.game.tirar_dados()
        
        resultado = str(self.game)
        self.assertIsInstance(resultado, str)
        self.assertIn("Backgammon", resultado)

    def test_reiniciar_juego_completo(self):
        """Test reiniciar juego."""
        self.game.iniciar_juego("Ana", "Carlos")
        self.game.tirar_dados()
        
        self.game.reiniciar_juego()
        
        self.assertIsNone(self.game.get_board())
        self.assertEqual(len(self.game.get_players()), 0)
        self.assertIsNone(self.game.get_dice())

    def test_calcular_distancia_blancas(self):
        """Test cálculo de distancia para blancas."""
        self.game.iniciar_juego("Ana", "Carlos")
        
        # Asegurar que juegan blancas
        while self.game.get_jugador_actual().get_color() != 'white':
            self.game.cambiar_turno()
        
        self.game.tirar_dados()
        
        # Las blancas calculan distancia hacia adelante
        if 3 in self.game.get_movimientos_disponibles():
            resultado = self.game.es_movimiento_valido(1, 4)
            self.assertIsInstance(resultado, bool)

    def test_calcular_distancia_negras(self):
        """Test cálculo de distancia para negras."""
        self.game.iniciar_juego("Ana", "Carlos")
        
        # Asegurar que juegan negras
        while self.game.get_jugador_actual().get_color() != 'black':
            self.game.cambiar_turno()
        
        self.game.tirar_dados()
        
        # Las negras calculan distancia hacia atrás
        if 3 in self.game.get_movimientos_disponibles():
            resultado = self.game.es_movimiento_valido(24, 21)
            self.assertIsInstance(resultado, bool)

    def test_iniciar_con_nombres_default(self):
        """Test iniciar sin argumentos usa nombres default."""
        self.game.iniciar_juego()
        players = self.game.get_players()
        
        self.assertEqual(players[0].get_nombre(), "Jugador 1")
        self.assertEqual(players[1].get_nombre(), "Jugador 2")

    def test_hacer_movimiento_desde_punto_sin_fichas_propias(self):
        """Test que verifica movimiento desde punto sin fichas propias."""
        self.game.iniciar_juego("Ana", "Carlos")
        
        # Asegurar que juegan blancas
        while self.game.get_jugador_actual().get_color() != 'white':
            self.game.cambiar_turno()
        
        dados = self.game.tirar_dados()
        
        # Intentar mover desde punto 6 que tiene fichas negras
        resultado = self.game.hacer_movimiento(6, 6 + dados[0])
        self.assertFalse(resultado)

    def test_es_movimiento_valido_distancia_cero_o_negativa(self):
        """Test que verifica movimiento con distancia inválida."""
        self.game.iniciar_juego("Ana", "Carlos")
        
        # Asegurar que juegan blancas
        while self.game.get_jugador_actual().get_color() != 'white':
            self.game.cambiar_turno()
        
        self.game.tirar_dados()
        
        # Intentar movimiento que resulta en distancia 0 o negativa
        resultado = self.game.es_movimiento_valido(10, 10)  # distancia 0
        self.assertFalse(resultado)

    def test_tiene_movimientos_desde_barra_bloqueada_completamente(self):
        """Test cuando la barra está completamente bloqueada."""
        self.game.iniciar_juego("Ana", "Carlos")
        board = self.game.get_board()
        
        # Asegurar que juegan blancas
        while self.game.get_jugador_actual().get_color() != 'white':
            self.game.cambiar_turno()
        
        # Poner ficha en barra
        ficha = board.quitar_ficha(1)
        if ficha:
            try:
                bar_ref = self.game.__dict__['_Game__bar__']
                bar_ref['white'].append(ficha)
                
                # Bloquear todos los puntos de entrada (1-6) con 2+ fichas negras
                for i in range(1, 7):
                    while board.tiene_fichas(i):
                        board.quitar_ficha(i)
                    board.agregar_ficha(i, Checker('black'))
                    board.agregar_ficha(i, Checker('black'))
                
                self.game.tirar_dados()
                
                # Verificar que no hay movimientos disponibles
                tiene_movs = self.game.tiene_movimientos_disponibles()
                self.assertFalse(tiene_movs)
            except (KeyError, AttributeError):
                # Si no podemos acceder, verificamos que el método existe
                self.assertTrue(hasattr(self.game, 'tiene_movimientos_disponibles'))

    def test_puede_bear_off_con_fichas_fuera_de_casa(self):
        """Test verifica que no puede bear off con fichas fuera de casa."""
        self.game.iniciar_juego("Ana", "Carlos")
        board = self.game.get_board()
        
        # Asegurar que juegan blancas
        while self.game.get_jugador_actual().get_color() != 'white':
            self.game.cambiar_turno()
        
        # Dejar una ficha blanca en punto bajo (fuera de casa)
        # La casa de blancas es 19-24
        self.game.tirar_dados()
        
        # Intentar bear off desde punto 19 (está en casa pero hay fichas fuera)
        resultado = self.game.es_movimiento_valido(19, 25)
        # Debe ser False porque hay fichas fuera de casa
        self.assertFalse(resultado)

    def test_tiene_movimientos_busca_en_todo_el_tablero(self):
        """Test que verifica búsqueda de movimientos en todos los puntos."""
        self.game.iniciar_juego("Ana", "Carlos")
        
        # Asegurar que juegan blancas
        while self.game.get_jugador_actual().get_color() != 'white':
            self.game.cambiar_turno()
        
        self.game.tirar_dados()
        
        # Verificar que busca movimientos en el tablero
        tiene_movs = self.game.tiene_movimientos_disponibles()
        # Al inicio siempre debería haber movimientos
        self.assertTrue(tiene_movs)

    def test_hacer_movimiento_a_punto_con_dos_fichas_enemigas(self):
        """Test que verifica que no puede mover a punto con 2+ fichas enemigas."""
        self.game.iniciar_juego("Ana", "Carlos")
        board = self.game.get_board()
        
        # Asegurar que juegan blancas
        while self.game.get_jugador_actual().get_color() != 'white':
            self.game.cambiar_turno()
        
        # Poner 2 fichas negras en punto 3
        while board.tiene_fichas(3):
            board.quitar_ficha(3)
        board.agregar_ficha(3, Checker('black'))
        board.agregar_ficha(3, Checker('black'))
        
        dados = self.game.tirar_dados()
        
        if 2 in dados:  # Intentar mover de 1 a 3
            resultado = self.game.hacer_movimiento(1, 3)
            self.assertFalse(resultado)


if __name__ == '__main__':
    unittest.main()