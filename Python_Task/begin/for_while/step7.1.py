s=input()
for i in range(10):
    print(i, s)

s = int(input())+1
for i in range(s):
    print('Квадрат числа', i, 'равен', i*i)
#Даны два целых числа mm и nn ( m \le nm≤n). Напишите программу, которая выводит все числа от mm до nn включительно.
m,n = int(input()),int(input())
n1=n+1
for i in range(m,n1):
  print(i)
#Даны два целых числа mm и nn. Напишите программу, которая выводит все числа от mm до nn включительно в порядке возрастания, если m < nm<n, или в порядке убывания в противном случае.
m,n = int(input()),int(input())
if m<n:
  n1=n+1
  for i in range(m,n1,1):
    print(i)
elif m>n:
  n2=n-1
  for i in range(m,n2,-1):
    print(i)
elif m==n:
    print(m)
#Даны два натуральных числа mm и nn ( m \le nm≤n). Напишите программу, которая выводит все числа от mm до nn включительно удовлетворяющие хотя бы одному из условий:
m,n =int(input()),int(input())
for i in range(m,n+1):
    if i%15 == 0 or i%10==9 or i%17 ==0 or m==n:
        print(i)
#Дано натуральное число nn. Напишите программу, которая выводит таблицу умножения на nn.
n=int(input())
for i in range(1,10+1):
    print(n, "x",i, "=", n*i)
#На вход программе подается натуральное число nn. Напишите программу, которая вычисляет n!n!.
n=int(input())
tot=1
for i in range(2,n+1):
    tot*=i
print(tot)
#Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.
tot=1
for i in range(10):
  a = int(input())
  if a!= 0:
    tot=tot*a
print(tot)

















