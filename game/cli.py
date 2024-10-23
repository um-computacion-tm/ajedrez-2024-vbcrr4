import os
from .chess import Game
from .exepciones import *

class Interfaz:
    def __init__(self):
        self.__game__ = Game()
        self.contador_turnos = 0  # Contador de turnos

    def limpiar_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_menu_principal(self):
        print(r"""
        Bienvenido a ChessGame
        ----------------------
        Selecciona una opción:
        1. Iniciar nueva partida
        2. Ver reglas
        3. Salir
        """)

    def iniciar(self):
        while True:
            self.limpiar_terminal()
            self.mostrar_menu_principal()
            opcion = input("Escribe tu selección aquí: ")

            if opcion == "1":
                self.limpiar_terminal()
                self.iniciar_partida()
            elif opcion == "2":
                self.limpiar_terminal()
                self.mostrar_reglas()
            elif opcion == "3":
                print("Saliendo de ChessGame. ¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, intenta de nuevo.")

    def mostrar_reglas(self):
        print(r"""
        Reglas del __game__ de ajedrez:
        ---------------------------
        1. Las blancas siempre comienzan.
        2. Los jugadores alternan moviendo una pieza.
        3. El objetivo es hacer jaque mate al rey del oponente.
        4. Puedes rendirte o pedir empate en cualquier momento.

        Presiona Enter para regresar al menú principal.
        """)
        input()
        self.limpiar_terminal()

    def iniciar_partida(self):
        self.__game__ = Game()  # Reiniciar el __game__
        self.contador_turnos = 0  # Reiniciar el contador de turnos
        print("¡Partida iniciada!\n")
        self.bucle_juego()

    def bucle_juego(self):
        while not self.__game__.game_over():
            self.mostrar_estado_juego()

            print("\nSelecciona una acción:")
            print("1. Hacer un movimiento")
            print("2. Ver tablero")
            print("3. Ofrecer empate")
            print("4. Rendirse")
            print("5. Volver al menú principal\n")

            opcion = input("Escribe tu selección aquí: ")

            if opcion == "1":
                pos_inicial = input(f"{self.__game__.get_turn()} - Ingresa la posición de la pieza que deseas mover: ").strip()
                pos_final = input("Ingresa la posición de destino: ").strip()
                self.realizar_movimiento(pos_inicial, pos_final)  # Pasar los argumentos correctos
            elif opcion == "2":
                self.limpiar_terminal()
                self.mostrar_estado_juego()
            elif opcion == "3":
                if self.ofrecer_empate():
                    break
            elif opcion == "4":
                if self.rendirse():
                    break
            elif opcion == "5":
                print("Regresando al menú principal...\n")
                break
            else:
                print("Opción inválida. Por favor, intenta de nuevo.")

    def mostrar_estado_juego(self):
        # Muestra el estado del __game__: tablero y turno actual
        print(f"\nTurno {self.contador_turnos + 1}: Es el turno de {self.__game__.get_turn()}")
        self.__game__.show_board()

    def realizar_movimiento(self, pos_inicial, pos_final ):
        try:
            
            print(f"Intentando mover de {pos_inicial} a {pos_final}")
        
            # Llamamos a play() con las posiciones pasadas
            self.__game__.play(pos_inicial, pos_final)

            self.contador_turnos += 1  # Incrementar el contador de turnos tras un movimiento válido
            self.limpiar_terminal()

        except (InvalidMoveError, InvalidColorError, PieceNotFoundError, InvalidPieceMovement) as e:
            print(f"Movimiento inválido: {e}")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

    def ofrecer_empate(self):
        print(f"\n{self.__game__.get_turn()} ofrece un empate. ¿El oponente acepta? [S/N]")
        respuesta = input().strip().lower()
        if respuesta == "s":
            print("Empate aceptado. La partida termina en empate.")
            return True
        elif respuesta == "n":
            print("Empate rechazado. La partida continúa.")
            return False
        else:
            print("Entrada inválida. Por favor, ingresa S o N.")
            return False

    def rendirse(self):
        jugador = self.__game__.get_turn()
        confirmacion = input(f"\n{jugador}, ¿estás seguro de que deseas rendirte? [S/N]: ").strip().lower()

        if confirmacion == "s":
            ganador = "Negras" if jugador == "Blancas" else "Blancas"
            print(f"\n{jugador} se ha rendido. ¡{ganador} ganan la partida!")
            return True
        else:
            print("Cancelación de la rendición.")
            return False

if __name__ == "__main__":
    interfaz = Interfaz()
    interfaz.iniciar()


