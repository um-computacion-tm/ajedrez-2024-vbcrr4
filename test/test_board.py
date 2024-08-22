import unittest
from game.board import *
from game.piece import *
from game.alfil import *
from game.torre import *
from game.rey import *
from game.caballo import *
from game.peon import *
from game.reina import *
from game.exepciones import *
class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_board_initial_setup(self):
        # Verificar que las piezas blancas y negras estén en sus posiciones iniciales
        self.assertIsInstance(self.board.__board__[0][0], Torre)
        self.assertIsInstance(self.board.__board__[0][1], Caballo)
        self.assertIsInstance(self.board.__board__[0][2], Alfil)
        self.assertIsInstance(self.board.__board__[0][3], Reina)
        self.assertIsInstance(self.board.__board__[0][4], Rey)
        self.assertIsInstance(self.board.__board__[0][5], Alfil)
        self.assertIsInstance(self.board.__board__[0][6], Caballo)
        self.assertIsInstance(self.board.__board__[0][7], Torre)
        for i in range(8):
            self.assertIsInstance(self.board.__board__[1][i], Peon)
        
        self.assertIsInstance(self.board.__board__[7][0], Torre)
        self.assertIsInstance(self.board.__board__[7][1], Caballo)
        self.assertIsInstance(self.board.__board__[7][2], Alfil)
        self.assertIsInstance(self.board.__board__[7][3], Reina)
        self.assertIsInstance(self.board.__board__[7][4], Rey)
        self.assertIsInstance(self.board.__board__[7][5], Alfil)
        self.assertIsInstance(self.board.__board__[7][6], Caballo)
        self.assertIsInstance(self.board.__board__[7][7], Torre)
        for i in range(8):
            self.assertIsInstance(self.board.__board__[6][i], Peon)

    '''def test_move_piece_valid(self):
        # Mover un peón blanco adelante una casilla
        self.board.move_piece([1, 0], [2, 0])
        self.assertIsInstance(self.board.__board__[2][0], Peon)
        self.assertIsNone(self.board.__board__[1][0])'''

    def test_move_piece_invalid(self):
        # Intentar mover una pieza en un movimiento inválido
        with self.assertRaises(ValueError):
            self.board.move_piece([0, 0], [2, 2])  # Torre no puede moverse en diagonal

    def test_move_piece_blocked(self):
        # Intentar mover una pieza a través de otra pieza
        with self.assertRaises(ValueError):
            self.board.move_piece([0, 0], [0, 3])  # Torre está bloqueada por otras piezas

    def test_is_clear_path_horizontal(self):
        # Verificar si el camino está despejado horizontalmente
        self.board.__board__[0][1] = None  # Eliminar el caballo blanco de la casilla [0, 1]
        self.board.__board__[0][2] = None  # Eliminar el alfil blanco de la casilla [0, 2]
        self.assertTrue(self.board.is_clear_path([0, 0], [0, 3]))

    def test_is_clear_path_vertical(self):
        # Verificar si el camino está despejado verticalmente
        self.board.__board__[1][0] = None  # Eliminar el peón blanco de la casilla [1, 0]
        self.board.__board__[2][0] = None  # Eliminar el peón blanco de la casilla [2, 0]
        self.assertTrue(self.board.is_clear_path([0, 0], [3, 0]))

    def test_is_not_clear_path(self):
        # Verificar si el camino no está despejado (bloqueado)
        self.assertFalse(self.board.is_clear_path([0, 0], [0, 3]))  # Bloqueado por caballo y alfil

    def test_board_repr(self):
        board = Board()
        expected_board = """      a      b      c      d      e      f      g      h
   ┌───────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┐
8  │   ♖   │  ♘   │  ♗   │  ♕   │  ♔   │  ♗   │  ♘   │  ♖   │ 8
   ├───────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
7  │   ♙   │  ♙   │  ♙   │  ♙   │  ♙   │  ♙   │  ♙   │  ♙   │ 7
   ├───────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
6  │       │      │      │      │      │      │      │      │ 6
   ├───────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
5  │       │      │      │      │      │      │      │      │ 5
   ├───────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
4  │       │      │      │      │      │      │      │      │ 4
   ├───────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
3  │       │      │      │      │      │      │      │      │ 3
   ├───────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
2  │   ♟   │  ♟   │  ♟   │  ♟   │  ♟   │  ♟   │  ♟   │  ♟   │ 2
   ├───────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
1  │   ♜   │  ♞   │  ♝   │  ♛   │  ♚   │  ♝   │  ♞   │  ♜   │ 1
   └───────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┘
      a      b      c      d      e      f      g      h"""
        self.assertEqual(repr(board), expected_board)

if __name__ == "__main__":
    unittest.main()

  