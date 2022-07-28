# # поиск локального максимума
# a_l = [int(i) for i in input().split()]
#
# for i in range(1, len(a_l) - 1):
#     if a_l[i] > a_l[i + 1] and a_l[i] > a_l[i - 1]:
#         print(a_l[i])

# поиск уникальных элементов

a = [int(i) for i in input().split()]
for i in a:
    if a.count(i) == 1:
        print(a)