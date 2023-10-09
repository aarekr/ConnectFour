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

class UI:  # class has too many instance attributes 12/7 and should be split
    """ User interface for the game """

    def __init__(self):
        self.n_rows = 6
        self.n_columns = 7
        self.board = self.create_game_board(self.n_rows, self.n_columns)
        self.turn = 0
        self.game_active = True
        self.winner = 0
        # creating the game window
        self.slot_size = 100
        self.height = (self.n_rows + 1) * self.slot_size
        self.width = self.n_columns * self.slot_size
        self.board_size = (self.height, self.width)
        self.radius = int(self.slot_size/2 - 5)
        self.screen = pygame.display.set_mode(self.board_size)
        #self.text_font = pygame.font.SysFont("Comic Sans MS", 60)

    def create_game_board(self, rows, columns):
        """ creating the game board """
        board = np.zeros((rows, columns), dtype=int)
        return board

    def initialize_random_turn(self):
        """ starting player chosen randomly """
        turn = random.randint(1, 2)  # game starter chosen randomly: 1=human (red), 2=AI (yellow)
        return turn

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

    def print_board(self, board):
        """ printing slots and chips in console """
        print(np.flip(board, 0))

    def get_chip_count(self, board):
        """ returning the number of chips players have dropped """
        chip_count = 0
        for row in board:  # refactor this
            for item in row:
                if item != 0:
                    chip_count += 1
        return chip_count

    def draw_board(self, board):
        """ drawing the game board in a window """
        # drawing the blue game board and white empty slots
        for col in range(self.n_columns):
            for row in range(self.n_rows):
                pygame.draw.rect(self.screen, blue, (col*self.slot_size,
                                                     row*self.slot_size+self.slot_size,
                                                     self.slot_size, self.slot_size))
                pygame.draw.circle(self.screen, white, (int(col*self.slot_size+self.slot_size/2),
                                                        int(row*self.slot_size+self.slot_size+
                                                            self.slot_size/2)), self.radius)
        # drawing players' red and yellow chips
        for col in range(self.n_columns):
            for row in range(self.n_rows):
                if board[row][col] == 1:
                    pygame.draw.circle(self.screen, red, (int(col*self.slot_size+self.slot_size/2),
                                                          self.height-
                                                          int(row*self.slot_size+
                                                              self.slot_size/2)), self.radius)
                elif board[row][col] == 2:
                    pygame.draw.circle(self.screen, yellow, (int(col*self.slot_size+
                                                                 self.slot_size/2),
                                                             self.height-
                                                             int(row*self.slot_size+
                                                                 self.slot_size/2)), self.radius)
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

    def drop_chip(self, board, row, col, chip):
        """ player drops their chip and TURN is given to the other player """
        # this global variable causes a pylint error, so it should be replaced
        row = self.next_free_row(board, col)
        board[row][col] = chip
        if self.turn == 1:
            self.turn = 2
        elif self.turn == 2:
            self.turn = 1
        return self.turn

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

    def count_ai_position_value_points(self, four_consequtive_slots, player):
        """ counts the AI position value for 4 consequtive slots """
        position_value = 0
        if four_consequtive_slots.count(player) == 3 and four_consequtive_slots.count(0) == 1:
            position_value += 30
        elif four_consequtive_slots.count(player) == 2 and four_consequtive_slots.count(0) == 2:
            position_value += 10
        return position_value

    def count_human_position_value_points(self, four_consequtive_slots, player):
        """ counts the human player position value for 4 consequtive slots
            AI gets negative points for certain human player chip positions """
        position_value = 0
        if four_consequtive_slots.count(player) == 3 and four_consequtive_slots.count(0) == 1:
            position_value -= 90
        elif four_consequtive_slots.count(player) == 2 and four_consequtive_slots.count(0) == 2:
            position_value -= 20
        return position_value

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
                position_value += self.count_ai_position_value_points(four_consequtive_slots,
                                                                      player)
                position_value += self.count_human_position_value_points(four_consequtive_slots, 1)

        # Vertical counting
        for col in range(self.n_columns):
            for row in range(self.n_rows-3):
                four_consequtive_slots = [board[row][col],
                                          board[row+1][col],
                                          board[row+2][col],
                                          board[row+3][col]]
                position_value += self.count_ai_position_value_points(four_consequtive_slots,
                                                                      player)
                position_value += self.count_human_position_value_points(four_consequtive_slots, 1)

        # Positive diagonal counting
        for row in range(self.n_rows-3):
            for col in range(self.n_columns-3):
                four_consequtive_slots = [board[row][col],
                                          board[row+1][col+1],
                                          board[row+2][col+2],
                                          board[row+3][col+3]]
                position_value += self.count_ai_position_value_points(four_consequtive_slots,
                                                                      player)
                position_value += self.count_human_position_value_points(four_consequtive_slots, 1)

        # Negative diagonal counting
        for col in range(self.n_columns-3):
            for row in range(self.n_rows-3):
                four_consequtive_slots = [board[self.n_rows-1-row][col],
                                          board[self.n_rows-1-row-1][col+1],
                                          board[self.n_rows-1-row-2][col+2],
                                          board[self.n_rows-1-row-3][col+2]]
                position_value += self.count_ai_position_value_points(four_consequtive_slots,
                                                                      player)
                position_value += self.count_human_position_value_points(four_consequtive_slots, 1)

        return position_value

    def is_terminal_node(self, board):
        """ minimax helper function,
            returns False if game continues,
            returns tuple (True, draw(0)/winner(1 or 2)) if all chips used or
            one of the players won """
        if self.get_chip_count(board) == 42:  # all chips used and draw (0)
            return True, 0
        if not self.check_if_game_active(board, 1):  # human player won (1)
            return True, 1
        if not self.check_if_game_active(board, 2):  # AI won (2)
            return True, 2
        return False, -1  # game continues, no winner or draw

    def minimax(self, board, depth, alpha, beta, maximizing_player):
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

    def handle_game_end_in_console(self):
        """ Prints game result in console """
        print("game ended")
        if self.winner == 1:
            print("You won!")
        elif self.winner == 2:
            print("AI won...")
        self.print_board(self.board)

    def game_loop(self):
        """ main function calls this function that starts the game """
        # add an option here where player is asked who starts
        # or let the game choose randomly in initialize_random_turn()
        self.turn = self.initialize_random_turn()
        self.print_board(self.board)
        pygame.init()
        self.game_start_text(self.turn)
        self.draw_board(self.board)
        pygame.display.update()

        print("game started")
        # game runs in this while loop until somebody wins or all 42 chips are used
        while self.game_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self.screen, black, (0, 0, self.width, self.slot_size))
                    posx = event.pos[0]
                    if self.turn == 1:
                        pygame.draw.circle(self.screen, red, (posx, int(self.slot_size/2)),
                                           self.radius)
                pygame.display.update()
                # Player 1, human player
                if self.turn == 1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.draw.rect(self.screen, black, (0, 0, self.width, self.slot_size))
                        posx = event.pos[0]
                        col = int(math.floor(posx/self.slot_size))
                        row = self.next_free_row(self.board, col)
                        if self.board[self.n_rows-1][col] == 0:
                            self.drop_chip(self.board, row, col, 1)
                        self.print_board(self.board)
                        self.draw_board(self.board)
                        self.game_active = self.check_if_game_active(self.board, 1)
                        if not self.game_active:
                            self.winner = 1
                            self.game_end_text(self.winner)
                            break
                        self.turn = 2
                # Player 2, AI
                elif self.turn == 2:
                    # pygame.time.wait(1000)
                    best_col = self.minimax(self.board, 3, -math.inf, math.inf, True)[1]
                    self.drop_chip(self.board, 0, best_col, 2)
                    self.print_board(self.board)
                    self.draw_board(self.board)
                    self.game_active = self.check_if_game_active(self.board, 2)
                    if not self.game_active:
                        self.winner = 2
                        self.game_end_text(self.winner)
                        self.draw_board(self.board)
                        pygame.time.wait(3000)
                        break
                    self.turn = 1
                # checking if there are chips available
                if self.get_chip_count(self.board) == 42:
                    self.game_end_text(self.winner)
                    self.game_active = False
                    break
        self.handle_game_end_in_console()

def main():
    """ This function calls the game_loop method in UI class that starts the game """
    UI().game_loop()

if __name__ == "__main__":
    main()
