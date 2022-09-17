"""
Import prompt functionality.

Using a Library to Validate Data Input
"""
import prompt


def welcome_user():
    """Asking for a name of user."""
    name = prompt.string('Mai I have your name?')
    return str('Hello ') + {name} + str('!')
