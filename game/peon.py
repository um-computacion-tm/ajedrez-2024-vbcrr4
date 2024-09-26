from .piece import Piece

class Peon(Piece):
    __w_str__ = "♙"
    __b_str__ = "♟"
    def __init__(self, color, position):
        super().__init__(color, position)

    def assign_value(self):
        return 1

    def es_movimiento_valido(self, position_new, positions):
        """Valida el movimiento de un peón."""
        if self.color == "blanco":
            return self._es_movimiento_valido_direccion(position_new, positions, -1, 6)
        elif self.color == "negro":
            return self._es_movimiento_valido_direccion(position_new, positions, 1, 1)
        return False

    def _es_movimiento_valido_direccion(self, position_new, positions, direccion, fila_inicial):
        """Valida el movimiento del peón dada una dirección."""
        start_row, start_col = self.__position__
        end_row, end_col = position_new

        if end_col == start_col:
            return self._es_movimiento_adelante(start_row, end_row, start_col, positions, direccion, fila_inicial)
        elif abs(end_col - start_col) == 1 and end_row == start_row + direccion:
            return self._es_movimiento_captura(end_row, end_col, positions)
        return False

    def _es_movimiento_adelante(self, start_row, end_row, start_col, positions, direccion, fila_inicial):
        """Valida el movimiento del peón hacia adelante."""
        if start_row == fila_inicial and end_row == start_row + 2 * direccion:
            return positions[start_row + direccion][start_col] is None and positions[end_row][start_col] is None
        elif end_row == start_row + direccion:
            return positions[end_row][start_col] is None
        return False

    def _es_movimiento_captura(self, end_row, end_col, positions):
        """Valida el movimiento de captura del peón."""
        return positions[end_row][end_col] is not None