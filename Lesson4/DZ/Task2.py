#  вывод графика для квадратного уравнения
import matplotlib.pyplot as plt

def func_quad(x, a, b, c):
    return (a * x ** 2) + (b * x) + c

a, b, c = map(int, input("Введите коэффициенты для квадратного уравнения: ").split())
x_coords = [x for x in range(-10, 10, 1)]
y_coords = []
for x in x_coords:
    y_coords.append(func_quad(x, a, b, c))
plt.plot(x_coords, y_coords, "r--")
# plt.scatter(x_coords, y_coords, c="red")
plt.title("Квадратное уравнение")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()