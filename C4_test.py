import unittest
import numpy as np
import C4_game

# run the tests with command: python3 -m unittest -v C4_test.py

class TestGameStart(unittest.TestCase):
    def test_bottom_row_is_all_zeros_when_game_starts(self):
        """ Test that the bottom row has all zeros when game starts """
        board = np.zeros((6, 7))
        self.assertEqual(C4_game.next_free_row(board, 0), 0)
        self.assertEqual(C4_game.next_free_row(board, 1), 0)
        self.assertEqual(C4_game.next_free_row(board, 2), 0)
        self.assertEqual(C4_game.next_free_row(board, 3), 0)
        self.assertEqual(C4_game.next_free_row(board, 4), 0)
        self.assertEqual(C4_game.next_free_row(board, 5), 0)
        self.assertEqual(C4_game.next_free_row(board, 6), 0)

    def test_who_starts_the_game_text_is_generated(self): # fix this
        """ Test that the You start or AI starts text is visible when game starts """
        board = np.zeros((6, 7))
        self.assertEqual(C4_game.game_start_text(), None)

    def test_all_columns_free_when_game_starts(self):
        """ Should return [0,1,2,3,4,5,6] as free columns """
        board = np.zeros((6, 7))
        self.assertEqual(C4_game.all_free_columns(board), [0,1,2,3,4,5,6])

class TestTurnChanges(unittest.TestCase):
    def turn_changes_from_1_to_2(self):
        """ Test that turn changes from human(1) to AI(2) """
        board = np.zeros((6, 7))
        self.assertEqual(C4_game.drop_chip(board, 0, 0, 1), 2)

    def turn_changes_from_2_to_1(self):
        """ Test that turn changes from AI(2) to human(1) """
        board = np.zeros((6, 7))
        self.assertEqual(C4_game.drop_chip(board, 0, 0, 2), 1)

class TestFourInRow(unittest.TestCase):
    def test_four_chips_in_row_ends_the_game(self):
        """ Test that 4 chips in row ends the game """
        board = np.zeros((6, 7))
        board[0][0] = 1
        board[0][1] = 1
        board[0][2] = 1
        board[0][3] = 1
        self.assertFalse(C4_game.check_if_game_active(board, 1), False)

    def test_four_chips_in_column_ends_the_game(self):
        """ Test that 4 chips in column ends the game """
        board = np.zeros((6, 7))
        board[0][1] = 1
        board[1][1] = 1
        board[2][1] = 1
        board[3][1] = 1
        self.assertFalse(C4_game.check_if_game_active(board, 1), False)

    def test_four_chips_in_positive_diagonal_ends_the_game(self):
        """ Test that 4 chips in positive diagonal ends the game """
        board = np.zeros((6, 7))
        board[0][0] = 1
        board[1][1] = 1
        board[2][2] = 1
        board[3][3] = 1
        self.assertFalse(C4_game.check_if_game_active(board, 1), False)

    def test_four_chips_in_negative_diagonal_ends_the_game(self):
        """ Test that 4 chips in negative diagonal ends the game """
        board = np.zeros((6, 7))
        board[5][0] = 1
        board[4][1] = 1
        board[3][2] = 1
        board[2][3] = 1
        self.assertFalse(C4_game.check_if_game_active(board, 1), False)

    def test_four_chips_of_both_players_in_row_does_not_end_the_game(self):
        """ Test that 4 chips of both players in row continues the game """
        board = np.zeros((6, 7))
        board[0][0] = 1
        board[0][1] = 2  # this chip breaks the row
        board[0][2] = 1
        board[0][3] = 1
        self.assertTrue(C4_game.check_if_game_active(board, 1), True)

class TestFreeColumns(unittest.TestCase):
    def should_show_7_free_columns(self):
        """ Test that all 7 columns free when game starts """
        board = np.zeros((6, 7))
        self.asserEqual(C4.game.all_free_columns(board), [0,1,2,3,4,5,6])

    def should_show_6_free_columns(self):
        """ Test that 6 columns are free when column 2 is full """
        board = np.zeros((6, 7))
        board[2][0] = 1
        board[2][1] = 2
        board[2][2] = 1
        board[2][3] = 2
        board[2][4] = 1
        board[2][5] = 2
        board[2][6] = 1
        self.asserEqual(C4.game.all_free_columns(board), [0,1,3,4,5,6])

if __name__ == '__main__':
    unittest.main()
