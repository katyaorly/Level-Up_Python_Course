#  Является ли строка палиндромом
a = input()
a = a.lower()
a = a.replace(" ", "")
if a == a[::-1]: # или a == reversed(a)
    print("Палиндром")
else:
    print("Не палиндром")