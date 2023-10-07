import timeit
import cProfile

# timeit test
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

test_get_chip_count = """
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

if __name__ == "__main__":
    print("Tests with timeit")
    time_all_free_columns = timeit.timeit(test_all_free_columns)
    print("  1. all_free_columns:", time_all_free_columns)
    time_next_free_row = timeit.timeit(test_next_free_row)
    print("  2. next_free_row   :", time_next_free_row)
    time_get_chip_count = timeit.timeit(test_get_chip_count)
    print("  3. get_chip_count  :", time_get_chip_count)

    print("\nTests with cProfile")
    print("  1. all_free_columns:")
    cProfile.run(test_all_free_columns_cProfile)
    print("  2. next_free_row:")
    cProfile.run(test_next_free_row_cProfile)
    print("  3. get_chip_count:")
    cProfile.run(test_get_chip_count_cProfile)
