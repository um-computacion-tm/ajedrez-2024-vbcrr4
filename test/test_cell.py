import unittest
from game.cell import *
from game.piece import *    
from game.peon import Peon
class CellTestCase(unittest.TestCase):
    
    def test_initialization(self):
        """Prueba que una celda se inicializa correctamente sin pieza."""
        cell = Cell(None, (0, 0))
        self.assertIsNone(cell.get_piece())
        self.assertEqual(cell.get_position(), (0, 0))
        self.assertFalse(cell.is_occupied())

    def test_place_piece(self):
        """Prueba que se puede colocar una pieza en una celda."""
        cell = Cell(None, (0, 0))
        peon = Peon("white")
        cell.place_piece(peon)
        self.assertTrue(cell.is_occupied())
        self.assertEqual(cell.get_piece(), peon)

    def test_remove_piece(self):
        """Prueba que se puede remover una pieza de una celda."""
        cell = Cell(None, (0, 0))
        peon = Peon("white")
        cell.place_piece(peon)
        removed_piece = cell.remove_piece()
        self.assertFalse(cell.is_occupied())
        self.assertIsNone(cell.get_piece())
        self.assertEqual(removed_piece, peon)

    def test_place_piece_on_occupied_cell(self):
        """Prueba que no se puede colocar una pieza en una celda ya ocupada."""
        cell = Cell(None, (0, 0))
        peon1 = Peon("white")
        peon2 = Peon("black")
        cell.place_piece(peon1)
        with self.assertRaises(ValueError):
            cell.place_piece(peon2)

    def test_remove_piece_from_empty_cell(self):
        """Prueba que remover una pieza de una celda vacía no causa errores."""
        cell = Cell(None, (0, 0))
        removed_piece = cell.remove_piece()
        self.assertIsNone(removed_piece)
        self.assertFalse(cell.is_occupied())

if __name__ == '__main__':
    unittest.main()