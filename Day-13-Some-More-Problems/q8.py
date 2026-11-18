def chunks(numbers, k):
    reallist = []
    templist = []
    for i in range(0, len(numbers), k):
        templist = []
        for j in range(k):
            if i + j < len(numbers):
                templist.append(numbers[i + j])
        reallist.append(templist)
    return reallist


print(chunks([1, 2, 3, 4, 5], 2))
print(chunks([1, 2, 3], 5))