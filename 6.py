#Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел
l = [x for x in range(1,101)]
o = sum(l) ** 2
print(o)

x = [i ** 2 for i in range(1,101)]
y = [i for i in range(1,101)]
print((sum(y) ** 2) - sum(x))