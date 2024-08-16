import unittest
from game.board import *
from game.piece import *
#patchear salidas de print
class TestBoard(unittest.TestCase):

    def setUp(self):
        # Crear una instancia de Board para usar en las pruebas
        self.board = Board()

    def test_init(self):
        board = Board()

        # Check if the board is initialized with a 8x8 matrix
        self.assertEqual(len(board.__positions__), 8)
        for row in board.__positions__:
            self.assertEqual(len(row), 8)

        # Check if the white pieces are placed correctly
        self.assertIsInstance(board.__positions__[0][0], Rook)
        self.assertIsInstance(board.__positions__[0][1], Knight)
        self.assertIsInstance(board.__positions__[0][2], Bishop)
        self.assertIsInstance(board.__positions__[0][3], Queen)
        self.assertIsInstance(board.__positions__[0][4], King)
        self.assertIsInstance(board.__positions__[0][5], Bishop)
        self.assertIsInstance(board.__positions__[0][6], Knight)
        self.assertIsInstance(board.__positions__[0][7], Rook)

        # Check if the black pieces are placed correctly
        self.assertIsInstance(board.__positions__[7][0], Rook)
        self.assertIsInstance(board.__positions__[7][1], Knight)
        self.assertIsInstance(board.__positions__[7][2], Bishop)
        self.assertIsInstance(board.__positions__[7][3], Queen)
        self.assertIsInstance(board.__positions__[7][4], King)
        self.assertIsInstance(board.__positions__[7][5], Bishop)
        self.assertIsInstance(board.__positions__[7][6], Knight)
        self.assertIsInstance(board.__positions__[7][7], Rook)

        # Check if the white pawns are placed correctly
        for i in range(8):
            self.assertIsInstance(board.__positions__[1][i], Pawn)

        # Check if the black pawns are placed correctly
        for i in range(8):
            self.assertIsInstance(board.__positions__[6][i], Pawn)
            


if __name__ == '__main__':
    unittest.main()