import random


DESCRIPTION = 'What is the result of the expression?'
START = 1
FINISH = 100


def play_game():
    num_1 = random.randint(START, FINISH)
    num_2 = random.randint(START, FINISH)
    # submit an operator and get the desired expression
    list_operations = {
        '+': num_1 + num_2,
        '-': num_1 - num_2,
        '*': num_1 * num_2
    }
    random_expressions = random.choice(list(list_operations.keys()))
    question = f'{num_1} {random_expressions} {num_2}'
    correct_answer = str(list_operations[random_expressions])
    return question, correct_answer
