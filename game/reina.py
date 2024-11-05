from .piece import Piece

class Reina(Piece):
    """
    Representa una pieza de ajedrez de tipo Reina.

    Atributos:
        __w_str__ (str): Representación visual de la Reina blanca.
        __b_str__ (str): Representación visual de la Reina negra.
    """
    __w_str__ = "♛"
    __b_str__ = "♕"

    def __init__(self, color, position):
        """
        Inicializa un objeto Reina con un color y posición inicial.
        
        Args:
            color (str): Color de la pieza ('White' o 'Black').
            position (tuple): Posición inicial de la pieza.
        """
        super().__init__(color, position)

    def assign_value(self):
        """
        Asigna el valor de la pieza (9 para la Reina).
        
        Returns:
            int: Valor asignado a la Reina.
        """
        return 9
    
    def piece_move(self, positions, position_new):
        """
        Verifica si el movimiento es válido para la Reina.
        
        La Reina se mueve en líneas rectas horizontales, verticales o diagonales.
        
        Args:
            positions (list): Estado actual del tablero.
            position_new (tuple): Nueva posición a verificar.
        
        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        if (self.vertical_move_positions(positions, position_new) or 
            self.horizontal_move_positions(positions, position_new) or 
            self.diagonal_move_positions(positions, position_new)):
            return True
        return False



    