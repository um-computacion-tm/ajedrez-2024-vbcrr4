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
        self.assertTrue(self.piece.diagonal_move_positions((3, 3), positions))

        # Prueba un movimiento diagonal inválido (camino bloqueado)
        positions[1][1] = Piece("White", (1, 1))  # Colocamos una pieza en el camino
        self.assertFalse(self.piece.diagonal_move_positions((3, 3), positions))

        # Prueba un movimiento no diagonal (debe devolver False)
        self.assertFalse(self.piece.diagonal_move_positions((2, 3), positions))

    def test_vertical_move_positions(self):
        # Prueba un movimiento vertical válido
        positions = [[None for _ in range(8)] for _ in range(8)]
        self.piece.update_position((0, 0))
        self.assertTrue(self.piece.vertical_move_positions((3, 0), positions))

        # Prueba un movimiento vertical inválido (camino bloqueado)
        positions[1][0] = Piece("White", (1, 0))  # Colocamos una pieza en el camino
        self.assertFalse(self.piece.vertical_move_positions((3, 0), positions))

        # Prueba un movimiento no vertical (debe devolver False)
        self.assertFalse(self.piece.vertical_move_positions((3, 1), positions))

    def test_horizontal_move_positions(self):
        # Prueba un movimiento horizontal válido
        positions = [[None for _ in range(8)] for _ in range(8)]
        self.piece.update_position((0, 0))
        self.assertTrue(self.piece.horizontal_move_positions((0, 3), positions))

        # Prueba un movimiento horizontal inválido (camino bloqueado)
        positions[0][1] = Piece("White", (0, 1))  # Colocamos una pieza en el camino
        self.assertFalse(self.piece.horizontal_move_positions((0, 3), positions))

        # Prueba un movimiento no horizontal (debe devolver False)
        self.assertFalse(self.piece.horizontal_move_positions((1, 3), positions))

class TestTorre(unittest.TestCase):
    def setUp(self):
        self.torre_White = Torre('White',(1, 1))
        self.torre_Black = Torre('Black', (2, 2))

    def test_initialization(self):
        # Test initialization and inherited properties
        self.assertEqual(self.torre_White.color, "White")
        self.assertEqual(self.torre_White.position, (1, 1))
        self.assertEqual(self.torre_Black.color, "Black")
        self.assertEqual(self.torre_Black.position, (2, 2))

    def test_assign_value(self):
        # Test the assign_value method
        self.assertEqual(self.torre_White.assign_value(), 5)
        self.assertEqual(self.torre_Black.assign_value(), 5)


class TestRey(unittest.TestCase):

    def setUp(self):
        # Creamos reyes blanco y negro antes de cada test
        self.White_king = Rey("White", (7, 4))  # Rey blanco en la posición inicial
        self.Black_king = Rey("Black", (0, 4))  # Rey negro en la posición inicial

    def test_assign_value(self):
        # Verifica que el valor del rey sea 1000
        self.assertEqual(self.White_king.assign_value(), 1000)
        self.assertEqual(self.Black_king.assign_value(), 1000)

    def test_str(self):
        # Verifica que el símbolo del rey se muestre correctamente
        self.assertEqual(str(self.White_king), "♚")
        self.assertEqual(str(self.Black_king), "♔")

    def test_move_king_valid(self):
        # Verifica que los movimientos válidos del rey sean permitidos
        positions = [[None for _ in range(8)] for _ in range(8)]  # Tablero vacío
        self.assertTrue(self.White_king.move_king((6, 4), positions))  # Movimiento hacia abajo
        self.assertTrue(self.White_king.move_king((6, 5), positions))  # Movimiento en diagonal
        self.assertTrue(self.White_king.move_king((7, 5), positions))  # Movimiento lateral

    def test_move_king_invalid(self):
        # Verifica que los movimientos inválidos del rey no sean permitidos
        positions = [[None for _ in range(8)] for _ in range(8)]  # Tablero vacío
        self.assertFalse(self.White_king.move_king((5, 4), positions))  # Movimiento de 2 casillas hacia abajo
        self.assertFalse(self.White_king.move_king((7, 6), positions))  # Movimiento de 2 casillas hacia la derecha

    def test_move_king_blocked_by_same_color(self):
        # Verifica que el rey no pueda moverse a una casilla ocupada por una pieza del mismo color
        positions = [[None for _ in range(8)] for _ in range(8)]
        positions[6][4] = Rey("White", (6, 4))  # Colocamos otro rey blanco en la posición (6, 4)
        self.assertFalse(self.White_king.move_king((6, 4), positions))  # Movimiento inválido, casilla ocupada

    def test_move_king_capture_opponent(self):
        # Verifica que el rey pueda capturar una pieza del color contrario
        positions = [[None for _ in range(8)] for _ in range(8)]
        positions[6][4] = Rey("Black", (6, 4))  # Colocamos un rey negro en la posición (6, 4)
        self.assertTrue(self.White_king.move_king((6, 4), positions))  # Movimiento válido, captura



