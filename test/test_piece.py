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
        self.piece = Piece("white", (0, 0))

    def test_get_color(self):
        # Verifica que el color de la pieza se obtiene correctamente
        self.assertEqual(self.piece.color, "white")

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
        self.piece.__w_str__ = "♔"  # Rey blanco
        self.piece.__b_str__ = "♚"  # Rey negro
        
        self.assertEqual(str(self.piece), "♔")  # Para una pieza blanca

        self.piece = Piece("black", (7, 7))  # Para una pieza negra
        self.piece.__w_str__ = "♔"
        self.piece.__b_str__ = "♚"
        self.assertEqual(str(self.piece), "♚")

    def test_is_path_clear(self):
        # Prueba que el camino esté despejado
        positions = [[None for _ in range(8)] for _ in range(8)]
        start = (0, 0)
        end = (3, 3)
        row_step = 1
        col_step = 1
        self.assertTrue(self.piece.is_path_clear((start, end), positions, row_step, col_step))

        # Prueba cuando el camino está bloqueado
        positions[1][1] = Piece("white", (1, 1))  # Colocamos una pieza en el camino
        self.assertFalse(self.piece.is_path_clear((start, end), positions, row_step, col_step))

    def test_diagonal_move_positions(self):
        # Prueba un movimiento diagonal válido
        positions = [[None for _ in range(8)] for _ in range(8)]
        self.piece.update_position((0, 0))
        self.assertTrue(self.piece.diagonal_move_positions((3, 3), positions))

        # Prueba un movimiento diagonal inválido (camino bloqueado)
        positions[1][1] = Piece("white", (1, 1))  # Colocamos una pieza en el camino
        self.assertFalse(self.piece.diagonal_move_positions((3, 3), positions))

        # Prueba un movimiento no diagonal (debe devolver False)
        self.assertFalse(self.piece.diagonal_move_positions((2, 3), positions))

    def test_vertical_move_positions(self):
        # Prueba un movimiento vertical válido
        positions = [[None for _ in range(8)] for _ in range(8)]
        self.piece.update_position((0, 0))
        self.assertTrue(self.piece.vertical_move_positions((3, 0), positions))

        # Prueba un movimiento vertical inválido (camino bloqueado)
        positions[1][0] = Piece("white", (1, 0))  # Colocamos una pieza en el camino
        self.assertFalse(self.piece.vertical_move_positions((3, 0), positions))

        # Prueba un movimiento no vertical (debe devolver False)
        self.assertFalse(self.piece.vertical_move_positions((3, 1), positions))

    def test_horizontal_move_positions(self):
        # Prueba un movimiento horizontal válido
        positions = [[None for _ in range(8)] for _ in range(8)]
        self.piece.update_position((0, 0))
        self.assertTrue(self.piece.horizontal_move_positions((0, 3), positions))

        # Prueba un movimiento horizontal inválido (camino bloqueado)
        positions[0][1] = Piece("white", (0, 1))  # Colocamos una pieza en el camino
        self.assertFalse(self.piece.horizontal_move_positions((0, 3), positions))

        # Prueba un movimiento no horizontal (debe devolver False)
        self.assertFalse(self.piece.horizontal_move_positions((1, 3), positions))

class TestTorre(unittest.TestCase):
    def setUp(self):
        self.torre_white = Torre('white',(1, 1))
        self.torre_black = Torre('black', (2, 2))

    def test_initialization(self):
        # Test initialization and inherited properties
        self.assertEqual(self.torre_white.color, "white")
        self.assertEqual(self.torre_white.position, (1, 1))
        self.assertEqual(self.torre_black.color, "black")
        self.assertEqual(self.torre_black.position, (2, 2))

    def test_assign_value(self):
        # Test the assign_value method
        self.assertEqual(self.torre_white.assign_value(), 5)
        self.assertEqual(self.torre_black.assign_value(), 5)


