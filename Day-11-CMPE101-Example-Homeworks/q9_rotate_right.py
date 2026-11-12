def rotate_right(numbers, k):
    original = numbers.copy()
    for i in range(len(numbers)):
        if i + k < len(numbers):
            numbers[i + k] = original[i]
        else:
            numbers[(i + k) % len(numbers)] = original[i]
    return numbers


print(rotate_right([1, 2, 3, 4, 5], 2))
print(rotate_right([1, 2, 3, 4, 5], 7))
print(rotate_right([1, 2, 3], 0))
