"""EX07 - `dict` Unit Tests."""

import pytest
from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance

__author__ = "730718389"


def test_invert_key_error():
    """Tests `invert` with a dictionary that when inverted raises a KeyError."""
    with pytest.raises(KeyError):
        my_dict: dict[str, str] = {'hello': 'world', 'other': 'world'}
        invert(my_dict)


def test_valid_invert():
    """Tests `invert` with a valid input."""
    assert invert({'foo': 'bar', 'baz': 'qux'}) == {'bar': 'foo', 'qux': 'baz'}


def test_invert_empty():
    """Tests `invert` with an empty dict."""
    assert invert({}) == {}


def test_favorite_color():
    """Tests `favorite_color` when there is multiple voted colors."""
    my_dict: dict[str, str] = {'josh': 'blue', 'josh 2': 'red', 'josh 3': 'blue'}
    assert favorite_color(my_dict) == 'blue'


def test_favorite_color_tie():
    """Tests `favorite_color` when there is a tie."""
    my_dict: dict[str, str] = {'josh': 'blue', 'josh 2': 'red'}
    assert favorite_color(my_dict) == 'blue'


def test_favorite_color_same():
    """Tests `favorite_color` when all votes are for the same color."""
    assert favorite_color({'josh': 'blue', 'jim': 'blue'}) == 'blue'


def test_count_empty():
    """Tests `count` on an empty list."""
    assert count([]) == {}


def test_count_reoccurring():
    """Tests `count` on a list with reoccurring words."""
    assert count(['hello', 'hello', 'hello']) == {'hello': 3}


def test_count_none():
    """Tests `count` on a list with no reoccurring words."""
    counted: dict[str, int] = count(['foo', 'bar', 'baz', 'qux'])
    assert counted == {'foo': 1, 'bar': 1, 'baz': 1, 'qux': 1}


def test_alphabetizer():
    """Tests `alphabetizer` on a sentance with both single and reoccurring characters."""
    alphabetized: dict[str, list[str]] = alphabetizer(['The', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog.'])
    assert len(alphabetized) == 8
    assert len(alphabetized['t']) == 2
    assert len(alphabetized['q']) == 1
    assert len(alphabetized['b']) == 1
    assert len(alphabetized['f']) == 1
    assert len(alphabetized['j']) == 1
    assert len(alphabetized['o']) == 1
    assert len(alphabetized['l']) == 1
    assert len(alphabetized['d']) == 1


def test_alphabetizer_single():
    """Tests `alphabetizer` on a list of one string."""
    assert alphabetizer(['The']) == {'t': 1}


def test_alphabetizer_empty():
    """Tests `alphabetizer` on an empty input list."""
    alphabetized: dict[str, list[str]] = alphabetizer([])
    assert alphabetized == {}


def test_update_attendance_empty():
    """Tests `update_attendance` on an empty attendance."""
    attendance: dict[str, list[str]] = dict()
    update_attendance(attendance, 'Monday', 'Josh')
    assert 'Monday' in attendance
    assert attendance['Monday'] == ['Josh']


def test_update_attendance_valid():
    """Tests `update_attendance` on a partially populated attendance."""
    attendance: dict[str, list[str]] = {
        'Monday': ['Josh'],
        'Tuesday': [],
        'Wednesday': ['Bill']
    }

    update_attendance(attendance, 'Tuesday', 'Josh')
    update_attendance(attendance, 'Wednesday', 'Josh')

    assert len(attendance['Tuesday']) == 1
    assert 'Josh' in attendance['Tuesday']

    assert len(attendance['Wednesday']) == 2
    assert 'Josh' in attendance['Wednesday']


def test_update_attendance_same_name():
    """Tests `update_attendance` by repeating the same name within a day."""
    attendance: dict[str, list[str]] = {'Monday': ['Josh']}
    update_attendance(attendance, 'Monday', 'Josh')
    assert attendance == {'Monday': 'Josh'}
