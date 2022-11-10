import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
START = 0
FINISH = 100


def determine_parity():
    """Generate a random number and check if it's even."""
    question = random.randint(START, FINISH)
    if question % 2 == 0:
        correct_answer = 'yes'
    elif question % 2 != 0:
        correct_answer = 'no'
    return question, correct_answer


def start_round():
    question, correct_answer = determine_parity()
    return question, correct_answer
