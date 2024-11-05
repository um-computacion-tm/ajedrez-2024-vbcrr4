from .board import Board
from .exepciones import *
class Game:
    def __init__(self):
        self.__board__ = Board()
        self.__winner__ = None
        self.__turn__ = "White"

    def show_board(self):
        """
        Muestra el estado actual del tablero.
        """
        print(self.__board__)

    def play(self, start_pos, end_pos):
        """
        Controla el flujo principal de una jugada, verificando y ejecutando el movimiento.

        Args:
            start_pos (str): Posición inicial en formato textual (ej. 'A2').
            end_pos (str): Posición final en formato textual (ej. 'A3').

        Returns:
            bool: True si el movimiento fue exitoso, False en caso contrario.
        """
        if start_pos == "Q":
            return  # Salir del juego si el usuario elige 'Q' para finalizar

        try:
            if self.is_valid_move(start_pos, end_pos):
                self.execute_move(start_pos, end_pos)  # Ejecuta y procesa el movimiento
                return True  # Retornar éxito si el movimiento fue válido
            else:
                print(f"Movimiento inválido de {start_pos} a {end_pos}")
                return False
        except (InvalidMoveError, PieceNotFoundError, InvalidPieceMovement, CantEatKingError, InvalidInputError) as e:
            print(f"Error: {str(e)}")
            return False

    def execute_move(self, start_pos, end_pos):
        """
        Intenta ejecutar un movimiento en el tablero y cambia el turno si es exitoso.

        Args:
            start_pos (str): Posición inicial.
            end_pos (str): Posición final.
        """
        print(f"Intentando mover desde {start_pos} hasta {end_pos}")
        if self.perform_movement(start_pos, end_pos):
            self.switch_turn()
            #print(f"Turno cambiado a: {self.__turn__}")

    def perform_movement(self, start_pos, end_pos):
        """
        Realiza el movimiento traduciendo las posiciones de texto a coordenadas.

        Args:
            start_pos (str): Posición inicial.
            end_pos (str): Posición final.

        Returns:
            bool: True si el movimiento es válido.
        """
        try:
            start_coords = self.translate_position(start_pos)
            end_coords = self.translate_position(end_pos)

            # Verificar si la pieza en la posición de inicio pertenece al jugador en turno
            origin = self.get_own_piece(start_coords)
            
            # Mover la pieza en el tablero
            move_successful = self.__board__.move(origin, end_coords)

            # Validar si el movimiento es aceptable en el juego actual
            return self.validate_move_result(move_successful)

        except (InvalidMoveError, PieceNotFoundError, InvalidPieceMovement, CantEatKingError, ValueError, InvalidColorError) as e:
            print(f"Error: {str(e)}")
            raise

    def is_valid_move(self, start_pos, end_pos):
        """
        Verifica si un movimiento es legal y pertenece al jugador en turno.

        Args:
            start_pos (str): Posición inicial.
            end_pos (str): Posición final.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        try:
            start_coords = self.translate_position(start_pos)
            end_coords = self.translate_position(end_pos)

            if not self.__board__.validate_out_of_board(start_coords) or not self.__board__.validate_out_of_board(end_coords):
                print(f"error de afuera de los limites {self.__board__.validate_out_of_board(start_coords)}")
                return False

            piece = self.__board__.get_piece(*start_coords)
            if piece is None:
                return False

            target_piece = self.__board__.get_piece(*end_coords)
            if target_piece is not None and target_piece.color == piece.color:
                return False

            return True

        except InvalidInputError as e:
            print(f"Error en la entrada: {e}")
            return False

    def get_own_piece(self, coords):
        """
        Verifica si la pieza en la posición dada pertenece al jugador en turno.

        Args:
            coords (tuple): Coordenadas de la pieza.

        Returns:
            tuple: Coordenadas de la pieza si pertenece al jugador en turno.

        Raises:
            PieceNotFoundError: Si no hay una pieza en la posición dada.
            InvalidColorError: Si la pieza no pertenece al jugador en turno.
        """
        piece = self.__board__.get_piece(*coords)
        if piece is None:
            raise PieceNotFoundError("No hay ninguna pieza en la posición de origen.")

        if self.__turn__ != piece.color:
            raise InvalidColorError("No puedes mover una pieza de otro color.")
        
        return coords

    def validate_move_result(self, move_result):
        """
        Evalúa el estado del juego después de un movimiento.

        Args:
            move_result (bool): Resultado del intento de movimiento.

        Returns:
            bool | str: True si el juego continúa, de lo contrario, un mensaje de victoria o empate.
        """
        status = self.check_victory_status()
        if move_result:
            if status != "El juego continúa":
                return status
            return True
        return False

    def switch_turn(self):
        """
        Cambia el turno al jugador contrario.
        """
        self.__turn__ = "Black" if self.__turn__ == "White" else "White"

    def get_turn(self):
        """
        Devuelve el jugador en turno.
        """
        return self.__turn__
    def check_victory_status(self):
        """
        Verifica el estado de victoria del juego, evaluando condiciones de victoria y empate.

        Returns:
            str: Mensaje de estado de victoria o empate, o si el juego continúa.
        """
        pieces_count = self.__board__.count_pieces()

    
        if pieces_count[0] > 1 and pieces_count[1] < 2 and self.__turn__ == "Black":
            return "Ganan las Blancas"

        if pieces_count[1] > 1 and pieces_count[0] < 2 and self.__turn__ == "White":
            return "Ganan las Negras"

        if pieces_count[0] + pieces_count[1] == 2:
            return "Empate"
        
        return "El juego continúa."

    def game_over(self):
        """
        Verifica si el juego ha concluido.
        """
        return self.check_victory_status() != "El juego continúa."

    def translate_position(self, pos):
        """
        Traduce una posición en formato textual a coordenadas del tablero.

        Args:
            pos (str): Posición en formato de texto (ej. 'A2').

        Returns:
            tuple: Coordenadas correspondientes.

        Raises:
            InvalidInputError: Si la posición es inválida o está fuera de los límites.
        """
        pos = pos.strip().upper()
        if len(pos) != 2:
            raise InvalidInputError(f"Posición '{pos}' no válida")

        col_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        row_dict = {'8': 0, '7': 1, '6': 2, '5': 3, '4': 4, '3': 5, '2': 6, '1': 7}

        col = col_dict.get(pos[0])
        row = row_dict.get(pos[1])

        if col is None or row is None:
            raise InvalidInputError(f"Posición '{pos}' fuera de los límites")

        return (row, col)