#cd D:python/python/14
#147.py
#7.	Напишите небольшую программу с объявлением класса, 
#имеющего одну переменную-член  и одну статическую переменную-член. 
#Пусть конструктор инициализирует переменную-член и инкрементирует 
#статическую переменную член, а деструктор – декрементирует ее.

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