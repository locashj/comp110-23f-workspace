"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730718389"

def exit_err(msg: str):
  print('Error:', msg)
  exit(1)


def read_word() -> str:
  word_input = input('Enter a 5-character word: ')
  if len(word_input) != 5:
    exit_err('Word must contain 5 characters')
  return word_input


def read_char() -> str:
  char_input = input('Enter a single character: ')
  if len(char_input) != 1:
    exit_err('Character must be a single character.')
  return char_input


if __name__ == '__main__':
  word_input = read_word()
  char_input = read_char()

  print('Searching for', char_input, 'in', word_input)

  num_instances = 0
  for idx in range(0, len(word_input)):
    if word_input[idx] == char_input:
      print(char_input, 'found at index', idx)
      num_instances += 1
  # 2 instances of e found in heels
  if num_instances == 0:
    print('No instances of', char_input, 'found in', word_input)
  elif num_instances == 1:
    print(num_instances, 'instance of', char_input, 'found in', word_input)
  else:
    print(num_instances, 'instances of', char_input, 'found in', word_input)