#!/usr/bin/env python3


"""File with functions."""


from random import randint

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


def check_even():
    """Func ask for an integer.

    Returns:
       something
    """
    username = prompt.string('May I have your name? ')
    print('Hello, {0}!\n'.format(username))
    right = 0
    i = 1
    while i <= 3:
        random_number = randint(1, 100)
        print('Question: {0}'.format(random_number))
        answer = prompt.string('Your answer: ')
        if random_number % 2 == 0:
            check = 'yes'
        else:
            check = 'no'

        if check == answer:
            print('Correct!')  # noqa: WPS421
            right += 1
        else:
            print("""
'{0}' is wrong answer ;(. Correct answer was '{1}'.
Let's try again, {2}!""".format(answer, check, username),
                  )
        i += 1
    if right == 3:
        print(f'Congratulations, {username}')


def main():  # noqa: D103
    welcome_user()
    check_even()


if __name__ == '__main__':
    main()
