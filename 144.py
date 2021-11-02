#cd D:python/python/14
#144.py
#Измените п.3 так, как если бы функция была членом класса  Car.

def max(a, b):
	if (a > b):
		print (float(a))
	elif (b > a):
		print (float(b))
	else:
		print("none")

x = input("x: ")
y = input("y: ")


max(x, y)