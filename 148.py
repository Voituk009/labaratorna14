#cd D:python/python/14
#148.py
#Напишите драйвер к п.7, в котором создается три объекта и 
#на экран выводятся значения обычной и статической переменных 
#членов класса. Уничтожьте эти объекты и проследите как будет 
#меняться значение статической переменной члена.

class Transport:

	static_fuil = 0
	color = ""

	def __init__(self, color, static_fuil):
		self.color = color
		self.static_fuil = static_fuil + 10

	def print(self):
		print("Цвет:",self.color,",","Количество топлива:" ,self.static_fuil, "\n")

	def __del__(self):
		self.static_fuil= self.static_fuil - self.static_fuil 



print("Машина 1")
Tr1 = Transport("red", 50)
Tr1.print()

print("Машины 2")
Tr2 = Transport("Blue", 70)
Tr2.print()

print("Машина 3")
Tr3 = Transport("Black", 60)
Tr3.print()