

"""File contains functions for script - brain_progression."""


import random

from brain_games.cli import engine, number_games


def prepare_progression_game(min_element, max_element):
    """Generate questions and right answers.

    Args:
        min_element: min element of progression
        max_element: max element of progression

    Returns:
        question: for question
        correct: right answer
    """
    start = random.randint(min_element, max_element)
    step = random.randint(min_element, max_element)
    hidden = random.randint(min_element, max_element)
    i = 1
    line = ''
    while i <= max_element:
        if i == hidden:
            line = line + ' ..'
            correct = start
        else:
            line = line + ' ' + str(start)
        start += step
        i += 1
    line = line.strip()
    question = f'{line}\n.. == '
    return (question, str(correct))


def run_progression():
    """Prepare data for game engine."""
    game_desc = 'What number is missing in the progression?'
    min_element = 1
    max_element = 10
    game_data = []
    i = 1
    while i <= number_games:
        game_data.append(prepare_progression_game(min_element, max_element))
        i += 1
    engine(game_desc, game_data)
