def product_except_self(numbers):
    replicate = numbers.copy()
    for i in range(len(numbers)):
        product = 1
        remainings = replicate.copy()
        remainings.pop(i)
        for element in remainings:
            product *= element
        numbers[i] = product
    return numbers


print(product_except_self([1, 2, 3, 4]))
print(product_except_self([0, 5, 2]))
