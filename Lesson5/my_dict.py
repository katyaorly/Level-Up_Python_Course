# вывод словаря (элемент строки: количество раз встречается в строке)

a = input()
dict = {}
for i in a:
    dict.update({i: a.count(i)})
print(dict)
