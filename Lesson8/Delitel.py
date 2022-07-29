#  Собственные делители
def delitel(n):
    l_del = []
    for i in range(1, n):
        if n % i == 0:
            l_del.append(i)
    return l_del

# a = int(input())
# print(delitel(a))

# Совершенные числа (сумма собственных делителей равна самому числу)

def perf_num(n):
    l_del = delitel(n)
    s = 0
    for i in l_del:
        s += i
    if s == n:
        return True
    else:
        return False

# b = int(input())
# print(perf_num(b))

#  Вывод всех совершенных чисел

l = []

for i in range(1, 10000):
    if perf_num(i) == True:
        l.append(i)
print(f"Список совершенных чисел: {l}")