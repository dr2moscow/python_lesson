# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
from googletrans import Translator

try:
	print("Переводим через собственный словарь:")
	my_dic = {1: "Один", 2: "Два", 3: "Три", 4: "Четыре", 5: "Пять", 6: "Шесть", 7: "Семь", 8: "Восемь", 9: "Девять"}
	with open("text_4.txt", "r", encoding = "utf-8") as result:
		content = result.readlines()
		for i in range(len(content)):
			a, b, c = content[i].split()
			content_result = my_dic[int(c)] + " " + b + " " + c
			print(content_result)
			with open("text_4_new.txt", "a", encoding = "utf-8") as result_end:
				result_end.write(f"{content_result}\n")
except IOError:
	print("Error!")

# ----------------------------- реализация через google translate ------------------------------
try:
	translator = Translator()
	print("\nПереводим через внешний сервис Google Translate:")
	with open("text_4.txt", "r", encoding = "utf-8") as result:
		content = result.readlines()
		for i in range(len(content)):
			a, b, c = content[i].split()
			my_dic_translate = translator.translate(a, dest = "ru")
			content_result = my_dic_translate.text + " " + b + " " + c
			print(content_result)
			with open("text_4_google.txt", "a", encoding = "utf-8") as result_end:
				result_end.write(f"{content_result}\n")
except AttributeError:
	print("Гугл опять распоясался и не переводит, мы уже принимаем меры!")
