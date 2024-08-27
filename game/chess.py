from .board import Board
from .player import Player
#Responsable de coordinar y controlar el flujo general del juego.
#Contiene instancias de las siguientes clases: Board y Player.
#Es responsable de manejar los turnos de los jugadores.
#Es responsable de verificar si el juego ha terminado.
#Es responsable de manejar la entrada y salida del juego.
#Es responsable de manejar las reglas del juego.
#Es responsable de manejar la lógica del juego.
#Es responsable de manejar la interacción entre las clases Board y Player.
#Es responsable de manejar la interacción entre las clases Board y Piece.
class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__winner__ = None
        self.__game_over__ = False
        self.__turns__ = 0
        self.__moves__ = []
        

    def display_board(self):
        return self.__board__

    def cambio_turno(self):
        if self.__turns__ % 2 == 0:
            return 'white'
        else:
            return 'black'
        
    '''def game_loop(self):
        while not self.__game_over__:
            self.__turns__ += 1
            self.__print_board__()
            self.__print_turn__()
            self.__print_moves__()
            self.__make_move__()
            self.__check_game_over__()
            self.__switch_players__()
        self.__print_winner__()'''
    


    