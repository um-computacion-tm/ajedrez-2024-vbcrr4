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
        self.piece = Piece("White", (0, 0))

    def test_get_color(self):
        # Verifica que el color de la pieza se obtiene correctamente
        self.assertEqual(self.piece.color, "White")

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
        self.piece.__w_str__ = "♚"  # Rey blanco
        self.piece.__b_str__ = "♔"  # Rey negro
        
        self.assertEqual(str(self.piece), "♚")  # Para una pieza blanca

        self.piece = Piece("Black", (7, 7))  # Para una pieza negra
        self.piece.__w_str__ = "♚"  # Rey blanco
        self.piece.__b_str__ = "♔"  # Rey negro
        self.assertEqual(str(self.piece), "♔")

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

    def test_diagonal_move_positions(self):
        # Prueba un movimiento diagonal válido
        positions = [[None for _ in range(8)] for _ in range(8)]
        self.piece.update_position((0, 0))
        self.assertTrue(self.piece.diagonal_move_positions( positions, (3, 3)))

        # Prueba un movimiento diagonal inválido (camino bloqueado)
        positions[1][1] = Piece("White", (1, 1))  # Colocamos una pieza en el camino
        self.assertFalse(self.piece.diagonal_move_positions(positions, (3, 3)))

        # Prueba un movimiento no diagonal (debe devolver False)
        self.assertFalse(self.piece.diagonal_move_positions( positions, (2, 3)))

    def test_vertical_move_positions(self):
        # Prueba un movimiento vertical válido
        positions = [[None for _ in range(8)] for _ in range(8)]
        self.piece.update_position((0, 0))
        self.assertTrue(self.piece.vertical_move_positions( positions, (3, 0)))

        # Prueba un movimiento vertical inválido (camino bloqueado)
        positions[1][0] = Piece("White", (1, 0))  # Colocamos una pieza en el camino
        self.assertFalse(self.piece.vertical_move_positions( positions, (3, 0)))

        # Prueba un movimiento no vertical (debe devolver False)
        self.assertFalse(self.piece.vertical_move_positions(positions, (3, 1)))

    def test_horizontal_move_positions(self):
        # Prueba un movimiento horizontal válido
        positions = [[None for _ in range(8)] for _ in range(8)]
        self.piece.update_position((0, 0))
        self.assertTrue(self.piece.horizontal_move_positions(positions, (0, 3)))

        # Prueba un movimiento horizontal inválido (camino bloqueado)
        positions[0][1] = Piece("White", (0, 1))  # Colocamos una pieza en el camino
        self.assertFalse(self.piece.horizontal_move_positions( positions, (0, 3)))

        # Prueba un movimiento no horizontal (debe devolver False)
        self.assertFalse(self.piece.horizontal_move_positions(positions, (1, 3)))

