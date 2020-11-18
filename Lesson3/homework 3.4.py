#  Программа принимает действительное положительное число x и
#  целое отрицательное число y. Необходимо выполнить возведение
#  числа x в степень y. Задание необходимо реализовать в виде
#  функции my_func(x, y). При решении задания необходимо обойтись
#  без встроенной функции возведения числа в степень.

def my_expt(x, n):
	def my_degree(x, n):
		"""Функция для x^n без использования ** """
		i = 0
		degree = 1  # если не задать 1, будет умножение на 0 = 0
		while i < abs(n):
			degree = x * degree
			i += 1
		return degree

	if n >= 0:  # Вычисления для положительной степени
		return my_degree(x, n)
	if n < 0:  # Вычисления для отрицательной степени
		return 1 / my_degree(x, n)


x = float(input("Введит число x: "))
n = int(input("Введите показатель степени n: "))
print(f"Расчет через созданную функцию, {x}^{n}:", my_expt(x, n))
print("Расчет через встроенную функцию, {x}^{n}:", x ** n)
