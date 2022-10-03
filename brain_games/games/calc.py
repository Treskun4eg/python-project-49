import random


DESCRIPTION = 'What is the result of the expression?'
START = 1
FINISH = 100


def current_game():
    num_1 = random.randint(START, FINISH)
    num_2 = random.randint(START, FINISH)
    correct_expressions = {
        '+': num_1 + num_2,
        '-': num_1 - num_2,
        '*': num_1 * num_2
    }
    random_expressions = random.choice(list(correct_expressions.keys()))
    question = f'{num_1} {random_expressions} {num_2}'
    correct_answer = str(correct_expressions[random_expressions])
    return question, correct_answer
