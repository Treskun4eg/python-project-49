import prompt
"""Adding the prompt module"""

NUMBER_ROUNDS = 3


def run_game(game):
    """
    Greet the user.
    Explain the rules of the game
    Play a game with him
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    for _ in range(NUMBER_ROUNDS):
        question, correct_answer = game.get_round()
        correct = 'Correct!'
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print(correct)
        elif answer != correct_answer:
            print(f'Is wrong answer {answer};(.')
            print(f'Correct answer was "{correct_answer}".')
            print(f'Let\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')
