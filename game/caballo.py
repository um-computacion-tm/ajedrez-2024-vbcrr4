from .piece import Piece

class Caballo(Piece):
    __w_str__ = "♘"
    __b_str__ = "♞"
    def __init__(self, color, position):
        super().__init__(color, position)

    def assign_value(self):
        return 3

    def is_valid_move(self, row_diff, col_diff):
        """
        Verifica si las diferencias de filas y columnas corresponden a un movimiento en 'L' del caballo.
        """
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)

    
    def is_valid_destination(self, end_row, end_col, positions):
        """
        Verifica si la casilla de destino está vacía o tiene una pieza del color contrario.
        """
        destination_piece = positions[end_row][end_col]
        return destination_piece is None or destination_piece.color != self.color
    

    def move_caballo(self, position_new, positions):
        """
        Verifica si el movimiento es válido para el Caballo.
        El Caballo se mueve en forma de 'L', es decir, 2 casillas en una dirección
        (horizontal o vertical) y 1 casilla en la dirección perpendicular.
        """
        start_row, start_col, end_row, end_col = self.get_cords(position_new)
        
        # Calcula las diferencias en filas y columnas
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        
        # Verifica si el movimiento es en 'L' y si el destino es válido
        if self.is_valid_move(row_diff, col_diff) and self.is_valid_destination(end_row, end_col, positions):
            return True
        
        return False

     
