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
#test de metodo 'assing_value' de la clase Piece  (aunque se puede probar indirectamente a través de las subclases)
#test de Método get_color y get_symbol: Asegurarse de que devuelvan los valores correctos.
#Prueba de los métodos abstractos: Usar una subclase de prueba para verificar que los métodos abstractos se comportan correctamente.

    def setUp(self):
        # Este método se ejecuta antes de cada test
        self.__piece_white__ = Piece("white", (1, 1))
        self.__piece_black__ = Piece("black", (2, 2))

    def test_initialization(self):
        # Test initialization and property getters
        self.assertEqual(self.__piece_white__.get_color, "white")
        self.assertEqual(self.__piece_white__.get_position, (1, 1))
        self.assertEqual(self.__piece_black__.get_color, "black")
        self.assertEqual(self.__piece_black__.get_position, (2, 2))
    
    def test_update_position(self):
        # Test updating position
        new_position = (3, 3)
        self.__piece_white__.update_position(new_position)
        self.assertEqual(self.__piece_white__.get_position, new_position)

    def test_get_cords(self):
        # Test get_cords method
        new_position = (3, 3)
        cords = self.__piece_white__.get_cords(new_position)
        self.assertEqual(cords, (1, 1, 3, 3))



class TestTorre(unittest.TestCase):
    def setUp(self):
        self.torre_white = Torre('white',(1, 1))
        self.torre_black = Torre('black', (2, 2))

    def test_initialization(self):
        # Test initialization and inherited properties
        self.assertEqual(self.torre_white.get_color, "white")
        self.assertEqual(self.torre_white.get_position, (1, 1))
        self.assertEqual(self.torre_black.get_color, "black")
        self.assertEqual(self.torre_black.get_position, (2, 2))

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
        self.assertEqual(self.rey_white.get_color, "white")
        self.assertEqual(self.rey_white.get_position, (0,3))
        self.assertEqual(self.rey_black.get_color, "black")
        self.assertEqual(self.rey_black.get_position, (7, 3))
    
    def test_assign_value(self):
        # Test the assign_value method
        self.assertEqual(self.rey_white.assign_value(), 1000)
        self.assertEqual(self.rey_black.assign_value(), 1000)

