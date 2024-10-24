from .piece import Piece

class Torre(Piece):
    __w_str__ = "♖"
    __b_str__ = "♜"
    def __init__(self, color, position):
        super().__init__(color, position)

    def assign_value(self):
        return 5

    def move_vertical_or_horizontal(self, position_new, positions):
        """
        Verifica si un movimiento vertical es válido para una torre.
        """
        if self.vertical_move_positions(position_new, positions) or self.horizontal_move_positions(position_new, positions):

            return True
        
        return False
