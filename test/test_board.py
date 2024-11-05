import unittest
from unittest.mock import MagicMock
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

    def test_torre_move2(self):
        # Coloca una torre blanca en la posición inicial (5, 0)
        torre = Torre("White", (5, 0))
        self.__board__.place_piece(5, 0, torre)

        # Verifica que la torre esté en la posición correcta
        self.assertIsInstance(self.__board__.get_piece(5, 0), Torre)

        # Movimiento válido (vertical) -> Intentamos mover la torre
        self.assertTrue(self.__board__.is_valid_move((5, 0), (5, 4)))
        # Realiza el movimiento 
        self.__board__.move((5, 0), (5, 4))

        # Verifica que la torre haya sido movida correctamente
        self.assertIsInstance(self.__board__.get_piece(5, 4), Torre)
        self.assertIsNone(self.__board__.get_piece(5, 0))  # La posición anterior debe estar vacía

    def test_validate_out_of_board(self):
        """Prueba que la validación de posiciones fuera del tablero funcione correctamente."""
        self.assertFalse(self.__board__.validate_out_of_board((-1, 0)))
        self.assertFalse(self.__board__.validate_out_of_board((8, 0)))
        self.assertFalse(self.__board__.validate_out_of_board((0, -1)))
        self.assertFalse(self.__board__.validate_out_of_board((0, 8)))
        self.assertTrue(self.__board__.validate_out_of_board((0, 0)))  # dentro del tablero
        self.assertTrue(self.__board__.validate_out_of_board((7, 7)))  # dentro del tablero


    def test_reset_board(self):
        """Prueba que reset_board vacíe correctamente todas las posiciones del tablero."""
        self.__board__.reset_board()
        for row in range(8):
            for col in range(8):
                self.assertIsNone(self.__board__.get_piece(row, col))  # Todas las posiciones deben estar vacías

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

    def test_move_valid(self):
        """Prueba un movimiento válido y verifica su resultado en el tablero."""
        peon_blanco = Peon("White", (6, 0))
        destino = (5, 0)
        self.__board__.place_piece(6, 0, peon_blanco)
        self.__board__.move((6, 0), destino)
        
        # Verificar que la pieza se haya movido correctamente
        self.assertIsNone(self.__board__.get_piece(6, 0))
        self.assertEqual(self.__board__.get_piece(*destino), peon_blanco)

    def test_move_invalid_out_of_bounds(self):
        """Prueba el manejo de un movimiento fuera de los límites del tablero."""
        with self.assertRaises(InvalidMoveError):
            self.__board__.move((-1, 0), (0, 0))

    def test_move_invalid_no_piece_at_origin(self):
        """Prueba el manejo de un movimiento desde una posición sin pieza."""
        destino = (4, 4)
        with self.assertRaises(PieceNotFoundError):
            self.__board__.move((4, 4), destino)

    def test_can_move_valid(self):
        """Prueba que `can_move` permita un movimiento válido."""
        peon_blanco = Peon("White", (6, 0))
        self.__board__.place_piece(6, 0, peon_blanco)
        destino = (5, 0)

        # No debe lanzar ninguna excepción
        try:
            self.__board__.can_move((6, 0), destino)
        except Exception as e:
            self.fail(f"can_move lanzó una excepción inesperada: {e}")

    def test_can_move_invalid_blocked_by_same_color(self):
        """Prueba que `can_move` prohíba movimientos a una posición ocupada por una pieza del mismo color."""
        torre_blanca = Torre("White", (7, 0))
        peon_blanco = Peon("White", (6, 0))
        self.__board__.place_piece(7, 0, torre_blanca)
        self.__board__.place_piece(6, 0, peon_blanco)

        with self.assertRaises(InvalidMoveError):
            self.__board__.can_move((7, 0), (6, 0))

    def test_is_valid_move_capturing_opponent(self):
        """Prueba `is_valid_move` con una captura válida de una pieza oponente."""
        peon_blanco = Peon("White", (6, 0))
        peon_negro = Peon("Black", (5, 1))
        self.__board__.place_piece(6, 0, peon_blanco)
        self.__board__.place_piece(5, 1, peon_negro)

        self.assertTrue(self.__board__.is_valid_move((6, 0), (5, 1)))

    def test_is_valid_move_blocked_by_own_piece(self):
        """Prueba `is_valid_move` en un intento de moverse a una posición ocupada por una pieza propia."""
        torre_blanca = Torre("White", (7, 0))
        peon_blanco = Peon("White", (6, 0))
        self.__board__.place_piece(7, 0, torre_blanca)
        self.__board__.place_piece(6, 0, peon_blanco)

        with self.assertRaises(InvalidMoveError):
            self.__board__.is_valid_move((7, 0), (6, 0))

    def test_execute_move(self):
        """Prueba `execute_move` para verificar que actualice correctamente el tablero."""
        peon_blanco = Peon("White", (6, 0))
        destino = (5, 0)
        self.__board__.place_piece(6, 0, peon_blanco)

        self.__board__.execute_move((6, 0), destino)

        # Comprobar que la pieza se movió
        self.assertIsNone(self.__board__.get_piece(6, 0))
        self.assertEqual(self.__board__.get_piece(*destino), peon_blanco)
        self.assertEqual(peon_blanco.position, destino)  # Verificar actualización de posición interna


