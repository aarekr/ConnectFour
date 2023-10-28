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
    def test_create_game_board_function_returns_valid_game_board(self):  # 1
        """ - Test that a valid game board is created when the game starts """
        board_right_shape = np.zeros((6, 7), dtype = int)
        self.assertEqual(ui.create_game_board(6, 7).shape, board_right_shape.shape)

    def test_bottom_row_is_all_zeros_when_game_starts(self):  # 2
        """ - Test that the bottom row has all zeros when game starts """
        board = np.zeros((6, 7), dtype = int)
        self.assertEqual(ai.next_free_row(board, 0), 0)
        self.assertEqual(ai.next_free_row(board, 1), 0)
        self.assertEqual(ai.next_free_row(board, 2), 0)
        self.assertEqual(ai.next_free_row(board, 3), 0)
        self.assertEqual(ai.next_free_row(board, 4), 0)
        self.assertEqual(ai.next_free_row(board, 5), 0)
        self.assertEqual(ai.next_free_row(board, 6), 0)

    def test_all_columns_free_when_game_starts(self):  # 3
        """ - Test that when game starts all columns are free """
        board = np.zeros((6, 7), dtype = int)
        self.assertEqual(ai.all_free_columns(board), [0,1,2,3,4,5,6])
    
    def test_print_board_functionality(self):  # 4
        """ - Testing that print_board() function exists and responds.
            Does not have any return value. """
        board = np.zeros((6, 7), dtype = int)
        self.assertEqual(ui.print_board(board), None)

    def test_draw_board(self):  # 5
        """ Test that the game board is drawn """
        board = np.zeros((6, 7), dtype = int)
        self.assertEqual(ui.UI().draw_board(board), None)

    def test_human_starts_the_game_text_is_generated(self):  # 6
        """ Test that the 'You start' text is visible when game starts and human player moves first """
        pygame.font.init()
        text_font = pygame.font.Font(pygame.font.get_default_font(), 60)
        correct_label = text_font.render("You start", 0, YELLOW)
        self.assertEqual(ui.game_start_text(1).get_size()[1], correct_label.get_size()[1])
        self.assertEqual(ui.game_start_text(1).get_colorkey(), correct_label.get_colorkey())

    def test_ai_starts_the_game_text_is_generated(self):  # 7
        """ Test that the 'AI starts' text is visible when game starts and AI moves first """
        pygame.font.init()
        text_font = pygame.font.Font(pygame.font.get_default_font(), 60)
        correct_label = text_font.render("AI starts", 0, YELLOW)
        self.assertEqual(ui.game_start_text(2).get_size()[1], correct_label.get_size()[1])
        self.assertEqual(ui.game_start_text(2).get_colorkey(), correct_label.get_colorkey())

    def test_draw_text_is_generated_when_game_ends_in_draw(self):  # 8
        """ Test that 'Draw' text is visible when neither wins """
        pygame.font.init()
        text_font = pygame.font.Font(pygame.font.get_default_font(), 60)
        correct_label = text_font.render("Draw", 0, YELLOW)
        self.assertEqual(ui.game_end_text(1).get_size()[1], correct_label.get_size()[1])
        self.assertEqual(ui.game_end_text(2).get_colorkey(), correct_label.get_colorkey())

    def test_human_won_text_is_generated_when_human_wins(self):  # 9
        """ Test that when human wins, 'YOU WON!!!' text is visible """
        pygame.font.init()
        text_font = pygame.font.Font(pygame.font.get_default_font(), 60)
        correct_label = text_font.render("YOU WON!!!", 0, YELLOW)
        self.assertEqual(ui.game_end_text(1).get_size()[1], correct_label.get_size()[1])
        self.assertEqual(ui.game_end_text(1).get_colorkey(), correct_label.get_colorkey())

    def test_ai_won_text_is_generated_when_human_wins(self):  # 10
        """ Test that when AI wins, 'AI won...' text is visible """
        pygame.font.init()
        text_font = pygame.font.Font(pygame.font.get_default_font(), 60)
        correct_label = text_font.render("AI won...", 0, YELLOW)
        self.assertEqual(ui.game_end_text(2).get_size()[1], correct_label.get_size()[1])
        self.assertEqual(ui.game_end_text(2).get_colorkey(), correct_label.get_colorkey())

