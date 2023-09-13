import numpy as np
import pygame
import sys

blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)

# creating the game board
n_rows = 6
n_columns = 7
board = np.zeros((n_rows, n_columns))

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
                pygame.draw.circle(screen, yellow, (col*slot_size+slot_size/2), height-int(row*slot_size+slot_size/2), radius)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, red, (col*slot_size+slot_size/2), height-int(row*slot_size+slot_size/2), radius)
    pygame.display.update()

print_board(board)
pygame.init()

# creating the game window
slot_size = 100
height = (n_rows + 1) * slot_size
width = n_columns * slot_size
board_size = (n_rows * slot_size, n_columns * slot_size)
radius = int(slot_size/2 - 5)
screen = pygame.display.set_mode(board_size)
draw_board(board)

print("game started")
pygame.time.wait(5000)
print("game ended")


