#!/usr/bin/env python3


"""File contains functions for script - brain_calc."""


import random

import prompt

from brain_games.cli import check_answer


def ask_even(name):
    """Func ask for an integer.

    Args:
        name: name of user

    Returns:
        answer: for question
        check: right answer
    """
    random_number = random.randint(1, 100)
    print(f'Question: {random_number}')
    answer = prompt.string('Your answer: ')
    if random_number % 2 == 0:
        check = 'yes'
    else:
        check = 'no'
    return answer, check


def even_logic(name):
    """Responses for logic Even Game: ask/check/print.

    Args:
        name: name of user
    """
    right = 0
    i = 1
    while i <= 3:
        qa_result = check_answer(ask_even(name), name)
        if qa_result == 'Correct!':
            print(qa_result)
            i += 1
            right += 1
        else:
            print(qa_result)
            break
    if right == 3:
        print(f'Congratulations, {name}')
