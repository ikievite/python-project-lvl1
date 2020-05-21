#!/usr/bin/env python3


"""Check basic calc knowledge."""


from brain_games.cli import welcome_user
from brain_games.games.calc import calc_logic


def main():
    """Responses for main logic."""
    print("""
Welcome to the Brain Games!
What is the result of the expression?
""")
    name = welcome_user()
    print(f'Hello, {name}!\n')
    calc_logic(name)


if __name__ == '__main__':
    main()
