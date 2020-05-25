#!/usr/bin/env python3


"""File contains functions for script - brain_calc."""


import random

import prompt

from brain_games.cli import check_answer


def ask_prog(name):
    """Func asl answeer hidden digit in progression.

    Args:
        name: name of user

    Returns:
        answer: for question
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
    print(f'Question: {line}')
    answer = prompt.integer('.. == ')
    return answer, correct


def progression_logic(name):
    """Responses for logic Fing Progression Game: ask/check/print.

    Args:
        name: name of user
    """
    right = 0
    i = 1
    while i <= 3:
        qa_result = check_answer(ask_prog(name), name)
        if qa_result == 'Correct!':
            print(qa_result)
            i += 1
            right += 1
        else:
            print(qa_result)
            break
    if right == 3:
        print(f'Congratulations, {name}')
