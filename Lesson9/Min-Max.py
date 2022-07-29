#  поменять местами мин и макс числа списка
# a = [1, 2, 3, 4, 5]
a = [int(i) for i in input().split()]
b = a.index(min(a))
c = a.index(max(a))

a[b], a[c] = a[c], a[b]

print(a)