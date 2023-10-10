""" Connect Four Game - User Interface """

import sys
import math
import pygame
import helper_functions as hf

black = (0, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)

SLOT_SIZE = 100
RADIUS = int(SLOT_SIZE/2 - 5)

class UI:  # class has too many instance attributes 8/7 (pylint), remove one of them
    """ User interface for the game """

    def __init__(self):
        self.n_rows = 6
        self.n_columns = 7
        self.board = hf.create_game_board(self.n_rows, self.n_columns)
        self.game_active = True
        # creating the game window
        self.height = (self.n_rows + 1) * SLOT_SIZE
        self.width = self.n_columns * SLOT_SIZE
        self.board_size = (self.height, self.width)
        self.screen = pygame.display.set_mode(self.board_size)

    def game_start_text(self, turn):
        """ printing who starts the game in top part of the game board window """
        text_font = pygame.font.SysFont("Comic Sans MS", 60)
        who_starts = ""
        if turn == 1:
            who_starts = "You start"
        elif turn == 2:
            who_starts = "AI starts"
        label = text_font.render(who_starts, 0, yellow)
        self.screen.blit(label, (250, 15))

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
        label = text_font.render(end_text, 0, yellow)
        self.screen.blit(label, (250, 15))

    def draw_board(self, board):
        """ drawing the game board in a window """
        # drawing the blue game board and white empty slots
        for col in range(self.n_columns):
            for row in range(self.n_rows):
                pygame.draw.rect(self.screen, blue, (col*SLOT_SIZE,
                                                     row*SLOT_SIZE+SLOT_SIZE,
                                                     SLOT_SIZE, SLOT_SIZE))
                pygame.draw.circle(self.screen, white, (int(col*SLOT_SIZE+SLOT_SIZE/2),
                                                        int(row*SLOT_SIZE+SLOT_SIZE+
                                                            SLOT_SIZE/2)), RADIUS)
        # drawing players' red and yellow chips
        for col in range(self.n_columns):
            for row in range(self.n_rows):
                if board[row][col] == 1:
                    pygame.draw.circle(self.screen, red, (int(col*SLOT_SIZE+SLOT_SIZE/2),
                                                          self.height-
                                                          int(row*SLOT_SIZE+
                                                              SLOT_SIZE/2)), RADIUS)
                elif board[row][col] == 2:
                    pygame.draw.circle(self.screen, yellow, (int(col*SLOT_SIZE+
                                                                 SLOT_SIZE/2),
                                                             self.height-
                                                             int(row*SLOT_SIZE+
                                                                 SLOT_SIZE/2)), RADIUS)
        pygame.display.update()

    def next_free_row(self, board, col):
        """ returning the lowest free row in the given column """
        free_row = -1
        for row in range(self.n_rows):
            if board[row][col] == 0:
                free_row = row
                break
        return free_row

    def all_free_columns(self, board):
        """ returning a list of columns that have at least one free slot/row """
        free_columns = []
        for col in range(self.n_columns):
            if board[self.n_rows-1][col] == 0:  # at least top row in column is empty
                free_columns.append(col)
        return free_columns

    def drop_chip(self, board, row, col, turn):
        """ player drops their chip and TURN is given to the other player """
        row = self.next_free_row(board, col)
        board[row][col] = turn
        if turn == 1:
            turn = 2
        elif turn == 2:
            turn = 1
        return turn

    def check_if_game_active(self, board, player):
        """ checking if the player has 4 chips in row/column/diagonal
            returning False if game ends and True if stays active """
        # Rows
        for row in range(self.n_rows):
            for col in range(self.n_columns-3):
                if (board[row][col] ==
                        board[row][col+1] ==
                        board[row][col+2] ==
                        board[row][col+3] == player):
                    return False
        # Columns
        for col in range(self.n_columns):
            for row in range(self.n_rows-3):
                if (board[row][col] ==
                        board[row+1][col] ==
                        board[row+2][col] ==
                        board[row+3][col] == player):
                    return False
        # Positive diagonals
        for row in range(self.n_rows-3):
            for col in range(self.n_columns-3):
                if (board[row][col] ==
                        board[row+1][col+1] ==
                        board[row+2][col+2] ==
                        board[row+3][col+3] == player):
                    return False
        # Negative diagonals
        for col in range(self.n_columns-3):
            for row in range(self.n_rows-3):
                if (board[self.n_rows-1-row][col] ==
                        board[self.n_rows-1-row-1][col+1] ==
                        board[self.n_rows-1-row-2][col+2] ==
                        board[self.n_rows-1-row-3][col+3] == player):
                    return False
        return True

    def get_position_value(self, board, player):
        """ calculates the optimal position value for the AI """
        position_value = 0

        # Horizontal counting
        for row in range(self.n_rows):
            for col in range(self.n_columns-3):
                four_consequtive_slots = [board[row][col],
                                          board[row][col+1],
                                          board[row][col+2],
                                          board[row][col+3]]
                position_value += hf.count_ai_position_value_points(four_consequtive_slots, player)
                position_value += hf.count_human_position_value_points(four_consequtive_slots, 1)

        # Vertical counting
        for col in range(self.n_columns):
            for row in range(self.n_rows-3):
                four_consequtive_slots = [board[row][col],
                                          board[row+1][col],
                                          board[row+2][col],
                                          board[row+3][col]]
                position_value += hf.count_ai_position_value_points(four_consequtive_slots, player)
                position_value += hf.count_human_position_value_points(four_consequtive_slots, 1)

        # Positive diagonal counting
        for row in range(self.n_rows-3):
            for col in range(self.n_columns-3):
                four_consequtive_slots = [board[row][col],
                                          board[row+1][col+1],
                                          board[row+2][col+2],
                                          board[row+3][col+3]]
                position_value += hf.count_ai_position_value_points(four_consequtive_slots, player)
                position_value += hf.count_human_position_value_points(four_consequtive_slots, 1)

        # Negative diagonal counting
        for col in range(self.n_columns-3):
            for row in range(self.n_rows-3):
                four_consequtive_slots = [board[self.n_rows-1-row][col],
                                          board[self.n_rows-1-row-1][col+1],
                                          board[self.n_rows-1-row-2][col+2],
                                          board[self.n_rows-1-row-3][col+2]]
                position_value += hf.count_ai_position_value_points(four_consequtive_slots, player)
                position_value += hf.count_human_position_value_points(four_consequtive_slots, 1)

        return position_value

    def is_terminal_node(self, board):
        """ minimax helper function,
            returns False if game continues,
            returns tuple (True, draw(0)/winner(1 or 2)) if all chips used or
            one of the players won """
        if hf.get_chip_count(board) == 42:  # all chips used and draw (0)
            return True, 0
        if not self.check_if_game_active(board, 1):  # human player won (1)
            return True, 1
        if not self.check_if_game_active(board, 2):  # AI won (2)
            return True, 2
        return False, -1  # game continues, no winner or draw

    def minimax(self, board, depth, alpha, beta, maximizing_player):  # Too many arguments (6/5)
        """ minimax function that determins the best move for the AI """
        terminal_node, winner = self.is_terminal_node(board)
        if depth == 0 or terminal_node:  # recursion ends
            # return the heuristic value of node
            if depth == 0:
                return self.get_position_value(board, maximizing_player), 0
            if terminal_node and winner == 1:
                return -9999999, 0  # this return value should announce winner?
            if terminal_node and winner == 2:
                return 9999999, 0  # this return value should announce winner?
        free_columns = self.all_free_columns(board)
        if maximizing_player:
            value = -math.inf
            best_col = -1
            for col in free_columns:
                row = self.next_free_row(board, col)
                minimax_board = board.copy()
                self.drop_chip(minimax_board, row, col, 2)  # dropping AI chip
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
            row = self.next_free_row(board, col)
            minimax_board = board.copy()
            self.drop_chip(minimax_board, row, col, 1)  # dropping human player chip
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
        if winner == 1:
            print("You won!")
        elif winner == 2:
            print("AI won...")
        hf.print_board(self.board)

    def game_loop(self):
        """ main function calls this function that starts the game """
        # add an option here where player is asked who starts
        # or let the game choose randomly in initialize_random_turn()
        turn = hf.initialize_random_turn()
        hf.print_board(self.board)
        pygame.init()
        self.game_start_text(turn)
        self.draw_board(self.board)
        pygame.display.update()

        print("game started")
        # game runs in this while loop until somebody wins or all 42 chips are used
        while self.game_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self.screen, black, (0, 0, self.width, SLOT_SIZE))
                    posx = event.pos[0]
                    if turn == 1:
                        pygame.draw.circle(self.screen, red, (posx, int(SLOT_SIZE/2)), RADIUS)
                pygame.display.update()
                # Player 1, human player
                if turn == 1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.draw.rect(self.screen, black, (0, 0, self.width, SLOT_SIZE))
                        posx = event.pos[0]
                        col = int(math.floor(posx/SLOT_SIZE))
                        row = self.next_free_row(self.board, col)
                        if self.board[self.n_rows-1][col] == 0:
                            self.drop_chip(self.board, row, col, 1)
                        hf.print_board(self.board)
                        self.draw_board(self.board)
                        self.game_active = self.check_if_game_active(self.board, 1)
                        if not self.game_active:
                            winner = 1
                            self.game_end_text(winner)
                            break
                        turn = 2
                # Player 2, AI
                elif turn == 2:
                    # pygame.time.wait(1000)
                    best_col = self.minimax(self.board, 3, -math.inf, math.inf, True)[1]
                    self.drop_chip(self.board, 0, best_col, 2)
                    hf.print_board(self.board)
                    self.draw_board(self.board)
                    self.game_active = self.check_if_game_active(self.board, 2)
                    if not self.game_active:
                        winner = 2
                        self.game_end_text(winner)
                        self.draw_board(self.board)
                        pygame.time.wait(3000)
                        break
                    turn = 1
                # checking if there are chips available
                if hf.get_chip_count(self.board) == 42:
                    self.game_end_text(winner)
                    self.game_active = False
                    break
        self.handle_game_end_in_console(winner)
