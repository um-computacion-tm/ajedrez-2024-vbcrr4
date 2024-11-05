import unittest
from game.caballo import Caballo
from game.piece import Piece 

class TestCaballo(unittest.TestCase):

    def setUp(self):
    
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        self.caballo_negro = Caballo("Black", (0, 1))
        self.caballo_blanco = Caballo("White", (7, 6))
        self.__positions__[0][1] = self.caballo_negro
        self.__positions__[7][6] = self.caballo_blanco

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
        self.assertTrue(self.caballo_negro.is_valid_destination(2, 2, self.__positions__))

        # Prueba una casilla ocupada por una pieza del mismo color
        self.__positions__[2][2] = Piece("Black", (2, 2))
        self.assertFalse(self.caballo_negro.is_valid_destination(2, 2, self.__positions__))

        # Prueba una casilla ocupada por una pieza de diferente color
        self.__positions__[2][2] = Piece("White", (2, 2))
        self.assertTrue(self.caballo_negro.is_valid_destination(2, 2, self.__positions__))

    def test_piece_move_valid(self):
        # Prueba un movimiento válido para el Caballo a una casilla vacía
        new_position = (2, 2)
        self.assertTrue(self.caballo_negro.piece_move(self.__positions__, new_position))

        # Prueba un movimiento válido para el Caballo a una casilla ocupada por una pieza del color contrario
        self.__positions__[2][2] = Piece("White", (2, 2))
        self.assertTrue(self.caballo_negro.piece_move(self.__positions__, new_position))

    def test_piece_move_invalid(self):
        # Prueba un movimiento no válido para el Caballo (no en "L")
        new_position = (2, 3)
        self.assertFalse(self.caballo_negro.piece_move(self.__positions__, new_position))

        # Prueba un movimiento válido pero a una casilla ocupada por una pieza del mismo color
        new_position = (2, 2)
        self.__positions__[2][2] = Piece("Black", (2, 2))
        self.assertFalse(self.caballo_negro.piece_move(self.__positions__, new_position))


if __name__ == '__main__':
    unittest.main()