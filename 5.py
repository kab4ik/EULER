#Какое самое маленькое число делится нацело на все числа от 1 до 20?
x = 1
status = True
while status:
    z = []
    z = [i for i in range(1, 21) if x%i == 0]
    if len(z) == 20:
        print(x)
        status = False
    x+=1
