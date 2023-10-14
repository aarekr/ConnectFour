""" Connect Four Game - Artificial Intelligence """

import math
import random

N_ROWS = 6
N_COLUMNS = 7
YELLOW = (255, 255, 0)
OPTIMAL_ORDER = [3, 2, 4, 1, 5, 0, 6]  # preferred/optimal order of handling columns in minimax

def initialize_random_turn():
    """ starting player chosen randomly """
    turn = random.randint(1, 2)  # game starter chosen randomly: 1=human (red), 2=AI (yellow)
    return turn

def get_chip_count(board):
    """ returning the number of chips players have dropped """
    chip_count = 0
    for row in board:  # refactor this
        for item in row:
            if item != 0:
                chip_count += 1
    return chip_count

def next_free_row(board, col):
    """ returning the lowest free row in the given column """
    free_row = -1
    for row in range(N_ROWS):
        if board[row][col] == 0:
            free_row = row
            break
    return free_row

def all_free_columns(board):
    """ returning a list of columns that have at least one free slot/row """
    free_columns = []
    for col in range(N_COLUMNS):
        if board[N_ROWS-1][col] == 0:  # at least top row in column is empty
            free_columns.append(col)
    return free_columns

def optimal_column_traversing_order(free_columns):
    """ returns the optimal traversing order of columns """
    actual_order = []  # order used for going through all options
    for item in OPTIMAL_ORDER:
        if item in free_columns:
            actual_order.append(item)
    return actual_order

def drop_chip(board, row, col, turn):
    """ player drops their chip and TURN is given to the other player """
    row = next_free_row(board, col)
    board[row][col] = turn
    if turn == 1:
        turn = 2
    elif turn == 2:
        turn = 1
    return turn

def check_if_game_active(board, player):
    """ checking if the player has 4 chips in row/column/diagonal
        returning False if game ends and True if stays active """
    # Rows
    for row in range(N_ROWS):
        for col in range(N_COLUMNS-3):
            if (board[row][col] ==
                    board[row][col+1] ==
                    board[row][col+2] ==
                    board[row][col+3] == player):
                return False
    # Columns
    for col in range(N_COLUMNS):
        for row in range(N_ROWS-3):
            if (board[row][col] ==
                    board[row+1][col] ==
                    board[row+2][col] ==
                    board[row+3][col] == player):
                return False
    # Positive diagonals
    for row in range(N_ROWS-3):
        for col in range(N_COLUMNS-3):
            if (board[row][col] ==
                    board[row+1][col+1] ==
                    board[row+2][col+2] ==
                    board[row+3][col+3] == player):
                return False
    # Negative diagonals
    for col in range(N_COLUMNS-3):
        for row in range(N_ROWS-3):
            if (board[N_ROWS-1-row][col] ==
                    board[N_ROWS-1-row-1][col+1] ==
                    board[N_ROWS-1-row-2][col+2] ==
                    board[N_ROWS-1-row-3][col+3] == player):
                return False
    return True

def is_terminal_node(board):
    """ minimax helper function,
        returns False if game continues,
        returns tuple (True, draw(0)/winner(1 or 2)) if all chips used or
        one of the players won """
    if get_chip_count(board) == 42:  # all chips used and draw (0)
        return True, 0
    if not check_if_game_active(board, 1):  # human player won (1)
        return True, 1
    if not check_if_game_active(board, 2):  # AI won (2)
        return True, 2
    return False, -1  # game continues, no winner or draw

def count_ai_position_value_points(four_consequtive_slots, player):
    """ counts the AI position value for 4 consequtive slots """
    position_value = 0
    if four_consequtive_slots.count(player) == 3 and four_consequtive_slots.count(0) == 1:
        position_value += 30
    elif four_consequtive_slots.count(player) == 2 and four_consequtive_slots.count(0) == 2:
        position_value += 10
    return position_value

