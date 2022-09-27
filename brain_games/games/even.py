import random
"""This module implements pseudo-random number generators for various distributions."""

START = 0
FINISH = 100

def randome_number():
    """Generate a random number and check if it's even."""
    question = random.randint(START, FINISH)
    if question % 2 == 0:
        correct_answer = 'yes'
    elif question % 2 != 0:
        correct_answer = 'no'
    return question, correct_answer