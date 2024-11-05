import unittest
from unittest.mock import Mock, patch
from game.piece import Piece
from game.torre import Torre
from game.rey import Rey
from game.alfil import Alfil
from game.peon import Peon
from game.caballo import Caballo
from game.reina import Reina
#agreagrar las exepciones


class TestPiece(unittest.TestCase):

    def setUp(self):
        # Creamos una instancia de Piece antes de cada test
        self.piece = Piece("Black", (0, 0))
        self.piece2 = Piece("White", (7, 7))

    def test_get_color(self):
        # Verifica que el color de la pieza se obtiene correctamente
        self.assertEqual(self.piece.color, "Black")

    def test_get_position(self):
        # Verifica que la posición inicial de la pieza se obtiene correctamente
        self.assertEqual(self.piece.position, (0, 0))

    def test_update_position(self):
        # Verifica que la posición de la pieza se actualiza correctamente
        new_position = (2, 3)
        self.piece.update_position(new_position)
        self.assertEqual(self.piece.position, new_position)

    def test_str(self):
        # Probar la conversión a string de la pieza según su color
        # Esto requiere que la clase tenga `__w_str__` y `__b_str__` definidos
        self.piece.__w_str__ = "♜"
        self.piece.__b_str__ = "♖"
        
        self.assertEqual(str(self.piece), "♖")  

        self.piece = Piece("White", (7, 7))  # Para una pieza negra
        self.piece.__w_str__ = "♜"
        self.piece.__b_str__ = "♖"
        self.assertEqual(str(self.piece), "♜")

    def test_is_path_clear(self):
        # Prueba que el camino esté despejado
        positions = [[None for _ in range(8)] for _ in range(8)]
        start = (0, 0)
        end = (3, 3)
        row_step = 1
        col_step = 1
        self.assertTrue(self.piece.is_path_clear((start, end), positions, row_step, col_step))

        # Prueba cuando el camino está bloqueado
        positions[1][1] = Piece("White", (1, 1))  # Colocamos una pieza en el camino
        self.assertFalse(self.piece.is_path_clear((start, end), positions, row_step, col_step))
    
    def create_empty_board(self):
        """Crea un tablero vacío de 8x8."""
        return [[None for _ in range(8)] for _ in range(8)]

    def prepare_test(self, start_pos):
        """Configura el tablero vacío y actualiza la posición de la pieza."""
        positions = self.create_empty_board()
        self.piece.update_position(start_pos)
        return positions

    def test_diagonal_move_positions2(self):
        positions = self.prepare_test((0, 0))
        
        # Prueba un movimiento diagonal válido
        self.assertTrue(self.piece.diagonal_move_positions(positions, (3, 3)))

        # Prueba un movimiento diagonal inválido (camino bloqueado)
        positions[1][1] = Piece("White", (1, 1))  # Colocamos una pieza en el camino
        self.assertFalse(self.piece.diagonal_move_positions(positions, (3, 3)))

        # Prueba un movimiento no diagonal
        self.assertFalse(self.piece.diagonal_move_positions(positions, (2, 3)))

    def test_vertical_move_positions2(self):
        positions = self.prepare_test((0, 0))
        
        # Prueba un movimiento vertical válido
        self.assertTrue(self.piece.vertical_move_positions(positions, (3, 0)))

        # Prueba un movimiento vertical inválido (camino bloqueado)
        positions[1][0] = Piece("White", (1, 0))  # Colocamos una pieza en el camino
        self.assertFalse(self.piece.vertical_move_positions(positions, (3, 0)))

        # Prueba un movimiento no vertical
        self.assertFalse(self.piece.vertical_move_positions(positions, (3, 1)))

    def test_horizontal_move_positions2(self):
        positions = self.prepare_test((0, 0))
        
        # Prueba un movimiento horizontal válido
        self.assertTrue(self.piece.horizontal_move_positions(positions, (0, 3)))

        # Prueba un movimiento horizontal inválido (camino bloqueado)
        positions[0][1] = Piece("White", (0, 1))  # Colocamos una pieza en el camino
        self.assertFalse(self.piece.horizontal_move_positions(positions, (0, 3)))

        # Prueba un movimiento no horizontal
        self.assertFalse(self.piece.horizontal_move_positions(positions, (1, 3)))

class TestTorre(unittest.TestCase):
    def setUp(self):
        #inicializacion de tablero
        self.__positions__ = [[None] * 8 for _ in range(8)]
        #
        self.torre_White = Torre('White',(1, 1))
        self.__positions__[1][1] = self.torre_White

    def test_assign_value(self):
        # Test the assign_value method
        self.assertEqual(self.torre_White.assign_value(), 5)

    def test_valid_white_move(self):
        # Test a valid move for the white tower
        self.assertTrue(self.torre_White.piece_move(self.__positions__,(1, 5)))
        self.assertTrue(self.torre_White.piece_move(self.__positions__,(5, 1)))
    
    def test_torre_blocked_move(self):
        # Test a move that is blocked by another
        self.__positions__[1][3] = Torre('White', (1, 3))
        self.assertFalse(self.torre_White.piece_move(self.__positions__,(1, 5)))

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


