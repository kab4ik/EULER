#Существует только одна тройка Пифагора, для которой a + b + c = 1000. Найдите произведение abc

a = 1
b = 1
while True:
    c = a ** 2 + b ** 2
    if a + b + (c ** 0.5) == 1000 and a < b < c:
        print(a,b,int( c** 0.5))
    a += 1
    if a == 1000:
        a = 1
        b += 1
    if b == 1000:
        break