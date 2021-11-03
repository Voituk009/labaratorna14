#cd D:python/python/14
#149.py
#Сделайте статическую переменную п.7-8 приватной. 
#Напишите и используйте статическую функцию-член для 
#доступа к приватной статической переменной члену?

class Transport:

	__static_fuil = 0
	color = ""

	def __init__(self, color, _static_fuil):
		self.color = color
		self.__static_fuil = _static_fuil + 10

	def print_protected_data(self):
		print("Цвет:",self.color,",","Количество топлива:" ,self.__static_fuil, "\n")

	def __del__(self):
		self.__static_fuil = self.__static_fuil - self.__static_fuil 



print("Машина 1")
Tr1 = Transport("red", 50)
Tr1.print_protected_data()

print("Машины 2")
Tr2 = Transport("Blue", 70)
Tr2.print_protected_data()

print("Машина 3")
Tr3 = Transport("Black", 60)
Tr3.print_protected_data()