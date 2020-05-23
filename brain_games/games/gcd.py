#!/usr/bin/env python3


"""Contains functions for script - brain_gcd."""


import random

import prompt

from brain_games.cli import check_answer


def find_divider(d):
    """Find dividers.

    Args:
        d: digit

    Returns:
        dividers: list with dividers
    """
    dividers = []
    i = 1
    while d >= i:
        if d % i == 0:
            dividers.append(i)
        i += 1
    return dividers


def find_gcd(name):
    """Set qurstions and write anwsers.

    Args:
        name: name of user

    Returns:
        answer: answer for question
        right_answer: right calculated answer
    """
    random_a = random.randint(1, 100)
    random_b = random.randint(1, 100)
    deviders_a = find_divider(random_a)
    deviders_b = find_divider(random_b)
    right_answer = max(set(deviders_a).intersection(set(deviders_b)))
    answer = prompt.integer(f'Question: {random_a} {random_b}: \nYour answer: ')
    return answer, right_answer


def gcd_logic(name):
    """Respons for logic.

    Args:
        name: name of user
    """
    i = 1
    right = 0
    while i <= 3:
        qa_result = check_answer(find_gcd(name), name)
        if qa_result == 'Correct!':
            print(qa_result)
            i += 1
            right += 1
        else:
            print(qa_result)
            break
    if right == 3:
        print(f'Congratulations, {name}')
