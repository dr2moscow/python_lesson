# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

ss = int(input("Введите кол-во секунд: "))
dd = ss / 86400
hh = ss / 3600
ss %= 3600
mm = ss / 60
ss %= 60

print("%d дней или %.2d:%.2d:%.2d" % (dd, hh, mm, ss))

# Алтернативное решение
time = int(input("Enter the time in seconds: "))
hours = time // 3600
minutes = (time // 60) - (hours * 60)
seconds = time % 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")
