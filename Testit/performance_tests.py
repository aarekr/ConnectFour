import timeit
import cProfile

# timeit tests
test_all_free_columns = """
import numpy as np
N_ROWS = 6
N_COLUMNS = 7
board = np.zeros((6, 7), dtype=int)
def all_free_columns(board):
    free_columns = []
    for col in range(N_COLUMNS):
        if board[N_ROWS-1][col] == 0:
            free_columns.append(col)
    return free_columns
"""

test_next_free_row = """
import numpy as np
N_ROWS = 6
N_COLUMNS = 7
board = np.zeros((6, 7), dtype=int)
col = 2
def next_free_row(board, col):
    free_row = -1
    for row in range(N_ROWS):
        if board[row][col] == 0:
            free_row = row
            break
    return free_row
"""

test_get_chip_count_2_for_loops = """
import numpy as np
N_ROWS = 6
N_COLUMNS = 7
board = np.zeros((6, 7), dtype=int)
def get_chip_count(board):
    chip_count = 0
    for row in board:  # refactor this to list comprehension
        for item in row:
            if item != 0:
                chip_count += 1
    return chip_count
"""

test_get_chip_count_list_comprehension = """
import numpy as np
N_ROWS = 6
N_COLUMNS = 7
board = np.zeros((6, 7), dtype=int)
def get_chip_count_list_comprehension(board):
    value = len([item for row in board for item in row if item != 0])
    return value
"""

test_check_if_game_active = """
import numpy as np
N_ROWS = 6
N_COLUMNS = 7
board = np.zeros((6, 7), dtype=int)
def check_if_game_active(board, player):
    for row in range(N_ROWS):
        for col in range(N_COLUMNS-3):
            if (board[row][col] == board[row][col+1] ==
                    board[row][col+2] == board[row][col+3] == player):
                return False
    for col in range(N_COLUMNS):
        for row in range(N_ROWS-3):
            if (board[row][col] == board[row+1][col] ==
                    board[row+2][col] == board[row+3][col] == player):
                return False
    for row in range(N_ROWS-3):
        for col in range(N_COLUMNS-3):
            if (board[row][col] == board[row+1][col+1] ==
                    board[row+2][col+2] == board[row+3][col+3] == player):
                return False
    for col in range(N_COLUMNS-3):
        for row in range(N_ROWS-3):
            if (board[N_ROWS-1-row][col] == board[N_ROWS-1-row-1][col+1] ==
                    board[N_ROWS-1-row-2][col+2] == board[N_ROWS-1-row-3][col+3] == player):
                return False
    return True
"""

# cProfile tests
test_all_free_columns_cProfile = """
import numpy as np
N_ROWS = 6
N_COLUMNS = 7
board = np.zeros((6, 7), dtype=int)
for i in range(10000000):
    def all_free_columns(board):
        free_columns = []
        for col in range(N_COLUMNS):
            if board[N_ROWS-1][col] == 0:
                free_columns.append(col)
        return free_columns
"""

test_next_free_row_cProfile = """
import numpy as np
import random
N_ROWS = 6
N_COLUMNS = 7
board = np.zeros((6, 7), dtype=int)
for i in range(1000000):
    col = random.randint(0,6)
    def next_free_row(board, col):
        free_row = -1
        for row in range(N_ROWS):
            if board[row][col] == 0:
                free_row = row
                break
        return free_row
"""

test_get_chip_count_cProfile = """
import numpy as np
N_ROWS = 6
N_COLUMNS = 7
board = np.zeros((6, 7), dtype=int)
for i in range(10000000):
    def get_chip_count(board):
        chip_count = 0
        for row in board:  # refactor this to list comprehension
            for item in row:
                if item != 0:
                    chip_count += 1
        return chip_count
"""

test_check_if_game_active_cProfile = """
import numpy as np
N_ROWS = 6
N_COLUMNS = 7
board = np.zeros((6, 7), dtype=int)
for i in range(10000000):
    def check_if_game_active(board, player):
        for row in range(N_ROWS):
            for col in range(N_COLUMNS-3):
                if (board[row][col] == board[row][col+1] ==
                        board[row][col+2] == board[row][col+3] == player):
                    return False
        for col in range(N_COLUMNS):
            for row in range(N_ROWS-3):
                if (board[row][col] == board[row+1][col] ==
                        board[row+2][col] == board[row+3][col] == player):
                    return False
        for row in range(N_ROWS-3):
            for col in range(N_COLUMNS-3):
                if (board[row][col] == board[row+1][col+1] ==
                        board[row+2][col+2] == board[row+3][col+3] == player):
                    return False
        for col in range(N_COLUMNS-3):
            for row in range(N_ROWS-3):
                if (board[N_ROWS-1-row][col] == board[N_ROWS-1-row-1][col+1] ==
                        board[N_ROWS-1-row-2][col+2] == board[N_ROWS-1-row-3][col+3] == player):
                    return False
        return True
"""

if __name__ == "__main__":
    print("Tests with timeit")
    time_all_free_columns = timeit.timeit(test_all_free_columns)
    print("  1. all_free_columns:", time_all_free_columns)
    time_next_free_row = timeit.timeit(test_next_free_row)
    print("  2. next_free_row   :", time_next_free_row)
    time_get_chip_count_2_for_loops = timeit.timeit(test_get_chip_count_2_for_loops)
    print("  3a. get_chip_count_2_for_loops       :", time_get_chip_count_2_for_loops)
    time_get_chip_count_list_comprehension = timeit.timeit(test_get_chip_count_list_comprehension)
    print("  3b. get_chip_count_list_comprehension:", test_get_chip_count_list_comprehension)
    time_check_if_game_active = timeit.timeit(test_check_if_game_active)
    print("  4. check_if_game_active:", time_check_if_game_active)

    print("\nTests with cProfile")
    print("  1. all_free_columns:")
    cProfile.run(test_all_free_columns_cProfile)
    print("  2. next_free_row:")
    cProfile.run(test_next_free_row_cProfile)
    print("  3. get_chip_count:")
    cProfile.run(test_get_chip_count_cProfile)
    print("  4. check_if_game_active:")
    cProfile.run(test_check_if_game_active_cProfile)
