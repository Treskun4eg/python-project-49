#!/usr/bin/env python3
"""Enter shebang to run python."""
import prompt
"""
Import prompt functionality.

Using a Library to Validate Data Input
"""


def welcome_user():
    """Asking for a name of user."""
    name = prompt.string('Mai I have your name? ')
    print('Hello, {arg}!'.format(arg=name))


def main():
    """Say hello and ask for a username."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
