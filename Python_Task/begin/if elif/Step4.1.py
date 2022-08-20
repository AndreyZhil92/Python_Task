answer = input('Какой язык программирования мы изучаем?')
if answer == 'Python':
    print('Верно! Мы ботаем Python =)')
    print('Python - отличный язык!')
else:
    print('Не совсем так!')
#Пароль
a = input()
b = input()
if a == b:
  print('Пароль принят')
else:
  print('Пароль не принят')
#Четное или нечетное?
n = int(input())
if n % 2 == 0:
    print('Четное')
else:
    print('Нечетное')
#Программа должна вывести «ДА», если соотношение выполняется, и «НЕТ» — если не выполняется
a = int(input())
n1,n4 = (a%10000)//1000, a%10
n2,n3 = (a%1000)//100, (a%100)//10
print('ДА' if n1+n4==n2-n3 else "НЕТ")
#Наименьшее из двух чисел
a,b = int(input()),int(input())
if a<b:
   print(a)
else:
   print(b)

n = a if a<b else b
m = c if c<d else d
print(n if n<m else m)
#Принадлежность
print(" Принадлежит" if -1< int(input()) < 17 else "Не принадлежит")

print("Принадлежит" if a <= -3 or a >= 7 else "Не принадлежит")

if (1000 <= n <= 9999) and ( n%7 == 0 or n%17 == 0):
   print("YES")
else:
   print("NO")

if not (a%100 == 0) and a%4 == 0 or a%400 == 0:
  print ("YES")
else:
    print("NO")

#Ход ладьи
if 1 <= a == a1 <= 8 or 1 <= b == b1 <= 8:
   print("YES")
else:
   print("NO")
#step king
if -1 <= a1 - a <= 1 and -1 <= b1 - b <= 1:
    print("YES")
else:
    print("NO")
#Если Зум быстрее Флэша нужно вывести «NO», если Флэш быстрее Зума нужно вывести «YES», если их скорости равны нужно вывести "Don't know"
n,k = int(input()),int(input())
if n>k:
  print("NO")
elif n<k:
  print("YES")
else:
  print("Don't know")

a,b,c = int(input()),int(input()),int(input())
if a == b and b == c and a == c:
  print("Равносторонний")
elif a != b and a != c and b != c:
  print("Разносторонний")
elif a != b or c != a or b != c:
  print("Равнобедренный")

if a == "красный" and  b == "желтый" or a == "желтый" and  b == "красный":
 print("оранжевый")
elif a == "красный" and b == "синий" or a == "синий" and b == "красный":
 print("фиолетовый")
elif a == "синий" and b == "желтый" or a == "желтый" and b == "синий":
 print("зеленый")
elif a == b and (a == "красный" or a == "синий" or a == "желтый"):
  print(a)
else:
   print("ошибка цвета")















