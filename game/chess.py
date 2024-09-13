from .board import Board
#from .player import Player
#Responsable de coordinar y controlar el flujo general del juego.
#Contiene instancias de las siguientes clases: Board y Player.
#Es responsable de manejar los turnos de los jugadores.
#Es responsable de verificar si el juego ha terminado.
#Es responsable de manejar la entrada y salida del juego.
#Es responsable de manejar las reglas del juego.
#Es responsable de manejar la lógica del juego.
#Es responsable de manejar la interacción entre las clases Board y Player.
#Es responsable de manejar la interacción entre las clases Board y Piece.
class Game:
    def __init__(self):
        self.__board__ = Board()
        #self.__players__ = [Player("White"), Player("Black")]
        #self.__current_player__ = self.__players__[0]
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
    


    