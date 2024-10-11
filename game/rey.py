from .piece import Piece

class Rey(Piece):
    __b_str__ = "♚"
    __w_str__ = "♔"
    def __init__(self, color, position):
        super().__init__(color, position)

    def assign_value(self):
        return 1000
    
    def move_king(self, position_new, positions):
        """
        Verifica si un movimiento es válido para un rey.
        """
        start_row, start_col, end_row, end_col = self.get_cords(position_new)
        
        # Verifica que el movimiento sea de máximo un cuadrado en cualquier dirección
        if abs(end_row - start_row) <= 1 and abs(end_col - start_col) <= 1:
            # Verifica si la posición de destino está ocupada por una pieza del mismo color
            destination_piece = positions[end_row][end_col]
            if destination_piece is None or destination_piece.color != self.color:
                return True  # El movimiento es válido
        return False  # El movimiento no es válido
    

