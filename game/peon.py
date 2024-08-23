from game.piece import Piece

class Peon(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__nombre__ = "Peon"
        self.__value__ = self.assign_value()
        self.assign_symbol()
        self.assign_value()
        
    def assign_symbol(self):
        self.__symbol__ = "♙" if self.__color__ == "white" else "♟"

    def assign_value(self):
        return 1

    def is_valid_move(self, start_pos, end_pos):
            """
            Verifica si el movimiento es válido para el Peón.
            El Peón se mueve hacia adelante una casilla, excepto en su primer movimiento,
            donde puede moverse dos casillas.
            """
            direct_x = start_pos[0] - end_pos[0]
            direct_y = start_pos[1] - end_pos[1]
            if self.__color__ == "white":
                return (direct_x == 1 or (direct_x == 2 and start_pos[0] == 6)) and direct_y == 0
            else:
                return (direct_x == -1 or (direct_x == -2 and start_pos[0] == 1)) and direct_y == 0