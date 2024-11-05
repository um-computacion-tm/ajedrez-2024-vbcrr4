import unittest
from game.reina import Reina
class TestReina(unittest.TestCase):
    def setUp(self):
        #inicializacion de tablero
        self.__positions__ = [[None] * 8 for _ in range(8)]
        self.reina_White = Reina('White',(0,4))
        self.reina_Black = Reina('Black', (7, 4))
        self.__positions__[0][4] = self.reina_White
        self.__positions__[7][4] = self.reina_Black

    def test_assign_value(self):
        # Test the assign_value method
        self.assertEqual(self.reina_White.assign_value(), 9)
        self.assertEqual(self.reina_Black.assign_value(), 9)

    def test_valid_white_move(self):
        # Test a valid move for the white queen
        self.assertTrue(self.reina_White.piece_move(self.__positions__,(2, 6)))
        self.assertTrue(self.reina_White.piece_move(self.__positions__,(0, 0)))
        self.assertTrue(self.reina_White.piece_move(self.__positions__,(1, 3)))
        self.assertTrue(self.reina_White.piece_move(self.__positions__,(1, 4)))

    def test_valid_black_move(self):
        # Test a valid move for the black queen
        self.assertTrue(self.reina_Black.piece_move(self.__positions__,(6, 3)))
        self.assertTrue(self.reina_Black.piece_move(self.__positions__,(6, 5)))
        self.assertTrue(self.reina_Black.piece_move(self.__positions__,(7, 0)))
        self.assertTrue(self.reina_Black.piece_move(self.__positions__,(0, 4)))

    def test_invalid_move(self):
        self.assertFalse(self.reina_White.piece_move(self.__positions__,(5, 6)))
        self.assertFalse(self.reina_Black.piece_move(self.__positions__,(6, 6)))

if __name__ == '__main__':
    unittest.main()