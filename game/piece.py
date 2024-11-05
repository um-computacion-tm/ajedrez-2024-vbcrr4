from typing import Tuple

class Piece:
    """
    Clase base para representar una pieza de ajedrez.

    Atributos:
        __color__ (str): Color de la pieza ('White' o 'Black').
        __position__ (tuple): Posición actual de la pieza en el tablero.
    """

    def __init__(self, color: str, position: Tuple[int, int]):
        """
        Inicializa una pieza de ajedrez con su color y posición.

        Args:
            color (str): Color de la pieza ('White' o 'Black').
            position (tuple): Posición inicial de la pieza en formato (fila, columna).
        """
        self.__color__ = color
        self.__position__ = position
    
    @property
    def color(self) -> str:
        """
        Devuelve el color de la pieza.

        Returns:
            str: Color de la pieza ('White' o 'Black').
        """
        return self.__color__
    
    @property
    def position(self) -> Tuple[int, int]:
        """
        Devuelve la posición actual de la pieza.

        Returns:
            tuple: Posición actual de la pieza en formato (fila, columna).
        """
        return self.__position__
    
    def update_position(self, position_new: Tuple[int, int]) -> None:
        """
        Actualiza la posición de la pieza.

        Args:
            position_new (tuple): Nueva posición en formato (fila, columna).
        """
        self.__position__ = position_new
    
    def __str__(self):
        """
        Representación en cadena de la pieza, usando un símbolo visual basado en el color.

        Returns:
            str: Símbolo de la pieza dependiendo de su color.
        """
        return self.__w_str__ if self.__color__ == "White" else self.__b_str__
    
    def piece_move(self, positions, position_new):
        """
        Verifica si el movimiento es válido para una pieza específica.
        
        Args:
            positions (list): Estado actual del tablero.
            position_new (tuple): Nueva posición a verificar.
        
        Returns:
            bool: True si el movimiento es válido (comportamiento predeterminado).
        """
        return True

    def get_cords(self, position_new):
        """
        Devuelve las coordenadas de inicio y fin en el formato necesario para el cálculo de movimiento.

        Args:
            position_new (tuple): Nueva posición en formato (fila, columna).

        Returns:
            tuple: Coordenadas de fila y columna para la posición actual y la posición nueva.
        """
        start_row, start_col = self.__position__
        end_row, end_col = position_new
        return start_row, start_col, end_row, end_col

    def is_path_clear(self, path, positions, row_step, col_step):
        """
        Verifica si el camino entre la posición inicial y la final está despejado.

        Args:
            path (tuple): Posiciones inicial y final en el formato ((start_row, start_col), (end_row, end_col)).
            positions (list): Estado actual del tablero.
            row_step (int): Incremento de fila para verificar cada paso en el camino.
            col_step (int): Incremento de columna para verificar cada paso en el camino.

        Returns:
            bool: True si el camino está despejado, False si hay una pieza bloqueando.
        """
        (start_row, start_col), (end_row, end_col) = path

        row, col = start_row, start_col
        for i in range(1, abs(end_row - start_row) + abs(end_col - start_col)):
            row += row_step
            col += col_step
            if positions[row][col] is not None:
                return False  # El camino no está despejado
        return True  # El camino está despejado

    def diagonal_move_positions(self, positions, position_new): 
        """
        Verifica si un movimiento diagonal es válido.

        Args:
            positions (list): Estado actual del tablero.
            position_new (tuple): Nueva posición a verificar.

        Returns:
            bool: True si el movimiento es diagonal y el camino está despejado, False en caso contrario.
        """
        start_row, start_col, end_row, end_col = self.get_cords(position_new)

        if abs(end_row - start_row) == abs(end_col - start_col):
            row_step = 1 if end_row > start_row else -1
            col_step = 1 if end_col > start_col else -1
            return self.is_path_clear(
                ((start_row, start_col), (end_row, end_col)), positions, row_step, col_step
            )

        return False

    def vertical_move_positions(self, positions, position_new):
        """
        Verifica si un movimiento vertical es válido.

        Args:
            positions (list): Estado actual del tablero.
            position_new (tuple): Nueva posición a verificar.

        Returns:
            bool: True si el movimiento es vertical y el camino está despejado, False en caso contrario.
        """
        start_row, start_col, end_row, end_col = self.get_cords(position_new)

        if end_row != start_row and end_col == start_col:
            row_step = 1 if end_row > start_row else -1
            return self.is_path_clear(
                ((start_row, start_col), (end_row, end_col)), positions, row_step, 0
            )
        
        return False
    
    def horizontal_move_positions(self, positions, position_new):
        """
        Verifica si un movimiento horizontal es válido.

        Args:
            positions (list): Estado actual del tablero.
            position_new (tuple): Nueva posición a verificar.

        Returns:
            bool: True si el movimiento es horizontal y el camino está despejado, False en caso contrario.
        """
        start_row, start_col, end_row, end_col = self.get_cords(position_new)

        if end_row == start_row and end_col != start_col:
            col_step = 1 if end_col > start_col else -1
            return self.is_path_clear(
                ((start_row, start_col), (end_row, end_col)), positions, 0, col_step
            )
        
        return False
