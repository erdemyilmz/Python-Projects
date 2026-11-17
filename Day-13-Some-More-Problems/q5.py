def differences(numbers):
    differencelist = []
    if len(numbers) < 2:
        return []
    else:
        for element in numbers:
            if numbers.index(element) != len(numbers) -1:
                differencelist.append(numbers[numbers.index(element)+1] - element)

        return differencelist

print(differences([5, 7, 3, 9]))
print(differences([4]))