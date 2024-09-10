from .piece import Piece

class Peon(Piece):
    __w_str__ = "♙"
    __b_str__ = "♟"
    def __init__(self, color, position):
        super().__init__(color, position)

    def assign_value(self):
        return 1

    def es_movimiento_valido(self, position_new, positions):
        # Si es blanco, se mueve hacia arriba, si es negro, hacia abajo
        if self.color == "blanco":
            return self._es_movimiento_valido_blanco(position_new, positions)
        elif self.color == "negro":
            return self._es_movimiento_valido_negro(position_new, positions)
        return False

    def _es_movimiento_valido_blanco(self, position_new, positions):
        # Los peones blancos se mueven hacia arriba en el tablero
        return self._es_movimiento_valido_peon(position_new, positions, -1, 6)

    def _es_movimiento_valido_negro(self, position_new, positions):
        # Los peones negros se mueven hacia abajo en el tablero
        return self._es_movimiento_valido_peon(position_new, positions, 1, 1)

    def _es_movimiento_valido_peon(self, position_new, positions, direccion, fila_inicial):
        start_row, start_col = self.__position__
        end_row, end_col = position_new

        # Movimiento hacia adelante en la misma columna
        if end_col == start_col:
            # Movimiento inicial: puede avanzar dos casillas
            if start_row == fila_inicial and end_row == start_row + 2 * direccion:
                if positions[start_row + direccion][start_col] is None and positions[end_row][end_col] is None:
                    return True
            # Movimiento normal de una casilla hacia adelante
            elif end_row == start_row + direccion and positions[end_row][end_col] is None:
                return True

        # Movimiento de captura en diagonal
        elif end_row == start_row + direccion and abs(end_col - start_col) == 1 and positions[end_row][end_col] is not None:
            return True

        return False