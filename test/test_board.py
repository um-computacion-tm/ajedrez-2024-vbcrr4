import unittest
from game.board import Board
from game.piece import *
from game.alfil import *
from game.torre import *
from game.rey import *
from game.caballo import *
from game.peon import Peon
from game.reina import *
from game.exepciones import *
class TestBoard(unittest.TestCase):
    def setUp(self):
        """Configura un tablero de ajedrez para usar en las pruebas."""
        self.board = Board()

    def test_create_board(self):
        """Verifica que el tablero se cree correctamente con las piezas en sus posiciones iniciales."""
        board = self.board.__board__
        self.assertEqual(board[0][0].get_piece().get_color(), 'white')
        self.assertEqual(board[7][7].get_piece().get_color(), 'black')
        self.assertIsInstance(board[0][0].get_piece(), Torre)
        self.assertIsInstance(board[0][3].get_piece(), Reina)
        self.assertIsInstance(board[7][4].get_piece(), Rey)

    '''def test_move_piece_valid(self):
        """Verifica que un movimiento válido se realice correctamente."""
        self.board.move_piece([1, 0], [2, 0])  # Peón blanco de la columna 'a' se mueve hacia adelante
        self.assertIsInstance(self.board.__board__[2][0].get_piece(), Peon)
        self.assertIsNone(self.board.__board__[1][0].get_piece())

    def test_move_piece_invalid_for_piece(self):
        """Verifica que un movimiento inválido para una pieza específica lance InvalidMoveError."""
        with self.assertRaises(InvalidMoveError):
            self.board.move_piece([1, 0], [3, 0])  # Movimiento inválido para un Peón blanco

    def test_move_piece_blocked(self):
        """Verifica que un movimiento bloqueado por otra pieza lance InvalidMoveError."""
        with self.assertRaises(InvalidMoveError):
            self.board.move_piece([0, 0], [0, 3])  # La torre está bloqueada por otras piezas

    def test_is_clear_path_horizontal(self):
        """Verifica que is_clear_path detecte correctamente los bloqueos en movimientos horizontales."""
        # Limpiar la fila 0 para realizar la prueba
        for col in range(1, 8):
            self.board.__board__[0][col].remove_piece()

        self.board.__board__[0][0].place_piece(Torre('white'))
        self.assertTrue(self.board.is_clear_path([0, 0], [0, 7]))

        # Bloquear el camino nuevamente
        self.board.__board__[0][3].place_piece(Peon('white'))
        self.assertFalse(self.board.is_clear_path([0, 0], [0, 7]))

    def test_is_clear_path_vertical(self):
        """Verifica que is_clear_path detecte correctamente los bloqueos en movimientos verticales."""
        # Limpiar la columna 0 para realizar la prueba
        for row in range(1, 8):
            self.board.__board__[row][0].remove_piece()

        self.board.__board__[0][0].place_piece(Torre('white'))
        self.assertTrue(self.board.is_clear_path([0, 0], [7, 0]))

        # Bloquear el camino nuevamente
        self.board.__board__[3][0].place_piece(Peon('white'))
        self.assertFalse(self.board.is_clear_path([0, 0], [7, 0]))

    def test_knight_can_jump(self):
        """Verifica que el caballo pueda saltar sobre otras piezas sin depender de is_clear_path."""
        self.board.move_piece([0, 1], [2, 2])  # El caballo blanco puede saltar sobre otras piezas
        self.assertIsInstance(self.board.__board__[2][2].get_piece(), Caballo)
        self.assertIsNone(self.board.__board__[0][1].get_piece())'''

    def test_board_repr(self):
        board = Board()
        expected_board = """      a       b       c       d       e       f       g       h
   ┌───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┐
  8│   ♖   │   ♘   │   ♗   │   ♕   │   ♔   │   ♗   │   ♘   │   ♖   │  8
   ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
  7│   ♙   │   ♙   │   ♙   │   ♙   │   ♙   │   ♙   │   ♙   │   ♙   │  7
   ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
  6│       │       │       │       │       │       │       │       │  6
   ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
  5│       │       │       │       │       │       │       │       │  5
   ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
  4│       │       │       │       │       │       │       │       │  4
   ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
  3│       │       │       │       │       │       │       │       │  3
   ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
  2│   ♟   │   ♟   │   ♟   │   ♟   │   ♟   │   ♟   │   ♟   │   ♟   │  2
   ├───────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
  1│   ♜   │   ♞   │   ♝   │   ♛   │   ♚   │   ♝   │   ♞   │   ♜   │  1
   └───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┘
      a       b       c       d       e       f       g       h"""
        self.assertEqual(repr(board), expected_board)

if __name__ == "__main__":
    unittest.main()

  