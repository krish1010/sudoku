import requests
from .constants import PUZZLE_URL


def get_puzzle():
    response = requests.request("GET", PUZZLE_URL)
    board = response.json().get('board')
    l2 = []
    for items in board:
        l = []
        for i in range(0, len(items), 3):
            l.append(items[i: i + 3])
        l2.append(l)
    return l2
