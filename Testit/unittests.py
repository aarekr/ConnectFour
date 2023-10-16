import unittest
import numpy as np
import random
import math
import pygame
import sys
sys.path.append('../')
import ai
import ui

# run the tests with command: python3 -m unittest -v unittest.py

YELLOW = (255, 255, 0)

class TestGameStart(unittest.TestCase):
    def test_create_game_board_function_returns_valid_game_board(self):
        """ Test that create_game_board() function returns the valid game board """
        board_right_shape = np.zeros((6, 7), dtype = int)
        self.assertEqual(ui.create_game_board(6, 7).shape, board_right_shape.shape)

    def test_bottom_row_is_all_zeros_when_game_starts(self):
        """ Test that the bottom row has all zeros when game starts """
        board = np.zeros((6, 7), dtype = int)
        self.assertEqual(ai.next_free_row(board, 0), 0)
        self.assertEqual(ai.next_free_row(board, 1), 0)
        self.assertEqual(ai.next_free_row(board, 2), 0)
        self.assertEqual(ai.next_free_row(board, 3), 0)
        self.assertEqual(ai.next_free_row(board, 4), 0)
        self.assertEqual(ai.next_free_row(board, 5), 0)
        self.assertEqual(ai.next_free_row(board, 6), 0)

    def test_all_columns_free_when_game_starts(self):
        """ Should return [0,1,2,3,4,5,6] as free columns """
        board = np.zeros((6, 7), dtype = int)
        self.assertEqual(ai.all_free_columns(board), [0,1,2,3,4,5,6])
    
    def test_print_board_functionality(self):
        """ Testing that print_board() function exists and responds.
            Does not have any return value. """
        board = np.zeros((6, 7), dtype = int)
        self.assertEqual(ui.print_board(board), None)

    def test_draw_board(self):  # is this sensible? additionally, red&yellow chips part not covered
        """ Test that the game board is drawn """
        board = np.zeros((6, 7), dtype = int)
        self.assertEqual(ui.UI().draw_board(board), None)

    def test_human_starts_the_game_text_is_generated(self):
        """ Test that the 'You start' text is visible when game starts and human player moves first """
        pygame.font.init()
        text_font = pygame.font.Font(pygame.font.get_default_font(), 60)
        correct_label = text_font.render("You start", 0, YELLOW)
        print("\n  ---> ", correct_label.get_size())      # (260, 60)
        print("\n  ---> ", correct_label.get_colorkey())  # (0, 0, 255, 255) i.e. YELLOW
        print("\n  ---> ", correct_label.get_clip())      # <rect(0, 0, 178, 41)>
        print("\n  ---> ", correct_label.get_height())    # 60
        self.assertEqual(ui.game_start_text(1).get_size()[1], correct_label.get_size()[1])
        self.assertEqual(ui.game_start_text(1).get_colorkey(), correct_label.get_colorkey())

    def test_ai_starts_the_game_text_is_generated(self):
        """ Test that the 'AI starts' text is visible when game starts and AI moves first """
        pygame.font.init()
        text_font = pygame.font.Font(pygame.font.get_default_font(), 60)
        correct_label = text_font.render("AI starts", 0, YELLOW)
        self.assertEqual(ui.game_start_text(2).get_size()[1], correct_label.get_size()[1])
        self.assertEqual(ui.game_start_text(2).get_colorkey(), correct_label.get_colorkey())

