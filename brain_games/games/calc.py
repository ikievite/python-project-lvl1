#!/usr/bin/env python3


"""File contains functions for script - brain_calc."""


import random

import prompt

from brain_games.cli import check_answer


def ask_reply(name):
    """Set qurstions and write anwsers.

    Args:
        name: name of user

    Returns:
        answer: answer for question
        right_answer: right calculated answer
    """
    operation = random.choice('+-*')
    random_a = random.randint(1, 10)
    random_b = random.randint(1, 10)
    if operation == '+':
        answer = prompt.integer(f'Question: {random_a} + {random_b}: ')
        right_answer = random_a + random_b
    elif operation == '-':
        answer = prompt.integer(f'Question: {random_a} - {random_b}: ')
        right_answer = random_a - random_b
    elif operation == '*':
        answer = prompt.integer(f'Question: {random_a} * {random_b}: ')
        right_answer = random_a * random_b
    return answer, right_answer


def calc_logic(name):
    """Responses for logic: ask/check/print.

    Args:
        name: name of user
    """
    i = 1
    right = 0
    while i <= 3:
        qa_result = check_answer(ask_reply(name), name)
        if qa_result == 'Correct!':
            print(qa_result)
            i += 1
            right += 1
        else:
            print(qa_result)
            break
    if right == 3:
        print(f'Congratulations, {name}')


if __name__ == '__main__':
    calc_logic()
