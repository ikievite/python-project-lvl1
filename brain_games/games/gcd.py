

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
    highest_num = max(int1, int2)
    lowest_num = min(int1, int2)
    while lowest_num != 0:
        result_of_division = highest_num % lowest_num
        highest_num = lowest_num
        lowest_num = result_of_division
    else:
        return highest_num


def prepare_gcd_game():
    """Func generate answers and right answers.

    Returns:
        answer: answer for question
        right_answer: right calculated answer
    """
    random_a = random.randint(1, 100)
    random_b = random.randint(1, 100)
    right_answer = find_gcd(random_a, random_b)
    question = f'{random_a} {random_b}'
    return question, str(right_answer)


def run_gcd():
    """Prepare data for game engine."""
    game_description = 'Find the greatest common divisor of given numbers.'
    engine(game_description, prepare_gcd_game)
