

"""File with functions."""


import prompt

number_of_games = 3


def engine(description, entries):
    """Make for game logic.

    Args:
        description: of game
        entries: list with tuples, tuple contain question and right answer
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(description + '\n')
    count = 0
    while count < number_of_games:
        question, right_answer = entries[count]
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == right_answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}')
