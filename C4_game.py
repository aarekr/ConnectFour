""" Connect Four Game """

import sys
import math
import random
import numpy as np
import pygame

black = (0, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)

TURN = random.randint(1, 2)  # game starter chosen randomly: 1=human (red), 2=AI (yellow)
# CHIP_COUNT = 0  # counting total number of chips players have dropped

def create_game_board(rows, columns):
    """ creating the game board """
    board = np.zeros((rows, columns), dtype=int)
    return board

def game_start_text():
    """ printing who starts the game in top part of the game board window """
    who_starts = ""
    if TURN == 1:
        who_starts = "You start"
    elif TURN == 2:
        who_starts = "AI starts"
    label = text_font.render(who_starts, 0, yellow)
    screen.blit(label, (250, 15))

def print_board(board):
    """ printing slots and chips in console """
    print(np.flip(board, 0))

def get_chip_count(board):
    """ returning the number of chips players have dropped """
    chip_count = 0
    for row in board:  # refactor this
        for item in row:
            if item != 0:
                chip_count += 1
    return chip_count

def draw_board(board):
    """ drawing the game board in a window """
    # drawing the blue game board and white empty slots
    for col in range(N_COLUMNS):
        for row in range(N_ROWS):
            pygame.draw.rect(screen, blue, (col*SLOT_SIZE, row*SLOT_SIZE+SLOT_SIZE, SLOT_SIZE,
                                            SLOT_SIZE))
            pygame.draw.circle(screen, white, (int(col*SLOT_SIZE+SLOT_SIZE/2),
                                               int(row*SLOT_SIZE+SLOT_SIZE+SLOT_SIZE/2)), RADIUS)
    # drawing players' red and yellow chips
    for col in range(N_COLUMNS):
        for row in range(N_ROWS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, red, (int(col*SLOT_SIZE+SLOT_SIZE/2),
                                                 HEIGHT-int(row*SLOT_SIZE+SLOT_SIZE/2)), RADIUS)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, yellow, (int(col*SLOT_SIZE+SLOT_SIZE/2),
                                                    HEIGHT-int(row*SLOT_SIZE+SLOT_SIZE/2)), RADIUS)
    pygame.display.update()

def drop_chip(board, row, col, chip):
    """ player drops their chip and TURN is given to the other player """
    # global variables are causing pylint errors, so they should be replaced
    global TURN
    row = next_free_row(board, col)
    board[row][col] = chip
    if TURN == 1:
        TURN = 2
    elif TURN == 2:
        TURN = 1
    return TURN

def next_free_row(board, col):
    """ returning the lowest free row in the given column """
    free_row = -1
    for row in range(N_ROWS):
        if board[row][col] == 0:
            free_row = row
            break
    return free_row

def all_free_columns(board):
    """ returning a list of columns that have at least of free slot/row """
    free_columns = []
    for col in range(N_COLUMNS):
        if board[N_ROWS-1][col] == 0:  # at least top row in column is empty
            free_columns.append(col)
    return free_columns

def check_if_game_active(board, player):
    """ checking if the player has 4 in row and game ends or is still active """
    for row in range(N_ROWS-3):
        for col in range(N_COLUMNS-3):
            if (board[row][col] == player and board[row+1][col] == player
                    and board[row+2][col] == player and board[row+3][col] == player):
                return False
    for row in range(N_ROWS-3):
        for col in range(N_COLUMNS-3):
            if (board[row][col] == player and board[row][col+1] == player
                    and board[row][col+2] == player and board[row][col+3] == player):
                return False
    for row in range(N_ROWS-3):
        for col in range(N_COLUMNS-3):
            if (board[row][col] == player and board[row+1][col+1] == player
                    and board[row+2][col+2] == player and board[row+3][col+3] == player):
                return False
    for row in range(3, N_ROWS):
        for col in range(N_COLUMNS-3):
            if (board[row][col] == player and board[row-1][col+1] == player
                    and board[row-2][col+2] == player and board[row-3][col+3] == player):
                return False
    return True

