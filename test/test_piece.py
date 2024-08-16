import unittest
from game.board import *
from game.piece import *

class TestPiece(unittest.TestCase):

    def test_piece_get_color_white(self):
        """Probar que get_color devuelve el color 'WHITE' para una pieza blanca."""
        piece = Piece("WHITE")
        self.assertEqual(piece.get_color(), "WHITE")

    def test_piece_get_color_black(self):
        """Probar que get_color devuelve el color 'BLACK' para una pieza negra."""
        piece = Piece("BLACK")
        self.assertEqual(piece.get_color(), "BLACK")


class TestPawn(unittest.TestCase):

    def test_pawn_str_white(self):
        """Probar que __str__ devuelve 'p' para un peón blanco."""
        pawn = Pawn("WHITE")
        self.assertEqual(str(pawn), "p")

    def test_pawn_str_black(self):
        """Probar que __str__ devuelve 'P' para un peón negro."""
        pawn = Pawn("BLACK")
        self.assertEqual(str(pawn), "P")


class TestRook(unittest.TestCase):

    def test_rook_str_white(self):
        """Probar que __str__ devuelve 'r' para una torre blanca."""
        rook = Rook("WHITE")
        self.assertEqual(str(rook), "r")

    def test_rook_str_black(self):
        """Probar que __str__ devuelve 'R' para una torre negra."""
        rook = Rook("BLACK")
        self.assertEqual(str(rook), "R")


class TestKnight(unittest.TestCase):

    def test_knight_str_white(self):
        """Probar que __str__ devuelve 'k' para un caballo blanco."""
        knight = Knight("WHITE")
        self.assertEqual(str(knight), "k")

    def test_knight_str_black(self):
        """Probar que __str__ devuelve 'K' para un caballo negro."""
        knight = Knight("BLACK")
        self.assertEqual(str(knight), "K")


class TestBishop(unittest.TestCase):

    def test_bishop_str_white(self):
        """Probar que __str__ devuelve 'b' para un alfil blanco."""
        bishop = Bishop("WHITE")
        self.assertEqual(str(bishop), "b")

    def test_bishop_str_black(self):
        """Probar que __str__ devuelve 'B' para un alfil negro."""
        bishop = Bishop("BLACK")
        self.assertEqual(str(bishop), "B")


class TestQueen(unittest.TestCase):

    def test_queen_str_white(self):
        """Probar que __str__ devuelve 'q' para una reina blanca."""
        queen = Queen("WHITE")
        self.assertEqual(str(queen), "q")

    def test_queen_str_black(self):
        """Probar que __str__ devuelve 'Q' para una reina negra."""
        queen = Queen("BLACK")
        self.assertEqual(str(queen), "Q")


class TestKing(unittest.TestCase):

    def test_king_str_white(self):
        """Probar que __str__ devuelve 'k' para un rey blanco."""
        king = King("WHITE")
        self.assertEqual(str(king), "k")

    def test_king_str_black(self):
        """Probar que __str__ devuelve 'K' para un rey negro."""
        king = King("BLACK")
        self.assertEqual(str(king), "K")


if __name__ == '__main__':
    unittest.main()
