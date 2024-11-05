from .piece import Piece

class Alfil(Piece):
    """
    Representa una pieza de ajedrez de tipo Alfil.

    Atributos:
        __w_str__ (str): Representación visual del Alfil blanco.
        __b_str__ (str): Representación visual del Alfil negro.
    """
    __w_str__ = "♝"
    __b_str__ = "♗"

    def __init__(self, color, positions):
        """
        Inicializa un objeto Alfil con un color y posición inicial.
        
        Args:
            color (str): Color de la pieza ('White' o 'Black').
            positions (tuple): Posición inicial de la pieza.
        """
        super().__init__(color, positions)

    def assign_value(self):
        """
        Asigna el valor de la pieza (3 para el Alfil).
        
        Returns:
            int: Valor asignado al Alfil.
        """
        return 3
  
    def piece_move(self, positions, position_new):
        """
        Verifica si el movimiento es válido para el Alfil.
        
        El Alfil se mueve en líneas diagonales.
        
        Args:
            positions (list): Representación actual del tablero.
            position_new (tuple): Posición de destino.
            
        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        if self.diagonal_move_positions(positions, position_new):
            return True
        return False

    