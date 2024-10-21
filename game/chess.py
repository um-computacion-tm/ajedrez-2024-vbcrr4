from .board import Board
from .exepciones import *

class Game:
    def __init__(self):
        self.__board__ = Board()
        self.__winner__ = None
        self.__turn__ = "White"

    def show_board(self):
        print(self.__board__)
    
    def play(self, start_pos=None, end_pos=None):
        while not self.game_over():
            if not start_pos or not end_pos:
                start_pos = input(f"Es el turno de {self.__turn__}. Ingresa la posición de la pieza que deseas mover: ")
                if start_pos == "Q":
                    break
                end_pos = input("Ingrese la posición a donde te quieres mover: ")

            print(f"Intentando mover desde {start_pos} hasta {end_pos}")  # Depuración
            if self.valid_moves(start_pos, end_pos):
                print(f"Movimiento válido de {start_pos} a {end_pos}")  # Depuración
                self.movimiento(start_pos, end_pos)
                self.change_turn()  # Cambiar turno solo después de un movimiento válido
                print(f"Turno cambiado a: {self.__turn__}")  # Depuración
            else:
                print(f"Movimiento inválido de {start_pos} a {end_pos}")  # Depuración
                return  # Salir de la función en caso de un movimiento inválido en los tests
            start_pos, end_pos = None, None  # Reset para el siguiente ciclo

        print(self.verify_victory())



    def movimiento(self, pos_actual, pos_destino):
        try:
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
        
    def own_pieces(self, row, col, pos_actual):
    
        #metodo para verificar si la pieza es del mismo color que el turno
        piece = self.__board__.get_piece(row, col)
        #print(f"Verificando si la pieza en ({row}, {col}) es del color correcto: {piece, piece_signal}")
        if piece is None:
            raise PieceNotFoundError("No hay ninguna pieza en la posición de origen.")
            
        color_turn = self.__turn__
        piece_color = self.__board__.color_pieces(row, col)

        if color_turn != piece_color:
            #print(f"Error: La pieza es del color {color_piece}, pero el jugador actual es {color_turn}.")
            raise InvalidColorError("No puedes mover una pieza de otro color.(chess)")
        return piece
        
  
    def check_move(self, move):
        """
        Verifica el estado del juego después de un movimiento.
        Si hay victoria o empate, retorna el resultado.
        De lo contrario, indica que el juego continúa.
        """
        estado_victoria = self.verify_victory()
        if move:
            if estado_victoria == "Ganan las Blancas":
                return "Ganan las Blancas"
            elif estado_victoria == "Ganan las Negras":
                return "Ganan las Negras"
            elif estado_victoria == "Empate":
                return "Empate"
            else:
                return True  # El juego continúa

    def get_turn(self):
        return self.__turn__
    
    def change_turn(self):
        self.__turn__ = "Black" if self.__turn__ == "White" else "White"
        #return self.__turn__
    
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
                raise InvalidInputError
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

