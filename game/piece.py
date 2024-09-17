class Piece():
    def __init__(self, color, position):
        self.__color__ = color
        self.__position__ = position
    
    @property
    def color(self):
        return self.__color__
    
    @property
    def position(self):
        return self.__position__
    
    def update_position(self, position_new):
        self.__position__ = position_new
    
    def __str__(self):
        return self.__w_str__ if self.__color__ == "white" else self.__b_str__
    
    def get_cords(self, position_new):
        end_row, end_col = position_new
        start_row, start_col = self.__position__
        return start_row, start_col, end_row, end_col

    def is_path_clear(self, start, end, positions, row_step, col_step):
        """
        Verifica si el camino entre la posición inicial y la final está despejado.
        """
        row, col = start
        end_row, end_col = end

        # Recorre todas las posiciones entre start y end (sin incluir la final)
        for i in range(1, abs(end_row - row) + abs(end_col - col)):
            row += row_step
            col += col_step
            if positions[row][col] is not None:
                return False  # El camino no está despejado
        return True  # El camino está despejado

    def diagonal_move_positions(self, position_new, positions): 
        """
        Verifica si un movimiento diagonal es válido.
        """
        start_row, start_col, end_row, end_col = self.get_cords(position_new)

        # Comprueba si el movimiento es diagonal
        if abs(end_row - start_row) == abs(end_col - start_col):
            row_step = 1 if end_row > start_row else -1
            col_step = 1 if end_col > start_col else -1
            return self.is_path_clear(
                (start_row, start_col), (end_row, end_col), positions, row_step, col_step
            )

        return False

    def vertical_move_positions(self, position_new, positions):
        """
        Verifica si un movimiento vertical es válido.
        """
        start_row, start_col, end_row, end_col = self.get_cords(position_new)

        if end_row != start_row and end_col == start_col:
            row_step = 1 if end_row > start_row else -1
            return self.is_path_clear(
                (start_row, start_col), (end_row, end_col), positions, row_step, 0
            )
        
        return False
    
    def horizontal_move_positions(self, position_new, positions):
        """
        Verifica si un movimiento horizontal es válido.
        """
        start_row, start_col, end_row, end_col = self.get_cords(position_new)

        if end_row == start_row and end_col != start_col:
            col_step = 1 if end_col > start_col else -1
            return self.is_path_clear(
                (start_row, start_col), (end_row, end_col), positions, 0, col_step
            )
        
        return False
