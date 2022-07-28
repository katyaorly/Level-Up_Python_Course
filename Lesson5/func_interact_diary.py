
def func_add(student, number, my_dict):
    my_dict[number] = {student: []}
    print("OK")
    return my_dict

def func_all(my_dict):
    for k1, v1 in my_dict.items():
        for k2, v2 in v1.items():
            if v2 == []:
                print(f"{k1}. {k2}")
            else:
                print(f"{k1}. {k2}", end=" ")
                for i in range(len(v2)):
                    if i == len(v2) - 1:
                        print(f"{v2[i]}", end=" ")
                    else:
                        print(f"{v2[i]},", end=" ")
                print("")

def func_mark(mark, number, my_dict):
    for v in my_dict[number].values():
        v.append(mark)
    print("OK")
    return my_dict

def func_edit(number, new_student, my_dict):
    for v in my_dict[number].values():
        my_dict[number] = {new_student: v}
    print("OK")
    return my_dict

def func_delete(number, my_dict):
    del my_dict[number]
    print("OK")
    return my_dict  # не знаю, как сделать уменьшение number при удалении

def func_average_mark(my_dict):
    for k1, v1 in my_dict.items():
        for k2, v2 in v1.items():
            if v2 == []:
                print(f"{k1}. {k2}")
            else:
                print(f"{k1}. {k2}", end=" ")
                s = 0
                for i in v2:
                    s += i
                print(f"{s / len(v2)}")

