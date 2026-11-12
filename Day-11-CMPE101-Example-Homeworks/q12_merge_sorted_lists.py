def merge(a, b):
    mergedlist = a + b
    for i in range(len(mergedlist)):
        for j in range(len(mergedlist) - 1):
            if mergedlist[j + 1] < mergedlist[j]:
                mergedlist[j], mergedlist[j + 1] = mergedlist[j + 1], mergedlist[j]

    return mergedlist


print(merge([1, 3, 5], [2, 4, 6]))
print(merge([], [1, 2]))
print(merge([1, 1, 4], [1, 2]))
