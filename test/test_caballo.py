import unittest
from game.caballo import Caballo
class TestCaballo(unittest.TestCase):

    def setUp(self):
        #inicializacion de tablero
        self.__positions__ = [[None] * 8 for _ in range(8)]
        # Creamos caballos blanco y negro antes de cada test
        self.White_knight = Caballo("White", (7, 1))  # Caballo blanco en la fila 7, columna 1 (posición inicial)
        self.Black_knight = Caballo("Black", (0, 1))  # Caballo negro en la fila 0, columna 1 (posición inicial)
        self.__positions__[7][1] = self.White_knight
        self.__positions__[0][1] = self.Black_knight
    def test_assign_value(self):
        # Verifica que el valor del caballo sea 3
        self.assertEqual(self.White_knight.assign_value(), 3)
        self.assertEqual(self.Black_knight.assign_value(), 3)

    def test_str(self):
        # Verifica que el símbolo del caballo se muestre correctamente
        self.assertEqual(str(self.Black_knight), "♘")
        self.assertEqual(str(self.White_knight), "♞")

    def test_is_valid_move(self):
        # Verifica que los movimientos en "L" sean válidos
        self.assertTrue(self.White_knight.piece_move(self.__positions__,(5, 0)))  # Movimiento válido
        self.assertTrue(self.White_knight.piece_move(self.__positions__,(5, 2)))  # Movimiento válido
        #
        self.assertTrue(self.Black_knight.piece_move(self.__positions__,(2, 0)))  # Movimiento 
        self.assertTrue(self.Black_knight.piece_move(self.__positions__,(2, 2)))  # Movimiento 
    
    def test_invalid_move(self):
        # Verifica que los movimientos inválidos no sean permitidos
        self.assertFalse(self.White_knight.piece_move(self.__positions__,(7, 2)))
        self.assertFalse(self.Black_knight.piece_move(self.__positions__,(0, 0)))

if __name__ == '__main__':
    unittest.main()