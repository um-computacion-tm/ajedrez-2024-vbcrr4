class Player:
    def __init__(self, color):
        self.__color__ = color
        self.__pieces__ = []
        self.__captured_pieces__ = []
        
    def get_color(self):
        return self.__color__
    
    def get_pieces(self):
        return self.__pieces__
    
