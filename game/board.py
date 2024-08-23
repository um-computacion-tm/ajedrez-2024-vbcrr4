from .peon import Peon
from .torre import Torre
from .alfil import Alfil
from .caballo import Caballo
from .reina import Reina
from .rey import Rey
from .exepciones import InvalidMoveError
class Board:
    def __init__(self):
        self.__board__ = self.create_board()

    def create_board(self):
        # Crear un tablero vacío de 8x8
        board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces(board)
        return board

    def setup_pieces(self, board):
        # Colocar las piezas blancas en sus posiciones iniciales
        board[0][0] = Torre('white')
        board[0][1] = Caballo('white')
        board[0][2] = Alfil('white')
        board[0][3] = Reina('white')
        board[0][4] = Rey('white')
        board[0][5] = Alfil('white')
        board[0][6] = Caballo('white')
        board[0][7] = Torre('white')
        for i in range(8):
            board[1][i] = Peon('white')
        
        # Colocar las piezas negras en sus posiciones iniciales
        board[7][0] = Torre('black')
        board[7][1] = Caballo('black')
        board[7][2] = Alfil('black')
        board[7][3] = Reina('black')
        board[7][4] = Rey('black')
        board[7][5] = Alfil('black')
        board[7][6] = Caballo('black')
        board[7][7] = Torre('black')
        for i in range(8):
            board[6][i] = Peon('black')

    def move_piece(self, start_pos, end_pos):
        piece = self.__board__[start_pos[0]][start_pos[1]]
        if piece is None:
            raise InvalidMoveError("No hay pieza en la posición de inicio")
        if piece.is_valid_move(start_pos, end_pos):
            if self.is_clear_path(start_pos, end_pos):
                # Realizar el movimiento
                self.__board__[end_pos[0]][end_pos[1]] = piece
                self.__board__[start_pos[0]][start_pos[1]] = None
            else:
                raise InvalidMoveError("Movimiento bloqueado por otra pieza")
        else:
            raise InvalidMoveError("Movimiento inválido para esta pieza")

    def is_clear_path(self, start_pos, end_pos):
        """
        Verifica que no haya piezas en el camino entre la posición inicial y final.
        """
        if start_pos[0] == end_pos[0]:  # Movimiento horizontal
            step = 1 if start_pos[1] < end_pos[1] else -1
            for col in range(start_pos[1] + step, end_pos[1], step):
                if self.__board__[start_pos[0]][col] is not None:
                    return False
        elif start_pos[1] == end_pos[1]:  # Movimiento vertical
            step = 1 if start_pos[0] < end_pos[0] else -1
            for row in range(start_pos[0] + step, end_pos[0], step):
                if self.__board__[row][start_pos[1]] is not None:
                    return False
        elif abs(start_pos[0] - end_pos[0]) == abs(start_pos[1] - end_pos[1]):  # Movimiento diagonal
            row_step = 1 if start_pos[0] < end_pos[0] else -1
            col_step = 1 if start_pos[1] < end_pos[1] else -1
            row, col = start_pos[0] + row_step, start_pos[1] + col_step
            while row != end_pos[0] and col != end_pos[1]:
                if self.__board__[row][col] is not None:
                    return False
                row += row_step
                col += col_step
        return True
    
    def __repr__(self):

        spaces = " " * 3
        horizontal_line = spaces + "┌─" + "──────┬" * 7 + "──────┐" + "\n"
        middle_horizontal_line = spaces + "├─" + "──────┼" * 7 + "──────┤" + "\n"
        bottom_horizontal_line = spaces + "└─" + "──────┴" * 7 + "──────┘"
        
        # Agregamos la fila superior con las etiquetas de columnas
        board_repr = "  " * 3 + "      ".join([chr(i) for i in range(ord('a'), ord('h')+1)]) + "\n"
        board_repr += horizontal_line

        for i in range(8):
            board_repr += f"{8 - i}  │ "
            for j in range(8):
                piece = self.__board__[i][j]
                if piece is not None:
                   
                    cell_repr = f" {piece.get_symbol()} ".center(5, " ")
                else:
                    cell_repr = " ".center(5, " ")
                board_repr += cell_repr + " │"
            board_repr += f" {8 - i}\n"
            if i != 7:
                board_repr += middle_horizontal_line

        # Agregamos la fila inferior con las etiquetas de columnas
        board_repr += bottom_horizontal_line + "\n" + "  " * 3 + "      ".join([chr(i) for i in range(ord('a'), ord('h')+1)])
        return board_repr


#imprimir board
board = Board()
print(board)    
