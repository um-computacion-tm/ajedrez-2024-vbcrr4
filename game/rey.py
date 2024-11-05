from .piece import Piece

class Rey(Piece):
    """
    Representa una pieza de ajedrez de tipo Rey.

    Atributos:
        __w_str__ (str): Representación visual del Rey blanco.
        __b_str__ (str): Representación visual del Rey negro.
    """
    __b_str__ = "♔"
    __w_str__ = "♚"

    def __init__(self, color, position):
        """
        Inicializa un objeto Rey con un color y posición inicial.
        
        Args:
            color (str): Color de la pieza ('White' o 'Black').
            position (tuple): Posición inicial de la pieza.
        """
        super().__init__(color, position)

    def assign_value(self):
        """
        Asigna el valor de la pieza (1000 para el Rey, debido a su importancia en el juego).
        
        Returns:
            int: Valor asignado al Rey.
        """
        return 1000
    
    def piece_move(self, positions, position_new):
        """
        Verifica si un movimiento es válido para el Rey.
        
        El Rey puede moverse una casilla en cualquier dirección, siempre que no termine 
        en una posición ocupada por una pieza del mismo color.
        
        Args:
            positions (list): Estado actual del tablero.
            position_new (tuple): Nueva posición a verificar.
        
        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        start_row, start_col, end_row, end_col = self.get_cords(position_new)
        
        if abs(end_row - start_row) <= 1 and abs(end_col - start_col) <= 1:
            destination_piece = positions[end_row][end_col]
            if destination_piece is None or destination_piece.color != self.color:
                return True
        return False

