import numpy as np
import pygame
import sys
import math
import random

black = (0, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
global turn
turn = random.randint(1,2)  # game starter chosen randomly: 1=human, 2=AI
global chip_count  # counting total number of chips players have dropped
chip_count = 0

# creating the game board
n_rows = 6
n_columns = 7
board = np.zeros((n_rows, n_columns))

def game_start_text():
    who_starts = ""
    if turn == 1:
        who_starts = "You start"
    elif turn == 2:
        who_starts = "AI starts"
    label = text_font.render(who_starts, 0, yellow)
    screen.blit(label, (250, 15))

# printing slots and chips in console
def print_board(board):
    print(np.flip(board, 0))

# drawing the game board in a window
def draw_board(board):
    for col in range(n_columns):
        for row in range(n_rows):
            pygame.draw.rect(screen, blue, (col*slot_size, row*slot_size+slot_size, slot_size, slot_size))
            pygame.draw.circle(screen, white, (int(col*slot_size+slot_size/2), int(row*slot_size+slot_size+slot_size/2)), radius)
    for col in range(n_columns):
        for row in range(n_rows):
            if board[row][col] == 1:
                pygame.draw.circle(screen, red, (int(col*slot_size+slot_size/2), height-int(row*slot_size+slot_size/2)), radius)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, yellow, (int(col*slot_size+slot_size/2), height-int(row*slot_size+slot_size/2)), radius)
    pygame.display.update()

def drop_chip(board, row, col, chip):
    global turn
    print("dropping chip:", chip)
    global chip_count
    chip_count += 1
    print("chip_count:", chip_count)
    board[row][col] = chip
    if turn == 1: turn = 2
    elif turn == 2: turn = 1
    return turn

def next_free_row(board, col):
    for row in range(n_rows):
        if board[row][col] == 0:
            return row

def all_free_columns(board):
    free_columns = []
    for col in range(n_columns):
        if board[n_rows-1][col] == 0:  # at least top row in column is empty
            free_columns.append(col)
    print("all free columns:", free_columns)
    return free_columns

def check_if_game_active(board, player):
    print("checking winner", player)
    for row in range(n_rows-3):
        for col in range(n_columns-3):
            if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                print("player", player, "won")
                return False
    for row in range(n_rows-3):
        for col in range(n_columns-3):
            if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player:
                print("player", player, "won")
                return False
    for row in range(n_rows-3):
        for col in range(n_columns-3):
            if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player:
                print("player", player, "won")
                return False
    for row in range(3, n_rows):
        for col in range(n_columns-3):
            if board[row][col] == player and board[row-1][col+1] == player and board[row-2][col+2] == player and board[row-3][col+3] == player:
                print("player", player, "won")
                return False
    return True

def is_terminal_node(board):
    if chip_count == 42:  # all chips used
        return True
    if check_if_game_active(board, 1) == False or check_if_game_active(board, 2) == False:
        return True       # one of the players won
    return False

def minimax(board, depth, maximizingPlayer):
    terminal_node = is_terminal_node(board)
    if depth == 0 or terminal_node == True:  # game ends
        print("depth == 0 or terminal_node == True")
        # return the heuristic value of node
    free_columns = all_free_columns(board)
    if maximizingPlayer:
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

print_board(board)
game_active = True
pygame.init()

# creating the game window
slot_size = 100
height = (n_rows + 1) * slot_size
width = n_columns * slot_size
board_size = (height, width)
radius = int(slot_size/2 - 5)
screen = pygame.display.set_mode(board_size)
text_font = pygame.font.SysFont("Comic Sans MS", 60)
game_start_text()
draw_board(board)
pygame.display.update()

print("game started")
print("turn:", turn)
while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION and turn == 1:
            pygame.draw.rect(screen, black, (0, 0, width, slot_size))
            posx = event.pos[0]
            if turn == 1:
                pygame.draw.circle(screen, red, (posx, int(slot_size/2)), radius)
            elif turn == 2:
                pygame.draw.circle(screen, yellow, (posx, int(slot_size/2)), radius)
        pygame.display.update()
        # Player 1, human
        if turn == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, black, (0, 0, width, slot_size))
                if turn == 1:
                    posx = event.pos[0]
                    col = int(math.floor(posx/slot_size))
                    row = next_free_row(board, col)
                    if board[n_rows-1][col] == 0:
                        drop_chip(board, row, col, 1)
                print_board(board)
                draw_board(board)
                game_active = check_if_game_active(board, 1)
                if game_active == False: break
        # Player 2, AI
        elif turn == 2:
            pygame.time.wait(1000)
            col = 0
            # all_free_columns function should be used here
            while True:
                col = random.randint(0,6)
                row = next_free_row(board, col)
                print("player 2 row-col:", row, col)
                if board[n_rows-1][col] == 0:
                    drop_chip(board, row, col, 2)
                    break
            print_board(board)
            draw_board(board)
            game_active = check_if_game_active(board, 2)
            if game_active == False: break
print("game ended")

