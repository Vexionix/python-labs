class Matrix:
    def __init__(self, n, m):
        self.rows = n
        self.cols = m
        self.data = [[0 for _ in range(m)] for _ in range(n)]

    def get(self, i, j):
        return self.data[i][j]

    def set(self, i, j, value):
        self.data[i][j] = value

    def transpose(self):
        transpose_matrix = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transpose_matrix.set(j, i, self.data[i][j])
        return transpose_matrix

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("The given matrices do not meet the requirements for multiplying.")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    def apply(self, func):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = func(self.data[i][j])

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str

matrix = Matrix(2, 3)
matrix.set(0, 0, 1)
matrix.set(0, 1, 2)
matrix.set(0, 2, 3)
matrix.set(1, 0, 4)
matrix.set(1, 1, 5)
matrix.set(1, 2, 6)

another_matrix = Matrix(3, 2)
another_matrix.set(0, 0, 1)
another_matrix.set(0, 1, 2)
another_matrix.set(1, 0, 3)
another_matrix.set(1, 1, 4)
another_matrix.set(2, 0, 5)
another_matrix.set(2, 1, 6)

print("Original matrix:")
print(matrix)

print("Second matrix:")
print(another_matrix)

transposed_matrix = matrix.transpose()
print("\nTransposed (initial) matrix:")
print(transposed_matrix)

multiplied_matrix = matrix.multiply(another_matrix)
print("\nMultiplied matrix with another_matrix:")
print(multiplied_matrix)

matrix.apply(lambda x: x * 2)
print("\nMatrix after applying lambda function (x * 2):")
print(matrix)
