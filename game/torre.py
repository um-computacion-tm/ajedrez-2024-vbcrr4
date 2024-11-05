from .piece import Piece

class Torre(Piece):
    """
    Representa una pieza de ajedrez de tipo Torre.

    Atributos:
        __w_str__ (str): Representación visual de la Torre blanca.
        __b_str__ (str): Representación visual de la Torre negra.
    """
    __w_str__ = "♜"
    __b_str__ = "♖"

    def __init__(self, color, position):
        """
        Inicializa un objeto Torre con un color y posición inicial.
        
        Args:
            color (str): Color de la pieza ('White' o 'Black').
            position (tuple): Posición inicial de la pieza.
        """
        super().__init__(color, position)

    def assign_value(self):
        """
        Asigna el valor de la pieza (5 para la Torre).
        
        Returns:
            int: Valor asignado a la Torre.
        """
        return 5

    def piece_move(self, positions, position_new):
        """
        Verifica si el movimiento es válido para la Torre.
        
        La Torre se mueve en líneas rectas horizontales o verticales.
        
        Args:
            positions (list): Estado actual del tablero.
            position_new (tuple): Nueva posición a verificar.
        
        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        if self.vertical_move_positions(positions, position_new) or self.horizontal_move_positions(positions, position_new):
            return True
        return False
