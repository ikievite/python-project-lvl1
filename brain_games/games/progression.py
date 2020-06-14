

"""File contains functions for script - brain_progression."""


import random

from brain_games.cli import engine


def generate_progression():
    """Generate questions and right answers.

    Returns:
        question: for question
        correct: right answer
    """
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    hidden = random.randint(1, 10)
    i = 1
    line = ''
    while i <= 10:
        if i == hidden:
            line = line + ' ..'
            correct = start
        else:
            line = line + ' ' + str(start)
        start += step
        i += 1
    line = line.strip()
    question = f'{line}\n.. == '
    return (question, correct)


def run_progression():
    """Prepare data for game engine."""
    game_desc = 'What number is missing in the progression?'
    games_count = 3
    game_data = []
    i = 1
    while i <= games_count:
        game_data.append(generate_progression())
        i += 1
    engine(game_desc, game_data, games_count)