class TestFourInRow(unittest.TestCase):
    def test_four_chips_in_row_ends_the_game(self):
        """ Test that 4 chips in row ends the game """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 1
        board[0][1] = 1
        board[0][2] = 1
        board[0][3] = 1
        self.assertFalse(ai.check_if_game_active(board, 1), False)

    def test_four_chips_in_column_ends_the_game(self):
        """ Test that 4 chips in column ends the game """
        board = np.zeros((6, 7), dtype = int)
        board[0][1] = 1
        board[1][1] = 1
        board[2][1] = 1
        board[3][1] = 1
        self.assertFalse(ai.check_if_game_active(board, 1), False)

    def test_four_chips_in_positive_diagonal_ends_the_game(self):
        """ Test that 4 chips in positive diagonal ends the game """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 1
        board[1][1] = 1
        board[2][2] = 1
        board[3][3] = 1
        self.assertFalse(ai.check_if_game_active(board, 1), False)

    def test_four_chips_in_negative_diagonal_ends_the_game(self):
        """ Test that 4 chips in negative diagonal ends the game """
        board = np.zeros((6, 7), dtype = int)
        board[5][0] = 1
        board[4][1] = 1
        board[3][2] = 1
        board[2][3] = 1
        self.assertFalse(ai.check_if_game_active(board, 1), False)

    def test_four_chips_of_both_players_in_row_does_not_end_the_game(self):
        """ Test that 4 chips of both players in a row continues the game """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 1
        board[0][1] = 2  # this chip breaks the row
        board[0][2] = 1
        board[0][3] = 1
        self.assertTrue(ai.check_if_game_active(board, 1), True)

class TestTurnChanges(unittest.TestCase):
    def test_turn_changes_from_1_to_2(self):
        """ Test that turn changes from human(1) to AI(2) """
        board = np.zeros((6, 7), dtype = int)
        self.assertEqual(ai.drop_chip(board, 0, 0, 1), 2)

    def test_turn_changes_from_2_to_1(self):
        """ Test that turn changes from AI(2) to human(1) """
        board = np.zeros((6, 7), dtype = int)
        self.assertEqual(ai.drop_chip(board, 0, 0, 2), 1)

    def test_random_turn_generated(self):
        """ Test that turn 1 or 2 is generated """
        random_turn = ai.initialize_random_turn()
        if random_turn == 1:
            self.assertEqual(random_turn, 1)
        elif random_turn == 2:
            self.assertEqual(random_turn, 2)

class TestChipCount(unittest.TestCase):
    def test_empty_board_returns_chip_count_zero(self):
        """ Test that chip count is zero when board is empty """
        board = np.zeros((6, 7), dtype = int)
        self.assertEqual(ai.get_chip_count(board), 0)
    
    def test_chip_count_returns_4_when_both_players_have_dropped_2(self):
        """ Test that chip count is 4 when both players have dropped 2 chips """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 1
        board[1][0] = 1
        board[0][3] = 2
        board[1][3] = 2
        self.assertEqual(ai.get_chip_count(board), 4)
    
    def test_chip_count_is_42_when_all_chips_dropped(self):
        """ Test that chip count is 42 when the board is full """
        board = create_full_42_chip_board()
        self.assertEqual(ai.get_chip_count(board), 42)

class TestFreeRows(unittest.TestCase):
    def test_row_3_is_free_when_3_chips_dropped(self):
        """ Test that row 3 is free when 3 chips dropped in that column """
        board = np.zeros((6, 7), dtype = int)
        board[0][5] = 1
        board[1][5] = 2
        board[2][5] = 1
        self.assertEqual(ai.next_free_row(board, 5), 3)
    
    def test_no_free_rows_when_column_full(self):
        """ Test that no free rows when all 6 slots full in that column """
        board = np.zeros((6, 7), dtype = int)
        board[0][6] = 1
        board[1][6] = 2
        board[2][6] = 1
        board[3][6] = 2
        board[4][6] = 1
        board[5][6] = 2
        self.assertEqual(ai.next_free_row(board, 6), -1)

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
        self.assertEqual(ai.all_free_columns(board), [0,1,3,4,5,6])
    
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
        self.assertEqual(ai.all_free_columns(board), [0,1,2,3,4,5,6])

