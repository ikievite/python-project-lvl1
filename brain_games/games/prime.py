

"""File contains functions for script - brain_prime."""


import random

from brain_games.cli import engine


def prepare_prime_game():
    """Func generate questions and right answer.

    Returns:
        question: answer for question
        right_answer: right calculated answer
    """
    digit = random.randint(1, 10)
    i = 1
    while i < digit:
        if digit % i == 0:
            divider = i
        i += 1
        if divider > 1:
            right_answer = 'no'
        else:
            right_answer = 'yes'
    question = f'Is {digit} prime?: '
    return question, right_answer


def run_prime():
    """Prepare data for game engine."""
    game_desc = """
Welcome to the Brain Games!
Answer "yes" if given number is prime. Otherwise answer "no".
                """
    games_count = 3
    game_data = []
    i = 1
    while i <= games_count:
        game_data.append(prepare_prime_game())
        i += 1
    engine(game_desc, game_data, games_count)
