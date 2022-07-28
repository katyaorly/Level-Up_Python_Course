from math import sqrt

def count_quad_eq(a, b, c):
    d = (b ** 2) - 4 * a * c
    if a == 0:
        raise Exception("Делить на 0 нельзя!")
    if d < 0:
        return "Корней нет"
    if d == 0:
        return (- b) / (2 * a)
    if d > 0:
        return (- b + sqrt(d)) / (2 * a),  (- b - sqrt(d)) / (2 * a)


