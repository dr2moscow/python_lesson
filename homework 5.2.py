# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

try:
	with open("homework 5.1 result.txt", "r", encoding = "utf-8") as result:
		content = result.readlines()
		print(f"Анализирую файл {result.name}")
		print(f"Кол-во строк: {len(content)}")
		for i in range(len(content)):
			print(f"Строка {i + 1}, кол-во слов {len(content[i].split())}")

except IOError:
	print("Error!")
