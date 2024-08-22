import unittest
from game.cell import cell

class CellTestCase(unittest.TestCase):
    def test_get_piece(self):
        # Create a cell with a piece
        piece = "pawn"
        status = "occupied"
        c = cell(piece, status)
        
        # Check if the get_piece method returns the correct piece
        self.assertEqual(c.get_piece(), piece)
    
    def test_get_status(self):
        # Create a cell with a status
        piece = "rook"
        status = "occupied"
        c = cell(piece, status)
        
        # Check if the get_status method returns the correct status
        self.assertEqual(c.get_status(), status)

if __name__ == '__main__':
    unittest.main()