class TestRey(unittest.TestCase):

    def setUp(self):
        self.rey_white = Rey('white',(0,3))
        self.rey_black = Rey('black', (7, 3))

    def test_initialization(self):
        # Test initialization and inherited properties
        self.assertEqual(self.rey_white.color, "white")
        self.assertEqual(self.rey_white.position, (0,3))
        self.assertEqual(self.rey_black.color, "black")
        self.assertEqual(self.rey_black.position, (7, 3))
    
    def test_assign_value(self):
        # Test the assign_value method
        self.assertEqual(self.rey_white.assign_value(), 1000)
        self.assertEqual(self.rey_black.assign_value(), 1000)


class TestAlfil(unittest.TestCase):

    def setUp(self):
        self.alfil_white1 = Alfil('white',(0,2))
        self.alfil_white2 = Alfil('white',(0,5))
        self.alfil_black1 = Alfil('black', (7, 2))
        self.alfil_black2 = Alfil('black', (7, 5))

    def test_initialization(self):
        # Test initialization and inherited properties
        self.assertEqual(self.alfil_white1.color, "white")
        self.assertEqual(self.alfil_white1.position, (0,2))
        self.assertEqual(self.alfil_white2.color, "white")
        self.assertEqual(self.alfil_white2.position, (0,5))
        self.assertEqual(self.alfil_black1.color, "black")
        self.assertEqual(self.alfil_black1.position, (7, 2))
        self.assertEqual(self.alfil_black2.color, "black")
        self.assertEqual(self.alfil_black2.position, (7, 5))
    
    def test_assign_value(self):
        # Test the assign_value method
        self.assertEqual(self.alfil_white1.assign_value(), 3)
        self.assertEqual(self.alfil_white2.assign_value(), 3)
        self.assertEqual(self.alfil_black1.assign_value(), 3)
        self.assertEqual(self.alfil_black2.assign_value(), 3)
        
class TestReina(unittest.TestCase):
    def setUp(self):
        self.reina_white = Reina('white',(0,4))
        self.reina_black = Reina('black', (7, 4))

    def test_initialization(self):
        # Test initialization and inherited properties
        self.assertEqual(self.reina_white.color, "white")
        self.assertEqual(self.reina_white.position, (0,4))
        self.assertEqual(self.reina_black.color, "black")
        self.assertEqual(self.reina_black.position, (7, 4))
    
    def test_assign_value(self):
        # Test the assign_value method
        self.assertEqual(self.reina_white.assign_value(), 9)
        self.assertEqual(self.reina_black.assign_value(), 9)

