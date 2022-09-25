#!/usr/bin/env python3
"""Enter shebang to run python."""
import prompt
import random
"""
Import prompt functionality.

Using a Library to Validate Data Input
"""


def welcome_user():
    """Asking for a name of user."""
    global name
    name = prompt.string('Mai I have your name? ')
    print('Hello, {arg}!'.format(arg=name))


def randome_number():
    global r_n
    r_n = random.randint(0, 100)
    print('Question: {arg}'.format(arg=r_n))


def your_answer():
    correct = 'Correct!'
    answer = prompt.string('Your answer: ')
    if r_n % 2 != 0 and answer == 'yes':
        print('\'yes\' is wrong answer ;(. Correct answer was \'no\'.')
        print('Let\'s try again, {arg}!'.format(arg=name))
    if r_n % 2 == 0 and answer == 'no':
        print('\'no\' is wrong answer ;(. Correct answer was \'yes\'.')
        print('Let\'s try again, {arg}!'.format(arg=name))
    if answer != 'yes' and answer != 'no':
        print('Is wrong answer ;(. Correct answer was \'no\' or \'yes\'.')
        print('Let\'s try again, {arg}!'.format(arg=name))
    if r_n % 2 == 0 and answer == 'yes':
        print(correct)
    if r_n % 2 != 0 and answer == 'no':
        print(correct)


def main():
    """Say hello and ask for a username."""
    print('Welcome to the Brain Games!')
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    randome_number()
    your_answer()


if __name__ == '__main__':
    main()