class TestTerminalNode(unittest.TestCase):
    def test_terminal_node_when_board_is_full_of_chips(self):
        """ Test that the node is terminal when all 42 chips dropped """
        board = create_full_42_chip_board()
        self.assertEqual(ai.is_terminal_node(board), (True, 0))
    
    def test_terminal_node_is_True_when_human_has_4_chips_in_row(self):
        """ Test that the node is terminal when human player has 4 in row """
        board = np.zeros((6, 7), dtype = int)
        board[1][4] = 1
        board[2][4] = 1
        board[3][4] = 1
        board[4][4] = 1
        board[1][3] = 1
        board[1][5] = 1
        board[1][6] = 1
        self.assertEqual(ai.is_terminal_node(board), (True, 1))
    
    def test_terminal_node_is_True_when_AI_has_4_chips_in_row(self):
        """ Test that the node is terminal when AI has 4 in row """
        board = np.zeros((6, 7), dtype = int)
        board[2][2] = 2
        board[3][2] = 2
        board[4][2] = 2
        board[5][2] = 2
        self.assertEqual(ai.is_terminal_node(board), (True, 2))
    
    def test_terminal_node_is_False_when_neither_player_has_4_in_row(self):
        """ Test that the node is not terminal when when both players have random 4 chips """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 1
        board[1][0] = 1
        board[2][0] = 2
        board[3][0] = 2
        board[0][4] = 1
        board[1][4] = 1
        board[0][3] = 2
        board[1][3] = 2
        self.assertEqual(ai.is_terminal_node(board), (False, -1))

class TestMinimaxBasicFunctionalities(unittest.TestCase):
    def test_minimax_depth_0(self):
        """ Test that minimax returns tuple (points, 0) when depth is zero """
        board = np.zeros((6, 7), dtype = int)
        depth = 0
        maximizing_player = True
        self.assertEqual(ai.AI().minimax(board, depth, -math.inf, math.inf, maximizing_player), (0, 0))
    
    def test_minimax_terminal_node_True_when_human_won(self):
        """ Test that terminal node when human player won """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 1
        board[1][0] = 1
        board[2][0] = 1
        board[3][0] = 1
        depth = 1
        maximizing_player = True
        self.assertEqual(ai.AI().minimax(board, depth, -math.inf, math.inf, maximizing_player), (-9999999, 0))
    
    def test_minimax_terminal_node_True_when_AI_won(self):
        """ Test that terminal node when AI won """
        board = np.zeros((6, 7), dtype = int)
        board[0][1] = 2
        board[1][1] = 2
        board[2][1] = 2
        board[3][1] = 2
        depth = 1
        maximizing_player = True
        self.assertEqual(ai.AI().minimax(board, depth, -math.inf, math.inf, maximizing_player), (9999999, 0))

    def test_optimal_column_traversing_order_when_all_columns_free(self):
        """ Test that optimal traversing order is returned when all columns are free """
        free_columns = [0, 1, 2, 3, 4, 5, 6]
        self.assertEqual(ai.optimal_column_traversing_order(free_columns), [3, 2, 4, 1, 5, 0, 6])

    def test_optimal_column_traversing_order_when_2_columns_are_full(self):
        """ Test that optimal traversing order is returned when 2 columns are full """
        free_columns = [1, 2, 4, 5, 6]
        self.assertEqual(ai.optimal_column_traversing_order(free_columns), [2, 4, 1, 5, 6])

    def test_optimal_column_traversing_order_when_all_columns_are_full(self):
        """ Test that optimal traversing order is returned when all columns are full """
        # game has ended before this situation, reason for test is function correctness check
        free_columns = []
        self.assertEqual(ai.optimal_column_traversing_order(free_columns), [])

