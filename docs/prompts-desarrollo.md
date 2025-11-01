# Prompts de Desarrollo - Backgammon

Este documento registra todas las consultas realizadas durante el desarrollo del proyecto y las soluciones implementadas.

---

## 1. Crear clase Board

**Pregunta**: Tengo que hacer el juego backgammon pero con varios commit. Ahora quiero hacer la clase board con posiciones iniciales. En board.py crear clase Board con atributo `__puntos__` (lista de 24 posiciones).

**Respuesta**:
```python
class Board:
    def __init__(self):
        self.__puntos__ = [None] * 24  # 24 posiciones (índices 0-23 para puntos 1-24)
        
        # Configuración inicial del backgammon
        # Jugador blanco (white)
        self.__puntos__[0] = ('white', 2)   # Punto 1: 2 fichas blancas
        self.__puntos__[11] = ('white', 5)  # Punto 12: 5 fichas blancas
        self.__puntos__[16] = ('white', 3)  # Punto 17: 3 fichas blancas
        self.__puntos__[18] = ('white', 5)  # Punto 19: 5 fichas blancas
        
        # Jugador negro (black)
        self.__puntos__[5] = ('black', 5)   # Punto 6: 5 fichas negras
        self.__puntos__[7] = ('black', 3)   # Punto 8: 3 fichas negras
        self.__puntos__[12] = ('black', 5)  # Punto 13: 5 fichas negras
        self.__puntos__[23] = ('black', 2)  # Punto 24: 2 fichas negras
    
    def get_puntos(self):
        return self.__puntos__
    
    def get_punto(self, posicion):
        if 1 <= posicion <= 24:
            return self.__puntos__[posicion - 1]
        else:
            raise ValueError("La posición debe estar entre 1 y 24")
```

---

## 2. Crear clase Dice

**Pregunta**: En dice.py crear clase Dice con atributos dado1 y dado2. Método tirar() que devuelva números aleatorios 1-6. Manejar dobles (si ambos dados iguales → se repite).

**Respuesta**:
```python
import random

class Dice:
    def __init__(self):
        self.__dado1__ = None
        self.__dado2__ = None
    
    def tirar(self):
        self.__dado1__ = random.randint(1, 6)
        self.__dado2__ = random.randint(1, 6)
        
        # Si ambos dados son iguales (dobles), se repite el valor 4 veces
        if self.__dado1__ == self.__dado2__:
            return [self.__dado1__, self.__dado1__, self.__dado1__, self.__dado1__]
        else:
            return [self.__dado1__, self.__dado2__]
    
    def get_dado1(self):
        return self.__dado1__
    
    def get_dado2(self):
        return self.__dado2__
```

---

## 3. Crear clase Player

**Pregunta**: En player.py crear clase Player con atributos nombre, fichas (15), color. Método reset_fichas() que reinicie fichas.

**Respuesta**:
```python
class Player:
    def __init__(self, nombre, color):
        self.__nombre__ = nombre
        self.__color__ = color
        self.__fichas__ = 15  # Cada jugador empieza con 15 fichas
    
    def get_nombre(self):
        return self.__nombre__
    
    def get_color(self):
        return self.__color__
    
    def get_fichas(self):
        return self.__fichas__
    
    def reset_fichas(self):
        self.__fichas__ = 15
    
    def set_fichas(self, cantidad):
        if cantidad >= 0:
            self.__fichas__ = cantidad
        else:
            raise ValueError("La cantidad de fichas no puede ser negativa")