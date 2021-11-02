#cd D:python/python/14
#143.py
#Напишите объявление указателя на функцию, возвращающую long и принимающую целое.

def max(a, b):
	if (a > b):
		print (int(a))
	elif (b > a):
		print (int(b))
	else:
		print("none")

x = float(input("x: "))
y = float(input("y: "))


max(x, y)