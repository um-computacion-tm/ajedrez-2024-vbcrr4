from .piece import Piece

class Peon(Piece):
    __w_str__ = "♟"
    __b_str__ = "♙"
    def __init__(self, color, position):
        super().__init__(color, position)

    def assign_value(self):
        return 1

    def validate_movimiento(self, positions, position_new):
        if self.__color__ == "White":
            return self.valid_white_move(positions, position_new)
        elif self.__color__ == "Black":
            return self.valid_black_move(positions, position_new)
        return False    #17

    def valid_black_move(self, positions, position_new):

        return self.is_valid_move(positions, position_new, 1, 1)
    
    def valid_white_move(self, positions, position_new):
        return self.is_valid_move(positions, position_new, -1, 6)


    def is_valid_move(self, positions, position_new, direction, initial_row):
        start_row, start_col = self.position  # Posición actual del peón
        end_row, end_col = position_new       # Nueva posición del peón

        result = False

        # Movimiento vertical simple
        if start_col == end_col:
            # Movimiento de una casilla hacia adelante
            if start_row + direction == end_row and positions[end_row][end_col] is None:
                result = True
            # Movimiento inicial de dos casillas hacia adelante
            elif start_row == initial_row and start_row + 2 * direction == end_row and positions[start_row + direction][start_col] is None and positions[end_row][end_col] is None:
                result = True

        # Movimiento diagonal para capturar
        elif abs(start_col - end_col) == 1 and start_row + direction == end_row and positions[end_row][end_col] is not None:
            result = True

        return result


    def move(self, positions, position_new, direction):
        start_row, start_col = self.position
        end_row, end_col = position_new

        # Movimiento de una casilla hacia adelante
        if start_row + direction == end_row and positions[end_row][end_col] is None:
            return True

        return False

