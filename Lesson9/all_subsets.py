def all_subset(data):
    subsets = [[]]
    for i in range(len(data)):
        for j in range(len(subsets)):
            new_subset = subsets[j] + [data[i]]
            subsets = subsets + [new_subset]
    return subsets

x = [int(i) for i in input().split()]
print(all_subset(x))
