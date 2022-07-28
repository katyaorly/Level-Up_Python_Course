from Calculator.Calc import vvod, calculate

x1, sign, x2  = vvod()
print(x1, sign, x2, end=" = ")
result = calculate(x1, sign, x2)
if result is not None:
    print(result)