def count_human_position_value_points(four_consequtive_slots, player):
    """ counts the human player position value for 4 consequtive slots
        AI gets negative points for certain human player chip positions """
    position_value = 0
    if four_consequtive_slots.count(player) == 3 and four_consequtive_slots.count(0) == 1:
        position_value -= 90
    elif four_consequtive_slots.count(player) == 2 and four_consequtive_slots.count(0) == 2:
        position_value -= 20
    return position_value

def get_position_value(board, player):
    """ calculates the optimal position value for the AI """
    position_value = 0

    # Horizontal counting
    for row in range(N_ROWS):
        for col in range(N_COLUMNS-3):
            four_consequtive_slots = [board[row][col],
                                      board[row][col+1],
                                      board[row][col+2],
                                      board[row][col+3]]
            position_value += count_ai_position_value_points(four_consequtive_slots, player)
            position_value += count_human_position_value_points(four_consequtive_slots, 1)

    # Vertical counting
    for col in range(N_COLUMNS):
        for row in range(N_ROWS-3):
            four_consequtive_slots = [board[row][col],
                                      board[row+1][col],
                                      board[row+2][col],
                                      board[row+3][col]]
            position_value += count_ai_position_value_points(four_consequtive_slots, player)
            position_value += count_human_position_value_points(four_consequtive_slots, 1)

    # Positive diagonal counting
    for row in range(N_ROWS-3):
        for col in range(N_COLUMNS-3):
            four_consequtive_slots = [board[row][col],
                                      board[row+1][col+1],
                                      board[row+2][col+2],
                                      board[row+3][col+3]]
            position_value += count_ai_position_value_points(four_consequtive_slots, player)
            position_value += count_human_position_value_points(four_consequtive_slots, 1)

    # Negative diagonal counting
    for col in range(N_COLUMNS-3):
        for row in range(N_ROWS-3):
            four_consequtive_slots = [board[N_ROWS-1-row][col],
                                      board[N_ROWS-1-row-1][col+1],
                                      board[N_ROWS-1-row-2][col+2],
                                      board[N_ROWS-1-row-3][col+2]]
            position_value += count_ai_position_value_points(four_consequtive_slots, player)
            position_value += count_human_position_value_points(four_consequtive_slots, 1)

    return position_value

class AI:
    """ This class handles the AI logic """

    def __init__(self):
        self.winner = 0

    def minimax(self, board, depth, alpha, beta, maximizing_player):  # Too many arguments (6/5)
        """ minimax function that determins the best move for the AI """
        terminal_node, self.winner = is_terminal_node(board)
        if depth == 0 or terminal_node:  # recursion ends
            # return the heuristic value of node
            if terminal_node and self.winner == 1:
                return -9999999, 0  # high negative value equals human won
            if terminal_node and self.winner == 2:
                return 9999999, 0   # high positive value equals AI won
            if depth == 0:
                return get_position_value(board, maximizing_player), 0
        free_columns = all_free_columns(board)
        if maximizing_player:
            value = -math.inf
            best_col = -1
            for col in optimal_column_traversing_order(free_columns):
                row = next_free_row(board, col)
                minimax_board = board.copy()
                drop_chip(minimax_board, row, col, 2)  # dropping AI chip
                minimax_value = self.minimax(minimax_board, depth-1, alpha, beta, False)[0]
                if minimax_value > value:
                    value = minimax_value
                    best_col = col
                if value > beta:
                    break
                alpha = max(alpha, value)
            return value, best_col
        # else: minimizing player - pylint recommended removing else
        value = math.inf
        best_col = -1
        for col in optimal_column_traversing_order(free_columns):
            row = next_free_row(board, col)
            minimax_board = board.copy()
            drop_chip(minimax_board, row, col, 1)  # dropping human player chip
            minimax_value = self.minimax(minimax_board, depth-1, alpha, beta, True)[0]
            if minimax_value < value:
                value = minimax_value
                best_col = col
            if value < alpha:
                break
            beta = min(beta, value)
        return value, best_col
