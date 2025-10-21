from core.game import Game

class BackgammonCLI:
    """
    Interfaz de línea de comandos para el juego de Backgammon.
    Responsabilidad única: Manejar la interacción con el usuario.
    """
    
    def __init__(self):
        """Inicializa la interfaz CLI."""
        self.__game__ = Game()
        self.__jugando__ = False
    
    def iniciar(self):
        """Punto de entrada principal de la CLI."""
        self.__mostrar_bienvenida__()
        
        while True:
            opcion = self.__menu_principal__()
            
            if opcion == "1":
                self.__nueva_partida__()
            elif opcion == "2":
                self.__mostrar_reglas__()
            elif opcion == "3":
                print("\n¡Gracias por jugar Backgammon! ¡Hasta pronto!")
                break
            else:
                print("\n❌ Opción inválida. Por favor, elige 1, 2 o 3.")
    
    def __mostrar_bienvenida__(self):
        """Muestra el mensaje de bienvenida."""
        print("\n" + "="*60)
        print("🎲  BIENVENIDO A BACKGAMMON  🎲".center(60))
        print("="*60)
    
    def __menu_principal__(self):
        """Muestra el menú principal y retorna la opción elegida."""
        print("\n📋 MENÚ PRINCIPAL")
        print("1. Nueva Partida")
        print("2. Ver Reglas")
        print("3. Salir")
        return input("\nElige una opción: ").strip()
    
    def __nueva_partida__(self):
        """Configura e inicia una nueva partida."""
        print("\n" + "="*60)
        print("NUEVA PARTIDA".center(60))
        print("="*60)
        
        nombre1 = input("\n👤 Nombre del Jugador 1 (fichas blancas): ").strip() or "Jugador 1"
        nombre2 = input("👤 Nombre del Jugador 2 (fichas negras): ").strip() or "Jugador 2"
        
        self.__game__.iniciar_juego(nombre1, nombre2)
        self.__jugando__ = True
        
        print(f"\n✅ Partida iniciada: {nombre1} (blancas) vs {nombre2} (negras)")
        print("\nℹ️  Las blancas mueven de 1→24, las negras de 24→1")
        
        self.__ciclo_de_juego__()
    
    def __ciclo_de_juego__(self):
        """Ciclo principal del juego."""
        while self.__jugando__ and not self.__game__.esta_terminado():
            jugador = self.__game__.get_jugador_actual()
            
            print("\n" + "-"*60)
            print(f"🎯 TURNO DE: {jugador.get_nombre()} ({jugador.get_color()})".center(60))
            print("-"*60)
            
            self.__mostrar_tablero__()
            
            # Tirar dados
            if not self.__tirar_dados__():
                continue
            
            # Realizar movimientos
            self.__realizar_movimientos__()
        
        if self.__game__.esta_terminado():
            self.__mostrar_resultado_final__()
    
    def __tirar_dados__(self):
        """Maneja la tirada de dados."""
        input("\n🎲 Presiona ENTER para tirar los dados...")
        
        dados = self.__game__.tirar_dados()
        print(f"\n🎲 Dados: {dados}")
        
        if not self.__game__.tiene_movimientos_disponibles():
            print("❌ No hay movimientos válidos disponibles. Turno perdido.")
            self.__game__.cambiar_turno()
            return False
        
        return True
    
    def __realizar_movimientos__(self):
        """Permite al jugador realizar sus movimientos."""
        while self.__game__.get_movimientos_disponibles():
            print(f"\n📊 Movimientos disponibles: {self.__game__.get_movimientos_disponibles()}")
            
            if not self.__game__.tiene_movimientos_disponibles():
                print("\n⚠️  No hay más movimientos válidos disponibles.")
                break
            
            opcion = input("\n💡 Escribe 'ayuda' para ver instrucciones o presiona ENTER para mover: ").strip().lower()
            
            if opcion == 'ayuda':
                self.__mostrar_ayuda_movimiento__()
                continue
            
            if not self.__solicitar_movimiento__():
                continuar = input("\n¿Intentar otro movimiento? (s/n): ").strip().lower()
                if continuar == 'n':
                    break
        
        print("\n✅ Turno completado.")
        self.__game__.cambiar_turno()
    
    def __solicitar_movimiento__(self):
        """Solicita y ejecuta un movimiento del jugador."""
        jugador = self.__game__.get_jugador_actual()
        color = jugador.get_color()
        
        # Verificar si hay fichas en la barra
        bar = self.__game__.get_bar(color)
        if bar:
            print(f"\n⚠️  Tienes {len(bar)} ficha(s) en la barra. Debes entrarlas primero.")
            desde = 0
        else:
            try:
                desde_input = input("\n📍 Desde qué punto (1-24, 0=barra): ").strip()
                desde = int(desde_input)
                
                if desde < 0 or desde > 24:
                    print("❌ Posición inválida. Debe estar entre 0 y 24.")
                    return False
            except ValueError:
                print("❌ Entrada inválida. Ingresa un número.")
                return False
        
        try:
            hasta_input = input("📍 Hacia qué punto (1-24, 25=sacar): ").strip()
            hasta = int(hasta_input)
            
            if hasta < 1 or hasta > 25:
                print("❌ Posición inválida. Debe estar entre 1 y 25.")
                return False
        except ValueError:
            print("❌ Entrada inválida. Ingresa un número.")
            return False
        
        if self.__game__.hacer_movimiento(desde, hasta):
            print("✅ Movimiento realizado exitosamente.")
            return True
        else:
            print("❌ Movimiento inválido. Intenta con otro.")
            return False
    
    def __mostrar_tablero__(self):
        """Muestra el estado actual del tablero."""
        print("\n" + "="*60)
        print("TABLERO DE BACKGAMMON".center(60))
        print("="*60)
        
        # Mostrar bar (fichas capturadas)
        bar_white = len(self.__game__.get_bar('white'))
        bar_black = len(self.__game__.get_bar('black'))
        print(f"\n🔸 Barra Blancas: {bar_white} | Barra Negras: {bar_black} 🔸")
        
        # Mostrar puntos del tablero
        board = self.__game__.get_board()
        
        # Mostrar mitad superior (puntos 13-24)
        print("\n┌" + "─"*58 + "┐")
        print("│ Puntos 13-24 (Negro → Blanco)".ljust(59) + "│")
        
        for i in range(12, 24):
            punto = board.get_punto(i + 1)
            if punto:
                color_symbol = "⚪" if punto[0].get_color() == 'white' else "⚫"
                cantidad = len(punto)
                print(f"│ Punto {i+1:2d}: {color_symbol} x{cantidad}".ljust(59) + "│")
        
        print("├" + "─"*58 + "┤")
        
        # Mostrar mitad inferior (puntos 1-12)
        print("│ Puntos 1-12 (Blanco → Negro)".ljust(59) + "│")
        
        for i in range(0, 12):
            punto = board.get_punto(i + 1)
            if punto:
                color_symbol = "⚪" if punto[0].get_color() == 'white' else "⚫"
                cantidad = len(punto)
                print(f"│ Punto {i+1:2d}: {color_symbol} x{cantidad}".ljust(59) + "│")
        
        print("└" + "─"*58 + "┘")
        
        # Mostrar home (fichas sacadas)
        home_white = len(self.__game__.get_home('white'))
        home_black = len(self.__game__.get_home('black'))
        print(f"\n🏠 Casa Blancas: {home_white}/15 | Casa Negras: {home_black}/15 🏠")
    
    def __mostrar_ayuda_movimiento__(self):
        """Muestra ayuda sobre cómo realizar movimientos."""
        print("\n" + "="*60)
        print("AYUDA DE MOVIMIENTO".center(60))
        print("="*60)
        print("""
        🎲 CÓMO MOVER:
        - Elige el punto de origen (1-24) o 0 si tienes fichas en barra
        - Elige el punto de destino (1-24) o 25 para sacar fichas
        
        📋 REGLAS:
        - Solo puedes mover tus propias fichas
        - El movimiento debe coincidir con los dados disponibles
        - No puedes mover a un punto con 2+ fichas del oponente
        - Si tienes fichas en la barra, debes entrarlas primero
        - Solo puedes sacar fichas (25) cuando todas estén en casa
        
        ⚪ Blancas: mueven de 1 → 24 (casa: 19-24)
        ⚫ Negras: mueven de 24 → 1 (casa: 1-6)
        """)
    
    def __mostrar_reglas__(self):
        """Muestra las reglas completas del Backgammon."""
        print("\n" + "="*60)
        print("REGLAS DEL BACKGAMMON".center(60))
        print("="*60)
        print("""
        🎯 OBJETIVO:
        Ser el primero en sacar todas tus 15 fichas del tablero.
        
        🎲 MOVIMIENTO:
        - Cada turno, tira dos dados
        - Mueve tus fichas según los valores de los dados
        - Si sacas dobles, puedes mover 4 veces ese número
        
        📍 DIRECCIÓN:
        - Blancas: mueven de 1 hacia 24
        - Negras: mueven de 24 hacia 1
        
        🔸 CAPTURA:
        - Si un punto tiene solo 1 ficha enemiga (blot), puedes capturarla
        - Las fichas capturadas van a la barra
        - Debes reentrar fichas capturadas antes de mover otras
        
        🏠 SACAR FICHAS:
        - Solo cuando todas tus fichas estén en tu casa (últimos 6 puntos)
        - Blancas: casa en puntos 19-24
        - Negras: casa en puntos 1-6
        
        ✅ VICTORIA:
        - Gana quien primero saca todas sus 15 fichas
        """)
        input("\nPresiona ENTER para volver al menú...")
    
    def __mostrar_resultado_final__(self):
        """Muestra el resultado final de la partida."""
        ganador = self.__game__.get_ganador()
        
        print("\n" + "="*60)
        print("🎉 ¡PARTIDA TERMINADA! 🎉".center(60))
        print("="*60)
        print(f"\n🏆 GANADOR: {ganador.get_nombre()} ({ganador.get_color()})")
        print("\n¡Felicitaciones por el excelente juego!")
        print("="*60)
        
        self.__jugando__ = False


def main():
    """Función principal para ejecutar el CLI."""
    try:
        cli = BackgammonCLI()
        cli.iniciar()
    except KeyboardInterrupt:
        print("\n\n⚠️  Juego interrumpido por el usuario.")
        print("¡Hasta pronto!")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        print("Por favor, reporta este error.")


if __name__ == "__main__":
    main()
