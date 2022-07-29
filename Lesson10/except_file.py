#  прочитать файл, удалить строку с #, записать в новый файл

try:
    f = open("test.txt", mode="r", encoding="utf8")
    fw = open("test1.txt", mode="w", encoding="utf8")
except FileNotFoundError:
    print("Файл не найден")
else:
    lines = f.readlines()
    for i in lines:
        if i[0] != "#":
            fw.write(i)
finally:
    f.close()
    fw.close()

