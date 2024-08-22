from game.piece import Piece

class Reina(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__nombre__ = "Reina"
        self.__value__ = self.assign_value()
        self.assign_symbol()
        self.assign_value()

    def assign_symbol(self):
        self.__symbol__ = "♕" if self.__color__ == "white" else "♛"

    def assign_value(self):
        return 9
    
    def is_valid_move(self, star_pos, end_pos):
        """
        Verifica si el movimiento es válido para la Reina.
        La Reina se mueve en líneas rectas horizontales, verticales o diagonales.
        """
        direct_x = abs(star_pos[0] - end_pos[0])
        direct_y = abs(star_pos[1] - end_pos[1])
        return (direct_x == direct_y) or (star_pos[0] == end_pos[0]) or (star_pos[1] == end_pos[1])
    




    