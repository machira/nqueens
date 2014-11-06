__author__ = 'machira'

import unittest
import Nqueens

class NQueensTests(unittest.TestCase):
    board = []
    board_size = 8

    def test_alldiff(self):
        # real solution has all columns being different
        self.assertEqual(len(self.board),len(set(self.board)))

    def test_diagonals(self):


        self.assertEqual(True, False)

    def setUp(self):
        board = Nqueens.initialise(board_size=self.board_size)
        new_board, is_solved = Nqueens.solve(board)

        # find a solution
        while not is_solved:
            new_board, is_solved = Nqueens.solve(board)

        self.board = new_board

if __name__ == '__main__':
    unittest.main()
