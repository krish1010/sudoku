import requests
from flask import Blueprint, render_template, jsonify, request

home_blueprint = Blueprint('index', __name__)


@home_blueprint.route('/')
def home():
    print('here i go')
    board = get_puzzle()
    return render_template('home/home.html', value=board)


def get_puzzle():
    response = requests.request("GET", 'https://sugoku.herokuapp.com/board?difficulty=easy')
    board = response.json().get('board')
    l2 = []
    for items in board:
        l = []
        for i in range(0, len(items), 3):
            l.append(items[i: i + 3])
        l2.append(l)
    return l2


@home_blueprint.route('/solve', methods=['POST'])
def solve():
    board = request.json.get('board')
    l = []
    for i in range(0, len(board), 9):
        temp = []
        for item in board[i: i + 9]:
            try:
                temp.append(int(item))
            except ValueError:
                temp.append(0)
        l.append(temp)
    job = request.json.get('job')
    if job == 'check':
        r = check_validity(l)
        return jsonify({'status': r})
    else:
        solveSudoku(l)
    return jsonify({'solution': l})


def findNextCellToFill(sudoku):
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:
                return x, y
    return -1, -1


def isValid(sudoku, i, j, e):
    rowOk = all([e != sudoku[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != sudoku[x][j] for x in range(9)])
        if columnOk:
            secTopX, secTopY = 3 * (i // 3), 3 * (j // 3)
            for x in range(secTopX, secTopX + 3):
                for y in range(secTopY, secTopY + 3):
                    if sudoku[x][y] == e:
                        return False
            return True
    return False


def solveSudoku(sudoku, i=0, j=0):
    i, j = findNextCellToFill(sudoku)
    if i == -1:
        return True
    for e in range(1, 10):
        if isValid(sudoku, i, j, e):
            sudoku[i][j] = e
            if solveSudoku(sudoku, i, j):
                return True
            sudoku[i][j] = 0
    return False


def check_validity(l):
    return isValidSudoku(l)


def isinRange(board):
    N = 9

    for i in range(0, N):
        for j in range(0, N):

            if ((board[i][j] <= 0) or
                    (board[i][j] > 9)):
                return False

    return True


def isValidSudoku(board):
    N = 9

    if (isinRange(board) == False):
        return False

    unique = [False] * (N + 1)

    for i in range(0, N):

        for m in range(0, N + 1):
            unique[m] = False

        for j in range(0, N):

            Z = board[i][j]

            if (unique[Z] == True):
                return False

            unique[Z] = True

    for i in range(0, N):

        for m in range(0, N + 1):
            unique[m] = False

        for j in range(0, N):

            Z = board[j][i]

            if (unique[Z] == True):
                return False

            unique[Z] = True

    for i in range(0, N - 2, 3):

        for j in range(0, N - 2, 3):

            for m in range(0, N + 1):
                unique[m] = False

            for k in range(0, 3):
                for l in range(0, 3):

                    X = i + k

                    Y = j + l

                    Z = board[X][Y]

                    if unique[Z] == True:
                        return False

                    unique[Z] = True

    return True
