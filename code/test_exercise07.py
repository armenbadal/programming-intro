from exercise07 import *

def test_empty_text():
    assert 0 == space_percentile('')

def test_ten_percent():
    assert 10 == space_percentile('abcde fghi')

def test_fifty_percent():
    assert 50 == space_percentile('a b c d e f g h ')