class TestAlfil(unittest.TestCase):

    def setUp(self):
        # Creamos alfiles blanco y negro antes de cada test
        self.White_alfil = Alfil("White", (7, 2))  # Alfil blanco en la posición inicial
        self.Black_alfil = Alfil("Black", (0, 2))  # Alfil negro en la posición inicial

    def test_assign_value(self):
        # Verifica que el valor del alfil sea 3
        self.assertEqual(self.White_alfil.assign_value(), 3)
        self.assertEqual(self.Black_alfil.assign_value(), 3)

    def test_str(self):
        # Verifica que el símbolo del alfil se muestre correctamente
        self.assertEqual(str(self.Black_alfil), "♗")
        self.assertEqual(str(self.White_alfil), "♝")

    def test_alfil_move_valid(self):
        # Prueba movimientos válidos en diagonal
        positions = [[None for _ in range(8)] for _ in range(8)]  # Tablero vacío
        self.assertTrue(self.White_alfil.alfil_move((5, 0), positions))  # Movimiento diagonal válido
        self.assertTrue(self.White_alfil.alfil_move((4, 5), positions))  # Otro movimiento diagonal válido

    def test_alfil_move_invalid(self):
        # Prueba movimientos inválidos (no diagonales) para el alfil
        positions = [[None for _ in range(8)] for _ in range(8)]  # Tablero vacío
        self.assertFalse(self.White_alfil.alfil_move((7, 3), positions))  # Movimiento horizontal inválido
        self.assertFalse(self.White_alfil.alfil_move((5, 2), positions))  # Movimiento vertical inválido

    def test_alfil_move_blocked(self):
        # Verifica que el movimiento del alfil sea inválido si hay una pieza bloqueando el camino
        positions = [[None for _ in range(8)] for _ in range(8)]
        positions[6][3] = Alfil("White", (6, 3))  # Colocamos una pieza en la diagonal del alfil
        self.assertFalse(self.White_alfil.alfil_move((5, 4), positions))  # Movimiento inválido, bloqueado


    def test_alfil_move_blocked_by_same_color(self):
        # Verifica que el alfil no pueda moverse a una casilla ocupada por una pieza del mismo color
        positions = [[None for _ in range(8)] for _ in range(8)]
        positions[5][0] = Alfil("White", (5, 0))  # Colocamos un alfil blanco en la diagonal
        self.assertFalse(self.White_alfil.alfil_move((5, 0), positions))  # Movimiento inválido, casilla ocupada

        
class TestReina(unittest.TestCase):
    def setUp(self):
        self.reina_White = Reina('White',(0,4))
        self.reina_Black = Reina('Black', (7, 4))

    def test_initialization(self):
        # Test initialization and inherited properties
        self.assertEqual(self.reina_White.color, "White")
        self.assertEqual(self.reina_White.position, (0,4))
        self.assertEqual(self.reina_Black.color, "Black")
        self.assertEqual(self.reina_Black.position, (7, 4))
    
    def test_assign_value(self):
        # Test the assign_value method
        self.assertEqual(self.reina_White.assign_value(), 9)
        self.assertEqual(self.reina_Black.assign_value(), 9)

