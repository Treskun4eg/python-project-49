import random


DESCRIPTION = 'What number is missing in the progression?'
START_1 = 1
START_2 = 20
STEP_1 = 1
STEP_2 = 10
element_1 = 0
element_2 = 9
SEQUENCE_TERM = 10


def current_game():
    INITIAL = random.randint(START_1, START_2)
    COMMON_DIFFERECE = random.randint(STEP_1, STEP_2)
    LAST_TERM = INITIAL + (SEQUENCE_TERM - 1) * COMMON_DIFFERECE
    randome_progression = list(range(INITIAL, LAST_TERM, COMMON_DIFFERECE))
    randome_element = random.randint(element_1, element_2)

    def replace_value():
        correct_answer = str(randome_progression[randome_element])
        randome_progression[randome_element] = '..'
        question = ''
        for progression in randome_progression:
            question += " " + str(progression)
            question = str(question.strip())
        return question, correct_answer
    return replace_value()
