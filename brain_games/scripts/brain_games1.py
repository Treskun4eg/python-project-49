#!/usr/bin/env python3
"""Enter shebang to run python."""
from brain_games.cli import welcome_user


def main():
    """Say hello and ask for a username."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
