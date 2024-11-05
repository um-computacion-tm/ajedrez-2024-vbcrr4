import unittest
from game.reina import Reina
from game.piece import Piece 

class TestReina(unittest.TestCase):

    def setUp(self):
        # Inicializa una Reina negra y una blanca para las pruebas
        self.reina_negra = Reina("Black", (0, 3))
        self.reina_blanca = Reina("White", (4, 4))
        # Crea un tablero vacío de 8x8
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]

    def test_piece_move(self):
        # Prueba un movimiento vertical válido (camino despejado)
        self.assertTrue(self.reina_negra.piece_move(self.__positions__, (3, 3)))

        # Prueba un movimiento vertical bloqueado
        self.__positions__[1][3] = Piece("White", (1, 3))
        self.assertFalse(self.reina_negra.piece_move(self.__positions__, (3, 3)))

    #test_piece_move_horizontal(self):
        # Prueba un movimiento horizontal válido (camino despejado)
        self.assertTrue(self.reina_blanca.piece_move(self.__positions__, (4, 6)))

        # Prueba un movimiento horizontal bloqueado
        self.__positions__[0][5] = Piece("White", (0, 5))
        self.assertFalse(self.reina_negra.piece_move(self.__positions__, (0, 7)))

if __name__ == '__main__':
    unittest.main()