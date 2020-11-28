# Реализуйте базовый класс Car. У данного класса должны быть
# следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда). Опишите несколько
# дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов
# методов и также покажите результат.
from random import randint


class Car:
	def __init__(self, speed, color, name, is_police):
		self.speed = speed
		self.color = color
		self.name = name
		self.is_police = is_police

	def go(self):
		print(f"Поехали!")

	def stop(self):
		print("Остановились!")

	def turn(self, direction):
		self.direction = direction
		print(f"Поверните на {direction}!")

	def show_speed(self):
		print(f"your speed {self.speed}")


class TownCar(Car):
	def towncar(self, speed, is_police):
		self.speed = speed
		self.is_police = is_police
		if self.speed > 60:
			if self.is_police == False:
				print(f"Ваша скорость {speed} км, превышаете! Сбавьте скорость!")
			else:
				print(f"Ваша скорость {speed} км господин полицейский, удачи!")
		else:
			print(f"Ваша скорость {speed} км, вы примерный гражданин!")


class WorkCar(Car):
	def workcar(self, speed, is_police):
		self.speed = speed
		self.is_police = is_police
		if self.speed > 40:
			if self.is_police == False:
				print(f"Ваша скорость {speed} км, превышаете! Сбавьте скорость!")
			else:
				print(f"Ваша скорость {speed} км господин полицейский, удачи!")
		else:
			print(f"Ваша скорость {speed} км, вы примерный гражданин!")


class SportCar(Car):
	def sportcar(self, speed, is_police):
		self.speed = speed
		self.is_police = is_police
		if self.speed > 120:
			if self.is_police == False:
				print(f"Ваша скорость {speed} км, превышаете! Сбавьте скорость!")
			else:
				print(f"Ваша скорость {speed} км господин полицейский, удачи!")
		else:
			print(f"Ваша скорость {speed} км, вы примерный гражданин!")


class PoliceCar(Car):
	def policecar(self, speed, is_police):
		self.speed = speed
		self.is_police = is_police
		if self.speed > 120:
			if self.is_police == False:
				print(f"Ваша скорость {speed} км, и вы не полцейски! Мы вас найдем")
			else:
				print(f"Ваша скорость {speed} км господин полицейский, удачи!")
		else:
			print(f"Ваша скорость {speed} км, вы на обед?")


def my_random():
	z = randint(0, 3)
	i = randint(1, 100)
	p = randint(0, 1)
	return z, i, p


car_color = ["красного", "черного", "белого", "зеленого"]
car_model = ["Mercedes", "Volvo", "ZAZ", "Lada"]
car_turn = ["лево", "право"]
car_type = ["TownCar", "WorkCar", "SportCar", "PoliceCar"]
car = Car(60, "зеленый", "ZAZ", True)

print("Пристегните ремни, сейчас будет увлекательная поездка по городу!")
while True:
	if input("Если у вас изменились планы, для выхода нажмите - q, или нажмите Enter для продолжения: ") == "q":
		break
	z, i, p = my_random()
	if z == 0:
		t = TownCar(i, car_color[z], car_model[z], p)
		print(f"Вы за рулем городской машины марки {t.name}, {t.color} цвета")
		car.go()
		car.turn(car_turn[p])
		t.towncar(i, p)
		car.stop()
	if z == 1:
		t = SportCar(i, car_color[z], car_model[z], p)
		print(f"Вы за рулем спортивной машины марки {t.name}, {t.color} цвета")
		car.go()
		car.turn(car_turn[p])
		t.sportcar(i, p)
		car.stop()
	if z == 2:
		t = WorkCar(i, car_color[z], car_model[z], p)
		print(f"Вы за рулем уборочной машины марки {t.name}, {t.color} цвета")
		car.go()
		car.turn(car_turn[p])
		t.workcar(i, p)
		car.stop()
	if z == 3:
		t = PoliceCar(i, car_color[z], car_model[z], p)
		print(f"Вы за рулем полицейской машины марки {t.name}, {t.color} цвета")
		car.go()
		car.turn(car_turn[p])
		t.policecar(i, p)
		car.stop()
