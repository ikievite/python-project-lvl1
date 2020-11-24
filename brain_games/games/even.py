

"""File contains functions for script - brain_calc."""


import random

from brain_games.cli import engine


def prepare_even_game():
    """Func generate questions and right answer.

    Returns:
        question: for question
        right_answer: right calculated answer
    """
    random_number = random.randint(1, 100)
    question = f'{random_number}'
    if random_number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer


def run_even():
    """Prepare data for game engine."""
    game_description = 'Answer "yes" if number even otherwise answer "no".'
    engine(game_description, prepare_even_game)
