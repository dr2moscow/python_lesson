# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операци

digital = int(input("Введите целое положительное число: "))
digital_int = 0
big_digital = 0

while digital != 0:
    digital_int = digital % 10
    digital //= 10
    if big_digital < digital_int:
        big_digital = digital_int

print("Самое большая цифра в Вашем числе: ", big_digital)
