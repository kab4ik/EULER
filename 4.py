#Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
x = 999
y = 999
z = []
z1 = 0

while y > 100:
    c = x*y
    if str(c) == str(c)[::-1] and c > z1:
        z1 = c
        z.clear()
        z.append([x,y])
    else:
        x-=1
        if x == 100:
            y-=1
            x = 999
print(z, z1)