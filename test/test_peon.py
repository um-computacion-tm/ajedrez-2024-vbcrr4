import unittest
from game.peon import Peon
class TestPeon(unittest.TestCase):
    def setUp(self):
        #inicializamos tablero
        self.__positions__ = [[None] * 8 for _ in range(8)]
        # Creamos peones blanco y negro antes de cada test
        self.White_peon = Peon("White", (6, 0))  # Peón blanco en la fila 6 (posición inicial)
        self.White_peon3 = Peon("White", (6, 4))  # Peón blanco en la fila 6 (posición inicial)
        self.White_peon2 = Peon("White", (6, 2))  # Peón blanco en la fila 6 (posición inicial)
        self.Black_peon = Peon("Black", (1, 0))  # Peón negro en la fila 1 (posición inicial)
        self.Black_peon2 = Peon("Black", (1, 2))  # Peón negro en la fila 1 (posición inicial)
        self.__positions__[6][0] = self.White_peon
        self.__positions__[6][2] = self.White_peon2
        self.__positions__[1][0] = self.Black_peon
        self.__positions__[1][2] = self.Black_peon2

    def test_assign_value(self):
        # Verifica que el valor del peón sea 1
        self.assertEqual(self.White_peon.assign_value(), 1)
        self.assertEqual(self.Black_peon.assign_value(), 1)
        self.assertEqual(self.White_peon2.assign_value(), 1)
        self.assertEqual(self.Black_peon2.assign_value(), 1)

    def test_str(self):
        # Verifica que el símbolo del peón se muestre correctamente
        self.assertEqual(str(self.Black_peon), "♙")
        self.assertEqual(str(self.White_peon), "♟")

    def test_ataque_white_peon(self):
        self.__positions__[5][5] = Peon("Black", (5, 5))  # Coloca un peón negro en la posición (5, 5)
        #print("Peón negro en: ", (5, 5))
        #print("Estado del tablero: ", self.__positions__)
        self.assertTrue(self.White_peon3.piece_move(self.__positions__, (5, 5)))  # Captura diagonal

    def test_movimiento_inicial_dos_casillas_blanco(self):
        # Movimiento inicial válido de dos casillas para el peón blanco
        self.assertTrue(self.White_peon.piece_move(self.__positions__, (4, 0)))

    def test_movimiento_inicial_dos_casillas_negro(self):
        # Movimiento inicial válido de dos casillas para el peón negro
        self.assertTrue(self.Black_peon.piece_move(self.__positions__, (3, 0)))


    def test_movimiento_invalido_vertical_obstaculo(self):
        # Intentar mover un peón hacia adelante cuando hay una pieza en el camino
        self.__positions__[5][0] = Peon("White", (5, 0))  # Obstáculo delante del peón blanco
        self.assertFalse(self.White_peon.piece_move(self.__positions__, (5, 0)))

    def test_movimiento_invalido_horizontal(self):
        # Intentar mover el peón horizontalmente (lo cual no es permitido)
        self.assertFalse(self.White_peon.piece_move(self.__positions__, (6, 1)))

    def test_captura_diagonal_blanco(self):
        # Colocamos un peón negro en una posición que el peón blanco puede capturar
        self.__positions__[5][1] = Peon("Black", (5, 1))
        self.assertTrue(self.White_peon.piece_move(self.__positions__, (5, 1)))

    def test_captura_diagonal_negro(self):
        # Colocamos un peón blanco en una posición que el peón negro puede capturar
        self.__positions__[2][1] = Peon("White", (2, 1))
        self.assertTrue(self.Black_peon.piece_move(self.__positions__, (2, 1)))

    def test_movimiento_vertical_simple_blanco(self):
        # Movimiento válido de una casilla hacia adelante para el peón blanco
        self.assertTrue(self.White_peon.piece_move(self.__positions__, (5, 0)))

    def test_movimiento_vertical_simple_negro(self):
        # Movimiento válido de una casilla hacia adelante para el peón negro
        self.assertTrue(self.Black_peon.piece_move(self.__positions__, (2, 0)))

    def test_movimiento_invalido_fuera_de_limites(self):
        # Intentar mover el peón fuera del tablero
        self.assertFalse(self.White_peon.piece_move(self.__positions__, (8, 0)))
        self.assertFalse(self.Black_peon.piece_move(self.__positions__, (-1, 0)))

    def test_movimiento_invalido_sin_captura_diagonal(self):
        # Intentar mover diagonalmente sin que haya una pieza enemiga para capturar
        self.assertFalse(self.White_peon.piece_move(self.__positions__, (5, 1)))

    def test_captura_invalida_vertical(self):
        # Intentar capturar en movimiento vertical (lo cual no es permitido)
        self.__positions__[5][0] = Peon("Black", (5, 0))  # Peón enemigo justo en frente
        self.assertFalse(self.White_peon.piece_move(self.__positions__, (5, 0)))

    def test_piece_move_invalid_color(self):
        """Prueba que `piece_move` devuelva False si el color del peón es inválido."""
        # Creamos un peón con un color inválido
        invalid_peon = Peon("Green", (6, 0))  
        self.assertFalse(invalid_peon.piece_move(self.__positions__, (5, 0)))

    def test_move_invalid_no_forward(self):
        """Prueba que `move` devuelva False si el peón no avanza correctamente."""
        white_peon = Peon("White", (6, 0))
        black_peon = Peon("Black", (1, 0))
        
        # Colocamos los peones en el tablero
        self.__positions__[6][0] = white_peon
        self.__positions__[1][0] = black_peon

        # Prueba de movimiento inválido hacia una posición no permitida
        self.assertFalse(white_peon.move(self.__positions__, (7, 0), -1))  # Movimiento hacia atrás
        self.assertFalse(black_peon.move(self.__positions__, (0, 0), 1))   # Movimiento hacia fuera del tablero

    def test_move_invalid_destination_occupied(self):
        """Prueba que `move` devuelva False si la posición de destino está ocupada."""
        white_peon = Peon("White", (6, 0))
        blocking_piece = Peon("Black", (5, 0))

        # Colocamos el peón blanco y una pieza bloqueadora en el tablero
        self.__positions__[6][0] = white_peon
        self.__positions__[5][0] = blocking_piece

        # Intento de mover el peón blanco adelante, lo cual debería fallar por estar ocupado
        self.assertFalse(white_peon.move(self.__positions__, (5, 0), -1))

if __name__ == '__main__':
    unittest.main()