from game.piece import Piece

class Caballo(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__nombre__ = "Caballo"
        self.__value__ = self.assign_value()
        self.assign_symbol()
        self.assign_value()

    def assign_symbol(self):
        self.__symbol__ = "♘" if self.__color__ == "white" else "♞"

    def assign_value(self):
        return 3

    def is_valid_move(self, start_pos, end_pos):
        """
        Verifica si el movimiento es válido para el Caballo.
        El Caballo se mueve en forma de 'L'.
        """
        direct_x = abs(start_pos[0] - end_pos[0])
        direct_y = abs(start_pos[1] - end_pos[1])
        return (direct_x, direct_y) in [(2, 1), (1, 2)]
