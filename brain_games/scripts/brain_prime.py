#!/usr/bin/env python3


"""Guess prime number."""


from brain_games.cli import welcome_user
from brain_games.games.prime import prime_logic


def main():
    """Responses for main logic."""
    print("""
Welcome to the Brain Games!
Answer "yes" if given number is prime. Otherwise answer "no".
          """)
    name = welcome_user()
    print(f'Hello, {name}!\n')
    prime_logic(name)


if __name__ == '__main__':
    main()
