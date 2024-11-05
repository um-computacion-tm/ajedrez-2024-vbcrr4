import unittest
from game.reina import Reina
from game.piece import Piece 

class TestReina(unittest.TestCase):

    def setUp(self):
        # Inicializa una Reina negra y una blanca para las pruebas
        self.reina_negra = Reina("Black", (0, 3))
        self.reina_blanca = Reina("White", (7, 3))
        # Crea un tablero vacío de 8x8
        self.positions = [[None for _ in range(8)] for _ in range(8)]

    def test_assign_value(self):
        # Verifica que el valor asignado a la Reina es 9
        self.assertEqual(self.reina_negra.assign_value(), 9)
        self.assertEqual(self.reina_blanca.assign_value(), 9)

    def test_piece_move_vertical(self):
        # Prueba un movimiento vertical válido (camino despejado)
        self.assertTrue(self.reina_negra.piece_move(self.positions, (3, 3)))

        # Prueba un movimiento vertical bloqueado
        self.positions[1][3] = Piece("White", (1, 3))
        self.assertFalse(self.reina_negra.piece_move(self.positions, (3, 3)))

    def test_piece_move_horizontal(self):
        # Prueba un movimiento horizontal válido (camino despejado)
        self.assertTrue(self.reina_negra.piece_move(self.positions, (0, 7)))

        # Prueba un movimiento horizontal bloqueado
        self.positions[0][5] = Piece("White", (0, 5))
        self.assertFalse(self.reina_negra.piece_move(self.positions, (0, 7)))

    def test_str_representation(self):
        # Verifica la representación visual de la Reina
        self.assertEqual(str(self.reina_negra), "♕")
        self.assertEqual(str(self.reina_blanca), "♛")

if __name__ == '__main__':
    unittest.main()