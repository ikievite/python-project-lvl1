

"""File contains functions for script - brain_calc."""


import random

from brain_games.cli import engine, number_of_games


def prepare_calc_game():
    """Func generate questions and right answer.

    Returns:
        question: answer for question
        right_answer: right calculated answer
    """
    operator = random.choice('+-*')
    random_a = random.randint(1, 10)
    random_b = random.randint(1, 10)
    question = f'{random_a} {operator} {random_b}: '
    if operator == '+':
        right_answer = random_a + random_b
    elif operator == '-':
        right_answer = random_a - random_b
    elif operator == '*':
        right_answer = random_a * random_b
    return (question, str(right_answer))


def run_calc():
    """Prepare data for game engine."""
    game_description = 'What is the result of the expression?'
    game_data = []
    i = 1
    while i <= number_of_games:
        game_data.append(prepare_calc_game())
        i += 1
    engine(game_description, game_data)
