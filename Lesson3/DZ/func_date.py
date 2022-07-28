from datetime import date

def set_date(y, m, d):
    try:
        date(y, m, d)
        return "Ok!"
    except:
        return "Failed!"

#  !! не получается сделать исключения для високосных годов
# def set_date(d, m, y):
#     if d <= 0 or d > 31:
#         return "Failed!"
#     elif m <= 0 or m > 12:
#         return "Failed!"
#     elif y <= 0 or y > 9999:
#         return "Failed!"
#   !!!  elif y % 400 == 0:
#         if  d > 29 and m == 2:
#             return "Failed!"
#         else:
#             if d > 28 and m == 2:
#                 return "Failed!"
#     elif y % 4 == 0 and y % 100 != 0:
#         if  d > 29 and m == 2:
#             return "Failed!"
#         else:
#             if d > 28 and m == 2:
#                 return "Failed!"
#     elif m == 4 and d > 30:
#         return "Failed!"
#     elif m == 6 and d > 30:
#         return "Failed!"
#     elif m == 9 and d > 30:
#         return "Failed!"
#     elif m == 11 and d > 30:
#         return "Failed!"
#     else:
#         return "Ok!"
#

def vvod_date(vv_date):
    d = list(map(int, vv_date.split('.')))
    return set_date(d[2], d[1], d[0])
