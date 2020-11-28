# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный. В рамках метода
# реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его
# нарушении выводить соответствующее сообщение и завершать скрипт.
import time
import turtle


class TrafficLight:
	def __init__(self, color):
		self.__color = color

	# методы класса
	def running(self):
		pen = turtle.Turtle()
		pen.color("black")
		pen.width(3)
		pen.hideturtle()

		pen.penup()
		pen.setposition(-30, 60)
		pen.pendown()
		pen.forward(60)
		pen.right(90)
		pen.forward(120)
		pen.right(90)
		pen.forward(60)
		pen.right(90)
		pen.forward(120)

		red_light = turtle.Turtle()  # создаем объект
		red_light.shape('circle')  # делаем круг
		red_light.color('grey')  # меняем цвет на серый
		red_light.penup()
		red_light.setposition(0, 40)  # позиция лампы

		yellow_light = turtle.Turtle()
		yellow_light.shape('circle')
		yellow_light.color('grey')
		yellow_light.penup()
		yellow_light.setposition(0, 00)

		green_light = turtle.Turtle()
		green_light.shape('circle')
		green_light.color('grey')
		green_light.penup()
		green_light.setposition(0, -40)

		n = 1
		for n in range(10):
			red_light.color('red')
			time.sleep(7)
			yellow_light.color('yellow')
			time.sleep(1)
			red_light.color('grey')
			time.sleep(2)
			green_light.color('green')
			yellow_light.color('grey')
			time.sleep(10)
			yellow_light.color('yellow')
			time.sleep(1)
			green_light.color('grey')
			yellow_light.color('grey')
			n += 1


traffic = TrafficLight("green")
traffic.running()
