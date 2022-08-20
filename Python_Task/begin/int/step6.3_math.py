import math
num1 = math.sqrt(2)     # вычисление корня квадратного из двух
num2 = math.ceil(3.8)   # округление числа вверх
num3 = math.floor(3.8)  # округление числа вниз
print(num1)
print(num2)
print(num3)

from math import sqrt
x1,y1,x2,y2= float(input()),float(input()),float(input()),float(input())
a=((x1-x2)**2) + ((y1-y2)**2)
print (sqrt(a))

#Площадь и длина
from math import sqrt
x1,y1,x2,y2= float(input()),float(input()),float(input()),float(input())
a=((x1-x2)**2) + ((y1-y2)**2)
print (sqrt(a))

#Правильный многоугольник
from math import tan, pi
n,a = float(input()),float(input())
x = pi/n
y = tan(x)
print((n*(a**2))/(4*y))















