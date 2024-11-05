import unittest
from game.alfil import Alfil
class TestAlfil(unittest.TestCase):

    def setUp(self):
        #iniiclizacion de tablero
        self.__positions__ = [[None] * 8 for _ in range(8)]
        # Creamos alfiles blanco y negro antes de cada test
        self.__White_alfil__ = Alfil("White", (7, 2))  # Alfil blanco en la posición inicial
        self.__Black_alfil__ = Alfil("Black", (0, 2))  # Alfil negro en la posición inicial
        self.__posicionocupada__ = Alfil("White", (5, 0)) 
        self.__positions__[7][2] = self.__White_alfil__
        self.__positions__[0][2] = self.__Black_alfil__
        self.__positions__[5][0] = self.__posicionocupada__

    def test_assign_value(self):
        # Verifica que el valor del alfil sea 3
        self.assertEqual(self.__White_alfil__.assign_value(), 3)
        self.assertEqual(self.__Black_alfil__.assign_value(), 3)

    def test_str(self):
        # Verifica que el símbolo del alfil se muestre correctamente
        self.assertEqual(str(self.__Black_alfil__), "♗")
        self.assertEqual(str(self.__White_alfil__), "♝")

    def test_alfil_white_move_valid(self):
        # Prueba movimientos válidos en diagonal
        self.assertTrue(self.__White_alfil__.piece_move(self.__positions__,(5, 4) ))  # Movimiento diagonal válido
        self.assertTrue(self.__White_alfil__.piece_move(self.__positions__,(4, 5) ))  # Otro movimiento diagonal válido

    #test_alfil_black_move_valid(self):
        # Prueba movimientos válidos en diagonal
        self.assertTrue(self.__Black_alfil__.piece_move(self.__positions__,(3, 5) ))  # Movimiento diagonal válido
        self.assertTrue(self.__Black_alfil__.piece_move(self.__positions__,(2, 0) ))  # Movimiento diagonal válido 

    def test_alfil_white_move_invalid(self):
        # Prueba movimientos inválidos (no diagonales) para el alfil
        self.assertFalse(self.__White_alfil__.piece_move(self.__positions__,(7, 3)))
        self.assertFalse(self.__White_alfil__.piece_move(self.__positions__,(5, 2)))
    
    #test_alfil_black_move_invalid(self):
        # Prueba movimientos inválidos (no diagonales) para el alfil
        self.assertFalse(self.__Black_alfil__.piece_move(self.__positions__,(0, 3)))
        self.assertFalse(self.__Black_alfil__.piece_move(self.__positions__,(2, 2)))

    def test_piece_move_blocked_by_same_color(self):
        # Verifica que el alfil no pueda moverse a una casilla ocupada por una pieza del mismo color
        self.assertFalse(self.__White_alfil__.piece_move(self.__positions__,(5, 0)))  # Movimiento inválido, casilla ocupada

if __name__ == '__main__':
    unittest.main()