####
    def test_execute_move_piece_origen_is_none(self):
        """Prueba que `execute_move` lance `PieceNotFoundError` si `pieza_origen` es `None`."""
        with self.assertRaises(PieceNotFoundError):
            self.__board__.execute_move((4, 4), (5, 5))

    def test_execute_move_piece_destino_not_none(self):
        """Prueba que `execute_move` actualice `pieza_destino` si no es `None`."""
        # Mock de las piezas de origen y destino
        pieza_origen = MagicMock()
        pieza_destino = MagicMock()
        self.__board__.get_piece = MagicMock(side_effect=[pieza_origen, pieza_destino])

        # Ejecutar movimiento
        self.__board__.execute_move((4, 4), (5, 5))

        # Verificar que `pieza_destino.update_position` se llame con `None`
        pieza_destino.update_position.assert_called_once_with(None)

    def test_is_valid_move_destino_piece_is_king(self):
        """Prueba que `is_valid_move` lance `CantEatKingError` si `destino_piece` es un Rey."""
        origen_piece = MagicMock(color="White")
        destino_piece = Rey("Black", (7, 7))

        # Mock de piezas de origen y destino
        self.__board__.get_piece = MagicMock(side_effect=[origen_piece, destino_piece])

        with self.assertRaises(CantEatKingError):
            self.__board__.is_valid_move((6, 6), (7, 7))

    def test_is_valid_move_destino_out_of_bounds(self):
        """Prueba que `is_valid_move` lance `InvalidMoveError` si `destino` está fuera del tablero."""
        origen = (3, 3)
        destino = (8, 8)  # fuera del tablero
        self.__board__.validate_out_of_board = MagicMock(return_value=False)

        with self.assertRaises(InvalidMoveError):
            self.__board__.is_valid_move(origen, destino)

    def test_is_valid_move_origen_out_of_bounds(self):
        """Prueba que `is_valid_move` lance `InvalidMoveError` si `origen` está fuera del tablero."""
        origen = (-1, 0)  # fuera del tablero
        destino = (3, 3)
        self.__board__.validate_out_of_board = MagicMock(side_effect=[False, True])

        with self.assertRaises(InvalidMoveError):
            self.__board__.is_valid_move(origen, destino)

    def test_can_move_invalid_piece_movement(self):
        """Prueba que `can_move` lance `InvalidPieceMovement` si `is_valid_move` es False."""
        origen_piece = MagicMock()
        self.__board__.get_piece = MagicMock(return_value=origen_piece)
        self.__board__.is_valid_move = MagicMock(return_value=False)

        with self.assertRaises(InvalidPieceMovement):
            self.__board__.can_move((2, 2), (3, 3))

    def test_move_destino_out_of_bounds(self):
        """Prueba que `move` lance `InvalidMoveError` si `destino` está fuera del tablero."""
        origen = (2, 2)
        destino = (9, 9)  # fuera del tablero
        self.__board__.validate_out_of_board = MagicMock(side_effect=[True, False])

        with self.assertRaises(InvalidMoveError):
            self.__board__.move(origen, destino)

    def test_move_cant_eat_king_error(self):
        """Prueba que `move` maneje la excepción `CantEatKingError` correctamente."""
        origen = (2, 2)
        destino = (3, 3)
        self.__board__.validate_out_of_board = MagicMock(return_value=True)
        self.__board__.can_move = MagicMock(side_effect=CantEatKingError("No puedes capturar al rey del oponente."))

        with self.assertRaises(CantEatKingError):
            self.__board__.move(origen, destino)

    def test_color_pieces_piece_not_found(self):
        """Prueba que `color_pieces` retorne `PieceNotFoundError` si no hay ninguna pieza en la posición."""
        row, col = 4, 4
        self.__board__.get_piece = MagicMock(return_value=None)  # No hay pieza en la posición

        result = self.__board__.color_pieces(row, col)
        self.assertIsInstance(result, PieceNotFoundError)
        self.assertEqual(str(result), "No hay ninguna pieza en la posición de origen.")

if __name__ == "__main__":
    unittest.main()
   

