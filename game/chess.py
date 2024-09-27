from .board import Board

class Game:
    def __init__(self):
        self.__board__ = Board()
        self.__winner__ = None
        self.__turn__ = "white"

    @property
    def set_board(self):
        return self.__board__
    
    def get_turn(self):
        return self.__turn__
    
    def change_turn(self):
        self.__turn__ = "black" if self.__turn__ == "white" else "white"

    def inittial_game(self):
        self.__board__ = Board()
        self.__turn__ = "white"

    def end_game(self):
        self.__board__ = None
        self.__turn__ = None

    def get_piece(self, row, col):
        return self.__board__.get_piece(row, col)
    
    def move (self):
        pass
    


    