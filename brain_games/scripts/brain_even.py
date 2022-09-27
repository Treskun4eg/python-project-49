#!/usr/bin/env python3
"""Enter shebang to run python."""
import prompt
import random
"""
Import prompt functionality.

Using a Library to Validate Data Input
"""


GET_ROUND = 3


def welcome_user():
    """Asking for a name of user."""
    global name
    name = prompt.string('Mai I have your name? ')
    print('Hello, {arg}!'.format(arg=name))


def randome_number():
    global question
    global correct_answer
    question = random.randint(0, 100)
    if question % 2 == 0:
        correct_answer = 'yes'
    elif question % 2 != 0:
        correct_answer = 'no'
    return question, correct_answer


def your_answer():
    print('Welcome to the Brain Games!')
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(GET_ROUND):
        question, correct_answer = randome_number()
        correct = 'Correct!'
        print('Question: {arg}'.format(arg=question))
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print(correct)
        elif answer != correct_answer:
            print('Is wrong answer {arg1};(.'.format(arg1=answer))
            print('Correct answer was "{arg2}".'.format(arg2=correct_answer))
            print('Let\'s try again, {arg3}!'.format(arg3=name))
            return
    print('Congratulations, {arg}!'.format(arg=name))


def main():
    """Say hello and ask for a username."""
    your_answer()


if __name__ == '__main__':
    main()
