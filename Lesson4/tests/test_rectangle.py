from geometry_figures.rectangle import is_correct_rectangle, get_square_rectangle, get_perimetr_rectangle


def test_is_correct_rect():
    assert is_correct_rectangle(3, 4) == None


def test_square_circle():
    assert get_square_rectangle(3, 4) == 12


def test_perimetr_circle():
    assert get_perimetr_rectangle(3, 4) == 14