import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
START = 0
FINISH = 100


def is_even(question):
    return question % 2 == 0


def get_round():
    question = random.randint(START, FINISH)
    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer
