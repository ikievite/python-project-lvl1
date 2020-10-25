

"""File with functions."""


import prompt

number_games = 3


def welcome_user():
    """Func welcomes gamer."""
    print('Welcome to the Brain Games!')


def ask_name():
    """Func asks user`s name.

    Returns:
        username.
    """
    return prompt.string('May I have your name? ')


def engine(description, entries):
    """Make for game logic.

    Args:
        description: of game
        entries: list with tuples, tuple contain question and right answer
    """
    welcome_user()
    print(description + '\n')
    name = ask_name()
    count = 0
    for i in entries:
        question, right_answer = i
        question = f'Question: {question}'
        answer = prompt.string(question)
        if answer == right_answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            break
    if count == number_games:
        print(f'Congratulations, {name}')
