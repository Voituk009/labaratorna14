#cd D:python/python/14
#1411.py
#Добавьте еще две переменные- члена в класс. 
#Включите функции доступа, принимающие значения этих переменных, 
#обеспечив при этом всем функциям- членам одинаковый тип возврата 
#и сигнатуры. Используйте указатель на функцию-член для доступа к этим функциям.

class Transport:

	__static_fuil = 0
	__static_speed = 0
	__static_weight = 0
	color = ""

	def __init__(self, color, fuil, speed, weight):
		self.color = color
		self.__static_fuil = fuil + 10
		self.__static_speed = speed + 5
		self.__static_weight = weight + 15

	def print_protected_data(self):
		print("Цвет:",self.color,",","Количество топлива:" ,self.__static_fuil,
			",","Скорость: ",self.__static_speed,",","Вес",self.__static_weight,"\n")

	def __del__(self):
		self.__static_fuil = self.__static_fuil - self.__static_fuil 
		self.__static_speed = self.__static_speed - self.__static_speed
		self.__static_weight = self.__static_weight - self.__static_weight



print("Машина 1")
Tr1 = Transport("red", 50, 45, 1640)
Tr1.print_protected_data()

print("Машины 2")
Tr2 = Transport("Blue", 70, 64, 1385)
Tr2.print_protected_data()

print("Машина 3")
Tr3 = Transport("Black", 60, 53, 1547)
Tr3.print_protected_data()