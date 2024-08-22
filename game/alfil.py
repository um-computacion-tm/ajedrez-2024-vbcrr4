from game.piece import Piece

class Alfil(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__nombre__ = "Alfil"
        self.__value__ = self.assign_value()
        self.assign_symbol()
        self.assign_value()

    def assign_symbol(self):
        self.__symbol__ = "♗" if self.__color__ == "white" else "♝"

    def assign_value(self):
        return 3
  
    def is_valid_move(self, star_pos, end_pos):
        """
        Verifica si el movimiento es válido para el Alfil.
        El Alfil se mueve en diagonales.
        """
        direct_x = abs(star_pos[0] - end_pos[0])
        direct_y = abs(star_pos[1] - end_pos[1])
        return direct_x == direct_y
    
    