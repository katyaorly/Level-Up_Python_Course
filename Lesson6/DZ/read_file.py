#  считывает путь до файла из консоли и выводит самое длинное слово из файла

f1 = input("Введите название исходного файла: ")
f2 = input("Введите название входного файла: ")
try:
    f1 = open(f1)
    f2 = open(f2, mode="w", encoding="utf8")
except FileNotFoundError:
    print("Файл не найден")
else:
    lines = f1.readlines()
    f2.write(max(lines, key=len))
    f1.close()
    f2.close()

