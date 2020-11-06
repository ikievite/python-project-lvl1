

"""Contains functions for script - brain_gcd."""


import random

from brain_games.cli import engine


def find_gcd(int1, int2):
    """Find dividers via Euclidean algorithm.

    Args:
        int1: digit1
        int2: digit2

    Returns:
        max divider
    """
    a = max(int1, int2)
    b = min(int1, int2)
    while b != 0:
        r = a % b
        a = b
        b = r
    else:
        return a


def prepare_gcd_game():
    """Func generate answers and right answers.

    Returns:
        answer: answer for question
        right_answer: right calculated answer
    """
    random_a = random.randint(1, 100)
    random_b = random.randint(1, 100)
    gcd = find_gcd(random_a, random_b)
    answer = f'{random_a} {random_b}'
    return answer, str(gcd)


def run_gcd():
    """Prepare data for game engine."""
    game_description = 'Find the greatest common divisor of given numbers.'
    engine(game_description, prepare_gcd_game)
