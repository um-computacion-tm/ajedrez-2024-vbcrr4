class Piece:
    """
    Clase base para las piezas de ajedrez.

    Atributos:
        __color__ (str): Color de la pieza, puede ser "WHITE" o "BLACK".

    Métodos:
        get_color(): Devuelve el color de la pieza.
    """
    def __init__(self, color):
        self.__color__ = color

    def get_color(self):
        return self.__color__

class Pawn(Piece):  # peón
    def __str__(self):
        return "p" if self.get_color() == "WHITE" else "P"

class Rook(Piece):  # torre
    def __str__(self):
        return "r" if self.get_color() == "WHITE" else "R"

class Knight(Piece):  # caballo
    def __str__(self):
        return "k" if self.get_color() == "WHITE" else "K"

class Bishop(Piece):  # alfil
    def __str__(self):
        return "b" if self.get_color() == "WHITE" else "B"

class Queen(Piece):  # reina
    def __str__(self):
        return "q" if self.get_color() == "WHITE" else "Q"

class King(Piece):  # rey
    def __str__(self):
        return "k" if self.get_color() == "WHITE" else "K"


'''
class Pawn(Piece):  # peón
    def __str__(self):
        return "♙" if self.get_color() == "WHITE" else "♟"

class Rook(Piece):  # torre
    def __str__(self):
        return "♖" if self.get_color() == "WHITE" else "♜"

class Knight(Piece):  # caballo
    def __str__(self):
        return "♘" if self.get_color() == "WHITE" else "♞"

class Bishop(Piece):  # alfil
    def __str__(self):
        return "♗" if self.get_color() == "WHITE" else "♝"

class Queen(Piece):  # reina
    def __str__(self):
        return "♕" if self.get_color() == "WHITE" else "♛"

class King(Piece):  # rey
    def __str__(self):
        return "♔" if self.get_color() == "WHITE" else "♚"

'''