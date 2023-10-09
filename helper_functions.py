""" Connect Four Game - helper functions for User Interface """

import random
import numpy as np

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

def get_chip_count(board):
    """ returning the number of chips players have dropped """
    chip_count = 0
    for row in board:  # refactor this
        for item in row:
            if item != 0:
                chip_count += 1
    return chip_count

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
