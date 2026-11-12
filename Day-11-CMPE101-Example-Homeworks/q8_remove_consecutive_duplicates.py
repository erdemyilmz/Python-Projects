def squeeze(numbers):
    unseen = []
    for i in range(len(numbers) - 1):
        if numbers[i] != numbers[i + 1] or i == len(numbers) - 2:
            unseen.append(numbers[i])

    return unseen


print(squeeze([1, 1, 2, 2, 2, 3, 1, 1]))
print(squeeze([]))
