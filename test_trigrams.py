"""Test file for our Trigram program."""


import pytest


s = "key word value key word kiwi"
result = {'key word': ['value', 'kiwi'], 'word value': ['key'], 'value key':
          ['word']}


def test_generate_dictionary_from_source_text():
    """Function that tests generate_dictionary_from_source_text function."""
    from trigrams import generate_dictionary_from_source_text
    assert generate_dictionary_from_source_text(s) == result


s_b = 'a b c'
result_b = 'a b c'


def test_generate_trigrams_output():
    """Test that our listed function produced the desired output."""
    from trigrams import generate_trigrams_output
    assert generate_trigrams_output(s_b, 3) == result_b


def test_main():
    """Test that our listed function produced the desired output."""
    from trigrams import main
    assert len(main('sherlock.txt', 100).split()) == 100
    assert type(main('sherlock.txt', 100)) == str
