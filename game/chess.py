from board import Board

class Chess:
    def __init__(self):
        self.board = Board()
        self.turn = "w"        
    def move(self, from_row, from_col, to_row, to_col):
        self.board.move(from_row, from_col, to_row, to_col)
        self.turn = "b" if self.turn == "w" else "w"