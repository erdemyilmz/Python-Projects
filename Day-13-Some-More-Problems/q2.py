def swap_ends(numbers):
    numbers[0], numbers[-1] = numbers[-1], numbers[0]

data = [1, 2, 3, 4]
swap_ends(data)
print(data)
one = [5]
swap_ends(one)
print(one)