import unittest
from unittest.mock import patch, MagicMock
from game.cli import Interfaz
from game.chess import Game
from game.exepciones import *

class TestInterfaz(unittest.TestCase):

    def setUp(self):
        """Se ejecuta antes de cada prueba."""
        self.interfaz = Interfaz()
        self.interfaz.__game__ = MagicMock(spec=Game)  # Mock para evitar comportamiento real de Game

    """@patch('builtins.input', side_effect=['1', '4', 's'])  # Simula más entradas
    #@patch('game.cli.Interfaz.rendirse')
    @patch('builtins.print')
    def test_menu_principal(self,mock_print , mock_input):
        self.interfaz.iniciar()
        #self.interfaz.bucle_juego()
        #self.interfaz.rendirse()
        #mock_rendirse.assert_called_once()
        mock_print.assert_called_with("Game Over")"""

    @patch('builtins.input', side_effect=["5", "5"])  # Agrega suficientes valores para el mock de input
    def test_iniciar_partida2(self, mock_input):
        self.interfaz = Interfaz()
        self.interfaz.iniciar_partida()
        self.assertEqual(self.interfaz.contador_turnos, 0)
        # Agrega más aserciones según sea necesario para verificar el comportamiento


    @patch('builtins.input', side_effect=['B1', 'C3'])  # Opción de menú + posiciones de ajedrez
    @patch('os.system')
    def test_realizar_movimiento_valido1(self, mock_os, mock_input):
        """Test para realizar un movimiento válido pasando por el menú."""
        self.interfaz.__game__.valid_moves.return_value = True
        self.interfaz.realizar_movimiento('B1', 'C3')  # Ahora se pasan los argumentos
        self.interfaz.__game__.play.assert_called_once_with('B1', 'C3')  # Verifica la llamada correcta
        self.assertEqual(self.interfaz.contador_turnos, 1)


    @patch('builtins.input', side_effect=[ 'A2', 'A3'])  # Menú: opción 1, movimiento: A2 a A3
    @patch('os.system')
    def test_realizar_movimiento_valido2(self, mock_os, mock_input):
        """Test para realizar un movimiento válido."""
        self.interfaz.__game__.valid_moves.return_value = True
        self.interfaz.realizar_movimiento('A2', 'A3')  # Ahora se pasan los argumentos
        self.interfaz.__game__.play.assert_called_once_with('A2', 'A3')  # Verifica la llamada correcta
        self.assertEqual(self.interfaz.contador_turnos, 1)


    @patch('builtins.input', side_effect=[ 'A2', 'A3'])  # Menú: opción 1, mover de A2 a A3
    @patch('os.system')
    def test_realizar_movimiento_invalido1(self, mock_os, mock_input):
        """Test para un movimiento inválido que lanza una excepción."""
        self.interfaz.__game__.play.side_effect = InvalidMoveError("Movimiento inválido")
        self.interfaz.realizar_movimiento('A2', 'A3')  # Ahora se pasan los argumentos
        self.interfaz.__game__.play.assert_called_once_with('A2', 'A3')
        self.assertEqual(self.interfaz.contador_turnos, 0)  # No debe incrementar el turno


    @patch('builtins.input', side_effect=[ 'A1', 'A3'])  # Menú: opción 1, mover de A2 a A3
    @patch('os.system')
    def test_realizar_movimiento_invalido2(self, mock_os, mock_input):
        """Test para un movimiento inválido que lanza una excepción."""
        self.interfaz.__game__.play.side_effect = InvalidMoveError("Movimiento inválido")
        self.interfaz.realizar_movimiento( 'A1', 'A3')
        self.interfaz.__game__.play.assert_called_once_with('A1', 'A3')
        self.assertEqual(self.interfaz.contador_turnos, 0)  # No debe incrementar el turno


    @patch('builtins.input', side_effect=['s'])
    def test_ofrecer_empate_aceptado(self, mock_input):
        """Test para verificar si el empate es aceptado."""
        self.assertTrue(self.interfaz.ofrecer_empate())

    @patch('builtins.input', side_effect=['n'])
    def test_ofrecer_empate_rechazado(self, mock_input):
        """Test para verificar si el empate es rechazado."""
        self.assertFalse(self.interfaz.ofrecer_empate())

    @patch('builtins.input', side_effect=['s'])
    def test_rendirse(self, mock_input):
        """Test para verificar la rendición de un jugador."""
        self.interfaz.__game__.get_turn.return_value = "Blancas"
        self.assertTrue(self.interfaz.rendirse())

    @patch('builtins.input', side_effect=['n'])
    def test_cancelar_rendicion(self, mock_input):
        """Test para verificar si la rendición es cancelada."""
        self.interfaz.__game__.get_turn.return_value = "Blancas"
        self.assertFalse(self.interfaz.rendirse())

    @patch('builtins.input', side_effect=['2'])
    @patch('os.system')
    def test_mostrar_reglas(self, mock_os, mock_input):
        """Test para mostrar las reglas del __game__."""
        with patch('builtins.print') as mock_print:
            self.interfaz.mostrar_reglas()
            self.assertTrue(mock_print.called)
            self.assertIn("Reglas del __game__ de ajedrez", mock_print.call_args[0][0])

    @patch('builtins.input', side_effect=['3'])
    @patch('os.system')
    def __game__(self, mock_os, mock_input):
        """Test para la opción de salir del __game__."""
        with patch('builtins.print') as mock_print:
            self.interfaz.iniciar()  # Simula la salida del __game__
            self.assertIn("Saliendo de ChessGame", mock_print.call_args[0][0])


if __name__ == '__main__':
    unittest.main()
 