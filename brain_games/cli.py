

"""File with functions."""


import prompt


def welcome_user():
    """Func asks user`s name.

    Returns:
        greeting and user`s name.
    """
    return prompt.string('May I have your name? ')


def check_answer(answer_right, username):
    """Funcrion checks correctness.

    Args:
        answer_right: tuple that contain anwer from username and correct answer
        username: name of user :)

    Returns:
        answer 'Correct!'
        or wrong and right answer
    """
    answer, right = answer_right
    if answer == right:
        output = 'Correct!'
    else:
        output = f"""'{answer}' is wrong answer ;(. Correct answer was '{right}'.
Let's try again, {username}!"""
    return output


def engine(description, entries, number_games):
    """Make for game logic.

    Args:
        description: of game
        entries: list with tuples, tuple contain question and right answer
        number_games: number of games that user can execute
    """
    print(description)
    name = welcome_user()
    count = 0
    for i in entries:
        question, right_answer = i
        if isinstance(right_answer, int):
            answer = prompt.integer(question)
        elif isinstance(right_answer, str):
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
