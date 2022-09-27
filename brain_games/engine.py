from brain_games.games.even import randome_number
from brain_games.cli import welcome_user
import prompt


GET_ROUND = 3


def your_answer():
    """
    Greet the user.
    Explain the rules of the game
    Play a game with him
    """
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(GET_ROUND):
        question, correct_answer = randome_number()
        correct = 'Correct!'
        print('Question: {arg}'.format(arg=question))
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print(correct)
        elif answer != correct_answer:
            print('Is wrong answer {arg1};(.'.format(arg1=answer))
            print('Correct answer was "{arg2}".'.format(arg2=correct_answer))
            print('Let\'s try again, {arg3}!'.format(arg3=name))
            return
    print('Congratulations, {arg}!'.format(arg=name))
