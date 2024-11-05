import unittest
from unittest.mock import patch, MagicMock
import sys
from io import StringIO
from game.cli import main, iniciar_juego

class TestChessCLI(unittest.TestCase):

    @patch('game.cli.Game')  # Mockear la clase Game
    def test_argument_parsing(self, MockGame):
        """Testea que el argumento `comando` acepte sólo el valor 'iniciar'."""
        test_args = ['cli.py', 'iniciar']
        with patch.object(sys, 'argv', test_args):
            with patch('game.cli.iniciar_juego') as mock_iniciar:
                main()
                mock_iniciar.assert_called_once()  # Asegurarse que iniciar_juego se llama con 'iniciar'

    @patch('builtins.input', side_effect=['A2', 'A4', 'Q'])  # Secuencia de inputs de usuario
    @patch('game.cli.Game')  # Mockear la clase Game
    def test_iniciar_juego_normal_play(self, MockGame, mock_input):
        """Simula un juego en el que el usuario realiza un movimiento y luego sale."""
        mock_game_instance = MockGame.return_value

        # Mockear métodos de la clase Game
        mock_game_instance.play.return_value = True  # Suponer que el movimiento es válido
        mock_game_instance.game_over.return_value = False  # No se termina hasta que se introduce 'Q'
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            iniciar_juego()
            output = fake_out.getvalue()

            # Validar llamadas clave
            mock_game_instance.show_board.assert_called()  # Tablero mostrado inicialmente y después de cada turno
            self.assertIn("Turno de las", output)
            mock_game_instance.play.assert_called_with(start_pos='A2', end_pos='A4')
            mock_game_instance.game_over.assert_called()

    @patch('builtins.input', side_effect=['A2', 'A11', 'Q'])  # Secuencia de inputs inválidos
    @patch('game.cli.Game')
    def test_iniciar_juego_invalid_input(self, Mock_Game, mock_input):
        """Simula entradas inválidas del usuario para verificar el manejo de errores."""
        mock_instance = Mock_Game

        # Asegurarse de que game_over devuelva False hasta que se envíe la entrada 'Q'
        mock_instance.game_over.side_effect = [False, False, True]

        with patch('sys.stdout', new=StringIO()) as false_out:
            iniciar_juego()
            salida = false_out.getvalue()

            # Validar mensajes de error y manejo de entradas inválidas
            self.assertIn("Entrada inválida en la posición final. Asegúrate de ingresar las posiciones en formato correcto (ej. A2, H8).", salida)
            mock_instance.play.assert_not_called()  # No debería intentar jugar con entrada inválida
            self.assertIn("Turno de las", salida)

    @patch('builtins.input', side_effect=['A11', 'A3', 'Q'])  # Secuencia de inputs inválidos
    @patch('game.cli.Game')
    def test_iniciar_juego_invalid_input2(self, MockGame, mock_input):
        """Simula entradas inválidas del usuario para verificar el manejo de errores."""
        mock_game_instance = MockGame.return_value

        # Asegurarse de que game_over devuelva False hasta que se envíe la entrada 'Q'
        mock_game_instance.game_over.side_effect = [False, False, True]

        with patch('sys.stdout', new=StringIO()) as fake_out:
            iniciar_juego()
            output = fake_out.getvalue()

            # Validar mensajes de error y manejo de entradas inválidas
            self.assertIn("Entrada inválida en la posición inicial. Asegúrate de ingresar las posiciones en formato correcto (ej. A2, H8).", output)
            mock_game_instance.play.assert_not_called()  # No debería intentar jugar con entrada inválida
            self.assertIn("Turno de las", output)
    @patch('builtins.input', side_effect=['Q'])
    @patch('game.cli.Game')
    def test_iniciar_juego_exit(self, MockGame, mock_input):
        """Simula la salida del juego con la entrada 'Q'."""
        mock_game_instance = MockGame.return_value

        with patch('sys.stdout', new=StringIO()) as fake_out:
            iniciar_juego()
            output = fake_out.getvalue()

            # Validar que se muestra el mensaje de salida
            self.assertIn("Saliendo del juego...", output)
            mock_game_instance.show_board.assert_called_once()  # Mostrar el tablero solo una vez al inicio
            mock_game_instance.play.assert_not_called()  # No debería intentar jugar si se elige 'Q'

if __name__ == '__main__':
    unittest.main()
