def count_fixed_points(numbers):
    count = 0
    for i in range(len(numbers)):
        if i == numbers[i]:
            count += 1

    return count


print(count_fixed_points([0, 2, 2, 3]))
print(count_fixed_points([-1, 1, 2, 4, 3]))
