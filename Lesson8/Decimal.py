#  Перевод числа из двоичной системы в десятичную

# a = input("Введите число в двоичной системе: ")
# b = 0
# ext = 0
# for i in reversed(a):
#     b += (2 ** ext) * int(i)
#     ext += 1
# print("Число в десятичной системе: ", b)

#  Вариант 2

a = input("Введите число в двоичной системе: ")
decimal = 0
for i in a:
    decimal = decimal * 2 + int(i)
print("Число в десятичной системе: ", decimal)