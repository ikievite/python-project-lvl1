#!/usr/bin/env python3


"""Check for Even."""


from brain_games.cli import check_even


def main():
    """Func responses for main logic."""
    print('\nWelcome to the Brain Games!')  # noqa: WPS421
    print('Answer "yes" if number even otherwise answer "no".\n')  # noqa: WPS421
    check_even()


if __name__ == '__main__':
    main()
