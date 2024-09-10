from .piece import Piece

class Caballo(Piece):
    __w_str__ = "♘"
    __b_str__ = "♞"
    def __init__(self, color, position):
        super().__init__(color, position)

    def assign_value(self):
        return 3

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
        
        # El movimiento en 'L' tiene que ser 2 en una dirección y 1 en la otra
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            # Verifica si la casilla de destino está vacía o tiene una pieza del color contrario
            destination_piece = positions[end_row][end_col]
            if destination_piece is None or destination_piece.get_color != self.get_color:
                return True  

        return False  

     
