import colorama
from colorama import Fore, Back, Style
from piece import *

# Inicializa colorama para el uso de colores en la consola
colorama.init(autoreset=True)

class Board:
    """
    Clase que representa el tablero de ajedrez. 

    El tablero es una matriz de 8x8 donde se colocan las piezas de ajedrez en sus posiciones iniciales. 
    Las piezas blancas y negras se colocan en las filas correspondientes según las reglas estándar de ajedrez.
    """

    def __init__(self):
        """
        Inicializa el tablero de ajedrez y coloca las piezas en sus posiciones iniciales.

        - Crea una matriz de 8x8 para representar el tablero.
        - Coloca las piezas blancas en las dos primeras filas (fila 0 y fila 1).
        - Coloca las piezas negras en las dos últimas filas (fila 6 y fila 7).
        """
        self.__positions__ = []
        for fila in range(8):
            self.__positions__.append([])
            for columna in range(8):
                self.__positions__[fila].append(None)
        
        # Colocación de las piezas blancas
        self.__positions__[0][0] = Rook("WHITE")
        self.__positions__[0][1] = Knight("WHITE")
        self.__positions__[0][2] = Bishop("WHITE")
        self.__positions__[0][3] = Queen("WHITE")  # Reina en su color
        self.__positions__[0][4] = King("WHITE")
        self.__positions__[0][5] = Bishop("WHITE")
        self.__positions__[0][6] = Knight("WHITE")
        self.__positions__[0][7] = Rook("WHITE")

        # Peones blancos
        for i in range(8):
            self.__positions__[1][i] = Pawn("WHITE")

        # Colocación de las piezas negras
        self.__positions__[7][0] = Rook("BLACK")
        self.__positions__[7][1] = Knight("BLACK")
        self.__positions__[7][2] = Bishop("BLACK")
        self.__positions__[7][3] = Queen("BLACK")  # Reina en su color
        self.__positions__[7][4] = King("BLACK")
        self.__positions__[7][5] = Bishop("BLACK")
        self.__positions__[7][6] = Knight("BLACK")
        self.__positions__[7][7] = Rook("BLACK")

        # Peones negros
        for i in range(8):
            self.__positions__[6][i] = Pawn("BLACK")

    def imprimir_tablero_con_piezas(self):
        """
        Imprime el tablero de ajedrez en la consola, mostrando las piezas en sus posiciones actuales.

        El tablero se imprime con letras de columna ('a' a 'h') en la parte superior e inferior,
        y números de fila (1 a 8) en los laterales. Las casillas se alternan en color para representar 
        el patrón del tablero de ajedrez.
        """
        tamaño = 8
        letras_columnas = 'abcdefgh'
        
        # Imprimir las letras de las columnas (parte superior)
        print("    " + "  ".join(letras_columnas))
        
        for fila in range(tamaño):
            # Imprimir el número de la fila en el lateral izquierdo
            print(f"{tamaño - fila} ", end="")
            for columna in range(tamaño):
                pieza = self.__positions__[fila][columna]
                color_casilla = Back.WHITE if (fila + columna) % 2 == 0 else Back.BLACK
                pieza_str = str(pieza) if pieza else " "
                print(color_casilla + f"  {pieza_str}  ", end="")  # Ajustar el espaciado
            # Imprimir el número de la fila en el lateral derecho
            print(f" {tamaño - fila}")
        
        # Imprimir las letras de las columnas (parte inferior)
        print("    " + "    ".join(letras_columnas))

'''
board = Board()
board.imprimir_tablero_con_piezas()
'''