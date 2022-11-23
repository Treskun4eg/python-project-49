import random


START = 2
START_1 = 2
FINISH = 100
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(question):
    q = 0
    iteration_object = range(START_1, question // 2 + 1)
    for i in iteration_object:
        if question % i == 0:
            q += 1
    if q <= 0:
        return True


def get_round():
    question = random.randint(START, FINISH)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, correct_answer
