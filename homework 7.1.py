# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
# класса (метод __init__()), который должен принимать данные (список списков)
# для формирования матрицы.
#
# Подсказка: матрица — система некоторых математических величин, расположенных
# в виде прямоугольной схемы.

class Matrix:
	def __init__(self, matrix):
		self.matrix = matrix

	def __add__(self, other):
		try:
			result = []
			numbers = []
			for y in range(len(self.matrix)):
				for x in range(len(self.matrix[0])):
					summa = other[y][x] + self.matrix[y][x]
					numbers.append(summa)
					if len(numbers) == len(self.matrix):
						result.append(numbers)
						numbers = []
			return Matrix(result)
		except IndexError:
			return f"Ошибка размернойстей матрицы"

	def __str__(self):
		return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

	def __getitem__(self, index):
		return self.matrix[index]


matrix_1 = Matrix([[1, 2, 3], [3, 4], [5, 6]])
matrix_2 = Matrix([[3, 0], [3, 3], [9, 6]])

print(f"Матрица №1\n{matrix_1}\n\nМатрица №2\n{matrix_2}")
print(f"\nСумма матриц:")
print(matrix_1 + matrix_2)