class TestTorre(unittest.TestCase):
    def setUp(self):
        #inicializacion de tablero
        self.__positions__ = [[None] * 8 for _ in range(8)]
        #
        self.torre_White = Torre('White',(1, 1))
        self.torre_Black = Torre('Black', (2, 2))
        self.__positions__[1][1] = self.torre_White
        self.__positions__[2][2] = self.torre_Black

    def test_assign_value(self):
        # Test the assign_value method
        self.assertEqual(self.torre_White.assign_value(), 5)
        self.assertEqual(self.torre_Black.assign_value(), 5)

    def test_valid_white_move(self):
        # Test a valid move for the white tower
        self.assertTrue(self.torre_White.torre_move(self.__positions__,(1, 5)))
        self.assertTrue(self.torre_White.torre_move(self.__positions__,(5, 1)))

    def test_valid_balck_move(self):
        # Test a valid move for the black tower
        self.assertTrue(self.torre_Black.torre_move(self.__positions__,(2, 5)))
        self.assertTrue(self.torre_Black.torre_move(self.__positions__,(5, 2)))
    
    def test_torre_blocked_move(self):
        # Test a move that is blocked by another
        self.__positions__[1][3] = Torre('White', (1, 3))
        self.assertFalse(self.torre_White.torre_move(self.__positions__,(1, 5)))

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
        self.assertTrue(self.White_king.move_king(self.__positions__,(6, 4)))  # Movimiento hacia abajo
        self.assertTrue(self.White_king.move_king(self.__positions__,(6, 5)))  # Movimiento en diagonal
        self.assertTrue(self.White_king.move_king(self.__positions__,(7, 5)))  # Movimiento lateral

    def test_king_black_move_valid(self):
        # Verifica que los movimientos válidos del rey sean permitidos
        self.assertTrue(self.Black_king.move_king(self.__positions__,(0, 3)))  # Movimiento hacia arriba
        self.assertTrue(self.Black_king.move_king(self.__positions__,(0, 5)))  # Movimiento en diagonal

    def test_king_invalid(self):
        # Verifica que los movimientos inválidos del rey no sean permitido
        self.assertFalse(self.White_king.move_king(self.__positions__,(5, 4)))  # Movimiento de 2 casillas hacia abajo
        self.assertFalse(self.White_king.move_king(self.__positions__,(7, 6)))  # Movimiento de 2 casillas hacia la derecha 


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
        self.assertTrue(self.__White_alfil__.alfil_move(self.__positions__,(5, 0) ))  # Movimiento diagonal válido
        self.assertTrue(self.__White_alfil__.alfil_move(self.__positions__,(4, 5) ))  # Otro movimiento diagonal válido

    def test_alfil_black_move_valid(self):
        # Prueba movimientos válidos en diagonal
        self.assertTrue(self.__Black_alfil__.alfil_move(self.__positions__,(3, 5) ))  # Movimiento diagonal válido
        self.assertTrue(self.__Black_alfil__.alfil_move(self.__positions__,(2, 0) ))  # Movimiento diagonal válido 

    def test_alfil_white_move_invalid(self):
        # Prueba movimientos inválidos (no diagonales) para el alfil
        self.assertFalse(self.__White_alfil__.alfil_move(self.__positions__,(7, 3)))
        self.assertFalse(self.__White_alfil__.alfil_move(self.__positions__,(5, 2)))
    
    def test_alfil_black_move_invalid(self):
        # Prueba movimientos inválidos (no diagonales) para el alfil
        self.assertFalse(self.__Black_alfil__.alfil_move(self.__positions__,(0, 3)))
        self.assertFalse(self.__Black_alfil__.alfil_move(self.__positions__,(2, 2)))

    def test_alfil_move_blocked_by_same_color(self):
        # Verifica que el alfil no pueda moverse a una casilla ocupada por una pieza del mismo color
        self.__positions__[5][0] = Alfil("White", (5, 0))  # Colocamos un alfil blanco en la diagonal
        self.assertFalse(self.__White_alfil__.alfil_move(self.__positions__,(5, 0)))  # Movimiento inválido, casilla ocupada

        
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
        self.assertTrue(self.reina_White.reina_move(self.__positions__,(2, 6)))
        self.assertTrue(self.reina_White.reina_move(self.__positions__,(0, 0)))
        self.assertTrue(self.reina_White.reina_move(self.__positions__,(1, 3)))
        self.assertTrue(self.reina_White.reina_move(self.__positions__,(1, 4)))

    def test_valid_black_move(self):
        # Test a valid move for the black queen
        self.assertTrue(self.reina_Black.reina_move(self.__positions__,(6, 3)))
        self.assertTrue(self.reina_Black.reina_move(self.__positions__,(6, 5)))
        self.assertTrue(self.reina_Black.reina_move(self.__positions__,(7, 0)))
        self.assertTrue(self.reina_Black.reina_move(self.__positions__,(0, 4)))

    def test_invalid_move(self):
        self.assertFalse(self.reina_White.reina_move(self.__positions__,(5, 6)))
        self.assertFalse(self.reina_Black.reina_move(self.__positions__,(6, 6)))
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
        self.assertTrue(self.White_knight.move_caballo(self.__positions__,(5, 0)))  # Movimiento válido
        self.assertTrue(self.White_knight.move_caballo(self.__positions__,(5, 2)))  # Movimiento válido
        #
        self.assertTrue(self.Black_knight.move_caballo(self.__positions__,(2, 0)))  # Movimiento 
        self.assertTrue(self.Black_knight.move_caballo(self.__positions__,(2, 2)))  # Movimiento 
    
    def test_invalid_move(self):
        # Verifica que los movimientos inválidos no sean permitidos
        self.assertFalse(self.White_knight.move_caballo(self.__positions__,(7, 2)))
        self.assertFalse(self.Black_knight.move_caballo(self.__positions__,(0, 0)))

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

    def test_valid_White_move_initial(self):
        self.assertFalse(self.White_peon.validate_movimiento(self.__positions__, (5, 0)))  # Mover una fila hacia adelante
        self.assertFalse(self.White_peon2.validate_movimiento(self.__positions__, (4, 0)))  # Mover dos filas hacia adelante

    def test_valid_Black_move_initial(self):
        self.assertFalse(self.Black_peon.validate_movimiento(self.__positions__, (2, 0)))  # Mover una fila hacia adelante
        self.assertFalse(self.Black_peon2.validate_movimiento(self.__positions__, (3, 0)))  # Mover dos filas hacia adelante

    def test_ataque_white_peon(self):
        self.__positions__[5][5] = Peon("Black", (5, 5))  # Coloca un peón negro en la posición (5, 5)
        #print("Peón negro en: ", (5, 5))
        #print("Estado del tablero: ", self.__positions__)
        self.assertTrue(self.White_peon3.validate_movimiento(self.__positions__, (5, 5)))  # Captura diagonal
    
    """def test_invalid_color_peon(self):
        peon_invalid = Peon(None, (6, 0))  # Color inválido
        self.assertFalse(peon_invalid.validate_movimiento(self.__positions__, (5, 0)))

    def test_white_peon_double_step(self):
        self.assertTrue(self.White_peon.validate_movimiento(self.__positions__, (4, 0)))  # Movimiento de dos casillas
    
    def test_white_peon_single_step_after_move(self):
        self.White_peon.update_position((5, 0))  # Mover a la fila 5
        self.assertTrue(self.White_peon.validate_movimiento(self.__positions__, (4, 0)))  # Una casilla hacia adelante

    def test_white_peon_single_step(self):
        self.assertTrue(self.White_peon.validate_movimiento(self.__positions__, (5, 0)))  # Movimiento de una casilla hacia adelante
        """


if __name__ == '__main__':
    unittest.main()
