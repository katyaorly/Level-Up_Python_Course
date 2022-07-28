# Вывод макс/мин, делятся на 3 и не делятся на 5 числа из списка

l = [int(i) for i in input().split()]
print(l)

print(max(l))
print(min(l))

for i in l:
    if i % 3 == 0 and i % 5 != 0:
      print(i, end=" ")