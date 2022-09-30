import random
import prompt


GET_ROUND = 3
START = 0
FINISH = 100


def randome_number():
    """Generate a random number and check if it's even."""
    question = random.randint(START, FINISH)
    if question % 2 == 0:
        correct_answer = 'yes'
    elif question % 2 != 0:
        correct_answer = 'no'
    return question, correct_answer


def your_answer():
    """
    Greet the user.
    Explain the rules of the game
    Play a game with him
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('Mai I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(GET_ROUND):
        question, correct_answer = randome_number()
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
