#  Является ли строка палиндромом
#  Вариант 1
a = input()
a = a.lower()
a = a.replace(" ", "")
if a == a[::-1]: # или a == reversed(a)
    print("Палиндром")
else:
    print("Не палиндром")

#  Вариант 2

# i = 0
# if i <= len(a) / 2:
#     if a[- i - 1] == a[i]:
#         i += 1
#         print("Палиндром")
#     else:
#         print("Не палиндром")