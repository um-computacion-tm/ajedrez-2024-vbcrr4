import unittest
from game.torre import Torre
class TestTorre(unittest.TestCase):
    def setUp(self):
        #inicializacion de tablero
        self.__positions__ = [[None] * 8 for _ in range(8)]
        #
        self.torre_White = Torre('White',(1, 1))
        self.__positions__[1][1] = self.torre_White

    def test_assign_value(self):
        # Test the assign_value method
        self.assertEqual(self.torre_White.assign_value(), 5)

    def test_valid_white_move(self):
        # Test a valid move for the white tower
        self.assertTrue(self.torre_White.piece_move(self.__positions__,(1, 5)))
        self.assertTrue(self.torre_White.piece_move(self.__positions__,(5, 1)))
    
    def test_torre_blocked_move(self):
        # Test a move that is blocked by another
        self.__positions__[1][3] = Torre('White', (1, 3))
        self.assertFalse(self.torre_White.piece_move(self.__positions__,(1, 5)))

if __name__ == '__main__':
    unittest.main()