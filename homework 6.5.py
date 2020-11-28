# Реализовать класс Stationery (канцелярская принадлежность). Определить
# в нем атрибут title (название) и метод draw (отрисовка). Метод выводит
# сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
# переопределение метода draw. Для каждого из классов метод должен выводить
# уникальное сообщение. Создать экземпляры классов и проверить, что выведет
# описанный метод для каждого экземпляра.

class Stationery:
	title = "Запуск отрисовки"

	def draw(self):
		self.title = "Запуск отрисовки"
		return self.title


class Pen(Stationery):
	def draw(self):
		self.title = "ручкой"
		return self.title


class Pencil(Stationery):
	def draw(self):
		self.title = "карандошом"
		return self.title


class Handle(Stationery):
	def draw(self):
		self.title = "маркером"
		return self.title


my_draw = Stationery()

my_draw_pen = Pen()
print(my_draw.draw(), my_draw_pen.draw())

my_draw_pencil = Pencil()
print(my_draw.draw(), my_draw_pencil.draw())

my_draw_handle = Handle()
print(my_draw.draw(), my_draw_handle.draw())
