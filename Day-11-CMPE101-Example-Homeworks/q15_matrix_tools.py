def transpose(matrix):
    if len(matrix) == 0:
        return []

    result = []

    for column in range(len(matrix[0])):
        new_row = []

        for row in range(len(matrix)):
            new_row.append(matrix[row][column])

        result.append(new_row)

    return result


def diagonal_sum(matrix):
    total = 0
    index1 = 0
    index2 = len(matrix) - 1

    for liste in matrix:
        total += liste[index1]

        if index1 != index2:
            total += liste[index2]

        index1 += 1
        index2 -= 1

    return total


print(transpose([[1, 2, 3], [4, 5, 6]]))
print(diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(diagonal_sum([[1, 2], [3, 4]]))
