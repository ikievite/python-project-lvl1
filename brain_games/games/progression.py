

"""File contains functions for script - brain_progression."""


import random

from brain_games.cli import engine, number_of_games


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
    question = ''
    while i <= max_element:
        if i == hidden:
            question = question + ' ..'
            correct = start
        else:
            question = question + ' ' + str(start)
        start += step
        i += 1
    question = question.strip()
    question = f'{question}\n.. == '
    return (question, str(correct))


def run_progression():
    """Prepare data for game engine."""
    game_description = 'What number is missing in the progression?'
    min_element = 1
    max_element = 10
    game_data = []
    i = 1
    while i <= number_of_games:
        game_data.append(prepare_progression_game(min_element, max_element))
        i += 1
    engine(game_description, game_data)
