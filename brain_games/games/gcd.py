import math
import random


START = 1
FINISH = 20
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(num_1, num_2):
    return math.gcd(num_1, num_2)


def get_round():
    num_1 = random.randint(START, FINISH)
    num_2 = random.randint(START, FINISH)
    question = f'{num_1} {num_2}'
    correct_answer = str(gcd(num_1, num_2))
    return question, correct_answer