'''
class TestAlfil(unittest.TestCase):

    def setUp(self):
        self.alfil_blanco = Alfil('white')
        self.alfil_negro = Alfil('black')

    def test_assign_symbol_white(self):
        self.assertEqual(self.alfil_blanco.get_symbol(), '♗')

    def test_assign_symbol_black(self):
        self.assertEqual(self.alfil_negro.get_symbol(), '♝')

    def test_assign_value(self):
        self.assertEqual(self.alfil_blanco.get_value(), 3)
        self.assertEqual(self.alfil_negro.get_value(), 3)

    def test_is_valid_move_diagonal(self):
        # Movimiento diagonal válido
        start_pos = [2, 0]
        end_pos = [5, 3]
        self.assertTrue(self.alfil_blanco.is_valid_move(start_pos, end_pos))

    def test_is_invalid_move(self):
        # Movimiento no diagonal, inválido
        start_pos = [2, 0]
        end_pos = [4, 3]
        self.assertFalse(self.alfil_blanco.is_valid_move(start_pos, end_pos))
    
class TestPeon(unittest.TestCase):

    def setUp(self):
        self.peon_blanco = Peon('white')
        self.peon_negro = Peon('black')

    def test_assign_symbol_white(self):
        self.assertEqual(self.peon_blanco.get_symbol(), '♙')

    def test_assign_symbol_black(self):
        self.assertEqual(self.peon_negro.get_symbol(), '♟')

    def test_assign_value(self):
        self.assertEqual(self.peon_blanco.get_value(), 1)
        self.assertEqual(self.peon_negro.get_value(), 1)

    def test_is_valid_move_white_one_step(self):
        # Movimiento de una casilla hacia adelante (válido para peón blanco)
        self.assertTrue(self.peon_blanco.is_valid_move([6, 4], [5, 4]))

    def test_is_valid_move_white_two_steps_first_move(self):
        # Movimiento de dos casillas hacia adelante (válido solo en el primer movimiento)
        self.assertTrue(self.peon_blanco.is_valid_move([6, 4], [4, 4]))

    def test_is_invalid_move_white_two_steps_after_first(self):
        # Movimiento de dos casillas después del primer movimiento (inválido)
        self.peon_blanco.is_valid_move([6, 4], [4, 4])  # Primer movimiento para avanzar dos
        self.assertFalse(self.peon_blanco.is_valid_move([4, 4], [2, 4]))

    def test_is_invalid_move_white_sideways(self):
        # Movimiento lateral (inválido)
        self.assertFalse(self.peon_blanco.is_valid_move([6, 4], [6, 5]))

    def test_is_valid_move_black_one_step(self):
        # Movimiento de una casilla hacia adelante (válido para peón negro)
        self.assertTrue(self.peon_negro.is_valid_move([1, 4], [2, 4]))

    def test_is_valid_move_black_two_steps_first_move(self):
        # Movimiento de dos casillas hacia adelante (válido solo en el primer movimiento)
        self.assertTrue(self.peon_negro.is_valid_move([1, 4], [3, 4]))

    def test_is_invalid_move_black_two_steps_after_first(self):
        # Movimiento de dos casillas después del primer movimiento (inválido)
        self.peon_negro.is_valid_move([1, 4], [3, 4])  # Primer movimiento para avanzar dos
        self.assertFalse(self.peon_negro.is_valid_move([3, 4], [5, 4]))

    def test_is_invalid_move_black_sideways(self):
        # Movimiento lateral (inválido)
        self.assertFalse(self.peon_negro.is_valid_move([1, 4], [1, 5]))

class TestReina(unittest.TestCase):
    def setUp(self):
        self.reina_blanca = Reina('white')
        self.reina_negra = Reina('black')

    def test_assign_symbol_white(self):
        self.assertEqual(self.reina_blanca.get_symbol(), '♕')

    def test_assign_symbol_black(self):
        self.assertEqual(self.reina_negra.get_symbol(), '♛')

    def test_assign_value(self):
        self.assertEqual(self.reina_blanca.get_value(), 9)
        self.assertEqual(self.reina_negra.get_value(), 9)

    def test_is_valid_move_horizontal(self):
        # Movimiento horizontal válido
        start_pos = [3, 3]
        end_pos = [3, 7]
        self.assertTrue(self.reina_blanca.is_valid_move(start_pos, end_pos))

    def test_is_valid_move_vertical(self):
        # Movimiento vertical válido
        start_pos = [3, 3]
        end_pos = [7, 3]
        self.assertTrue(self.reina_blanca.is_valid_move(start_pos, end_pos))

    def test_is_valid_move_diagonal(self):
        # Movimiento diagonal válido
        start_pos = [3, 3]
        end_pos = [6, 6]
        self.assertTrue(self.reina_blanca.is_valid_move(start_pos, end_pos))

    def test_is_invalid_move(self):
        # Movimiento no válido (ni horizontal, vertical, ni diagonal)
        start_pos = [3, 3]
        end_pos = [5, 6]
        self.assertFalse(self.reina_blanca.is_valid_move(start_pos, end_pos))

class TestCaballo(unittest.TestCase):
    def setUp(self):
        self.caballo_blanco = Caballo('white')
        self.caballo_negro = Caballo('black')

    def test_assign_symbol_white(self):
        self.assertEqual(self.caballo_blanco.get_symbol(), '♘')

    def test_assign_symbol_black(self):
        self.assertEqual(self.caballo_negro.get_symbol(), '♞')

    def test_assign_value(self):
        self.assertEqual(self.caballo_blanco.get_value(), 3)
        self.assertEqual(self.caballo_negro.get_value(), 3)

    def test_is_valid_move_L_shape(self):
        # Movimientos válidos en forma de 'L'
        valid_moves = [
            ([3, 3], [5, 4]),  # 2 abajo, 1 derecha
            ([3, 3], [1, 4]),  # 2 arriba, 1 derecha
            ([3, 3], [4, 5]),  # 1 abajo, 2 derecha
            ([3, 3], [2, 5]),  # 1 arriba, 2 derecha
            ([3, 3], [5, 2]),  # 2 abajo, 1 izquierda
            ([3, 3], [1, 2]),  # 2 arriba, 1 izquierda
            ([3, 3], [4, 1]),  # 1 abajo, 2 izquierda
            ([3, 3], [2, 1])   # 1 arriba, 2 izquierda
        ]

        for start_pos, end_pos in valid_moves:
            with self.subTest(start=start_pos, end=end_pos):
                self.assertTrue(self.caballo_blanco.is_valid_move(start_pos, end_pos))

    def test_is_invalid_move(self):
        # Movimientos no válidos (no en forma de 'L')
        invalid_moves = [
            ([3, 3], [4, 4]),  # 1 abajo, 1 derecha
            ([3, 3], [5, 5]),  # 2 abajo, 2 derecha
            ([3, 3], [3, 5]),  # 0 abajo, 2 derecha
            ([3, 3], [1, 1])   # 2 arriba, 2 izquierda
        ]

        for start_pos, end_pos in invalid_moves:
            with self.subTest(start=start_pos, end=end_pos):
                self.assertFalse(self.caballo_blanco.is_valid_move(start_pos, end_pos))
'''
if __name__ == '__main__':
    unittest.main()
