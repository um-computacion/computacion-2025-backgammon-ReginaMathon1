# Backgammon

Implementación del juego de Backgammon en Python con dos interfaces: CLI y Pygame.

## Características

- ✅ Lógica completa del juego de Backgammon
- ✅ Interfaz de línea de comandos (CLI)
- ✅ Interfaz gráfica con Pygame
- ✅ Tests unitarios completos
- ✅ Validación de reglas oficiales

## Instalación

```bash
pip install -r requirements.txt
```

## Cómo Jugar

### CLI (Terminal)
```bash
python -m cli.main
```

### Pygame (Gráfico)
```bash
python -m pygame_ui.main
```

## Controles Pygame

- **Click y Arrastra**: Selecciona y mueve fichas con el mouse
- **Botón "Tirar Dados"**: Tira los dados al inicio de tu turno
- **Botón "Nueva Partida"**: Reinicia el juego

## Reglas Implementadas

- Movimiento según valores de dados
- Dobles (4 movimientos del mismo valor)
- Captura de fichas (blots)
- Barra (fichas capturadas)
- Bear off (sacar fichas)
- Condiciones de victoria

## Tests

```bash
# Ejecutar todos los tests
python -m unittest discover

# Con coverage
coverage run -m unittest discover
coverage report
```

## Estructura del Proyecto

