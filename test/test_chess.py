import unittest
from unittest.mock import patch
from game.chess import Game
from game.exepciones import *
from game.rey import Rey
from game.peon import Peon
from game.piece import Piece
from game.caballo import Caballo
from game.alfil import Alfil
from game.torre import Torre
from game.reina import Reina


class TestGame(unittest.TestCase):
    def setUp(self):
        self.__game__ = Game()
       
    def test_initial_turn(self):
        # Verificar que el turno inicial sea "White"
        self.assertEqual(self.__game__.get_turn(), "White")

    def test_change_turn(self):
        # Verificar el cambio de turnos
        self.__game__.change_turn()
        self.assertEqual(self.__game__.get_turn(), "Black")
        self.__game__.change_turn()
        self.assertEqual(self.__game__.get_turn(), "White")

    def test_translate_input_valid(self):
        # Verificar que se traduzcan correctamente las entradas válidas
        self.assertEqual(self.__game__.traductor_de_input("A2"), (6, 0))
        self.assertEqual(self.__game__.traductor_de_input("H8"), (0, 7))

    def test_translate_input_invalid(self):
        # Verificar que se levanten excepciones para entradas inválidas
        with self.assertRaises(InvalidInputError):
            self.__game__.traductor_de_input("QI9")  # Fuera del rango de tablero
        with self.assertRaises(InvalidInputError):
            self.__game__.traductor_de_input("AQ9")  # Fila inválida
        with self.assertRaises(InvalidInputError):
            self.__game__.traductor_de_input("A")   # Longitud incorrecta
        with self.assertRaises(InvalidInputError):
            self.__game__.traductor_de_input("1QA")  # Formato incorrecto

    @patch('builtins.input', side_effect=["B1", "C3", "A7", "A6", "Q"])  # Simula entradas de usuario
    @patch('builtins.print')  # Para evitar la salida de impresión en los tests
    def test_play(self, mock_print, mock_input):
        """
        Testea el método `play` simulando algunos movimientos y verificando el flujo de turnos.
        Las entradas simuladas son: "B1", "C3", "A7", "A6", "B2", "B3", "Q" (para terminar).
        """
        # Colocar el caballo blanco en B1 y el rey negro en A7 para poder realizar movimientos
        self.__game__.__board__.place_piece(7, 1, Caballo('White', (7, 1)))  
        self.__game__.__board__.place_piece(1, 0, Peon('Black', (1, 0)))  
        self.__game__.__board__.place_piece(6, 1, Peon("White", (6, 1)))

        # Iniciar el juego simulando entradas de usuario para jugar
        self.__game__.play("B1", "C3")

        # Verificar que después del primer movimiento, el turno haya cambiado a "Black"
        self.__game__.change_turn()  # Depuración
        self.assertEqual(self.__game__.get_turn(), "Black")

        # Simular otro movimiento y verificar el cambio de turno
        self.__game__.play("A7", "A6")
        self.__game__.change_turn()  # Depuración
        self.assertEqual(self.__game__.get_turn(), "White")

        # Verificar que el juego continúa correctamente con las entradas
        self.__game__.play("B2", "B3")  # Simula otro movimiento blanco
        self.__game__.change_turn() # Depuración
        self.assertEqual(self.__game__.get_turn(), "Black")

    def test_verify_victory(self):
        # Simular que las blancas ganan
        self.__game__.__board__.reset_board()
        self.__game__.change_turn()
        self.__game__.__board__.place_piece(5, 2, Peon('White', (5, 2)))
        self.__game__.__board__.place_piece(4, 2, Rey('White', (4, 2)))
        self.assertEqual(self.__game__.verify_victory(), "Ganan las Blancas")


        # Simular un empate (solo quedan los reyes)
        self.__game__.__board__.reset_board()
        self.__game__.__board__.place_piece(0, 0, Rey('White', (0, 0)))
        self.__game__.__board__.place_piece(7, 7, Rey('Black', (7, 7)))
        self.assertEqual(self.__game__.verify_victory(), "Empate")

        # Simular victoria de las negras
        self.__game__.__board__.reset_board()
        self.__game__.change_turn()
        self.__game__.__board__.place_piece(5, 2, Peon('Black', (5, 2)))
        self.__game__.__board__.place_piece(4, 2, Rey('Black', (4, 2)))

        self.assertEqual(self.__game__.verify_victory(), "Ganan las Negras")

    def test_invalid_moves_chess(self):

        # Movimiento inválido (fuera del tablero)
        #self.assertFalse(self.__game__.valid_moves("A2", "A9"))

        # Movimiento inválido (misma pieza en destino)
        self.assertFalse(self.__game__.valid_moves("A2", "A1"))

        # Movimiento inválido (posición vacía)
        self.assertFalse(self.__game__.valid_moves("C3", "C4"))

    def test_valid_moves_chess(self):
    
        # Forzar el turno a White antes de mover
        self.__game__.__turn__ = "White"
        # Depuración: Imprimir el turno actual
        print(f"Turno actual: {self.__game__.get_turn()}")
        
        # Depuración: Mostrar el tablero antes del movimiento
        print("Tablero antes del movimiento:")
        self.__game__.show_board()

        # Intentar mover el peón blanco de A2 a A3
        result = self.__game__.movimiento("A2", "A3")

        # Depuración: Verificar si el movimiento fue exitoso
        print(f"Resultado del movimiento: {result}")
        
        # Depuración: Mostrar el tablero después del movimiento
        print("Tablero después del movimiento:")
        self.__game__.show_board()

        # Verificar que el movimiento sea válido
        self.assertTrue(result)

    def test_valid_moves_chess2(self):
    
        self.__game__.change_turn()
        # Depuración: Imprimir el turno actual
        #print(f"Turno actual: {self.__game__.get_turn()}")
        
        # Depuración: Mostrar el tablero antes del movimiento
        #print("Tablero antes del movimiento:")
        #self.__game__.show_board()

        # Intentar mover 
        result = self.__game__.movimiento("B8", "C6")

        # Depuración: Verificar si el movimiento fue exitoso
        #print(f"Resultado del movimiento: {result}")
        
        # Depuración: Mostrar el tablero después del movimiento
        #print("Tablero después del movimiento:")
        #self.__game__.show_board()

        # Verificar que el movimiento sea válido
        self.assertTrue(result)
        


if __name__ == "__main__":
    unittest.main()

