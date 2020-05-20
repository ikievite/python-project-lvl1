#!/usr/bin/env python3


"""Check for Even."""


from brain_games.cli import welcome_user
from brain_games.games.even import even_logic


def main():
    """Func responses for main logic."""
    print('\nWelcome to the Brain Games!')  # noqa: WPS421
    print('Answer "yes" if number even otherwise answer "no".\n')  # noqa: WPS421
    name = welcome_user()
    print(f'Hello, {name}!')
    even_logic(name)


if __name__ == '__main__':
    main()
