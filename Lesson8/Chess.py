#  Вывод черная/белая клетка на шахматной доске по ее номеру

letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
let = input("Введите номер буквы: ")
dig = int(input("Введите номер цифры: "))
dig_num = letters.index(let) + 1
if dig % 2 == dig_num % 2:
    print(f"{str(let) + str(dig)} - черная клетка")
else:
    print(f"{str(let) + str(dig)} - белая клетка")