class TestCaballo(unittest.TestCase):

    def setUp(self):
        # Creamos caballos blanco y negro antes de cada test
        self.White_knight = Caballo("White", (7, 1))  # Caballo blanco en la fila 7, columna 1 (posición inicial)
        self.Black_knight = Caballo("Black", (0, 1))  # Caballo negro en la fila 0, columna 1 (posición inicial)

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
        self.assertTrue(self.White_knight.is_valid_move(2, 1))  # Movimiento válido
        self.assertTrue(self.White_knight.is_valid_move(1, 2))  # Movimiento válido
        self.assertFalse(self.White_knight.is_valid_move(2, 2))  # Movimiento inválido
        self.assertFalse(self.White_knight.is_valid_move(3, 0))  # Movimiento inválido

    def test_is_valid_destination(self):
        positions = [[None for _ in range(8)] for _ in range(8)]  # Tablero vacío

        # Casilla vacía
        self.assertTrue(self.White_knight.is_valid_destination(5, 2, positions))

        # Casilla ocupada por una pieza del mismo color (invalida)
        positions[5][2] = Caballo("White", (5, 2))
        self.assertFalse(self.White_knight.is_valid_destination(5, 2, positions))

        # Casilla ocupada por una pieza de color contrario (válido para captura)
        positions[5][2] = Caballo("Black", (5, 2))
        self.assertTrue(self.White_knight.is_valid_destination(5, 2, positions))

    def test_move_caballo_valid(self):
        # Prueba un movimiento válido en forma de "L"
        positions = [[None for _ in range(8)] for _ in range(8)]  # Tablero vacío
        self.assertTrue(self.White_knight.move_caballo((5, 2), positions))  # Movimiento válido
        self.assertTrue(self.White_knight.move_caballo((6, 3), positions))  # Movimiento válido

    def test_move_caballo_invalid(self):
        # Prueba un movimiento inválido que no es en forma de "L"
        positions = [[None for _ in range(8)] for _ in range(8)]  # Tablero vacío
        self.assertFalse(self.White_knight.move_caballo((6, 6), positions))  # Movimiento inválido
        self.assertFalse(self.White_knight.move_caballo((7, 3), positions))  # Movimiento inválido

    def test_move_caballo_capture(self):
        # Prueba un movimiento válido de captura
        positions = [[None for _ in range(8)] for _ in range(8)]
        positions[5][2] = Caballo("Black", (5, 2))  # Colocamos un caballo negro en la casilla (5, 2)
        self.assertTrue(self.White_knight.move_caballo((5, 2), positions))  # Movimiento válido de captura

    def test_move_caballo_blocked_by_same_color(self):
        # Prueba que el caballo no pueda moverse a una casilla ocupada por una pieza del mismo color
        positions = [[None for _ in range(8)] for _ in range(8)]
        positions[5][2] = Caballo("White", (5, 2))  # Colocamos un caballo blanco en la casilla (5, 2)
        self.assertFalse(self.White_knight.move_caballo((5, 2), positions))  # Movimiento inválido (casilla ocupada)

    

class TestPeon(unittest.TestCase):


    def setUp(self):
        # Creamos peones blanco y negro antes de cada test
        self.White_peon = Peon("White", (6, 0))  # Peón blanco en la fila 6 (posición inicial)
        self.Black_peon = Peon("Black", (1, 0))  # Peón negro en la fila 1 (posición inicial)

    def test_assign_value(self):
        # Verifica que el valor del peón sea 1
        self.assertEqual(self.White_peon.assign_value(), 1)
        self.assertEqual(self.Black_peon.assign_value(), 1)

    def test_str(self):
        # Verifica que el símbolo del peón se muestre correctamente
        self.assertEqual(str(self.Black_peon), "♙")
        self.assertEqual(str(self.White_peon), "♟")

    def test_valid_White_move_initial(self):
        # Prueba un movimiento válido para el peón blanco en su posición inicial (2 pasos adelante)
        positions = [[None for _ in range(8)] for _ in range(8)]
        #self.assertTrue(self.White_peon.validate_movimiento(positions, (4, 0)))  # Mover dos filas hacia adelante
        self.assertFalse(self.White_peon.validate_movimiento(positions, (5, 0)))  # Mover una fila hacia adelante

    def test_valid_Black_move_initial(self):
        # Prueba un movimiento válido para el peón negro en su posición inicial (2 pasos adelante)
        positions = [[None for _ in range(8)] for _ in range(8)]
        #self.assertTrue(self.Black_peon.validate_movimiento(positions, (3, 0)))  # Mover dos filas hacia adelante
        self.assertFalse(self.Black_peon.validate_movimiento(positions, (2, 0)))  # Mover una fila hacia adelante


if __name__ == '__main__':
    unittest.main()
