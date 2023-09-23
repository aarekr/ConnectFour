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
global TURN
TURN = random.randint(1, 2)  # game starter chosen randomly: 1=human, 2=AI
global CHIP_COUNT  # counting total number of chips players have dropped
CHIP_COUNT = 0

def create_game_board(rows, columns):
    """ creating the game board """
    board = np.zeros((rows, columns))
    return board

def game_start_text():
    """ printing who starts the game on top of the game board """
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
    global TURN
    print("dropping chip:", chip)
    global CHIP_COUNT
    CHIP_COUNT += 1
    print("chip_count:", CHIP_COUNT)
    board[row][col] = chip
    if TURN == 1:
        TURN = 2
    elif TURN == 2:
        TURN = 1
    return TURN

def next_free_row(board, col):
    """ returning the lowest free row in the given column """
    for row in range(N_ROWS):
        if board[row][col] == 0:
            return row

def all_free_columns(board):
    """ returning a list of columns that have at least of free slot/row """
    free_columns = []
    for col in range(N_COLUMNS):
        if board[N_ROWS-1][col] == 0:  # at least top row in column is empty
            free_columns.append(col)
    print("all free columns:", free_columns)
    return free_columns

def check_if_game_active(board, player):
    """ checking if the player has 4 in row and game ends or is still active """
    print("checking winner", player)
    for row in range(N_ROWS-3):
        for col in range(N_COLUMNS-3):
            if (board[row][col] == player and board[row+1][col] == player
                    and board[row+2][col] == player and board[row+3][col] == player):
                print("player", player, "won")
                return False
    for row in range(N_ROWS-3):
        for col in range(N_COLUMNS-3):
            if (board[row][col] == player and board[row][col+1] == player
                    and board[row][col+2] == player and board[row][col+3] == player):
                print("player", player, "won")
                return False
    for row in range(N_ROWS-3):
        for col in range(N_COLUMNS-3):
            if (board[row][col] == player and board[row+1][col+1] == player
                    and board[row+2][col+2] == player and board[row+3][col+3] == player):
                print("player", player, "won")
                return False
    for row in range(3, N_ROWS):
        for col in range(N_COLUMNS-3):
            if (board[row][col] == player and board[row-1][col+1] == player
                    and board[row-2][col+2] == player and board[row-3][col+3] == player):
                print("player", player, "won")
                return False
    return True

def is_terminal_node(board):
    """ minimax helper function,
        returns False is game continues,
        True if all chips used or one of the players won """
    if CHIP_COUNT == 42:  # all chips used
        return True
    if check_if_game_active(board, 1) == False or check_if_game_active(board, 2) == False:
        return True       # one of the players won
    return False

def minimax(board, depth, maximizing_player):
    """ minimax function that determins the best move for the AI """
    terminal_node = is_terminal_node(board)
    if depth == 0 or terminal_node == True:  # game ends
        print("depth == 0 or terminal_node == True")
        # return the heuristic value of node
    free_columns = all_free_columns(board)
    if maximizing_player:
        value = -math.inf
        best_col = -1
        for col in free_columns:
            row = next_free_row(board, col)
            # value = max(value, minimax(child, depth - 1, False))
        return value  # value_new?
    else:  # minimizing player
        value = math.inf
        best_col = -1
        for col in free_columns:
            row = next_free_row(board, col)
            # value = min(value, minimax(child, depth - 1, True))
        return value  # value_new?

N_ROWS = 6
N_COLUMNS = 7
board = create_game_board(N_ROWS, N_COLUMNS)
print_board(board)
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
draw_board(board)
pygame.display.update()

print("game started")
# game runs in this while loop until somebody wins or all 42 chips are used
while GAME_ACTIVE:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION and TURN == 1:
            pygame.draw.rect(screen, black, (0, 0, WIDTH, SLOT_SIZE))
            posx = event.pos[0]
            if TURN == 1:
                pygame.draw.circle(screen, red, (posx, int(SLOT_SIZE/2)), RADIUS)
            elif TURN == 2:
                pygame.draw.circle(screen, yellow, (posx, int(SLOT_SIZE/2)), RADIUS)
        pygame.display.update()
        # Player 1, human
        if TURN == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, black, (0, 0, WIDTH, SLOT_SIZE))
                if TURN == 1:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SLOT_SIZE))
                    row = next_free_row(board, col)
                    if board[N_ROWS-1][col] == 0:
                        drop_chip(board, row, col, 1)
                print_board(board)
                draw_board(board)
                GAME_ACTIVE = check_if_game_active(board, 1)
                if GAME_ACTIVE == False:
                    break
        # Player 2, AI
        elif TURN == 2:
            pygame.time.wait(1000)
            col = 0
            # all_free_columns function should be used here
            while True:
                col = random.randint(0, 6)
                row = next_free_row(board, col)
                print("player 2 row-col:", row, col)
                if board[N_ROWS-1][col] == 0:
                    drop_chip(board, row, col, 2)
                    break
            print_board(board)
            draw_board(board)
            GAME_ACTIVE = check_if_game_active(board, 2)
            if GAME_ACTIVE == False:
                break
print("game ended")
