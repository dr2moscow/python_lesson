# Создать (не программно) текстовый файл, в котором каждая строка
# должна содержать данные о фирме: название, форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки,
# в расчет средней прибыли ее не включать.
#
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить
# ее в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

with open("text_7.txt", "r", encoding = "utf-8") as result:
	lines = result.readlines()
	lines_len = len(lines)
	lines = [line.rstrip('\n') for line in lines]
	sum_proffit = 0
	sum_proffit_count = 0
	my_dic = {}

	for i in range(lines_len):
		company, type_company, revenue, cost = lines[i].split()
		profit = int(revenue) - int(cost)
		if profit > 0:
			print(f"{company} {type_company}, прибыль {profit}")
			sum_proffit += profit
			sum_proffit_count += 1
			my_dic[company] = profit
		else:
			print(f"{company} {type_company}, убыток {profit}")
			my_dic[company] = profit
	my_dic_proffit = {}
	my_dic_proffit["average_profit"] = sum_proffit / sum_proffit_count
	my_dic_total = [my_dic, my_dic_proffit]
	print(f"\nСредняя прибыль {sum_proffit_count} компаний: {sum_proffit / sum_proffit_count}")

with open("text_7.json", "w", encoding = "utf-8") as write_f:
	json.dump(my_dic_total, write_f, ensure_ascii = False, indent = 4)
	print(f"\nИнформация сохранена в файле {write_f.name}")
