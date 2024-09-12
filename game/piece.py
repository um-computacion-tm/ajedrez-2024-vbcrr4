
class Piece():
    def __init__(self, color, position):
        self.__color__ = color
        self. __position__ = position
    @property
    def color(self):
        return self.__color__
    
    @property
    def position(self):
        return self.__position__
    
    def update_position(self, position_new):
        self.__position__ = position_new
    
    def __str__(self):
        return self.__w_str__ if self.__color__  ==  "white" else self.__b_str__
    
    def get_cords(self, position_new):
        end_row, end_col = position_new
        start_row, start_col = self.__position__
        return start_row, start_col, end_row, end_col
    
    def diagonal_move_positions(self, position_new, positions): 
        """
        Verifica si un movimiento diagonal es válido verificando el camino en el tablero.
        """
        start_row, start_col, end_row, end_col = self.get_cords(position_new)
        # Comprueba si el movimiento es diagonal
        if abs(end_row - start_row) == abs(end_col - start_col):
            row_step = 1 if end_row > start_row else -1  # Determina la dirección de la fila
            col_step = 1 if end_col > start_col else -1  # Determina la dirección de la columna

            # Recorre todas las posiciones entre la posición inicial y la final (sin incluir la final)
            for i in range(1, abs(end_row - start_row)):
                current_row = start_row + i * row_step
                current_col = start_col + i * col_step
                
                # Verifica si hay una pieza en el camino
                if positions[current_row][current_col] is not None:
                    return False  # El camino no está despejado
            return True  # El camino está despejado y el movimiento es válido

        return False
        
    def vertical_move_positions(self, position_new, positions):
        """
        Verifica si un movimiento vertical es válido verificando el camino en el tablero.
        """
        start_row, start_col, end_row, end_col = self.get_cords(position_new)

        if end_row != start_row and end_col == start_col:
            step = 1 if end_row > start_row else -1  # Determina la dirección del movimiento (hacia arriba o hacia abajo)

            # Recorre todas las posiciones entre la fila de inicio y la fila final (sin incluir la final)
            for i in range(1, abs(end_row - start_row)):
                if positions[start_row + i * step][start_col] is not None:
                    return False  # El camino no está despejado
            return True  # El camino está despejado y el movimiento es válido
        
        return False
    
    def horizontal_move_positions(self, position_new, positions):
        """
        Verifica si un movimiento horizontal es válido verificando el camino en el tablero.
        """
        start_row, start_col, end_row, end_col = self.get_cords(position_new)

        if end_row == start_row and end_col != start_col:
            step = 1 if end_col > start_col else -1  # Determina la dirección del movimiento (hacia la derecha o izquierda)
        # Recorre todas las posiciones entre la columna de inicio y la columna final (sin incluir la final)
            for i in range(1, abs(end_col - start_col)):
            # Verifica si hay una pieza en el camino
                if positions[end_row][start_col + i * step] is not None:
                    return False 
            return True  # El camino está despejado y el movimiento es válido
        
        return False
    