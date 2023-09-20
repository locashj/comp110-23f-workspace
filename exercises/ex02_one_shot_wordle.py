"""EX02 - One-shot Wordle - A single-guess implementation of Wordle."""

__author__ = '730718389'

SECRET_WORD: str = 'python'

WHITE_BOX: str = '\U00002B1C'
GREEN_BOX: str = '\U0001F7E9'
YELLOW_BOX: str = '\U0001F7E8'


def read_guess() -> str:
    required_len: int = len(SECRET_WORD)
    guess: str = input(f'What is your {required_len}-letter guess? ')
    while len(guess) != required_len:
        guess = input(f'That was not {required_len} letters! Try again: ')
    return guess


def is_present(src: str, char: str) -> bool:
    idx: int = 0
    while idx < len(src):
        if src[idx] == char:
            return True
        idx += 1
    return False


guess: str = read_guess()
result: str = ''
idx: int = 0
num_correct_chars: int = 0
while idx < len(guess):
    if guess[idx] == SECRET_WORD[idx]:
        result += GREEN_BOX
        num_correct_chars += 1
    elif is_present(SECRET_WORD, guess[idx]):
        result += YELLOW_BOX
    else:
        result += WHITE_BOX
    idx += 1

print(result)

if num_correct_chars == len(guess):
    print('Woo! You got it!')
else:
    print('Not quite. Play again soon!')
