from .piece import Piece

class Alfil(Piece):
    __w_str__ = "♝"
    __b_str__ = "♗"
    def __init__(self, color, positions):
        super().__init__(color, positions)

    def assign_value(self):
        return 3
  
    def alfil_move(self, position_new, positions):
        """
        Verifica si el movimiento es válido para el Alfil.
        El Alfil se mueve en líneas diagonales.
        """
        if self.diagonal_move_positions(position_new, positions):
            return True
        
        return False
    