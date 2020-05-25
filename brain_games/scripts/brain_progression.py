#!/usr/bin/env python3


"""Find missing number in progression."""


from brain_games.cli import welcome_user
from brain_games.games.progression import progression_logic


def main():
    """Responses for main logic."""
    print("""
Welcome to the Brain Games!
What number is missing in the progression?
          """)
    name = welcome_user()
    print(f'Hello, {name}!\n')
    progression_logic(name)


if __name__ == '__main__':
    main()
