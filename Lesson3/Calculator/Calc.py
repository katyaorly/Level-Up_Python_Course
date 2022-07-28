def vvod():
    in_str = input().split()
    x1 = in_str[0]
    x2 = in_str[2]
    sign = in_str[1]
    return int(x1), sign, int(x2)

def calculate(x1, sign, x2):
    if sign == "+":
        return x1 + x2
    elif sign == "-":
        return x1 - x2
    elif sign == "*":
        return x1 * x2
    elif sign == "/":
        if x2 == 0:
            print("Ошибка! На ноль делить нельзя!")
        else:
            return x1 / x2