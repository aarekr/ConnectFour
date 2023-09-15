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
    board[row][col] = chip
    if turn == 1: turn = 2
    elif turn == 2: turn = 1
    return turn

def next_free_row(board, col):
    for row in range(n_rows):
        if board[row][col] == 0:
            return row

def check_if_4_in_row(board, player):
    print("checking winner")
    # one of the if statements has to be removed in each loop
    for row in range(n_rows-3):
        for col in range(n_columns-3):
            if board[row][col] == 1 and board[row+1][col] == 1 and board[row+2][col] == 1 and board[row+3][col] == 1:
                print("player 1 won")
                return False
            if board[row][col] == 2 and board[row+1][col] == 2 and board[row+2][col] == 2 and board[row+3][col] == 2:
                print("player 2 won")
                return False
    for row in range(n_rows-3):
        for col in range(n_columns-3):
            if board[row][col] == 1 and board[row][col+1] == 1 and board[row][col+2] == 1 and board[row][col+3] == 1:
                print("player 1 won")
                return False
            if board[row][col] == 2 and board[row][col+1] == 2 and board[row][col+2] == 2 and board[row][col+3] == 2:
                print("player 2 won")
                return False
    for row in range(n_rows-3):
        for col in range(n_columns-3):
            if board[row][col] == 1 and board[row+1][col+1] == 1 and board[row+2][col+2] == 1 and board[row+3][col+3] == 1:
                print("player 1 won")
                return False
            if board[row][col] == 2 and board[row+1][col+1] == 2 and board[row+2][col+2] == 2 and board[row+3][col+3] == 2:
                print("player 2 won")
                return False
    for row in range(3, n_rows):
        for col in range(n_columns-3):
            if board[row][col] == 1 and board[row-1][col+1] == 1 and board[row-2][col+2] == 1 and board[row-3][col+3] == 1:
                print("player 1 won")
                return False
            if board[row][col] == 2 and board[row-1][col+1] == 2 and board[row-2][col+2] == 2 and board[row-3][col+3] == 2:
                print("player 2 won")
                return False
    return True

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
                        game_active = check_if_4_in_row(board, turn)
                print_board(board)
                draw_board(board)
        # Player == 2, AI
        elif turn == 2:
            pygame.time.wait(1000)
            col = 0
            while True:
                col = random.randint(0,5)
                row = next_free_row(board, col)
                print("player 2 row-col:", row, col)
                if board[n_rows-1][col] == 0:
                    drop_chip(board, row, col, 2)
                    game_active = check_if_4_in_row(board, turn)
                    break
            print_board(board)
            draw_board(board)
print("game ended")

