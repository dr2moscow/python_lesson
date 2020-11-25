# Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников

try:
	with open("text_3.txt", "r", encoding = "utf-8") as result:
		content = result.readlines()
		print(f"Анализирую файл {result.name}")
		print(f"Кол-во сотрудников: {len(content)}\nСотрудники с окладом менее 20000 руб.:")
		summ = 0
		n = 0
		for i in range(len(content)):
			a, b = content[i].split()
			if float(b) < 20000:
				n += 1
				print(n, a)
			summ = summ + float(b)
		print("\nСредния величина дохода всех сотрудников: %.2f" % (summ / len(content)), "руб.")
except IOError:
	print("Error!")
