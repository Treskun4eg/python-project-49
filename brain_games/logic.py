import prompt
"""Adding the prompt module"""

GET_ROUND = 3


def your_answer(game):
    """
    Greet the user.
    Explain the rules of the game
    Play a game with him
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    for _ in range(GET_ROUND):
        question, correct_answer = game.current_game()
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
