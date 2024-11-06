import unittest
from game.alfil import Alfil
class TestAlfil(unittest.TestCase):

    def setUp(self):
    
        self.__positions__ = [[None] * 8 for _ in range(8)]
        self.__White_alfil__ = Alfil("White", (7, 2))  
        self.__Black_alfil__ = Alfil("Black", (2, 0))  
        self.__posicionocupada__ = Alfil("White", (5, 0)) 
        self.__positions__[7][2] = self.__White_alfil__
        self.__positions__[2][0] = self.__Black_alfil__
        self.__positions__[5][0] = self.__posicionocupada__

    def test_assign_value(self):
        # Verifica que el valor del alfil sea 3
        self.assertEqual(self.__White_alfil__.assign_value(), 3)
        self.assertEqual(self.__Black_alfil__.assign_value(), 3)

    def test_alfil_white_move_valid(self):
        self.assertTrue(self.__Black_alfil__.piece_move(self.__positions__, (4, 2)))  # Movimiento diagonal vál

    def test_alfil_move_invalid(self):
        # Prueba movimientos inválidos (no diagonales) para el alfil
        self.assertFalse(self.__Black_alfil__.piece_move(self.__positions__,(2, 3)))

    def test_piece_move_blocked_by_same_color(self):
        # Verifica que el alfil no pueda moverse a una casilla ocupada por una pieza del mismo color
        self.assertFalse(self.__White_alfil__.piece_move(self.__positions__,(5, 0)))  # Movimiento inválido, casilla ocupada

if __name__ == '__main__':
    unittest.main()