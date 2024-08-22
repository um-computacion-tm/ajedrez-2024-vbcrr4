from game.piece import Piece

class Torre(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__nombre__ = "Torre"
        self.__value__ = self.assign_value()
        self.assign_symbol()
        self.assign_value()

    def assign_symbol(self):
        self.__symbol__ = "♖" if self.__color__ == "white" else "♜"

    def assign_value(self):
        return 5

    def is_valid_move(self, start_pos, end_pos):
        """
        Verifica si el movimiento es válido para la Torre.
        La Torre se mueve en líneas rectas horizontales o verticales.
        """
        return start_pos[0] == end_pos[0] or start_pos[1] == end_pos[1]
