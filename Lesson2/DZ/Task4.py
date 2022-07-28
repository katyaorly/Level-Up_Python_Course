# Создание функции для определения вклада пользователя
def vklad(n, m):
    for i in range(m):
        i += 1
        n = n + (n / 100 * 10)
    print(n)
    # i = 0
    # while i < m:
    #     i += 1
    #     n = n + (n / 100 * 10)
    # print(n)
print(vklad(float(input()), int(input())))
