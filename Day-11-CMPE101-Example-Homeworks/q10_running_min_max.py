def running_min_max(numbers):
    mins = numbers.copy()
    maxs = numbers.copy()
    for i in range(len(numbers) - 1):
        if mins[i] < mins[i + 1]:
            mins[i + 1] = mins[i]
        if maxs[i] > maxs[i + 1]:
            maxs[i + 1] = maxs[i]

    return mins, maxs


mins, maxs = running_min_max([5, 2, 7, 1, 6])
print(mins)
print(maxs)
