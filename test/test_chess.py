import unittest
from game.chess import Game
from game.board import Board
from game.exepciones import *
from game.rey import Rey
from game.peon import Peon

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
        self.assertEqual(self.__game__.traductor_de_input("A2"), (0, 6))
        self.assertEqual(self.__game__.traductor_de_input("H8"), (7, 0))

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

    def test_valid_moves(self):
    
        # Verificar que el turno inicial es de las blancas
        self.assertEqual(self.__game__.get_turn(), "White")
        
        # Verificar un movimiento válido de una pieza blanca
        self.assertTrue(self.__game__.movimiento("B1", "C3"))
        
        # Verificar que después de un movimiento válido, el turno cambie a "Black"
        self.assertEqual(self.__game__.get_turn(), "Black")

        # Realizar un movimiento para las piezas negras
        self.assertTrue(self.__game__.movimiento("A7", "A6"))
        
        # Verificar que el turno vuelva a ser "White"
        self.assertEqual(self.__game__.get_turn(), "White")


    def test_invalid_move(self):
        # Verificar excepciones por movimientos inválidos
        with self.assertRaises(InvalidMoveError):
            self.__game__.movimiento("A3", "A8")

        with self.assertRaises(InvalidMoveError):
            self.__game__.movimiento("B2", "B8")


    def test_verify_victory(self):
        # Simular que las blancas ganan
        self.__game__.__board__.reset_board()
        self.__game__.change_turn()
        self.__game__.__board__.place_piece(5, 2, Peon('White', (5, 2)))
        self.__game__.__board__.place_piece(4, 2, Rey('White', (4, 2)))
        self.__game__.__board__.place_piece(3, 2, Rey('Black', (3, 2)))
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
        self.__game__.__board__.place_piece(3, 2, Rey('White', (3, 2)))

        self.assertEqual(self.__game__.verify_victory(), "Ganan las Negras")

    def test_verify_victory_no_king(self):
            # Verificar que el juego detecta la victoria cuando no hay rey
            self.__game__.__board__.reset_board()
            self.__game__.__board__.place_piece(0, 0, Rey('White', (0, 0)))
            self.assertEqual(self.__game__.verify_victory(), "El juego continúa.")
            self.__game__.__board__.remove_piece(0, 0)
            self.assertEqual(self.__game__.verify_victory(), "Ganan las Negras")


 

if __name__ == "__main__":
    unittest.main()

