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
        self.assertIsInstance(self.__board__.get_piece(0, 1), Caballo)
        self.assertIsInstance(self.__board__.get_piece(0, 2), Alfil)
        self.assertIsInstance(self.__board__.get_piece(0, 3), Rey)
        self.assertIsInstance(self.__board__.get_piece(0, 4), Reina)
        self.assertIsInstance(self.__board__.get_piece(0, 5), Alfil)
        self.assertIsInstance(self.__board__.get_piece(0, 6), Caballo)
        self.assertIsInstance(self.__board__.get_piece(0, 7), Torre)
        self.assertIsInstance(self.__board__.get_piece(1, 0), Peon)
        self.assertIsInstance(self.__board__.get_piece(1, 7), Peon)
        #
        self.assertIsInstance(self.__board__.get_piece(7, 0), Torre)
        self.assertIsInstance(self.__board__.get_piece(7, 1), Caballo)
        self.assertIsInstance(self.__board__.get_piece(7, 2), Alfil)
        self.assertIsInstance(self.__board__.get_piece(7, 3), Rey)
        self.assertIsInstance(self.__board__.get_piece(7, 4), Reina)
        self.assertIsInstance(self.__board__.get_piece(7, 5), Alfil)
        self.assertIsInstance(self.__board__.get_piece(7, 6), Caballo)
        self.assertIsInstance(self.__board__.get_piece(7, 7), Torre)
        self.assertIsInstance(self.__board__.get_piece(6, 0), Peon)
        self.assertIsInstance(self.__board__.get_piece(6, 7), Peon)
 
    def test_pieces_color(self):
        
        piece = self.__board__.get_piece(0, 0)
        piece2 = self.__board__.get_piece(0, 1)
        piece3 = self.__board__.get_piece(0, 2)
        piece4 = self.__board__.get_piece(0, 3)
        piece5 = self.__board__.get_piece(0, 4)
        piece6 = self.__board__.get_piece(0, 5)
        piece7 = self.__board__.get_piece(0, 6)
        #
        piece8 = self.__board__.get_piece(7, 0)
        piece9 = self.__board__.get_piece(7, 1)
        piece10 = self.__board__.get_piece(7, 2)
        piece11 = self.__board__.get_piece(7, 3)
        piece12 = self.__board__.get_piece(7, 4)
        piece13 = self.__board__.get_piece(7, 5)
        piece14 = self.__board__.get_piece(7, 6)
        #
        self.assertIsInstance(piece, Torre)
        self.assertIsInstance(piece2, Caballo)
        self.assertIsInstance(piece3, Alfil)
        self.assertIsInstance(piece4, Rey)
        self.assertIsInstance(piece5, Reina)
        self.assertIsInstance(piece6, Alfil)
        self.assertIsInstance(piece7, Caballo)
        #
        self.assertIsInstance(piece8, Torre)
        self.assertIsInstance(piece9, Caballo)
        self.assertIsInstance(piece10, Alfil)
        self.assertIsInstance(piece11, Rey)
        self.assertIsInstance(piece12, Reina)
        self.assertIsInstance(piece13, Alfil)
        self.assertIsInstance(piece14, Caballo)
        #
        self.assertEqual(piece.color, "Black")
        self.assertEqual(piece2.color, "Black")
        self.assertEqual(piece3.color, "Black")
        self.assertEqual(piece4.color, "Black")
        self.assertEqual(piece5.color, "Black")
        self.assertEqual(piece6.color, "Black")
        self.assertEqual(piece7.color, "Black")
        #
        self.assertEqual(piece8.color, "White")
        self.assertEqual(piece9.color, "White")
        self.assertEqual(piece10.color, "White")
        self.assertEqual(piece11.color, "White")
        self.assertEqual(piece12.color, "White")
        self.assertEqual(piece13.color, "White")
        self.assertEqual(piece14.color, "White")

    def test_get_piece(self):
        # Verifica que al llamar el método "get_piece", se obtengan las piezas en sus posiciones iniciales (no None)
        for i in range(8):
            piece_0 = self.__board__.get_piece(0, i)
            piece_1 = self.__board__.get_piece(1, i)
            piece_6 = self.__board__.get_piece(6, i)
            piece_7 = self.__board__.get_piece(7, i)
            
            self.assertIsNotNone(piece_0)
            self.assertEqual(piece_0.position, (0, i))
            
            self.assertIsNotNone(piece_1)
            self.assertEqual(piece_1.position, (1, i))
            
            self.assertIsNotNone(piece_6)
            self.assertEqual(piece_6.position, (6, i))
            
            self.assertIsNotNone(piece_7)
            self.assertEqual(piece_7.position, (7, i))

    def test_place_piece(self):
        """Prueba que place_piece coloque correctamente una pieza."""
        peon_blanco = Peon("White", (3, 3))
        self.__board__.place_piece(3, 3, peon_blanco)
        self.assertEqual(self.__board__.get_piece(3, 3), peon_blanco)

    def test_search_piece(self):
        """Prueba la búsqueda de una pieza específica en el tablero."""
        rey_negro = self.__board__.get_piece(0, 3)
        posicion = self.__board__.search_piece(rey_negro)
        self.assertEqual(posicion, (0, 3))
        # Verifica la búsqueda de una pieza no presente
        self.assertIsNone(self.__board__.search_piece(None))

    def test_move_valid(self):
        """Prueba un movimiento válido de una pieza."""
        # Mueve un peón blanco
        origen = (6, 0)
        destino = (4, 0)
        self.__board__.move(origen, destino)
        self.assertIsNone(self.__board__.get_piece(6, 0))  # La posición de origen debe estar vacía
        self.assertIsInstance(self.__board__.get_piece(4, 0), Peon)  # El peón debe estar en la posición de destino

    def test_move_invalid(self):
        """Prueba un movimiento inválido que lanza excepciones."""
        # Intenta mover una pieza desde una posición vacía
        with self.assertRaises(PieceNotFoundError):
            self.__board__.move((2, 2), (3, 3))

        # Intenta mover una pieza a una posición ocupada por una pieza del mismo color
        with self.assertRaises(InvalidMoveError):
            self.__board__.move((0, 0), (0, 1))  # Mover la torre negra al lugar del caballo negro

    def test_only_kings_left(self):
        """Prueba si solo quedan los reyes en el tablero."""
        self.__board__.reset_board()
        self.__board__.place_piece(0, 3, Rey("Black", (0, 3)))
        self.__board__.place_piece(7, 3, Rey("White", (7, 3)))
        self.assertTrue(self.__board__.only_kings_left())

        # Si hay alguna otra pieza, debería retornar False
        self.__board__.place_piece(1, 1, Peon("Black", (1, 1)))
        self.assertFalse(self.__board__.only_kings_left())

    def test_find_king(self):
        """Prueba la búsqueda del rey por su color."""
        self.assertEqual(self.__board__.find_king("Black"), (0, 3))
        self.assertEqual(self.__board__.find_king("White"), (7, 3))

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

    def test_validate_out_of_board(self):
        """Prueba que la validación de posiciones fuera del tablero funcione correctamente."""
        self.assertTrue(self.__board__.validate_out_of_board((-1, 0)))
        self.assertTrue(self.__board__.validate_out_of_board((8, 0)))
        self.assertTrue(self.__board__.validate_out_of_board((0, -1)))
        self.assertTrue(self.__board__.validate_out_of_board((0, 8)))
        self.assertFalse(self.__board__.validate_out_of_board((0, 0)))  # dentro del tablero
        self.assertFalse(self.__board__.validate_out_of_board((7, 7)))  # dentro del tablero

    def test_move_capture_piece(self):
        """Prueba que una pieza capture correctamente una pieza enemiga."""
        origen = (6, 0)  # Peón blanco
        destino = (1, 0)  # Peón negro
        self.__board__.move(origen, destino)  # El peón blanco debe capturar al peón negro
        self.assertIsInstance(self.__board__.get_piece(1, 0), Peon)  # El peón blanco ahora en la posición del peón negro
        self.assertIsNone(self.__board__.get_piece(6, 0))  # La posición original del peón blanco debe estar vacía

    def test_reset_board(self):
        """Prueba que reset_board vacíe correctamente todas las posiciones del tablero."""
        self.__board__.reset_board()
        for row in range(8):
            for col in range(8):
                self.assertIsNone(self.__board__.get_piece(row, col))  # Todas las posiciones deben estar vacías

    def test_invalid_move_raises_exception(self):
        """Prueba que mover una pieza fuera del tablero o de forma inválida levanta las excepciones correctas."""
        # Movimiento fuera del tablero
        with self.assertRaises(InvalidMoveError):
            self.__board__.move((6, 0), (8, 0))  # Mover un peón fuera del tablero

        # Mover una pieza de manera inválida
        with self.assertRaises(InvalidPieceMovement):
            self.__board__.move((0, 0), (2, 3))  # Mover una torre de manera inválida (diagonal)

    def test_search_piece_not_found(self):
        """Prueba la búsqueda de una pieza que no está en el tablero."""
        pieza_no_existe = Peon("White", (4, 4))
        self.assertIsNone(self.__board__.search_piece(pieza_no_existe))  # Debe devolver None ya que no existe

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
   

