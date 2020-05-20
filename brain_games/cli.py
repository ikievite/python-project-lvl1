#!/usr/bin/env python3


"""File with functions."""


import prompt


def welcome_user():
    """Func asks user`s name.

    Returns:
        greeting and user`s name.
    """
    return prompt.string('May I have your name? ')


def check_answer(answer_right, username):
    """Funcrion checks correctness.

    Args:
        answer_right: tuple that contain anwer from username and correct answer
        username: name of user :)

    Returns:
        answer 'Correct!'
        or wrong and right answer
    """
    answer, right = answer_right
    if answer == right:
        output = 'Correct!'
    else:
        output = f"""'{answer}' is wrong answer ;(. Correct answer was '{right}'.
Let's try again, {username}!"""
    return output


def main():  # noqa: D103
    welcome_user()


if __name__ == '__main__':
    main()
