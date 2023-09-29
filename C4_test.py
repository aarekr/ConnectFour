import unittest
import numpy as np
import C4_game

# run the tests with command: python3 -m unittest -v C4_test.py

class TestGameStart(unittest.TestCase):
    def test_create_game_board_function_returns_valid_game_board(self):
        """ Test that create_game_board() function returns the valid game board """
        board_right_shape = np.zeros((6, 7), dtype = int)
        self.assertEqual(C4_game.create_game_board(6, 7).shape, board_right_shape.shape)

    def test_bottom_row_is_all_zeros_when_game_starts(self):
        """ Test that the bottom row has all zeros when game starts """
        board = np.zeros((6, 7), dtype = int)
        self.assertEqual(C4_game.next_free_row(board, 0), 0)
        self.assertEqual(C4_game.next_free_row(board, 1), 0)
        self.assertEqual(C4_game.next_free_row(board, 2), 0)
        self.assertEqual(C4_game.next_free_row(board, 3), 0)
        self.assertEqual(C4_game.next_free_row(board, 4), 0)
        self.assertEqual(C4_game.next_free_row(board, 5), 0)
        self.assertEqual(C4_game.next_free_row(board, 6), 0)

    def test_who_starts_the_game_text_is_generated(self):
        """ Test that the You start or AI starts text is visible when game starts """
        board = np.zeros((6, 7), dtype = int)
        # who_starts or label has to be tested somehow, returns None at the moment
        self.assertEqual(C4_game.game_start_text(), None)

    def test_all_columns_free_when_game_starts(self):
        """ Should return [0,1,2,3,4,5,6] as free columns """
        board = np.zeros((6, 7), dtype = int)
        self.assertEqual(C4_game.all_free_columns(board), [0,1,2,3,4,5,6])
    
    def test_print_board_functionality(self):
        """ Testing that print_board() function exists and responds.
            Does not have any return value. """
        board = np.zeros((6, 7), dtype = int)
        self.assertEqual(C4_game.print_board(board), None)

class TestFourInRow(unittest.TestCase):
    def test_four_chips_in_row_ends_the_game(self):
        """ Test that 4 chips in row ends the game """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 1
        board[0][1] = 1
        board[0][2] = 1
        board[0][3] = 1
        self.assertFalse(C4_game.check_if_game_active(board, 1), False)

    def test_four_chips_in_column_ends_the_game(self):
        """ Test that 4 chips in column ends the game """
        board = np.zeros((6, 7), dtype = int)
        board[0][1] = 1
        board[1][1] = 1
        board[2][1] = 1
        board[3][1] = 1
        self.assertFalse(C4_game.check_if_game_active(board, 1), False)

    def test_four_chips_in_positive_diagonal_ends_the_game(self):
        """ Test that 4 chips in positive diagonal ends the game """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 1
        board[1][1] = 1
        board[2][2] = 1
        board[3][3] = 1
        self.assertFalse(C4_game.check_if_game_active(board, 1), False)

    def test_four_chips_in_negative_diagonal_ends_the_game(self):
        """ Test that 4 chips in negative diagonal ends the game """
        board = np.zeros((6, 7), dtype = int)
        board[5][0] = 1
        board[4][1] = 1
        board[3][2] = 1
        board[2][3] = 1
        self.assertFalse(C4_game.check_if_game_active(board, 1), False)

    def test_four_chips_of_both_players_in_row_does_not_end_the_game(self):
        """ Test that 4 chips of both players in a row continues the game """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 1
        board[0][1] = 2  # this chip breaks the row
        board[0][2] = 1
        board[0][3] = 1
        self.assertTrue(C4_game.check_if_game_active(board, 1), True)

class TestTurnChanges(unittest.TestCase):
    def test_turn_changes_from_1_to_2(self):
        """ Test that turn changes from human(1) to AI(2) """
        board = np.zeros((6, 7), dtype = int)
        self.assertEqual(C4_game.drop_chip(board, 0, 0, 1), 2)

    def test_turn_changes_from_2_to_1(self):
        """ Test that turn changes from AI(2) to human(1) """
        board = np.zeros((6, 7), dtype = int)
        self.assertEqual(C4_game.drop_chip(board, 0, 0, 2), 1)

