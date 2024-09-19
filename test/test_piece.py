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
        self.caballo_white1 = Caballo('white',(0,1))
        self.caballo_white2 = Caballo('white',(0,6))
        self.caballo_black1 = Caballo('black', (7, 1))
        self.caballo_black2 = Caballo('black', (7, 6))

    def test_initialization(self):
        # Test initialization and inherited properties
        self.assertEqual(self.caballo_white1.color, "white")
        self.assertEqual(self.caballo_white1.position, (0,1))
        self.assertEqual(self.caballo_white2.color, "white")
        self.assertEqual(self.caballo_white2.position, (0,6))
        self.assertEqual(self.caballo_black1.color, "black")
        self.assertEqual(self.caballo_black1.position, (7, 1))
        self.assertEqual(self.caballo_black2.color, "black")
        self.assertEqual(self.caballo_black2.position, (7, 6))
    
    def test_assign_value(self):
        # Test the assign_value method
        self.assertEqual(self.caballo_white1.assign_value(), 3)
        self.assertEqual(self.caballo_white2.assign_value(), 3)
        self.assertEqual(self.caballo_black1.assign_value(), 3)
        self.assertEqual(self.caballo_black2.assign_value(), 3)
    

class TestPeon(unittest.TestCase):

    def setUp(self):
        self.peon_white1 = Peon('white',(1,0))
        self.peon_white2 = Peon('white',(1,1))
        self.peon_black1 = Peon('black', (6, 0))
        self.peon_black2 = Peon('black', (6, 1))

    def test_initialization(self):
        # Test initialization and inherited properties
        self.assertEqual(self.peon_white1.color, "white")
        self.assertEqual(self.peon_white1.position, (1,0))
        self.assertEqual(self.peon_white2.color, "white")
        self.assertEqual(self.peon_white2.position, (1,1))
        self.assertEqual(self.peon_black1.color, "black")
        self.assertEqual(self.peon_black1.position, (6, 0))
        self.assertEqual(self.peon_black2.color, "black")
        self.assertEqual(self.peon_black2.position, (6, 1))
    
    def test_assign_value(self):
        # Test the assign_value method
        self.assertEqual(self.peon_white1.assign_value(), 1)
        self.assertEqual(self.peon_white2.assign_value(), 1)
        self.assertEqual(self.peon_black1.assign_value(), 1)
        self.assertEqual(self.peon_black2.assign_value(), 1)

if __name__ == '__main__':
    unittest.main()
