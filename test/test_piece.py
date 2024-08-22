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

    def test_get_color(self):
        piece = Torre('white')
        self.assertEqual(piece.get_color(), 'white')

    def test_get_symbol(self):
        piece = Torre('white')
        piece.assign_symbol()  # Necesario para asignar el símbolo
        self.assertEqual(piece.get_symbol(), '♖')

    def test_get_value(self):
        piece = Torre('white')
        self.assertEqual(piece.get_value(), 5)

class TestTorre(unittest.TestCase):
    def setUp(self):
        self.torre_blanca = Torre('white')
        self.torre_negra = Torre('black')

    def test_assign_symbol_white(self):
        self.torre_blanca.assign_symbol()
        self.assertEqual(self.torre_blanca.get_symbol(), '♖')

    def test_assign_symbol_black(self):
        self.torre_negra.assign_symbol()
        self.assertEqual(self.torre_negra.get_symbol(), '♜')

    def test_is_valid_move_horizontal(self):
        result = self.torre_blanca.is_valid_move([0, 0], [0, 7])
        self.assertTrue(result)

    def test_is_valid_move_vertical(self):
        result = self.torre_blanca.is_valid_move([0, 0], [7, 0])
        self.assertTrue(result)

    def test_is_valid_move_invalid(self):
        result = self.torre_blanca.is_valid_move([0, 0], [1, 1])
        self.assertFalse(result)

class TestRey(unittest.TestCase):
    def setUp(self):
        self.rey_blanco = Rey('white')
        self.rey_negro = Rey('black')

    def test_assign_symbol_white(self):
        self.assertEqual(self.rey_blanco.get_symbol(), '♔')

    def test_assign_symbol_black(self):
        self.assertEqual(self.rey_negro.get_symbol(), '♚')

    def test_assign_value(self):
        self.assertEqual(self.rey_blanco.get_value(), 1000)
        self.assertEqual(self.rey_negro.get_value(), 1000)

    def test_is_valid_move_one_square_any_direction(self):
        # Movimientos válidos (una casilla en cualquier dirección)
        valid_moves = [
            ([4, 4], [5, 4]),  # Abajo
            ([4, 4], [3, 4]),  # Arriba
            ([4, 4], [4, 5]),  # Derecha
            ([4, 4], [4, 3]),  # Izquierda
            ([4, 4], [5, 5]),  # Abajo-Derecha
            ([4, 4], [3, 3]),  # Arriba-Izquierda
            ([4, 4], [5, 3]),  # Abajo-Izquierda
            ([4, 4], [3, 5]),  # Arriba-Derecha
        ]

        for start_pos, end_pos in valid_moves:
            with self.subTest(start=start_pos, end=end_pos):
                self.assertTrue(self.rey_blanco.is_valid_move(start_pos, end_pos))

    def test_is_invalid_move_more_than_one_square(self):
        # Movimientos inválidos (más de una casilla en cualquier dirección)
        invalid_moves = [
            ([4, 4], [6, 4]),  # Dos casillas hacia abajo
            ([4, 4], [4, 6]),  # Dos casillas hacia derecha
            ([4, 4], [2, 2]),  # Diagonal de dos casillas
            ([4, 4], [6, 6]),  # Diagonal de dos casillas (contrario)
        ]

        for start_pos, end_pos in invalid_moves:
            with self.subTest(start=start_pos, end=end_pos):
                self.assertFalse(self.rey_blanco.is_valid_move(start_pos, end_pos))

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

if __name__ == '__main__':
    unittest.main()
