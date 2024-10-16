def replace_diagonal_to_0(matrix: [[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                matrix[i][j] = 0
    return matrix

# we assume the given matrix is valid for the logic

matrix = [[1,2,3], [4,5,6], [7,8,9]]

print("Initial matrix:")
for line in matrix:
    print(line)

matrix = replace_diagonal_to_0(matrix)
print("New matrix:")
for line in matrix:
    print(line)
