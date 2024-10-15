from .piece import Piece

class Peon(Piece):
    __w_str__ = "♟"
    __b_str__ = "♙"
    def __init__(self, color, position):
        super().__init__(color, position)

    def assign_value(self):
        return 1

    def validate_movimiento(self, positions, position_new):
        if self.__color__ == "white":
            return self.valid_white_move(positions, position_new)
        elif self.__color__ == "black":
            return self.valid_black_move(positions, position_new)
        return False

    def valid_black_move(self, positions, position_new):

        return self.is_valid_move(positions, position_new, 1, 1)
    
    def valid_white_move(self, positions, position_new):
        return self.is_valid_move(positions, position_new, -1, 6)


    def is_valid_move(self, positions, position_new, direction, initial_row):
        row, col, actual_row, actual_col = self.get_cords(position_new)
        result = False
        if col == actual_col: 
    
            # Valida que el movimiento sea en la misma columna
            if actual_row == initial_row:
                if self.move(positions, position_new, direction):
                    result = True
                elif row == actual_row + 2 * direction and positions[actual_row + direction][actual_col] is None and positions[actual_row + 2 * direction][actual_col] is None:
                    result = True
            elif self.move(positions, position_new, direction):
                result = True
        elif row == actual_row + direction and abs(col - actual_col) == 1 and positions[row][col] is not None:
        # Movimiento de captura
            result = True
        return result
    
    def move(self, positions, position_new, direction):
        row, col, actual_row, actual_col = self.get_cords(position_new)
        if row == actual_row + direction and positions[actual_row + direction][actual_col] is None:
            return True
        return False
