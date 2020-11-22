# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
#
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
#
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

from random import randrange

my_list = [randrange(1, 100, 2) for el in range(1, 10)]
print(my_list)
print([my_list[i + 1] for i in range(len(my_list) - 1) if my_list[i] < my_list[i + 1]])
