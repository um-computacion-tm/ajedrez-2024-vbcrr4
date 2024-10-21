from .board import Board
from .exepciones import *

class Game:
    def __init__(self):
        self.__board__ = Board()
        self.__winner__ = None
        self.__turn__ = "White"

    def show_board(self):
        print(self.__board__)
    
    def play(self, pos_actual, pos_destino):

        while not self.game_over():
            # Obtener la posición de origen y destino del jugador
            pos_actual = input(f"Es el turno de {self.__turn__}. Ingresa la posición de la pieza que deseas mover: ")
            pos_destino = input("Ingrese la posicion a donde te quieres mover: ")

            # Verificar si el movimiento es válido
            if self.valid_moves(pos_actual, pos_destino):
                # Realizar el movimiento
                self.movimiento(pos_actual, pos_destino)
                print(f"Has movido de {pos_actual} a {pos_destino}.")
            else:
                print("Movimiento inválido. Intenta de nuevo.")
                continue

            # Cambiar el turno
            self.change_turn()  

        # Verificar quién es el ganador
        print(self.verify_winner())

    def movimiento(self, pos_actual, pos_destino):
        try:
            # Imprimir el turno actual y las posiciones antes de realizar cualquier movimiento
            print(f"Turno actual: {self.__turn__}, Moviendo de {pos_actual} a {pos_destino}")
            
            # Traducir input de texto a coordenadas en el tablero
            start_x, start_y = self.traductor_de_input(pos_actual)
            end_x, end_y = self.traductor_de_input(pos_destino)

            # Obtener la pieza en la posición inicial y verificar que sea del color correcto
            origen = self.own_pieces(start_x, start_y, pos_actual)
            destino = (end_x, end_y)
            
            # Mover la pieza en el tablero
            mover_pieza = self.__board__.move(origen, destino)
            
            # Verificar si el movimiento es válido
            movimiento_check = self.check_move(mover_pieza)

            # Imprimir el turno después de intentar el movimiento
            print(f"Turno después del movimiento: {self.__turn__}")

            return movimiento_check

        except (InvalidMoveError, PieceNotFoundError, InvalidPieceMovement, CantEatKingError, ValueError, InvalidColorError) as e:
            print(f"Error: {str(e)}")
            raise

    def valid_moves(self, start_pos, end_pos):
        """
        Verifica si los movimientos son válidos.
        :param start_pos: Cadena con la posición inicial (ej. 'A2').
        :param end_pos: Cadena con la posición final (ej. 'A3').
        :return: True si el movimiento es válido, False en caso contrario.
        """
        try:
            # Traducir las posiciones de entrada a coordenadas
            start_row, start_col = self.traductor_de_input(start_pos)
            end_row, end_col = self.traductor_de_input(end_pos)

            # Verificar si las posiciones están dentro del tablero
            if not self.__board__.validate_out_of_board((start_row, start_col)) or not self.__board__.validate_out_of_board((end_row, end_col)):
                return False

            # Obtener la pieza en la posición inicial
            piece = self.__board__.get_piece(start_row, start_col)
            if piece is None:
                return False

            # Verificar si puede atacar (que no sea su propia pieza)
            target_piece = self.__board__.get_piece(end_row, end_col)
            if target_piece is not None and target_piece.color == piece.color:
                return False

            return True
        except InvalidInputError as e:
            print(f"Error en la entrada: {e}")
            return False
        
    def own_pieces(self, row, col, actual_pos):
        piece = self.__board__.get_piece(row, col)
        print(f"Verificando si la pieza en ({row}, {col}) es del color correcto: {piece}")
        if piece is None:
            raise PieceNotFoundError("No hay ninguna pieza en la posición de origen.")
        if piece.color != actual_pos:
            print(f"Error: La pieza es del color {piece.color}, pero el jugador actual es {actual_pos}.")
            raise InvalidMoveError("No puedes mover una pieza de otro color.")
        return piece


    def check_move(self, move):
        # Llamar a `verify_victory` para verificar si alguien ha ganado o si es empate
        estado_victoria = self.verify_victory()
        result = True
        if move:
            if estado_victoria == "Ganan las Blancas":

                result = "Ganan las Blancas"
            elif estado_victoria == "Ganan las Negras":
                result = "Ganan las Negras"
                
            elif estado_victoria == "Empate":
                result = "Empate"
            # Si no hay un ganador ni empate, cambiar el turno
            else:
                self.change_turn()
                result = True

            return result

    
    def get_turn(self):
        return self.__turn__
    
    def change_turn(self):
        if self.__turn__ == "White":
            self.__turn__ = "Black"
            print("Turno cambiado a Negras")  # Mensaje de depuración
            return "Black"
        else:
            self.__turn__ = "White"
            print("Turno cambiado a Blancas")  # Mensaje de depuración
            return "White"
    def verify_victory(self):
        # Verificar si algún rey ha sido capturado
        rey_blanco = self.__board__.find_king('White')
        rey_negro = self.__board__.find_king('Black')

        if rey_blanco is None:
            self.__winner__ = "Ganan las Negras"
            return "Ganan las Negras"
        elif rey_negro is None:
            self.__winner__ = "Ganan las Blancas"
            return "Ganan las Blancas"

        # Verificar si hay empate (por ejemplo, si solo quedan los reyes)
        if self.__board__.only_kings_left():
            return "Empate"

        # Si no hay victoria ni empate, el juego continúa
        return "El juego continúa."
    
    def game_over(self):
        estado = self.verify_victory()
        return estado != "El juego continúa."


    def traductor_de_input(self, pos):
        try:
            # Limpiar input y validar longitud
            pos = pos.strip()
            if len(pos) != 2:
                raise InvalidInputError("El input ingresado no es válido. Debe tener dos caracteres.")

            # Diccionario para traducir letras a números
            letras_de_col = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
            numeros_de_row = {'8': 0, '7': 1, '6': 2, '5': 3, '4': 4, '3': 5, '2': 6, '1': 7}

            # Convertir la letra a una columna
            letra = letras_de_col.get(pos[0].upper())
            numero = numeros_de_row.get(pos[1])

            # Verificar que ambas coordenadas sean válidas
            if letra is None or numero is None:
                raise InvalidInputError(f"El input ingresado [{pos}] no es válido.")

            return letra, numero
        except InvalidInputError as e:
            print(e)
            raise

