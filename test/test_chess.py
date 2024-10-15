import unittest
from game.chess import Game
from game.piece import *
from game.exepciones import *   
from unittest.mock import Mock

class TestGame(unittest.TestCase):

    def setUp(self):
        # Creamos una instancia de Game antes de cada test
        self.game = Game()
        self.game.__board__ = Mock()  # Usamos un mock para el tablero para aislar las pruebas

    def test_get_turn(self):
        # Verifica que el turno inicial es "white"
        self.assertEqual(self.game.get_turn(), "white")

    def test_change_turn(self):
        # Verifica el cambio de turno entre "white" y "black"
        self.assertEqual(self.game.change_turn(), "black")  # Cambia a negro
        self.assertEqual(self.game.get_turn(), "black")
        self.assertEqual(self.game.change_turn(), "white")  # Cambia de vuelta a blanco
        self.assertEqual(self.game.get_turn(), "white")

    def test_validate_move_valid_piece(self):
        # Simulamos un movimiento válido con una pieza del turno correcto
        piece = Mock()  # Mock de una pieza válida
        self.game.__board__.get_piece.return_value = piece
        self.game.__board__.color_pieces.return_value = "white"  # El color de la pieza es "white"
        
        result = self.game.validate_move(0, 0)
        self.assertEqual(result, piece)  # Debe devolver la pieza si todo es correcto

    def test_validate_move_no_piece(self):
        # Simulamos una posición sin pieza, lo que debe lanzar PieceNotFoundError
        self.game.__board__.get_piece.return_value = None
        
        with self.assertRaises(PieceNotFoundError):
            self.game.validate_move(0, 0, from_input=["a", 1])

    def test_validate_move_wrong_color(self):
        # Simulamos un movimiento con una pieza del color incorrecto para el turno
        piece = Mock()
        self.game.__board__.get_piece.return_value = piece
        self.game.__board__.color_pieces.return_value = "black"  # El color de la pieza es "black"
        
        with self.assertRaises(InvalidColorError):
            self.game.validate_move(0, 0)

    def test_print_board(self):
        # Verifica que se llama al método print_board del tablero
        self.game.print_board()
        self.game.__board__.print_board.assert_called_once()

if __name__ == '__main__':
    unittest.main()
