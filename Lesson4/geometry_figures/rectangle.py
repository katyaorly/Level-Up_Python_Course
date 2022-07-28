def is_correct_rectangle(x, y):
    if x <= 0 or y <= 0:
        raise Exception("Сторона прямоугольника <= 0!")

def get_square_rectangle(x, y):
    is_correct_rectangle(x, y)
    return x * y

def get_perimetr_rectangle(x, y):
    is_correct_rectangle(x, y)
    return 2 * (x + y)
