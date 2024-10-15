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
        self.__board__ = Board()
    
    def test_initial_setup(self):
        # Verifica que las piezas se han inicializado correctamente
        self.assertIsInstance(self.__board__.get_piece(0, 0), Torre)
        self.assertIsInstance(self.__board__.get_piece(0, 4), Reina)
        self.assertIsInstance(self.__board__.get_piece(7, 0), Torre)
        self.assertIsInstance(self.__board__.get_piece(6, 0), Peon)

    def test_get_piecee(self):
        # Prueba obtener piezas en posiciones específicas
        self.assertIsInstance(self.__board__.get_piece(0, 0), Torre)
        self.assertIsInstance(self.__board__.get_piece(0, 1), Caballo)
        self.assertIsInstance(self.__board__.get_piece(0, 2), Alfil)
        self.assertIsInstance(self.__board__.get_piece(0, 3), Rey)
        self.assertIsInstance(self.__board__.get_piece(0, 4), Reina)
    
    def test_get_piece(self):
        # Prueba que obtener una pieza en una posición específica funcione correctamente
        piece = self.__board__.get_piece(0, 0)
        self.assertIsInstance(piece, Torre)
        self.assertEqual(piece.color, "Black")
    
    def test_get_piece2(self):
        # Prueba que obtener una pieza en una posición específica funcione correctamente
        piece = self.__board__.get_piece(7, 7)
        self.assertIsInstance(piece, Torre)
        self.assertEqual(piece.color, "White")

    def test_move_valid(self):
        # Testea un movimiento válido (peón avanzando una casilla)
        origen = (1, 0)
        destino = (2, 0)
        self.assertTrue(self.__board__.move(origen, destino))
        self.assertIsNone(self.__board__.get_piece(origen[0], origen[1]))  # Verifica que la casilla original esté vacía
        self.assertIsInstance(self.__board__.get_piece(destino[0], destino[1]), Peon)  # Verifica que el peón esté en la nueva casilla

    def test_move_invalid_no_piece(self):
        # Testea mover desde una casilla vacía
        origen = (3, 3)
        destino = (4, 4)
        with self.assertRaises(PieceNotFoundError):
            self.__board__.move(origen, destino)

    def test_move_invalid_path_blocked(self):
        # Prueba que un movimiento inválido (camino bloqueado) lanza la excepción correcta
        origen = (0, 0)  # Torre blanca en (0, 0)
        destino = (3, 0)
        with self.assertRaises(InvalidPieceMovement):
            self.__board__.move(origen, destino)

    def test_move_invalid_destination_occupied(self):
        # Prueba mover una pieza a una casilla ocupada por otra pieza del mismo color
        origen = (0, 0)  # Torre blanca en (0, 0)
        destino = (0, 1)  # Caballo blanco en (0, 1)
        with self.assertRaises(InvalidMoveError):
            self.__board__.move(origen, destino)

    def test_update_positions(self):
        # Prueba que update_positions funcione correctamente
        origen = (1, 0)
        destino = (2, 0)
        self.__board__.update_positions(origen, destino)
        self.assertIsNone(self.__board__.get_piece(origen[0], origen[1]))
        self.assertIsInstance(self.__board__.get_piece(destino[0], destino[1]), Peon)

    def test_is_diagonal_move(self):
        # Prueba que el método is_diagonal_move funcione correctamente
        self.assertTrue(self.__board__.is_diagonal_move((0, 0), (2, 2)))
        self.assertFalse(self.__board__.is_diagonal_move((0, 0), (2, 3)))

    def test_is_vertical_move(self):
        # Prueba que el método is_vertical_move funcione correctamente
        self.assertTrue(self.__board__.is_vertical_move((0, 0), (3, 0)))
        self.assertFalse(self.__board__.is_vertical_move((0, 0), (3, 1)))

    def test_is_horizontal_move(self):
        # Prueba que el método is_horizontal_move funcione correctamente
        self.assertTrue(self.__board__.is_horizontal_move((0, 0), (0, 3)))
        self.assertFalse(self.__board__.is_horizontal_move((0, 0), (1, 3)))

    def test_board_repr(self):
        self.maxDiff = None
        __board__ = Board()
        expected_board = """      a       b       c       d       e       f       g       h
   ┌───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┐
  8│   ♖   │   ♘   │   ♗   │   ♔   │   ♕   │   ♗   │   ♘   │   ♖   │  8
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
  1│   ♜   │   ♞   │   ♝   │   ♚   │   ♛   │   ♝   │   ♞   │   ♜   │  1
   └───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┘
      a       b       c       d       e       f       g       h"""
 
        self.assertEqual(repr(__board__), expected_board)







if __name__ == "__main__":
    unittest.main()
   

