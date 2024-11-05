import unittest
from game.torre import Torre
from game.peon import Peon
class TestTorre(unittest.TestCase):
    def setUp(self):
        #inicializacion de tablero
        self.__positions__ = [[None] * 8 for _ in range(8)]
        #
        self.__torre_White__ = Torre('White',(3, 3))
        self.__posicionocupada__ = Peon('White',(5, 1))
        self.__positions__[1][1] = self.__torre_White__
        self.__positions__[1][3] = self.__posicionocupada__

    def test_assign_value(self):
        self.assertEqual(self.__torre_White__.assign_value(), 5)

    def test_valid_white_move(self):
        self.assertTrue(self.__torre_White__.piece_move(self.__positions__,(5, 3)))
    
    def test_torre_blocked_move(self):
        self.__positions__[4][3] = Torre("Black", (4, 3))
        self.assertFalse(self.__torre_White__.piece_move(self.__positions__, (6, 3)))

if __name__ == '__main__':
    unittest.main()