#!/usr/bin/env python3


"""File contains functions for script - brain_prime."""


import random

import prompt

from brain_games.cli import check_answer


def ask_prime(name):
    """Set qurstions and write anwsers.

    Args:
        name: name of user

    Returns:
        answer: answer for question
        rightr: right calculated answe
    """
    digit = random.randint(1, 10)
    i = 1
    while i < digit:
        if digit % i == 0:
            divider = i
        i += 1
        if divider > 1:
            right = 'no'
        else:
            right = 'yes'
    answer = prompt.string(f'Is {digit} prime?: ')
    return answer, right


def prime_logic(name):
    """Responses for logic - game guess prime digit: ask/check/print.

    Args:
        name: name of user
    """
    right = 0
    i = 1
    while i <= 3:
        qa_result = check_answer(ask_prime(name), name)
        if qa_result == 'Correct!':
            print(qa_result)
            i += 1
            right += 1
        else:
            print(qa_result)
            break
    if right == 3:
        print(f'Congratulations, {name}')
