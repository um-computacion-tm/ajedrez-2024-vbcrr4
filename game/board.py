class Board:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        # Crear un tablero de 8x8 con las posiciones iniciales
        board = [[' ' for _ in range(8)] for _ in range(8)]
        self.setup_pieces(board)
        return board

    def setup_pieces(self, board):
        # Colocamos las piezas en su posición inicial
        # Piezas blancas
        board[0] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        board[1] = ['p' for _ in range(8)]
        # Piezas negras
        board[6] = ['P' for _ in range(8)]
        board[7] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']

    def __repr__(self):
        spaces = " " * 3
        horizontal_line = spaces + "┌─" + "──────┬" * 7 + "──────┐" + "\n"
        middle_horizontal_line = spaces + "├─" + "──────┼" * 7 + "──────┤" + "\n"
        bottom_horizontal_line = spaces + "└─" + "──────┴" * 7 + "──────┘"
        
        # Agregamos la fila superior con las etiquetas de columnas
        board_repr = " " * 5 + "      ".join([chr(i) for i in range(ord('a'), ord('h')+1)]) + "\n"
        board_repr += horizontal_line

        for i in range(8):
            board_repr += f"{8 - i}  │ "#
            for j in range(8):
                cell_repr = f" {self.board[i][j]} ".center(5, " ")
                board_repr += cell_repr + " │"
            board_repr += f" {8 - i}\n"
            if i != 7:
                board_repr += middle_horizontal_line
        
        # Agregamos la fila inferior con las etiquetas de columnas
        board_repr += bottom_horizontal_line + "\n" + " " * 5 + "      ".join([chr(i) for i in range(ord('a'), ord('h')+1)])
        return board_repr


