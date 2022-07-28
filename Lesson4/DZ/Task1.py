# Вывод действительного корня квадратного уравнения
from func_quad_eq import count_quad_eq

a, b, c = map(int, input("Введите коэффициенты для квадратного уравнения: ").split())
print(count_quad_eq(a, b, c))