class TestMinimaxStrategies(unittest.TestCase):
    def test_minimax_ai_wins_with_1_move_when_3_consequtive_chips_in_column(self):
        """ Test that AI wins with one move when 3 consequtive chips in column """
        board = np.zeros((6, 7), dtype = int)
        board[0][5] = 2
        board[1][5] = 2
        board[2][5] = 2
        depth = 3
        maximizing_player = True
        self.assertEqual(ai.AI().minimax(board, depth, -math.inf, math.inf, maximizing_player), (9999999, 5))

    def test_minimax_ai_wins_with_1_move_when_3_consequtive_chips_in_row(self):
        """ Test that AI wins with one move when 3 consequtive chips in row """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 2
        board[0][1] = 2
        board[0][2] = 2
        depth = 3
        maximizing_player = True
        self.assertEqual(ai.AI().minimax(board, depth, -math.inf, math.inf, maximizing_player), (9999999, 3))

    """def test_ai_wins_with_2_moves_when_row_has_0002200_and_human_drops_1_chip(self):
        #Test that AI builds 3 chips in row, responds to human chip drop and wins with 2 moves 
        board = np.zeros((6, 7), dtype = int)
        board[0][3] = 2
        board[0][4] = 2
        depth = 2
        maximizing_player = False
        print("\n\nboard, starting   :", board[0])
        ai_1st_move = ui.UI().minimax(board, depth, -math.inf, math.inf, maximizing_player)[1]
        print("AI 1st_move:", ai_1st_move)
        board[0][ai_1st_move] = 2
        print("board, AI 1st move:", board[0])
        if ai_1st_move == 5:    # ai choses column 4
            board[0][6] = 1  # human counters with column 5
            print("board, human moves:", board[0])
            ai_2nd_move = ui.UI().minimax(board, depth, -math.inf, math.inf, maximizing_player)[1]  # error: AI choses 1 but should choose 2
            print("AI 2nd_move:", ai_2nd_move)
            board[0][ai_2nd_move] = 2
            print("board, AI 2nd move:", board[0])
            #self.assertEqual(ui.UI().minimax(board, depth, -math.inf, math.inf, maximizing_player), (9999999, 2))
        elif ai_1st_move == 2:  # ai choses column 1
            board[0][1] = 1  # human counters with column 2
            print("board, human moves:", board[0])
            self.assertEqual(ui.UI().minimax(board, depth, -math.inf, math.inf, maximizing_player), (9999999, 5))"""

class TestAIPositionValue(unittest.TestCase):
    def test_3_in_row_and_1_empty_gives_AI_30_points(self):
        """ Test that 3 in row and 1 empty gives AI 30 points """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 2
        board[0][1] = 2
        board[0][2] = 2
        board[0][3] = 0
        four_consequtive_slots = [board[0][0], board[0][1], board[0][2], board[0][3]]
        self.assertEqual(ai.count_ai_position_value_points(four_consequtive_slots, 2), 30)

    def test_2_in_row_and_2_empty_gives_AI_10_points(self):
        """ Test that 2 in row and 2 empty gives AI 10 points """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 0
        board[0][1] = 2
        board[0][2] = 2
        board[0][3] = 0
        four_consequtive_slots = [board[0][0], board[0][1], board[0][2], board[0][3]]
        self.assertEqual(ai.count_ai_position_value_points(four_consequtive_slots, 2), 10)

class TestHumanPlayerPositionValue(unittest.TestCase):
    def test_3_human_player_chips_in_row_gives_AI_negative_90_points(self):
        """ Test that 3 human player chips in row and 1 empty gives AI -90 points """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 1
        board[0][1] = 1
        board[0][2] = 1
        board[0][3] = 0
        four_consequtive_slots = [board[0][0], board[0][1], board[0][2], board[0][3]]
        self.assertEqual(ai.count_human_position_value_points(four_consequtive_slots, 1), -90)

    def test_2_human_player_chips_in_row_gives_AI_negative_20_points(self):
        """ Test that 2 human player chips in row and 2 empty gives AI -20 points """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 0
        board[0][1] = 1
        board[0][2] = 1
        board[0][3] = 0
        four_consequtive_slots = [board[0][0], board[0][1], board[0][2], board[0][3]]
        self.assertEqual(ai.count_human_position_value_points(four_consequtive_slots, 1), -20)

class TestGameEnd(unittest.TestCase):
    def test_human_won_accounced_in_console(self):
        """ Test that when human wins, console text is You won! """
        self.assertEqual(ui.UI().handle_game_end_in_console(1), "You won!")

    def test_ai_won_accounced_in_console(self):
        """ Test that when AI wins, console text is AI won... """
        self.assertEqual(ui.UI().handle_game_end_in_console(2), "AI won...")

# helper function
def create_full_42_chip_board():
    """ fills the game board with 42 chips """
    board = np.zeros((6, 7), dtype = int)
    for row in range(6):
        for col in range(7):
            board[row][col] = random.randint(1,2)
    return board

if __name__ == '__main__':
    unittest.main()