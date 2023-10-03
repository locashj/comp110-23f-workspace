"""EX03 - Structured Wordle - A more complete implementation of Wordle."""

__author__ = "730718389"

SECRET_WORD: str = "codes"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(s: str, char: str) -> bool:
    """`contains_char` accepts a string `s` and a single character `char`, and returns `True` if `char` is contained within `s`."""
    assert len(char) == 1
    idx: int = 0
    while idx < len(s):
        if s[idx] == char:
            return True
        idx += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """`emojified` accepts two string inputs, `guess` and `secret`, and returns a string of emoji representing the Wordle guess."""
    assert len(guess) == len(secret)
    result: str = ""
    guess_idx: int = 0
    while guess_idx < len(guess):
        if guess[guess_idx] == secret[guess_idx]:
            result += GREEN_BOX
        elif contains_char(secret, guess[guess_idx]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        guess_idx += 1
    return result

    
def input_guess(required_len: int) -> str:
    """`input_guess` reads a `required_len`-length string from user input and re-prompts if the input is of incorrect length."""
    guess = input(f"Enter a {required_len} character word: ")
    while len(guess) != required_len:
        guess = input(f"That wasn't {required_len} chars! Try again: ")
    return guess


def main() -> None:
    """`main` is the main game loop. Players must guess the secret word within 6 turns in order to win."""
    num_turns: int = 6
    current_turn: int = 1
    won: bool = False

    while current_turn <= num_turns:
        print(f"=== Turn {current_turn}/{num_turns} ===")
        guess: str = input_guess(len(SECRET_WORD))
        print(emojified(guess, SECRET_WORD))
        if guess == SECRET_WORD:
            won = True
            break
        current_turn += 1

    if won is True:
        print(f"You won in {current_turn}/{num_turns} turns!")
    else:
        print(f"X/{num_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
