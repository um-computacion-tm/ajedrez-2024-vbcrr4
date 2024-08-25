from .peon import Peon
from .torre import Torre
from .alfil import Alfil
from .caballo import Caballo
from .reina import Reina
from .rey import Rey
from .cell  import Cell
from .exepciones import InvalidMoveError
class Board:
    def __init__(self):
        self.__board__ = self.create_board()

    def create_board(self):
        # Crear un tablero vacío de 8x8
        board = [[Cell(None, (row, col)) for col in range(8)] for row in range(8)]
        self.setup_pieces(board)
        return board
    
    def setup_pieces(self, board):
        # Colocar las piezas blancas en sus posiciones iniciales
        board[0][0].place_piece(Torre('white'))
        board[0][1].place_piece(Caballo('white'))
        board[0][2].place_piece(Alfil('white'))
        board[0][3].place_piece(Reina('white'))
        board[0][4].place_piece(Rey('white'))
        board[0][5].place_piece(Alfil('white'))
        board[0][6].place_piece(Caballo('white'))
        board[0][7].place_piece(Torre('white'))
        for i in range(8):
            board[1][i].place_piece(Peon('white'))
        
        # Colocar las piezas negras en sus posiciones iniciales
        board[7][0].place_piece(Torre('black'))
        board[7][1].place_piece(Caballo('black'))
        board[7][2].place_piece(Alfil('black'))
        board[7][3].place_piece(Reina('black'))
        board[7][4].place_piece(Rey('black'))
        board[7][5].place_piece(Alfil('black'))
        board[7][6].place_piece(Caballo('black'))
        board[7][7].place_piece(Torre('black'))
        for i in range(8):
            board[6][i].place_piece(Peon('black'))

    def move_piece(self, start_pos, end_pos):
        start_cell = self.__board__[start_pos[0]][start_pos[1]]
        end_cell = self.__board__[end_pos[0]][end_pos[1]]
        piece = start_cell.get_piece()

        if piece is None:
            raise InvalidMoveError("No hay pieza en la posición de inicio")
        if piece.is_valid_move(start_pos, end_pos, self.__board__):
            if self.is_clear_path(start_pos, end_pos):
                # Realizar el movimiento
                end_cell.place_piece(piece)
                start_cell.remove_piece()
            else:
                raise InvalidMoveError("Movimiento bloqueado por otra pieza")
        else:
            raise InvalidMoveError("Movimiento inválido para esta pieza")

    def is_clear_path(self, start_pos, end_pos):
        """
        Verifica que no haya piezas en el camino entre la posición inicial y final.
        Utiliza la clase Cell para verificar si las celdas están ocupadas.
        """
        #importante los Caballos no pueden utiizar este motodo, ya que pueden saltar piezas
        start_row, start_col = start_pos
        end_row, end_col = end_pos
    
        # Movimiento horizontal
        if start_row == end_row:
            step = 1 if start_col < end_col else -1
            for col in range(start_col + step, end_col, step):
                if self.__board__[start_row][col].is_occupied():
                    return False
    
        # Movimiento vertical
        elif start_col == end_col:
            step = 1 if start_row < end_row else -1
            for row in range(start_row + step, end_row, step):
                if self.__board__[row][start_col].is_occupied():
                    return False
    
        # Movimiento diagonal
        elif abs(start_row - end_row) == abs(start_col - end_col):
            row_step = 1 if start_row < end_row else -1
            col_step = 1 if start_col < end_col else -1
            row, col = start_row + row_step, start_col + col_step
            while row != end_row and col != end_col:
                if self.__board__[row][col].is_occupied():
                    return False
                row += row_step
                col += col_step
    
        return True
    
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
                cell = self.__board__[i][j]
                cell_repr = repr(cell).center(7)  
                board_repr += f"{cell_repr}│"
            board_repr += f"  {8 - i}\n"
            if i != 7:
                board_repr += middle_horizontal_line

        # Agregamos la fila inferior con las etiquetas de columnas
        board_repr += bottom_horizontal_line + "\n" + "  " * 3 + "       ".join([chr(i) for i in range(ord('a'), ord('h')+1)])
        return board_repr


if __name__ == "__main__":
    board = Board()
    print(board)  

