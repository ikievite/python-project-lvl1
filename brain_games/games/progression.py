

"""File contains functions for script - brain_progression."""


import random

from brain_games.cli import engine


def prepare_progression_game():
    """Generate questions and right answers.

    Returns:
        question: for question
        correct: right answer
    """
    min_start_element = 1
    max_start_element = 10
    min_step_element = 1
    max_step_element = 10
    min_hidden_element = 1
    max_hidden_element = 10
    start = random.randint(min_start_element, max_start_element)
    step = random.randint(min_step_element, max_step_element)
    hidden = random.randint(min_hidden_element, max_hidden_element)
    i = 1
    question = ''
    while i <= max_hidden_element:
        if i == hidden:
            question = question + ' ..'
            right_answer = start
        else:
            question = question + ' ' + str(start)
        start += step
        i += 1
    question = question.strip()
    return question, str(right_answer)


def run_progression():
    """Prepare data for game engine."""
    game_description = 'What number is missing in the progression?'
    engine(game_description, prepare_progression_game)
