import unittest
from game.piece import Piece
class TestPiece(unittest.TestCase):

    def setUp(self):
        # Creamos una instancia de Piece antes de cada test
        self.piece = Piece("Black", (0, 0))
        self.piece2 = Piece("White", (7, 7))
        self.positions = self.prepare_test((0, 0))

    def test_get_color(self):
        # Verifica que el color de la pieza se obtiene correctamente
        self.assertEqual(self.piece.color, "Black")

    def test_get_position(self):
        # Verifica que la posición inicial de la pieza se obtiene correctamente
        self.assertEqual(self.piece.position, (0, 0))

    def test_update_position(self):
        # Verifica que la posición de la pieza se actualiza correctamente
        new_position = (2, 3)
        self.piece.update_position(new_position)
        self.assertEqual(self.piece.position, new_position)

    def test_str(self):
        # Probar la conversión a string de la pieza según su color
        # Esto requiere que la clase tenga `__w_str__` y `__b_str__` definidos
        self.piece.__w_str__ = "♜"
        self.piece.__b_str__ = "♖"
        
        self.assertEqual(str(self.piece), "♖")  

        self.piece = Piece("White", (7, 7))  # Para una pieza negra
        self.piece.__w_str__ = "♜"
        self.piece.__b_str__ = "♖"
        self.assertEqual(str(self.piece), "♜")

    def test_is_path_clear(self):
        # Prueba que el camino esté despejado
        positions = [[None for _ in range(8)] for _ in range(8)]
        start = (0, 0)
        end = (3, 3)
        row_step = 1
        col_step = 1
        self.assertTrue(self.piece.is_path_clear((start, end), positions, row_step, col_step))

        # Prueba cuando el camino está bloqueado
        positions[1][1] = Piece("White", (1, 1))  # Colocamos una pieza en el camino
        self.assertFalse(self.piece.is_path_clear((start, end), positions, row_step, col_step))
    
    def create_empty_board(self):
        """Crea un tablero vacío de 8x8."""
        return [[None for _ in range(8)] for _ in range(8)]

    def prepare_test(self, start_pos):
        """Configura el tablero vacío y actualiza la posición de la pieza."""
        positions = self.create_empty_board()
        self.piece.update_position(start_pos)
        return positions

    def test_diagonal_move_positions2(self):
        # Prueba un movimiento diagonal inválido (camino bloqueado)
        self.positions[1][1] = Piece("White", (1, 1))  # Colocamos una pieza en el camino
        self.assertFalse(self.piece.diagonal_move_positions(self.positions, (3, 3)))

        # Prueba un movimiento no diagonal
        self.assertFalse(self.piece.diagonal_move_positions(self.positions, (2, 3)))

    def test_vertical_move_positions2(self):
        # Prueba un movimiento vertical inválido (camino bloqueado)
        self.positions[1][0] = Piece("White", (1, 0))  # Colocamos una pieza en el camino
        self.assertFalse(self.piece.vertical_move_positions(self.positions, (3, 0)))

        # Prueba un movimiento no vertical
        self.assertFalse(self.piece.vertical_move_positions(self.positions, (3, 1)))

    def test_horizontal_move_positions2(self):
        # Prueba un movimiento horizontal inválido (camino bloqueado)
        self.positions[0][1] = Piece("White", (0, 1))  # Colocamos una pieza en el camino
        self.assertFalse(self.piece.horizontal_move_positions(self.positions, (0, 3)))
        # Prueba un movimiento no horizontal
        self.assertFalse(self.piece.horizontal_move_positions(self.positions, (1, 3)))

    def test_valid_moves(self):
        # Prueba un movimiento horizontal válido
        self.assertTrue(self.piece.horizontal_move_positions(self.positions, (0, 3)))

        # Prueba un movimiento vertical válido
        self.assertTrue(self.piece.vertical_move_positions(self.positions, (3, 0)))

        # Prueba un movimiento diagonal válido
        self.assertTrue(self.piece.diagonal_move_positions(self.positions, (3, 3)))

if __name__ == '__main__':
    unittest.main()