class TestAlfil(unittest.TestCase):

    def setUp(self):
        #iniiclizacion de tablero
        self.__positions__ = [[None] * 8 for _ in range(8)]
        # Creamos alfiles blanco y negro antes de cada test
        self.__White_alfil__ = Alfil("White", (7, 2))  # Alfil blanco en la posición inicial
        self.__Black_alfil__ = Alfil("Black", (0, 2))  # Alfil negro en la posición inicial
        self.__positions__[7][2] = self.__White_alfil__
        self.__positions__[0][2] = self.__Black_alfil__

    def test_assign_value(self):
        # Verifica que el valor del alfil sea 3
        self.assertEqual(self.__White_alfil__.assign_value(), 3)
        self.assertEqual(self.__Black_alfil__.assign_value(), 3)

    def test_str(self):
        # Verifica que el símbolo del alfil se muestre correctamente
        self.assertEqual(str(self.__Black_alfil__), "♗")
        self.assertEqual(str(self.__White_alfil__), "♝")

    def test_alfil_white_move_valid(self):
        # Prueba movimientos válidos en diagonal
        self.assertTrue(self.__White_alfil__.piece_move(self.__positions__,(5, 0) ))  # Movimiento diagonal válido
        self.assertTrue(self.__White_alfil__.piece_move(self.__positions__,(4, 5) ))  # Otro movimiento diagonal válido

    def test_alfil_black_move_valid(self):
        # Prueba movimientos válidos en diagonal
        self.assertTrue(self.__Black_alfil__.piece_move(self.__positions__,(3, 5) ))  # Movimiento diagonal válido
        self.assertTrue(self.__Black_alfil__.piece_move(self.__positions__,(2, 0) ))  # Movimiento diagonal válido 

    def test_alfil_white_move_invalid(self):
        # Prueba movimientos inválidos (no diagonales) para el alfil
        self.assertFalse(self.__White_alfil__.piece_move(self.__positions__,(7, 3)))
        self.assertFalse(self.__White_alfil__.piece_move(self.__positions__,(5, 2)))
    
    def test_alfil_black_move_invalid(self):
        # Prueba movimientos inválidos (no diagonales) para el alfil
        self.assertFalse(self.__Black_alfil__.piece_move(self.__positions__,(0, 3)))
        self.assertFalse(self.__Black_alfil__.piece_move(self.__positions__,(2, 2)))

    def test_piece_move_blocked_by_same_color(self):
        # Verifica que el alfil no pueda moverse a una casilla ocupada por una pieza del mismo color
        self.__positions__[5][0] = Alfil("White", (5, 0))  # Colocamos un alfil blanco en la diagonal
        self.assertFalse(self.__White_alfil__.piece_move(self.__positions__,(5, 0)))  # Movimiento inválido, casilla ocupada

        
class TestReina(unittest.TestCase):
    def setUp(self):
        #inicializacion de tablero
        self.__positions__ = [[None] * 8 for _ in range(8)]
        self.reina_White = Reina('White',(0,4))
        self.reina_Black = Reina('Black', (7, 4))
        self.__positions__[0][4] = self.reina_White
        self.__positions__[7][4] = self.reina_Black

    def test_assign_value(self):
        # Test the assign_value method
        self.assertEqual(self.reina_White.assign_value(), 9)
        self.assertEqual(self.reina_Black.assign_value(), 9)

    def test_valid_white_move(self):
        # Test a valid move for the white queen
        self.assertTrue(self.reina_White.piece_move(self.__positions__,(2, 6)))
        self.assertTrue(self.reina_White.piece_move(self.__positions__,(0, 0)))
        self.assertTrue(self.reina_White.piece_move(self.__positions__,(1, 3)))
        self.assertTrue(self.reina_White.piece_move(self.__positions__,(1, 4)))

    def test_valid_black_move(self):
        # Test a valid move for the black queen
        self.assertTrue(self.reina_Black.piece_move(self.__positions__,(6, 3)))
        self.assertTrue(self.reina_Black.piece_move(self.__positions__,(6, 5)))
        self.assertTrue(self.reina_Black.piece_move(self.__positions__,(7, 0)))
        self.assertTrue(self.reina_Black.piece_move(self.__positions__,(0, 4)))

    def test_invalid_move(self):
        self.assertFalse(self.reina_White.piece_move(self.__positions__,(5, 6)))
        self.assertFalse(self.reina_Black.piece_move(self.__positions__,(6, 6)))
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