class TestCaballo(unittest.TestCase):
    
    def setUp(self):
        # Creamos caballos blanco y negro antes de cada test
        self.white_knight = Caballo("white", (7, 1))  # Caballo blanco en la fila 7, columna 1 (posición inicial)
        self.black_knight = Caballo("black", (0, 1))  # Caballo negro en la fila 0, columna 1 (posición inicial)

    def test_assign_value(self):
        # Verifica que el valor del caballo sea 3
        self.assertEqual(self.white_knight.assign_value(), 3)
        self.assertEqual(self.black_knight.assign_value(), 3)

    def test_str(self):
        # Verifica que el símbolo del caballo se muestre correctamente
        self.assertEqual(str(self.white_knight), "♘")
        self.assertEqual(str(self.black_knight), "♞")

    def test_is_valid_move(self):
        # Verifica que los movimientos en "L" sean válidos
        self.assertTrue(self.white_knight.is_valid_move(2, 1))  # Movimiento válido
        self.assertTrue(self.white_knight.is_valid_move(1, 2))  # Movimiento válido
        self.assertFalse(self.white_knight.is_valid_move(2, 2))  # Movimiento inválido
        self.assertFalse(self.white_knight.is_valid_move(3, 0))  # Movimiento inválido

    def test_is_valid_destination(self):
        positions = [[None for _ in range(8)] for _ in range(8)]  # Tablero vacío

        # Casilla vacía
        self.assertTrue(self.white_knight.is_valid_destination(5, 2, positions))

        # Casilla ocupada por una pieza del mismo color (invalida)
        positions[5][2] = Caballo("white", (5, 2))
        self.assertFalse(self.white_knight.is_valid_destination(5, 2, positions))

        # Casilla ocupada por una pieza de color contrario (válido para captura)
        positions[5][2] = Caballo("black", (5, 2))
        self.assertTrue(self.white_knight.is_valid_destination(5, 2, positions))

    def test_move_caballo_valid(self):
        # Prueba un movimiento válido en forma de "L"
        positions = [[None for _ in range(8)] for _ in range(8)]  # Tablero vacío
        self.assertTrue(self.white_knight.move_caballo((5, 2), positions))  # Movimiento válido
        self.assertTrue(self.white_knight.move_caballo((6, 3), positions))  # Movimiento válido

    def test_move_caballo_invalid(self):
        # Prueba un movimiento inválido que no es en forma de "L"
        positions = [[None for _ in range(8)] for _ in range(8)]  # Tablero vacío
        self.assertFalse(self.white_knight.move_caballo((6, 6), positions))  # Movimiento inválido
        self.assertFalse(self.white_knight.move_caballo((7, 3), positions))  # Movimiento inválido

    def test_move_caballo_capture(self):
        # Prueba un movimiento válido de captura
        positions = [[None for _ in range(8)] for _ in range(8)]
        positions[5][2] = Caballo("black", (5, 2))  # Colocamos un caballo negro en la casilla (5, 2)
        self.assertTrue(self.white_knight.move_caballo((5, 2), positions))  # Movimiento válido de captura

    def test_move_caballo_blocked_by_same_color(self):
        # Prueba que el caballo no pueda moverse a una casilla ocupada por una pieza del mismo color
        positions = [[None for _ in range(8)] for _ in range(8)]
        positions[5][2] = Caballo("white", (5, 2))  # Colocamos un caballo blanco en la casilla (5, 2)
        self.assertFalse(self.white_knight.move_caballo((5, 2), positions))  # Movimiento inválido (casilla ocupada)

    

class TestPeon(unittest.TestCase):


    def setUp(self):
        # Creamos peones blanco y negro antes de cada test
        self.white_peon = Peon("white", (6, 0))  # Peón blanco en la fila 6 (posición inicial)
        self.black_peon = Peon("black", (1, 0))  # Peón negro en la fila 1 (posición inicial)

    def test_assign_value(self):
        # Verifica que el valor del peón sea 1
        self.assertEqual(self.white_peon.assign_value(), 1)
        self.assertEqual(self.black_peon.assign_value(), 1)

    def test_str(self):
        # Verifica que el símbolo del peón se muestre correctamente
        self.assertEqual(str(self.white_peon), "♙")
        self.assertEqual(str(self.black_peon), "♟")

    def test_valid_white_move_initial(self):
        # Prueba un movimiento válido para el peón blanco en su posición inicial (2 pasos adelante)
        positions = [[None for _ in range(8)] for _ in range(8)]
        #self.assertTrue(self.white_peon.validate_movimiento(positions, (4, 0)))  # Mover dos filas hacia adelante
        self.assertFalse(self.white_peon.validate_movimiento(positions, (5, 0)))  # Mover una fila hacia adelante

    def test_valid_black_move_initial(self):
        # Prueba un movimiento válido para el peón negro en su posición inicial (2 pasos adelante)
        positions = [[None for _ in range(8)] for _ in range(8)]
        #self.assertTrue(self.black_peon.validate_movimiento(positions, (3, 0)))  # Mover dos filas hacia adelante
        self.assertFalse(self.black_peon.validate_movimiento(positions, (2, 0)))  # Mover una fila hacia adelante


if __name__ == '__main__':
    unittest.main()
