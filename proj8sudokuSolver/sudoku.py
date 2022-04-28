# Sudoku Solver
from pprint import pprint
def find_next_empty(puzzle):

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None # if no spaces in the puzzle are empty (-1)

def is_valid(puzzle, guess, row, col):
    # check valid row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    # check for valid column
    col_vals = [puzzle[i][col] for i in range(9)] # append values of i row at col column
    if guess in col_vals:
        return False

    # for 3*3 matrix
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    # if false does not come, we may return true
    return True

        
def solve_sudoku(puzzle):

    row, col = find_next_empty(puzzle)

    if row is None:
        return True

    for guess in range(1, 10):
        # check if valid guess
        if is_valid(puzzle, guess, row, col):
            # if this is valid, then place that guess on the puzzle
            puzzle[row][col] = guess

            if solve_sudoku(puzzle):
                return True

    # if not valid or if our guess does not solve the puzzle, then we need to backtrack and try a new number

        puzzle[row][col] = -1

    # if none of the numbers that we try word, then this puzzle is UNSOLVABLE
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9,-1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],


        [-1, 5,-1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1], 
    ]

    print(solve_sudoku(example_board))
    pprint(example_board)

