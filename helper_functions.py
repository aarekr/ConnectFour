""" Connect Four Game - helper functions for User Interface """

import pygame
import random
import numpy as np

N_ROWS = 6
N_COLUMNS = 7
YELLOW = (255, 255, 0)

def create_game_board(rows, columns):
    """ creating the game board """
    board = np.zeros((rows, columns), dtype=int)
    return board

def print_board(board):
    """ printing slots and chips in console """
    print(np.flip(board, 0))

def initialize_random_turn():
    """ starting player chosen randomly """
    turn = random.randint(1, 2)  # game starter chosen randomly: 1=human (red), 2=AI (yellow)
    return turn

def game_start_text(turn):
    """ printing who starts the game in top part of the game board window """
    #text_font = pygame.font.SysFont("Comic Sans MS", 60)
    #text_font = pygame.font.SysFont(pygame.font.get_default_font(), 60)  # size = 41
    #text_font = pygame.font.Font(pygame.font.get_default_font(), 60)
    text_font = pygame.font.Font(pygame.font.get_default_font(), 60)
    #print(pygame.font.get_fonts()[7])
    who_starts = ""
    if turn == 1:
        who_starts = "You start"
    elif turn == 2:
        who_starts = "AI starts"
    label = text_font.render(who_starts, 0, YELLOW)
    return label

def game_end_text(winner):
    """ printing the game result when game ends: winner or draw """
    text_font = pygame.font.SysFont("Comic Sans MS", 60)
    end_text = ""
    if winner == 0:
        end_text = "Draw"
    elif winner == 1:
        end_text = "YOU WON!!!"
    elif winner == 2:
        end_text = "AI won..."
    label = text_font.render(end_text, 0, YELLOW)
    return label

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

def drop_chip(board, row, col, turn):
    """ player drops their chip and TURN is given to the other player """
    row = next_free_row(board, col)
    board[row][col] = turn
    if turn == 1:
        turn = 2
    elif turn == 2:
        turn = 1
    return turn

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
