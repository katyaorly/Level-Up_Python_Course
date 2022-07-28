from Lesson4.geometry_figures.circle import get_square_circle, get_perimetr_circle
from Lesson4.geometry_figures.rectangle import get_square_rectangle, get_perimetr_rectangle, is_correct_rectangle
from Lesson4.geometry_figures.triangle import get_square_triangle, get_perimetr_triangle


rad = int(input("Введите радиус: "))
sq_c = get_square_circle(rad)
per_c = get_perimetr_circle(rad)
print("Площадь круга равна: ", sq_c)
print("Периметр круга равен: ", per_c)

st1_tr = int(input("Введите первую сторону треугольника: "))
st2_tr = int(input("Введите вторую сторону треугольника: "))
st3_tr = int(input("Введите третью сторону треугольника: "))
sq_tr = get_square_triangle(st1_tr, st2_tr, st3_tr)
per_tr = get_perimetr_triangle(st1_tr, st2_tr, st3_tr)
print("Площадь треугольника равна: ", sq_tr)
print("Периметр треугольника равен: ", per_tr)

st1_rec = int(input("Введите первую сторону прямоугольника: "))
st2_rec = int(input("Введите вторую сторону прямоугольника: "))
sq_rec = get_square_rectangle(st1_rec, st2_rec)
per_rec = get_perimetr_rectangle(st1_rec, st2_rec)
print("Площадь прямоугольника равна: ", sq_rec)
print("Периметр прямоугольника равен: ", per_rec)