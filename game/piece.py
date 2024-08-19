class InvalidMoveError(Exception):
    pass

class OutOfBoundsError(Exception):
    pass

class InvalidColorError(Exception): 
    pass
class Piece:
    def __init__(self, piece_type, color, initial_position):
        self.__type__ = piece_type
        self.__color__ = color
        self.__position__ = initial_position
        self.__symbol__ = None

    def assign_symbol(self):

        symbols_white = {
            'King': 'k', 'Queen': 'q', 'Rook': 'r', 'Bishop': 'b', 'Knight': 'n', 'Pawn': 'p'
        }
        symbols_black = {
            'King': 'K', 'Queen': 'Q', 'Rook': 'R', 'Bishop': 'B', 'Knight': 'N', 'Pawn': 'P'
        }
        
        if self.__color__ == 'white':
            self.__symbol__ = symbols_white[self.__type__]
        elif self.__color__ == 'black':
            self.__symbol__ = symbols_black[self.__type__]
        else:
            raise InvalidColorError(f"El color {self.__color__} no es válido")


    def validate_move(self, target_position):
        if not (0 <= target_position[0] < 8 and 0 <= target_position[1] < 8):
            raise OutOfBoundsError("La posicion elegida está fuera de los límites del tablero")

    def move(self, target_position):
        self.validate_move(target_position)
        if self.is_valid_move(target_position):
            self.__position__ = target_position
        else:
            raise InvalidMoveError(f"Movimiento inválido para la pieza {self.__type__}")

class Rook(Piece):
    def __init__(self, color, initial_position):
        super().__init__('Rook', color, initial_position)
    
    
    def is_valid_move(self, target_position):
        return self.__position__[0] == target_position[0] or self.__position__[1] == target_position[1]

class Bishop(Piece):
    def __init__(self, color, initial_position):
        super().__init__('Bishop', color, initial_position)

    def is_valid_move(self, target_position):
        return abs(self.__position__[0] - target_position[0]) == abs(self.__position__[1] - target_position[1])

class Queen(Piece):
    def __init__(self, color, initial_position):
        super().__init__('Queen', color, initial_position)

    def is_valid_move(self, target_position):
        return (
            Rook(self.__color__, self.__position__).is_valid_move(target_position) or
            Bishop(self.__color__, self.__position__).is_valid_move(target_position)
        )

class King(Piece):
    def __init__(self, color, initial_position):
        super().__init__('King', color, initial_position)

    def is_valid_move(self, target_position):
        return max(abs(self.__position__[0] - target_position[0]), abs(self.__position__[1] - target_position[1])) == 1

class Knight(Piece):
    def __init__(self, color, initial_position):
        super().__init__('Knight', color, initial_position)

    def is_valid_move(self, target_position):
        dx = abs(self.__position__[0] - target_position[0])
        dy = abs(self.__position__[1] - target_position[1])
        return (dx, dy) in [(1, 2), (2, 1)]

class Pawn(Piece):
    def __init__(self, color, initial_position):
        super().__init__('Pawn', color, initial_position)

    def is_valid_move(self, target_position):
        dx = target_position[0] - self.__position__[0]
        dy = abs(target_position[1] - self.__position__[1])

        if self.__color__ == 'white':
            if self.__position__[0] == 1:
                return (dx == 1 or dx == 2) and dy == 0
            return dx == 1 and dy == 0
        else:
            if self.__position__[0] == 6:
                return (dx == -1 or dx == -2) and dy == 0
            return dx == -1 and dy == 0
