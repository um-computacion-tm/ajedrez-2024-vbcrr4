import unittest
from game.torre import Torre
from game.peon import Peon
class TestTorre(unittest.TestCase):
    def setUp(self):
        #inicializacion de tablero
        self.__positions__ = [[None] * 8 for _ in range(8)]
        self.__torre__ = Torre('Black',(3, 3))
        self.__positions__[1][1] = self.__torre__

    def test_assign_value(self):
        self.assertEqual(self.__torre__.assign_value(), 5)

    def test_valid_white_move(self):
        self.assertTrue(self.__torre__.piece_move(self.__positions__,(5, 3)))
    
    def test_torre_blocked_move(self):
        self.__positions__[4][3] = Torre("White", (4, 3))
        self.assertFalse(self.__torre__.piece_move(self.__positions__, (6, 3)))

if __name__ == '__main__':
    unittest.main()