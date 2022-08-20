#Три последовательных числа
x = int(input())
y = x + 1
z = y + 1
print(x)
print(y)
print(z)
#Сумма трёх чисел
x1 = int(input())
x2 = int(input())
x3 = int(input())
print(x1 + x2 + x3)
#Куб
a = int(input())
V = a**3
S = 6*a**2
print("Объём =", V)
print("Площадь полной поверхности =", S)
#Значение функции
a = int(input())
b = int(input())
print(3*(a + b)**3 + 275*b**2 -127*a -41)
#Следующее и предыдущее
x = int(input())
y = x - 1
z = x + 1
print('Следующее за числом', x, 'число:', z)
print('Для числа', x, 'предыдущее число:', y)
#Стоимость покупки
a = int(input())
b = int(input())
c = int(input())
d = int(input())
S = (a + b + c + d)* 3
print(S)
#Арифметические операции
a = int(input())
b = int(input())
f1 = a + b
f2 = a - b
f3 = a * b
print(a, '+', b, '=', f1)
print(a, '-', b, '=', f2)
print(a, '*', b, '=', f3)
#Арифметическая прогрессия
print(int(input()) + int(input())*(int(input()) - 1))
#Геометрическая прогрессия
b1 = int(input())
q = int(input())
n = int(input())
bn = b1*q**(n-1)
print(bn)
#Расстояние в метрах
n = 100
print(m // n)
#Программа должна вывести одно число – номер купе, в котором находится указаное место
m = int(input())
n = 4
k = (m + n - 1)//4
print(k)
#Пересчет временного интервала
c = int(input())
print(c, 'мин - это', c//60, 'час', c%60, 'минут.')
#Трехзначное число
num =  int(input())
a, b, c, = num%10, (num%100)//10, num//100
print("Сумма цифр =", a + b + c)
print("Произведение цифр =", a * b * c)









