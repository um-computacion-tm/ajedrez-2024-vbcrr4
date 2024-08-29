
class Piece():
    def __init__(self, color, position):
        self.__color__ = color
        self. __position__ = position

    def get_color(self):
        return self.__color__
    
    def get_position(self):
        return self.__position__
    
    def update_position(self, position_new):
        self.__position__ = position_new
    
    def __str__(self):
        # Llama a assign_symbol, que se espera que esté definido en cada subclase
        return self.assign_symbol()

    def assign_symbol(self):
        # Método que las subclases deben sobrescribir
        raise NotImplementedError("Este método debe ser implementado por las subclases.")
    
    def get_cords(self, position_new):
        end_row, end_col = position_new
        start_row, start_col = self.__position__
        return start_row, start_col, end_row, end_col
    
    def diagonal_move_positions(self, position_new):
        """
        Devuelve las posiciones que la pieza atravesaría si realiza un movimiento diagonal.
        """
        start_row, start_col, end_row, end_col = self.get_cords(position_new)
        positions_to_check = []

        # Comprueba si el movimiento es diagonal
        if abs(start_row - end_row) == abs(start_col - end_col):
            row_step = 1 if start_row < end_row else -1
            col_step = 1 if start_col < end_col else -1
            row, col = start_row + row_step, start_col + col_step
            
            # Genera todas las posiciones entre el inicio y el fin del movimiento
            while row != end_row and col != end_col:
                positions_to_check.append((row, col))
                row += row_step
                col += col_step

        return positions_to_check
    
    def vertical_move_positions(self, position_new):
        """
        Devuelve las posiciones que la pieza atravesaría si realiza un movimiento vertical.
        """
        start_row, start_col, end_row, end_col = self.get_cords(position_new)
        positions_to_check = []

        # Comprueba si el movimiento es vertical
        if start_col == end_col:
            step = 1 if start_row < end_row else -1
            for row in range(start_row + step, end_row, step):
                positions_to_check.append((row, start_col))
        
        return positions_to_check
    
    def horizontal_move_positions(self, position_new):
        """
        Devuelve las posiciones que la pieza atravesaría si realiza un movimiento horizontal.
        """
        start_row, start_col, end_row, end_col = self.get_cords(position_new)
        positions_to_check = []

        # Comprueba si el movimiento es horizontal
        if start_row == end_row:
            step = 1 if start_col < end_col else -1
            for col in range(start_col + step, end_col, step):
                positions_to_check.append((start_row, col))
        
        return positions_to_check
    