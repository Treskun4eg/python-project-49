import random


DESCRIPTION = 'What is the result of the expression?'
START = 1
FINISH = 100


def current_game():
    rand_num = random.randint(START, FINISH)
    random_operator = random.choice(['+', '-', '*'])
    question = f'{rand_num} {random_operator} {rand_num}'
    correct_answer = question
    return question, correct_answer