def get_position_value(board, player):
    """ calcluates the optimal position value for the AI """
    position_value = 0
    # Horizontal counting
    for row in range(N_ROWS):
        for col in range(N_COLUMNS - 3):
            four_consequtive_slots = [board[row][col], board[row][col+1], board[row][col+2],
                                      board[row][col+3]]
            if four_consequtive_slots.count(player) == 4:
                position_value += 100
            elif four_consequtive_slots.count(player) == 3 and four_consequtive_slots.count(0) == 1:
                position_value += 30
            elif four_consequtive_slots.count(player) == 2 and four_consequtive_slots.count(0) == 2:
                position_value += 10
            # print("four_consequtive_chips:", four_consequtive_chips)
            # print("AI chips:", four_consequtive_chips.count(2))

    # Vertical counting
    for col in range(N_COLUMNS):
        for row in range(N_ROWS-3):
            four_consequtive_slots = [board[row][col], board[row+1][col], board[row+2][col],
                                      board[row+3][col]]
            # print("four_consequtive_slots:", row, col, four_consequtive_slots)
            if four_consequtive_slots.count(player) == 4:
                position_value += 100
            elif four_consequtive_slots.count(player) == 3 and four_consequtive_slots.count(0) == 1:
                position_value += 30
            elif four_consequtive_slots.count(player) == 2 and four_consequtive_slots.count(0) == 2:
                position_value += 10
            # print("AI chips:", four_consequtive_slots.count(2), "position_value:", position_value)

    return position_value

def is_terminal_node(board):
    """ minimax helper function,
        returns False if game continues,
        returns tuple (True, draw(0)/winner(1 or 2)) if all chips used or one of the players won """
    if get_chip_count(board) == 42:  # all chips used and draw (0)
        return True, 0
    if not check_if_game_active(board, 1):  # human player won (1)
        return True, 1
    if not check_if_game_active(board, 2):  # AI won (2)
        return True, 2
    return False, -1  # game continues, no winner or draw

def minimax(board, depth, maximizing_player):
    """ minimax function that determins the best move for the AI """
    terminal_node, winner = is_terminal_node(board)
    if depth == 0 or terminal_node:  # game ends
        # return the heuristic value of node
        if depth == 0:
            return get_position_value(board, maximizing_player), 0
        if terminal_node and winner == 1:
            return -9999999, 0
        if terminal_node and winner == 2:
            return 9999999, 0
    free_columns = all_free_columns(board)
    if maximizing_player:
        value = -math.inf
        best_col = -1
        for col in free_columns:
            row = next_free_row(board, col)
            minimax_board = board.copy()
            drop_chip(minimax_board, row, col, 2)  # dropping AI chip
            minimax_value = minimax(minimax_board, depth - 1, False)[0]
            if minimax_value > value:
                value = minimax_value
                best_col = col
        return value, best_col
    else:  # minimizing player
        value = math.inf
        best_col = -1
        for col in free_columns:
            row = next_free_row(board, col)
            minimax_board = board.copy()
            drop_chip(minimax_board, row, col, 1)  # dropping human player chip
            minimax_value = minimax(minimax_board, depth - 1, True)[0]
            if minimax_value < value:
                value = minimax_value
                best_col = col
        return value, best_col

N_ROWS = 6
N_COLUMNS = 7
BOARD = create_game_board(N_ROWS, N_COLUMNS)
print_board(BOARD)
GAME_ACTIVE = True
pygame.init()

# creating the game window
SLOT_SIZE = 100
HEIGHT = (N_ROWS + 1) * SLOT_SIZE
WIDTH = N_COLUMNS * SLOT_SIZE
board_size = (HEIGHT, WIDTH)
RADIUS = int(SLOT_SIZE/2 - 5)
screen = pygame.display.set_mode(board_size)
text_font = pygame.font.SysFont("Comic Sans MS", 60)
game_start_text()
draw_board(BOARD)
pygame.display.update()

print("game started")
# game runs in this while loop until somebody wins or all 42 chips are used
while GAME_ACTIVE:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, black, (0, 0, WIDTH, SLOT_SIZE))
            posx = event.pos[0]
            if TURN == 1:
                pygame.draw.circle(screen, red, (posx, int(SLOT_SIZE/2)), RADIUS)
        pygame.display.update()
        # Player 1, human
        if TURN == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, black, (0, 0, WIDTH, SLOT_SIZE))
                posx = event.pos[0]
                COL = int(math.floor(posx/SLOT_SIZE))
                ROW = next_free_row(BOARD, COL)
                if BOARD[N_ROWS-1][COL] == 0:
                    drop_chip(BOARD, ROW, COL, 1)
                print_board(BOARD)
                draw_board(BOARD)
                GAME_ACTIVE = check_if_game_active(BOARD, 1)
                if not GAME_ACTIVE:
                    break
        # Player 2, AI
        elif TURN == 2:
            pygame.time.wait(1000)
            # ROW, COL = random_AI_chip_position(BOARD)  # random AI
            minimax_value, best_col = minimax(BOARD, 3, True)  # minimax
            drop_chip(BOARD, 0, best_col, 2) # this might cause errors
            print_board(BOARD)
            draw_board(BOARD)
            GAME_ACTIVE = check_if_game_active(BOARD, 2)
            if not GAME_ACTIVE:
                break
            TURN = 1
        if get_chip_count(BOARD) == 42:
            print("all chips used, game ends")
            GAME_ACTIVE = False
            break
print("game ended")
