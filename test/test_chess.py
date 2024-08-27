import unittest
from game.chess import Chess

class TestChess(unittest.TestCase):
    def setUp(self):
        self.__juego__ = Chess()

    def test_display_board(self):
        self.assertEqual(self.__juego__.display_board(), self.__juego__.__board__)

    def test_cambio_turno(self):
        self.assertEqual(self.__juego__.cambio_turno(), 'white')    
