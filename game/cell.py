class Cell:
    def __init__(self,piece = None, position = None):
        self.__piece__ = piece
        self.__position__ = position

    def get_piece(self):
        return self.__piece__
    
    def get_position(self):  
        return self.__position__    
    
    def is_occupied(self):
        return self.__piece__ is not None
    
    def place_piece(self, piece):
        if self.is_occupied():
            raise ValueError("La celda ya está ocupada.")
        self.__piece__ = piece

    def remove_piece(self):
        piece = self.__piece__
        self.__piece__ = None
        return piece

    def __repr__(self):
        return self.__piece__.__repr__() if self.is_occupied() else "   "
    