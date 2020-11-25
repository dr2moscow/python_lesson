# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
# выводить ее на экран.

try:
	with open("homework 5.5 result.txt", "w", encoding = "utf-8") as result:
		user_data = input("Введите набор чисел разделенные пробелами:")
		result.write(f"{user_data}\n")
		print(f"Результат записан в файл {result.name}\n")

	with open("homework 5.5 result.txt", "r", encoding = "utf-8") as result:
		digital = result.readline().split()
		summ = 0
		for i in range(len(digital)):
			summ += int(digital[i])
		print(f"Сумма чисел в файле {result.name} составила: {summ}")

except IOError:
	print("Error!")
