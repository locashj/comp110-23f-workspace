"""EX06 - A suite of practice dictionary functions."""

__author__ = "730718389"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Accepts a dict[str, str] and returns a new dict with inverted keys and values."""
    result: dict[str, str] = dict()
    for k in d:
        if d[k] in result:
            raise KeyError(f"Key {d[k]} is already present!")
        result[d[k]] = k
    return result


def favorite_color(person_colors: dict[str, str]) -> str:
    """Accepts a dictionary whose keys are people and values are their favorite color, and returns the most popular color."""
    color_counts: dict[str, int] = dict()
    for person in person_colors:
        color: str = person_colors[person]
        if color not in color_counts:
            color_counts[color] = 1
        else:
            color_counts[color] += 1
    
    favorite: str = ""
    for color in color_counts:
        if favorite == "" or color_counts[color] > color_counts[favorite]:
            favorite = color
    return favorite


def count(strings: list[str]) -> dict[str, int]:
    """Accepts a list of strings and returns a dictionary of list values to occurrences."""
    occurrences: dict[str, int] = dict()
    for s in strings:
        if s not in occurrences:
            occurrences[s] = 1
        else:
            occurrences[s] += 1
    return occurrences


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Accepts a list of words and returns a dictionary mapping unique letters to the list of words in which they occur."""
    letter_freq: dict[str, list[str]] = dict()
    for word in words:
        letter = word[0].lower()
        if letter not in letter_freq:
            letter_freq[letter] = [word]
        else:
            letter_freq[letter].append(word)
    return letter_freq


def update_attendance(attendance: dict[str, list[str]], day_of_week: str, student: str) -> dict[str, list[str]]:
    """Updates `attendance` by adding the given student to the given day of the week."""
    if day_of_week not in attendance:
        attendance[day_of_week] = [student]
    if student not in attendance[day_of_week]:
        attendance[day_of_week].append(student)
    return attendance
