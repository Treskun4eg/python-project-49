import random


DESCRIPTION = 'What number is missing in the progression?'
START_1 = 1
START_2 = 20
STEP_1 = 1
STEP_2 = 10
index_first = 0
index_last = 9
SEQUENCE_TERM = 11


def calculate_arguments():
    INITIAL = random.randint(START_1, START_2)
    DIFFERENCE = random.randint(STEP_1, STEP_2)
    LAST_TERM = INITIAL + (SEQUENCE_TERM - 1) * DIFFERENCE
    return INITIAL, DIFFERENCE, LAST_TERM


def generate_progression():
    INITIAL, DIFFERENCE, LAST_TERM = calculate_arguments()
    progression = list(range(INITIAL, LAST_TERM, DIFFERENCE))
    index = random.randint(index_first, index_last)
    return index, progression


def start_round():
    index, progression = generate_progression()
    correct_answer = str(progression[index])
    progression[index] = '..'
    question = " ".join(map(str, progression))
    return question, correct_answer
