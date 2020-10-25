

"""File contains functions for script - brain_prime."""


import random

from brain_games.cli import engine, games_count


def is_prime(digit):
    """Func checks is digit prime.

    Args:
        digit: fot checking

    Returns:
        bool value
    """
    if digit == 1:
        return False
    i = 1
    while i < digit:
        if digit % i == 0:
            divider = i
        i += 1
    return divider == 1


def prepare_prime_game():
    """Func generate questions and right answer.

    Returns:
        question: answer for question
        right_answer: right calculated answer
    """
    digit = random.randint(1, 10)
    if is_prime(digit):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    question = f'is {digit} prime?: '
    return question, right_answer


def run_prime():
    """Prepare data for game engine."""
    game_desc = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    game_data = []
    i = 1
    while i <= games_count:
        game_data.append(prepare_prime_game())
        i += 1
    engine(game_desc, game_data, games_count)
