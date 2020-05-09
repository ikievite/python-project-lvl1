#!/usr/bin/env python3


"""File with functions."""


import prompt


def welcome_user():
    """Func asks user`s name.

    Returns:
        greeting and user`s name.
    """
    name = prompt.string('May I have your name? ')
    return '\nHello, {0}!'.format(name)


def main():
    welcome_user()


if __name__ == '__main__':
    main()
