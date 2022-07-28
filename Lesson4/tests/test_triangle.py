from geometry_figures.triangle import is_correct_triangle, get_square_triangle, get_perimetr_triangle


def test_is_correct_triangle():
    assert is_correct_triangle(3, 4, 5) == None


def test_square_triangle():
    assert get_square_triangle(3, 4, 5) == 6


def test_perimetr_triangle():
    assert get_perimetr_triangle(3, 4, 5) == 12