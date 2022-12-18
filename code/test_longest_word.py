from longest_word import *


def test_words_with_equal_length():
    lw = longest_word('abc def ghi jkl')
    assert lw == 'abc'
    assert len(lw) == 3

