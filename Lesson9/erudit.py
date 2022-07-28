erudit = {1 : ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'], 2 : ['D', 'G'], 3 : ['B', 'C', 'M', 'P'], 4 : ['F', 'H', 'V', 'W', 'Y'], 5 : ['K'], 8 : ['J', 'X'], 10: ['Q', 'Z']}
data = input('Введите слово: ')
summ = 0
for point in erudit:
    for i in data:
        if i in erudit[point]:
            summ = summ + point

print(summ)