class TestFourInRow(unittest.TestCase):
    def test_four_chips_in_row_ends_the_game(self):
        """ Test that 4 chips in row ends the game """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 1
        board[0][1] = 1
        board[0][2] = 1
        board[0][3] = 1
        self.assertFalse(ai.check_if_game_active(board, 1), False)
        board = np.zeros((6, 7), dtype = int)
        board[0][2] = 2
        board[0][3] = 2
        board[0][4] = 2
        board[0][5] = 2
        self.assertFalse(ai.check_if_game_active(board, 2), False)

    def test_four_chips_in_column_ends_the_game(self):
        """ Test that 4 chips in column ends the game """
        board = np.zeros((6, 7), dtype = int)
        board[0][1] = 1
        board[1][1] = 1
        board[2][1] = 1
        board[3][1] = 1
        self.assertFalse(ai.check_if_game_active(board, 1), False)
        board = np.zeros((6, 7), dtype = int)
        board[2][3] = 2
        board[3][3] = 2
        board[4][3] = 2
        board[5][3] = 2
        self.assertFalse(ai.check_if_game_active(board, 2), False)

    def test_four_chips_in_positive_diagonal_ends_the_game(self):
        """ Test that 4 chips in positive diagonal ends the game """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 1
        board[1][1] = 1
        board[2][2] = 1
        board[3][3] = 1
        self.assertFalse(ai.check_if_game_active(board, 1), False)
        board = np.zeros((6, 7), dtype = int)
        board[1][2] = 2
        board[2][3] = 2
        board[3][4] = 2
        board[4][5] = 2
        self.assertFalse(ai.check_if_game_active(board, 2), False)

    def test_four_chips_in_negative_diagonal_ends_the_game(self):
        """ Test that 4 chips in negative diagonal ends the game """
        board = np.zeros((6, 7), dtype = int)
        board[5][0] = 1
        board[4][1] = 1
        board[3][2] = 1
        board[2][3] = 1
        self.assertFalse(ai.check_if_game_active(board, 1), False)
        board = np.zeros((6, 7), dtype = int)
        board[4][1] = 2
        board[3][2] = 2
        board[2][3] = 2
        board[1][4] = 2
        self.assertFalse(ai.check_if_game_active(board, 2), False)

    def test_four_chips_of_both_players_in_row_does_not_end_the_game(self):
        """ Test that 4 chips of both players in a row continues the game """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 1
        board[0][1] = 2  # this chip breaks the row
        board[0][2] = 1
        board[0][3] = 1
        self.assertTrue(ai.check_if_game_active(board, 1), True)
        board = np.zeros((6, 7), dtype = int)
        board[2][2] = 2  # this chip breaks the row
        board[2][3] = 1
        board[2][4] = 1
        board[2][5] = 2  # this chip breaks the row
        self.assertTrue(ai.check_if_game_active(board, 2), True)

class TestTurnChanges(unittest.TestCase):
    def test_turn_changes_from_1_to_2(self):
        """ Test that turn changes from human(1) to AI(2) after chip dropped """
        board = np.zeros((6, 7), dtype = int)
        self.assertEqual(ai.drop_chip(board, 0, 0, 1), 2)

    def test_turn_changes_from_2_to_1(self):
        """ Test that turn changes from AI(2) to human(1) after chip dropped """
        board = np.zeros((6, 7), dtype = int)
        self.assertEqual(ai.drop_chip(board, 0, 0, 2), 1)

    def test_random_turn_generated(self):
        """ Test that turn 1 or 2 is generated """
        random_turn = ai.initialize_random_turn()
        self.assertEqual(random_turn >=1 and random_turn <=2 , True)

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

    def test_chip_count_returns_7_when_players_have_dropped_4_and_3(self):
        """ Test that chip count is 7 when players have dropped 3 and 4 """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 1
        board[0][1] = 1
        board[1][2] = 1
        board[0][2] = 2
        board[0][3] = 2
        board[1][3] = 2
        board[0][6] = 2
        self.assertEqual(ai.get_chip_count(board), 7)

    def test_chip_count_is_42_when_all_chips_dropped(self):
        """ Test that chip count is 42 when the board is full """
        board = create_full_42_chip_board()
        self.assertEqual(ai.get_chip_count(board), 42)

