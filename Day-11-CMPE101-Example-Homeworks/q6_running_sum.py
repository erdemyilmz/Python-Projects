def running_sum(numbers):
    sum = 0
    if len(numbers) == 0:
        return []
    else:
        for i in range(len(numbers)):
            sum += numbers[i]
            numbers[i] = sum

        return numbers


print(running_sum([1, 2, 3, 4]))
print(running_sum([]))
