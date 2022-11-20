import random


DESCRIPTION = 'What number is missing in the progression?'
INITIAL_LOWER_BOUND = 1
INITIAL_UPPER_BOUND = 20
STEP_LOWER_BOUND = 1
STEP_UPPER_BOUND = 10
index_first = 0
index_last = 9
LENGTH = 11


def generate_progression(INITIAL_TERM, DIFFERENCE, LENGTH):
    LAST_TERM = INITIAL_TERM + (LENGTH - 1) * DIFFERENCE
    progression = list(range(INITIAL_TERM, LAST_TERM, DIFFERENCE))
    return progression


def get_round():
    INITIAL_TERM = random.randint(INITIAL_LOWER_BOUND, INITIAL_UPPER_BOUND)
    DIFFERENCE = random.randint(STEP_LOWER_BOUND, STEP_UPPER_BOUND)
    progression = generate_progression(INITIAL_TERM, DIFFERENCE, LENGTH)
    index = random.randint(index_first, index_last)
    correct_answer = str(progression[index])
    progression[index] = '..'
    question = " ".join(map(str, progression))
    return question, correct_answer
