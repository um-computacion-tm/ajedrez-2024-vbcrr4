import unittest
from unittest.mock import MagicMock, patch
from game.chess import Game
from game.board import Board
from game.exepciones import *
from game.rey import Rey
from game.peon import Peon

class TestGame(unittest.TestCase):
    def setUp(self):
        self.__game__ = Game()

    def test_check_victory_status_draw(self):
        # Mock específico para simular un empate
        self.__game__.__board__.count_pieces = MagicMock(return_value=(1, 1))
        self.assertEqual(self.__game__.check_victory_status(), "Empate")

    def test_check_victory_status_white_wins(self):
        # Mock para simular una victoria de las Blancas
        self.__game__.__board__.count_pieces = MagicMock(return_value=(2, 0))
        self.__game__.__turn__ = "Black"
        self.assertEqual(self.__game__.check_victory_status(), "Ganan las Blancas")

    def test_soloq(self):
        self.assertFalse(self.__game__.play("Q", None))

    def test_move(self):
        resultado = self.__game__.play("A2", "A3")
        self.assertTrue(resultado)

    def test_invalidate(self):
        self.assertFalse(self.__game__.play("A2", "C8"))

    def test_initial_turn_is_white(self):
        self.assertEqual(self.__game__.__turn__, "White")

    def test_execute_move_switches_turn(self):
        start_pos, end_pos = "A2", "A4"
        self.__game__.perform_movement = MagicMock(return_value=True)
        
        with patch('builtins.print'):
            self.__game__.execute_move(start_pos, end_pos)
            self.assertEqual(self.__game__.__turn__, "Black")

    def test_execute_move_does_not_switch_turn_on_failed_move(self):
        start_pos, end_pos = "A2", "A4"
        self.__game__.perform_movement = MagicMock(return_value=False)
        
        with patch('builtins.print'):
            self.__game__.execute_move(start_pos, end_pos)
            self.assertEqual(self.__game__.__turn__, "White")

    def test_is_valid_move_out_of_bounds(self):
        start_pos, end_pos = "Z9", "A3"
        self.__game__.translate_position = MagicMock(side_effect=InvalidInputError("Posición no válida"))
        
        with patch('builtins.print'):
            self.assertFalse(self.__game__.is_valid_move(start_pos, end_pos))

    def test_get_own_piece_valid(self):
        self.__game__.__board__ = MagicMock(spec=Board)
        coords = (6, 0)
        piece = MagicMock(color="White")
        self.__game__.__board__.get_piece.return_value = piece
        self.assertEqual(self.__game__.get_own_piece(coords), coords)

    def test_get_own_piece_invalid_color(self):
        self.__game__.__board__ = MagicMock(spec=Board)
        coords = (6, 0)
        piece = MagicMock(color="Black")
        self.__game__.__board__.get_piece.return_value = piece
        
        with self.assertRaises(InvalidColorError):
            self.__game__.get_own_piece(coords)

    def test_validate_move_result_game_continues(self):
        self.__game__.check_victory_status = MagicMock(return_value="El juego continúa")
        self.assertTrue(self.__game__.validate_move_result(True))

    def test_validate_move_result_game_over(self):
        self.__game__.check_victory_status = MagicMock(return_value="Ganan las Blancas")
        self.assertEqual(self.__game__.validate_move_result(True), "Ganan las Blancas")

    def test_switch_turn(self):
        self.__game__.switch_turn()
        self.assertEqual(self.__game__.__turn__, "Black")
        self.__game__.switch_turn()
        self.assertEqual(self.__game__.__turn__, "White")

    def test_translate_position_valid(self):
        self.assertEqual(self.__game__.translate_position("A1"), (7, 0))
        self.assertEqual(self.__game__.translate_position("H8"), (0, 7))

    def test_translate_position_invalid(self):
        with self.assertRaises(InvalidInputError):
            self.__game__.translate_position("Z9")

    def test_check_victory_status_draw(self):
        self.__game__.__board__.count_pieces = MagicMock(return_value=(1, 1))
        self.assertEqual(self.__game__.check_victory_status(), "Empate")
