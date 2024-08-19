import unittest
from game.piece import Piece, Rook, Bishop, Queen, King, Knight, Pawn
from game.piece import InvalidMoveError, InvalidColorError , OutOfBoundsError

class TestPiece(unittest.TestCase):
    
    def test_set_pawn_symbol_black(self):
        pawn_1 = Piece('Pawn', 'black', (1,0))
        pawn_2 = Piece('Pawn', 'black', (1,1))
        pawn_3 = Piece('Pawn', 'black', (1,2))
        pawn_4 = Piece('Pawn', 'black', (1,3))
        pawn_5 = Piece('Pawn', 'black', (1,4))
        pawn_6 = Piece('Pawn', 'black', (1,5))
        pawn_7 = Piece('Pawn', 'black', (1,6))
        pawn_8 = Piece('Pawn', 'black', (1,7))
        pawn_1.assign_symbol()
        pawn_2.assign_symbol()
        pawn_3.assign_symbol()
        pawn_4.assign_symbol()
        pawn_5.assign_symbol()
        pawn_6.assign_symbol()
        pawn_7.assign_symbol()  
        pawn_8.assign_symbol()
        self.assertEqual(pawn_1.__symbol__, 'P')
        self.assertEqual(pawn_2.__symbol__, 'P')
        self.assertEqual(pawn_3.__symbol__, 'P')
        self.assertEqual(pawn_4.__symbol__, 'P')
        self.assertEqual(pawn_5.__symbol__, 'P')
        self.assertEqual(pawn_6.__symbol__, 'P')
        self.assertEqual(pawn_7.__symbol__, 'P')
        self.assertEqual(pawn_8.__symbol__, 'P')

    def test_set_queen_symbol(self):
            queen_1 = Piece('Queen', 'black', [0,3])
            queen_2 = Piece('Queen', 'white', (7,3))
            queen_1.assign_symbol()
            queen_2.assign_symbol()
            self.assertEqual(queen_1.__symbol__, 'Q')
            self.assertEqual(queen_2.__symbol__, 'q') 
         
    def test_invalid_color(self):
        with self.assertRaises(InvalidColorError):
            Piece('Queen', 'green', [0, 0]).assign_symbol()

    def test_invalid_color_2(self):
        with self.assertRaises(InvalidColorError):
            Piece('Pawn', 'blak', [1, 0]).assign_symbol()
    
    def test_valid_rook_move(self):
        rook = Rook('white', [0, 0])
        rook.move([0, 5])
        self.assertEqual(rook.__position__, [0, 5])

    def test_invalid_rook_move(self):
        rook = Rook('white', [0, 0])
        with self.assertRaises(InvalidMoveError):
            rook.move([1, 1])

class TestRook(unittest.TestCase):
    def test_rook_horizontal(self):
        rook = Rook('white', [0, 0])
        result = rook.is_valid_move([0, 7])
        self.assertTrue(result)

    def test_rook_vertical(self):
        rook = Rook('white', [0, 0])
        result = rook.is_valid_move([7, 0])
        self.assertTrue(result)

    def test_rook_invalid_move(self):
        rook = Rook('white', [0, 0])
        result = rook.is_valid_move([1, 1])
        self.assertFalse(result)

class TestBishop(unittest.TestCase):
    def test_bishop_diagonal(self):
        bishop = Bishop('white', [0, 0])
        result = bishop.is_valid_move([3, 3])
        self.assertTrue(result)

    def test_bishop_invalid_move(self):
        bishop = Bishop('white', [0, 0])
        result = bishop.is_valid_move([3, 4])
        self.assertFalse(result)

class TestQueen(unittest.TestCase):
    def test_queen_rook_move(self):
        queen = Queen('white', [0, 0])
        result = queen.is_valid_move([0, 5])
        self.assertTrue(result)

    def test_queen_bishop_move(self):
        queen = Queen('white', [0, 0])
        result = queen.is_valid_move([5, 5])
        self.assertTrue(result)

    def test_queen_invalid_move(self):
        queen = Queen('white', [0, 0])
        result = queen.is_valid_move([1, 2])
        self.assertFalse(result)

class TestKing(unittest.TestCase):
    def test_king_valid_move(self):
        king = King('white', [4, 4])
        result = king.is_valid_move([5, 5])
        self.assertTrue(result)

    def test_king_invalid_move(self):
        king = King('white', [4, 4])
        result = king.is_valid_move([6, 6])
        self.assertFalse(result)

class TestKnight(unittest.TestCase):
    def test_knight_l_move(self):
        knight = Knight('white', [0, 0])
        result = knight.is_valid_move([2, 1])
        self.assertTrue(result)

    def test_knight_invalid_move(self):
        knight = Knight('white', [0, 0])
        result = knight.is_valid_move([3, 3])
        self.assertFalse(result)

class TestPawn(unittest.TestCase):
    def test_pawn_first_move_white(self):
        pawn = Pawn('white', [1, 0])
        result = pawn.is_valid_move([3, 0])
        self.assertTrue(result)

    def test_pawn_single_step_white(self):
        pawn = Pawn('white', [2, 0])
        result = pawn.is_valid_move([3, 0])
        self.assertTrue(result)

    def test_pawn_invalid_move_white(self):
        pawn = Pawn('white', [2, 0])
        result = pawn.is_valid_move([4, 0])
        self.assertFalse(result)

    def test_pawn_first_move_black(self):
        pawn = Pawn('black', [6, 0])
        result = pawn.is_valid_move([4, 0])
        self.assertTrue(result)

    def test_pawn_single_step_black(self):
        pawn = Pawn('black', [5, 0])
        result = pawn.is_valid_move([4, 0])
        self.assertTrue(result)

    def test_pawn_invalid_move_black(self):
        pawn = Pawn('black', [5, 0])
        result = pawn.is_valid_move([3, 0])
        self.assertFalse(result)