# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
#
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(word):
	my_dic = {"a": "A", "b": "B", "c": "C", "d": "D", "e": "E", "f": "F", "g": "G", "h": "H", "i": "I",
	          "j": "J", "k": "K", "l": "L", "m": "M", "n": "N", "o": "O", "p": "P", "q": "Q", "r": "R",
	          "s": "S", "t": "T", "u": "U", "v": "V", "w": "W", "x": "X", "y": "Y", "z": "Z"}
	word_transfer = my_dic[word[0]] + word[1:]
	return word_transfer + " "


my_str = "COOL авп dfsвыв hkjjпаро gOOd dfhыва nice Pepsi".split()
my_str_transfer = ""
for i in range(len(my_str)):
	word = my_str[i].lower()
	for a in range(len(word)):
		if 110 > ord(word[a]) < 122:
			word_good = True
		else:
			word_good = False  # если в слове есть буква не из латинского алфавита
	if word_good == True:
		my_str_transfer += int_func(word)

print(my_str_transfer)
