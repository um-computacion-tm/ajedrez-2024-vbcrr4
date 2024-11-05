import argparse
from .chess import Game

def iniciar_juego():
    """
    Inicializa e inicia una partida de ajedrez, capturando y validando las entradas del usuario.
    """
    # Inicializamos la clase Game
    __game__ = Game()
    
    print("¡Bienvenido al juego de ajedrez! Escribe 'Q' en la posición inicial para salir.")
    __game__.show_board()

    while True:
        # Mostramos el turno actual
        print(f"Turno de las {__game__.get_turn()}")

        # Capturamos las posiciones de inicio y fin
        start_pos = input("Introduce la posición inicial (ej. A2, o Q para salir): ").strip().upper()
        if start_pos == "Q":
            print("Saliendo del juego...")
            break

        end_pos = input("Introduce la posición final (ej. A4): ").strip().upper()

        # Validamos el formato de las entradas antes de intentar jugar
        if (len(start_pos) != 2 or not start_pos[0].isalpha() or not start_pos[1].isdigit()):
            print("Entrada inválida en la posición inicial. Asegúrate de ingresar las posiciones en formato correcto (ej. A2, H8).")
            continue

        if (len(end_pos) != 2 or not end_pos[0].isalpha() or not end_pos[1].isdigit()):
            print("Entrada inválida en la posición final. Asegúrate de ingresar las posiciones en formato correcto (ej. A2, H8).")
            continue
        # Intentamos ejecutar la jugada
        if __game__.play(start_pos=start_pos, end_pos=end_pos):
            # Mostramos el tablero después de cada jugada
            __game__.show_board()
        else:
            print("Movimiento no válido.")

        # Verificamos si el juego ha terminado
        if __game__.game_over():
            print("El juego ha terminado.")
            print(__game__.check_victory_status())  # Mostramos el estado final
            break

def main():
    iniciar_juego()
if __name__ == '__main__':
    main()


