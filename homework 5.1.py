# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

try:
	with open("homework 5.1 result.txt", "w", encoding = "utf-8") as result:
		while True:
			user_data = input("Введите информацию:")
			if user_data == "":
				print(f"Спасибо, введеная информция сохранена в файл: {result.name}")
				break
			result.write(f"{user_data}\n")
except IOError:
	print("Error!")
