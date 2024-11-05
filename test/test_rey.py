import unittest
from game.rey import Rey
class TestRey(unittest.TestCase):

    def setUp(self):
 
        self.__positions__ = [[None] * 8 for _ in range(8)]
        self.__king__ = Rey("White", (7, 4)) 
        self.__positions__[7][4] = self.__king__

    def test_assign_value(self):
        # Verifica que el valor del rey sea 1000
        self.assertEqual(self.__king__.assign_value(), 1000)
      
    def test_str(self):
        # Verifica que el símbolo del rey se muestre correctamente
        self.assertEqual(str(self.__king__), "♚")
 
    def test_king_white_move_valid(self):
        # Verifica que los movimientos válidos del rey sean permitidos
        self.assertTrue(self.__king__.piece_move(self.__positions__,(6, 4)))  # Movimiento hacia abajo
        self.assertTrue(self.__king__.piece_move(self.__positions__,(6, 5)))  # Movimiento en diagonal

    def test_king_invalid(self):
        # Verifica que los movimientos inválidos del rey no sean permitido
        self.assertFalse(self.__king__.piece_move(self.__positions__,(5, 4)))  # Movimiento de 2 casillas hacia abajo
        self.assertFalse(self.__king__.piece_move(self.__positions__,(7, 6)))  # Movimiento de 2 casillas hacia la derecha 

if __name__ == '__main__':
    unittest.main()