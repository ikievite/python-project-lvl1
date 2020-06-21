

"""Contains functions for script - brain_gcd."""


import random

from brain_games.cli import engine


def find_gcd(a, b):
    """Find dividers.

    Args:
        a: digits
        b: digit

    Returns:
        dividers: list with dividers
    """
    dict_dividers = {}
    for d in a, b:
        i = 1
        dividers = []
        while d >= i:
            if d % i == 0:
                dividers.append(i)
            i += 1
        dict_dividers[d] = dividers
    gcd = set(dict_dividers[a]).intersection(set(dict_dividers[b]))
    return max(gcd)


def prepare_gcd_game():
    """Func generate answers and right answers.

    Returns:
        answer: answer for question
        right_answer: right calculated answer
    """
    random_a = random.randint(1, 100)
    random_b = random.randint(1, 100)
    gcd = find_gcd(random_a, random_b)
    answer = f'{random_a} {random_b}: \nYour answer: '
    return answer, gcd


def run_gcd():
    """Prepare data for game engine."""
    game_descr = 'Find the greatest common divisor of given numbers.'
    games_count = 3
    game_data = []
    i = 1
    while i <= games_count:
        game_data.append(prepare_gcd_game())
        i += 1
    engine(game_descr, game_data, games_count)
