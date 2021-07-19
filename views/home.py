import requests
from flask import Blueprint, render_template, jsonify, request
from utils.sudoku import solve_sudoku, is_valid_sudoku
from utils.puzzle import get_puzzle

home_blueprint = Blueprint('index', __name__)


@home_blueprint.route('/')
def home():
    board = get_puzzle()
    return render_template('home/home.html', value=board)


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
        r = is_valid_sudoku(l)
        return jsonify({'status': r})
    else:
        solve_sudoku(l)
    return jsonify({'solution': l})
