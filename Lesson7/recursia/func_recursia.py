# вывод факториала от числа n
# n = int(input())
# def factorial(n):
#     if  n > 1:
#         return factorial(n - 1) * n
#     else:
#         return 1
#
# print(factorial(n))


#  поиск числа Фибоначчи под номером n
#   0 1 1 2 3 5 8 13 21...
# n 1 2 3 4 5 6 7 8  9...
n = int(input())
def fib(n):
    if  n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(n))