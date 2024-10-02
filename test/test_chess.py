import unittest
from game.chess import Game
from game.board import Board

class TestChess(unittest.TestCase):

    def setUp(self):
        # Creamos una instancia de Game antes de cada test
        self.game = Game()

    def test_initial_game_state(self):
        # Verifica el estado inicial del juego
        self.assertIsInstance(self.game.set_board, Board)
        self.assertEqual(self.game.get_turn(), "white")

    def test_change_turn(self):
        # Verifica que el turno cambie correctamente
        self.assertEqual(self.game.get_turn(), "white")  # Turno inicial
        self.game.change_turn()
        self.assertEqual(self.game.get_turn(), "black")
        self.game.change_turn()
        self.assertEqual(self.game.get_turn(), "white")

    def test_inittial_game(self):
        # Verifica que el juego se inicialice correctamente
        self.game.change_turn()  # Cambiamos el turno para probar la reinicialización
        self.game.inittial_game()  # Reinicia el juego
        self.assertEqual(self.game.get_turn(), "white")  # Debe reiniciarse a "white"
        self.assertIsInstance(self.game.set_board, Board)

    def test_end_game(self):
        # Verifica que el juego termine correctamente
        self.game.end_game()
        self.assertIsNone(self.game.set_board)
        self.assertIsNone(self.game.get_turn())

    def test_get_piece(self):
        # Verifica que se pueda obtener una pieza del tablero
        piece = self.game.get_piece(0, 0)
        self.assertIsNotNone(piece)  # Debería haber una pieza en (0, 0)
        self.assertEqual(piece.color, "White")  # Suponiendo que es una pieza blanca

        # Verificar que no haya pieza en una casilla vacía
        empty_piece = self.game.get_piece(3, 3)
        self.assertIsNone(empty_piece)  # No debería haber una pieza en (3, 3)

if __name__ == '__main__':
    unittest.main()