class TestFreeRows(unittest.TestCase):
    def test_bottom_row_is_free_when_no_chips_dropped_in_that_column(self):
        """ Test bottom row is available when no chips dropped in that column """
        board = np.zeros((6, 7), dtype = int)
        board[0][1] = 1
        board[1][1] = 2
        board[0][3] = 1
        board[0][6] = 2
        self.assertEqual(ai.next_free_row(board, 0), 0)
        self.assertEqual(ai.next_free_row(board, 2), 0)
        self.assertEqual(ai.next_free_row(board, 4), 0)
        self.assertEqual(ai.next_free_row(board, 5), 0)

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
    def test_should_show_6_free_columns_when_1_column_full(self):
        """ Test that 6 columns are free when 1 column (#2) is full """
        board = np.zeros((6, 7), dtype = int)
        board[0][2] = 1
        board[1][2] = 2
        board[2][2] = 1
        board[3][2] = 2
        board[4][2] = 1
        board[5][2] = 2
        board[0][1] = 1
        board[0][5] = 2
        self.assertEqual(ai.all_free_columns(board), [0,1,3,4,5,6])

    def test_no_free_columns_when_board_full(self):
        """ Test that no free columns when the board is full of chips """
        board = create_full_42_chip_board()
        self.assertEqual(ai.all_free_columns(board), [])

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
        """ Test that the node is terminal when human player has 4 in row (#1) """
        board = np.zeros((6, 7), dtype = int)
        board[2][4] = 1
        board[3][4] = 1
        board[4][4] = 1
        board[1][3] = 1
        board[1][4] = 1
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

    def test_4_chips_in_row_of_both_players_is_not_terminal_node(self):
        """ Test that tne node is not terminal when 2 chips of both players in row """
        board = np.zeros((6, 7), dtype = int)
        board[0][1] = 1
        board[0][2] = 1
        board[0][3] = 2
        board[0][4] = 2
        self.assertEqual(ai.is_terminal_node(board), (False, -1))

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
        """ Test that minimax returns tuple (points, None) when depth is zero """
        board = np.zeros((6, 7), dtype = int)
        depth = 0
        maximizing_player = True
        self.assertEqual(ai.AI().minimax(board, depth, -math.inf, math.inf, maximizing_player), (0, None))
    
    def test_minimax_terminal_node_True_and_winner_announced_when_human_won(self):
        """ Test that terminal node when human player won """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 1
        board[1][0] = 1
        board[2][0] = 1
        board[3][0] = 1
        depth = 1
        maximizing_player = True
        self.assertEqual(ai.AI().minimax(board, depth, -math.inf, math.inf, maximizing_player), (-math.inf, None))
    
    def test_minimax_terminal_node_True_and_winner_announced_when_AI_won(self):
        """ Test that terminal node when AI won """
        board = np.zeros((6, 7), dtype = int)
        board[0][1] = 2
        board[1][1] = 2
        board[2][1] = 2
        board[3][1] = 2
        depth = 1
        maximizing_player = True
        self.assertEqual(ai.AI().minimax(board, depth, -math.inf, math.inf, maximizing_player), (math.inf, None))

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
        # game has ended before this situation, reason for the test is function correctness check
        free_columns = []
        self.assertEqual(ai.optimal_column_traversing_order(free_columns), [])

