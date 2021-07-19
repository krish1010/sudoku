from utils.constants import N


def is_valid_sudoku(board):
    if not is_in_range(board):
        return False
    unique = [False] * (N + 1)
    for i in range(N):
        for m in range(N + 1):
            unique[m] = False
        for j in range(N):
            Z = board[i][j]
            if unique[Z]:
                return False
            unique[Z] = True
    for i in range(N):
        for m in range(N + 1):
            unique[m] = False
        for j in range(N):
            Z = board[j][i]
            if unique[Z]:
                return False
            unique[Z] = True

    for i in range(0, N - 2, 3):
        for j in range(0, N - 2, 3):
            for m in range(0, N + 1):
                unique[m] = False
            for k in range(3):
                for l in range(3):
                    X = i + k
                    Y = j + l
                    Z = board[X][Y]
                    if unique[Z]:
                        return False
                    unique[Z] = True
    return True


def is_in_range(board):
    for i in range(N):
        for j in range(N):
            if ((board[i][j] <= 0) or
                    (board[i][j] > N)):
                return False
    return True


def solve_sudoku(sudoku, i=0, j=0):
    i, j = find_next_cell_to_fill(sudoku)
    if i == -1:
        return True
    for e in range(1, N + 1):
        if is_valid(sudoku, i, j, e):
            sudoku[i][j] = e
            if solve_sudoku(sudoku, i, j):
                return True
            sudoku[i][j] = 0
    return False


def is_valid(sudoku, i, j, e):
    row_ok = all([e != sudoku[i][x] for x in range(N)])
    if row_ok:
        column_ok = all([e != sudoku[x][j] for x in range(N)])
        if column_ok:
            sec_top_x, sec_top_y = 3 * (i // 3), 3 * (j // 3)
            for x in range(sec_top_x, sec_top_x + 3):
                for y in range(sec_top_y, sec_top_y + 3):
                    if sudoku[x][y] == e:
                        return False
            return True
    return False


def find_next_cell_to_fill(sudoku):
    for x in range(N):
        for y in range(N):
            if sudoku[x][y] == 0:
                return x, y
    return -1, -1
