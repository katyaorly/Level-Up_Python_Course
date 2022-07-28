# Программа интерактивной работы с консолью
# (электронный дневник для студентов одной группы по одному предмету)
help_message = """ 
Интерактивный дневник
Список команд:
add <Имя> <Фамилия> - Добавить ученика
all - Вывести список учеников. Вывод - [Список]
mark <Оценка> <Номер> - Добавить ученику оценку
edit <Номер> <Имя> <Фамилия> - Изменяет имя
delete <Номер> - Удаляет ученика
average - Список со средним баллом. Вывод - [Список]
"""
from func_interact_diary import func_add, func_mark, func_all, func_edit, func_delete, func_average_mark

my_dict = {}
number = 1

while True:
    cmd = input("Введите команду:").split()
    if cmd[0] == "exit":
        break
    if cmd[0] == "help":
        print(help_message)
    elif cmd[0] == "add":
        my_dict = func_add(cmd[1] + " " + cmd[2], number,  my_dict)
        number += 1
    elif cmd[0] == "all":
        func_all(my_dict)
    elif cmd[0] == "mark":
        my_dict = func_mark(int(cmd[1]), int(cmd[2]), my_dict)
    elif cmd[0] == "edit":
        my_dict = func_edit(int(cmd[1]), cmd[2] + " " + cmd[3], my_dict)
    elif cmd[0] == "delete":
        my_dict = func_delete(int(cmd[1]), my_dict)
        number -= 1
    elif cmd[0] == "average":
        func_average_mark(my_dict)
    else:
        print("Некорректная команда! Введите 'help' для вызова списка команд!")