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

students_list = []

while True:
    data = input("Введите команду: ")
    command = data.split()[0]
    if command == "exit":
        break
    elif command == "help":
        print(help_message)
    elif command == "add":
        new_student = {"Имя студента": data.split()[1] + " " + data.split()[2], "Оценки": []}
        if new_student in students_list:
            print("Студент уже есть в списке!")
        else:
            students_list.append(new_student)
    elif command == "all":
        print(students_list)
    elif command == "mark":
        mark = int(data.split()[1])
        number = int(data.split()[2])
        new_number = students_list[number - 1]
        new_number["Оценки"].append(mark)
    elif command == "edit":
        number = int(data.split()[1])
        new_number = students_list[number - 1]
        new_number["Имя студента"] = data.split()[2] + " " + data.split()[3]
        new_number["Оценки"] = []
    elif command == "delete":
        number = int(data.split()[1])
        students_list.pop(number - 1)
    elif command == "average":
        number = int(data.split()[1])
        new_number = students_list[number - 1]
        average = float(sum(new_number["Оценки"]) / len(new_number["Оценки"]))
        print(average)
    else:
        print("Некорректная команда! Введите 'help' для вызова списка команд!")