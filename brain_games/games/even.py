import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
START = 0
FINISH = 100


def check_is_even():
    """Generate a random number and check if it's even."""
    question = random.randint(START, FINISH)
    if question % 2 == 0:
        correct_answer = 'yes'
    elif question % 2 != 0:
        correct_answer = 'no'
    return question, correct_answer


def get_round():
    question, correct_answer = check_is_even()
    return question, correct_answer
