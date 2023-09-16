import unittest
import numpy as np
import C4_game

class TestGameStart(unittest.TestCase):
    def test_bottom_row_is_all_zeros_when_game_starts(self):
        board = np.zeros((6, 7))
        self.assertEqual(C4_game.next_free_row(board, 0), 0)
        self.assertEqual(C4_game.next_free_row(board, 1), 0)
        self.assertEqual(C4_game.next_free_row(board, 2), 0)
        self.assertEqual(C4_game.next_free_row(board, 3), 0)
        self.assertEqual(C4_game.next_free_row(board, 4), 0)
        self.assertEqual(C4_game.next_free_row(board, 5), 0)
        self.assertEqual(C4_game.next_free_row(board, 6), 0)

class TestFourInRow(unittest.TestCase):
    def test_four_chips_in_row_ends_the_game(self):
        board = np.zeros((6, 7))
        board[0][0] = 1
        board[0][1] = 1
        board[0][2] = 1
        board[0][3] = 1
        self.assertEqual(C4_game.check_if_4_in_row(board, 1), False)

    def test_four_chips_not_in_row_does_not_end_the_game(self):
        board = np.zeros((6, 7))
        board[0][0] = 1
        board[0][1] = 2  # this chip breaks the row
        board[0][2] = 1
        board[0][3] = 1
        self.assertEqual(C4_game.check_if_4_in_row(board, 1), True)

if __name__ == '__main__':
    unittest.main()