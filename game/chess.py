from .board import Board
from .exepciones import *

class Game:
    def __init__(self):
        self.__board__ = Board()
        self.__winner__ = None
        self.__turn__ = "white"

    def print_board(self):
        self.__board__.print_board()

    def get_turn(self):
        return self.__turn__
    
    def change_turn(self):
        if self.__turn__ == "white":
            self.__turn__ = "black"
            return "black"
        else:
            self.__turn__ = "white"
            return "white"

    # Método para validar el movimiento de una pieza
    def validate_move(self, x, y, from_input=["a", 1]):
        try:
            piece = self.__board__.get_piece(x, y)
            if piece is None:
                #Se lanza si no hay una pieza en la posición seleccionada.
                raise PieceNotFoundError(f'In "{from_input[0] + str(from_input[1])}" no se encontó la pieza en la posición seleccionada.')

            color_turn = self.__turn__.lower()
            color_piece = self.__board__.color_pieces(x, y).lower()

            if color_turn == color_piece:
                return piece  # La pieza es válida y es del color correcto
            else:
                raise InvalidColorError(f'No se puede mover una pieza de otro color. Es el turno de {self.__turn__}.')

        except PieceNotFoundError as e:
            raise e
        except InvalidColorError as e:
            raise e
    

    #hice todos estos metodos