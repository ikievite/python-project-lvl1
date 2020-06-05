

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
    question = f'Question: {random_number}\nYour answer: '
    if random_number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return (question, right_answer)


def run_even():
    """Prepare data for game engine."""
    game_description = """
Welcome to the Brain Games!
Answer "yes" if number even otherwise answer "no".
                       """
    games_count = 3
    game_data = []
    i = 1
    while i <= games_count:
        game_data.append(prepare_even_game())
        i += 1
    engine(game_description, game_data, games_count)
