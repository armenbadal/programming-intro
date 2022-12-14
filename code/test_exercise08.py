from exercise08 import *

def test_four_zeros():
    assert 0 == max4(0, 0, 0, 0)

def test_first_is_greatest():
    assert 1000 == max4(1000, 900, 800, 700)
