# Реализовать структуру «Рейтинг», представляющую собой не возрастающий
# набор натуральных чисел. У пользователя необходимо запрашивать новый
# элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
#
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде,
# например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
min = 9
while True:
	print("Рейтинг:", my_list)
	my_list_len = len(my_list)
	user_rating = input('Введите новый элемент рейтинга. Для выхода нажмите q: ')
	if user_rating == 'q':
		break
	if not user_rating.isdigit():
		print('только натуральные числа или q для выхода')
		continue
	user_rating = int(user_rating)
	for count in range(my_list_len):
		if min > my_list[count]:
			min = my_list[count]
	if user_rating == 0:
		my_list.insert(my_list_len + 1, user_rating)
		continue
	if user_rating < min:
		my_list.insert(my_list_len, user_rating)
		continue
	else:
		for i in range(my_list_len):
			if user_rating > my_list[i]:
				my_list.insert(i, user_rating)
				break
			else:
				continue
