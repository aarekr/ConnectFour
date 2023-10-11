""" Connect Four Game - User Interface """

import sys
import math
import pygame
import helper_functions as hf

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

class UI:
    """ User interface for the game """

    def __init__(self):
        self.board = hf.create_game_board(N_ROWS, N_COLUMNS)
        self.game_active = True
        self.screen = pygame.display.set_mode(BOARD_SIZE)

    def game_start_text(self, turn):
        """ printing who starts the game in top part of the game board window """
        text_font = pygame.font.SysFont("Comic Sans MS", 60)
        who_starts = ""
        if turn == 1:
            who_starts = "You start"
        elif turn == 2:
            who_starts = "AI starts"
        label = text_font.render(who_starts, 0, YELLOW)
        return label

    def game_end_text(self, winner):
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

    def minimax(self, board, depth, alpha, beta, maximizing_player):  # Too many arguments (6/5)
        """ minimax function that determins the best move for the AI """
        terminal_node, winner = hf.is_terminal_node(board)
        if depth == 0 or terminal_node:  # recursion ends
            # return the heuristic value of node
            if depth == 0:
                return hf.get_position_value(board, maximizing_player), 0
            if terminal_node and winner == 1:
                return -9999999, 0  # this return value should announce winner?
            if terminal_node and winner == 2:
                return 9999999, 0  # this return value should announce winner?
        free_columns = hf.all_free_columns(board)
        if maximizing_player:
            value = -math.inf
            best_col = -1
            for col in free_columns:
                row = hf.next_free_row(board, col)
                minimax_board = board.copy()
                hf.drop_chip(minimax_board, row, col, 2)  # dropping AI chip
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
        for col in free_columns:
            row = hf.next_free_row(board, col)
            minimax_board = board.copy()
            hf.drop_chip(minimax_board, row, col, 1)  # dropping human player chip
            minimax_value = self.minimax(minimax_board, depth-1, alpha, beta, True)[0]
            if minimax_value < value:
                value = minimax_value
                best_col = col
            if value < alpha:
                break
            beta = min(beta, value)
        return value, best_col

    def handle_game_end_in_console(self, winner):
        """ Prints game result in console """
        print("game ended")
        announcing_winner = ""
        if winner == 1:
            announcing_winner = "You won!"
        elif winner == 2:
            announcing_winner = "AI won..."
        hf.print_board(self.board)
        return announcing_winner

    def game_loop(self):
        """ main function calls this function that starts the game """
        # add an option here where player is asked who starts
        # or let the game choose randomly in initialize_random_turn()
        turn = hf.initialize_random_turn()
        hf.print_board(self.board)
        pygame.init()
        self.screen.blit(self.game_start_text(turn), (250, 15))
        self.draw_board(self.board)
        pygame.display.update()

        print("game started")
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
                        row = hf.next_free_row(self.board, col)
                        if self.board[N_ROWS-1][col] == 0:
                            hf.drop_chip(self.board, row, col, 1)
                        hf.print_board(self.board)
                        self.draw_board(self.board)
                        self.game_active = hf.check_if_game_active(self.board, 1)
                        if not self.game_active:
                            winner = 1
                            self.screen.blit(self.game_end_text(winner), (250, 15))
                            break
                        turn = 2
                # Player 2, AI
                elif turn == 2:
                    # pygame.time.wait(1000)  # uncomment and give time value if delay wanted
                    best_col = self.minimax(self.board, 3, -math.inf, math.inf, True)[1]
                    hf.drop_chip(self.board, 0, best_col, 2)
                    hf.print_board(self.board)
                    self.draw_board(self.board)
                    self.game_active = hf.check_if_game_active(self.board, 2)
                    if not self.game_active:
                        winner = 2
                        self.screen.blit(self.game_end_text(winner), (250, 15))
                        self.draw_board(self.board)
                        pygame.time.wait(3000)
                        break
                    turn = 1
                # checking if there are chips available
                if hf.get_chip_count(self.board) == 42:
                    self.screen.blit(self.game_end_text(winner), (250, 15))
                    self.game_active = False
                    break
        print(self.handle_game_end_in_console(winner))
