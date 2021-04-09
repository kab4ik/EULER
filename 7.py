#Какое число является 10001-м простым числом?
x = 0
n = 0
while n <= 10001:
    x += 1
    z = [i for i in range(1,x+1) if x%i == 0]
    if len(z) == 2:
        n += 1
print(x)