# Вывести предложение из строк

n = int(input())
m = []
d = []
for i in range(n):
    m.append(input())

d = " ".join(m)
print(d, end=".")



