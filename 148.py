#cd D:python/python/14
#148.py
#8.	Напишите драйвер к п.7, в котором создается три объекта и 
#на экран выводятся значения обычной и статической переменных 
#членов класса. Уничтожьте эти объекты и проследите как будет 
#меняться значение статической переменной члена.

class Transport:

	static_speed = 0
	color = ""

	def __init__(self, color, static_speed):
		self.color = color
		self.static_speed = static_speed + 1

	def print(self):
		print(self.color, self.static_speed)

	def __del__(self):
		self.static_speed = self.static_speed - 1
		print(self.static_speed)



Tr = Transport("red", 50)

Tr.print()