class TestMinimaxStrategiesDepthOne(unittest.TestCase):
    def test_minimax_ai_wins_with_1_move_when_3_consequtive_chips_in_column(self):
        """ Test that AI wins with one move when 3 consequtive chips in column """
        board = np.zeros((6, 7), dtype = int)
        board[0][5] = 2
        board[1][5] = 2
        board[2][5] = 2
        depth = 1
        maximizing_player = True
        self.assertEqual(ai.AI().minimax(board, depth, -math.inf, math.inf, maximizing_player), (math.inf, 5))

        board = np.zeros((6, 7), dtype = int)
        board[0][4] = 1
        board[1][4] = 2
        board[2][4] = 2
        board[3][4] = 2
        depth = 1
        maximizing_player = True
        self.assertEqual(ai.AI().minimax(board, depth, -math.inf, math.inf, maximizing_player), (math.inf, 4))

        board = np.zeros((6, 7), dtype = int)
        board[0][3] = 1
        board[1][3] = 1
        board[2][3] = 2
        board[3][3] = 2
        board[4][3] = 2
        depth = 1
        maximizing_player = True
        self.assertEqual(ai.AI().minimax(board, depth, -math.inf, math.inf, maximizing_player), (math.inf, 3))

    def test_minimax_ai_wins_with_1_move_when_3_consequtive_chips_in_row(self):
        """ Test that AI wins with one move when 3 consequtive chips in row """
        # chip lands in row 0
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 2
        board[0][1] = 2
        board[0][2] = 2
        depth = 1
        maximizing_player = True
        self.assertEqual(ai.AI().minimax(board, depth, -math.inf, math.inf, maximizing_player), (math.inf, 3))

        board = np.zeros((6, 7), dtype = int)
        board[0][1] = 2
        board[0][2] = 2
        board[0][3] = 2
        depth = 1
        maximizing_player = True
        self.assertEqual(ai.AI().minimax(board, depth, -math.inf, math.inf, maximizing_player), (math.inf, 4))

        board = np.zeros((6, 7), dtype = int)
        board[0][2] = 2
        board[0][3] = 2
        board[0][4] = 2
        depth = 1
        maximizing_player = True
        self.assertEqual(ai.AI().minimax(board, depth, -math.inf, math.inf, maximizing_player), (math.inf, 1))

        board = np.zeros((6, 7), dtype = int)
        board[0][3] = 2
        board[0][4] = 2
        board[0][5] = 2
        depth = 1
        maximizing_player = True
        self.assertEqual(ai.AI().minimax(board, depth, -math.inf, math.inf, maximizing_player), (math.inf, 2))

        board = np.zeros((6, 7), dtype = int)
        board[0][4] = 2
        board[0][5] = 2
        board[0][6] = 2
        depth = 1
        maximizing_player = True
        self.assertEqual(ai.AI().minimax(board, depth, -math.inf, math.inf, maximizing_player), (math.inf, 3))

        # chip lands in row 1
        board = np.zeros((6, 7), dtype = int)
        board[0][1] = 1
        board[1][1] = 1
        board[1][2] = 2
        board[1][3] = 2
        board[1][4] = 2
        board[0][5] = 1  # should drop the chip on top of this
        board[0][6] = 1
        depth = 1
        maximizing_player = True
        self.assertEqual(ai.AI().minimax(board, depth, -math.inf, math.inf, maximizing_player), (math.inf, 5))

        # chip lands in row 2
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 1
        board[1][0] = 1
        board[0][1] = 2
        board[1][1] = 2
        board[0][2] = 2
        board[1][2] = 2
        board[0][3] = 1
        board[1][3] = 2
        board[0][4] = 1  # should drop the chip on top of this
        board[0][5] = 1
        depth = 1
        maximizing_player = True
        self.assertEqual(ai.AI().minimax(board, depth, -math.inf, math.inf, maximizing_player), (math.inf, 4))