#####
    def test_translate_position_invalid_length(self):
        """Prueba que `translate_position` lance `InvalidInputError` cuando el input tiene más de dos caracteres."""
        with self.assertRaises(InvalidInputError):
            self.__game__.translate_position("A12")  # Input inválido con longitud mayor a 2

    def test_check_victory_status_black_wins(self):
        """Prueba que `check_victory_status` retorne 'Ganan las Negras' cuando cumplen las condiciones de victoria."""
        self.__game__.__board__.count_pieces = MagicMock(return_value=(0, 2))  # Solo quedan piezas negras
        self.__game__.__turn__ = "White"
        self.assertEqual(self.__game__.check_victory_status(), "Ganan las Negras")

    def test_get_turn(self):
        """Prueba que `get_turn` devuelva el turno actual."""
        self.assertEqual(self.__game__.get_turn(), "White")  # Turno inicial debe ser White
        self.__game__.switch_turn()
        self.assertEqual(self.__game__.get_turn(), "Black")  # Después del cambio debe ser Black

    def test_validate_move_result_returns_false(self):
        """Prueba que `validate_move_result` retorne False si `move_result` es False."""
        self.assertFalse(self.__game__.validate_move_result(False))

    def test_get_own_piece_piece_is_none(self):
        """Prueba que `get_own_piece` lance `PieceNotFoundError` si no hay ninguna pieza en `coords`."""
        self.__game__.__board__ = MagicMock(spec=Board)
        self.__game__.__board__.get_piece.return_value = None  # No hay pieza en las coordenadas
        with self.assertRaises(PieceNotFoundError):
            self.__game__.get_own_piece((4, 4))

    def test_is_valid_move_target_piece_same_color_returns_false(self):
        """Prueba que `is_valid_move` retorne False si `target_piece` es del mismo color que `piece`."""
        piece_mock = MagicMock(color="White")
        target_piece_mock = MagicMock(color="White")
        
        self.__game__.__board__ = MagicMock(spec=Board)
        self.__game__.__board__.get_piece.side_effect = [piece_mock, target_piece_mock]  # Simula pieza y destino del mismo color
        self.assertFalse(self.__game__.is_valid_move("A2", "A3"))

    def test_is_valid_move_piece_is_none_returns_false(self):
        """Prueba que `is_valid_move` retorne False si `piece` es None en la posición inicial."""
        self.__game__.__board__ = MagicMock(spec=Board)
        self.__game__.__board__.get_piece.return_value = None  # No hay pieza en la posición inicial
        self.assertFalse(self.__game__.is_valid_move("A2", "A3"))

    def test_game_over_when_game_finished(self):
        """Test para verificar que el juego termina cuando se ha decidido un ganador o empate."""
        self.__game__.check_victory_status = MagicMock(return_value="Ganan las Blancas")
        self.assertTrue(self.__game__.game_over())

    def test_play_raises_InvalidMoveError(self):
        """Simula `play` cuando `perform_movement` genera un `InvalidMoveError`."""
        self.__game__.is_valid_move = MagicMock(return_value=True)
        self.__game__.perform_movement = MagicMock(side_effect=InvalidMoveError("Error de movimiento inválido"))

        with patch('builtins.print') as mocked_print:
            self.assertFalse(self.__game__.play("A2", "A4"))
            mocked_print.assert_any_call("Error: Error de movimiento inválido")

    def test_play_raises_PieceNotFoundError(self):
        """Simula `play` cuando `perform_movement` genera un `PieceNotFoundError`."""
        self.__game__.is_valid_move = MagicMock(return_value=True)
        self.__game__.perform_movement = MagicMock(side_effect=PieceNotFoundError("Error: Pieza no encontrada"))

        with patch('builtins.print') as mocked_print:
            self.assertFalse(self.__game__.play("A2", "A4"))
            mocked_print.assert_any_call("Error: Error: Pieza no encontrada")

    def test_play_invalid_move(self):
        """Prueba `play` cuando el movimiento es inválido según `is_valid_move`."""
        self.__game__.is_valid_move = MagicMock(return_value=False)

        with patch('builtins.print') as mocked_print:
            self.assertFalse(self.__game__.play("A2", "A8"))
            mocked_print.assert_any_call("Movimiento inválido de A2 a A8")

    def test_execute_move_turn_stays_same_on_failed_move(self):
        """Prueba `execute_move` para verificar que el turno no cambia si el movimiento falla."""
        start_pos, end_pos = "A2", "A4"
        self.__game__.perform_movement = MagicMock(return_value=False)

        with patch('builtins.print'):
            self.__game__.execute_move(start_pos, end_pos)
            self.assertEqual(self.__game__.__turn__, "White")  # El turno debe permanecer igual

    def test_perform_movement_successful(self):
        """Prueba `perform_movement` cuando el movimiento es exitoso."""
        start_pos, end_pos = "A2", "A4"
        self.__game__.translate_position = MagicMock(side_effect=[(6, 0), (4, 0)])
        self.__game__.get_own_piece = MagicMock(return_value=(6, 0))
        self.__game__.__board__.move = MagicMock(return_value=True)
        self.__game__.validate_move_result = MagicMock(return_value=True)

        self.assertTrue(self.__game__.perform_movement(start_pos, end_pos))
        self.__game__.__board__.move.assert_called_once_with((6, 0), (4, 0))

    def test_perform_movement_invalid_input_error(self):
        """Prueba `perform_movement` cuando ocurre un `InvalidInputError`."""
        start_pos, end_pos = "Z9", "A4"
        self.__game__.translate_position = MagicMock(side_effect=InvalidInputError("Posición no válida"))

        with self.assertRaises(InvalidInputError):
            self.__game__.perform_movement(start_pos, end_pos)

    def test_translate_position_invalid_format(self):
        """Prueba `translate_position` cuando la entrada tiene formato incorrecto."""
        with self.assertRaises(InvalidInputError):
            self.__game__.translate_position("AA")
        with self.assertRaises(InvalidInputError):
            self.__game__.translate_position("1A")  # Formato incorrecto

    

if __name__ == "__main__":
    unittest.main()

