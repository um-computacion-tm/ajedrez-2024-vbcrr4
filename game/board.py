from .piece import Piece
from .torre import Torre
from .peon import Peon
from .alfil import Alfil
from .caballo import Caballo
from .reina import Reina
from .rey import Rey
from .exepciones import * 
class Board:
    def __init__(self):
        #creacion del tablero de 8x8
        #inicializacion de las piezas
        self.__positions__ = []
        for fila in range(8):
            col = []
            for columna in range(8):
                col.append(None)
            self.__positions__.append(col)

        self.__positions__[0][0] = Torre("White", (0, 0))
        self.__positions__[0][1] = Caballo("White", (0, 1))
        self.__positions__[0][2] = Alfil("White", (0, 2))
        self.__positions__[0][3] = Rey("White", (0, 3))
        self.__positions__[0][4] = Reina("White", (0, 4))
        self.__positions__[0][5] = Alfil("White", (0, 5))
        self.__positions__[0][6] = Caballo("White", (0, 6))
        self.__positions__[0][7] = Torre("White", (0, 7))

        for i in range(8):
            self.__positions__[1][i] = Peon("White", (1, i))

        self.__positions__[7][0] = Torre("Black", (7, 0))
        self.__positions__[7][1] = Caballo("Black", (7, 1))
        self.__positions__[7][2] = Alfil("Black", (7, 2))
        self.__positions__[7][3] = Rey("Black", (7, 3))
        self.__positions__[7][4] = Reina("Black", (7, 4))
        self.__positions__[7][5] = Alfil("Black", (7, 5))
        self.__positions__[7][6] = Caballo("Black", (7, 6))
        self.__positions__[7][7] = Torre("Black", (7, 7))

        for i in range(8):
            self.__positions__[6][i] = Peon("Black", (6, i))
    
    def get_piece(self, row, col):
        return self.__positions__[row][col]

    def move(self, origen, destino):
        try:
            self.can_move(origen, destino)
            self.update_positions(origen, destino)
            return True
        except PieceNotFoundError as e:
            print(f"Error: {e}")
            raise
        except InvalidPieceMovement as e:
            print(f"Error: {e}")
            raise
        except InvalidMoveError as e:
            print(f"Error: {e}")
            raise  

    def can_move(self, origen, destino):
        piece = self.get_piece(origen[0], origen[1])
        destino_piece = self.get_piece(destino[0], destino[1])

        if piece is None:
            raise PieceNotFoundError("Pieza no encontrada en el tablero.")

        # Verifica si el movimiento es válido
        if not self.is_valid_move(piece, origen, destino):
            raise InvalidPieceMovement("Movimiento de pieza inválido, el camino no está despejado o el movimiento no es válido.")
        
        # Verifica si hay una pieza en el destino que sea del mismo color
        if destino_piece is not None and piece.color == destino_piece.color:
            raise InvalidMoveError("No puedes moverte donde tienes otra pieza.")
    
    def is_valid_move(self, piece, origen, destino):
        """Verifica si el movimiento es válido para la pieza y el camino está despejado"""
        return (
            (self.is_diagonal_move(origen, destino) and piece.diagonal_move_positions(destino, self.__positions__)) or
            (self.is_vertical_move(origen, destino) and piece.vertical_move_positions(destino, self.__positions__)) or
            (self.is_horizontal_move(origen, destino) and piece.horizontal_move_positions(destino, self.__positions__))
        )


    def update_positions(self, origen, destino):
        piece = self.get_piece(origen[0], origen[1])
        destino_piece = self.get_piece(destino[0], destino[1])

        # Actualizar posiciones en el tablero
        self.__positions__[destino[0]][destino[1]] = piece
        self.__positions__[origen[0]][origen[1]] = None
        piece.update_position(destino)
        if destino_piece is not None:
            destino_piece.update_position(None)

    def is_diagonal_move(self, origen, destino):
        start_row, start_col = origen
        end_row, end_col = destino
        return abs(start_row - end_row) == abs(start_col - end_col)

    def is_vertical_move(self, origen, destino):
        start_row, start_col = origen
        end_row, end_col = destino
        return start_col == end_col and start_row != end_row

    def is_horizontal_move(self, origen, destino):
        start_row, start_col = origen
        end_row, end_col = destino
        return start_row == end_row and start_col != end_col

    def __repr__(self):
        spaces = " " * 3
        horizontal_line = spaces + "┌" + "───────┬" * 7 + "───────┐" + "\n"
        middle_horizontal_line = spaces + "├" + "───────┼" * 7 + "───────┤" + "\n"
        bottom_horizontal_line = spaces + "└" + "───────┴" * 7 + "───────┘"
    
        # Agregamos la fila superior con las etiquetas de columnas
        board_repr = "  " * 3 + "       ".join([chr(i) for i in range(ord('a'), ord('h')+1)]) + "\n"
        board_repr += horizontal_line

        for i in range(8):
            board_repr += f"  {8 - i}│"
            for j in range(8):
                cell = self.__positions__[i][j]
                if cell is None:
                # Si la celda está vacía, representamos como 'None'
                    cell_repr = " ".center(7)
                else:
                # Si hay una pieza, usamos su método __str__()
                    cell_repr = str(cell).center(7)  
                board_repr += f"{cell_repr}│"
            board_repr += f"  {8 - i}\n"
            if i != 7:
                board_repr += middle_horizontal_line

        # Agregamos la fila inferior con las etiquetas de columnas
        board_repr += bottom_horizontal_line + "\n" + "  " * 3 + "       ".join([chr(i) for i in range(ord('a'), ord('h')+1)])
        return board_repr



#if __name__ == "__main__":
    # Crear una instancia de Board
#    tablero = Board()

    # Imprimir la representación del tablero usando __repr__
#    print(tablero)