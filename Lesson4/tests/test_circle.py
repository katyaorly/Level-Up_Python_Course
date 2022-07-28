from math import pi
from geometry_figures.circle import is_correct_circle, get_square_circle, get_perimetr_circle

def test_is_correct_cir():
    assert is_correct_circle(3) == None

def test_square_circle():
    assert get_square_circle(3) == pi * (3 ** 2)

def test_perimetr_circle():
    assert get_perimetr_circle(3) == 2 * 3 * pi