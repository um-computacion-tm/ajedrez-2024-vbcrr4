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
        if start_col == end_col:  # Movimiento en la misma columna
            if start_row == initial_row:
                if self.move(positions, position_new, direction):
                    result = True  #40
                elif start_row == end_row + 2 * direction and positions[start_row + direction][start_col] is None and positions[start_row + 2 * direction][start_col] is None:
                    result = True  #42
            elif self.move(positions, position_new, direction):  #43
                result = True  #44
        # Movimiento de captura en diagonal
        elif end_row == start_row + direction and abs(end_col - start_col) == 1 and positions[end_row][end_col] is not None:
            #print("Movimiento de captura detectado")  # Debug
            result = True
        
        return result

    def move(self, positions, position_new, direction):
        start_row, start_col, end_row, end_col = self.get_cords(position_new)

        if start_row == end_row + direction and positions[end_row + direction][end_col] is None:
            return True  #61
        return False
