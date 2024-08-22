from abc import ABC, abstractmethod
class Piece(ABC):
    def __init__(self, color):
        self.__color__ = color
        self.__symbol__ = None
        self.__value__ = self.assign_value()

    @abstractmethod
    def assign_symbol(self):
        pass
    
    @abstractmethod
    def is_valid_move(self, star_pos, end_pos, board):
        pass

    @abstractmethod
    def assign_value(self):
        return self.__value__

    def get_color(self):
        return self.__color__

    def get_symbol(self):
        return self.__symbol__
    
    def get_value(self):
        return self.__value__
    