class TestMinimaxStrategiesDepthThree(unittest.TestCase):
    # DEPTH 3
    def test_minimax_has_2_in_row_builds_3_and_wins_with_total_of_2_moves(self):
        """ Test Minimax, AI has 0002200 in bottom row, fills col 2 and wins with next move """
        board = np.zeros((6, 7), dtype = int)
        board[0][3] = 2
        board[1][3] = 1
        board[0][4] = 2
        board[1][4] = 1
        depth = 3  # gameplay: 1) AI: col 2, 2) human: col 1 or 5, 3) AI wins with 1 or 5
        maximizing_player = True
        self.assertEqual(ai.AI().minimax(board, depth, -math.inf, math.inf, maximizing_player), (math.inf, 2))

    def test_minimax_blocks_human_2_chip_row(self):
        """ Test human has 0011000 in bottom row, AI should block 1 side """
        board = np.zeros((6, 7), dtype = int)
        board[0][2] = 1
        board[0][3] = 1
        board[1][3] = 2
        depth = 3  # gameplay: AI: col 4, which gives best play value 10
        maximizing_player = True
        self.assertEqual(ai.AI().minimax(board, depth, -math.inf, math.inf, maximizing_player), (10, 2))

    def test_minimax_builds_cross_diagonals_of_3_chips_and_wins_with_total_of_2_moves(self):
        """ Test Minimax drops to col 2 and has 2 diagonal win options with next move """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 2
        board[0][1] = 1
        board[0][2] = 1
        board[0][3] = 1
        board[0][4] = 2
        board[1][1] = 2
        board[1][2] = 1
        board[1][3] = 2
        board[1][4] = 1
        board[2][1] = 2
        board[2][3] = 1
        depth = 3
        maximizing_player = True
        self.assertEqual(ai.AI().minimax(board, depth, -math.inf, math.inf, maximizing_player), (math.inf, 2))

    def test_minimax_blocks_4_in_row_twice_when_human_counters(self):
        """ Test AI should block 4 in row 1011000 with col 1, human counters with 4, AI counters with 5 """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 1
        board[0][2] = 1
        board[0][3] = 1
        board[1][2] = 2
        board[1][3] = 2
        depth = 3
        maximizing_player = True
        self.assertEqual(ai.AI().minimax(board, depth, -math.inf, math.inf, maximizing_player), (80, 1))
        board[0][1] = 2  # 1) AI: col 1
        board[0][4] = 1  # 2) human: col 4 and has now 3 in row
        depth = 3        # 3) AI should counter with col 5
        maximizing_player = True
        self.assertEqual(ai.AI().minimax(board, depth, -math.inf, math.inf, maximizing_player), (70, 5))

#class TestMinimaxStrategiesDepthFive(unittest.TestCase):
    # DEPTH 5
#    def test_minimax_wins_with_3_moves(self):

    # DEPTH 7



class TestAIPositionValue(unittest.TestCase):
    def test_3_in_row_and_1_empty_gives_AI_50_points(self):
        """ Test that 3 in row and 1 empty gives AI 50 points """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 2
        board[0][1] = 2
        board[0][2] = 2
        board[0][3] = 0
        four_consequtive_slots = [board[0][0], board[0][1], board[0][2], board[0][3]]
        self.assertEqual(ai.count_position_value(four_consequtive_slots), 50)

    def test_3_in_row_and_1_human_chip_gives_AI_0_points(self):
        """ Test that 3 in row and 1 empty gives AI 0 points """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 2
        board[0][1] = 2
        board[0][2] = 2
        board[0][3] = 1
        four_consequtive_slots = [board[0][0], board[0][1], board[0][2], board[0][3]]
        self.assertEqual(ai.count_position_value(four_consequtive_slots), 0)

    def test_2_in_row_and_2_empty_gives_AI_20_points(self):
        """ Test that 2 in row and 2 empty gives AI 20 points """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 0
        board[0][1] = 2
        board[0][2] = 2
        board[0][3] = 0
        four_consequtive_slots = [board[0][0], board[0][1], board[0][2], board[0][3]]
        self.assertEqual(ai.count_position_value(four_consequtive_slots), 20)

        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 2
        board[0][1] = 0
        board[0][2] = 2
        board[0][3] = 0
        four_consequtive_slots = [board[0][0], board[0][1], board[0][2], board[0][3]]
        self.assertEqual(ai.count_position_value(four_consequtive_slots), 20)

    def test_2_in_row_1_human_chip_and_1_empty_gives_AI_0_points(self):
        """ Test that 2 in row and 2 empty gives AI 0 points """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 1
        board[0][1] = 2
        board[0][2] = 2
        board[0][3] = 0
        four_consequtive_slots = [board[0][0], board[0][1], board[0][2], board[0][3]]
        self.assertEqual(ai.count_position_value(four_consequtive_slots), 0)

    def test_1_AI_chip_gives_AI_0_points(self):
        """ Test that 1 single AI chip gives 0 points """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 0
        board[0][1] = 0
        board[0][2] = 2
        board[0][3] = 0
        four_consequtive_slots = [board[0][0], board[0][1], board[0][2], board[0][3]]
        self.assertEqual(ai.count_position_value(four_consequtive_slots), 0)

