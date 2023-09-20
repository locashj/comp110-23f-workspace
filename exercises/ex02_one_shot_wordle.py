"""EX02 - One-shot Wordle - A single-guess implementation of Wordle."""

__author__ = '730718389'

SECRET_WORD: str = 'python'

WHITE_BOX: str = '\U00002B1C'
GREEN_BOX: str = '\U0001F7E9'
YELLOW_BOX: str = '\U0001F7E8'


required_len: int = len(SECRET_WORD)
guess: str = input(f'What is your {required_len}-letter guess? ')
while len(guess) != required_len:
    guess = input(f'That was not {required_len} letters! Try again: ')

result: str = ''
guess_idx: int = 0
num_correct_chars: int = 0
while guess_idx < len(guess):
    if guess[guess_idx] == SECRET_WORD[guess_idx]:
        result += GREEN_BOX
        num_correct_chars += 1
    else:
        secret_idx: int = 0
        present = False
        while secret_idx < len(SECRET_WORD):
            if SECRET_WORD[secret_idx] == guess[guess_idx]:
                present = True
                break
            secret_idx += 1
        if present:
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
    guess_idx += 1

print(result)

if num_correct_chars == len(guess):
    print('Woo! You got it!')
else:
    print('Not quite. Play again soon!')
