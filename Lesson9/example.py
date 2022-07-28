# a = [23, 14, 54]
# b = ['bread', 'butter', 'eggs']
# c = dict(zip(a, b))
# print(c)

a = ['s001', 's002', 's003']
b = ['Ivanov Ivan', 'Petrov Petr', 'Igor Igorev']
c = [73, 84, 93]

students = []
for i in range(len(a)):
    group_number = a[i]
    name = b[i]
    mark = c[i]

    d = {}
    d_m = {name: mark}
    d[group_number] = d_m

    students.append(d)
print(students)


a = ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U']
b = ['D', 'G']
c = ['B', 'C', 'M', 'P']
d = ['F', 'H', 'V', 'W', 'Y']
e = ['K']
f = ['J', 'X']
g = ['Q', 'Z']