class TestHumanPlayerPositionValue(unittest.TestCase):
    def test_3_human_player_chips_in_row_gives_AI_negative_50_points(self):
        """ Test that 3 human player chips in row and 1 empty gives AI -50 points """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 1
        board[0][1] = 1
        board[0][2] = 1
        board[0][3] = 0
        four_consequtive_slots = [board[0][0], board[0][1], board[0][2], board[0][3]]
        self.assertEqual(ai.count_position_value(four_consequtive_slots), -50)

    def test_3_human_player_chips_in_row_and_1_AI_chip_gives_AI_0_points(self):
        """ Test that 3 human player chips in row and 1 empty gives AI 0 points """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 1
        board[0][1] = 1
        board[0][2] = 1
        board[0][3] = 2
        four_consequtive_slots = [board[0][0], board[0][1], board[0][2], board[0][3]]
        self.assertEqual(ai.count_position_value(four_consequtive_slots), 0)

    def test_2_human_player_chips_in_row_gives_AI_negative_20_points(self):
        """ Test that 2 human player chips in row and 2 empty gives AI -20 points """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 0
        board[0][1] = 1
        board[0][2] = 1
        board[0][3] = 0
        four_consequtive_slots = [board[0][0], board[0][1], board[0][2], board[0][3]]
        self.assertEqual(ai.count_position_value(four_consequtive_slots), -20)

        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 1
        board[0][1] = 0
        board[0][2] = 1
        board[0][3] = 0
        four_consequtive_slots = [board[0][0], board[0][1], board[0][2], board[0][3]]
        self.assertEqual(ai.count_position_value(four_consequtive_slots), -20)

    def test_2_human_player_chips_and_1_AI_chip_gives_AI_0_points(self):
        """ Test that 2 in row, 1 empty gives and 1 AI chip gives AI 0 points """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 2
        board[0][1] = 1
        board[0][2] = 1
        board[0][3] = 0
        four_consequtive_slots = [board[0][0], board[0][1], board[0][2], board[0][3]]
        self.assertEqual(ai.count_position_value(four_consequtive_slots), 0)

    def test_1_human_player_chip_gives_AI_0_points(self):
        """ Test that 1 single human player chip gives AI 0 points """
        board = np.zeros((6, 7), dtype = int)
        board[0][0] = 0
        board[0][1] = 0
        board[0][2] = 1
        board[0][3] = 0
        four_consequtive_slots = [board[0][0], board[0][1], board[0][2], board[0][3]]
        self.assertEqual(ai.count_position_value(four_consequtive_slots), 0)

class TestGameEnd(unittest.TestCase):
    def test_draw_announced_in_console(self):
        """ Test that when game ends in draw, console text is Draw """
        self.assertEqual(ui.UI().handle_game_end_in_console(0), "Draw\n")

    def test_human_won_accounced_in_console(self):
        """ Test that when human wins, console text is You won! """
        self.assertEqual(ui.UI().handle_game_end_in_console(1), "You won!\n")

    def test_ai_won_accounced_in_console(self):
        """ Test that when AI wins, console text is AI won... """
        self.assertEqual(ui.UI().handle_game_end_in_console(2), "AI won...\n")

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
