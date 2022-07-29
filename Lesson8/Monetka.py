#  подброс монетки до выпадания орла или решки 3 раза подряд

from random import randint
from statistics import mean

coin = []
count = []

for i in range(1, 100):
    for j in range(1, 100):
        random_number = randint(1, 2)
        coin.append(random_number)
        if random_number == 1:
            print("О", end=" ")
        else:
            print("P", end=" ")

        if int(len(coin)) > 2 and coin[-1] == coin[-2] == coin[-3]:
            count.append(j)
            print(f"(Количество попыток = {j})")
            coin = []
            break

print(f"\n"
      f"Максимальное количество попыток - {max(count)} \n"
      f"Минимальное количество попыток - {min(count)} \n"
      f"Среднее количество попыток - {round(mean(count), 1)} \n")