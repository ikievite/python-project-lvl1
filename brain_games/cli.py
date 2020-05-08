#!/usr/bin/env python3


import prompt


def welcome_user():
    """ func asks and prints user`s name"""
    print()
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))


def main():
    welcome_user()


if __name__ == '__main__':
    main()
