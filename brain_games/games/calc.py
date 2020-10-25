

"""File contains functions for script - brain_calc."""


import random

from brain_games.cli import engine, games_count


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
    return (question, right_answer)


def run_calc():
    """Prepare data for game engine."""
    game_descr = 'What is the result of the expression?'
    game_data = []
    i = 1
    while i <= games_count:
        game_data.append(prepare_calc_game())
        i += 1
    engine(game_descr, game_data, games_count)
