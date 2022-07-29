# def Is_Subset(x, y):
#     if set(y) < set(x):
#         return True
#     else:
#         return False

x = {int(i) for i in input().split()}
y = {int(i) for i in input().split()}
# a = Is_Subset(x, y)
print(y.issubset(x))
