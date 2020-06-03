

"""Contains functions for script - brain_gcd."""


import random

from brain_games.cli import engine


def find_divider(d):
    """Find dividers.

    Args:
        d: digit

    Returns:
        dividers: list with dividers
    """
    dividers = []
    i = 1
    while d >= i:
        if d % i == 0:
            dividers.append(i)
        i += 1
    return dividers


def prepare_gcd_game():
    """Func generate answers and right answers.

    Returns:
        answer: answer for question
        right_answer: right calculated answer
    """
    random_a = random.randint(1, 100)
    random_b = random.randint(1, 100)
    deviders_a = find_divider(random_a)
    deviders_b = find_divider(random_b)
    right_answer = max(set(deviders_a).intersection(set(deviders_b)))
    answer = f'Question: {random_a} {random_b}: \nYour answer: '
    return answer, right_answer


def run_gcd():
    """Prepare data for game engine."""
    game_descr = """
Welcome to the Brain Games!
Find the greatest common divisor of given numbers.
                 """
    number_games = 3
    game_data = []
    i = 1
    while i <= number_games:
        game_data.append(prepare_gcd_game())
        i += 1
    engine(game_descr, game_data, number_games)
