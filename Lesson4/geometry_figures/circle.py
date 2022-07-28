from math import pi

def is_correct_circle(r):
    if r <= 0:
        raise Exception("Радиус круга <= 0!")

def get_square_circle(r):
    is_correct_circle(r)
    return pi * (r ** 2)

def get_perimetr_circle(r):
    is_correct_circle(r)
    return 2 * pi * r
