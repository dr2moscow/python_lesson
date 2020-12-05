# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число). В классе должны быть
# реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
# деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и целочисленное (с округлением до целого) деление клеток,
# соответственно.
class Cell:
	def __init__(self, cell):
		self.cell = cell

	def make_order(self, row):
		self.row = row
		star = ""
		a = 0
		for i in range(self.cell):
			if a == self.row:
				star = star + "\n"
				a = 0
			star = star + "*"
			a += 1
		print(star)

	def __add__(self, other):
		return Cell(self.cell + other.cell)

	def __str__(self):
		return f"{self.cell}"

	def __mul__(self, other):
		cell = int(self.cell * other.cell)
		if cell <= 0:
			cell = "клетки не размножились"
		return cell

	def __sub__(self, other):
		cell = int(self.cell - other.cell)
		if cell < 0:
			cell = "клетки погибли"
		return cell

	def __floordiv__(self, other):
		cell = int(self.cell // other.cell)
		if cell <= 0:
			cell = "клетки погибли"
		return cell


cell_1 = Cell(23)
cell_2 = Cell(3)

print(f"Сейчас у нас ячеек {cell_1} и {cell_2}")
print(f"Колдуем (+), ячеек: {cell_1 + cell_2}")
print(f"Колдуем (*), ячеек: {cell_1 * cell_2}")
print(f"Колдуем (-), ячеек: {cell_1 - cell_2}")
print(f"Колдуем (/), ячеек: {cell_1 // cell_2}")

row = 5
print(f"\nРисуем клетку из {cell_1} ячеек по {row} в ряд:")
cell_1.make_order(row)
