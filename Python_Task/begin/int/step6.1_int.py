a = 13
b = 7
total = a + b
diff = a - b
prod = a * b
div1 = a / b
div2 = a // b
mod = a % b
exp = a ** b
print(a, '+', b, '=', total)
print(a, '-', b, '=', diff)
print(a, '*', b, '=', prod)
print(a, '/', b, '=', div1)
print(a, '//', b, '=', div2)
print(a, '%', b, '=', mod)
print(a, '**', b, '=', exp)

a = max(3, 8, -3, 12, 9)
b = min(3, 8, -3, 12, 9)
c = max(3.14, 2.17, 9.8)
print(a)
print(b)
print(c)

n = int(input())
a,b,c = n%10, (n%100)//10, n//100
x = (a+b+c) - max(a,b,c) - min(a,b,c)
if max(a,b,c) - min(a,b,c) == x:
  print("Число интересное")
else:
  print("Число неинтересное")


