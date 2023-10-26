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
    print(np.flip(board, 0), "\n")

def game_start_text(turn):
    """ displaying who starts the game in top part of the game board window """
    text_font = pygame.font.Font(pygame.font.get_default_font(), 60)
    who_starts = ""
    if turn == 1:
        who_starts = "You start"
    elif turn == 2:
        who_starts = "AI starts"
    label = text_font.render(who_starts, 0, YELLOW)
    return label

def game_end_text(winner):
    """ displaying the game result when game ends: winner or draw """
    text_font = pygame.font.Font(pygame.font.get_default_font(), 60)
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
        """ prints game result in console """
        print("Game ended")
        announcing_winner = ""
        if winner == 0:
            announcing_winner = "Draw\n"
        elif winner == 1:
            announcing_winner = "You won!\n"
        elif winner == 2:
            announcing_winner = "AI won...\n"
        print_board(self.board)
        return announcing_winner

    def handle_game_end_in_window(self, board, winner):
        """ shows game end result in the game window """
        self.screen.blit(game_end_text(winner), (250, 15))
        self.draw_board(board)
        pygame.time.wait(3000)

    def who_starts(self):
        """ game.py calls this function where game starter is chosen """
        while True:
            pygame.init()
            pygame.draw.rect(self.screen, BLACK, (0, 0, WIDTH, SLOT_SIZE))
            text_font_question = pygame.font.Font(pygame.font.get_default_font(), 30)
            text_font_options = pygame.font.Font(pygame.font.get_default_font(), 25)
            who_starts_text = "Who starts the game?"
            starter_options_text = "R = Random, Y = You, A = AI, E = End"
            text_question = text_font_question.render(who_starts_text, 0, YELLOW)
            text_options = text_font_options.render(starter_options_text, 0, YELLOW)
            self.screen.blit(text_question, (100, 15))
            self.screen.blit(text_options, (100, 60))
            self.draw_board(self.board)
            pygame.time.wait(3000)
            who_starts = None
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    print("Player chose:", event.key, " (R=114, H=104, A=97, E=101)")
                    if event.key == pygame.K_r:    # random starter
                        who_starts = ai.initialize_random_turn()
                    elif event.key == pygame.K_y:  # human starts
                        who_starts = 1
                    elif event.key == pygame.K_a:  # AI starts
                        who_starts = 2
                    elif event.key == pygame.K_e:  # game ends
                        who_starts = "end game"
            if who_starts == None:
                continue
            if who_starts == "end game":
                break
            pygame.draw.rect(self.screen, BLACK, (0, 0, WIDTH, SLOT_SIZE))
            print("who_starts:", who_starts)
            self.board = create_game_board(N_ROWS, N_COLUMNS)
            self.game_active = True
            self.screen = pygame.display.set_mode(BOARD_SIZE)
            self.game_loop(who_starts)

    def game_loop(self, who_starts):
        """ who_starts function calls this function and game starts """
        turn = who_starts
        winner = 0
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
                        else:  # column is full, can't drop the chip here
                            continue
                        print_board(self.board)
                        self.draw_board(self.board)
                        self.game_active = ai.check_if_game_active(self.board, 1)
                        if not self.game_active:
                            winner = 1
                            self.handle_game_end_in_window(self.board, winner)
                            break
                        turn = 2

                # Player 2, AI
                elif turn == 2:
                    # pygame.time.wait(1000)  # uncomment and give time value if delay wanted
                    print("Entering minimax")
                    for depth in [0, 1, 2, 3, 4, 5, 7]:
                        if depth%2 == 0:
                            minimax_value, best_col = ai.AI().minimax(self.board, depth, -math.inf, math.inf, False)
                        elif depth%2 == 1:
                            minimax_value, best_col = ai.AI().minimax(self.board, depth, -math.inf, math.inf, True)
                        print("- depth: " + str(depth) + ", col: " + str(best_col) + ", value: " + str(minimax_value))
                        if minimax_value < -99999 or minimax_value > 99999:
                            break
                    ai.drop_chip(self.board, 0, best_col, 2)
                    print("AI chip dropped in column:", best_col)
                    print_board(self.board)
                    self.draw_board(self.board)
                    self.game_active = ai.check_if_game_active(self.board, 2)
                    if not self.game_active:
                        winner = 2
                        self.handle_game_end_in_window(self.board, winner)
                        break
                    turn = 1

                # checking if all chips are dropped
                if ai.get_chip_count(self.board) == 42:
                    winner = 0
                    self.handle_game_end_in_window(self.board, winner)
                    break
        print(self.handle_game_end_in_console(winner))
