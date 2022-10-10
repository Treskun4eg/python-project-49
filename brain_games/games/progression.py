import random


DESCRIPTION = 'What number is missing in the progression?'
START_1 = 1
START_2 = 20
STEP_1 = 1
STEP_2 = 10
element_1 = 0
element_2 = 9


def FINISH():
    i = 1
    last_number = START + STEP
    while i < 10:
        last_number = last_number + STEP
        i = i + 1
    return last_number


def current_game():
    global START
    global STEP
    START = random.randint(START_1, START_2)
    STEP = random.randint(STEP_1, STEP_2)
    randome_progression = list(range(START, FINISH(), STEP))
    randome_element = random.randint(element_1, element_2)
    correct_answer = str(randome_progression[randome_element])
    randome_progression[randome_element] = '..'
    question = ''
    for progression in randome_progression:
        question += " " + str(progression)
    question = str(question.strip())
    return question, correct_answer
