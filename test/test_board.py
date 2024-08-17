import unittest
from game.board import Board

class TestBoard(unittest.TestCase):
    def test_board_initialization(self):
        board = Board()
        self.assertEqual(board.board[0], ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'])
        self.assertEqual(board.board[1], ['P' for _ in range(8)])
        self.assertEqual(board.board[6], ['p' for _ in range(8)])
        self.assertEqual(board.board[7], ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'])

    def test_board_repr(self):
        board = Board()
        expected_board = """     a      b      c      d      e      f      g      h
   ┌───────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┐
8  │   R   │  N   │  B   │  Q   │  K   │  B   │  N   │  R   │ 8
   ├───────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
7  │   P   │  P   │  P   │  P   │  P   │  P   │  P   │  P   │ 7
   ├───────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
6  │       │      │      │      │      │      │      │      │ 6
   ├───────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
5  │       │      │      │      │      │      │      │      │ 5
   ├───────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
4  │       │      │      │      │      │      │      │      │ 4
   ├───────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
3  │       │      │      │      │      │      │      │      │ 3
   ├───────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
2  │   p   │  p   │  p   │  p   │  p   │  p   │  p   │  p   │ 2
   ├───────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
1  │   r   │  n   │  b   │  q   │  k   │  b   │  n   │  r   │ 1
   └───────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┘
     a      b      c      d      e      f      g      h"""
        self.assertEqual(repr(board), expected_board)

if __name__ == "__main__":
    unittest.main()