class TestFreeRows(unittest.TestCase):
    def test_row_3_is_free_when_3_chips_dropped(self):
        """ Test that row 3 is free when 3 chips dropped in that column """
        board = np.zeros((6, 7), dtype = int)
        board[0][5] = 1
        board[1][5] = 2
        board[2][5] = 1
        self.assertEqual(C4_game.next_free_row(board, 5), 3)
    
    def test_no_free_rows_when_column_full(self):
        """ Test that no free rows when all 6 slots full in that column """
        board = np.zeros((6, 7), dtype = int)
        board[0][6] = 1
        board[1][6] = 2
        board[2][6] = 1
        board[3][6] = 2
        board[4][6] = 1
        board[5][6] = 2
        self.assertEqual(C4_game.next_free_row(board, 6), -1)

class TestFreeColumns(unittest.TestCase):
    def test_should_show_6_free_columns(self):
        """ Test that 6 columns are free when 1 column (#2) is full """
        board = np.zeros((6, 7), dtype = int)
        board[0][2] = 1
        board[1][2] = 2
        board[2][2] = 1
        board[3][2] = 2
        board[4][2] = 1
        board[5][2] = 2
        self.assertEqual(C4_game.all_free_columns(board), [0,1,3,4,5,6])
    
    def test_free_columns_when_1_row_is_full(self):
        """ Test that all columns are free when row 0 is full """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 1
        board[0][1] = 2
        board[0][2] = 1
        board[0][3] = 2
        board[0][4] = 1
        board[0][5] = 2
        board[0][6] = 1
        self.assertEqual(C4_game.all_free_columns(board), [0,1,2,3,4,5,6])

class TestTerminalNode(unittest.TestCase):
    # chip_count = 42 test has to be added
    
    def test_terminal_node_is_True_when_human_has_4_chips_in_row(self):
        board = np.zeros((6, 7), dtype = int)
        board[1][4] = 1
        board[2][4] = 1
        board[3][4] = 1
        board[4][4] = 1
        board[1][3] = 1
        board[1][5] = 1
        board[1][6] = 1
        self.assertEqual(C4_game.is_terminal_node(board), (True, 1))
    
    def test_terminal_node_is_True_when_AI_has_4_chips_in_row(self):
        board = np.zeros((6, 7), dtype = int)
        board[2][2] = 2
        board[3][2] = 2
        board[4][2] = 2
        board[5][2] = 2
        self.assertEqual(C4_game.is_terminal_node(board), (True, 2))
    
    def test_terminal_node_is_False_when_neither_player_has_4_in_row(self):
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 1
        board[1][0] = 1
        board[2][0] = 2
        board[3][0] = 2
        board[0][4] = 1
        board[1][4] = 1
        board[0][3] = 2
        board[1][3] = 2
        self.assertEqual(C4_game.is_terminal_node(board), (False, -1))

class TestMinimax(unittest.TestCase):
    def test_minimax_depth_0(self):
        board = np.zeros((6, 7), dtype = int)
        depth = 0
        maximizing_player = True
        self.assertEqual(C4_game.minimax(board, depth, maximizing_player), (0, 0))
    
    def test_minimax_terminal_node_True_human_won(self):
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 1
        board[1][0] = 1
        board[2][0] = 1
        board[3][0] = 1
        depth = 1
        maximizing_player = True
        self.assertEqual(C4_game.minimax(board, depth, maximizing_player), (-9999999, 0))
    
    def test_minimax_terminal_node_True_AI_won(self):
        board = np.zeros((6, 7), dtype = int)
        board[0][1] = 2
        board[1][1] = 2
        board[2][1] = 2
        board[3][1] = 2
        depth = 1
        maximizing_player = True
        self.assertEqual(C4_game.minimax(board, depth, maximizing_player), (9999999, 0))

if __name__ == '__main__':
    unittest.main()
