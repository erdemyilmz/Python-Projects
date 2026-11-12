data = [3, -2, 5, -8, 0]


def zero_negatives(numbers):
    for element in numbers:
        if element < 0:
            data[data.index(element)] = 0

    return None


zero_negatives(data)
print(data)
