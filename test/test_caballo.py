import unittest
from game.caballo import Caballo
from game.piece import Piece 

class TestCaballo(unittest.TestCase):

    def setUp(self):
        # Inicializa un Caballo negro y uno blanco para las pruebas
        self.caballo_negro = Caballo("Black", (0, 1))
        self.caballo_blanco = Caballo("White", (7, 6))
        # Crea un tablero vacío de 8x8
        self.positions = [[None for _ in range(8)] for _ in range(8)]

    def test_assign_value(self):
        # Verifica que el valor asignado al Caballo es 3
        self.assertEqual(self.caballo_negro.assign_value(), 3)
        self.assertEqual(self.caballo_blanco.assign_value(), 3)

    def test_is_valid_move(self):
        # Movimientos válidos en "L" para el Caballo
        self.assertTrue(self.caballo_negro.is_valid_move(2, 1))
        self.assertTrue(self.caballo_negro.is_valid_move(1, 2))

        # Movimientos no válidos
        self.assertFalse(self.caballo_negro.is_valid_move(2, 2))
        self.assertFalse(self.caballo_negro.is_valid_move(3, 1))
        self.assertFalse(self.caballo_negro.is_valid_move(0, 0))

    def test_is_valid_destination(self):
        # Prueba una casilla vacía
        self.assertTrue(self.caballo_negro.is_valid_destination(2, 2, self.positions))

        # Prueba una casilla ocupada por una pieza del mismo color
        self.positions[2][2] = Piece("Black", (2, 2))
        self.assertFalse(self.caballo_negro.is_valid_destination(2, 2, self.positions))

        # Prueba una casilla ocupada por una pieza de diferente color
        self.positions[2][2] = Piece("White", (2, 2))
        self.assertTrue(self.caballo_negro.is_valid_destination(2, 2, self.positions))

    def test_piece_move_valid(self):
        # Prueba un movimiento válido para el Caballo a una casilla vacía
        new_position = (2, 2)
        self.assertTrue(self.caballo_negro.piece_move(self.positions, new_position))

        # Prueba un movimiento válido para el Caballo a una casilla ocupada por una pieza del color contrario
        self.positions[2][2] = Piece("White", (2, 2))
        self.assertTrue(self.caballo_negro.piece_move(self.positions, new_position))

    def test_piece_move_invalid(self):
        # Prueba un movimiento no válido para el Caballo (no en "L")
        new_position = (2, 3)
        self.assertFalse(self.caballo_negro.piece_move(self.positions, new_position))

        # Prueba un movimiento válido pero a una casilla ocupada por una pieza del mismo color
        new_position = (2, 2)
        self.positions[2][2] = Piece("Black", (2, 2))
        self.assertFalse(self.caballo_negro.piece_move(self.positions, new_position))

    def test_str_representation(self):
        # Verifica la representación visual del Caballo
        self.assertEqual(str(self.caballo_negro), "♘")
        self.assertEqual(str(self.caballo_blanco), "♞")


if __name__ == '__main__':
    unittest.main()