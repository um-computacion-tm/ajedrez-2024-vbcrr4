from .piece import Piece

class Peon(Piece):
    __w_str__ = "♙"
    __b_str__ = "♟"
    def __init__(self, color, position):
        super().__init__(color, position)

    def assign_value(self):
        return 1

    def validar_movimiento(self, positions, position_new):
        """Verifica si el movimiento del soldado es válido."""
        if self.color == "white":
            return self._validar_movimiento_peon(positions, position_new, -1, 6)
        elif self.color == "black":
            return self._validar_movimiento_peon(positions, position_new, 1, 1)
        return False

    def _validar_movimiento_peon(self, positions, position_new, direction, fila_inicial):
        """Valida el movimiento del peón tanto en captura como en avance."""
        fila_actual, columna_actual = self.__position__
        nueva_fila, nueva_columna = position_new

        # Movimiento hacia adelante en la misma columna
        if columna_actual == nueva_columna:
            # Si es el primer movimiento del peón, puede avanzar dos casillas
            if fila_actual == fila_inicial and nueva_fila == fila_actual + 2 * direction:
                return positions[fila_actual + direction][columna_actual] is None and positions[nueva_fila][columna_actual] is None
            # Movimiento normal de una casilla hacia adelante
            elif nueva_fila == fila_actual + direction:
                return positions[nueva_fila][columna_actual] is None

        # Movimiento de captura en diagonal
        elif abs(nueva_columna - columna_actual) == 1 and nueva_fila == fila_actual + direction:
            return positions[nueva_fila][nueva_columna] is not None

        return False


