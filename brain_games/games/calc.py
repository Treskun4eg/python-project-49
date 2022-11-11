import random


DESCRIPTION = 'What is the result of the expression?'
START = 1
FINISH = 100


def start_round():
    num_1 = random.randint(START, FINISH)
    num_2 = random.randint(START, FINISH)
    # submit an operator and get the desired expression
    sign_to_operation_result = {
        '+': num_1 + num_2,
        '-': num_1 - num_2,
        '*': num_1 * num_2
    }
    operation_sign = random.choice(list(sign_to_operation_result.keys()))
    question = f'{num_1} {operation_sign} {num_2}'
    correct_answer = str(sign_to_operation_result[operation_sign])
    return question, correct_answer
