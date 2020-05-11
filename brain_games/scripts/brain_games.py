#!/usr/bin/env python3


"""Game Brain Game."""


from brain_games.cli import welcome_user


def main():
    """Func responses for main logic."""
    print(welcome_user())  # noqa: WPS421


if __name__ == '__main__':
    print('Welcome to the Brain Games!')  # noqa: WPS421
    main()
