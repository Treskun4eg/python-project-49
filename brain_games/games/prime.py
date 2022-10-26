import random


START = 1
START_1 = 2
FINISH = 100
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def current_game():
    question = random.randint(START, FINISH)
    q = 0
    for i in range(START_1, question // 2 + 1):
        """
        Check for the number of divisors
        of a number from the given range
        """
        if question % i == 0:
            q += 1
    if q <= 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
