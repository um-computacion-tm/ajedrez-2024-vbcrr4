from .piece import Piece

class Reina(Piece):
    __w_str__ = "♛"
    __b_str__ = "♕"
    def __init__(self, color,position):
        super().__init__(color, position)

    def assign_value(self):
        return 9
    
  
    def reina_move(self, positions, position_new):
        """
        Verifica si el movimiento es válido para la Reina.
        La Reina se mueve en líneas rectas horizontales, verticales o diagonales.
        """
    
        # Verifica el movimiento 
        if self.vertical_move_positions(position_new, positions) or self.horizontal_move_positions(position_new, positions) or self.diagonal_move_positions(position_new, positions):
            return True
        
        return False  # El movimiento no es válido
    




    