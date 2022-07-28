# Вывод числа, повторяющегося 1 раз, из списка

# a = input().split()
# l = []
# for i in range(len(a)):
#     l.append(a[i])
# print(l)

l = [int(i) for i in input().split()]
print(l)

for i in l:
    if l.count(i) == 1:
        print(i, end=' ')