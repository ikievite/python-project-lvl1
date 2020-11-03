

"""File contains functions for script - brain_prime."""


import random

from brain_games.cli import engine, number_of_games


def is_prime(digit):
    """Func checks is digit prime.

    Args:
        digit: for checking

    Returns:
        bool value
    """
    if digit < 2:
        return False
    i = 2
    while i <= digit / 2:
        if digit % i == 0:
            return False
        else:
            i += 1
    return True


def prepare_prime_game():
    """Func generate questions and right answer.

    Returns:
        question: answer for question
        right_answer: right calculated answer
    """
    digit = random.randint(0, 10)
    if is_prime(digit):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    question = f'is {digit} prime?: '
    return question, right_answer


def run_prime():
    """Prepare data for game engine."""
    game_description = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    game_data = []
    i = 1
    while i <= number_of_games:
        game_data.append(prepare_prime_game())
        i += 1
    engine(game_description, game_data)
