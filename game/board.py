
from .torre import Torre
from .peon import Peon
from .alfil import Alfil
from .caballo import Caballo
from .reina import Reina
from .rey import Rey
from .piece import Piece
from .exepciones import * 
class Board:
    """
    Representa el tablero de ajedrez y maneja las posiciones de las piezas y las reglas básicas de movimiento.

    Atributos:
        __positions__ (list): Matriz 8x8 que almacena las posiciones de las piezas en el tablero.
    """
    def __init__(self):
        """
        Inicializa el tablero de ajedrez y coloca las piezas en sus posiciones iniciales.
        """
        self.__positions__ = []
        for fila in range(8):
            col = []
            for columna in range(8):
                col.append(None)
            self.__positions__.append(col)

        self.__positions__[0][0] = Torre("Black", (0, 0))
        self.__positions__[0][1] = Caballo("Black", (0, 1))
        self.__positions__[0][2] = Alfil("Black", (0, 2))
        self.__positions__[0][3] = Rey("Black", (0, 3))
        self.__positions__[0][4] = Reina("Black", (0, 4))
        self.__positions__[0][5] = Alfil("Black", (0, 5))
        self.__positions__[0][6] = Caballo("Black", (0, 6))
        self.__positions__[0][7] = Torre("Black", (0, 7))   

        for i in range(8):
            self.__positions__[1][i] = Peon("Black", (1, i))

        self.__positions__[7][0] = Torre("White", (7, 0))
        self.__positions__[7][1] = Caballo("White", (7, 1))
        self.__positions__[7][2] = Alfil("White", (7, 2))
        self.__positions__[7][3] = Rey("White", (7, 3))
        self.__positions__[7][4] = Reina("White", (7, 4))
        self.__positions__[7][5] = Alfil("White", (7, 5))
        self.__positions__[7][6] = Caballo("White", (7, 6))
        self.__positions__[7][7] = Torre("White", (7, 7))

        for i in range(8):
            self.__positions__[6][i] = Peon("White", (6, i))
    
    def get_piece(self, row, col):
        """
        Devuelve la pieza en una posición dada.

        Args:
            row (int): Fila de la posición.
            col (int): Columna de la posición.

        Returns:
            Piece | None: La pieza en la posición dada, o None si está vacía.
        """
        piece = self.__positions__[row][col]
        return piece
    
    def place_piece(self, row, col, piece):
        """
        Coloca una pieza en una posición específica.

        Args:
            row (int): Fila de la posición.
            col (int): Columna de la posición.
            piece (Piece): La pieza a colocar.
        """
        self.__positions__[row][col] = piece

    def search_piece(self, piece):
        """
        Busca la posición de una pieza específica en el tablero.

        Args:
            piece (Piece): La pieza a buscar.

        Returns:
            tuple | None: Coordenadas de la pieza o None si no se encuentra.
        """
        if piece is not None:
            for row in range(8):
                for col in range(8):
                    if self.__positions__[row][col] == piece:
                        return (row, col)
            return None
        else:
            return None
    
    def color_pieces(self, row, col):
        """
        Devuelve el color de la pieza en una posición dada.

        Args:
            row (int): Fila de la posición.
            col (int): Columna de la posición.

        Returns:
            str | Exception: El color de la pieza o un error si no hay pieza.
        """
        piece = self.get_piece(row, col)
        if piece is None:
            return PieceNotFoundError("No hay ninguna pieza en la posición de origen.")
        return piece.color
        
    def validate_out_of_board(self, position):
        """
        Verifica si una posición está dentro del tablero.

        Args:
            position (tuple): Posición a verificar.

        Returns:
            bool: True si la posición está dentro del tablero, False en caso contrario.
        """
        row, col = position
        return 0 <= row < 8 and 0 <= col < 8
    def move(self, origen, destino):
        """
        Intenta mover una pieza de una posición origen a una posición destino.

        Args:
            origen (tuple): Posición de inicio.
            destino (tuple): Posición final.

        Returns:
            bool: True si el movimiento es exitoso.

        Raises:
            PieceNotFoundError: Si no hay ninguna pieza en origen.
            InvalidMoveError: Si el movimiento es inválido.
            CantEatKingError: Si se intenta capturar al rey.
        """
        try:
            # Verifica si las posiciones de origen y destino están dentro del tablero
            if not self.validate_out_of_board(origen):
                raise InvalidMoveError(f"El origen {origen} está fuera del tablero.")
            if not self.validate_out_of_board(destino):
                raise InvalidMoveError(f"El destino {destino} está fuera del tablero.")

            #print(f"Metodo move:Intentando mover pieza desde {origen} hasta {destino}")
            self.can_move(origen, destino)
            self.execute_move(origen, destino)
            return True
        except PieceNotFoundError as e:
            print(f"Error: {e}")
            raise
        except InvalidPieceMovement as e:
            print(f"Error: {e}")
            raise
        except InvalidMoveError as e:
            print(f"Error: {e}")
            raise 
        except CantEatKingError as e:
            print(f"Error: {e}")
            raise


    def can_move(self, origen, destino):
        """
        Verifica si una pieza puede moverse de origen a destino.

        Args:
            origen (tuple): Posición de inicio.
            destino (tuple): Posición final.

        Raises:
            InvalidMoveError: Si el destino tiene una pieza del mismo color.
            InvalidPieceMovement: Si el movimiento no es válido para la pieza.
        """
        row, col = origen
        origen_piece = self.get_piece(row, col)
        destino_piece = self.get_piece(destino[0], destino[1])
    
        #print(f"Verificando movimiento de {origen_piece} desde {origen} a {destino}")
        if origen_piece is None:
            raise PieceNotFoundError("No hay ninguna pieza en la posición de origen. (board)")
        
        # Verifica si el movimiento es válido
        if not self.is_valid_move(origen, destino):
            raise InvalidPieceMovement(f"Movimiento de pieza inválido {origen_piece}, el camino no está despejado {destino_piece} o el movimiento no es válido.(board)")
        
        # Verifica si hay una pieza en el destino que sea del mismo color
        if destino_piece is not None and origen_piece.color == destino_piece.color:
            raise InvalidMoveError("No puedes moverte donde tienes otra pieza del mismo color.(board)")
    
    def is_valid_move(self, origen, destino):
        """
        Verifica si un movimiento es válido, incluyendo todas las restricciones de la pieza y del tablero.

        Args:
            origen (tuple): Posición inicial de la pieza.
            destino (tuple): Posición de destino.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        # Verifica si las posiciones de origen y destino están dentro del tablero
        if not self.validate_out_of_board(origen):
            raise InvalidMoveError(f"El origen {origen} está fuera del tablero.")
        if not self.validate_out_of_board(destino):
            raise InvalidMoveError(f"El destino {destino} está fuera del tablero.")

        # Obtiene las piezas de origen y destino
        origen_piece = self.get_piece(origen[0], origen[1])
        destino_piece = self.get_piece(destino[0], destino[1])

        # Verifica que exista una pieza en el origen
        if origen_piece is None:
            raise PieceNotFoundError("No hay ninguna pieza en la posición de origen.")

        # Verifica si el tipo de movimiento es válido para la pieza de origen
        if not origen_piece.piece_move(self.__positions__, destino):
            raise InvalidPieceMovement("Movimiento de pieza inválido.")

        # Verifica si hay una pieza en el destino que sea del mismo color
        if destino_piece is not None and origen_piece.color == destino_piece.color:
            raise InvalidMoveError("No puedes moverte donde tienes otra pieza del mismo color.")
        
        #Verifica si el destino es el rey oponente (no se puede capturar al rey)
        if isinstance(destino_piece, Rey):
            raise CantEatKingError("No puedes capturar al rey del oponente.")

        # Si pasa todas las verificaciones, el movimiento es válido
        return True

    def execute_move(self, origen, destino):
        """
        Ejecuta el movimiento de una pieza desde origen hasta destino.

        Args:
            origen (tuple): Posición de inicio.
            destino (tuple): Posición final.

        Raises:
            PieceNotFoundError: Si no hay ninguna pieza en la posición origen.
        """
        # Obtiene la pieza en la posición de origen
        pieza_origen = self.get_piece(origen[0], origen[1])
        
        if pieza_origen is None:
            raise PieceNotFoundError(f"No hay ninguna pieza en {origen}.")
        # Obtiene la pieza en la posición de destino (si existe)
        pieza_destino = self.get_piece(destino[0], destino[1])
        # Actualiza la posición de la pieza de origen en el tablero
        self.place_piece(destino[0], destino[1], pieza_origen)
        self.place_piece(origen[0], origen[1], None)  # Vacía la posición de origen
        # Actualiza la posición interna de la pieza de origen
        pieza_origen.update_position(destino)
        #verificar el si se esta llamando a update position
        # Si hay una pieza en el destino (es decir, fue capturada), actualizar su posición
        if pieza_destino is not None:
            pieza_destino.update_position(None)

    def __repr__(self):
        spaces = " " * 3
        horizontal_line = spaces + "┌" + "───────┬" * 7 + "───────┐" + "\n"
        middle_horizontal_line = spaces + "├" + "───────┼" * 7 + "───────┤" + "\n"
        bottom_horizontal_line = spaces + "└" + "───────┴" * 7 + "───────┘"
    
        # Agregamos la fila superior con las etiquetas de columnas
        board_repr = "  " * 3 + "       ".join([chr(i) for i in range(ord('a'), ord('h')+1)]) + "\n"
        board_repr += horizontal_line

        for i in range(8):
            board_repr += f"  {8 - i}│"
            for j in range(8):
                cell = self.__positions__[i][j]
                if cell is None:
                # Si la celda está vacía, representamos como 'None'
                    cell_repr = " ".center(7)
                else:
                # Si hay una pieza, usamos su método __str__()
                    cell_repr = str(cell).center(7)  
                board_repr += f"{cell_repr}│"
            board_repr += f"  {8 - i}\n"
            if i != 7:
                board_repr += middle_horizontal_line

        # Agregamos la fila inferior con las etiquetas de columnas
        board_repr += bottom_horizontal_line + "\n" + "  " * 3 + "       ".join([chr(i) for i in range(ord('a'), ord('h')+1)])
        return board_repr

    def reset_board(self):
        """
        Restablece el tablero eliminando todas las piezas.
        """
        for row in range(8):
            for col in range(8):
                self.__positions__[row][col] = None

    def count_pieces(self):
        """
        Cuenta el número de piezas de cada color en el tablero.

        Returns:
            tuple: Número de piezas blancas y negras.
        """
        white_pieces = 0
        black_pieces = 0
        for row in range(8):
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece is not None:
                    if piece.color == "White":
                        white_pieces += 1
                    else:
                        black_pieces += 1
        return (white_pieces, black_pieces)

    
    