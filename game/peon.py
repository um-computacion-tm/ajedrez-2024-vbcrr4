from .piece import Piece

class Peon(Piece):
    """
    Representa una pieza de ajedrez de tipo Peón.

    Atributos:
        __w_str__ (str): Representación visual del Peón blanco.
        __b_str__ (str): Representación visual del Peón negro.
    """
    __w_str__ = "♟"
    __b_str__ = "♙"

    def __init__(self, color, position):
        """
        Inicializa un objeto Peón con un color y posición inicial.
        
        Args:
            color (str): Color de la pieza ('White' o 'Black').
            position (tuple): Posición inicial de la pieza.
        """
        super().__init__(color, position)

    def assign_value(self):
        """
        Asigna el valor de la pieza (1 para el Peón).
        
        Returns:
            int: Valor asignado al Peón.
        """
        return 1

    def piece_move(self, positions, position_new):
        """
        Verifica si el movimiento es válido para el Peón.
        
        Args:
            positions (list): Estado actual del tablero.
            position_new (tuple): Nueva posición a verificar.
        
        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        if self.__color__ == "White":
            return self.valid_white_move(positions, position_new)
        elif self.__color__ == "Black":
            return self.valid_black_move(positions, position_new)
        return False

    def valid_black_move(self, positions, position_new):
        """
        Valida el movimiento para un Peón negro.
        
        Args:
            positions (list): Estado actual del tablero.
            position_new (tuple): Nueva posición a verificar.
        
        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        return self.is_valid_move(positions, position_new, 1, 1)
    
    def valid_white_move(self, positions, position_new):
        """
        Valida el movimiento para un Peón blanco.
        
        Args:
            positions (list): Estado actual del tablero.
            position_new (tuple): Nueva posición a verificar.
        
        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        return self.is_valid_move(positions, position_new, -1, 6)

    def is_valid_move(self, positions, position_new, direction, initial_row):
        """
        Verifica si el movimiento es válido dependiendo de la dirección y fila inicial.
        
        Args:
            positions (list): Estado actual del tablero.
            position_new (tuple): Nueva posición a verificar.
            direction (int): Dirección de movimiento (1 para negro, -1 para blanco).
            initial_row (int): Fila inicial para permitir un movimiento de dos pasos.
        
        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        start_row, start_col = self.position
        end_row, end_col = position_new
        result = False

        # Movimiento vertical
        if start_col == end_col:
            if start_row + direction == end_row and positions[end_row][end_col] is None:
                result = True
            elif start_row == initial_row and start_row + 2 * direction == end_row and positions[start_row + direction][start_col] is None and positions[end_row][end_col] is None:
                result = True
        elif abs(start_col - end_col) == 1 and start_row + direction == end_row and positions[end_row][end_col] is not None:
            result = True

        return result

    def move(self, positions, position_new, direction):
        """
        Realiza el movimiento de una casilla hacia adelante.
        
        Args:
            positions (list): Estado actual del tablero.
            position_new (tuple): Nueva posición a verificar.
            direction (int): Dirección de movimiento.
        
        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        start_row, start_col = self.position
        end_row, end_col = position_new

        if start_row + direction == end_row and positions[end_row][end_col] is None:
            return True
        return False

