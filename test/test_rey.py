import unittest
from game.rey import Rey
class TestRey(unittest.TestCase):

    def setUp(self):
        #inicializacion de tablero
        self.__positions__ = [[None] * 8 for _ in range(8)]
        # Creamos reyes blanco y negro antes de cada test
        self.White_king = Rey("White", (7, 4))  # Rey blanco en la posición inicial
        self.Black_king = Rey("Black", (0, 4))  # Rey negro en la posición inicial
        self.__positions__[7][4] = self.White_king
        self.__positions__[0][4] = self.Black_king

    def test_assign_value(self):
        # Verifica que el valor del rey sea 1000
        self.assertEqual(self.White_king.assign_value(), 1000)
        self.assertEqual(self.Black_king.assign_value(), 1000)

    def test_str(self):
        # Verifica que el símbolo del rey se muestre correctamente
        self.assertEqual(str(self.White_king), "♚")
        self.assertEqual(str(self.Black_king), "♔")

    def test_king_white_move_valid(self):
        # Verifica que los movimientos válidos del rey sean permitidos
        self.assertTrue(self.White_king.piece_move(self.__positions__,(6, 4)))  # Movimiento hacia abajo
        self.assertTrue(self.White_king.piece_move(self.__positions__,(6, 5)))  # Movimiento en diagonal
        self.assertTrue(self.White_king.piece_move(self.__positions__,(7, 5)))  # Movimiento lateral

    def test_king_black_move_valid(self):
        # Verifica que los movimientos válidos del rey sean permitidos
        self.assertTrue(self.Black_king.piece_move(self.__positions__,(0, 3)))  # Movimiento hacia arriba
        self.assertTrue(self.Black_king.piece_move(self.__positions__,(0, 5)))  # Movimiento en diagonal

    def test_king_invalid(self):
        # Verifica que los movimientos inválidos del rey no sean permitido
        self.assertFalse(self.White_king.piece_move(self.__positions__,(5, 4)))  # Movimiento de 2 casillas hacia abajo
        self.assertFalse(self.White_king.piece_move(self.__positions__,(7, 6)))  # Movimiento de 2 casillas hacia la derecha 

if __name__ == '__main__':
    unittest.main()