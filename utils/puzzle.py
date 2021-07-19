import requests
from .constants import PUZZLE_URL


def get_puzzle():
    response = requests.request("GET", PUZZLE_URL)
    return [[items[i: i + 3] for i in range(0, len(items), 3)] for items in response.json().get('board')]
