from typing import List


# Time complexity is O(n^2) where n is the sudoku size board
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    # TODO - you fill in here.
    def is_valid_sudoku_square(start_row: int, start_col: int) -> bool:
        set_square = [0] * 10
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if partial_assignment[r][c] == 0: continue
                if set_square[partial_assignment[r][c]]:
                    return False
                set_square[partial_assignment[r][c]] = 1
        return True

    def is_valid_column(column: int):
        set_column = [0] * 10
        for r in range(0, len(partial_assignment)):
            if partial_assignment[r][column] == 0: continue
            if set_column[partial_assignment[r][column]]:
                return False
            set_column[partial_assignment[r][column]] = 1
        return True

    def is_valid_row(row: int):
        set_row = [0] * 10
        for c in range(0, len(partial_assignment[0])):
            if partial_assignment[row][c] == 0: continue
            if set_row[partial_assignment[row][c]]:
                return False
            set_row[partial_assignment[row][c]] = 1
        return True

    for row in range(len(partial_assignment)):
        if not is_valid_row(row):
            return False
        if not is_valid_column(row):
            return False

    for r in range(0, 7, 3):
        for c in range(0, 7, 3):
            if not is_valid_sudoku_square(r, c):
                return False
    return True
