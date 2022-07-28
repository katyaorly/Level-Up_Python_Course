from math import sqrt

def is_correct_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise Exception("Сторона треугольника <= 0!")

def get_square_triangle(a, b, c):
    is_correct_triangle(a, b, c)
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def get_perimetr_triangle(a, b, c):
    is_correct_triangle(a, b, c)
    return a + b + c

