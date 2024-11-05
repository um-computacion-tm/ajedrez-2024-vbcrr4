from .piece import Piece

class Caballo(Piece):
    """
    Representa una pieza de ajedrez de tipo Caballo.

    Atributos:
        __w_str__ (str): Representación visual del Caballo blanco.
        __b_str__ (str): Representación visual del Caballo negro.
    """
    __w_str__ = "♞"
    __b_str__ = "♘"

    def __init__(self, color, position):
        """
        Inicializa un objeto Caballo con un color y posición inicial.
        
        Args:
            color (str): Color de la pieza ('White' o 'Black').
            position (tuple): Posición inicial de la pieza.
        """
        super().__init__(color, position)

    def assign_value(self):
        """
        Asigna el valor de la pieza (3 para el Caballo).
        
        Returns:
            int: Valor asignado al Caballo.
        """
        return 3

    def is_valid_move(self, row_diff, col_diff):
        """
        Verifica si las diferencias de filas y columnas corresponden 
        a un movimiento en 'L' del Caballo.
        
        Args:
            row_diff (int): Diferencia de filas.
            col_diff (int): Diferencia de columnas.
        
        Returns:
            bool: True si es un movimiento válido, False en caso contrario.
        """
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)

    def is_valid_destination(self, end_row, end_col, positions):
        """
        Verifica si la casilla de destino está vacía o tiene una pieza del color contrario.
        
        Args:
            end_row (int): Fila de destino.
            end_col (int): Columna de destino.
            positions (list): Estado actual del tablero.
        
        Returns:
            bool: True si el destino es válido, False en caso contrario.
        """
        destination_piece = positions[end_row][end_col]
        return destination_piece is None or destination_piece.color != self.color

    def piece_move(self, positions, position_new):
        """
        Verifica si el movimiento es válido para el Caballo.

        Args:
            positions (list): Representación actual del tablero.
            position_new (tuple): Nueva posición a verificar.
            
        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        start_row, start_col, end_row, end_col = self.get_cords(position_new)
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)

        if self.is_valid_move(row_diff, col_diff) and self.is_valid_destination(end_row, end_col, positions):
            return True
        return False

     
