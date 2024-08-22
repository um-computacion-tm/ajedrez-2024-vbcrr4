class cell:
    def __init__(self,piece,status):
        self.__piece__ = piece
        self.__status__ = status

    def get_piece(self):
        return self.__piece__
    
    def get_status(self):  
        return self.__status__