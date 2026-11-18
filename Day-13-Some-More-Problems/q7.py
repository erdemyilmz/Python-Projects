def record_highs(numbers):
    mylist = []
    for i in range(len(numbers)-1):
        if numbers[i] < numbers[i+1] or i == 0:
            mylist.append(numbers[i+1])

    return mylist


print(record_highs([2, 2, 3, 1, 5, 4, 6]))
print(record_highs([]))