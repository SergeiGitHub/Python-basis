class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):  # срабатывает при передаче объекта функциям str() и print(), преобразует объект к строке
        return '\n'.join(" ".join(str(el) for el in row) for row in self.matrix)

    def __add__(self, other):  # срабатывает при участии объекта в операции сложения в качестве операнда с левой
        # стороны, обеспеивает перегрузку оператора сложения
        return [[a + b for a, b in zip(my_row, other_row)] for my_row, other_row in zip(self.matrix, other.matrix)]


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(matrix_1)
print(matrix_1 + matrix_2)
