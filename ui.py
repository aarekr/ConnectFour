""" Connect Four Game - User Interface """

import sys
import math
import pygame
import numpy as np
import ai

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

N_ROWS = 6
N_COLUMNS = 7
SLOT_SIZE = 100
RADIUS = int(SLOT_SIZE/2 - 5)
HEIGHT = (N_ROWS + 1) * SLOT_SIZE
WIDTH = N_COLUMNS * SLOT_SIZE
BOARD_SIZE = (HEIGHT, WIDTH)

def create_game_board(rows, columns):
    """ creating the game board """
    board = np.zeros((rows, columns), dtype=int)
    return board

def print_board(board):
    """ printing slots and chips in console """
    print(np.flip(board, 0))

def game_start_text(turn):
    """ printing who starts the game in top part of the game board window """
    text_font = pygame.font.Font(pygame.font.get_default_font(), 60)
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

class UI:
    """ User interface for the game """

    def __init__(self):
        self.board = create_game_board(N_ROWS, N_COLUMNS)
        self.game_active = True
        self.screen = pygame.display.set_mode(BOARD_SIZE)

    def draw_board(self, board):
        """ drawing the game board in a window """
        # drawing the blue game board and white empty slots
        for col in range(N_COLUMNS):
            for row in range(N_ROWS):
                pygame.draw.rect(self.screen, BLUE, (col*SLOT_SIZE, row*SLOT_SIZE+SLOT_SIZE,
                                                     SLOT_SIZE, SLOT_SIZE))
                pygame.draw.circle(self.screen, WHITE, (int(col*SLOT_SIZE+SLOT_SIZE/2),
                                                        int(row*SLOT_SIZE+SLOT_SIZE+
                                                            SLOT_SIZE/2)), RADIUS)
        # drawing players' red and yellow chips
        for col in range(N_COLUMNS):
            for row in range(N_ROWS):
                if board[row][col] == 1:
                    pygame.draw.circle(self.screen, RED, (int(col*SLOT_SIZE+SLOT_SIZE/2),
                                                          HEIGHT-int(row*SLOT_SIZE+
                                                                     SLOT_SIZE/2)), RADIUS)
                elif board[row][col] == 2:
                    pygame.draw.circle(self.screen, YELLOW, (int(col*SLOT_SIZE+SLOT_SIZE/2),
                                                             HEIGHT-int(row*SLOT_SIZE+
                                                                        SLOT_SIZE/2)), RADIUS)
        pygame.display.update()

    def handle_game_end_in_console(self, winner):
        """ Prints game result in console """
        print("Game ended")
        announcing_winner = ""
        if winner == 0:
            announcing_winner = "Draw"
        elif winner == 1:
            announcing_winner = "You won!"
        elif winner == 2:
            announcing_winner = "AI won..."
        print_board(self.board)
        return announcing_winner

    def game_loop(self):
        """ main function calls this function that starts the game """
        # add an option here where player is asked who starts
        # or let the game choose randomly in initialize_random_turn()
        turn = ai.initialize_random_turn()
        print_board(self.board)
        pygame.init()
        self.screen.blit(game_start_text(turn), (250, 15))
        self.draw_board(self.board)
        pygame.display.update()

        print("Game started")
        # game runs in this while loop until somebody wins or all 42 chips are used
        while self.game_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self.screen, BLACK, (0, 0, WIDTH, SLOT_SIZE))
                    posx = event.pos[0]
                    if turn == 1:
                        pygame.draw.circle(self.screen, RED, (posx, int(SLOT_SIZE/2)), RADIUS)
                pygame.display.update()
                # Player 1, human player
                if turn == 1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.draw.rect(self.screen, BLACK, (0, 0, WIDTH, SLOT_SIZE))
                        posx = event.pos[0]
                        col = int(math.floor(posx/SLOT_SIZE))
                        row = ai.next_free_row(self.board, col)
                        if self.board[N_ROWS-1][col] == 0:
                            ai.drop_chip(self.board, row, col, 1)
                        print_board(self.board)
                        self.draw_board(self.board)
                        self.game_active = ai.check_if_game_active(self.board, 1)
                        if not self.game_active:
                            winner = 1
                            self.screen.blit(game_end_text(winner), (250, 15))
                            self.draw_board(self.board)
                            pygame.time.wait(3000)
                            break
                        turn = 2
                # Player 2, AI
                elif turn == 2:
                    # pygame.time.wait(1000)  # uncomment and give time value if delay wanted
                    best_col = ai.AI().minimax(self.board, 3, -math.inf, math.inf, True)[1]
                    ai.drop_chip(self.board, 0, best_col, 2)
                    print_board(self.board)
                    self.draw_board(self.board)
                    self.game_active = ai.check_if_game_active(self.board, 2)
                    if not self.game_active:
                        winner = 2
                        self.screen.blit(game_end_text(winner), (250, 15))
                        self.draw_board(self.board)
                        pygame.time.wait(3000)
                        break
                    turn = 1
                # checking if all chips are dropped
                if ai.get_chip_count(self.board) == 42:
                    winner = 0
                    self.screen.blit(game_end_text(winner), (250, 15))
                    self.draw_board(self.board)
                    pygame.time.wait(3000)
                    self.game_active = False
                    break
        print(self.handle_game_end_in_console(winner))
