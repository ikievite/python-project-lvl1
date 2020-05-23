#!/usr/bin/env python3


"""Find General Common Divider."""


from brain_games.cli import welcome_user
from brain_games.games.gcd import gcd_logic


def main():
    """Responses for main logic."""
    print("""
Welcome to the Brain Games!
Find the greatest common divisor of given numbers.
          """)
    name = welcome_user()
    print(f'Hello, {name}!\n')
    gcd_logic(name)


if __name__ == '__main__':
    main()
