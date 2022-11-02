import math
import random


START = 1
FINISH = 20
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def play_game():
    num_1 = random.randint(START, FINISH)
    num_2 = random.randint(START, FINISH)
    question = f'{num_1} {num_2}'
    correct_answer = str(math.gcd(num_1, num_2))
    return question, correct_answer
